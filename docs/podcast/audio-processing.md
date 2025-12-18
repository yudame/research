# Audio Processing

This document describes the audio processing pipeline for converting source audio into podcast-ready MP3 files with transcription and chapters.

## Overview

The audio pipeline processes source files (typically M4A from NotebookLM) through four stages:

1. **Conversion** - M4A to MP3 at 128kbps
2. **Transcription** - Speech-to-text via local Whisper
3. **Chapter Generation** - AI analysis of transcript
4. **Embedding** - Insert chapters into MP3 metadata

---

## Audio Specifications

### Target Format

| Property | Value |
|----------|-------|
| Format | MP3 |
| Bitrate | 128 kbps |
| Sample Rate | 44.1 kHz |
| Channels | Stereo or Mono |

### File Size Guidelines

| Bitrate | Size per Hour |
|---------|---------------|
| 64 kbps | ~29 MB |
| 96 kbps | ~43 MB |
| 128 kbps | ~58 MB |

**Target:** 30-40 minute episodes at 128kbps = ~30-40 MB

### Duration Guidelines

- Target episode length: 30-40 minutes
- Maximum recommended: 60 minutes
- Minimum for chapters: 10 minutes

---

## Stage 1: Audio Conversion

Convert source audio to podcast-standard MP3.

### Input

- Source file format: M4A (from NotebookLM) or other audio formats
- Source location: User-provided file path

### Process

FFmpeg converts the source to 128kbps MP3:
- Audio codec: libmp3lame
- Bitrate: 128k (constant)
- Overwrite output if exists

### Output

- File: `YYYY-MM-DD-slug.mp3`
- Location: Episode directory

### Metadata Collection

After conversion, collect:
- **File size in bytes** - Used in RSS feed `<enclosure length="">`
- **Duration** - Used in RSS feed `<itunes:duration>`

---

## Stage 2: Transcription

Generate text transcript from audio using local Whisper.

### Whisper Model Options

| Model | Speed | Quality | Use Case |
|-------|-------|---------|----------|
| tiny | ~1-2 min | Basic | Quick drafts |
| base | ~5-10 min | Good | **Recommended** |
| small | ~15-20 min | Better | Quality-focused |
| medium | ~30-40 min | Best | Critical content |

Times are approximate for 30-minute audio.

### Process

Local Whisper processes the MP3:
- No API costs (runs entirely on local machine)
- Full privacy (audio never leaves machine)
- Outputs word-level timestamps

### Output Format

JSON transcript file containing:

```json
{
  "text": "Full transcript text...",
  "segments": [
    {
      "id": 0,
      "start": 0.0,
      "end": 5.2,
      "text": "Segment text...",
      "words": [
        {"word": "Hello", "start": 0.0, "end": 0.5},
        {"word": "world", "start": 0.6, "end": 1.0}
      ]
    }
  ],
  "language": "en"
}
```

### Output File

- File: `YYYY-MM-DD-slug_transcript.json`
- Size: ~400KB for 30-40 minute episode
- Location: Episode directory (or `tmp/` to reduce git size)

---

## Stage 3: Chapter Generation

Analyze transcript to create logical chapter divisions.

### Chapter Guidelines

| Property | Guideline |
|----------|-----------|
| Count | 10-15 chapters per episode |
| Length | 2-4 minutes each |
| Transitions | Natural topic changes |
| Titles | Clear, descriptive |

### Process

Claude analyzes the full transcript:
1. Identifies natural topic transitions
2. Creates chapter boundaries
3. Generates descriptive titles
4. Ensures logical flow

### Output Formats

Two chapter formats are generated for maximum compatibility:

**Format 1: FFmpeg Metadata**

File: `YYYY-MM-DD-slug_chapters.txt`

```
;FFMETADATA1
[CHAPTER]
TIMEBASE=1/1000
START=0
END=120000
title=Introduction

[CHAPTER]
TIMEBASE=1/1000
START=120000
END=240000
title=Understanding the Basics
```

- TIMEBASE: 1/1000 (milliseconds)
- START/END: Times in milliseconds
- title: Chapter title

**Format 2: Podcasting 2.0**

File: `YYYY-MM-DD-slug_chapters.json`

```json
{
  "version": "1.2.0",
  "chapters": [
    {
      "startTime": 0,
      "title": "Introduction"
    },
    {
      "startTime": 120,
      "title": "Understanding the Basics"
    }
  ]
}
```

- startTime: Seconds from beginning
- version: Podcasting 2.0 chapters spec version

---

## Stage 4: Chapter Embedding

Insert chapter metadata directly into MP3 file.

### Process

FFmpeg embeds the FFmpeg-format chapters into the MP3:
- Maps metadata from chapters.txt to MP3
- Copies audio codec (no re-encoding)
- Creates temporary file, then replaces original

### Verification

After embedding, verify chapters:
- Play in podcast app with chapter support
- Check chapter navigation works
- Verify chapter titles display correctly

---

## File Outputs Summary

| File | Purpose | Size |
|------|---------|------|
| `YYYY-MM-DD-slug.mp3` | Final audio with chapters | ~30 MB |
| `_transcript.json` | Whisper output | ~400 KB |
| `_chapters.txt` | FFmpeg metadata format | ~1 KB |
| `_chapters.json` | Podcasting 2.0 format | ~1 KB |

---

## Metadata Requirements for Publishing

After audio processing, collect this metadata for feed.xml:

| Metadata | How to Obtain | Feed Element |
|----------|---------------|--------------|
| File size | File system (bytes) | `<enclosure length="">` |
| Duration | FFmpeg output | `<itunes:duration>` |
| Chapter count | chapters.json | Documentation only |
| Chapters URL | After publishing | `<podcast:chapters url="">` |

---

## Quality Assurance Checklist

Before publishing:

- [ ] MP3 file plays correctly
- [ ] Audio quality acceptable (no artifacts)
- [ ] Duration matches expected length
- [ ] Transcript accuracy spot-checked
- [ ] Chapter count is 10-15
- [ ] Chapter transitions make logical sense
- [ ] Chapter titles are descriptive
- [ ] Chapters embedded in MP3
- [ ] File size within limits (<100 MB)
- [ ] File size recorded in bytes
- [ ] Duration recorded in MM:SS or HH:MM:SS

---

## Troubleshooting

### Whisper Model Errors

**Problem:** Model download fails or hangs
**Solution:** Run certificate installation for Python, check internet connection

### FFmpeg Errors

**Problem:** Chapter embedding fails
**Solution:** Verify chapters.txt format, check TIMEBASE is 1/1000, verify START/END are integers

### Large Transcript Files

**Problem:** Transcript JSON is very large
**Solution:** Store in `tmp/` directory (gitignored) or commit without word-level timestamps

### Audio Quality Issues

**Problem:** Audio sounds distorted after conversion
**Solution:** Check source file quality, try higher bitrate (160k or 192k)

---

## Alternative: API-Based Transcription

For faster transcription or when local Whisper isn't available:

### OpenAI Whisper API

- Faster than local processing
- Requires OPENAI_API_KEY
- Incurs API costs
- Use `--use-api` flag with transcription tool

### Considerations

| Aspect | Local Whisper | API Whisper |
|--------|---------------|-------------|
| Speed | Slower | Faster |
| Cost | Free | Per-minute billing |
| Privacy | Full | Data sent to OpenAI |
| Quality | Same models | Same models |
