# Yudame Research Design Specification
*Opinionated Implementation Guide - Lock These Down*

> This is not a brief. This is the specification. These patterns are validated and locked. Implement exactly as specified.

---

## Mobile-First Specifications

### Mobile Breakpoints (Locked)
```css
--mobile: 375px;        /* iPhone SE, base mobile */
--tablet: 768px;        /* iPad portrait */
--desktop: 1024px;      /* Laptop */
--wide: 1440px;         /* Desktop */
```

**Implementation rule:** Design mobile-first, then scale up. Never design desktop and squeeze down.

---

## Navigation System (Locked)

### Desktop Header
```
Height: 80px
Background: #FFFFFF
Border bottom: 1px solid #E5E5E5 (only on scroll)
Shadow on scroll: 0 2px 8px rgba(0,0,0,0.04)

Left:
  Logo wordmark: "Yudame Research"
  Font: Playfair Display, 20px, weight 600
  Color: #000000
  Margin left: 48px

Right:
  Navigation items: Home | Research | Podcast | About | Contact
  Font: Inter, 14px, weight 400
  Color: #000000
  Letter spacing: 0.02em
  Margin right: 48px

  Item spacing: 32px between items

  Active state:
    - 2px solid salmon (#E8B4A8) underline
    - Positioned 4px below text
    - Width: 100% of text

  Hover state:
    - 2px solid salmon (#E8B4A8) underline, 40% opacity
    - Transition: opacity 200ms ease
```

### Mobile Header
```
Height: 64px
Background: #FFFFFF
Border bottom: 1px solid #E5E5E5

Left:
  Logo wordmark: "Yudame Research"
  Font: Playfair Display, 18px, weight 600
  Margin left: 20px

Right:
  Hamburger menu icon
  Size: 24px × 24px
  Color: #000000
  Three horizontal lines, 2px stroke
  Spacing: 6px between lines
  Margin right: 20px
  Tap target: 44px × 44px (extended hit area)
```

### Footer (Desktop)
```
Background: #FAFAF9
Padding: 64px 48px 32px 48px

Layout: 4 columns, equal width
Gap: 48px between columns

Column 1 (Brand):
  Logo: "Yudame Research" stacked
  Font: Playfair Display, 24px, weight 600
  Tagline below: "Research-based early childhood education"
  Tagline font: Inter, 12px, color #6B6B6B

Columns 2-4 (Navigation):
  Heading: Inter, 14px, weight 600, color #000000
  Links: Inter, 14px, weight 400, color #3A3A3A
  Line height: 2.0 (generous spacing)
  Hover: color changes to salmon #E8B4A8

Bottom section (full width):
  Border top: 1px solid #E5E5E5
  Margin top: 48px
  Padding top: 24px

  Copyright: Inter, 12px, color #6B6B6B, center aligned
  Dedication: Inter, 11px, color #6B6B6B, center aligned
  Line spacing: 8px between lines
```

---

## Button System (Exact Specifications)

### Primary Button
```css
background: #E8B4A8;
color: #000000;
font-family: Inter;
font-size: 16px;
font-weight: 500;
padding: 10px 24px;
border-radius: 6px;
border: none;
line-height: 1.5;
letter-spacing: 0.01em;

/* Hover state */
background: #F5D5CC;
transition: background-color 200ms ease;

/* Active state */
background: #D89B8E;

/* Disabled state */
background: #E5E5E5;
color: #6B6B6B;
cursor: not-allowed;
```

### Secondary Button
```css
background: transparent;
color: #000000;
font-family: Inter;
font-size: 16px;
font-weight: 500;
padding: 8px 22px; /* 2px less to account for border */
border: 2px solid #000000;
border-radius: 6px;
line-height: 1.5;
letter-spacing: 0.01em;

/* Hover state */
border-color: #E8B4A8;
color: #000000;
transition: border-color 200ms ease;

/* Active state */
border-color: #D89B8E;
```

