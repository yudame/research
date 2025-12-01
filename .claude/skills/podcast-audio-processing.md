# Podcast Audio Processing

**Skill name:** `podcast-audio-processing`

You are a specialized subagent that processes podcast audio files end-to-end: convert, transcribe, create chapters, embed metadata.

## How to Invoke This Skill

From the main podcast workflow, invoke this skill using the Task tool:

```
Use the Task tool with subagent_type="general-purpose" and prompt:

"Process the podcast audio file for this episode using the podcast-audio-processing skill.

Episode path: podcast/episodes/2025-12-01-topic-slug
Audio filename: [filename user provided, e.g., 'Original_Audio.m4a']
Episode slug: 2025-12-01-topic-slug

Follow the podcast-audio-processing skill to:
1. Convert to mp3 if needed (m4a → mp3)
2. Get file metadata (size in bytes, duration)
3. Transcribe with local Whisper (base model)
4. Analyze transcript and create 10-15 chapter markers
5. Embed chapters into mp3
6. Log to prompts.md

CRITICAL: Report back the file metadata when complete:
- Duration: MM:SS format
- File size: bytes
This metadata is needed for the publishing phase."
```

## Task

Take a raw audio file from NotebookLM and process it into a final podcast-ready mp3 with embedded chapters, transcript, and chapter files.

## Required Information

You will receive:
- **Episode path:** Full path to episode directory (e.g., `podcast/episodes/2025-12-01-topic-slug`)
- **Audio filename:** Name of the audio file the user added (e.g., `Original_Audio.m4a` or `2025-12-01-topic-slug.mp3`)
- **Episode slug:** The filename slug (e.g., `2025-12-01-topic-slug`)

## Workflow

### Step 1: Convert Audio Format (if needed)

Check if the audio file is .m4a format. If so, convert to mp3:

```bash
cd ~/src/research/podcast/episodes/EPISODE_PATH

# Convert m4a to mp3 (128kbps for optimal size/quality)
ffmpeg -i "AUDIO_FILENAME.m4a" -codec:a libmp3lame -b:a 128k "EPISODE_SLUG.mp3" -y
```

**Note the metadata from ffmpeg output:**
- Duration (format: HH:MM:SS or MM:SS)
- This will be needed for publishing

### Step 2: Get File Metadata

Get the file size in bytes:

```bash
ls -l EPISODE_SLUG.mp3 | awk '{print $5}'
```

**Record:**
- File size: [bytes]
- Duration: [from ffmpeg output]

### Step 3: Generate Transcript with Local Whisper

Run Whisper transcription locally (no API key needed):

```bash
cd ~/src/research/podcast/tools
python transcribe_only.py ../episodes/EPISODE_PATH/EPISODE_SLUG.mp3 --model base
```

**Whisper model options:**
- `tiny`: Fastest (~1-2 min for 30 min audio), basic accuracy
- `base`: **[recommended]** Fast (~5-10 min), good accuracy
- `small`: Slower (~15-20 min), better accuracy

**Default to `base` model unless user specifies otherwise.**

This creates: `EPISODE_SLUG_transcript.json` in the episode directory

**Output format:**
- JSON file with full transcript
- Includes text and word-level timestamps
- File size: ~300-400KB for 30-40 min episode

### Step 4: Analyze Transcript and Create Chapters

Read the transcript file and analyze it to identify natural topic transitions.

**Chapter creation guidelines:**
- Aim for 10-15 chapters for a 30-40 minute episode
- Each chapter should be 2-4 minutes long
- Chapter titles should be descriptive and capture the key topic/story
- Include subtitles or key concepts after the main title when helpful
- Analyze the full transcript to identify natural topic transitions
- Look for: topic shifts, new concepts introduced, story transitions, framework changes

**Create two chapter files:**

1. **FFmpeg metadata format** (`EPISODE_SLUG_chapters.txt`):
```
;FFMETADATA1
[CHAPTER]
TIMEBASE=1/1000
START=0
END=120000
title=Introduction: The Topic Overview

[CHAPTER]
TIMEBASE=1/1000
START=120000
END=300000
title=Historical Context: Early Development
```

