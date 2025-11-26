# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a dual-purpose repository:
1. **Podcast Publishing System** - Self-hosted GitHub Pages podcast feed (primary active component)
2. **Learning Research Library** - Educational framework for early childhood development (long-term development)

## Podcast Workflow Architecture

The podcast creation follows a 7-phase workflow defined in `.claude/skills/new-podcast-episode.md`. The user handles research and audio creation (NotebookLM), while Claude handles file processing, transcription, and publishing.

### Complete Episode Structure
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/
│   ├── sources.md          # Validated source links
│   ├── documents/          # PDFs, articles
│   └── assets/             # Images, charts
├── report.md               # Research report (~20KB)
├── YYYY-MM-DD-slug.mp3     # Final audio with chapters (~30MB, 128kbps)
├── YYYY-MM-DD-slug_transcript.json    # Whisper output (~400KB)
├── YYYY-MM-DD-slug_chapters.txt       # FFmpeg metadata format
└── YYYY-MM-DD-slug_chapters.json      # Podcasting 2.0 format
```

### Audio Processing Commands

**Convert m4a to mp3:**
```bash
cd podcast/episodes/YYYY-MM-DD-slug
ffmpeg -i "original.m4a" -codec:a libmp3lame -b:a 128k "YYYY-MM-DD-slug.mp3" -y
```

**Generate transcript (local Whisper):**
```bash
cd podcast/tools
python transcribe_only.py ../episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3 --model base
```

Whisper model options:
- `tiny` - Fastest (~1-2 min for 30 min audio), basic accuracy
- `base` - **Recommended** (~5-10 min), good accuracy
- `small` - Slower (~15-20 min), better accuracy

**Embed chapters into mp3:**
```bash
cd podcast/episodes/YYYY-MM-DD-slug
ffmpeg -i YYYY-MM-DD-slug.mp3 -i YYYY-MM-DD-slug_chapters.txt -map_metadata 1 -codec copy temp.mp3 -y
mv temp.mp3 YYYY-MM-DD-slug.mp3
```

**Get file metadata:**
```bash
ls -l file.mp3 | awk '{print $5}'  # File size in bytes
# Duration appears in ffmpeg output during conversion
```

### Chapter Guidelines

- Create 10-15 chapters for 30-40 minute episodes
- Each chapter: 2-4 minutes
- Analyze full transcript to identify natural topic transitions
- Create both formats:
  - `_chapters.txt` - FFmpeg metadata (TIMEBASE=1/1000, START/END in milliseconds)
  - `_chapters.json` - Podcasting 2.0 (startTime in seconds)

### Publishing Workflow

1. Update `podcast/feed.xml` with new `<item>` block (insert after `<channel>` metadata, before other episodes)
2. Include: title, description with report link, validated source links, pubDate (RFC 2822), enclosure URL/length/type, duration, keywords
3. Commit with descriptive message using heredoc format
4. GitHub Pages deploys automatically in 2-3 minutes

**Feed URL:** `https://research.yuda.me/podcast/feed.xml`

## Repository Constraints

### File Limits
- Max 8 episodes total
- Max 100MB per episode
- Target: ~30MB per 30-40 min episode (128kbps mp3)
- Keep repo under 1GB total

### Git Practices
- Use TodoWrite tool to track progress through podcast workflow phases
- Use heredoc format for multi-line commit messages
- Commit only when explicitly requested by user
- Source files (.m4a) are gitignored - only commit final .mp3

### File Naming Convention
- Episodes: `YYYY-MM-DD-topic-slug.mp3`
- Transcripts: `YYYY-MM-DD-topic-slug_transcript.json`
- Chapters: `YYYY-MM-DD-topic-slug_chapters.{txt,json}`

## GitHub Pages Setup

Located at: `https://research.yuda.me/`

Configuration:
- Source: main branch, root folder
- `.nojekyll` file present (disables Jekyll processing)
- Auto-deploys on push to main

Verify settings: Repository Settings → Pages

## Tools & Dependencies

### Podcast Tools (`podcast/tools/`)
- `transcribe_only.py` - Local Whisper transcription (no API key needed)
- `generate_chapters.py` - Whisper + Claude chapter generation (requires Anthropic API key)
- `requirements.txt` - Python dependencies (`openai-whisper`, `anthropic`)

### System Requirements
- Python 3.12
- FFmpeg 8.0
- Git

First-time Whisper setup (macOS):
```bash
cd podcast/tools
/Applications/Python\ 3.12/Install\ Certificates.command
pip install -r requirements.txt
```

## Learning Research Context

The secondary purpose is an educational framework for Pre-K through Grade 12, combining Montessori principles with neuroscience-based learning.

Key documents:
- `README.md` - Vision and philosophy
- `TODO.md` - Development roadmap (223 items)
- `level-0-goals.md` - Pre-K/Kindergarten weekly goals (8 core components)
- `ai-teacher-architecture.md` - iPad app specifications

Current focus: Level 0 (Pre-K/Kindergarten) development

## Research Prompt Methodology

When helping craft research prompts for episodes:
- Emphasize research methodology over predetermined structure
- Prioritize peer-reviewed studies, meta-analyses, authoritative sources
- Distinguish correlation from causation
- Report effect sizes and practical significance
- Note study populations and generalizability
- Compare individual studies against meta-analyses
- Identify preliminary vs well-replicated findings
- Note funding sources and conflicts of interest
- Include contradictory findings and uncertainties
- Cite specific studies and sources

Template in `.claude/skills/new-podcast-episode.md` lines 69-87.

## Episode Description Best Practices

- 1-2 compelling sentences highlighting key topics and takeaways
- Always include link to full report: `https://research.yuda.me/podcast/episodes/YYYY-MM-DD-slug/report.md`
- Add "Key Sources:" section with 3-5 validated official links
- Prioritize: official legislation/regulation, academic analysis, primary sources
- Use WebSearch to find and WebFetch to validate official URLs when possible

## Common Workflows

### Adding a New Podcast Episode
Use the `/podcast-episode` slash command with the topic, which triggers the complete 7-phase workflow from `.claude/skills/new-podcast-episode.md`.

### Purging Old Episodes (when approaching limits)
```bash
# Use BFG Repo-Cleaner to remove large files from git history
# Then force push with --force flag
```

### Validating Feed
After updating feed.xml, check:
- Valid XML structure
- Correct file sizes (in bytes)
- Correct duration format (MM:SS or HH:MM:SS)
- RFC 2822 date format for pubDate
- All URLs accessible
