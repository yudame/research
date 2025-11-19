#!/usr/bin/env python3
"""
Generate podcast chapters from an MP3 file.

Uses local Whisper for transcription and Claude for topic segmentation.
Outputs an FFmpeg-compatible chapters file.

Usage:
    python generate_chapters.py /path/to/episode.mp3

Requirements:
    pip install openai-whisper anthropic

Environment:
    ANTHROPIC_API_KEY must be set
"""

import argparse
import json
import os
import sys
from pathlib import Path

import whisper
import anthropic


def transcribe_audio(audio_path: str, model_name: str = "base") -> list[dict]:
    """
    Transcribe audio file using local Whisper.
    
    Returns list of segments with start, end, and text.
    """
    print(f"Loading Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)
    
    print(f"Transcribing {audio_path}...")
    result = model.transcribe(audio_path, verbose=False)
    
    return result["segments"]


def chunk_segments(segments: list[dict], chunk_duration: float = 120.0) -> list[dict]:
    """
    Group segments into chunks of approximately chunk_duration seconds.
    
    Returns list of chunks with start, end, and combined text.
    """
    chunks = []
    current_chunk = {
        "start": segments[0]["start"],
        "end": segments[0]["end"],
        "text": segments[0]["text"]
    }
    
    for segment in segments[1:]:
        # If adding this segment would exceed chunk duration, finalize current chunk
        if segment["end"] - current_chunk["start"] > chunk_duration:
            chunks.append(current_chunk)
            current_chunk = {
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            }
        else:
            current_chunk["end"] = segment["end"]
            current_chunk["text"] += " " + segment["text"]
    
    # Don't forget the last chunk
    chunks.append(current_chunk)
    
    return chunks


def generate_chapter_titles(chunks: list[dict], client: anthropic.Anthropic) -> list[dict]:
    """
    Use Claude to generate chapter titles for each chunk.
    
    Returns chunks with added 'title' field.
    """
    print("Generating chapter titles with Claude...")
    
    # Build the prompt with all chunks
    chunks_text = ""
    for i, chunk in enumerate(chunks):
        start_time = format_timestamp(chunk["start"])
        chunks_text += f"\n--- Chunk {i+1} (starts at {start_time}) ---\n{chunk['text']}\n"
    
    prompt = f"""Analyze this podcast transcript and generate chapter titles.

The transcript is divided into chunks of approximately 2 minutes each. For each chunk, provide a concise chapter title (3-6 words) that captures the main topic being discussed.

If adjacent chunks discuss the same topic, you can merge them into a single chapter. If a chunk contains multiple distinct topics, note the more prominent one.

{chunks_text}

Respond with a JSON array of chapters. Each chapter should have:
- "start_chunk": the first chunk number (1-indexed)
- "end_chunk": the last chunk number (1-indexed) 
- "title": the chapter title (3-6 words)

Example response:
[
  {{"start_chunk": 1, "end_chunk": 2, "title": "Introduction and Overview"}},
  {{"start_chunk": 3, "end_chunk": 5, "title": "Technical Deep Dive"}},
  {{"start_chunk": 6, "end_chunk": 6, "title": "Practical Applications"}}
]

Return only the JSON array, no other text."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Parse the response
    response_text = response.content[0].text.strip()
    
    # Handle potential markdown code blocks
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
        response_text = response_text.strip()
    
    chapter_definitions = json.loads(response_text)
    
    # Convert chunk-based chapters to time-based chapters
    chapters = []
    for chapter_def in chapter_definitions:
        start_chunk_idx = chapter_def["start_chunk"] - 1  # Convert to 0-indexed
        end_chunk_idx = chapter_def["end_chunk"] - 1
        
        chapters.append({
            "start": chunks[start_chunk_idx]["start"],
            "end": chunks[end_chunk_idx]["end"],
            "title": chapter_def["title"]
        })
    
    return chapters


def format_timestamp(seconds: float) -> str:
    """Format seconds as HH:MM:SS or MM:SS."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def generate_ffmpeg_chapters(chapters: list[dict], output_path: str):
    """
    Generate FFmpeg-compatible chapters metadata file.
    """
    with open(output_path, "w") as f:
        f.write(";FFMETADATA1\n")
        
        for chapter in chapters:
            # FFmpeg uses milliseconds
            start_ms = int(chapter["start"] * 1000)
            end_ms = int(chapter["end"] * 1000)
            
            f.write("\n[CHAPTER]\n")
            f.write("TIMEBASE=1/1000\n")
            f.write(f"START={start_ms}\n")
            f.write(f"END={end_ms}\n")
            f.write(f"title={chapter['title']}\n")
    
    print(f"Chapters written to {output_path}")


def generate_chapters_json(chapters: list[dict], output_path: str):
    """
    Generate Podcasting 2.0 compatible chapters JSON file.
    """
    pc2_chapters = {
        "version": "1.2.0",
        "chapters": [
            {
                "startTime": chapter["start"],
                "title": chapter["title"]
            }
            for chapter in chapters
        ]
    }
    
    with open(output_path, "w") as f:
        json.dump(pc2_chapters, f, indent=2)
    
    print(f"Podcasting 2.0 chapters written to {output_path}")


def print_chapters_summary(chapters: list[dict]):
    """Print a human-readable summary of chapters."""
    print("\n" + "=" * 50)
    print("CHAPTER SUMMARY")
    print("=" * 50)
    
    for i, chapter in enumerate(chapters, 1):
        timestamp = format_timestamp(chapter["start"])
        print(f"{timestamp}  {chapter['title']}")
    
    print("=" * 50 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate podcast chapters from an MP3 file"
    )
    parser.add_argument("audio_file", help="Path to the MP3 file")
    parser.add_argument(
        "--model", 
        default="base",
        choices=["tiny", "base", "small", "medium"],
        help="Whisper model size (default: base)"
    )
    parser.add_argument(
        "--chunk-duration",
        type=float,
        default=120.0,
        help="Target duration for transcript chunks in seconds (default: 120)"
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory for chapter files (default: same as audio file)"
    )
    
    args = parser.parse_args()
    
    # Validate input file
    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        print(f"Error: File not found: {audio_path}")
        sys.exit(1)
    
    # Set output directory
    output_dir = Path(args.output_dir) if args.output_dir else audio_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
    
    # Initialize Anthropic client
    client = anthropic.Anthropic()
    
    # Step 1: Transcribe
    segments = transcribe_audio(str(audio_path), args.model)
    print(f"Transcribed {len(segments)} segments")
    
    # Step 2: Chunk segments
    chunks = chunk_segments(segments, args.chunk_duration)
    print(f"Created {len(chunks)} chunks")
    
    # Step 3: Generate chapter titles
    chapters = generate_chapter_titles(chunks, client)
    print(f"Generated {len(chapters)} chapters")
    
    # Step 4: Output files
    base_name = audio_path.stem
    
    # FFmpeg chapters file
    ffmpeg_path = output_dir / f"{base_name}_chapters.txt"
    generate_ffmpeg_chapters(chapters, str(ffmpeg_path))
    
    # Podcasting 2.0 JSON
    json_path = output_dir / f"{base_name}_chapters.json"
    generate_chapters_json(chapters, str(json_path))
    
    # Print summary
    print_chapters_summary(chapters)
    
    # Print next steps
    print("To embed chapters in the MP3:")
    print(f"  ffmpeg -i \"{audio_path}\" -i \"{ffmpeg_path}\" -map_metadata 1 -codec copy \"{audio_path.stem}_with_chapters.mp3\"")


if __name__ == "__main__":
    main()
