# Redesign TODO

Complete redesign of all HTML files in the repository to use the locked design system from `docs/design/`.

**Scope:** Redesign branding (messaging, styles, page layout) while maintaining all existing functionality.

**Design System Reference:** `docs/design/DESIGN-SPECIFICATION.md` and `docs/design/components/`

---

## Design System Requirements

All redesigned pages MUST follow these locked specifications:

### Required CSS
- `docs/design/components/foundation.css` - Design tokens (REQUIRED for all pages)
- `docs/design/components/podcast-player.css` - Episode cards and audio players
- `docs/design/components/buttons.css` - Button components
- `docs/design/components/navigation.css` - Header and footer
- `docs/design/components/cards.css` - Content cards
- `docs/design/components/forms.css` - Form inputs (if needed)

### Required Fonts
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
```

### Locked Design Principles
- **Colors:** Black (#000000) text, Salmon (#E8B4A8) accents ONLY, Cream (#F5F1E8) backgrounds
- **Typography:** Playfair Display (headlines), Inter (body), IBM Plex Mono (timestamps/code)
- **Spacing:** 8px baseline grid using `--space-1` through `--space-12`
- **Transitions:** 200ms ease (LOCKED - use `--transition-base`)
- **Logo:** Yellow "A" icon (`podcast/yudame-logo.png`) + "Yudame Research" text inline
- **Navigation:** No pink/salmon hover - black underline only
- **Button order:** Primary (salmon) ALWAYS before secondary (outline)

### Component Reference
See `docs/design/components/podcast-player.html` for complete working example.

---

## Phase 1: Core Landing Pages

### 1.1 Main Landing Page
- **File:** `index.html`
- **Current state:** Yellow accent (#f5d563), basic layout
- **Redesign requirements:**
  - Replace yellow with salmon (#E8B4A8)
  - Add logo (podcast/yudame-logo.png) + "Yudame Research" inline
  - Use Playfair Display for headlines
  - Use component library button styles
  - Update navigation to use locked header styles
  - Add footer from navigation.css
  - Keep existing links/functionality
  - Reference: `docs/design/components/index.html` for layout patterns

**Functionality to preserve:**
- All existing navigation links
- Spotify link
- All content sections

**New branding:**
- Messaging should emphasize "research-based early childhood education"
- Professional but warm tone
- Minimal, clean design

---

## Phase 2: Series Index Pages

Each series landing page needs complete redesign using the podcast player component.

### 2.1 Active Recovery Series
- **File:** `podcast/episodes/active-recovery/index.html`
- **Episodes:** 4+
- **Redesign requirements:**
  - Use `podcast-player.css` for episode cards
  - Include foundation.css and design tokens
  - Update all episode cards to use `.episode` class
  - Use `.episode-number` (salmon badge), `.episode-title` (serif), `.episode-duration` (mono)
  - Use native `<details>` for expandable descriptions
  - Add proper header with logo + series title
  - Add breadcrumb navigation
  - Reference: `docs/design/components/podcast-player.html`

### 2.2 Algorithms for Life Series
- **File:** `podcast/episodes/algorithms-for-life/index.html`
- **Requirements:** Same as 2.1

### 2.3 Cardiovascular Health Series
- **File:** `podcast/episodes/cardiovascular-health/index.html`
- **Requirements:** Same as 2.1

### 2.4 Kindergarten First Principles Series
- **File:** `podcast/episodes/kindergarten-first-principles/index.html`
- **Requirements:** Same as 2.1

### 2.5 Solomon Islands Telecom Series
- **File:** `podcast/episodes/solomon-islands-telecom-series/index.html`
- **Requirements:** Same as 2.1

**Notes for all series pages:**
- Keep existing functionality (audio players, links, expandable details)
- Update coming soon episodes to match new styling
- Ensure all episode metadata is accurate
- Mobile responsive using component library breakpoints

---

## Phase 3: Episode Report Pages

All episode report.html files need redesigned using content card components.

### 3.1 Active Recovery Episodes
- [ ] `podcast/episodes/active-recovery/ep1-foundations/report.html`
- [ ] Additional episode reports as they exist

### 3.2 Algorithms for Life Episodes
- [ ] Episode report.html files

### 3.3 Cardiovascular Health Episodes
- [ ] `podcast/episodes/cardiovascular-health/ep1-lifestyle/report.html`
- [ ] `podcast/episodes/cardiovascular-health/ep2-vo2-max/report.html`
- [ ] `podcast/episodes/cardiovascular-health/ep3-hrv/report.html`
- [ ] `podcast/episodes/cardiovascular-health/ep4-supplementation/report.html`

### 3.4 Kindergarten First Principles Episodes
- [ ] `podcast/episodes/kindergarten-first-principles/ep1-developmental-imperative/report.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep2-play-pedagogy/report.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep3-sleep-memory-scheduling/report.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep4-social-laboratory/report.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep5-sustaining-excellence/report.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep6-frameworks-environment/report.html`

### 3.5 Solomon Islands Telecom Episodes
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-1-financial-infrastructure/report.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-2-breaking-duopoly/report.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-3-infrastructure-advantage/report.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-4-mobile-money/report.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-5-launch-execution/report.html`

### 3.6 Stablecoin Series Episodes
- [ ] `podcast/episodes/stablecoin-series/episode-1-market-evolution/report.html`
- [ ] `podcast/episodes/stablecoin-series/episode-2-legal-compliance/report.html`

