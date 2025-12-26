---
name: podcast-cover-art
description: Generate podcast cover art with AI and apply branding. Uses Gemini via OpenRouter for image generation with light cream backgrounds, then adds Yudame Research logo and series/episode text using Playfair Display typography. Use after report.md is complete and before audio processing. Requires OPENROUTER_API_KEY.
---

# Podcast Cover Art Generation

**Skill name:** `podcast-cover-art`

You are a specialized subagent that generates podcast cover art with AI and applies podcast branding.

## How to Invoke This Skill

From the main podcast workflow, invoke this skill using the Task tool:

```
Use the Task tool with subagent_type="general-purpose" and prompt:

"Generate podcast cover art for this episode using the podcast-cover-art skill.

Episode path: podcast/episodes/2025-12-01-topic-slug
Episode title: [Full episode title]
Series name: [Series name, or "None" for standalone episodes]
Episode text: [Text for branding overlay, e.g., "Ep 3 - Sleep & Memory"]

Follow the podcast-cover-art skill to:
1. Generate AI cover art with Gemini via OpenRouter
2. Apply podcast branding (logo, text, border)
3. Log to prompts.md
4. Report back when complete with file path and size"
```

## Task

Generate episode cover art using Gemini via OpenRouter, then add podcast branding (logo, text, border).

## Required Information

You will receive:
- **Episode path:** Full path to episode directory (e.g., `podcast/episodes/2025-12-01-topic-slug`)
- **Episode title:** Full title for the episode
- **Series name:** Series name if applicable, or "None" for standalone episodes
- **Episode text:** Text for branding overlay (e.g., "Ep 3 - Sleep & Memory" or just topic)

## Workflow

### Step 1: Generate Base Cover Art with AI

Run the cover art generation script:

```bash
cd ~/src/research/podcast/tools

# Basic usage - auto-generate from report.md
python generate_cover.py ../episodes/EPISODE_PATH --auto

# With organized logging (recommended for production)
mkdir -p ../episodes/EPISODE_PATH/logs
python generate_cover.py ../episodes/EPISODE_PATH --auto \
  --log-dir ../episodes/EPISODE_PATH/logs \
  --quiet

# With custom prompt
python generate_cover.py ../episodes/EPISODE_PATH \
  --prompt "Custom prompt here" \
  --log-dir ../episodes/EPISODE_PATH/logs \
  --quiet

# With custom model and aspect ratio
python generate_cover.py ../episodes/EPISODE_PATH --auto \
  --model google/gemini-3-pro-image-preview \
  --aspect-ratio "1:1" \
  --log-dir ../episodes/EPISODE_PATH/logs \
  --quiet
```