### Button Pairing Rule (Locked)
**When showing two CTAs together:**
1. Primary (salmon fill) is ALWAYS on top (mobile) or left (desktop)
2. Secondary (outline) is ALWAYS below (mobile) or right (desktop)
3. Vertical spacing (mobile): 16px gap
4. Horizontal spacing (desktop): 16px gap
5. Both buttons same width on mobile (full width minus 40px margins)

**Example (Mobile):**
```
[Explore Research] ← salmon fill, full width
     ↓ 16px gap
[Browse Podcast]  ← outline, full width
```

---

## Form Input System (Exact Specifications)

### Text Input (Default)
```css
background: #FFFFFF;
border: 1px solid #D4D4D4;
border-radius: 6px;
padding: 10px 14px;
font-family: Inter;
font-size: 16px;
color: #000000;
line-height: 1.5;

/* Placeholder */
color: #6B6B6B;

/* Focus state */
border: 2px solid #E8B4A8;
padding: 9px 13px; /* Adjust for thicker border */
outline: none;

/* Error state */
border: 2px solid #C8867A;

/* Disabled state */
background: #F5F5F5;
border: 1px solid #E5E5E5;
color: #6B6B6B;
```

### Text Input (Dashed - Newsletter/Upload)
```css
background: #FFFFFF;
border: 2px dashed #D4D4D4;
border-radius: 6px;
padding: 12px 16px;
font-family: Inter;
font-size: 16px;
color: #000000;

/* Focus state */
border: 2px dashed #E8B4A8;
outline: none;
```

### Input + Button Combo (Newsletter Pattern)
```
Mobile (stacked):
  Input: full width
  Button: full width, 12px margin top

Desktop (horizontal):
  Container: max-width 400px
  Input: flex-grow 1
  Button: fixed width 120px, attached right (no gap)
  Border radius: Input left only (6px 0 0 6px), Button right only (0 6px 6px 0)
```

---

## Icon System (Locked Specifications)

### Icon Technical Specs
```
Stroke weight: 2px (NEVER 1px or 3px)
Sizes: 24px, 32px, 48px (ONLY these three)
Color: #000000 (default), #E8B4A8 (active/hover)
Style: Outlined, never filled
Corner radius: 2px on rounded elements
Padding: Icons centered in bounding box
Export: SVG only
```

### Icon Usage Rules
1. **24px icons:** Inline with text, small UI elements, mobile navigation
2. **32px icons:** Feature cards on mobile, sidebar elements
3. **48px icons:** Feature cards on desktop, hero sections
4. **Hover behavior:** Color transition from black to salmon, 200ms ease
5. **Active state:** Solid salmon fill

### Icon Grid (24 Core Icons)
```
Evidence & Research:
- connection-dots (the signature pattern)
- network-nodes
- book-document
- magnifying-glass
- academic-cap
- beaker-flask

Audio & Podcast:
- waveform
- play-button
- microphone
- headphones
- volume-speaker
- timeline-chapters

Tools & Interface:
- gear-settings
- download-arrow
- upload-cloud
- search
- filter
- menu

Time & Progress:
- clock-timer
- calendar
- checkmark-circle
- star-achievement
- progress-arrow
- chart-graph
```

**Implementation note:** Use this exact list. Don't add custom icons without design review.

---

## Feature Card System (Exact Pattern)

### Desktop Feature Card
```css
/* Container (cream section) */
background: #F5F1E8;
padding: 64px 48px;

/* Individual card */
background: #FFFFFF;
border: 1px solid #E5E5E5;
border-radius: 8px;
padding: 32px;
box-shadow: 0 2px 8px rgba(0,0,0,0.06);

/* Card layout */
display: flex;
flex-direction: column;
align-items: flex-start;
gap: 16px;

/* Icon */
width: 48px;
height: 48px;
margin-bottom: 8px;

/* Title */
font-family: Playfair Display;
font-size: 22px;
font-weight: 600;
color: #000000;
line-height: 1.3;

/* Description */
font-family: Inter;
font-size: 15px;
font-weight: 400;
color: #3A3A3A;
line-height: 1.6;

/* Grid */
display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 24px;
max-width: 1200px;
margin: 0 auto;
```

