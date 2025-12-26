#!/usr/bin/env python3
"""
Yudame Research Solo Podcast Generator

Generates a ~36-minute solo podcast episode using Gemini 2.5 Native Audio.
Creates audio in 3 sequential sections with transcript continuity.

Usage:
    python generate_audio.py <episode_dir>
    python generate_audio.py ../episodes/2025-12-23-topic-slug/
    python generate_audio.py ../episodes/cardiovascular-health/ep3-hrv/

Environment:
    GOOGLE_API_KEY - Required for Gemini API access

Prerequisites:
    - report.md in episode directory (structured with Episode Planning Framework)
    - ffmpeg installed for audio processing
    - Python dependencies: google-genai, pydub, numpy, openai-whisper
"""

import asyncio
import json
import os
import struct
import sys
import wave
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Lazy imports for heavy dependencies
genai = None
AudioSegment = None
whisper = None


def import_dependencies():
    """Lazily import heavy dependencies."""
    global genai, AudioSegment, whisper

    if genai is None:
        from google import genai as _genai
        genai = _genai

    if AudioSegment is None:
        from pydub import AudioSegment as _AudioSegment
        AudioSegment = _AudioSegment

    if whisper is None:
        import whisper as _whisper
        whisper = _whisper


# =============================================================================
# Configuration
# =============================================================================

@dataclass
class AudioConfig:
    """Audio generation configuration."""
    model: str = "gemini-2.5-flash-native-audio-latest"
    beat_sheet_model: str = "gemini-2.5-pro"
    voice: str = "Alnilam"
    temperature: float = 1.3
    sample_rate: int = 24000
    channels: int = 1
    sample_width: int = 2  # 16-bit
    output_bitrate: str = "128k"

    # Segment configuration
    target_duration_per_part: int = 720  # 12 minutes in seconds
    room_tone_duration: float = 0.5
    room_tone_amplitude: float = 0.001

    # Transcription
    whisper_model: str = "base"


@dataclass
class GenerationMetrics:
    """Metrics for tracking generation progress."""
    episode_slug: str
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None

    # Audio metrics
    part_durations: list = field(default_factory=list)
    total_duration_seconds: float = 0
    final_file_size_bytes: int = 0

    # Quality metrics
    retry_count: int = 0
    error_count: int = 0

    def to_dict(self) -> dict:
        return {
            "episode_slug": self.episode_slug,
            "duration_minutes": self.total_duration_seconds / 60,
            "file_size_mb": self.final_file_size_bytes / (1024 * 1024),
            "part_durations": self.part_durations,
            "processing_time_minutes": (
                (self.end_time - self.start_time).total_seconds() / 60
                if self.end_time else None
            ),
            "retries": self.retry_count,
            "errors": self.error_count
        }


# =============================================================================
# Beat Sheet Generator
# =============================================================================

async def generate_beat_sheet(
    client,
    report: str,
    config: AudioConfig,
    log_func=print
) -> dict:
    """Generate a structured beat sheet from research materials."""
    from prompts import BEAT_SHEET_SYSTEM_PROMPT

    log_func("[2/6] Generating beat sheet from report...")

    response = await client.aio.models.generate_content(
        model=config.beat_sheet_model,
        contents=[
            {"role": "user", "parts": [{"text": f"""
{BEAT_SHEET_SYSTEM_PROMPT}

Here is the research report to create a beat sheet for:

{report}

Output the beat sheet as valid JSON.
"""}]}
        ],
        config={
            "temperature": 0.7,
            "response_mime_type": "application/json"
        }
    )

    beat_sheet = json.loads(response.text)
    log_func(f"  Generated {len(beat_sheet.get('parts', []))} parts with "
             f"{sum(len(p.get('beats', [])) for p in beat_sheet.get('parts', []))} beats")

    return beat_sheet


# =============================================================================
# Audio Generation via Live API
# =============================================================================

