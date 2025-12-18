# Tools Reference

This document provides detailed specifications for all tools used in the podcast system.

## Overview

The podcast system uses the following categories of tools:

| Category | Tools |
|----------|-------|
| Research | Perplexity, Gemini, GPT-Researcher |
| Audio | Whisper, FFmpeg |
| Image | Gemini (OpenRouter), Pillow |
| Synthesis | Claude |

---

## Research Tools

### Perplexity Deep Research

**Purpose:** Academic research with peer-reviewed sources

**Location:** `podcast/tools/perplexity_deep_research.py`

**API:** Perplexity API (sonar-deep-research model)

**API Key:** `PERPLEXITY_API_KEY`

**Speed:** 30-120 seconds

**Strengths:**
- Peer-reviewed papers
- Meta-analyses
- Systematic reviews
- Academic citation chains

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--file` | path | - | Input file with research questions |
| `--output` | path | auto | Output file path |
| `--reasoning-effort` | choice | medium | low, medium, high |
| `--quiet` | flag | false | Suppress output |
| `--no-auto-save` | flag | false | Don't auto-save results |

**Output:** Timestamped markdown with inline citations

---

### Gemini Deep Research

**Purpose:** Policy and regulatory research

**Location:** `podcast/tools/gemini_deep_research.py`

**API:** Google Gemini Deep Research

**API Key:** `GOOGLE_AI_API_KEY`

**Speed:** 3-10 minutes (with polling)

**Strengths:**
- Policy analysis
- Regulatory frameworks
- Government documents
- Strategic context

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--file` | path | - | Input file with research questions |
| `--output` | path | auto | Output file path |
| `--stream` | flag | false | Stream output |
| `--poll-interval` | int | 30 | Seconds between status checks |
| `--max-wait` | int | 600 | Maximum wait time in seconds |
| `--quiet` | flag | false | Suppress output |
| `--no-auto-save` | flag | false | Don't auto-save results |

**Output:** Timestamped markdown with structured sections

---

### GPT-Researcher

**Purpose:** Comprehensive technical research

**Location:** `podcast/tools/gpt_researcher_run.py`

**API:** Multiple (OpenAI, Anthropic, OpenRouter, Tavily)

**API Keys:**
- `OPENAI_API_KEY` (primary)
- `ANTHROPIC_API_KEY` (alternative)
- `OPENROUTER_API_KEY` (alternative)
- `TAVILY_API_KEY` (search enhancement)

**Speed:** 6-20 minutes

**Strengths:**
- Multi-agent research
- 100+ sources in parallel
- Technical depth
- Comprehensive synthesis

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--file` | path | - | Input file with research questions |
| `--output` | path | auto | Output file path |
| `--model` | string | gpt-4o | Model specification |
| `--report-type` | choice | research | research_report, detailed_report, quick_report, deep |
| `--detailed` | flag | false | Use detailed_report type |
| `--quiet` | flag | false | Suppress output |
| `--no-auto-save` | flag | false | Don't auto-save results |

**Report Types:**

| Type | Description |
|------|-------------|
| research_report | Standard comprehensive report |
| detailed_report | Extended analysis with more depth |
| quick_report | Faster, less comprehensive |
| deep | Maximum depth research |

**Output:** Markdown report with sources

---

## Audio Tools

### Whisper Transcription

**Purpose:** Speech-to-text transcription

**Location:** `podcast/tools/transcribe_only.py`

**API:** Local Whisper (default) or OpenAI API

**API Key:** `OPENAI_API_KEY` (only for API mode)

**Speed:** Varies by model (see below)

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| input | path | required | Audio file path |
| `--model` | choice | base | tiny, base, small, medium |
| `--use-api` | flag | false | Use OpenAI API instead |
| `--output` | path | auto | Output file path |
| `--log-dir` | path | logs/ | Log directory |
| `--quiet` | flag | false | Suppress output |

**Model Comparison:**

| Model | Speed (30 min audio) | Quality | Use Case |
|-------|---------------------|---------|----------|
| tiny | ~1-2 min | Basic | Quick drafts |
| base | ~5-10 min | Good | **Recommended** |
| small | ~15-20 min | Better | Quality focus |
| medium | ~30-40 min | Best | Critical content |

**Output Format:**

```json
{
  "text": "Full transcript...",
  "segments": [
    {
      "id": 0,
      "start": 0.0,
      "end": 5.2,
      "text": "Segment text...",
      "words": [...]
    }
  ],
  "language": "en"
}
```

---

### Chapter Generator

**Purpose:** Create chapters from transcript

**Location:** `podcast/tools/generate_chapters.py`

**API:** Anthropic (Claude)

**API Key:** `ANTHROPIC_API_KEY`

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| input | path | required | Audio file path |
| `--transcript` | path | - | Existing transcript (skip transcription) |
| `--model` | choice | base | Whisper model if transcribing |
| `--claude-model` | string | claude-3-sonnet | Claude model for analysis |
| `--chunk-duration` | int | 300 | Analysis chunk size (seconds) |
| `--output` | path | auto | Output file path |
| `--log-dir` | path | logs/ | Log directory |
| `--quiet` | flag | false | Suppress output |

**Output Files:**

1. `_chapters.txt` (FFmpeg metadata format)
2. `_chapters.json` (Podcasting 2.0 format)

**Chapter Guidelines:**
- 10-15 chapters per episode
- 2-4 minutes each
- Natural topic transitions
- Descriptive titles

---

### FFmpeg (System Tool)

**Purpose:** Audio conversion and chapter embedding

**Location:** System installation

**Common Operations:**

**Convert M4A to MP3:**
```bash
ffmpeg -i input.m4a -codec:a libmp3lame -b:a 128k output.mp3 -y
```

**Embed chapters:**
```bash
ffmpeg -i input.mp3 -i chapters.txt -map_metadata 1 -codec copy output.mp3 -y
```

**Get duration:**
```bash
ffmpeg -i file.mp3 2>&1 | grep Duration
```

**Key Parameters:**

| Parameter | Description |
|-----------|-------------|
| `-codec:a libmp3lame` | Use LAME MP3 encoder |
| `-b:a 128k` | 128 kbps bitrate |
| `-map_metadata 1` | Map metadata from second input |
| `-codec copy` | Copy without re-encoding |
| `-y` | Overwrite output |

---

## Image Tools

### Cover Art Generator

**Purpose:** AI image generation

**Location:** `podcast/tools/generate_cover.py`

**API:** OpenRouter (Gemini 3 Pro Image)

**API Key:** `OPENROUTER_API_KEY`

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--auto` | flag | false | Auto-generate prompt from report.md |
| `--prompt` | string | - | Custom prompt text |
| `--model` | string | gemini-3-pro | Image model |
| `--aspect-ratio` | string | 1:1 | Output aspect ratio |
| `--output` | path | cover.png | Output file |
| `--log-dir` | path | logs/ | Log directory |
| `--quiet` | flag | false | Suppress output |