### Mobile Feature Card
```css
/* Container */
background: #F5F1E8;
padding: 40px 20px;

/* Individual card */
Same as desktop, but:
- Full width (no grid)
- Stack vertically with 16px gap
- Icon: 32px (smaller)
- Padding: 24px (tighter)
```

**Locked pattern:** Always use 3 cards on desktop, stacked on mobile. Icon at top left, title below, description below that.

---

## Data Visualization System (The Signature Move)

### Graph Paper Background
```css
background: #F5F1E8;
background-image:
  linear-gradient(#E5E5E5 1px, transparent 1px),
  linear-gradient(90deg, #E5E5E5 1px, transparent 1px);
background-size: 20px 20px;
padding: 32px;
border-radius: 8px;
```

**Locked specs:**
- Grid size: Exactly 20px squares
- Grid color: #E5E5E5 (1px lines)
- Base color: #F5F1E8 (cream)
- Never use on white background

### Chart Specifications
```
Axes: 1px solid #000000
Grid lines: 1px solid #E5E5E5
Labels: Inter, 12px, #3A3A3A
Title: Playfair Display, 14px, #000000

Data lines:
- Primary/Control: 2px solid #000000
- Highlight/Treatment: 2px solid #E8B4A8
- Additional series: #4A7C8C, #E8C547

Data points: 6px circles, filled, same color as line
```

### Hand-Drawn Annotations (Exact Style)
```
Font: Caveat or Virgil (handwriting style)
Size: 16-18px
Color: #000000
Style: Casual, slightly irregular

Elements allowed:
- Circles around data points (2px stroke, black)
- Arrows pointing to insights (2px stroke, black)
- Underlines for emphasis (2px stroke, wavy)
- Stars/checkmarks for achievements (16px, black)
- Short text labels (handwriting font)

Rules:
1. Maximum 3-4 annotations per chart
2. Never obscure actual data
3. Always in black (never salmon)
4. Casual but legible
5. Point to specific insights, not general areas
```

### Side Stat Cards (With Charts)
```css
background: #FFFFFF;
border-radius: 8px;
padding: 24px;
box-shadow: 0 2px 8px rgba(0,0,0,0.06);

/* Large number */
font-family: Inter;
font-size: 48px;
font-weight: 700;
color: #E8B4A8; /* Salmon for impact */
line-height: 1.0;
margin-bottom: 8px;

/* Label */
font-family: Inter;
font-size: 14px;
font-weight: 400;
color: #3A3A3A;
line-height: 1.5;

/* Stack vertically */
gap: 24px between cards;
```

**Locked pattern:** Always pair charts with 2-3 stat cards. Large salmon number, black description text.

---

## Typography Scale (Exact Sizes)

### Headlines (Playfair Display, weight 600)
```
h1 (Hero): 60px / line-height 1.1 / letter-spacing -0.02em (desktop)
          32px / line-height 1.2 / letter-spacing -0.01em (mobile)

h2 (Page): 48px / line-height 1.2 / letter-spacing -0.01em (desktop)
          28px / line-height 1.2 / letter-spacing 0 (mobile)

h3 (Section): 36px / line-height 1.3 / letter-spacing 0 (desktop)
             24px / line-height 1.3 / letter-spacing 0 (mobile)

h4 (Card): 22px / line-height 1.3 / letter-spacing 0 (desktop)
          20px / line-height 1.3 / letter-spacing 0 (mobile)
```

### Body Text (Inter, weight 400)
```
Large: 18px / line-height 1.6 / letter-spacing 0
Base: 16px / line-height 1.6 / letter-spacing 0
Small: 14px / line-height 1.5 / letter-spacing 0
Tiny: 12px / line-height 1.5 / letter-spacing 0.01em
```

