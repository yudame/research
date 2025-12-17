# Yudame Research Design System
*Visual Identity & Brand Guidelines v2.0*

## Brand Essence

Yudame Research bridges rigorous academic research with human-centered design. The visual language balances:
- **Scholarly credibility** with **approachable warmth**
- **Systematic structure** with **organic human touches**
- **Digital clarity** with **analog tactility**

---

## Foundation: Color & Typography

### Color Palette
```css
/* Foundation - Use these 95% of the time */
--black: #000000;              /* Primary text, icons, lines */
--white: #FFFFFF;              /* Primary backgrounds */
--cream: #F5F1E8;              /* Alternate backgrounds, cards */

/* Salmon Accent - Use sparingly for emphasis */
--salmon: #E8B4A8;             /* CTAs, active states, highlights */
--salmon-light: #F5D5CC;       /* Hover states, tints */

/* Grays - Supporting roles only */
--gray-100: #F5F5F5;           /* Subtle backgrounds */
--gray-200: #E5E5E5;           /* Borders, dividers */
--gray-300: #D4D4D4;           /* Input borders */
--gray-600: #6B6B6B;           /* Secondary text, metadata */

/* Supporting Accents - Data visualization only */
--teal: #4A7C8C;               /* Charts, connection lines */
--yellow: #E8C547;             /* Charts, connection lines */
--rust: #C8867A;               /* Charts, connection lines */
```

### Typography System
**Serif (Playfair Display or similar):**
- Page headlines: 48-72px, weight 600-700
- Article titles: 36-48px, weight 600
- Pull quotes: 24-32px, weight 400, italic

**Sans-serif (Inter, Helvetica Neue, or similar):**
- UI elements, navigation: 14-16px, weight 400-500
- Body text: 16-18px, weight 400, line-height 1.6
- Metadata: 12-14px, weight 400, color gray-600
- Small caps labels: 11px, weight 500, letter-spacing 0.05em

**Monospace (IBM Plex Mono or similar):**
- Timestamps: 12-14px, weight 400
- Technical data: 14-16px, weight 400

---

## Proven Component Patterns

### 1. Buttons (CTA Pattern)
**Primary Button:**
```
Background: salmon (#E8B4A8)
Text: black, sans-serif, 14-16px, weight 500
Padding: 12px 24px
Border radius: 6px
Hover: salmon-light background
```

**Secondary Button:**
```
Background: transparent
Border: 2px solid black
Text: black, sans-serif, 14-16px, weight 500
Padding: 10px 22px (account for border)
Border radius: 6px
Hover: salmon border, black text
```

**Usage:** Always pair primary + secondary in hero sections (see Homepage mockup).

### 2. Form Inputs
**Text Input:**
```
Background: white
Border: 1px solid gray-300 (#D4D4D4)
Padding: 12px 16px
Border radius: 6px
Focus: 2px solid salmon
Placeholder: gray-600
```

**Upload/Drag Area:**
```
Border: 2px dashed gray-300
Background: gray-100
Border radius: 8px
Padding: 32px
Hover: dashed salmon border
```

**Newsletter Input (Homepage pattern):**
```
Input + Button in single row
Input: white background, dashed border (#D4D4D4)
Button: salmon fill, attached to right side
```

### 3. Feature Cards
**Structure (from Homepage):**
```
Background: white
Border: 1px solid gray-200
Shadow: 0 2px 8px rgba(0,0,0,0.06)
Padding: 32px
Border radius: 8px

Icon at top: 48x48px, minimal line drawing, black
Title: Serif, 20-24px, weight 600
Body: Sans-serif, 14-16px, gray-800
```

**Container:**
```
Background: cream (#F5F1E8) with subtle paper grain texture
Cards arranged in 3-column grid (desktop)
Gap: 24px between cards
```

### 4. Audio Waveform (Podcast Pages)
**Critical: Must look functional, not decorative**

```
Style: Amplitude bars (like audio editing software)
Color: Black lines on cream background
Width: Full width, height: 120-160px
Playhead: Vertical salmon line (2px) with small circle handle
Background: Subtle paper texture

DO: Dense vertical lines showing actual audio peaks/valleys
DON'T: Stylized wave illustrations, decorative curves
```

### 5. Audio Player Controls
**Layout (from Podcast mockup):**
```
Centered horizontal layout:
[Skip -15s] [Play/Pause] [Skip +30s]

Buttons:
- Circular outlines, black 2px stroke
- Play: 60px diameter
- Skip: 48px diameter
- Icons: black, centered
- Hover: salmon stroke

Progress bar below:
- Height: 4px
- Background: gray-200
- Filled: salmon
- Handle: 12px circle, salmon, white border
```

