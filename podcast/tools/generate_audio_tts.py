#!/usr/bin/env python3
"""
Yudame Research TTS Audio Generator

Generates podcast audio from script.md using Gemini TTS API.

Usage:
    python generate_audio_tts.py <episode_dir>
    python generate_audio_tts.py ../episodes/cardiovascular-health/ep5-diet/

Environment:
    GOOGLE_API_KEY - Required (stored in /Users/valorengels/.env, auto-loaded via ~/.zshenv)
"""

import os
import re
import sys
import wave
from pathlib import Path

from google import genai
from google.genai import types
from pydub import AudioSegment


# Configuration
TTS_MODEL = "gemini-2.5-flash-preview-tts"
VOICE = "Alnilam"
SAMPLE_RATE = 24000
CHANNELS = 1
SAMPLE_WIDTH = 2  # 16-bit
OUTPUT_BITRATE = "128k"


def generate_audio(client: genai.Client, script_text: str) -> bytes:
    """Generate audio for the full script using Gemini TTS."""

    response = client.models.generate_content(
        model=TTS_MODEL,
        contents=script_text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=VOICE
                    )
                )
            )
        )
    )

    return response.candidates[0].content.parts[0].inline_data.data


def pcm_to_wav(pcm_data: bytes, output_path: Path):
    """Convert raw PCM data to WAV file."""
    with wave.open(str(output_path), 'wb') as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(SAMPLE_WIDTH)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(pcm_data)


def strip_directives(script_text: str) -> str:
    """Remove TTS directives to create plain transcript."""
    # Remove directive blocks
    text = re.sub(r'\[(?:VOICE|PACE|PAUSE|EMPHASIS|TRANSITION):[^\]]+\]', '', script_text)
    # Remove markdown headers but keep the text
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)
    return text.strip()


def generate_episode(episode_dir: str, verbose: bool = True):
    """Generate complete podcast audio from script.md."""

    episode_path = Path(episode_dir).resolve()
    script_path = episode_path / "script.md"

    if not script_path.exists():
        print(f"Error: Missing script.md in {episode_path}")
        print("\nExpected file: script.md")
        print("Generate script.md first using the podcast-episode-planner skill.")
        return None

    if verbose:
        print(f"Generating audio for: {episode_path.name}")
        print("=" * 60)

    # Check API key
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not set")
        print("\nAPI keys should be in /Users/valorengels/.env")
        print("Add: GOOGLE_API_KEY=your_key_here")
        return None

    # Initialize client
    client = genai.Client(api_key=api_key)

    # Load script
    if verbose:
        print("\n[1/3] Loading script...")
    script_text = script_path.read_text()
    word_count = len(script_text.split())
    if verbose:
        print(f"  Words: {word_count} (~{word_count/150:.1f} min estimated)")

    # Validate word count
    if word_count < 3000:
        print(f"  Warning: Script seems short ({word_count} words, expected ~5,200)")
    elif word_count > 8000:
        print(f"  Warning: Script seems long ({word_count} words, expected ~5,200)")

    # Generate audio (single call)
    if verbose:
        print("\n[2/3] Generating audio...")
        print("  This may take 1-2 minutes...")

    try:
        audio_data = generate_audio(client, script_text)
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None

    # Save as WAV then convert to MP3
    tmp_dir = episode_path / "tmp"
    tmp_dir.mkdir(exist_ok=True)
    wav_path = tmp_dir / "full_audio.wav"
    pcm_to_wav(audio_data, wav_path)

    # Convert to MP3
    episode_slug = episode_path.name
    output_path = episode_path / f"{episode_slug}.mp3"

    audio = AudioSegment.from_wav(str(wav_path))
    audio.export(
        str(output_path),
        format="mp3",
        bitrate=OUTPUT_BITRATE,
        tags={
            "artist": "Yudame Research",
            "album": "Yudame Research Podcast",
        }
    )

    duration_seconds = len(audio) / 1000
    file_size_mb = output_path.stat().st_size / (1024 * 1024)

    if verbose:
        print(f"  Duration: {duration_seconds/60:.1f} minutes")
        print(f"  File size: {file_size_mb:.1f} MB")

    # Generate transcript
    if verbose:
        print("\n[3/3] Generating transcript...")
    transcript = strip_directives(script_text)
    transcript_path = episode_path / f"{episode_slug}_transcript.txt"
    transcript_path.write_text(transcript)
    if verbose:
        print(f"  Saved: {transcript_path.name}")

    # Cleanup
    wav_path.unlink()
    try:
        tmp_dir.rmdir()
    except OSError:
        pass  # Directory not empty, that's fine

    if verbose:
        print("\n" + "=" * 60)
        print("Audio generation complete!")
        print(f"Output: {output_path}")
        print(f"\nNext steps:")
        print("  1. Listen to the audio and verify quality")
        print("  2. Generate chapters from transcript")
        print("  3. Embed chapters into mp3")
        print("  4. Update feed.xml")

    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_audio_tts.py <episode_dir>")
        print("\nExample:")
        print("  python generate_audio_tts.py ../episodes/cardiovascular-health/ep5-diet/")
        sys.exit(1)

    episode_dir = sys.argv[1]
    verbose = "--quiet" not in sys.argv

    result = generate_episode(episode_dir, verbose=verbose)

    if result is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
