# Cover Art Generation

This document describes the cover art pipeline for generating AI artwork and applying consistent podcast branding.

## Overview

The cover art pipeline has two stages:

1. **Generation** - AI creates base image from prompt
2. **Branding** - Apply Yudame logo, text, and border

---

## Image Specifications

### Dimensions

| Purpose | Minimum | Recommended |
|---------|---------|-------------|
| Channel cover | 1400x1400 px | 3000x3000 px |
| Episode cover | 1400x1400 px | 3000x3000 px |

Apple Podcasts requires minimum 1400x1400 pixels.

### Format

- **Format:** PNG or JPEG
- **Color space:** RGB
- **Aspect ratio:** 1:1 (square)
- **File size:** Under 500KB preferred

---

## Stage 1: Image Generation

### AI Model

- **Model:** Google Gemini 3 Pro Image
- **Provider:** OpenRouter API
- **API Key:** OPENROUTER_API_KEY

### Visual Theme Requirements

All generated images must follow these guidelines:

**Color Palette:**
- Primary: Dark navy/blue backgrounds
- Accent: Yellow (#FFC20E) for Yudame brand
- Avoid: Bright backgrounds, clashing colors

**Style:**
- Minimalist, contemporary
- Sophisticated modernism
- Abstract or conceptual imagery
- Negative space emphasis

**Forbidden Elements:**
- Text in generated image (added during branding)
- Logos in generated image (added during branding)
- Literal microphones or podcast equipment
- Stock photo aesthetics
- Busy or cluttered compositions

### Prompt Generation

Two approaches for generating prompts:

**Auto-Generation (Preferred):**
- Analyze report.md content
- Extract key themes and concepts
- Generate visual metaphor prompt
- Enforce color and style guidelines

**Custom Prompt:**
- User provides specific prompt
- Must still follow visual theme requirements
- Review prompt for forbidden elements

### Prompt Structure

```
Create a [style] image depicting [concept].
Visual style: minimalist, contemporary, sophisticated
Color palette: dark navy blue background, [accent colors]
Composition: [specific composition guidance]
Mood: [emotional tone]
Do not include any text, logos, or literal objects.
```

---

## Stage 2: Branding Application

### Brand Elements

| Element | Specification |
|---------|---------------|
| Logo | Yellow "A" icon (#FFC20E) |
| Logo position | Top-left (default) |
| Logo size | 10% of image width (default) |
| Border | Yellow (#FFC20E), 20px (default) |

### Text Overlay

**For Series Episodes:**
- Series name: Larger font (6.5% of width)
- Episode number: Smaller font (5% of width)
- Position: Bottom area
- Color: White or yellow on dark backgrounds

**For Standalone Episodes:**
- Episode title may be added
- Keep minimal for legibility at small sizes

### Logo Placement Options

| Position | Use Case |
|----------|----------|
| top-left | Default, most common |
| top-right | Alternative |
| bottom-left | If top conflicts with image |
| bottom-right | Alternative |

### Branding Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| Logo opacity | 100% | Transparency level |
| Logo size | 10% | Relative to image width |
| Border width | 20px | Yellow border thickness |
| Border color | #FFC20E | Yudame yellow |

---

## Channel vs Episode Cover Art

### Channel Cover

- **File:** `podcast/cover.png`
- **Purpose:** Default image for podcast feed
- **Content:** General podcast branding
- **Updates:** Rarely changed

### Episode Cover

- **File:** `episode-directory/cover.png`
- **Purpose:** Episode-specific image
- **Content:** Reflects episode topic
- **Updates:** Created for each episode

---

## Output Files

| File | Location | Purpose |
|------|----------|---------|
| base_cover.png | Temporary | Raw AI output |
| cover.png | Episode directory | Final branded image |

---

## Visual Identity Guidelines

### Brand Colors

| Color | Hex | Use |
|-------|-----|-----|
| Yudame Yellow | #FFC20E | Logo, border, accents |
| Dark Navy | Variable | Image backgrounds |
| White | #FFFFFF | Text on dark backgrounds |

### Typography (Text Overlays)

- Series text: Bold, clean sans-serif
- Episode text: Regular weight
- Minimum legible size at 100x100 px display

### Scalability Requirements

Cover art must be legible at:
- 3000x3000 px (full resolution)
- 1400x1400 px (Apple minimum)
- 600x600 px (medium display)
- 100x100 px (thumbnail)

Test at all sizes before finalizing.

---

## Quality Assurance Checklist

Before finalizing cover art:

- [ ] Image is exactly 1:1 aspect ratio
- [ ] Minimum 1400x1400 px resolution
- [ ] Dark navy/blue background
- [ ] No AI-generated text in image
- [ ] Yudame logo properly placed
- [ ] Yellow border applied
- [ ] Series/episode text readable (if applicable)
- [ ] Image legible at 100x100 px
- [ ] File size under 500KB
- [ ] PNG or JPEG format
- [ ] RGB color space

---

## Troubleshooting

### Generation Issues

**Problem:** API returns error or timeout
**Solution:** Check OPENROUTER_API_KEY, verify API credits, retry with simpler prompt

**Problem:** Generated image doesn't match theme
**Solution:** Add more specific style guidance to prompt, explicitly forbid unwanted elements

**Problem:** Image contains text
**Solution:** Explicitly add "no text" to prompt, regenerate

### Branding Issues

**Problem:** Logo placement obscures important image content
**Solution:** Use alternative position (top-right, bottom-left)

**Problem:** Text overlay is illegible
**Solution:** Increase text size, add text shadow, adjust position

**Problem:** Colors clash with image
**Solution:** Dark backgrounds should be consistent with navy theme

---

## Prompt Examples

### Abstract Concept (Research Topic)

```
Create a minimalist abstract image representing the concept of
spaced repetition and memory formation. Visual style: contemporary,
sophisticated. Color palette: deep navy blue background with
subtle gold accents. Composition: geometric patterns suggesting
neural pathways and time intervals. Mood: intellectual, contemplative.
Do not include any text, logos, microphones, or literal objects.
```

### Series Identity

```
Create an abstract image for a podcast series about cardiovascular
health. Visual style: minimalist, modern. Color palette: dark blue
background with organic flowing shapes in warm coral tones.
Composition: suggests flow and rhythm without being literal.
Mood: vitality, precision, scientific.
Do not include hearts, medical imagery, or text.
```

### Technical Topic

```
Create an abstract visualization of digital infrastructure and
connectivity. Visual style: contemporary, geometric. Color palette:
deep navy with electric blue and gold linear elements.
Composition: network-like patterns with depth and dimensionality.
Mood: forward-looking, precise, technological.
Do not include any text, logos, or literal technology icons.
```

---

## Integration with Episode Workflow

Cover art generation occurs in Phase 8 of the episode workflow:

1. Report.md must be complete
2. Auto-generate prompt from report content
3. Generate base image via AI
4. Apply branding (logo, text, border)
5. Verify at multiple sizes
6. Save as cover.png in episode directory
7. Log prompt to logs/prompts.md
