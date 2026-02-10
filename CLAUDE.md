# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a dual-purpose repository:
1. **Podcast Publishing System** - Self-hosted GitHub Pages podcast feed (primary active component)
2. **Learning Research Library** - Educational framework for early childhood development (long-term development)

## Podcast Workflow Architecture

The podcast creation follows a **12-phase workflow** defined in `.claude/skills/new-podcast-episode.md`. The system uses NotebookLM for two-host AI audio generation with comprehensive quality controls.

### Quality Framework (Waves 1-5 Complete)

The workflow has been enhanced through 5 waves of improvements. Wave 1 validated on Episode 8 (28→44/50, +32%). Waves 2-5 implemented 2026-02-10.

| Wave | Focus | Status | Key Changes |
|------|-------|--------|-------------|
| Wave 1 | Research & Synthesis | ✅ Validated | Enhanced p3-briefing template, Phase 6 exit criteria, synthesis agent input validation |
| Wave 2 | Episode Planning | ✅ Complete | Episode planner v4.0 with Structure Map, Mode-Switching, Signposting, Depth Budget, Counterpoint Moments (assigned positions), Episode Arc. Phase 8 exit criteria enforce all sections |
| Wave 3 | Audio Generation | ✅ Complete | episodeFocus prompts enhanced with STRUCTURAL GUIDANCE, DIALOGUE DYNAMICS (explicit disagreement instructions), EPISODE ARC in both `notebooklm_prompt.py` and `notebooklm_api.py` |
| Wave 4 | Publishing | ✅ Complete | `update_feed.py` generates structured HTML (What You'll Learn, Timestamps, Resources, CTA), `<podcast:transcript>` tag, companion resources integrated into Phase 11 |
| Wave 5 | Quality Gates | ✅ Complete | Phase 8 exit criteria enforce Wave 2 structural sections (blocking). Phase 11 exit criteria enforce Wave 4 packaging sections (blocking) |

**Templates:**
- `docs/templates/p3-briefing-enhanced.md` — Research briefing with Wave 1 sections
- `docs/templates/content_plan-enhanced.md` — Episode plan with Wave 2 structural design
- `docs/templates/metadata-enhanced.md` — Publishing metadata with Wave 4 packaging sections

### Complete Episode Structure
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/
│   ├── p1-brief.md              # Research query
│   ├── p2-*.md                  # Research results (perplexity, grok, chatgpt, gemini, claude)
│   ├── p3-briefing.md           # Master briefing (Wave 1: Depth Analysis, Story Bank, Counterpoints, etc.)
│   ├── sources.md               # Validated source links
│   ├── documents/               # PDFs, articles
│   └── assets/                  # Images, charts
├── report.md                    # Narrative synthesis (~18KB)
├── sources.md                   # Validated links (~8KB)
├── content_plan.md              # Episode structure with Wave 2 design (~12KB)
│                                #   Structure Map, Mode-Switching, Signposting, Depth Budget,
│                                #   Counterpoint Moments, Episode Arc, NotebookLM guidance
├── YYYY-MM-DD-slug.mp3          # Final audio (~30MB, 128kbps)
├── YYYY-MM-DD-slug_chapters.json # Podcasting 2.0 chapters
├── transcript.txt               # Plain text transcript
├── companion/                   # Generated companion resources (Wave 4)
│   ├── *-summary.md
│   ├── *-checklist.md
│   └── *-frameworks.md
├── index.html                   # Landing page (Wave 4)
└── logs/
    ├── metadata.md              # Enhanced publishing metadata (Wave 4 template)
    │                            #   What You'll Learn, Timestamps, Resources, CTA, Show Notes HTML
    └── quality_scorecard.md     # 10-dimension quality assessment
```

### Key Tools (`podcast/tools/`)

| Script | Purpose |
|--------|---------|
| `notebooklm_api.py` | NotebookLM Enterprise API with enhanced episodeFocus (structural guidance, dialogue dynamics, arc) |
| `notebooklm_prompt.py` | Generate episodeFocus prompts with Wave 3 enhancements (counterpoint execution, signposting) |
| `transcribe_only.py` | Local Whisper transcription |
| `generate_chapters.py` | AI-powered chapter generation |
| `update_feed.py` | Update feed.xml with structured HTML show notes, `<podcast:transcript>`, enhanced metadata parsing |
| `generate_companion_resources.py` | Create summary, checklist, frameworks from report.md |
| `generate_landing_page.py` | Generate HTML episode page with full metadata |

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

1. Create `logs/metadata.md` using enhanced template (`docs/templates/metadata-enhanced.md`)
   - Includes: title, description, What You'll Learn, Key Timestamps, Resources grouped by type, CTA, Keywords
2. Run companion resource scripts:
   - `generate_companion_resources.py` → summary, checklist, frameworks in `companion/`
   - `generate_landing_page.py` → `index.html`
3. Update `podcast/feed.xml` using `update_feed.py`
   - Generates structured HTML `<content:encoded>` (Overview, What You'll Learn, Timestamps, Resources)
   - Adds `<podcast:transcript>` tag linking to `transcript.txt`
   - Includes `<itunes:episodeType>`, `<itunes:episode>` tags
4. Validate feed with `podcast-feed-validator` skill
5. Commit with descriptive message using heredoc format
6. GitHub Pages deploys automatically in 2-3 minutes

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
| `.claude/skills/new-podcast-episode.md` | Complete 12-phase workflow with Wave 1-5 exit criteria |
| `.claude/skills/podcast-episode-planner/SKILL.md` | Episode planner v4.0 with Wave 2 structural design |
| `.claude/agents/podcast-synthesis-writer.md` | Synthesis agent with Wave 1 input validation |
| `.claude/skills/podcast-quality-scorecard/SKILL.md` | 10-dimension quality assessment |
| `docs/plans/podcast_episode_improvements.md` | Improvement roadmap (Waves 1-5 complete, Wave 6 pending) |
| `docs/templates/p3-briefing-enhanced.md` | Wave 1 research briefing template |
| `docs/templates/content_plan-enhanced.md` | Wave 2 episode planning template |
| `docs/templates/metadata-enhanced.md` | Wave 4 publishing metadata template |

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

## Episode Metadata Best Practices

**Plain text description (`<description>`):**
- 1-2 compelling sentences highlighting key topics and takeaways
- Include link to full research report

**Enhanced HTML show notes (`<content:encoded>`):**
- Overview section with expanded description
- "What You'll Learn" section (3-5 verb-led bullets with specific numbers)
- Key timestamps (5-7 major sections with enticing descriptions)
- Resources grouped by type (Research Papers, Tools, Further Reading) with actionable descriptions
- Link to full research report
- Call-to-action (primary CTA + voiced CTA for audio)

**Feed.xml enhancements:**
- `<itunes:episodeType>` (full/trailer/bonus)
- `<itunes:episode>` and `<itunes:season>` for series episodes
- `<podcast:transcript>` linking to transcript.txt
- `<podcast:chapters>` linking to chapters JSON

## Common Workflows

### Adding a New Podcast Episode
Use the `/podcast-episode` slash command with the topic, which triggers the complete 12-phase workflow from `.claude/skills/new-podcast-episode.md`.

**Quality gates enforced during workflow:**
- **Phase 6 exit criteria (Wave 1):** p3-briefing.md must include Depth Distribution Analysis, Practical Implementation Audit, Story Bank, Counterpoint Discovery, and takeaway requirements
- **Phase 8 exit criteria (Wave 2):** content_plan.md must include Structure Map, Mode-Switching, Signposting, Depth Budget, Counterpoint Moments with assigned positions, Episode Arc
- **Phase 11 exit criteria (Wave 4/5):** metadata.md must include What You'll Learn, Timestamps, Resources with descriptions, CTA, companion resources generated

### Validating Feed
After updating feed.xml, use the `podcast-feed-validator` skill or check manually:
- Valid XML structure
- Correct file sizes (in bytes)
- Correct duration format (MM:SS or HH:MM:SS)
- RFC 2822 date format for pubDate
- All URLs accessible
- `<podcast:transcript>` tag present
- Enhanced `<content:encoded>` HTML sections present
