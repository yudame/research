#!/usr/bin/env python3
"""
Transcribe audio using local Whisper and output timestamped transcript.
No API key needed - runs entirely locally.

Usage:
    python transcribe_only.py /path/to/episode.mp3
"""

import argparse
import json
from pathlib import Path

import whisper


def transcribe_audio(audio_path: str, model_name: str = "base"):
    """Transcribe audio file using local Whisper."""
    print(f"Loading Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)

    print(f"Transcribing {audio_path}...")
    result = model.transcribe(audio_path, verbose=True)

    return result


def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper")
    parser.add_argument("audio_file", help="Path to the audio file")
    parser.add_argument(
        "--model",
        default="base",
        choices=["tiny", "base", "small", "medium"],
        help="Whisper model size (default: base)"
    )

    args = parser.parse_args()
    audio_path = Path(args.audio_file)

    if not audio_path.exists():
        print(f"Error: File not found: {audio_path}")
        return 1

    # Transcribe
    result = transcribe_audio(str(audio_path), args.model)

    # Save full result
    output_path = audio_path.parent / f"{audio_path.stem}_transcript.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\n✓ Transcript saved to: {output_path}")
    print(f"✓ Duration: {result['text'][:100]}...")

    return 0


if __name__ == "__main__":
    exit(main())
