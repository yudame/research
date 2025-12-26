# Design Patterns

Reference for consistent implementation across pages.

---

## Navigation

**Navbar order:** Home → Methodology → Podcast

- Methodology links to `/methodology.html`
- Podcast links to `/podcast/subscribe.html`
- Active state uses `is-active` class

---

## Backgrounds

**Hero sections:** Light cream gradient
```css
background: linear-gradient(135deg, var(--color-white) 0%, var(--color-cream) 100%);
```

**Alternating sections:** White, then graph-paper, then white...
```css
/* Graph paper pattern */
background:
    linear-gradient(var(--grid-color) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-color) 1px, transparent 1px),
    linear-gradient(135deg, var(--color-white) 0%, var(--color-cream) 100%);
background-size: var(--grid-size) var(--grid-size), var(--grid-size) var(--grid-size), 100% 100%;
```

---

## Synthesis Diagram

Visual representation of research process:

```
Proposal → [Academic, Real-Time, Industry, Policy] → Cross-Validated → Narrative
```

**Colors:**
- Proposal: Teal (#4A7C8C)
- Cross-Validated: Salmon (default)
- Narrative: Teal (#4A7C8C)
- Source icons: Academic (teal), Real-Time (black), Industry (green), Policy (blue)

---

## Subscribe Page Hero

Apple Podcasts-style layout:

1. **Artwork** (240x240, rounded corners, drop shadow)
2. **Meta line:** Category · Episode count · Updated date
3. **Title:** Podcast name
4. **Author:** "Produced by [Name]" with link
5. **Description:** 2-3 sentences
6. **Subscribe buttons:** Apple Podcasts, Spotify

---

## Series Cards

Condensed 2-column grid layout:

```html
<a href="..." class="series-card">
    <span class="series-card-title">Series Name</span>
    <span class="series-card-meta">N episodes</span>
</a>
```

- Inline layout (title + count on one line)
- No topic descriptions on homepage (save for series page)
- 2 columns on desktop, 1 on mobile

---

## Section Headers

**Avoid:** Self-answering questions ("Why This Works", "What We Do")

**Prefer:** Direct labels ("The Edge", "The Method", "Health", "Business")

---

## Proof Points

Key claims to use consistently:

- **40+ hours** of research per episode
- **Cross-validated** across multiple sources
- Every claim **sourced**, contradictions **shown**, uncertainty **stated**

---

## Attribution

**Podcast:** "Produced by Valor Engels"

**Footer tagline:** "We do the research. You get the edge."

---

*December 2025*