async def generate_audio_segment(
    client,
    prompt: str,
    config: AudioConfig,
    log_func=print
) -> bytes:
    """Generate audio for a single segment using the Live API."""
    from google.genai import types

    live_config = types.LiveConnectConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=config.voice
                )
            )
        ),
        temperature=config.temperature,
    )

    audio_chunks = []

    try:
        async with client.aio.live.connect(
            model=config.model,
            config=live_config
        ) as session:
            # Send the prompt using the newer API
            await session.send_client_content(
                turns=[{"role": "user", "parts": [{"text": prompt}]}],
                turn_complete=True
            )

            # Collect audio response
            async for response in session.receive():
                if response.data:
                    audio_chunks.append(response.data)

                # Check for turn completion
                if response.server_content and response.server_content.turn_complete:
                    break

    except Exception as e:
        log_func(f"  Error in audio generation: {e}")
        raise

    # Concatenate all audio chunks
    full_audio = b"".join(audio_chunks)
    duration = len(full_audio) / (config.sample_rate * config.sample_width * config.channels)
    log_func(f"    Generated {duration:.1f}s of audio")

    return full_audio


async def generate_part_audio_context_rich(
    client,
    part_number: int,
    source_material: str,
    previous_transcripts: list[str],
    config: AudioConfig,
    log_func=print
) -> bytes:
    """Generate audio using NotebookLM-style context-rich approach."""
    from prompts import (
        CONTEXT_RICH_GENERATION_PROMPT,
        PART_FOCUS,
        STRUCTURE_GUIDANCE,
    )

    # Build the full prompt with all context
    part_specific = ""
    if part_number == 1:
        part_specific = "Start with: 'Welcome to Yudame Research...'"
    elif part_number == 3:
        part_specific = "End with: '...find the full research at research dot yuda dot me - that's Y-U-D-A dot M-E. Until next time.'"

    prompt = CONTEXT_RICH_GENERATION_PROMPT.format(
        part_number=part_number,
        part_focus=PART_FOCUS[part_number],
        structure_guidance=STRUCTURE_GUIDANCE[part_number],
        source_material=source_material,
        previous_transcripts="\n\n".join(previous_transcripts) if previous_transcripts else "(This is Part 1 - no previous content)",
        part_specific_instructions=part_specific
    )

    log_func(f"    Prompt size: {len(prompt):,} chars")

    return await generate_audio_segment(client, prompt, config, log_func)


async def generate_part_audio(
    client,
    part: dict,
    beat_sheet: dict,
    previous_transcripts: list[str],
    config: AudioConfig,
    log_func=print
) -> bytes:
    """Generate audio for an entire part (multiple beats). [Legacy - beat sheet based]"""
    from prompts import (
        GENERATION_SYSTEM_PROMPT,
        PART_1_CONTINUATION,
        PART_2_CONTINUATION,
        PART_3_CONTINUATION
    )

    part_num = part["part_number"]

    # Build context from beat sheet
    beats_text = []
    for beat in part["beats"]:
        beat_text = f"""
### Beat {beat['beat_number']}: {beat['title']}
**Vocal Direction:** {beat.get('vocal_direction', 'Confident')}
**Key Message:** {beat['key_message']}
**Script Hook:** {beat.get('script_hook', '')}
**Key Points:**
{chr(10).join(f'- {p}' for p in beat.get('key_points', []))}
"""
        if beat.get('evidence'):
            beat_text += "\n**Evidence:**\n"
            for ev in beat['evidence']:
                beat_text += f"- {ev.get('source', 'Source')}: {ev.get('finding', '')}\n"

        if beat.get('self_interrogation'):
            beat_text += f"\n**Self-Interrogation Point:** {beat['self_interrogation']}\n"

        beats_text.append(beat_text)

    # Select continuation prompt based on part
    if part_num == 1:
        continuation = PART_1_CONTINUATION
    elif part_num == 2:
        continuation = PART_2_CONTINUATION.format(
            part_1_transcript=previous_transcripts[0] if previous_transcripts else ""
        )
    else:
        continuation = PART_3_CONTINUATION.format(
            previous_transcripts="\n\n---\n\n".join(previous_transcripts)
        )

    # Build full prompt
    prompt = f"""
{GENERATION_SYSTEM_PROMPT}

---

{continuation}

---

## Episode Information

**Title:** {beat_sheet.get('episode', {}).get('title', 'Yudame Research Episode')}
**Topic:** {beat_sheet.get('episode', {}).get('topic', '')}

## Narrative Arc

**Hook:** {beat_sheet.get('narrative_arc', {}).get('hook', '')}
**Stakes:** {beat_sheet.get('narrative_arc', {}).get('stakes', '')}
**Promise:** {beat_sheet.get('narrative_arc', {}).get('promise', '')}

## Part {part_num}: {part['title']} ({part['start_time']} - {part['end_time']})

Speak naturally through these beats, maintaining the Yudame Research voice identity.
Target duration: approximately {config.target_duration_per_part // 60} minutes.

{''.join(beats_text)}

## Key Takeaways (for Part 3 closing)
{json.dumps(beat_sheet.get('takeaways', []), indent=2) if part_num == 3 else 'N/A'}

## Branded Elements
{json.dumps(beat_sheet.get('branded_elements', {}), indent=2) if part_num in [1, 3] else 'N/A'}

Remember:
- Natural pauses indicated by ... and [pause]
- Self-interrogation at marked beats
- Define technical terms on first use
- Vary vocal dynamics based on the vocal direction for each beat
- {
    'Open with branded greeting' if part_num == 1 else
    'Continue naturally from Part ' + str(part_num - 1) if part_num == 2 else
    'Close with branded sign-off and URL'
}
"""

    return await generate_audio_segment(client, prompt, config, log_func)


