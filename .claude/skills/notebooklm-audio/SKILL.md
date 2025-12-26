---
name: notebooklm-audio
description: "LEGACY SKILL - Manual NotebookLM web interface workflow. The primary workflow now uses notebooklm-enterprise-api for automated audio generation. Use this skill only when the API is unavailable."
---

# NotebookLM Audio Generation (Manual Fallback)

**Skill name:** `notebooklm-audio`

**Status:** Manual fallback - Use only when NotebookLM Enterprise API is unavailable.

**Primary workflow uses:** `notebooklm-enterprise-api` skill (automated via Discovery Engine API)

---

## When to Use This Skill

Use manual NotebookLM only when:
- NotebookLM Enterprise API is unavailable
- Testing or experimenting with different formats
- API authentication issues

## Files to Upload to NotebookLM

Upload these 5 files:

1. `research/p1-brief.md` (research brief)
2. `report.md` (narrative synthesis)
3. `research/p3-briefing.md` (master briefing)
4. `sources.md` (validated source links)
5. `content_plan.md` (episode structure and NotebookLM guidance)

## NotebookLM Prompt (Standard Template)

Paste this into the "Customize" field, replacing `[EPISODE TITLE]` and `[SERIES NAME]`:

```
Create a two-host podcast episode on: [EPISODE TITLE] from our [SERIES NAME] series

IMPORTANT: Follow the structure and guidance in content_plan.md - it contains:
- The opening hook to use
- Key terms to define (with pronunciations)
- Studies to emphasize
- Three-section narrative arc (Foundation → Evidence → Application)
- Closing callback and sign-off

Brand elements:
- Host: Valor Engels
- Open with: "Welcome to Yuda Me Research from our [SERIES NAME] series. I'm Valor Engels..."
- Close with: "Find full research and sources at research dot yuda dot me - that's Y-U-D-A dot M-E"

Tone: Intellectually rigorous but accessible - two experts having a genuine conversation, making complex research understandable.

Style guidelines:
- Spell out acronyms on first use: "High-Intensity Interval Training, or HIIT"
- Define technical terms before building on them
- Use specific numbers with context (sample sizes, effect sizes, percentages)
- Distinguish correlation from causation
- Make statistics meaningful through comparisons
- Include human elements when the research contains them

Avoid:
- Undefined jargon
- Fabricated examples (use only what's in the source material)
- Over-hedging that obscures findings
- Repeating context unnecessarily
```

## NotebookLM Settings

- **Format:** Deep Dive
- **Length:** Long

## Workflow

1. Go to https://notebooklm.google.com/
2. Create new notebook
3. Upload all 5 source files (p1-brief.md, report.md, p3-briefing.md, sources.md, content_plan.md)
4. Open "Audio Overview" feature
5. Paste the prompt above into the customization field
6. Select format: **Deep Dive** and length: **Long**
7. Generate audio
8. Download the generated audio file (usually .m4a or .wav)

## Post-Generation Processing

After NotebookLM generates audio, use the `podcast-audio-processing` skill to:
1. Convert to mp3 (if needed)
2. Transcribe with local Whisper
3. Generate chapters from transcript
4. Embed chapters into mp3

## Why This is a Fallback

This manual workflow is only needed when the NotebookLM Enterprise API is unavailable.

**The API approach (`notebooklm-enterprise-api`) provides:**
- Fully automated workflow (no browser interaction)
- Same audio quality as manual upload
- Programmatic control and error handling
- Integration with the episode workflow

**Use manual when:**
- API authentication fails
- Testing different NotebookLM settings
- One-off experiments