### UI Text (Inter, weight 500)
```
Button: 16px / line-height 1.5 / letter-spacing 0.01em
Nav: 14px / line-height 1.5 / letter-spacing 0.02em
Label: 12px / line-height 1.5 / letter-spacing 0.05em (UPPERCASE)
```

### Technical Text (IBM Plex Mono, weight 400)
```
Timestamp: 12px / line-height 1.5
Code: 14px / line-height 1.6
Data: 14px / line-height 1.5
```

**Rule:** NEVER use font sizes outside this scale. If you think you need 17px, use 16px or 18px.

---

## Spacing System (8px Base - Exact Values)

```css
--space-1: 8px;     /* Tight inline spacing */
--space-2: 16px;    /* Related elements, small gaps */
--space-3: 24px;    /* Component spacing, card gaps */
--space-4: 32px;    /* Section spacing within components */
--space-5: 40px;    /* Section spacing (mobile) */
--space-6: 48px;    /* Section spacing (desktop) */
--space-8: 64px;    /* Major section spacing */
--space-10: 80px;   /* Hero/page spacing (desktop) */
--space-12: 96px;   /* Large page sections */
```

**Locked rules:**
1. ONLY use values from this scale
2. Mobile: Use smaller values (space-3 to space-5)
3. Desktop: Use larger values (space-6 to space-12)
4. Card padding: Always 32px (space-4) on desktop, 24px (space-3) on mobile
5. Section padding: Always 48px (space-6) on desktop, 40px (space-5) on mobile

---

## Color Usage (Strict Rules)

### When to Use Salmon (#E8B4A8)
✅ **USE for:**
- Primary CTA buttons (background)
- Active navigation state (underline)
- Chart highlight lines
- Large stat numbers
- Icon hover/active states
- Progress bar fills
- Form input focus borders
- Accent dots in decorations

❌ **NEVER use for:**
- Body text (fails contrast)
- Small text under 18px
- Backgrounds with white text
- Footer elements
- Chart axes or grids
- Secondary buttons (use black outline)

### When to Use Black (#000000)
✅ **USE for:**
- All body text
- All headlines
- Primary chart lines
- Icons (default state)
- Borders (primary)
- Hand-drawn annotations
- Secondary button text
- Navigation text

### When to Use Cream (#F5F1E8)
✅ **USE for:**
- Alternate section backgrounds
- Graph paper chart backgrounds
- Feature card container backgrounds
- Never for text

### When to Use Grays
```
#F5F5F5: Subtle section backgrounds, disabled button backgrounds
#E5E5E5: Borders, dividers, chart grids
#D4D4D4: Input borders, dashed borders
#6B6B6B: Secondary text, metadata, placeholders
#3A3A3A: Tertiary text, descriptions
```

**Rule:** If you're unsure about color, use black. Salmon is an accent, not a primary color.

---

## Component States (Exact Transitions)

### Button States
```css
/* Default */
transition: background-color 200ms ease;

/* Hover */
/* See button specs above */

/* Active (being clicked) */
transform: translateY(1px);

/* Focus (keyboard) */
outline: 2px solid #E8B4A8;
outline-offset: 2px;

/* Disabled */
cursor: not-allowed;
opacity: 0.6;
```

### Input States
```css
/* Default to Focus */
transition: border-color 200ms ease;

/* Focus (keyboard) */
outline: none; /* Border handles focus */
```

### Link States
```css
/* Hover */
transition: color 200ms ease;

/* Focus (keyboard) */
outline: 2px solid #E8B4A8;
outline-offset: 2px;
border-radius: 2px;
```

**Locked timing:** All transitions are 200ms ease. No other timing allowed.

---

## Mobile Patterns (Locked)

### Mobile Page Structure
```
1. Header (64px fixed height)
2. Content padding: 20px left/right
3. Section spacing: 40px vertical
4. Max width: 100% (no max-width constraint)
5. Bottom spacing: 40px before footer
```

### Mobile Typography Adjustments
```
- All headlines: Reduce by ~40-50%
- Body text: Keep at 16px (maintain readability)
- Buttons: Keep at 16px (maintain tap target)
- Line height: Keep at 1.6 (don't tighten)
```

