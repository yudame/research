# Yudame Research Design Documentation

This directory contains the complete design system and visual identity for Yudame Research.

## Start Here

### For Designers
Read **[DESIGN-SPECIFICATION.md](DESIGN-SPECIFICATION.md)** - This is the locked, opinionated implementation guide with exact measurements and non-negotiable patterns.

### For Developers
Use **[DESIGN-SPECIFICATION.md](DESIGN-SPECIFICATION.md)** for exact CSS values, component specs, and copy-paste ready code blocks.

### For Context
See **[DESIGN-BRIEF.md](DESIGN-BRIEF.md)** for the full rationale and design thinking behind the system.

---

## Files

### Implementation Documents

**[DESIGN-SPECIFICATION.md](DESIGN-SPECIFICATION.md)** ⭐ **START HERE**
- Opinionated, locked specifications
- Exact measurements (not ranges)
- Copy-paste ready CSS
- Non-negotiable patterns
- Validated through UI generation
- Implementation checklist

**[DESIGN-BRIEF.md](DESIGN-BRIEF.md)** - Design system rationale
- Color palette, typography, spacing philosophy
- Component patterns and usage guidelines
- Page templates with detailed hierarchies
- Data visualization and decorative element patterns
- Accessibility requirements
- Brand positioning and voice

### Reference Materials

**[UI-GENERATOR-PROMPTS.md](UI-GENERATOR-PROMPTS.md)** - AI UI generation prompts
- 4 validated prompts with exact specifications
- Mobile homepage, navigation, icons, data visualization
- Generated mockups validate the locked patterns

**[MOOD-BOARD-SOURCE.md](MOOD-BOARD-SOURCE.md)** - Original inspiration
- Source URLs for all 8 mood board images
- Images stored locally in `reference images/` directory
- Design theme analysis

## Reference Images

### Generated UI Validations
Located in `reference images/generated-ui/`:
- **Mobile homepage** - Validates responsive patterns, stacked buttons, feature cards
- **Header & footer** - Validates navigation system, footer layout
- **Icon library** - Validates 24 core icons, 2px stroke weight, salmon hover states
- **Data visualization** - Validates the signature hand-drawn annotation style

### Original Mood Board
Located in `reference images/`:
- 8 inspiration images from Cosmos.so mood board
- See MOOD-BOARD-SOURCE.md for source URLs and analysis

---

## Design System Summary

**Visual Identity:**
- Minimal black on white/cream foundation
- Muted salmon pink (#E8B4A8) accent color (never for body text)
- Serif (Playfair Display) + Sans-serif (Inter) + Monospace (IBM Plex Mono)
- Logo: Yellow "A" icon + "Yudame Research" text inline (see `podcast/yudame-logo.png`)

**The Signature Move:**
Hand-drawn annotations on clean data visualizations - rigorous research interpreted for human understanding.

**Locked Patterns:**
- Header: 80px desktop, 64px mobile
- Icons: 2px stroke weight ONLY
- Buttons: Salmon primary + black outline secondary, ALWAYS
- Transitions: 200ms ease, ALWAYS
- Graph paper: 20px squares on cream background
- Card padding: 32px desktop, 24px mobile

**Brand Positioning:**
- Professional enough for academic citation
- Warm enough for parent engagement
- Clean enough for focused reading
- Rich enough to feel crafted by humans

## Component Library

**[components/](components/)** - Production-ready vanilla HTML/CSS components
- ✅ Foundation CSS with design tokens
- ✅ Buttons (primary/secondary, all sizes)
- ✅ Forms (inputs, textareas, selects, file upload)
- ✅ Cards (feature, stat, content, article preview)
- ✅ Podcast player (episode cards with audio)
- ✅ Navigation (header, footer, mobile menu)

**Live Demo:** See `components/index.html`

All components use vanilla HTML/CSS with no frameworks or dependencies. Based on the locked specifications in DESIGN-SPECIFICATION.md.

---

## Status

- ✅ Design system v2.0 complete
- ✅ UI patterns validated through AI generation
- ✅ Exact specifications locked and ready for implementation
- ✅ Reference images validate all core patterns
- ✅ Component library built and documented

See **DESIGN-SPECIFICATION.md** for exact implementation requirements.