# =============================================================================
# Transcription
# =============================================================================

def transcribe_audio(audio_path: Path, config: AudioConfig, log_func=print) -> str:
    """Transcribe audio file using local Whisper."""
    log_func(f"  Transcribing {audio_path.name}...")

    model = whisper.load_model(config.whisper_model)
    result = model.transcribe(str(audio_path), verbose=False)

    transcript = result["text"]
    word_count = len(transcript.split())
    log_func(f"    Transcribed {word_count} words")

    return transcript


# =============================================================================
# Audio Processing
# =============================================================================

def pcm_to_wav(pcm_data: bytes, config: AudioConfig, output_path: Path):
    """Convert raw PCM data to WAV file."""
    with wave.open(str(output_path), 'wb') as wav_file:
        wav_file.setnchannels(config.channels)
        wav_file.setsampwidth(config.sample_width)
        wav_file.setframerate(config.sample_rate)
        wav_file.writeframes(pcm_data)


def generate_room_tone(config: AudioConfig) -> bytes:
    """Generate subtle room tone (white noise) for segment transitions."""
    num_samples = int(config.sample_rate * config.room_tone_duration)
    noise = np.random.normal(0, config.room_tone_amplitude, num_samples)
    noise = np.clip(noise, -1, 1)

    # Convert to 16-bit PCM
    pcm_data = (noise * 32767).astype(np.int16)
    return pcm_data.tobytes()


def stitch_segments(
    segment_paths: list[Path],
    output_path: Path,
    config: AudioConfig,
    log_func=print
) -> tuple[float, int]:
    """Stitch audio segments together with room tone transitions."""
    log_func("[5/6] Stitching segments...")

    # Load all segments
    segments = []
    for path in segment_paths:
        segment = AudioSegment.from_wav(str(path))
        segments.append(segment)
        log_func(f"  Loaded {path.name}: {len(segment) / 1000:.1f}s")

    # Generate room tone as AudioSegment
    room_tone_pcm = generate_room_tone(config)
    room_tone_path = segment_paths[0].parent / "room_tone.wav"
    pcm_to_wav(room_tone_pcm, config, room_tone_path)
    room_tone = AudioSegment.from_wav(str(room_tone_path))

    # Stitch together
    final = segments[0]
    for segment in segments[1:]:
        final = final + room_tone + segment

    # Export as MP3
    final.export(
        str(output_path),
        format="mp3",
        bitrate=config.output_bitrate,
        tags={
            "artist": "Yudame Research",
            "album": "Yudame Research Podcast",
        }
    )

    # Cleanup temp files
    room_tone_path.unlink()

    duration_seconds = len(final) / 1000
    file_size_bytes = output_path.stat().st_size

    log_func(f"  Final audio: {output_path.name}")
    log_func(f"  Duration: {duration_seconds / 60:.1f} minutes")
    log_func(f"  File size: {file_size_bytes / (1024 * 1024):.1f} MB")

    return duration_seconds, file_size_bytes


def combine_transcripts(transcripts: list[str], output_path: Path, log_func=print):
    """Combine part transcripts into final transcript file."""
    log_func("[6/6] Creating transcript...")

    full_transcript = "\n\n---\n\n".join([
        f"[Part {i + 1}]\n\n{t}" for i, t in enumerate(transcripts)
    ])

    output_path.write_text(full_transcript)

    word_count = len(full_transcript.split())
    log_func(f"  Saved transcript: {output_path.name} ({word_count} words)")