### 6. Chapter Navigation (Podcast Pages)
**Timeline Pattern:**
```
Horizontal line: 2px solid gray-300
Chapter markers: Circles (10px) positioned on line

States:
- Past chapters: Filled black circles
- Current chapter: Filled salmon circle (14px, emphasis)
- Future chapters: Outlined black circles (1px stroke)

Below markers:
- Chapter title: Sans-serif, 13px, black
- Timestamp: Monospace, 12px, gray-600
- Align text center under each marker
```

**DO NOT use organic connecting lines - keep professional and linear.**

---

## Hand-Drawn Elements (Use Sparingly)

### When to Use Hand-Drawn Style:
1. **Dashboard achievement cards** - Connecting dots with colorful lines on graph paper
2. **Background decorations** - Subtle dotted connection paths (10% opacity max)
3. **Chart annotations** - Hand-drawn arrows, labels on graph paper backgrounds
4. **Border decorations** - Organic patterns at page edges (top/bottom only)

### When NOT to Use:
- Navigation elements
- Buttons or forms
- Primary content areas
- Podcast player interfaces

### Execution Guidelines:
```
Hand-drawn annotations on charts:
- Black ink style
- Casual handwriting font or actual SVG paths
- Arrows, circles, labels
- On graph paper background (#F5F1E8 with light grid)

Connection dots pattern:
- Black dots (4-8px)
- Connecting lines: salmon, teal, yellow, rust
- Line weight: 1-2px
- Used in achievement/progress cards only

Background decorations:
- Minimal dotted paths connecting empty space
- 5-10% opacity
- Salmon color only
- Never compete with content
```

---

## Page Templates (Proven Patterns)

### Homepage Template
```
[Hero Section - White Background]
├─ Subtle graph paper grid background (5% opacity)
├─ Logo/wordmark: top left, black
├─ Navigation: top right, black text, minimal
├─ Headline: Serif, 60-72px, black, centered
├─ Subheadline: Sans-serif, 18px, gray-800, 2-3 lines, centered
├─ CTA buttons: Primary (salmon) + Secondary (outlined), centered
└─ Decorative: Subtle dotted connection paths in corners (salmon, 10% opacity)

[Feature Section - Cream Background (#F5F1E8)]
├─ Paper grain texture overlay
├─ 3 feature cards (white, with minimal icons)
├─ Card icons: Black line drawings (dots pattern, waveform, connection nodes)
└─ 24px gap between cards

[Newsletter Section - White Background]
├─ Headline: Serif, 32-36px, centered
├─ Input + Button: Horizontal layout, dashed input border
└─ Button: Salmon fill, "Subscribe" text

[Footer - Off-white (#FAFAF9)]
├─ 4-column layout
├─ Logo + tagline: left column
├─ Navigation links: Sans-serif, 14px, organized columns
└─ Copyright: 12px, gray-600
```

### Research Article Template
```
[Header - White Background]
├─ Title: Serif, 48px, black
├─ Metadata: Sans-serif, 14px, gray-600 ("Published Dec 2025 • 12 min read")
└─ Separator: 2px solid salmon, full width

[Article Body - Cream Background (#F5F1E8) with paper texture]
├─ Max width: 680px, centered
├─ Margins: 80px desktop, 24px mobile
├─ Body text: Serif, 18px, black, line-height 1.6
├─ Pull quotes: Serif italic, 24px, with 4px salmon left border
└─ Charts: Black lines, salmon highlights, on white cards

[Sidebar - White Card, absolute positioned right]
├─ "Key Sources" heading: Small caps, 11px, letterspaced
├─ Citations: Sans-serif, 13px, gray-800
└─ Shadow: 0 2px 8px rgba(0,0,0,0.06)
```

### Podcast Episode Template
```
[Hero - Cream Background (#F5F1E8) with paper texture]
├─ Waveform: Full width, functional amplitude style, black
├─ Playhead: Vertical salmon line (2px)
├─ Title: Serif, 36-48px, black, centered below waveform
└─ Metadata: Monospace, 12px, gray-600

[Player Controls - White Background]
├─ Controls: Centered, circular outlines, black
├─ Progress bar: Below controls, salmon fill
└─ Max width: 600px, centered

[Chapter Timeline - White Background]
├─ Horizontal timeline with dot markers
├─ Current chapter: Salmon dot (14px)
├─ Titles below dots: Sans-serif, 13px
└─ Timestamps: Monospace, 12px, gray-600

[Transcript - White Background]
├─ Max width: 800px
├─ Speaker labels: Sans-serif small caps, 11px, gray-800
├─ Timestamps: Monospace, 12px, gray-600, inline
├─ Speech text: Serif, 16px, black, line-height 1.6
└─ Alternate speaker backgrounds: Subtle gray-100 tint
```

