# Personal Podcast Feed

A simple self-hosted podcast feed using GitHub Pages.

## Episode Creation Workflow

```mermaid
flowchart TD
    Start([Start New Episode]) --> P1[Phase 1: Setup<br/>Create directory & files]

    P1 --> P2[Phase 2: Perplexity Research<br/>Academic foundation<br/>🤖 Automated - 30-120s]

    P2 --> P3[Phase 3: Question Discovery<br/>Analyze results, identify gaps<br/>🤖 Automated]

    P3 --> P4{Phase 4: Targeted Research<br/>ALL 4 TOOLS}

    P4 -->|Automated| P4a[GPT-Researcher<br/>Industry/technical<br/>🤖 6-20 min]
    P4 -->|Automated| P4b[Gemini Deep Research<br/>Policy/regulatory<br/>🤖 3-10 min]
    P4 -->|Manual| P4c[Claude Research<br/>Comprehensive synthesis<br/>👤 User pastes from claude.ai]
    P4 -->|Manual| P4d[Grok Research<br/>Real-time/regional<br/>👤 User pastes from x.com]

    P4a --> P5
    P4b --> P5
    P4c --> P5
    P4d --> P5

    P5[Phase 5: Cross-Validation<br/>Verify sources, find contradictions<br/>🤖 Automated]

    P5 --> P6[Phase 6: Master Briefing<br/>Create p3-briefing.md<br/>🤖 Automated]

    P6 --> P7[Phase 7: Synthesis<br/>Generate report.md<br/>🤖 Automated via agent]

    P7 --> P8[Phase 8: Cover Art<br/>AI generation + branding<br/>🤖 Automated]

    P7 --> P9[Phase 9: NotebookLM Audio<br/>User generates audio<br/>👤 Manual - User Task]

    P8 --> P10
    P9 --> P10[Phase 10: Audio Processing<br/>Convert, transcribe, chapters<br/>🤖 Automated]

    P10 --> P11[Phase 11: Publishing<br/>Update feed.xml<br/>🤖 Automated]

    P11 --> P12[Phase 12: Git Push<br/>🚨 CRITICAL - Deploy live<br/>🤖 Automated]

    P12 --> Verify{Verify Live?<br/>Check feed.xml}

    Verify -->|✅ Success| Done([Episode Live!])
    Verify -->|❌ Failed| P12

    style P12 fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px
    style P9 fill:#ffd93d,stroke:#f59f00
    style P4a fill:#ffd93d,stroke:#f59f00
    style Done fill:#51cf66,stroke:#2f9e44
```

## Research Tool Selection

**🚨 DEFAULT: USE ALL 5 TOOLS FOR EVERY EPISODE**

```mermaid
flowchart TD
    Start([Every Episode<br/>Uses All 5 Tools]) --> Phase1[1. Perplexity<br/>Academic Foundation<br/>🤖 Automated - 30-120s]

    Phase1 --> Phase3{2-5. Targeted Research<br/>ALL 4 TOOLS}

    Phase3 --> Tool1[2. GPT-Researcher<br/>Industry/Technical<br/>🤖 Automated - 6-20 min]
    Phase3 --> Tool2[3. Gemini<br/>Policy/Regulatory<br/>🤖 Automated - 3-10 min]
    Phase3 --> Tool3[4. Claude<br/>Comprehensive Synthesis<br/>👤 Manual - claude.ai]
    Phase3 --> Tool4[5. Grok<br/>Real-Time/Regional<br/>👤 Manual - x.com/i/grok]

    style Phase1 fill:#4dabf7,stroke:#1971c2,stroke-width:2px
    style Tool1 fill:#4dabf7,stroke:#1971c2
    style Tool2 fill:#4dabf7,stroke:#1971c2
    style Tool3 fill:#ffd93d,stroke:#f59f00
    style Tool4 fill:#ffd93d,stroke:#f59f00
    style Phase3 fill:#51cf66,stroke:#2f9e44,stroke-width:3px
```

**Rare exceptions:** Only skip a tool if its focus area is truly irrelevant to the topic.

## File Organization

```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/                    # Research organized by phase
│   ├── p1-brief.md             # Initial research brief
│   ├── p2-perplexity.md        # Academic research
│   ├── p2-chatgpt.md           # Industry/technical (GPT-Researcher)
│   ├── p2-gemini.md            # Policy/regulatory
│   ├── p2-claude.md            # Comprehensive synthesis (manual)
│   ├── p2-grok.md              # Real-time/regional (manual)
│   ├── p3-briefing.md          # Cross-validated synthesis
│   └── documents/              # PDFs, papers
├── logs/                        # Process logs
│   ├── prompts.md              # All prompts used
│   └── metadata.md             # Publishing metadata
├── tmp/                         # Temporary files
│   └── *_transcript.json       # Full Whisper output
├── cover.png                    # Episode cover art
├── report.md                    # Final narrative report
├── sources.md                   # Source documentation
├── YYYY-MM-DD-slug.mp3         # Final audio with chapters
└── YYYY-MM-DD-slug_chapters.json
```

---

## Quick Start

### Adding a New Episode

Use the automated workflow via Claude Code:
```
/podcast-episode
```

Or follow the `.claude/skills/new-podcast-episode.md` workflow manually.

### Manual Publishing (Legacy)

1. **Create your MP3 file** using your preferred audio tools
2. **Name it**: `YYYY-MM-DD-title-slug.mp3` (e.g., `2025-01-19-intro-to-math.mp3`)
3. **Add to episodes folder**: Drop the file into `podcast/episodes/`
4. **Update feed.xml**:
   - Copy an existing `<item>` block
   - Update: title, description, pubDate, file URL, file size, duration, guid
5. **Check episode count**: If more than 8 episodes exist:
   - Delete oldest MP3 from `episodes/`
   - Remove oldest `<item>` from feed.xml
   - Purge from git history (see below)
6. **Commit and push**

### Purging Old Episodes from Git History

When you delete an episode, remove it from git history to save space:

```bash
# Install BFG Repo-Cleaner (one-time setup)
brew install bfg

# Purge the old file
bfg --delete-files "old-episode.mp3" .git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

### Subscribe to Your Feed

Once GitHub Pages is enabled, subscribe to:
```
https://research.yuda.me/podcast/feed.xml
```

## Limits

- Maximum 8 episodes at a time
- Each file must be under 100 MB
- Repository should stay under 1 GB total

## File Sizes

For reference, typical podcast bitrates:
- 64 kbps = ~29 MB per hour
- 96 kbps = ~43 MB per hour
- 128 kbps = ~58 MB per hour (recommended)

## Legend

- 🤖 **Automated** - Claude Code handles this automatically
- 👤 **Manual** - User action required
- 🚨 **Critical** - Must not be skipped