# =============================================================================
# Main Pipeline
# =============================================================================

async def generate_episode_context_rich(episode_dir: str, verbose: bool = True, include_extra_research: bool = False):
    """Generate a podcast episode using NotebookLM-style context-rich approach.

    Loads 4 critical input files as rich context:
    - report.md (synthesized research report)
    - sources.md (validated citations)
    - research/p1-brief.md (Phase 1 academic briefing)
    - research/p3-briefing.md (Phase 3 policy/industry research)

    Args:
        episode_dir: Path to episode directory
        verbose: Print progress messages
        include_extra_research: If True, also load individual p2-*.md files (increases context size)
    """
    import_dependencies()

    episode_path = Path(episode_dir).resolve()
    config = AudioConfig()
    metrics = GenerationMetrics(episode_slug=episode_path.name)

    def log(msg):
        if verbose:
            print(msg)

    log(f"\n{'=' * 60}")
    log(f"Generating podcast (context-rich mode): {episode_path.name}")
    log(f"{'=' * 60}")

    # Initialize client
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        log("Error: GOOGLE_API_KEY environment variable not set")
        return None

    client = genai.Client(api_key=api_key)

    # 1. Load 4 CRITICAL input files
    log("\n[1/5] Loading research materials...")
    log("  Checking for 4 critical input files:")

    source_material_parts = []
    total_bytes = 0

    # Critical file 1: report.md (required)
    report_path = episode_path / "report.md"
    if not report_path.exists():
        log(f"  ERROR: Missing report.md in {episode_path}")
        return None
    report = report_path.read_text()
    source_material_parts.append(f"# MAIN RESEARCH REPORT\n\n{report}")
    log(f"  ✓ report.md ({len(report):,} chars, {len(report)//1024}KB)")
    total_bytes += len(report)

    # Critical file 2: sources.md (recommended)
    sources_path = episode_path / "sources.md"
    if sources_path.exists():
        sources = sources_path.read_text()
        source_material_parts.append(f"# VALIDATED SOURCES AND CITATIONS\n\n{sources}")
        log(f"  ✓ sources.md ({len(sources):,} chars, {len(sources)//1024}KB)")
        total_bytes += len(sources)
    else:
        log(f"  - sources.md not found (optional but recommended)")

    # Critical file 3: research/p1-brief.md (Phase 1 academic)
    p1_path = episode_path / "research" / "p1-brief.md"
    if p1_path.exists():
        p1 = p1_path.read_text()
        source_material_parts.append(f"# PHASE 1: ACADEMIC RESEARCH BRIEFING\n\n{p1}")
        log(f"  ✓ research/p1-brief.md ({len(p1):,} chars, {len(p1)//1024}KB)")
        total_bytes += len(p1)
    else:
        log(f"  - research/p1-brief.md not found (optional)")

    # Critical file 4: research/p3-briefing.md (Phase 3 policy/industry)
    p3_path = episode_path / "research" / "p3-briefing.md"
    if p3_path.exists():
        p3 = p3_path.read_text()
        source_material_parts.append(f"# PHASE 3: POLICY AND INDUSTRY RESEARCH\n\n{p3}")
        log(f"  ✓ research/p3-briefing.md ({len(p3):,} chars, {len(p3)//1024}KB)")
        total_bytes += len(p3)
    else:
        log(f"  - research/p3-briefing.md not found (optional)")

    # Load any additional research files (excluding p1 and p3 which we already loaded)
    research_dir = episode_path / "research"
    if research_dir.exists():
        loaded_files = {"p1-brief.md", "p3-briefing.md"}  # Already loaded
        additional_files = [f for f in sorted(research_dir.glob("*.md"))
                          if f.name not in loaded_files]
        if additional_files:
            log(f"\n  Loading {len(additional_files)} additional research files:")
            for research_file in additional_files:
                content = research_file.read_text()
                source_material_parts.append(f"# {research_file.stem.upper()}\n\n{content}")
                log(f"    + {research_file.name} ({len(content):,} chars, {len(content)//1024}KB)")
                total_bytes += len(content)

    source_material = "\n\n---\n\n".join(source_material_parts)
    total_words = len(source_material.split())
    log(f"\n  TOTAL CONTEXT: {len(source_material):,} chars ({total_bytes//1024}KB), {total_words:,} words")

    # Warn if context seems too small
    if total_bytes < 50000:  # Less than 50KB
        log(f"  WARNING: Context is small ({total_bytes//1024}KB). Audio may be shorter than target.")
        log(f"    Recommended: 80-150KB of source material for 36-minute episode")

    # 2. Create output directories
    tmp_dir = episode_path / "tmp"
    tmp_dir.mkdir(exist_ok=True)

    # 3. Generate audio segments with full context
    log("\n[2/5] Generating audio segments (context-rich mode)...")

    segment_paths = []
    transcripts = []

    for part_num in [1, 2, 3]:
        part_names = {1: "Foundation", 2: "Evidence", 3: "Application"}
        log(f"\n  Part {part_num}: {part_names[part_num]}")

        try:
            audio_data = await generate_part_audio_context_rich(
                client=client,
                part_number=part_num,
                source_material=source_material,
                previous_transcripts=transcripts,
                config=config,
                log_func=log
            )
        except Exception as e:
            log(f"  Error generating Part {part_num}: {e}")
            metrics.error_count += 1
            continue

        # Save segment as WAV
        segment_path = tmp_dir / f"part_{part_num}.wav"
        pcm_to_wav(audio_data, config, segment_path)
        segment_paths.append(segment_path)

        # Calculate duration
        duration = len(audio_data) / (config.sample_rate * config.sample_width * config.channels)
        metrics.part_durations.append(duration)
        log(f"    Saved: {segment_path.name} ({duration:.1f}s = {duration/60:.1f} min)")

        # Transcribe for continuity
        log(f"\n[3/5] Transcribing Part {part_num} for continuity...")
        transcript = transcribe_audio(segment_path, config, log)
        transcripts.append(transcript)
        log(f"    Words: {len(transcript.split())}")

        # Save individual transcript
        transcript_path = tmp_dir / f"part_{part_num}_transcript.txt"
        transcript_path.write_text(transcript)

    # 4. Stitch segments
    if segment_paths:
        episode_slug = episode_path.name
        output_mp3 = episode_path / f"{episode_slug}.mp3"
        output_transcript = episode_path / "transcript.txt"

        duration, file_size = stitch_segments(segment_paths, output_mp3, config, log)
        metrics.total_duration_seconds = duration
        metrics.final_file_size_bytes = file_size

        # 5. Combine transcripts
        combine_transcripts(transcripts, output_transcript, log)

        # Save metrics
        metrics.end_time = datetime.now()
        metrics_path = tmp_dir / "generation_metrics.json"
        metrics_path.write_text(json.dumps(metrics.to_dict(), indent=2))

        log(f"\n{'=' * 60}")
        log("Episode generation complete!")
        log(f"Audio: {output_mp3}")
        log(f"Transcript: {output_transcript}")
        log(f"Processing time: {(metrics.end_time - metrics.start_time).total_seconds() / 60:.1f} minutes")
        log(f"{'=' * 60}")

        return output_mp3

    return None