### Learning Dashboard Template
```
[Header - White Background]
├─ Title: Serif, 32-36px, black
├─ Date selector: Outlined dropdown, right aligned
└─ Decorative border: Hand-drawn pattern strip at top (salmon, 40px height)

[Main Content - Cream Background (#F5F1E8)]
├─ Two-column layout (60/40 split)
│
├─ [Left: Progress Chart]
│   ├─ Graph paper background with light grid
│   ├─ Line chart: Black lines, data points
│   ├─ Annotations: Hand-drawn style ("Reviews", "Gaps", arrows)
│   ├─ Highlighted periods: Salmon vertical bands
│   └─ White card container with subtle shadow
│
└─ [Right: Achievements Card]
    ├─ White card background
    ├─ "This Week's Achievements" heading
    ├─ Connection dots pattern: Black dots with colorful lines
    ├─ Hand-drawn annotations and checkmarks
    ├─ Decorative elements (star, small icons)
    └─ Casual handwritten style labels

[Progress Bars - White Background]
├─ Goal label: Sans-serif, 16px, black
├─ Percentage: Monospace, right aligned
├─ Bar: Height 24px, rounded 4px
├─ Filled portion: Salmon
├─ Empty portion: Gray-200
└─ 16px spacing between bars

[Activity Feed - White Background]
├─ Cards: White, minimal shadow, 16px padding
├─ Icon: Left side, 32px, black line drawing
├─ Activity text: Sans-serif, 14px, black
├─ Timestamp: Monospace, 12px, gray-600, below text
└─ 12px gap between cards
```

---

## Data Visualization Standards

### Chart Basics
```
Background: White or cream with graph paper grid
Axes: 1px solid black
Grid lines: 1px solid gray-200
Labels: Sans-serif, 12px, gray-800
Data points: 6px circles, black or salmon
```

### Color Usage in Charts
**For single data series:**
- Primary line/bar: Black
- Highlight/current: Salmon
- Comparison: Teal

**For multiple data series:**
- Use black + salmon + teal + yellow + rust
- Never more than 5 colors
- Include legend with color keys

### Hand-Drawn Chart Annotations
**When appropriate:**
- Dashboard progress tracking
- Informal learning insights
- Achievement visualizations

**Pattern:**
```
Base chart: Clean, professional (black lines, graph paper)
Annotations layer:
├─ Hand-drawn arrows pointing to insights
├─ Casual handwritten labels ("Reviews", "Gaps", "Great job!")
├─ Circles highlighting key data points
└─ All in black ink style on cream/graph paper background
```

---

## Decorative Elements Library

### 1. Dotted Connection Paths
**Usage:** Background decoration only, never interactive
```
Pattern: Scattered dots (4px, salmon) with thin connecting lines
Opacity: 5-10% maximum
Placement: Page corners, empty space between sections
Style: Organic curves, not geometric
```

### 2. Hand-Drawn Pattern Borders
**Usage:** Top or bottom page borders, section dividers
```
Height: 24-40px
Patterns: Mix of dots, waves, cross-hatching, organic shapes
Colors: Salmon primary, black accents
Style: Like decorative washi tape
Placement: Top of dashboard, bottom of newsletter sections
```

### 3. Graph Paper Backgrounds
**Usage:** Chart containers, achievement cards, creative sections
```
Base color: Cream (#F5F1E8)
Grid: Light gray (#E5E5E5), 1px lines
Grid spacing: 20px squares
Texture: Subtle paper grain overlay
```

### 4. Paper Texture Overlay
**Usage:** Cream background sections only
```
Pattern: Subtle fiber texture
Opacity: 3-5%
Blend mode: Multiply
Color: Warm gray
DO NOT use on white backgrounds
```

---

## Iconography System

### Minimal Line Icons
**Specification:**
- Style: Outlined, not filled
- Stroke weight: 2px
- Color: Black (default), salmon (active state)
- Size: 24px, 32px, 48px (multiples of 8)
- Corner radius: Consistent with overall design (2-4px)

