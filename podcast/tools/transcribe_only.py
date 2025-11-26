#!/usr/bin/env python3
"""
Transcribe audio using local Whisper or OpenAI's Whisper API.

Usage:
    python transcribe_only.py /path/to/episode.mp3
    python transcribe_only.py /path/to/episode.mp3 --use-api  # Use OpenAI API

Environment:
    OPENAI_API_KEY - Required only when using --use-api flag
    Can be set in .env file in repo root
"""

import argparse
import json
import os
from pathlib import Path

import whisper
from openai import OpenAI


def load_env():
    """Load environment variables from .env file."""
    env_path = Path(__file__).parent.parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip())


def transcribe_audio(audio_path: str, model_name: str = "base"):
    """Transcribe audio file using local Whisper."""
    print(f"Loading Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)

    print(f"Transcribing {audio_path}...")
    result = model.transcribe(audio_path, verbose=True)

    return result


def transcribe_audio_api(audio_path: str, model_name: str = "whisper-1"):
    """Transcribe audio file using OpenAI's Whisper API."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment or .env file")
        return None

    print(f"Transcribing {audio_path} using OpenAI API...")
    client = OpenAI(api_key=api_key)

    with open(audio_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model=model_name,
            file=audio_file,
            response_format="verbose_json",
            timestamp_granularities=["segment"],
        )

    result = {
        "text": response.text,
        "segments": [
            {"start": seg.start, "end": seg.end, "text": seg.text}
            for seg in response.segments
        ],
    }

    return result


def main():
    load_env()

    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper")
    parser.add_argument("audio_file", help="Path to the audio file")
    parser.add_argument(
        "--model",
        default="base",
        choices=["tiny", "base", "small", "medium"],
        help="Whisper model size for local transcription (default: base)",
    )
    parser.add_argument(
        "--use-api",
        action="store_true",
        help="Use OpenAI's Whisper API instead of local model (requires OPENAI_API_KEY)",
    )

    args = parser.parse_args()
    audio_path = Path(args.audio_file)

    if not audio_path.exists():
        print(f"Error: File not found: {audio_path}")
        return 1

    # Transcribe using API or local model
    if args.use_api:
        result = transcribe_audio_api(str(audio_path))
        if result is None:
            return 1
    else:
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