**Theme Requirements:**
- Dark navy/blue backgrounds
- Minimalist style
- No text in generated image
- No logos in generated image

**Output:** PNG image (raw, before branding)

---

### Logo Watermarker

**Purpose:** Apply branding to cover art

**Location:** `podcast/tools/add_logo_watermark.py`

**Dependencies:** Pillow

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| input | path | required | Input image |
| `--logo` | path | yudame-logo.png | Logo file |
| `--position` | choice | top-left | Logo position |
| `--opacity` | int | 100 | Logo opacity (0-100) |
| `--size` | int | 10 | Logo size (% of width) |
| `--brand` | string | - | Brand text |
| `--series` | string | - | Series text (larger font) |
| `--episode` | string | - | Episode text (smaller font) |
| `--border` | int | 20 | Border width (pixels) |
| `--border-color` | hex | #FFC20E | Border color |
| `--log-dir` | path | logs/ | Log directory |
| `--quiet` | flag | false | Suppress output |

**Position Options:**
- top-left (default)
- top-right
- bottom-left
- bottom-right

**Brand Colors:**
- Logo: Yellow (#FFC20E)
- Border: Yellow (#FFC20E)
- Text: White on dark backgrounds

**Output:** Branded PNG image

---

## Synthesis Tools

### Claude (Synthesis Agent)

**Purpose:** Transform research into narrative report

**Location:** `.claude/agents/podcast-synthesis-writer.md`

**API:** Anthropic

**API Key:** `ANTHROPIC_API_KEY`

**Input Requirements:**
- `research-briefing.md` (or p3-briefing.md)
- `research-results.md` (compiled research)

**Output:** `report.md`

**Evidence Standards:**
- Every claim cited
- Statistics include sample size, methodology
- Correlation vs causation distinguished
- Meta-analysis > RCT > observational > case study
- Contradictions presented fairly

**Report Structure:**
- Engaging narrative architecture
- Podcast-optimized accessibility
- Key takeaways
- Complete source list

---

## API Key Summary

| Key | Service | Tools |
|-----|---------|-------|
| `PERPLEXITY_API_KEY` | Perplexity | perplexity_deep_research.py |
| `GOOGLE_AI_API_KEY` | Google | gemini_deep_research.py |
| `OPENAI_API_KEY` | OpenAI | gpt_researcher_run.py, transcribe_only.py (API mode) |
| `ANTHROPIC_API_KEY` | Anthropic | generate_chapters.py, synthesis |
| `OPENROUTER_API_KEY` | OpenRouter | generate_cover.py |
| `TAVILY_API_KEY` | Tavily | gpt_researcher_run.py (search) |
| `XAI_API_KEY` | xAI | Optional for Grok |

---

## Installation Requirements

### Python Dependencies

```
openai-whisper          # Local transcription
anthropic               # Claude API
openai                  # OpenAI models
pillow                  # Image processing
gpt-researcher          # Multi-agent research
langchain-openai        # LLM integration
ddgs                    # DuckDuckGo search
```

### System Dependencies

- Python 3.12+
- FFmpeg 8.0+
- Git

### First-Time Setup (macOS)

```bash
cd podcast/tools
/Applications/Python\ 3.12/Install\ Certificates.command
pip install -r requirements.txt
```

---

## Troubleshooting

### API Errors

**Problem:** API key not found
**Solution:** Verify key is in `.env` file, check variable name

**Problem:** Rate limit exceeded
**Solution:** Wait and retry, or use different API key

**Problem:** API timeout
**Solution:** Increase timeout parameter, retry with exponential backoff

### Tool Errors

**Problem:** Whisper model download fails
**Solution:** Run certificate installation, check internet connection

**Problem:** FFmpeg command fails
**Solution:** Verify FFmpeg installed, check file paths

**Problem:** Image generation returns error
**Solution:** Check OpenRouter credits, simplify prompt

### File Errors

**Problem:** Output file not created
**Solution:** Check directory exists, verify write permissions

**Problem:** File size too large
**Solution:** Use lower bitrate (96k), or split content
