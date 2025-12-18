# Yudame Research Podcast System

A self-hosted podcast publishing platform using GitHub Pages, featuring AI-powered research, automated audio processing, and standards-compliant RSS feed generation.

## System Overview

The Yudame Research Podcast is a fully automated podcast production system that:

- Aggregates research from multiple AI sources (Perplexity, Gemini, GPT-Researcher, Claude, Grok)
- Cross-validates findings across sources to ensure accuracy
- Generates narrative research reports optimized for audio consumption
- Creates AI-generated cover art with consistent branding
- Processes audio files with automatic transcription and chapter generation
- Publishes via a self-hosted RSS 2.0 feed on GitHub Pages

**Feed URL:** `https://research.yuda.me/podcast/feed.xml`

**Website:** `https://research.yuda.me/`

---

## Documentation Index

### Core Documentation

| Document | Description |
|----------|-------------|
| [Architecture](architecture.md) | System architecture, components, and data flow |
| [Episode Workflow](episode-workflow.md) | Complete 12-phase episode creation process |
| [Research Pipeline](research-pipeline.md) | Multi-source research methodology and tools |
| [Audio Processing](audio-processing.md) | Conversion, transcription, and chapter generation |
| [Cover Art](cover-art.md) | AI generation and branding application |
| [Publishing](publishing.md) | RSS feed structure and GitHub Pages deployment |
| [Series Management](series-management.md) | Planning and organizing multi-episode series |
| [File Conventions](file-conventions.md) | Directory structure and naming standards |
| [Tools Reference](tools-reference.md) | Complete tool specifications and parameters |

### Related Documentation

| Document | Description |
|----------|-------------|
| [RSS Specification](../RSS-specification.md) | Feed format standards and requirements |
| [Design System](../design/README.md) | Website design specifications |

---

## Quick Start

### Prerequisites

- Python 3.12+
- FFmpeg 8.0+
- Git
- API keys for research tools (see [Tools Reference](tools-reference.md))

### Environment Variables

```bash
# Research APIs
PERPLEXITY_API_KEY=pplx-...           # Academic research
GOOGLE_AI_API_KEY=...                 # Gemini Deep Research
OPENAI_API_KEY=sk-...                 # GPT models, Whisper API
ANTHROPIC_API_KEY=sk-ant-...          # Claude for chapters/synthesis
OPENROUTER_API_KEY=sk-or-...          # Cover art generation
TAVILY_API_KEY=tvly-...               # Enhanced search (recommended)
```

### Creating an Episode

1. **Initialize** - Create episode directory structure
2. **Research** - Run parallel research across multiple AI tools
3. **Validate** - Cross-validate sources and identify contradictions
4. **Synthesize** - Generate narrative research report
5. **Cover Art** - Generate AI cover with branding
6. **Audio** - User creates audio via NotebookLM
7. **Process** - Convert, transcribe, generate chapters
8. **Publish** - Update feed.xml and push to GitHub Pages

See [Episode Workflow](episode-workflow.md) for the complete 12-phase process.

---

## Key Features

### Multi-Source Research Pipeline

The system uses 5 parallel research tools with different strengths:

| Tool | Speed | Best For |
|------|-------|----------|
| Perplexity | 30-120s | Academic papers, meta-analyses |
| Gemini | 3-10min | Policy, regulatory frameworks |
| GPT-Researcher | 6-20min | Technical deep-dives, 100+ sources |
| Claude | Variable | Synthesis, analysis |
| Grok | Variable | Real-time data, regional context |

### Automated Audio Processing

- Local Whisper transcription (no API costs, full privacy)
- AI-powered chapter generation from transcript analysis
- Automatic chapter embedding in MP3 files
- Support for Podcasting 2.0 chapter format

### Standards-Compliant Publishing

- RSS 2.0 with iTunes and Podcasting 2.0 extensions
- Automatic validation against podcast standards
- Self-hosted on GitHub Pages (no third-party dependencies)
- Platform-agnostic subscription support

---

## Repository Constraints

| Constraint | Limit |
|------------|-------|
| Maximum episodes | 8 total |
| Per-file size | 100 MB |
| Total repository | Under 1 GB |
| Target episode size | ~30 MB (30-40 min at 128kbps) |

---

## Directory Overview

```
podcast/
├── feed.xml                 # RSS feed
├── cover.png                # Channel cover art
├── subscribe.html           # Subscription page
├── episodes/                # All published episodes
│   ├── series-name/         # Series subdirectory
│   │   └── epN-topic/       # Individual episode
│   └── standalone/          # Non-series episodes
└── tools/                   # Python processing scripts
```

See [File Conventions](file-conventions.md) for complete structure details.

---

## Workflow Entry Points

### Slash Commands

- `/podcast-episode [topic]` - Create a single episode
- `/podcast-series [topic-area]` - Plan a multi-episode series

### Skills

- `podcast-audio-processing` - Process audio files
- `podcast-cover-art` - Generate and brand cover art
- `podcast-feed-validator` - Validate RSS feed
- `perplexity-deep-research` - Academic research
- `gemini-deep-research` - Policy research
- `gpt-researcher` - Technical research
- `podcast-synthesis-writer` - Generate narrative report

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Hosting | GitHub Pages |
| Feed Format | RSS 2.0 + iTunes + Podcasting 2.0 |
| Audio Format | MP3 (128kbps) |
| Transcription | OpenAI Whisper (local) |
| Research | Perplexity, Gemini, GPT-Researcher |
| Cover Art | Gemini via OpenRouter |
| Automation | Claude Code skills and agents |
