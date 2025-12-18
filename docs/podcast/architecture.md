# System Architecture

This document describes the technical architecture of the Yudame Research Podcast system.

## High-Level Overview

The podcast system consists of four main subsystems:

1. **Research Pipeline** - Multi-source AI research and synthesis
2. **Audio Pipeline** - Transcription, chapters, and encoding
3. **Asset Pipeline** - Cover art generation and branding
4. **Publishing Pipeline** - Feed generation and deployment

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PODCAST SYSTEM                                │
├─────────────────┬─────────────────┬─────────────────┬───────────────┤
│                 │                 │                 │               │
│    RESEARCH     │     AUDIO       │     ASSET       │   PUBLISHING  │
│    PIPELINE     │    PIPELINE     │    PIPELINE     │   PIPELINE    │
│                 │                 │                 │               │
│  ┌───────────┐  │  ┌───────────┐  │  ┌───────────┐  │ ┌───────────┐ │
│  │ Perplexity│  │  │  FFmpeg   │  │  │  Gemini   │  │ │ feed.xml  │ │
│  │  Gemini   │  │  │  Whisper  │  │  │  OpenRouter│  │ │  GitHub   │ │
│  │GPT-Resrch │  │  │  Claude   │  │  │  Pillow   │  │ │  Pages    │ │
│  │  Claude   │  │  └───────────┘  │  └───────────┘  │ └───────────┘ │
│  │   Grok    │  │                 │                 │               │
│  └───────────┘  │                 │                 │               │
│        │        │        │        │        │        │       │       │
│        ▼        │        ▼        │        ▼        │       ▼       │
│   report.md     │   .mp3 file     │   cover.png     │   Live Feed   │
│                 │                 │                 │               │
└─────────────────┴─────────────────┴─────────────────┴───────────────┘
```

---

## Component Architecture

### Research Pipeline

The research pipeline aggregates information from multiple AI sources, cross-validates findings, and synthesizes them into a narrative report.

**Components:**

| Component | Purpose | Output |
|-----------|---------|--------|
| Perplexity | Academic research | p2-perplexity.md |
| Gemini Deep Research | Policy/regulatory | p2-gemini.md |
| GPT-Researcher | Technical deep-dive | p2-chatgpt.md |
| Claude (manual) | Synthesis/analysis | p2-manual.md |
| Grok (manual) | Real-time/regional | p2-grok.md |
| Cross-Validator | Source verification | cross-validation.md |
| Synthesis Agent | Narrative creation | report.md |

**Data Flow:**

```
Topic Brief (p1-brief.md)
         │
         ▼
┌────────────────────────────────────────┐
│     PARALLEL RESEARCH EXECUTION        │
│                                        │
│  Perplexity ──┬── Gemini ──┬── GPT-R  │
│               │            │           │
│  Claude ──────┴── Grok ────┘           │
└────────────────────────────────────────┘
         │
         ▼
   research-results.md (compiled)
         │
         ▼
   cross-validation.md (verification)
         │
         ▼
   p3-briefing.md (organized synthesis)
         │
         ▼
   report.md (final narrative)
```

### Audio Pipeline

The audio pipeline handles all audio processing from source file to final MP3 with embedded metadata.

**Components:**

| Component | Purpose | Tool |
|-----------|---------|------|
| Converter | M4A to MP3 | FFmpeg |
| Transcriber | Speech-to-text | Whisper (local) |
| Chapter Generator | Topic segmentation | Claude |
| Embedder | Metadata insertion | FFmpeg |

**Data Flow:**

```
source.m4a (from NotebookLM)
         │
         ▼
    ┌─────────┐
    │ FFmpeg  │  Convert to 128kbps MP3
    └────┬────┘
         │
         ▼
    YYYY-MM-DD-slug.mp3 (initial)
         │
         ▼
    ┌─────────┐
    │ Whisper │  Local transcription
    └────┬────┘
         │
         ▼
    _transcript.json (~400KB)
         │
         ▼
    ┌─────────┐
    │ Claude  │  Analyze transcript, create chapters
    └────┬────┘
         │
         ├──────────────────┐
         ▼                  ▼
    _chapters.txt      _chapters.json
    (FFmpeg format)    (Podcasting 2.0)
         │
         ▼
    ┌─────────┐
    │ FFmpeg  │  Embed chapters into MP3
    └────┬────┘
         │
         ▼
    YYYY-MM-DD-slug.mp3 (final with chapters)