2. **Podcasting 2.0 format** (`EPISODE_SLUG_chapters.json`):
```json
{
  "version": "1.2.0",
  "chapters": [
    {
      "startTime": 0,
      "title": "Introduction: The Topic Overview"
    },
    {
      "startTime": 120,
      "title": "Historical Context: Early Development"
    }
  ]
}
```

**Important format notes:**
- FFmpeg format: START/END in milliseconds (TIMEBASE=1/1000)
- Podcasting 2.0 format: startTime in seconds (decimal)
- Last chapter END time should match audio duration in milliseconds

### Step 5: Embed Chapters into MP3

Embed the chapter metadata into the mp3 file:

```bash
cd ~/src/research/podcast/episodes/EPISODE_PATH

# Embed chapters using FFmpeg metadata file
ffmpeg -i EPISODE_SLUG.mp3 -i EPISODE_SLUG_chapters.txt -map_metadata 1 -codec copy temp.mp3 -y

# Replace original with chaptered version
mv temp.mp3 EPISODE_SLUG.mp3
```

**Result:**
- Chapters embedded in mp3 file
- Will appear in podcast apps that support chapters (Overcast, Pocket Casts, Apple Podcasts)
- File size remains the same

### Step 6: Log to prompts.md

Update the episode's `prompts.md` file:

```markdown
## Audio Processing Phase

**Audio File:** AUDIO_FILENAME
**Converted to:** EPISODE_SLUG.mp3
**Duration:** MM:SS
**File Size:** [bytes]

**Transcription:**
- Tool: Local Whisper (openai-whisper)
- Model: base
- Output: EPISODE_SLUG_transcript.json
- Date: YYYY-MM-DD

**Chapters:**
- Count: [N] chapters
- Created by analyzing transcript for natural topic transitions
- Formats: FFmpeg metadata (.txt) and Podcasting 2.0 (.json)
- Embedded into mp3 file

**Date:** YYYY-MM-DD
```

## First-Time Setup (if needed)

If the user hasn't set up Whisper yet:

```bash
cd ~/src/research/podcast/tools

# Fix SSL certificates (macOS Python)
/Applications/Python\ 3.12/Install\ Certificates.command

# Install dependencies
pip install -r requirements.txt
```

## Technical Notes

- **Transcription is 100% local:** No API calls, completely private, free
- **Transcript files are large:** 300-400KB - read in sections if needed using Read tool with offset/limit
- **Whisper timing:** base model takes ~5-10 minutes for 30-minute audio
- **Chapter support:** Modern podcast apps will display chapters; older apps will ignore them

## Files Created

After completion, these files should exist in the episode directory:
- `EPISODE_SLUG.mp3` - Final audio with embedded chapters (~30MB for 30-40 min)
- `EPISODE_SLUG_transcript.json` - Full transcript (~400KB)
- `EPISODE_SLUG_chapters.txt` - FFmpeg chapter format (~2KB)
- `EPISODE_SLUG_chapters.json` - Podcasting 2.0 format (~1KB)

## Error Handling

**If conversion fails:**
- Check that audio file exists and path is correct
- Verify ffmpeg is installed: `ffmpeg -version`

**If transcription fails:**
- Check that Whisper is installed: `pip list | grep openai-whisper`
- Verify audio file is accessible
- Try smaller model (tiny) if base is too slow

**If chapter embedding fails:**
- Verify chapters.txt file exists and has correct format
- Check that START/END times don't exceed audio duration
- Ensure TIMEBASE is set correctly (1/1000 for milliseconds)

## Final Report

When complete, report back to main agent:
- ✅ Audio processed: `EPISODE_SLUG.mp3`
- Duration: MM:SS
- File size: [bytes]
- ✅ Transcript generated: [N] words
- ✅ Chapters created: [N] chapters
- ✅ Chapters embedded in mp3
- Files ready for publishing phase
