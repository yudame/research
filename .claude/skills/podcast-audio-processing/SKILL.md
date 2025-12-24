---
name: podcast-audio-processing
description: Process podcast audio files end-to-end for episodes. Handles conversion (m4a→mp3), local Whisper transcription, chapter generation from transcript analysis, and chapter embedding. Use when user provides NotebookLM audio file that needs processing. Returns file metadata (duration, size) needed for publishing.
---

# Podcast Audio Processing

**Skill name:** `podcast-audio-processing`

You are a specialized subagent that processes podcast audio files end-to-end. This skill supports two workflows:

1. **Gemini Audio Generation** - Generate audio from research materials using Gemini 2.5 Native Audio API
2. **NotebookLM Processing** - Process existing audio from NotebookLM (convert, transcribe, chapter, embed)

## Required Input Files for Gemini Generation

For Gemini-based audio generation, you need **4 critical input files** as rich context:

| File | Location | Purpose | Typical Size |
|------|----------|---------|--------------|
| `p1-brief.md` | `research/` | Phase 1 academic research briefing | ~2KB |
| `p3-briefing.md` | `research/` | Phase 3 comprehensive policy/industry research | ~50-80KB |
| `report.md` | Episode root | Final synthesized research report | ~20-50KB |
| `sources.md` | Episode root | Validated source links and citations | ~5-10KB |

**Total context:** 80-140KB of rich, structured research material

This NotebookLM-style approach feeds the model massive context rather than sparse prompts, enabling it to elaborate and explore rather than summarize.

## How to Invoke This Skill

### For Gemini Audio Generation

```
Use the Task tool with subagent_type="general-purpose" and prompt:

"Generate podcast audio for this episode using the podcast-audio-processing skill with Gemini.

Episode path: podcast/episodes/cardiovascular-health/ep5-diet
Episode slug: 2025-12-20-cardiovascular-diet

Required input files:
- research/p1-brief.md (Phase 1 academic briefing)
- research/p3-briefing.md (Phase 3 policy/industry research)
- report.md (synthesized research report)
- sources.md (validated citations)

Follow the podcast-audio-processing skill to:
1. Verify all 4 required input files exist
2. Run generate_audio.py --context-rich mode
3. Process output (transcribe, chapters, embed)
4. Log to prompts.md

CRITICAL: Report back the file metadata when complete:
- Duration: MM:SS format
- File size: bytes"
```

### For NotebookLM Processing

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
- File size: bytes"
```

---

## Workflow A: Gemini Audio Generation

Use this workflow to generate podcast audio from research materials.

### Step A1: Verify Required Input Files

Check that all 4 critical input files exist:

```bash
cd ~/src/research/podcast/episodes/EPISODE_PATH

# Verify files exist
ls -la research/p1-brief.md research/p3-briefing.md report.md sources.md
```

**If any files are missing, stop and report which files are needed.**

### Step A2: Check Context Size

Verify the combined context is appropriate:

```bash
# Check total size of input files
wc -c research/p1-brief.md research/p3-briefing.md report.md sources.md
```

**Target:** 80-150KB combined. If much smaller, the audio may be too short.

### Step A3: Generate Audio with Gemini

Run the context-rich audio generation:

```bash
cd ~/src/research/podcast/tools

# Activate virtual environment
source .venv/bin/activate

# Generate audio using context-rich mode
python generate_audio.py ../episodes/EPISODE_PATH --context-rich --verbose
```

**What this does:**
1. Loads all source materials (report.md + research files) as rich context
2. Generates 3 parts (~12 minutes each) using Gemini 2.5 Native Audio API
3. Feeds transcript of each part into the next for continuity
4. Stitches parts together into final ~36 minute episode
5. Transcribes using local Whisper
6. Outputs: mp3 file + transcript.txt

**Expected runtime:** 15-30 minutes depending on API latency

**Output files:**
- `EPISODE_SLUG.mp3` - Final stitched audio (~30MB)
- `transcript.txt` - Full episode transcript
- `tmp/generation_metrics.json` - Generation stats

### Step A4: Create and Embed Chapters

After generation, analyze the transcript and create chapters:

```bash
cd ~/src/research/podcast/episodes/EPISODE_PATH

# Read transcript and identify topic transitions
# Create chapter files (see Step 4 in Workflow B for format)
```

Then embed chapters:

```bash
ffmpeg -i EPISODE_SLUG.mp3 -i EPISODE_SLUG_chapters.txt -map_metadata 1 -codec copy temp.mp3 -y
mv temp.mp3 EPISODE_SLUG.mp3
```

### Step A5: Log to prompts.md

Update the episode's `prompts.md`:

```markdown
## Audio Generation Phase (Gemini)

**Generation Method:** Gemini 2.5 Native Audio API (context-rich mode)
**Voice:** Alnilam
**Model:** gemini-2.5-flash-native-audio-latest

**Input Files:**
- research/p1-brief.md ([X] KB)
- research/p3-briefing.md ([X] KB)
- report.md ([X] KB)
- sources.md ([X] KB)
- Total context: [X] KB

**Output:**
- Duration: MM:SS
- File Size: [bytes]
- Parts: 3 (~12 min each)

**Transcription:**
- Tool: Local Whisper (openai-whisper)
- Model: base
- Output: transcript.txt

**Chapters:**
- Count: [N] chapters
- Embedded in mp3

**Date:** YYYY-MM-DD
```

---

## Workflow B: NotebookLM Processing

Use this workflow when user provides pre-made audio from NotebookLM.

### Step B1: Convert Audio Format (if needed)

Check if the audio file is .m4a format. If so, convert to mp3:

```bash
cd ~/src/research/podcast/episodes/EPISODE_PATH