async def generate_episode(episode_dir: str, verbose: bool = True):
    """Generate a complete podcast episode."""
    import_dependencies()

    episode_path = Path(episode_dir).resolve()
    config = AudioConfig()
    metrics = GenerationMetrics(episode_slug=episode_path.name)

    def log(msg):
        if verbose:
            print(msg)

    log(f"\n{'=' * 60}")
    log(f"Generating podcast for: {episode_path.name}")
    log(f"{'=' * 60}")

    # Initialize client
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        log("Error: GOOGLE_API_KEY environment variable not set")
        return None

    client = genai.Client(api_key=api_key)

    # 1. Load research materials
    log("\n[1/6] Loading research materials...")

    report_path = episode_path / "report.md"
    if not report_path.exists():
        log(f"Error: Missing report.md in {episode_path}")
        return None

    report = report_path.read_text()
    log(f"  Loaded report.md ({len(report):,} chars)")

    # 2. Generate beat sheet
    beat_sheet = await generate_beat_sheet(client, report, config, log)

    # Save beat sheet for reference
    tmp_dir = episode_path / "tmp"
    tmp_dir.mkdir(exist_ok=True)
    beat_sheet_path = tmp_dir / "beat_sheet.json"
    beat_sheet_path.write_text(json.dumps(beat_sheet, indent=2))
    log(f"  Saved beat sheet to {beat_sheet_path.name}")

    # 3. Generate audio segments sequentially
    log("\n[3/6] Generating audio segments...")

    segment_paths = []
    transcripts = []

    for part in beat_sheet.get("parts", []):
        part_num = part["part_number"]
        log(f"\n  Part {part_num}: {part['title']} ({part['start_time']} - {part['end_time']})")

        # Generate audio for this part
        try:
            audio_data = await generate_part_audio(
                client=client,
                part=part,
                beat_sheet=beat_sheet,
                previous_transcripts=transcripts,
                config=config,
                log_func=log
            )
        except Exception as e:
            log(f"  Error generating Part {part_num}: {e}")
            metrics.error_count += 1
            continue

        # Save segment as WAV
        segment_path = tmp_dir / f"part_{part_num}.wav"
        pcm_to_wav(audio_data, config, segment_path)
        segment_paths.append(segment_path)

        # Calculate duration
        duration = len(audio_data) / (config.sample_rate * config.sample_width * config.channels)
        metrics.part_durations.append(duration)
        log(f"    Saved: {segment_path.name} ({duration:.1f}s)")

        # Transcribe this part for continuity
        log(f"\n[4/6] Transcribing Part {part_num} for continuity...")
        transcript = transcribe_audio(segment_path, config, log)
        transcripts.append(transcript)

        # Save individual transcript
        transcript_path = tmp_dir / f"part_{part_num}_transcript.txt"
        transcript_path.write_text(transcript)

    # 5. Stitch segments
    if len(segment_paths) < len(beat_sheet.get("parts", [])):
        log(f"\nWarning: Only {len(segment_paths)} of {len(beat_sheet.get('parts', []))} parts generated")

    if segment_paths:
        episode_slug = episode_path.name
        output_mp3 = episode_path / f"{episode_slug}.mp3"
        output_transcript = episode_path / "transcript.txt"

        duration, file_size = stitch_segments(segment_paths, output_mp3, config, log)
        metrics.total_duration_seconds = duration
        metrics.final_file_size_bytes = file_size

        # 6. Combine transcripts
        combine_transcripts(transcripts, output_transcript, log)

        # Save metrics
        metrics.end_time = datetime.now()
        metrics_path = tmp_dir / "generation_metrics.json"
        metrics_path.write_text(json.dumps(metrics.to_dict(), indent=2))

        log(f"\n{'=' * 60}")
        log("Episode generation complete!")
        log(f"Audio: {output_mp3}")
        log(f"Transcript: {output_transcript}")
        log(f"Processing time: {(metrics.end_time - metrics.start_time).total_seconds() / 60:.1f} minutes")
        log(f"{'=' * 60}")

        return output_mp3

    return None