**Icon Subjects (from mockups):**
- Connection dots pattern (Evidence-Based Insights)
- Waveform (Podcast/Audio)
- Network nodes (Tools & Resources)
- Book/document (Research)
- Clock/timer (Time tracking)
- Gear/settings (Configuration)

**Style notes:**
- Keep geometric and minimal
- Avoid high detail
- Should work at small sizes
- Test at 16px minimum

---

## Spacing & Layout Standards

### Grid System
```
Desktop: 12 columns, 24px gutters
Tablet: 8 columns, 20px gutters
Mobile: 4 columns, 16px gutters

Max content width: 1200px
Article max width: 680px (single column reading)
Dashboard max width: 1400px (data needs space)
```

### Spacing Scale (8px base)
```
--space-1: 8px    (tight, inline elements)
--space-2: 16px   (related elements)
--space-3: 24px   (cards, components)
--space-4: 32px   (sections within page)
--space-6: 48px   (major sections)
--space-8: 64px   (page sections)
--space-10: 80px  (hero spacing, page margins)
--space-12: 96px  (large page sections)
```

### Card Spacing Pattern
```
Card padding: 32px (--space-4)
Between cards: 24px (--space-3)
Card to section edge: 48px (--space-6)
```

---

## Accessibility Requirements

### Color Contrast
- Body text (black on white): 21:1 ✓
- Body text (black on cream): 18:1 ✓
- Salmon accent on white: 3.2:1 (decorative only, not for text)
- Gray-600 metadata on white: 6.5:1 ✓

**Never use salmon for body text.** Only for backgrounds, buttons (with black text), and large UI elements.

### Typography Accessibility
- Minimum body text: 16px
- Maximum line length: 680px (65-75 characters)
- Line height: 1.6 minimum for body text
- Paragraph spacing: 1.5em minimum

### Interactive Elements
- Minimum touch target: 44x44px
- Focus indicators: 2px solid salmon outline
- Keyboard navigation: Full support required
- Screen reader: Semantic HTML, ARIA labels

---

## Implementation Checklist

### Core System
- [ ] Typography: Load Playfair Display + Inter + IBM Plex Mono
- [ ] Color variables: Implement CSS custom properties
- [ ] Spacing system: 8px grid utilities
- [ ] Button components: Primary + Secondary variants
- [ ] Form inputs: Text, textarea, dashed upload areas
- [ ] Card component: White with shadow, cream container

### Page Templates
- [ ] Homepage: Hero + feature cards + newsletter
- [ ] Research article: Header, body, sidebar, pull quotes
- [ ] Podcast player: Waveform, controls, chapter timeline, transcript
- [ ] Dashboard: Charts, achievement cards, progress bars, activity feed

### Visual Character
- [ ] Paper texture overlays (cream backgrounds only)
- [ ] Graph paper background pattern
- [ ] Decorative SVG elements (dots, connection lines, annotations)
- [ ] Decorative border patterns
- [ ] Icon library (24px, 32px, 48px sizes)

### Polish & Quality
- [ ] Accessibility audit (WCAG AA)
- [ ] Mobile responsive breakpoints
- [ ] Animation/transition timing
- [ ] Performance optimization (lazy load textures)
- [ ] Cross-browser testing

---

## What Makes This Design System Unique

**We are NOT:**
- Generic SaaS minimalism (we have warmth and character)
- Academic journal sterility (we're approachable)
- Childish ed-tech (we're professional and credible)
- Trendy startup (we're timeless and thoughtful)

**We ARE:**
- Rigorous research + human warmth
- Clean digital + analog textures
- Professional credibility + approachable design
- Systematic structure + organic touches

**The signature move:**
Hand-drawn annotations on clean data visualizations. This is the visual metaphor for our brand: rigorous research (clean charts, graph paper, professional typography) interpreted for human understanding (handwritten notes, casual annotations, warm connections).

---

## Maintenance & Evolution

### Design Tokens (source of truth)
All colors, spacing, typography stored in:
- CSS custom properties (web)
- Design tokens JSON (design tools)
- Never hard-code values

### Component Library
- Storybook or similar for component documentation
- Each component has: Default state, hover, active, focus, disabled
- Mobile variants documented

### Future Considerations
- Dark mode: Would need careful rethinking (cream becomes dark gray, salmon adjusts)
- Internationalization: Test with longer text strings, RTL languages
- Print styles: Research articles should print beautifully
- Email templates: Limited version of design system for newsletters

---

*Design System v2.0 - December 2025*
*Validated through AI UI generation testing*
*Ready for implementation*
