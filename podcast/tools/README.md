# Podcast Tools

## generate_chapters.py

Automatically generates chapter markers for podcast episodes using local Whisper transcription and Claude for topic detection.

### Setup

```bash
# Fix pyenv SSL issue first, or use system Python
pip install -r requirements.txt

# Ensure ANTHROPIC_API_KEY is set
export ANTHROPIC_API_KEY=your-key-here
```

### Usage

```bash
# Basic usage (uses 'base' Whisper model)
python generate_chapters.py /path/to/episode.mp3

# Use smaller/faster model
python generate_chapters.py --model tiny /path/to/episode.mp3

# Use larger/more accurate model (slower, needs more RAM)
python generate_chapters.py --model small /path/to/episode.mp3
```

### Output

The script generates two files in the same directory as the input:

1. `episode_chapters.txt` - FFmpeg metadata format
2. `episode_chapters.json` - Podcasting 2.0 format

### Embedding Chapters

After generating, embed into the MP3:

```bash
ffmpeg -i episode.mp3 -i episode_chapters.txt -map_metadata 1 -codec copy episode_with_chapters.mp3
```

### Whisper Model Sizes

| Model  | RAM   | Speed   | Accuracy |
|--------|-------|---------|----------|
| tiny   | ~1 GB | Fastest | Basic    |
| base   | ~1 GB | Fast    | Good     |
| small  | ~2 GB | Medium  | Better   |
| medium | ~5 GB | Slow    | Best     |

For 16 GB RAM, `base` or `small` are recommended.