```

### Asset Pipeline

The asset pipeline generates AI cover art and applies consistent podcast branding.

**Components:**

| Component | Purpose | Tool |
|-----------|---------|------|
| Generator | Base image creation | Gemini (via OpenRouter) |
| Watermarker | Branding application | Pillow |

**Data Flow:**

```
report.md (for auto-prompt) OR custom prompt
         │
         ▼
    ┌─────────────┐
    │   Gemini    │  Generate base image
    │ (OpenRouter)│  Dark navy/blue theme
    └──────┬──────┘
           │
           ▼
    base_cover.png (raw AI output)
           │
           ▼
    ┌─────────────┐
    │   Pillow    │  Apply branding:
    │             │  - Yudame logo (#FFC20E)
    └──────┬──────┘  - Series/episode text
           │         - Yellow border
           ▼
    cover.png (final branded)
```

### Publishing Pipeline

The publishing pipeline manages the RSS feed and deploys to GitHub Pages.

**Components:**

| Component | Purpose |
|-----------|---------|
| Feed Generator | RSS 2.0 + extensions |
| Validator | Standards compliance |
| GitHub Pages | Static hosting |

**Data Flow:**

```
Episode Files (mp3, cover, chapters)
         │
         ▼
    ┌─────────────┐
    │   Gather    │  Collect metadata:
    │  Metadata   │  - File size (bytes)
    └──────┬──────┘  - Duration (MM:SS)
           │         - Chapter count
           ▼
    ┌─────────────┐
    │   Update    │  Insert new <item> block
    │  feed.xml   │  with all required elements
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │  Validate   │  Check against RSS spec
    │    Feed     │
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │    Git      │  Commit and push
    │    Push     │
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │   GitHub    │  Auto-deploy (2-3 min)
    │    Pages    │
    └──────┬──────┘
           │
           ▼
    https://research.yuda.me/podcast/feed.xml
```

---

## Directory Architecture

```
/home/user/research/
├── podcast/
│   ├── feed.xml                    # RSS feed
│   ├── cover.png                   # Channel cover art
│   ├── yudame-logo.png            # Branding asset
│   ├── subscribe.html             # Subscription page
│   ├── SUBSCRIBE.md               # Subscription instructions
│   ├── README.md                  # Podcast documentation
│   │
│   ├── episodes/                  # All episodes
│   │   ├── series-name/           # Series container
│   │   │   └── epN-topic/         # Episode directory
│   │   │       ├── research/      # Research files
│   │   │       ├── logs/          # Process logs
│   │   │       ├── report.md      # Narrative report
│   │   │       ├── cover.png      # Episode cover
│   │   │       └── *.mp3          # Audio file
│   │   └── YYYY-MM-DD-topic/      # Standalone episode
│   │
│   └── tools/                     # Processing scripts
│       ├── perplexity_deep_research.py
│       ├── gemini_deep_research.py
│       ├── gpt_researcher_run.py
│       ├── transcribe_only.py
│       ├── generate_chapters.py
│       ├── generate_cover.py
│       ├── add_logo_watermark.py
│       └── requirements.txt
│
├── .claude/
│   ├── skills/                    # Workflow definitions
│   │   ├── new-podcast-episode.md
│   │   ├── podcast-series.md
│   │   └── */SKILL.md            # Individual skills
│   ├── commands/                  # Slash commands
│   │   ├── podcast-episode.md
│   │   └── podcast-series.md
│   └── agents/                    # Specialized agents
│       └── podcast-synthesis-writer.md
│
└── docs/
    ├── podcast/                   # This documentation
    ├── design/                    # Design system
    └── RSS-specification.md       # Feed standards
```

---

## Integration Points

### External Services

| Service | Integration | Purpose |
|---------|-------------|---------|
| Perplexity API | sonar-deep-research model | Academic research |
| Google AI API | Gemini Deep Research | Policy research |
| OpenAI API | GPT models, Whisper API | Research, transcription |
| Anthropic API | Claude models | Synthesis, chapters |
| OpenRouter API | Multi-model access | Cover art generation |
| Tavily API | Search enhancement | Research augmentation |
| GitHub Pages | Static hosting | Feed and asset hosting |

### Internal Automation

| Automation | Trigger | Function |
|------------|---------|----------|
| Slash commands | User invocation | Start workflows |
| Skills | Workflow phases | Execute specific tasks |
| Agents | Workflow triggers | Autonomous processing |
| Git hooks | Push events | Deploy to GitHub Pages |

---

## Security Considerations

### API Key Management

- All API keys stored in `.env` file (gitignored)
- Keys never committed to repository
- Each tool validates key presence before execution

### Content Privacy

- Local Whisper transcription available (no data sent to APIs)
- Episode content is publicly accessible once published
- Research files may be kept private (not committed)

### Repository Access

- GitHub Pages serves public content
- Repository can be private with Pages enabled
- Feed URL is public and accessible to podcast aggregators

---

## Scaling Considerations

### Current Limits

- 8 episodes maximum (GitHub Pages file limit)
- 100 MB per file
- 1 GB total repository size

### Mitigation Strategies

- Episode purging with BFG Repo-Cleaner
- 128kbps encoding to minimize file sizes
- Transcript files in tmp/ directory (optional commit)

### Future Scaling Options

- External audio hosting (S3, Cloudflare R2)
- Database-backed feed generation
- CDN for asset delivery
