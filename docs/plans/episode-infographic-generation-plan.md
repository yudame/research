# Episode Infographic Generation Plan

**Date:** 2026-02-10
**Purpose:** Systematize creation of high-quality branded infographics for every podcast episode

---

## Success Criteria (Based on Episode 3)

**What worked in the Episode 3 portrait infographic:**
- ✅ Clean visual hierarchy (header → protocols → takeaways)
- ✅ Generous white space with gray section dividers
- ✅ Consistent icon style (simple line art)
- ✅ Strong hook at top (89% stat)
- ✅ Numbered protocols (1-5) with icons
- ✅ Scannable in 10-15 seconds
- ✅ Professional color palette
- ✅ Readable at standard size (8.5"x11")

**What could be improved:**
- ⚠️ Branding integration (Yudame logo, exact colors)
- ⚠️ Typography (use Playfair Display + Inter)
- ⚠️ Color consistency (use exact Yudame salmon, cream, black)
- ⚠️ Icon style (match 2px stroke weight specification)

---

## Yudame Branding Requirements (LOCKED)

### Colors (Exact Hex Values)
```
Primary:
- Salmon: #E8B4A8 (accent, large numbers, icons)
- Cream: #F5F1E8 (section backgrounds, alternate bands)
- Black: #000000 (text, borders, icons)
- White: #FFFFFF (card backgrounds, main background)

Supporting Grays:
- #F5F5F5 (subtle backgrounds)
- #E5E5E5 (dividers, section separators)
- #6B6B6B (secondary text, metadata)
- #3A3A3A (body text on colored backgrounds)
```

**Usage rules:**
- Salmon: Large stat numbers, protocol numbers, active elements
- Cream: Section backgrounds (alternating bands)
- Black: All body text, headlines, default icons
- White: Main background, card backgrounds

### Typography (Exact Fonts)
```
Headlines:
- Font: Playfair Display
- Weight: 600 (Semibold)
- Sizes: 32px (title), 24px (section headers), 18px (protocol titles)

Body Text:
- Font: Inter
- Weight: 400 (Regular) for descriptions, 500 (Medium) for labels
- Sizes: 14px (body), 12px (metadata), 10px (footer)

Technical/Data:
- Font: IBM Plex Mono (optional for timestamps/stats)
- Weight: 400
- Size: 12px
```

### Icon Style (LOCKED)
```
Stroke weight: 2px (NEVER 1px or 3px)
Style: Outlined, never filled
Color: Black (#000000) default, Salmon (#E8B4A8) for emphasis
Sizes: 32px for protocols, 24px for smaller elements
Corner radius: 2px on rounded elements
```

### Logo Placement
```
Bottom left or center:
- Wordmark: "Yudame Research"
- Font: Playfair Display, 14px, weight 600
- Color: Black (#000000)
- Optional tagline: "Be the most prepared person in the room." (Inter, 10px, #6B6B6B)

OR

- Full logo mark (if available)
- Height: 24-32px
- Placement: Bottom left with 16px margin
```

---

## Infographic Structure (Template)

### Format Specifications
```
Orientation: Portrait
Size: 1080px × 1920px (Instagram/social media optimized)
      OR 2550px × 3300px (print quality, 8.5" × 11" at 300 DPI)
Margins: 48px on all sides
Background: White (#FFFFFF)
```

### Layout Structure (Top to Bottom)

```
┌─────────────────────────────────────────┐
│ HEADER SECTION (15%)                    │
│ - Episode series label (Inter 12px)    │
│ - Episode title (Playfair 32px)        │
│ - Key stat/hook (Salmon 48px number)   │
│ - Subtitle/thesis (Inter 14px)         │
│ Background: White or Cream              │
└─────────────────────────────────────────┘
│ DIVIDER (Gray #E5E5E5, 2px)            │
┌─────────────────────────────────────────┐
│ PROTOCOLS/CONTENT SECTION (65%)        │
│                                         │
│ ┌─ Protocol 1 ─────────────────────┐  │
│ │ [Icon] 1. Title                   │  │
│ │ Description (2-3 lines max)       │  │
│ └───────────────────────────────────┘  │
│   ↓ 16px spacing                        │
│ ┌─ Protocol 2 ─────────────────────┐  │
│ │ [Icon] 2. Title                   │  │
│ │ Description                        │  │
│ └───────────────────────────────────┘  │
│                                         │
│ (Repeat for 3-5 protocols)             │
│                                         │
│ Alternating backgrounds:                │
│ - Odd rows: White (#FFFFFF)            │
│ - Even rows: Cream (#F5F1E8)           │
└─────────────────────────────────────────┘
│ DIVIDER (Gray #E5E5E5, 2px)            │
┌─────────────────────────────────────────┐
│ TAKEAWAYS SECTION (15%)                │
│ "3 Critical Takeaways"                  │
│                                         │
│ [Icon] 1. Takeaway title               │
│        One-line description             │
│                                         │
│ [Icon] 2. Takeaway title               │
│        One-line description             │
│                                         │
│ [Icon] 3. Takeaway title               │
│        One-line description             │
│                                         │
│ Background: Cream (#F5F1E8)            │
└─────────────────────────────────────────┘
│ DIVIDER (Gray #E5E5E5, 2px)            │
┌─────────────────────────────────────────┐
│ FOOTER (5%)                             │
│ [Yudame Logo] research.yuda.me/podcast │
│ Background: White                       │
└─────────────────────────────────────────┘
```

