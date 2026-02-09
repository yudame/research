# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a dual-purpose repository:
1. **Podcast Publishing System** - Self-hosted GitHub Pages podcast feed (primary active component)
2. **Learning Research Library** - Educational framework for early childhood development (long-term development)

## Podcast Workflow Architecture

The podcast creation follows a **12-phase workflow** defined in `.claude/skills/new-podcast-episode.md`. The system uses NotebookLM for two-host AI audio generation with comprehensive quality controls.

### Quality Framework (Waves 1-5)

The workflow has been enhanced through 5 waves of improvements validated on Episode 8 (44/50 score):

| Wave | Focus | Key Artifacts |
|------|-------|---------------|
| Wave 1 | Research & Synthesis | `docs/templates/p3-briefing-enhanced.md` |
| Wave 2 | Episode Planning | `docs/templates/content_plan-enhanced.md` |
| Wave 3 | Audio Generation | NotebookLM episodeFocus enhancements |
| Wave 4 | Publishing | `docs/templates/metadata-enhanced.md` |
| Wave 5 | Quality Gates | Exit criteria enforcement |

### Complete Episode Structure
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/
│   ├── p1-brief.md              # Research query
│   ├── p2-*.md                  # Research results
│   ├── p3-briefing.md           # Master briefing (Wave 1 enhanced)
│   ├── sources.md               # Validated source links
│   ├── documents/               # PDFs, articles
│   └── assets/                  # Images, charts
├── report.md                    # Narrative synthesis (~18KB)
├── sources.md                   # Validated links (~8KB)
├── content_plan.md              # Episode structure (~10KB)
├── YYYY-MM-DD-slug.mp3          # Final audio (~30MB, 128kbps)
├── YYYY-MM-DD-slug_transcript.json
├── YYYY-MM-DD-slug_chapters.txt
├── YYYY-MM-DD-slug_chapters.json
├── companion/                   # One-pagers, checklists (Wave 4)
│   ├── *-summary.md
│   ├── *-checklist.md
│   └── *-frameworks.md
├── index.html                   # Landing page (Wave 4)
└── logs/
    ├── metadata.md              # Publishing metadata
    └── quality_scorecard.md     # 10-dimension quality assessment
```

### Key Tools (`podcast/tools/`)

| Script | Purpose |
|--------|---------|
| `notebooklm_api.py` | NotebookLM Enterprise API integration |
| `notebooklm_prompt.py` | Generate episodeFocus prompts |
| `transcribe_only.py` | Local Whisper transcription |
| `generate_chapters.py` | AI-powered chapter generation |
| `update_feed.py` | Update feed.xml with new episode |
| `generate_companion_resources.py` | Create summary, checklist, frameworks (Wave 4) |
| `generate_landing_page.py` | Generate HTML episode page (Wave 4) |

### Audio Processing Commands

**Generate transcript (local Whisper):**
```bash
cd podcast/tools
uv run python transcribe_only.py ../episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3 --model base
```

**Embed chapters into mp3:**
```bash
cd podcast/episodes/YYYY-MM-DD-slug
ffmpeg -i YYYY-MM-DD-slug.mp3 -i YYYY-MM-DD-slug_chapters.txt -map_metadata 1 -codec copy temp.mp3 -y
mv temp.mp3 YYYY-MM-DD-slug.mp3
```

**Generate companion resources:**
```bash
cd podcast/tools
python generate_companion_resources.py ../episodes/YYYY-MM-DD-slug/
python generate_landing_page.py ../episodes/YYYY-MM-DD-slug/
```

### Chapter Guidelines

- Create 10-15 chapters for 30-40 minute episodes
- Each chapter: 2-4 minutes
- Analyze full transcript to identify natural topic transitions
- Create both formats:
  - `_chapters.txt` - FFmpeg metadata (TIMEBASE=1/1000, START/END in milliseconds)
  - `_chapters.json` - Podcasting 2.0 (startTime in seconds)

### Publishing Workflow

1. Update `podcast/feed.xml` using `update_feed.py` or manually
2. Include: title, description, "What You'll Learn", timestamps, resources, CTAs
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
- Use Task tools (TaskCreate, TaskUpdate, TaskList) to track progress through workflow phases
- Use heredoc format for multi-line commit messages
- Commit only when explicitly requested by user

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

## System Requirements
- Python 3.12
- FFmpeg 8.0
- Git
- API keys in `.env`: ANTHROPIC_API_KEY, OPENROUTER_API_KEY, OPENAI_API_KEY

## Key Documentation

| Document | Purpose |
|----------|---------|
| `.claude/skills/new-podcast-episode.md` | Complete 12-phase workflow |
| `docs/plans/podcast_episode_improvements.md` | Improvement roadmap (37 tasks, 6 waves) |
| `docs/plans/podcast-content.md` | Content framework reference |
| `.claude/skills/podcast-quality-scorecard/SKILL.md` | 10-dimension quality assessment |

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

## Episode Description Best Practices

- 1-2 compelling sentences highlighting key topics and takeaways
- Include "What You'll Learn" section (3-5 bullets)
- Add key timestamps for navigation
- Group resources by type with actionable descriptions
- Always include link to full report
- Include clear call-to-action

## Common Workflows

### Adding a New Podcast Episode
Use the `/podcast-episode` slash command with the topic, which triggers the complete 12-phase workflow from `.claude/skills/new-podcast-episode.md`.

### Validating Feed
After updating feed.xml, check:
- Valid XML structure
- Correct file sizes (in bytes)
- Correct duration format (MM:SS or HH:MM:SS)
- RFC 2822 date format for pubDate
- All URLs accessible
