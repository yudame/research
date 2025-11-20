# Yudame Research

Evidence-based research and analysis across technology, health, economics, and human performance.

## Podcast

Deep dives into complex topics backed by rigorous research. Each episode synthesizes peer-reviewed studies, expert analysis, and primary sources to build frameworks for understanding important subjects.

**Feed:** https://yudame.github.io/research/podcast/feed.xml

### Recent Episodes

**Maximizing VO₂ Max and Heart Health: An Evidence-Based Guide** (34:27)
- Heart rate variability (HRV) as a master index of resilience
- Synthesizes findings from the Whitehall II cohort, behavioral modification trials, and sleep optimization research
- [Full research report](podcast/episodes/2025-11-19-cardiovascular-health-optimization/report.md)

**Stablecoin Market: Strategies and Pitfalls** (32:41)
- Analysis of stablecoin evolution from 2017-2025
- Covers the Terra/UST collapse, regulatory frameworks like the GENIUS Act, and lessons for protocol design
- [Full research report](podcast/episodes/2025-11-19-stablecoin-history/report.md)

## Research Approach

This repository documents research across multiple domains with an emphasis on:

- Peer-reviewed studies and meta-analyses over individual anecdotes
- Effect sizes and practical significance, not just statistical significance
- Distinguishing correlation from causation
- Identifying contradictory findings and areas of uncertainty
- Understanding study populations and generalizability
- Noting funding sources and potential conflicts of interest

## Topics

### Health & Performance
Evidence-based optimization of physical and cognitive performance. Research on cardiovascular health, HRV, VO₂ max, sleep optimization, exercise protocols, and supplementation strategies.

### Technology & Blockchain
Protocol design, cryptoeconomics, and decentralized systems. Analysis of stablecoins, DeFi mechanisms, consensus algorithms, and regulatory frameworks affecting crypto markets.

### Economics & Markets
Market dynamics, regulatory frameworks, and financial systems. Studies on monetary policy, market behavior, financial regulation, and economic mechanisms.

### Learning & Development
Educational frameworks for all ages based on neuroscience research. Montessori principles, memory consolidation, attention management, and evidence-based learning protocols for children and professionals.

## Repository Structure

```
research/
├── podcast/
│   ├── feed.xml                    # RSS feed
│   ├── episodes/                   # Episode audio files and research
│   │   └── YYYY-MM-DD-slug/
│   │       ├── report.md           # Full research report
│   │       ├── research/           # Source documents and links
│   │       ├── YYYY-MM-DD-slug.mp3 # Episode audio with chapters
│   │       └── *_transcript.json   # Full transcript
│   └── tools/                      # Transcription and processing tools
├── learning/                       # Educational protocols and frameworks
├── CLAUDE.md                       # Documentation for AI assistants
└── index.html                      # Landing page
```

## Research Methodology

When conducting research for episodes:

1. **Prioritize authoritative sources:** Peer-reviewed studies, meta-analyses, regulatory documents, official data
2. **Evaluate methodology:** Study design, sample size, control groups, potential biases
3. **Report effect sizes:** Practical significance matters more than p-values
4. **Note limitations:** Study populations, generalizability, contradictory findings
5. **Identify conflicts:** Funding sources, industry relationships, potential incentives
6. **Cite specific studies:** Enable verification and deeper exploration

## Contributing

This is a personal research repository. Episodes are created using:
1. Deep research with AI tools (Grok, ChatGPT, Claude)
2. NotebookLM for audio generation
3. Local Whisper for transcription
4. Manual chapter creation based on transcript analysis

See `.claude/skills/new-podcast-episode.md` for the complete workflow.

## License

Research reports and analysis are shared for educational purposes. Source materials retain their original licenses.