---

## Detailed Component Specifications

### Header Section
```
Spacing from top: 48px
Series label:
  - Text: "Algorithms for Life: Episode 3" or "[Series Name]: Ep. [N]"
  - Font: Inter, 12px, weight 500, color #6B6B6B
  - Letter spacing: 0.05em
  - Text transform: uppercase

Episode title:
  - Margin top: 8px
  - Font: Playfair Display, 32px, weight 600, color #000000
  - Line height: 1.2
  - Max width: 80% of container
  - Center aligned

Hook statistic (if applicable):
  - Margin top: 16px
  - Number: Playfair Display, 48px, weight 600, color #E8B4A8
  - Context text below: Inter, 14px, color #3A3A3A
  - Example: "89%" (salmon) / "of delegation failures are attitudinal" (gray)

Thesis statement:
  - Margin top: 12px
  - Font: Inter, 14px, weight 400, color #3A3A3A
  - Line height: 1.5
  - Max width: 85% of container
  - Center aligned
  - Max 2 lines
```

### Protocol/Content Cards
```
Container:
  - Width: 100% minus 48px margins each side
  - Padding: 20px
  - Border radius: 8px
  - Box shadow: 0 2px 4px rgba(0,0,0,0.06) (optional, subtle)
  - Margin bottom: 12px

Alternating backgrounds:
  - Card 1, 3, 5: White (#FFFFFF)
  - Card 2, 4: Cream (#F5F1E8)

Layout (horizontal):
  - Icon: 32px, left aligned, 2px stroke
  - Number: Salmon (#E8B4A8), Playfair 24px, weight 600, right of icon
  - Gap between icon and number: 12px
  - Title: Black (#000000), Inter 16px, weight 500, right of number
  - Gap between number and title: 8px

Description:
  - Margin top: 8px
  - Margin left: 52px (align with title, clear of icon/number)
  - Font: Inter, 14px, weight 400, color #3A3A3A
  - Line height: 1.5
  - Max 2-3 lines
```

### Takeaways Section
```
Background: Cream (#F5F1E8)
Padding: 24px 48px

Section title:
  - Font: Playfair Display, 22px, weight 600, color #000000
  - Margin bottom: 16px
  - Center aligned

Takeaway items:
  - Layout: Icon + text, horizontal
  - Icon: 24px, black, 2px stroke
  - Gap after icon: 12px
  - Title: Inter, 14px, weight 500, color #000000
  - Description: Inter, 12px, weight 400, color #3A3A3A
  - Margin top: 8px under title
  - Spacing between items: 16px
```

### Footer Section
```
Background: White (#FFFFFF)
Padding: 16px 48px
Border top: 1px solid #E5E5E5

Layout (horizontal, center aligned):
  - Left: Yudame wordmark or logo (24px height)
  - Right: URL "research.yuda.me/podcast"
  - Font: Inter, 12px, color #6B6B6B
  - Vertical center aligned
```

---

## Icon Library for Protocols

**Match these to Yudame design system:**

```
Common protocol icons (32px, 2px stroke):
- 🧠 Brain/learning: Network nodes, synapses, head outline
- ⚖️ Balance/calibration: Scales, slider, gauge
- 👥 People/team: Figures, collaboration, hierarchy
- 📈 Growth/timeline: Arrow up, steps, progress bar
- 🔄 Feedback/cycle: Circular arrows, loop, iteration
- 🎯 Target/goal: Bullseye, flag, checkmark
- 🔍 Research/analysis: Magnifying glass, data points
- 💡 Insight/idea: Lightbulb, star burst, connection
- 📊 Data/metrics: Bar chart, line graph, grid
- 🛠️ Tools/framework: Gear, wrench, blueprint
- 🌍 Global/context: Globe, pin, map
- ⏱️ Time/schedule: Clock, calendar, hourglass
```