### Mobile Interaction Rules
```
- Minimum tap target: 44px × 44px
- Button padding: 12px vertical minimum
- Form inputs: 48px height minimum
- Icon tap areas: Extend beyond visible icon
- Horizontal scrolling: NEVER (except intentional carousels)
```

---

## Accessibility (Non-Negotiable)

### Color Contrast Requirements
```
Black on white: 21:1 ✓ (WCAG AAA)
Black on cream: 18:1 ✓ (WCAG AAA)
Gray-600 on white: 6.5:1 ✓ (WCAG AA)
Salmon on white: 3.2:1 ✗ (Decorative only)
```

**Rule:** Never use salmon for text under 24px. Use black.

### Keyboard Navigation
```
- All interactive elements: keyboard accessible
- Tab order: logical left-to-right, top-to-bottom
- Focus indicators: 2px salmon outline, 2px offset
- Skip links: "Skip to content" at top
- No keyboard traps
```

### Screen Readers
```
- Semantic HTML: Use h1-h6, nav, main, footer, article
- Alt text: All images, descriptive not decorative
- ARIA labels: Forms, buttons, icons
- Link text: Descriptive, not "click here"
```

**Rule:** Test with keyboard only. If you can't use it, fix it.

---

## Implementation Checklist

Copy this exact pattern:

### Phase: Core System
- [ ] Load fonts: Playfair Display (600), Inter (400, 500), IBM Plex Mono (400)
- [ ] CSS variables: Implement exact color, spacing, typography scales
- [ ] Button components: Primary + Secondary with exact hover states (200ms ease)
- [ ] Input components: Default + Dashed variants with focus states
- [ ] Navigation: Desktop horizontal + Mobile hamburger (exact header heights)

### Phase: Page Templates
- [ ] Mobile homepage: Stacked layout, full-width buttons, feature cards
- [ ] Desktop homepage: 3-column feature cards, horizontal CTAs
- [ ] Navigation: Desktop (80px) + Mobile (64px) headers, footer 4-column layout
- [ ] Forms: Newsletter pattern (stacked mobile, horizontal desktop)

### Phase: Visual Character
- [ ] Icon library: Export all 24 icons as SVG, 24/32/48px sizes
- [ ] Graph paper background: CSS pattern with 20px grid
- [ ] Hand-drawn annotations: Source Caveat/Virgil font, create SVG examples
- [ ] Stat cards: Large salmon numbers with black labels

### Phase: Quality
- [ ] Accessibility: WCAG AA audit, keyboard navigation test
- [ ] Mobile responsive: Test at 375px, 768px, 1024px, 1440px
- [ ] Transitions: Verify all 200ms ease timing
- [ ] Cross-browser: Test Safari, Chrome, Firefox

---

## What You Cannot Change

These patterns are locked from validated UI generation:

1. **Button pairing:** Salmon primary + black outline secondary, ALWAYS in this order
2. **Icon stroke weight:** 2px, NEVER 1px or 3px
3. **Graph paper grid:** 20px squares on cream background
4. **Hand-drawn annotations:** Black only, maximum 3-4 per chart
5. **Header heights:** 80px desktop, 64px mobile
6. **Card padding:** 32px desktop, 24px mobile
7. **Salmon usage:** Accents only, never body text
8. **Transition timing:** 200ms ease, ALWAYS
9. **Typography scale:** Use ONLY the specified sizes
10. **Spacing system:** 8px base, use ONLY the scale values

---

## Reference Images

Validated UI examples in `docs/design/reference images/generated-ui/`:
- `mobile-homepage.png` - Mobile responsive pattern
- `header-footer.png` - Navigation system
- `icon-library.png` - Complete icon set
- `data-visualization.png` - Signature hand-drawn annotation style

These are not inspiration. These are the specification.

---

*Design Specification v1.0 - December 2025*
*Opinionated. Validated. Locked.*
*Implement exactly as specified.*
