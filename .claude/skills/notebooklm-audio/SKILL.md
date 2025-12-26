---
name: notebooklm-audio
description: "LEGACY SKILL - Manual NotebookLM web interface workflow. The primary workflow now uses notebooklm-enterprise-api for automated audio generation. Use this skill only when the API is unavailable."
---

# NotebookLM Audio Generation (Manual Fallback)

**Status:** Manual fallback - Use when NotebookLM Enterprise API is unavailable (no paid subscription).

---

## Quick Start

Generate a ready-to-paste prompt for an episode:

```bash
cd ~/src/research/podcast/tools
python notebooklm_prompt.py ../episodes/YYYY-MM-DD-slug/

# Auto-copy to clipboard (macOS):
python notebooklm_prompt.py ../episodes/YYYY-MM-DD-slug/ --copy
```

This script:
- Auto-detects episode title and series name from content_plan.md
- Verifies all 5 required files exist
- Outputs a ready-to-paste prompt (no manual substitution needed)
- Optionally copies to clipboard

---

## Manual Workflow

### Step 1: Verify Files Ready

Required files (5 total):
```
episode-directory/
├── research/p1-brief.md      # Research brief
├── research/p3-briefing.md   # Master briefing
├── report.md                 # Narrative synthesis
├── sources.md                # Validated sources
└── content_plan.md           # Episode structure guide
```

### Step 2: Generate Prompt

```bash
cd ~/src/research/podcast/tools
python notebooklm_prompt.py ../episodes/your-episode/ --copy
```

### Step 3: NotebookLM Web Interface

1. Go to https://notebooklm.google.com/
2. Create new notebook
3. Upload all 5 source files
4. Click "Audio Overview" → "Customize"
5. Paste the generated prompt
6. Settings: **Deep Dive** format, **Long** length
7. Generate and download audio (~10-15 min)

### Step 4: Process Audio

After download, use `podcast-audio-processing` skill:
```bash
# Process will: convert to mp3, transcribe, add chapters
```

---

## Prompt Template Reference

The prompt instructs NotebookLM to:

- **Follow content_plan.md** for structure, hooks, and key terms
- **Brand correctly** with "Yuda Me Research" intro/outro
- **Use proper style** - define terms, cite specifics, distinguish correlation/causation
- **Avoid issues** - no undefined jargon, no fabricated examples

The full template is embedded in `notebooklm_prompt.py` - don't duplicate it elsewhere.

---

## When API Becomes Available

Once NotebookLM Enterprise subscription is active:

1. Run `notebooklm_api.py` instead - fully automated
2. This manual skill becomes truly legacy
3. The prompt template is shared between both approaches