**Redesign requirements for all report.html files:**
- Use foundation.css and cards.css
- Use `.content-card` for main report container
- Use Playfair Display for section headings
- Use Inter for body text
- Add breadcrumb navigation (Series > Episode > Report)
- Add "Back to Series" link
- Keep all existing content and structure
- Style citations/sources with proper typography
- Add header with logo
- Mobile responsive

---

## Phase 4: Episode Transcript Pages

All episode transcript.html files need redesigned with clean, readable typography.

### 4.1 Active Recovery Episodes
- [ ] `podcast/episodes/active-recovery/ep1-foundations/transcript.html`
- [ ] Additional transcript files

### 4.2 Algorithms for Life Episodes
- [ ] Transcript.html files

### 4.3 Cardiovascular Health Episodes
- [ ] `podcast/episodes/cardiovascular-health/ep1-lifestyle/transcript.html`
- [ ] `podcast/episodes/cardiovascular-health/ep2-vo2-max/transcript.html`
- [ ] `podcast/episodes/cardiovascular-health/ep3-hrv/transcript.html`
- [ ] `podcast/episodes/cardiovascular-health/ep4-supplementation/transcript.html`

### 4.4 Kindergarten First Principles Episodes
- [ ] `podcast/episodes/kindergarten-first-principles/ep1-developmental-imperative/transcript.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep2-play-pedagogy/transcript.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep3-sleep-memory-scheduling/transcript.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep4-social-laboratory/transcript.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep5-sustaining-excellence/transcript.html`
- [ ] `podcast/episodes/kindergarten-first-principles/ep6-frameworks-environment/transcript.html`

### 4.5 Solomon Islands Telecom Episodes
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-1-financial-infrastructure/transcript.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-2-breaking-duopoly/transcript.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-3-infrastructure-advantage/transcript.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-4-mobile-money/transcript.html`
- [ ] `podcast/episodes/solomon-islands-telecom-series/episode-5-launch-execution/transcript.html`

### 4.6 Stablecoin Series Episodes
- [ ] `podcast/episodes/stablecoin-series/episode-1-market-evolution/transcript.html`
- [ ] `podcast/episodes/stablecoin-series/episode-2-legal-compliance/transcript.html`

**Redesign requirements for all transcript.html files:**
- Use foundation.css only (minimal styling)
- IBM Plex Mono for timestamps
- Inter for transcript text
- Clean, readable layout with good line-height
- Add breadcrumb navigation (Series > Episode > Transcript)
- Add "Back to Series" and "View Report" links
- Speaker labels if applicable
- Add header with logo
- Mobile responsive with good reading width

---

## Implementation Guidelines

### Before Starting Each Phase
1. Read `docs/design/DESIGN-SPECIFICATION.md` for exact specs
2. Review `docs/design/components/README.md` for component usage
3. Check `docs/design/components/podcast-player.html` for working example

### HTML Template Pattern
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Page Title] - Yudame Research</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">

    <!-- Design System -->
    <link rel="stylesheet" href="[relative-path]/docs/design/components/foundation.css">
    <link rel="stylesheet" href="[relative-path]/docs/design/components/[component].css">
</head>
<body>
    <!-- Use component library classes -->
    <div class="container">
        <!-- Content -->
    </div>
</body>
</html>
```

### CSS Custom Properties to Use
- Colors: `--color-black`, `--color-salmon`, `--color-cream`, `--color-gray-[100-800]`
- Typography: `--font-serif`, `--font-sans`, `--font-mono`
- Font sizes: `--text-5xl` through `--text-xs`
- Spacing: `--space-1` through `--space-12`
- Transitions: `--transition-base` (200ms ease - LOCKED)
- Shadows: `--shadow-sm`, `--shadow-md`

### Testing Checklist
For each redesigned page:
- [ ] Loads in Chrome/Safari/Firefox
- [ ] Mobile responsive (check at 375px, 768px, 1440px widths)
- [ ] All links work correctly
- [ ] Audio players work (if applicable)
- [ ] Typography is readable and follows specs
- [ ] Colors match design system exactly
- [ ] No custom CSS that violates locked specs
- [ ] Logo displays correctly
- [ ] Navigation works
- [ ] No console errors

---

## Update `.claude/skills/` References

After redesigning HTML templates, update these skill files to reference the new design system:

- [ ] `.claude/skills/new-podcast-episode.md` - Update HTML generation sections
- [ ] `.claude/skills/podcast-series.md` - Already updated with design system reference

---

## Exclusions

**Do NOT redesign these:**
- `docs/design/**/*.html` - Design system documentation
- `node_modules/**/*.html` - Dependencies
- `podcast/tools/.venv/**/*.html` - Python virtual environment
- `podcast/tools/htmlcov/**/*.html` - Test coverage reports

---

## Progress Tracking

**Phase 1:** ⬜ Not started
**Phase 2:** ⬜ Not started
**Phase 3:** ⬜ Not started
**Phase 4:** ⬜ Not started

---

## Notes

- All redesigned pages should feel cohesive as part of the Yudame Research brand
- Preserve all existing content - this is a visual/branding redesign only
- Use component library components - do NOT create custom CSS
- Reference existing series pages as "legacy" - new implementations should follow locked specs
- When in doubt, check `docs/design/DESIGN-SPECIFICATION.md` for exact requirements