# Convert m4a to mp3 (128kbps for optimal size/quality)
ffmpeg -i "AUDIO_FILENAME.m4a" -codec:a libmp3lame -b:a 128k "EPISODE_SLUG.mp3" -y
```

**Note the metadata from ffmpeg output:**
- Duration (format: HH:MM:SS or MM:SS)
- This will be needed for publishing

### Step B2: Get File Metadata

Get the file size in bytes:

```bash
ls -l EPISODE_SLUG.mp3 | awk '{print $5}'
```

**Record:**
- File size: [bytes]
- Duration: [from ffmpeg output]

### Step B3: Generate Transcript with Local Whisper

Run Whisper transcription locally (no API key needed):

```bash
cd ~/src/research/podcast/tools

# Basic transcription
python transcribe_only.py ../episodes/EPISODE_PATH/EPISODE_SLUG.mp3 --model base

# OR with organized logging (recommended for production)
mkdir -p ../episodes/EPISODE_PATH/logs
python transcribe_only.py ../episodes/EPISODE_PATH/EPISODE_SLUG.mp3 \
  --model base \
  --log-dir ../episodes/EPISODE_PATH/logs \
  --quiet
```

**Whisper model options:**
- `tiny`: Fastest (~1-2 min for 30 min audio), basic accuracy
- `base`: **[recommended]** Fast (~5-10 min), good accuracy
- `small`: Slower (~15-20 min), better accuracy
- `medium`: Slowest (~30-40 min), best accuracy

**Default to `base` model unless user specifies otherwise.**

**Output:**
- Creates: `EPISODE_SLUG_transcript.json` in the episode directory
- With `--log-dir`: Also creates timestamped log file in logs/ directory
- `--quiet`: Suppresses progress messages (useful in automated workflows)

**Output format:**
- JSON file with full transcript
- Includes text and word-level timestamps
- File size: ~300-400KB for 30-40 min episode

### Step B4: Analyze Transcript and Create Chapters

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

### Step B5: Embed Chapters into MP3

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

### Step B6: Log to prompts.md

Update the episode's `prompts.md` file:

```markdown
## Audio Processing Phase (NotebookLM)

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

---

## First-Time Setup

### For Gemini Generation

```bash
cd ~/src/research/podcast/tools

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify GOOGLE_API_KEY is set
echo $GOOGLE_API_KEY
```

### For Whisper Transcription

```bash
cd ~/src/research/podcast/tools

# Fix SSL certificates (macOS Python)
/Applications/Python\ 3.12/Install\ Certificates.command

# Install dependencies (if not using venv)
pip install -r requirements.txt
```

---

## Technical Notes

### Gemini Generation
- **Voice:** Alnilam (baritone, slight Austrian undertones)
- **Model:** gemini-2.5-flash-native-audio-latest
- **Target duration:** ~36 minutes (3 parts × 12 min)
- **Speaking rate:** ~135 words/minute
- **Context loading:** All source materials loaded for each part generation

### Whisper Transcription
- **Transcription is 100% local:** No API calls, completely private, free
- **Transcript files are large:** 300-400KB - read in sections if needed
- **Whisper timing:** base model takes ~5-10 minutes for 30-minute audio

### Chapter Support
- Modern podcast apps will display chapters; older apps will ignore them

---

## Files Created

After completion, these files should exist in the episode directory:

| File | Size | Description |
|------|------|-------------|
| `EPISODE_SLUG.mp3` | ~30MB | Final audio with embedded chapters |
| `transcript.txt` | ~15KB | Plain text transcript (Gemini) |
| `EPISODE_SLUG_transcript.json` | ~400KB | Full transcript with timestamps (NotebookLM) |
| `EPISODE_SLUG_chapters.txt` | ~2KB | FFmpeg chapter format |
| `EPISODE_SLUG_chapters.json` | ~1KB | Podcasting 2.0 format |

---

## Error Handling

### Gemini Generation Errors

**If generation produces short audio (<20 min):**
- Check that all 4 input files have sufficient content
- Verify total context is 80KB+
- Model may be summarizing - check prompts.py for duration requirements

**If API errors occur:**
- Verify GOOGLE_API_KEY is set and valid
- Check API quota/billing
- Try running with --verbose for detailed logs

### Audio Conversion Errors

**If conversion fails:**
- Check that audio file exists and path is correct
- Verify ffmpeg is installed: `ffmpeg -version`

### Transcription Errors

**If transcription fails:**
- Check that Whisper is installed: `pip list | grep openai-whisper`
- Verify audio file is accessible
- Try smaller model (tiny) if base is too slow

### Chapter Embedding Errors

**If chapter embedding fails:**
- Verify chapters.txt file exists and has correct format
- Check that START/END times don't exceed audio duration
- Ensure TIMEBASE is set correctly (1/1000 for milliseconds)

---

## Final Report

When complete, report back to main agent:

### Gemini Generation
- Audio generated: `EPISODE_SLUG.mp3`
- Duration: MM:SS (target: ~36:00)
- File size: [bytes]
- Transcript: transcript.txt ([N] words)
- Chapters: [N] chapters (embedded)
- Files ready for publishing phase

### NotebookLM Processing
- Audio processed: `EPISODE_SLUG.mp3`
- Duration: MM:SS
- File size: [bytes]
- Transcript generated: [N] words
- Chapters created: [N] chapters
- Chapters embedded in mp3
- Files ready for publishing phase
