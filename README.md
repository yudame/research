# Yudame Research

Research tools and frameworks for evidence-based analysis across technology, health, economics, and human performance.

## What This Is

A personal research lab for exploring complex topics through rigorous methodology. The repository contains:

- **Research tools** - Python scripts for transcription, audio processing, cover art generation, and content publishing
- **Research outputs** - Reports, analysis, and synthesized findings on various topics
- **Podcast episodes** - AI-generated audio discussions based on research findings
- **Educational frameworks** - Learning protocols based on neuroscience research

## Research Methodology

All research follows these principles:

1. **Prioritize authoritative sources** - Peer-reviewed studies, meta-analyses, regulatory documents, official data
2. **Evaluate methodology** - Study design, sample size, control groups, potential biases
3. **Report effect sizes** - Practical significance matters more than p-values
4. **Note limitations** - Study populations, generalizability, contradictory findings
5. **Identify conflicts** - Funding sources, industry relationships, potential incentives
6. **Cite specific studies** - Enable verification and deeper exploration

## Research Domains

**Health & Performance** - Cardiovascular health, HRV, VO₂ max, sleep optimization, exercise protocols, supplementation

**Technology & Blockchain** - Protocol design, stablecoins, DeFi mechanisms, consensus algorithms, regulatory frameworks

**Economics & Markets** - Monetary policy, market dynamics, financial regulation, economic mechanisms

**Learning & Development** - Educational frameworks, Montessori principles, memory consolidation, attention management

## Podcast

Research findings are synthesized into podcast episodes using NotebookLM for AI-generated audio discussions.

**Feed:** https://research.yuda.me/podcast/feed.xml

Each episode includes:
- Full research report with citations
- Complete transcript
- Chapter markers for navigation
- Validated source links

## Repository Structure

```
research/
├── podcast/
│   ├── feed.xml                    # RSS feed
│   ├── episodes/                   # Episode files and research
│   │   └── YYYY-MM-DD-slug/
│   │       ├── prompts.md          # All prompts used
│   │       ├── research-results.md # Raw research outputs
│   │       ├── sources.md          # Validated source links
│   │       ├── report.md           # Final research report
│   │       ├── cover.png           # Episode cover art
│   │       ├── *.mp3               # Audio with chapters
│   │       └── *_transcript.json   # Full transcript
│   └── tools/                      # Processing scripts
├── learning/                       # Educational frameworks
└── index.html                      # Landing page
```

## Tools

Located in `podcast/tools/`:

- **transcribe_only.py** - Local Whisper transcription (no API needed)
- **generate_cover.py** - DALL-E 3 cover art generation
- **add_logo_watermark.py** - Brand overlay for cover images
- **generate_chapters.py** - Chapter marker generation

## License

Research reports and analysis are shared for educational purposes. Source materials retain their original licenses.
