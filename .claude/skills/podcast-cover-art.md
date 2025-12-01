# Podcast Cover Art Generation

You are helping generate cover art for a podcast episode with AI and apply podcast branding.

## Task

Generate episode cover art using Gemini via OpenRouter, then add podcast branding (logo, text, border).

## Required Information

You will receive:
- **Episode path:** Full path to episode directory
- **Episode title:** Title for the episode
- **Series name:** (Optional) Series name if this is part of a series
- **Episode number/topic:** For text overlay (e.g., "Ep 3 - Sleep & Memory")

## Workflow

### Step 1: Generate Base Cover Art with AI

Run the cover art generation script:

```bash
cd ~/src/research/podcast/tools

# Generate cover art from report.md (recommended - auto-analyzes content)
python generate_cover.py ../episodes/EPISODE_PATH --auto

# OR use custom prompt if user provides one
python generate_cover.py ../episodes/EPISODE_PATH --prompt "Custom prompt here"

# Optional: specify aspect ratio (default: 1:1)
python generate_cover.py ../episodes/EPISODE_PATH --auto --aspect-ratio "1:1"
```

**generate_cover.py features:**
- Uses OpenRouter API with Google Gemini 3 Pro Image model (requires OPENROUTER_API_KEY environment variable)
- Auto-generates prompts by analyzing report.md content
- Automatically enforces dark navy/blue color theme throughout the image
- Automatically blocks unwanted text, icons, logos, and annotations
- Supports multiple aspect ratios: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 21:9
- Outputs to `cover.png` in the episode directory
- Logs all prompts to `prompts.md` for reproducibility

### Step 2: Add Podcast Branding

Apply branding overlay to the generated cover:

```bash
cd ~/src/research/podcast/tools

# For series episodes (with series and episode text)
python add_logo_watermark.py ../episodes/EPISODE_PATH/cover.png \
  --position top-left \
  --brand "Yudame Research" \
  --series "SERIES_NAME" \
  --episode "EPISODE_TEXT" \
  --border 20 \
  --border-color "#FFC20E"

# For standalone episodes (no series text)
python add_logo_watermark.py ../episodes/EPISODE_PATH/cover.png \
  --position top-left \
  --brand "Yudame Research" \
  --episode "EPISODE_TEXT" \
  --border 20 \
  --border-color "#FFC20E"
```

**add_logo_watermark.py features:**
- Adds yellow "A" logo (from `podcast/cover.png`) to specified position
- Adds text overlays: brand name, series name (optional), episode info
- Series text uses BIGGER font (6.5% of image width) to be prominent
- Episode text uses SMALLER font (5% of image width) to handle long topic names
- Series text is optional - omit `--series` for standalone episodes
- Adds yellow border (#FFC20E) matching logo color
- Recommended border width: 20px (15-25px range)
- Logo positioned top-left with brand text beside it
- Series/episode text positioned below logo with proper margin
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
- Position: top-left
- Brand: Yudame Research
- Series: [Series name if applicable]
- Episode: [Episode text]
- Border: 20px, #FFC20E

**Date:** YYYY-MM-DD
```

## Cover Art Specifications

- Base size: 1024x1024px (or custom aspect ratio)
- With 20px border: 1064x1064px total (for 1:1)
- Color scheme: Dark navy/blue dominant, teal/white/silver accents
- File size: ~500KB PNG format
- Clean abstract visualization without text from AI

## First-Time Setup (if needed)

If the user hasn't set up cover art generation tools yet:

```bash
cd ~/src/research/podcast/tools
pip install requests  # Only dependency needed
export OPENROUTER_API_KEY='your-api-key'  # Add to ~/.zshrc or ~/.bashrc
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