**Style requirements:**
- Outlined style (not filled)
- 2px stroke weight
- Black (#000000) default
- Salmon (#E8B4A8) for emphasis (optional)
- Consistent corner radius (2px)

---

## Generation Prompt Template

**Use this exact prompt structure with NotebookLM or Gemini:**

```
Create a ONE-PAGE PORTRAIT INFOGRAPHIC for a podcast episode with the following specifications:

FORMAT:
- Orientation: Portrait (9:16 ratio)
- Size: 1080px × 1920px for social media OR 2550px × 3300px for print
- Margins: 48px on all sides
- Background: White (#FFFFFF)

BRANDING (CRITICAL - EXACT COLORS REQUIRED):
- Primary accent: #E8B4A8 (salmon - use for numbers, emphasis)
- Background accent: #F5F1E8 (cream - use for alternating sections)
- Text: #000000 (black - headlines), #3A3A3A (dark gray - descriptions)
- Dividers: #E5E5E5 (light gray)
- Fonts: Playfair Display (headlines, 600 weight), Inter (body, 400/500 weight)

STRUCTURE (TOP TO BOTTOM):

1. HEADER (15% of height):
   - Series label: "[SERIES NAME]: Episode [N]" (Inter 12px, uppercase, gray)
   - Episode title: "[TITLE]" (Playfair Display 32px, black)
   - Hook statistic: "[NUMBER]" in salmon (#E8B4A8), 48px, bold
   - Context: "[context text]" (Inter 14px, dark gray)
   - Thesis: "[one-sentence summary]" (Inter 14px, max 2 lines)

2. CONTENT SECTION (65% of height):
   [N] Protocols/Findings (3-5 items):

   Protocol 1:
   - Icon: [describe icon] (32px, 2px stroke, black)
   - Number: "1" (salmon #E8B4A8, Playfair 24px)
   - Title: "[Protocol name]" (Inter 16px, black)
   - Description: "[2-3 line description]" (Inter 14px, dark gray)
   - Background: White (#FFFFFF)

   Protocol 2:
   - [Same structure]
   - Background: Cream (#F5F1E8)

   [Alternate white/cream backgrounds for each protocol]

3. TAKEAWAYS SECTION (15% of height):
   - Background: Cream (#F5F1E8)
   - Title: "3 Critical Takeaways" (Playfair 22px, black, centered)
   - 3 items, each with:
     - Icon (24px, 2px stroke, black)
     - Title (Inter 14px, black)
     - Description (Inter 12px, dark gray, one line)

4. FOOTER (5% of height):
   - Background: White
   - Left: "Yudame Research" wordmark (Playfair 14px)
   - Right: "research.yuda.me/podcast" (Inter 12px, gray)
   - Border top: 1px #E5E5E5

DESIGN REQUIREMENTS:
- Use EXACTLY these colors (no variations)
- Generous white space between sections
- 2px divider lines between major sections (gray #E5E5E5)
- Icons: 2px stroke weight, outlined style (not filled)
- Maximum 5 protocols (keep scannable)
- Text should be easily readable at mobile size
- Professional, clean, minimalist aesthetic
- NO stock photos, gradients, or decorative patterns
- NO shadows except subtle box shadows on cards (optional)

TARGET AUDIENCE: Someone scrolling social media with 10 seconds to decide if episode is worth listening to.

EPISODE CONTENT:
[Paste episode-specific content here]
```

---

## Episode-Specific Content Template

**For each episode, fill in this template and append to the generation prompt:**

```
EPISODE: [Series Name]: [Episode Title]

HOOK STATISTIC (if applicable):
Number: [e.g., "89%"]
Context: [e.g., "of delegation failures are attitudinal"]

THESIS STATEMENT:
[One sentence, max 2 lines, e.g., "Most delegation advice has zero empirical validation. Success depends on learning agility, not technical competence."]

PROTOCOLS/FINDINGS (3-5 items):

1. [Protocol Name]
   Icon: [Describe what icon should represent - e.g., "brain with connections"]
   Description: [2-3 lines, focus on the "what" and "how", e.g., "Select delegates based on their ability to learn from experience, not their credentials. Use behavioral interview questions to assess learning agility."]

2. [Protocol Name]
   Icon: [Describe icon]
   Description: [2-3 lines]

[Continue for 3-5 protocols]

CRITICAL TAKEAWAYS (exactly 3):

1. [Takeaway Title]
   Icon: [Describe icon - e.g., "target/bullseye"]
   Description: [One line, e.g., "Hire for learning agility, not technical competence"]

2. [Takeaway Title]
   Icon: [Describe icon]
   Description: [One line]

3. [Takeaway Title]
   Icon: [Describe icon]
   Description: [One line]
```

---

## Generation Workflow

### Step 1: Extract Content from Episode Assets

**Source files:**
- `report.md` - Research synthesis
- `content_plan.md` - Episode structure
- `logs/quality_scorecard.md` - Key findings (if available)

**What to extract:**
1. **Hook statistic:** Look for surprising numbers in report.md intro
2. **Thesis statement:** Usually in report.md executive summary or content_plan.md opening
3. **Protocols/frameworks:** Look for numbered lists, action items, implementation steps
4. **Takeaways:** Often in report.md conclusion or content_plan.md closing

### Step 2: Fill Content Template

Use this structure:

```markdown
# Infographic Content: [Episode Title]

## Hook
- Stat: [number + unit]
- Context: [what the stat measures]

## Thesis
[One compelling sentence about the episode's core insight]

## Protocols (Choose 3-5 Most Actionable)
1. **[Name]**: [2-line description focusing on "how to do it"]
2. **[Name]**: [description]
3. **[Name]**: [description]
[4-5 if applicable]

## Takeaways (Exactly 3)
1. **[Title]**: [One-line essence]
2. **[Title]**: [One-line essence]
3. **[Title]**: [One-line essence]
```

### Step 3: Generate Infographic

**Tool options:**

**Option A: NotebookLM (Current approach)**
- Create temporary NotebookLM notebook
- Upload the generation prompt + episode content
- Request image generation with exact specifications
- Download PNG

**Option B: Gemini via OpenRouter**
- Use Gemini 2.0 Flash with image generation
- Send full prompt via API
- Receive image URL
- Download and save

**Option C: Claude + DALL-E (fallback)**
- Use Claude to format prompt
- Send to DALL-E 3 via API
- Post-process if needed

### Step 4: Quality Check

**Before accepting the infographic, verify:**

✅ **Branding:**
- [ ] Colors match exactly (salmon #E8B4A8, cream #F5F1E8, black #000000)
- [ ] Fonts are Playfair Display (headlines) + Inter (body) OR close equivalents
- [ ] Yudame wordmark or logo present in footer
- [ ] No off-brand colors introduced

✅ **Structure:**
- [ ] Portrait orientation (9:16 ratio)
- [ ] Clear hierarchy (header → content → takeaways → footer)
- [ ] Section dividers present (gray lines)
- [ ] Alternating white/cream backgrounds for protocols
- [ ] Generous white space (not cramped)

✅ **Icons:**
- [ ] Consistent style (outlined, not filled)
- [ ] Similar stroke weight across all icons
- [ ] Black default color (or salmon for emphasis)
- [ ] Icons clearly represent their concepts

✅ **Readability:**
- [ ] Text large enough to read on mobile
- [ ] High contrast (black text on white/cream)
- [ ] Max 2-3 lines per protocol description
- [ ] No text overlapping or cramped

✅ **Content:**
- [ ] Hook statistic prominent (if applicable)
- [ ] 3-5 protocols (not more, not less)
- [ ] Exactly 3 takeaways
- [ ] Episode title and series name correct

**If quality check fails:** Regenerate with more specific guidance in problem areas.

### Step 5: Save and Deploy

```bash
# Save to episode directory
cp infographic.png podcast/episodes/[slug]/companion/infographic-portrait.png

# Optimize for web (if needed)
# Reduce to ~500KB for social sharing
# Original: Keep high-res version for print
```

---

## Workflow Integration

### Add to Phase 11 (Publishing)

**New step: Generate Episode Infographic**

**After:** Companion resources created (summary, checklist, frameworks)
**Before:** Feed update and final publishing

**Process:**
1. Read report.md, content_plan.md to extract content
2. Fill episode-specific content template
3. Append to generation prompt
4. Generate infographic using NotebookLM or Gemini
5. Run quality check
6. Save to `companion/infographic-portrait.png`
7. Reference in show notes and social posts

**Exit criteria addition:**
- ✓ `companion/infographic-portrait.png` exists
- ✓ Infographic uses exact Yudame colors (salmon, cream, black)
- ✓ Infographic follows template structure
- ✓ Text is readable, not cramped
- ✓ 3-5 protocols + 3 takeaways present

---

## Example: Episode 3 Content

```
EPISODE: Algorithms for Life: How to Delegate

HOOK STATISTIC:
Number: "89%"
Context: "of delegation failures are attitudinal"

THESIS STATEMENT:
Most delegation advice has zero empirical validation. The real predictor of success is learning agility, not technical competence.

PROTOCOLS (5 items):

1. Prioritize Learning Agility
   Icon: Brain with neural connections
   Description: Select delegates based on their ability to learn from experience, not credentials. Use behavioral interview questions to assess learning agility.

2. Calibrate by Task Stakes
   Icon: Scales/balance
   Description: Use the "70% Rule" for low-stakes tasks, but require 90-95% competence for high-stakes, irreversible decisions. Apply graduated autonomy over 8-week timeline.

3. Assess Cultural Context
   Icon: Globe with pin markers
   Description: In high power-distance cultures, grant higher participative autonomy. In low-distance cultures, use more directive assignments. Ask: "Template or goal only?"

4. Apply Graduated Autonomy
   Icon: Steps/stairs going up
   Description: Follow the OPPTY framework: Observation → Practice → Partnering → Taking Responsibility → You're On Your Own. Typically 9-12 week timeline.

5. Establish Feedback Loops
   Icon: Circular arrows
   Description: Schedule weekly 1-on-1s for first month, build "Psychological Safety" so team voices concerns early. Balance efficiency with error prevention.

CRITICAL TAKEAWAYS (3 items):

1. Hire for Traits
   Icon: Target/bullseye
   Description: Who > What. Attitude and learning agility predict 89% of delegation success.

2. Question the Rules
   Icon: Key
   Description: Popular tools (70% rule, RACI) are heuristics, not scientific laws. Use with epistemic humility.

3. Context Reverses
   Icon: Globe
   Description: Autonomy can backfire cross-culturally. Adapt your delegation style to power distance norms.
```

---

## Automation Potential (Future)

**Create script: `podcast/tools/generate_infographic_content.py`**

```python
"""
Extract infographic content from episode assets.

Reads:
- report.md (hook stats, thesis, protocols)
- content_plan.md (structure, takeaways)
- quality_scorecard.md (key findings)

Outputs:
- infographic-content.md (ready to append to generation prompt)
"""

def extract_hook_stat(report_md):
    """Find surprising statistics in intro/executive summary."""
    pass

def extract_protocols(report_md):
    """Find numbered protocols, frameworks, action items."""
    pass

def extract_takeaways(content_plan_md):
    """Find episode closing synthesis."""
    pass

def format_for_prompt(hook, thesis, protocols, takeaways):
    """Format as episode-specific content template."""
    pass
```

**Workflow with automation:**
```bash
# Extract content
python podcast/tools/generate_infographic_content.py episode-dir/

# Review and edit infographic-content.md

# Append to generation prompt and send to NotebookLM/Gemini
```

---

## Success Metrics

**Infographic should achieve:**
- ✅ Scannable in 10-15 seconds
- ✅ Communicates episode value immediately
- ✅ Professional appearance (matches Yudame brand)
- ✅ Readable on mobile devices
- ✅ Shareable on social media (Instagram, LinkedIn, Twitter)
- ✅ Works as standalone reference (even without listening)
- ✅ Drives episode listens (compelling enough to click)

**Measurement:**
- Social engagement (likes, shares, comments)
- Click-through rate to episode
- Visual quality (passes brand consistency check)
- Time to generate (should be <30 min per episode)

---

## Next Steps

**Immediate:**
1. Test generation prompt with Episode 3 content (regenerate to validate approach)
2. Verify color accuracy (compare against Episode 3 existing infographic)
3. Refine prompt based on results

**Short-term:**
4. Generate infographics for Episodes 8 (Stablecoin) retroactively
5. Document any prompt adjustments needed
6. Add to standard workflow exit criteria

**Long-term:**
7. Create automation script for content extraction
8. Build library of episode infographics
9. Use for social media promotion and episode landing pages

**Would you like me to:**
- Test the generation prompt with Episode 3 content now?
- Create the content extraction template for Episode 8?
- Draft social media captions for infographic sharing?