**generate_cover.py features:**
- Uses OpenRouter API with Google Gemini 3 Pro Image model (requires OPENROUTER_API_KEY environment variable)
- Auto-generates prompts by analyzing report.md content
- Automatically enforces light cream (#F5F1E8) background with salmon (#E8B4A8) and black accents
- Automatically blocks unwanted text, icons, logos, and annotations
- Supports multiple aspect ratios: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 21:9
- Outputs to `cover.png` in the episode directory
- With `--log-dir`: Also saves metadata JSON and timestamped log file
- `--quiet`: Suppresses progress messages
- `--model`: Customize image generation model (default: google/gemini-3-pro-image-preview)
- Logs all prompts to `prompts.md` for reproducibility

### Step 2: Add Podcast Branding

Apply branding overlay to the generated cover:

```bash
cd ~/src/research/podcast/tools

# Basic usage - for series episodes
python add_logo_watermark.py ../episodes/EPISODE_PATH/cover.png \
  --series "SERIES_NAME" \
  --episode "EPISODE_TEXT"

# With organized logging (recommended for production)
python add_logo_watermark.py ../episodes/EPISODE_PATH/cover.png \
  --series "SERIES_NAME" \
  --episode "EPISODE_TEXT" \
  --log-dir ../episodes/EPISODE_PATH/logs \
  --quiet

# For standalone episodes (no series text)
python add_logo_watermark.py ../episodes/EPISODE_PATH/cover.png \
  --episode "EPISODE_TEXT" \
  --log-dir ../episodes/EPISODE_PATH/logs \
  --quiet
```

**add_logo_watermark.py features:**
- Auto-detects background brightness (light/dark) and adjusts text color accordingly
- Adds Yudame logo (from `podcast/yudame-logo.png`) inline with brand name
- Logo and "Yudame Research" vertically centered, matching website header style
- Typography: Playfair Display SemiBold (brand), Playfair Display Italic (series/episode)
- Series text is optional - omit `--series` for standalone episodes
- Logo positioned top-left with brand text beside it
- Series/episode text positioned below with proper spacing
- With `--log-dir`: Saves metadata JSON and timestamped log file
- `--quiet`: Suppresses progress messages
- Replaces original cover.png with branded version

### Step 3: Log to prompts.md

Update the episode's `prompts.md` file with the cover art generation details:

```markdown
## Cover Art Generation Phase

**Tool Used:** Gemini 3 Pro Image via OpenRouter

**Generation Method:** [--auto from report.md OR custom prompt]

**Custom Prompt (if used):**
```
[Prompt text if custom prompt was provided]
```

**Branding Applied:**
- Logo: Yudame logo (top-left, vertically centered with brand text)
- Brand: Yudame Research (Playfair Display SemiBold)
- Series: [Series name if applicable] (Playfair Display Italic)
- Episode: [Episode text] (Playfair Display Italic)

**Date:** YYYY-MM-DD
```

## Cover Art Specifications

- Base size: 1024x1024px (or custom aspect ratio)
- Color scheme: Light cream (#F5F1E8) background with salmon (#E8B4A8) and black (#000000) accents
- Typography: Playfair Display SemiBold (brand), Playfair Display Italic (series/episode)
- Text color: Auto-detected based on background brightness (black on light, white on dark)
- File size: ~500KB-1MB PNG format
- Clean abstract visualization without text from AI

## Font Check

Before applying branding, verify required fonts are installed:

```bash
cd ~/src/research/podcast/tools
python add_logo_watermark.py --check-fonts
```

Expected output:
```
✓ Playfair Display SemiBold
✓ Playfair Display Italic
✓ All required fonts are installed!
```

If fonts are missing, the script will show installation instructions.

## First-Time Setup (if needed)

If the user hasn't set up cover art generation tools yet:

```bash
cd ~/src/research/podcast/tools
pip install requests pillow  # Required dependencies

# API keys are stored in /Users/valorengels/.env (auto-loaded via ~/.zshenv)
# Verify OPENROUTER_API_KEY is set:
grep OPENROUTER_API_KEY /Users/valorengels/.env

# Install Playfair Display fonts (required for branding)
mkdir -p ~/Library/Fonts && cd ~/Library/Fonts
curl -L -o playfair.zip "https://gwfh.mranftl.com/api/fonts/playfair-display?download=zip&subsets=latin&variants=600,italic"
unzip -o playfair.zip

# Verify fonts installed correctly
cd ~/src/research/podcast/tools
python add_logo_watermark.py --check-fonts
```

## Cost Information

- OpenRouter Gemini 3 Pro Image: ~$0.30/M input tokens + $2.50/M output tokens
- Typical image generation: ~$0.05-0.10 per image
- Cover art appears in podcast apps and directories
- Each episode can have unique cover art or reuse podcast-level cover

## Error Handling

If cover art generation fails:
1. Check that OPENROUTER_API_KEY is set in environment
2. Verify report.md exists in the episode directory
3. Check network connectivity
4. If auto-generation produces poor results, ask user if they want to provide a custom prompt

## Final Report

When complete, report back:
- ✅ Cover art generated at: `episode_path/cover.png`
- Size: [dimensions] (~[filesize]KB)
- Method: [auto or custom prompt]
- Branding: Applied with series/episode text
- Logged to: `episode_path/prompts.md`