# =============================================================================
# CLI Entry Point
# =============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate podcast audio using Gemini 2.5 Native Audio",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python generate_audio.py ../episodes/cardiovascular-health/ep3-hrv/
    python generate_audio.py ../episodes/cardiovascular-health/ep3-hrv/ --context-rich

Modes:
    Default (beat-sheet): Generates beat sheet first, then audio from structure
    --context-rich: NotebookLM-style - loads ALL source material into context
                    for richer, more detailed audio output (recommended)

Prerequisites:
    - report.md in episode directory
    - GOOGLE_API_KEY environment variable set
    - For context-rich mode: research/*.md files provide additional context

Output:
    - <episode-slug>.mp3 - Final audio file with 3 stitched parts
    - transcript.txt - Combined transcript of all parts
    - tmp/part_X.wav - Individual part audio files
    - tmp/part_X_transcript.txt - Individual part transcripts
        """
    )

    parser.add_argument(
        "episode_dir",
        help="Path to the episode directory containing report.md"
    )
    parser.add_argument(
        "--context-rich", "-c",
        action="store_true",
        help="Use NotebookLM-style context-rich generation (recommended for longer output)"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Minimal output (suppress progress messages)"
    )

    args = parser.parse_args()

    if not os.environ.get("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set")
        print("Get your API key at: https://aistudio.google.com/app/apikey")
        sys.exit(1)

    if args.context_rich:
        result = asyncio.run(generate_episode_context_rich(args.episode_dir, verbose=not args.quiet))
    else:
        result = asyncio.run(generate_episode(args.episode_dir, verbose=not args.quiet))

    if result is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
