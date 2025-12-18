# File Conventions

This document defines the directory structure, file naming standards, and organization conventions for the podcast system.

## Directory Structure

### Repository Root

```
/home/user/research/
├── podcast/                    # Podcast system root
│   ├── feed.xml               # RSS feed
│   ├── cover.png              # Channel cover art (3000x3000)
│   ├── yudame-logo.png        # Brand logo for watermarking
│   ├── subscribe.html         # Subscription page
│   ├── SUBSCRIBE.md           # Subscription instructions
│   ├── README.md              # Podcast documentation
│   ├── episodes/              # All episode content
│   └── tools/                 # Processing scripts
├── .claude/                    # Claude Code configuration
│   ├── skills/                # Workflow definitions
│   ├── commands/              # Slash commands
│   └── agents/                # Specialized agents
├── docs/                       # Documentation
│   ├── podcast/               # Podcast docs (this section)
│   ├── design/                # Design system
│   └── RSS-specification.md   # Feed standards
└── .env                        # API keys (gitignored)
```

### Episode Directory

```
podcast/episodes/
├── series-name/                # Series container
│   ├── ep1-topic-slug/        # Series episode
│   ├── ep2-topic-slug/
│   └── epN-topic-slug/
└── YYYY-MM-DD-topic-slug/      # Standalone episode
```

### Individual Episode Structure

```
episode-directory/
├── research/                   # Research files
│   ├── p1-brief.md            # Topic briefing
│   ├── p2-perplexity.md       # Academic research
│   ├── p2-gemini.md           # Policy research
│   ├── p2-chatgpt.md          # Technical research
│   ├── p2-grok.md             # Real-time research
│   ├── p2-manual.md           # Manual research
│   ├── cross-validation.md    # Source comparison
│   ├── p3-briefing.md         # Master briefing
│   └── documents/             # PDFs, papers
├── logs/                       # Process logs
│   ├── prompts.md             # All prompts used
│   └── metadata.md            # Publishing metadata
├── tmp/                        # Temporary files (optional commit)
│   └── *_transcript.json      # Large transcript files
├── report.md                   # Narrative report
├── cover.png                   # Episode cover art
├── sources.md                  # Source documentation
├── YYYY-MM-DD-slug.mp3        # Final audio
├── YYYY-MM-DD-slug_transcript.json
├── YYYY-MM-DD-slug_chapters.txt
└── YYYY-MM-DD-slug_chapters.json
```

---

## Naming Conventions

### Episode Directory Names

**Standalone Episodes:**
```
YYYY-MM-DD-topic-slug
```
- Date in ISO format
- Topic slug: lowercase, hyphenated
- Examples:
  - `2025-12-15-spaced-repetition`
  - `2025-12-18-memory-techniques`

**Series Episodes:**
```
epN-topic-slug
```
- N: Episode number (1, 2, 3...)
- Topic slug: lowercase, hyphenated
- Examples:
  - `ep1-foundations`
  - `ep2-advanced-techniques`

### Series Directory Names

```
series-name
```
- Lowercase, hyphenated
- Descriptive but concise
- Examples:
  - `cardiovascular-health`
  - `solomon-islands-telecom-series`
  - `kindergarten-first-principles`

### Audio Files

```
YYYY-MM-DD-slug.mp3
```
or for series:
```
epN-slug.mp3
```
- Match directory slug
- Always MP3 format
- Examples:
  - `2025-12-15-spaced-repetition.mp3`
  - `ep1-foundations.mp3`

### Transcript Files

```
YYYY-MM-DD-slug_transcript.json
```
or:
```
epN-slug_transcript.json
```
- Match audio file base name
- Underscore before "transcript"
- JSON format

### Chapter Files

**FFmpeg format:**
```
YYYY-MM-DD-slug_chapters.txt
```

**Podcasting 2.0 format:**
```
YYYY-MM-DD-slug_chapters.json
```
- Match audio file base name
- Underscore before "chapters"

### Cover Art

```
cover.png
```
- Always named "cover.png" in episode directory
- PNG format preferred
- 1400x1400 minimum, 3000x3000 preferred

---

## Research File Naming

### Phase-Based Naming

| File | Phase | Content |
|------|-------|---------|
| p1-brief.md | 1 | Topic briefing and questions |
| p2-perplexity.md | 2 | Perplexity academic research |
| p2-gemini.md | 4 | Gemini policy research |
| p2-chatgpt.md | 4 | GPT-Researcher output |
| p2-grok.md | 4 | Grok real-time research |
| p2-manual.md | 4 | Manual Claude research |
| cross-validation.md | 5 | Source comparison |
| p3-briefing.md | 6 | Master briefing |

### Naming Pattern

- `pN-` prefix indicates workflow phase
- Lowercase
- Hyphenated multi-word names
- `.md` extension for markdown

---

## Log Files

### prompts.md

Location: `logs/prompts.md`

Content:
- All prompts used during episode creation
- Timestamps for each prompt
- Tool/model used
- Response summaries (optional)

### metadata.md

Location: `logs/metadata.md`

Content:
- File sizes
- Durations
- Publishing metadata
- Scratch notes

---

## Git Conventions

### Gitignored Files

These files are not committed:

| Pattern | Reason |
|---------|--------|
| `.env` | Contains API keys |
| `*.m4a` | Source audio (large) |
| `tmp/` | Temporary files |

### Large File Handling

To minimize repository size:

- Commit only final MP3 (not source M4A)
- Optionally keep transcripts in tmp/
- Target ~30 MB per episode audio
- Remove old episodes if approaching limits

---

## URL Conventions

### Base URL

```
https://research.yuda.me/
```

### Feed URL

```
https://research.yuda.me/podcast/feed.xml
```

### Episode Asset URLs

**Standalone episode:**
```
https://research.yuda.me/podcast/episodes/YYYY-MM-DD-slug/[file]
```

**Series episode:**
```
https://research.yuda.me/podcast/episodes/series-name/epN-slug/[file]
```

### URL Components

| File | URL Pattern |
|------|-------------|
| Audio | `.../YYYY-MM-DD-slug.mp3` |
| Cover | `.../cover.png` |
| Chapters | `.../_chapters.json` |
| Report | `.../report.md` |

---

## File Size Guidelines

| File Type | Target Size | Maximum |
|-----------|-------------|---------|
| Audio (MP3) | ~30 MB | 100 MB |
| Cover art | ~500 KB | 2 MB |
| Transcript | ~400 KB | 1 MB |
| Report | ~20 KB | 50 KB |
| Chapters | ~1 KB | 5 KB |

### Repository Limits

| Metric | Limit |
|--------|-------|
| Total episodes | 8 |
| Per-file size | 100 MB |
| Repository total | 1 GB |

---

## Examples

### Standalone Episode

```
podcast/episodes/2025-12-15-spaced-repetition/
├── research/
│   ├── p1-brief.md
│   ├── p2-perplexity.md
│   ├── p2-gemini.md
│   ├── p2-chatgpt.md
│   ├── cross-validation.md
│   └── p3-briefing.md
├── logs/
│   └── prompts.md
├── report.md
├── cover.png
├── 2025-12-15-spaced-repetition.mp3
├── 2025-12-15-spaced-repetition_transcript.json
├── 2025-12-15-spaced-repetition_chapters.txt
└── 2025-12-15-spaced-repetition_chapters.json
```

### Series Episode

```
podcast/episodes/cardiovascular-health/ep2-vo2-max/
├── research/
│   ├── p1-brief.md
│   ├── p2-perplexity.md
│   ├── p2-gemini.md
│   ├── p2-chatgpt.md
│   ├── cross-validation.md
│   └── p3-briefing.md
├── logs/
│   └── prompts.md
├── report.md
├── cover.png
├── ep2-vo2-max.mp3
├── ep2-vo2-max_transcript.json
├── ep2-vo2-max_chapters.txt
└── ep2-vo2-max_chapters.json
```

---

## Validation Checklist

Before publishing, verify:

- [ ] Directory name follows convention
- [ ] Audio file name matches directory slug
- [ ] All research files use p-prefix naming
- [ ] Transcript file uses underscore prefix
- [ ] Chapter files use underscore prefix
- [ ] Cover art named `cover.png`
- [ ] Report named `report.md`
- [ ] No spaces in file/directory names
- [ ] All lowercase (except README.md)
