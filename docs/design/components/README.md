# Yudame Research Component Library

Production-ready vanilla HTML/CSS components based on the locked design specification.

## Getting Started

### 1. Include Foundation Styles

All pages must include the foundation CSS first:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="foundation.css">
```

### 2. Include Component Styles

Then include the specific component CSS you need:

```html
<link rel="stylesheet" href="buttons.css">
<link rel="stylesheet" href="forms.css">
<link rel="stylesheet" href="cards.css">
<link rel="stylesheet" href="navigation.css">
```

---

## Available Components

### Foundation (`foundation.css`)

**Required for all pages.** Provides:
- CSS variables for all design tokens (colors, spacing, typography)
- Base styles for HTML elements
- Utility classes
- Responsive breakpoints

**CSS Variables:**
```css
/* Colors */
--color-black, --color-white, --color-cream
--color-salmon, --color-salmon-light
--color-gray-100 through --color-gray-800

/* Typography */
--font-serif, --font-sans, --font-mono
--text-5xl (60px) through --text-xs (12px)
--weight-normal, --weight-medium, --weight-semibold

/* Spacing (8px base) */
--space-1 (8px) through --space-12 (96px)

/* Transitions (LOCKED at 200ms ease) */
--transition-base

/* Layout */
--header-height-desktop (80px)
--header-height-mobile (64px)
--card-padding-desktop (32px)
--card-padding-mobile (24px)
```

---

### Buttons (`buttons.css`)

#### Primary Button
Salmon fill (#E8B4A8) with black text. Use for primary CTAs.

```html
<button class="btn btn-primary">Explore Research</button>
<a href="#" class="btn btn-primary">Explore Research</a>
```

#### Secondary Button
Transparent with 2px black border. Hover shows salmon border.

```html
<button class="btn btn-secondary">Browse Podcast</button>
```

#### Button Sizes
```html
<button class="btn btn-primary btn-large">Large Button</button>
<button class="btn btn-primary">Default Button</button>
<button class="btn btn-primary btn-small">Small Button</button>
```

#### Button Groups (Locked Pattern)
**ALWAYS** put primary (salmon) before secondary (outline).

```html
<!-- Desktop: Horizontal -->
<div class="btn-group">
  <button class="btn btn-primary">Explore Research</button>
  <button class="btn btn-secondary">Browse Podcast</button>
</div>

<!-- Mobile: Always stacks vertically -->
<div class="btn-group-vertical">
  <button class="btn btn-primary">Explore Research</button>
  <button class="btn btn-secondary">Browse Podcast</button>
</div>
```

**States:**
- `:hover` - Lightens background (primary) or changes border color (secondary)
- `:active` - Translates down 1px
- `:focus` - 2px salmon outline with 2px offset
- `:disabled` - Gray with 60% opacity

**Demo:** See `buttons.html`

---

### Forms (`forms.css`)

#### Text Input
```html
<div class="form-group">
  <label class="form-label" for="email">Email Address</label>
  <input type="email" id="email" class="input" placeholder="you@example.com">
  <span class="form-hint">We'll never share your email.</span>
</div>
```

#### Textarea
```html
<div class="form-group">
  <label class="form-label" for="message">Message</label>
  <textarea id="message" class="textarea" placeholder="Your message..."></textarea>
</div>
```

#### Dashed Input (Newsletter/Upload Pattern)
```html
<input type="email" class="input-dashed" placeholder="Enter your email">
```

#### Select Dropdown
```html
<select class="select">
  <option>Select an option</option>
  <option>Option 1</option>
  <option>Option 2</option>
</select>
```

#### Input Group (Newsletter Pattern)
```html
<div class="input-group">
  <input type="email" class="input" placeholder="Enter your email">
  <button class="btn btn-primary">Subscribe</button>
</div>
```

#### Form States
```html
<!-- Error state -->
<div class="form-group">
  <input type="email" class="input input-error">
  <span class="form-error">Please enter a valid email address.</span>
</div>

<!-- Success state -->
<div class="form-group">
  <input type="email" class="input input-success">
  <span class="form-success">Email verified successfully!</span>
</div>
```

#### File Upload
```html
<div class="file-upload">
  <label class="file-upload-area" for="file">
    <svg class="file-upload-icon"><!-- Upload icon --></svg>
    <span class="file-upload-text">Click to upload or drag and drop</span>
    <span class="file-upload-hint">PDF, DOC, XLS, PPT or JPG (max 15MB)</span>
  </label>
  <input type="file" id="file">
</div>
```

---

### Cards (`cards.css`)

#### Feature Card (Homepage Pattern)
```html
<div class="feature-card">
  <svg class="feature-card-icon"><!-- Icon --></svg>
  <h3 class="feature-card-title">Evidence-Based Insights</h3>
  <p class="feature-card-description">
    Access synthesized findings from leading academic journals
    without the jargon, ready for classroom application.
  </p>
</div>
```

#### Feature Cards Section (Locked Layout)
```html
<section class="feature-cards-section">
  <div class="feature-cards-grid">
    <div class="feature-card">...</div>
    <div class="feature-card">...</div>
    <div class="feature-card">...</div>
  </div>
</section>
```

**Locked Pattern:**
- Desktop: 3 columns
- Tablet: 2 columns
- Mobile: 1 column (stacked)
- Background: Cream (#F5F1E8)
- Padding: 32px desktop, 24px mobile

#### Stat Card (Data Visualization)
```html
<div class="stat-card">
  <div class="stat-card-number">85%</div>
  <p class="stat-card-label">Average retention with active recovery</p>
</div>
```

#### Content Card
```html
<div class="content-card">
  <div class="content-card-header">
    <h3 class="content-card-title">Key Sources</h3>
  </div>
  <div class="content-card-body">
    <!-- Content here -->
  </div>
  <div class="content-card-footer">
    <!-- Footer actions -->
  </div>
</div>
```

#### Article Preview Card
```html
<a href="#" class="article-card">
  <div class="article-card-meta">Published Dec 2025 • 12 min read</div>
  <h3 class="article-card-title">The Science of Active Recovery in Learning</h3>
  <p class="article-card-excerpt">
    In the ever-evolving landscape of education, the focus has shifted...
  </p>
</a>
```

---

### Podcast Player (`podcast-player.css`)

#### Episode Card
```html
<div class="episode">
  <div class="episode-header">
    <span class="episode-number">Ep 1</span>
    <span class="episode-title">Lifestyle Foundations</span>
    <span class="episode-duration">43:57</span>
    <span class="episode-links-inline">
      <a href="ep1-lifestyle/report.html">Report</a>
      <a href="ep1-lifestyle/transcript.html">Transcript</a>
    </span>
  </div>
  <div class="episode-summary">
    How VO2 max and HRV predict longevity better than traditional risk factors.
  </div>
  <details class="episode-details">
    <summary>More details</summary>
    <div class="episode-full-description">
      Full description with additional context and research details.
    </div>
  </details>
  <audio controls preload="metadata">
    <source src="episode.mp3" type="audio/mpeg">
  </audio>
</div>
```

**Key Features:**
- **Episode number badge**: Salmon background with black text
- **Expandable details**: Click "More details" to reveal full description
- **Inline links**: Report and transcript links in header
- **Monospace duration**: IBM Plex Mono for timestamp
- **Native audio player**: HTML5 controls with focus styling

**Episode List Container:**
```html
<div class="episode-list">
  <h2 class="episode-list-header">Podcast Episodes</h2>
  <div class="episode">...</div>
  <div class="episode">...</div>
</div>
```

**Locked Specs:**
- Card padding: 32px desktop, 24px mobile
- Episode number: 4px 12px padding, full border-radius
- Details summary: `+` expands to `−` when open
- Links: Black with salmon hover
- Audio player: 48px height, 2px salmon focus outline

**Mobile Behavior:**
- Header elements stack vertically
- Duration moves to top-right
- Links remain inline at bottom
- Full width audio controls

**Demo:** See `podcast-player.html`

---

### Navigation (`navigation.css`)

#### Desktop Header (80px height)
```html
<header class="header">
  <div class="header-container">
    <a href="/" class="header-logo">Yudame Research</a>
    <nav>
      <ul class="nav">
        <li class="nav-item">
          <a href="/" class="nav-link is-active">Home</a>
        </li>
        <li class="nav-item">
          <a href="/research" class="nav-link">Research</a>
        </li>
        <li class="nav-item">
          <a href="/podcast" class="nav-link">Podcast</a>
        </li>
        <li class="nav-item">
          <a href="/about" class="nav-link">About</a>
        </li>
        <li class="nav-item">
          <a href="/contact" class="nav-link">Contact</a>
        </li>
      </ul>
    </nav>
  </div>
</header>
```

**Locked Specs:**
- Height: 80px desktop, 64px mobile
- Active state: 2px salmon underline
- Hover state: 40% opacity salmon underline
- Scrolled state: Shadow appears (add `.is-scrolled` class)

#### Mobile Header with Menu
```html
<header class="header">
  <div class="header-container">
    <a href="/" class="header-logo">Yudame Research</a>

    <!-- Mobile menu toggle -->
    <button class="mobile-menu-toggle" aria-label="Toggle menu">
      <span class="mobile-menu-icon">
        <span></span>
        <span></span>
        <span></span>
      </span>
    </button>
  </div>
</header>

<!-- Mobile menu (hidden by default) -->
<div class="mobile-menu">
  <ul class="mobile-nav">
    <li class="mobile-nav-item">
      <a href="/" class="mobile-nav-link is-active">Home</a>
    </li>
    <!-- More items -->
  </ul>
</div>
```

**JavaScript for mobile menu:**
```javascript
const toggle = document.querySelector('.mobile-menu-toggle');
const menu = document.querySelector('.mobile-menu');

toggle.addEventListener('click', () => {
  toggle.classList.toggle('is-open');
  menu.classList.toggle('is-open');
  document.body.style.overflow = menu.classList.contains('is-open') ? 'hidden' : '';
});
```

#### Footer (4-column layout)
```html
<footer class="footer">
  <div class="footer-container">
    <div class="footer-content">
      <!-- Column 1: Brand -->
      <div class="footer-column">
        <div class="footer-logo">Yudame Research</div>
        <p class="footer-tagline">
          Research-based early childhood education
        </p>
      </div>

      <!-- Column 2: Explore -->
      <div class="footer-column">
        <h3 class="footer-heading">Explore</h3>
        <ul class="footer-links">
          <li><a href="#">Research Archive</a></li>
          <li><a href="#">Podcast Episodes</a></li>
          <li><a href="#">Resources</a></li>
          <li><a href="#">About Us</a></li>
        </ul>
      </div>

      <!-- Column 3: Company -->
      <div class="footer-column">
        <h3 class="footer-heading">Company</h3>
        <ul class="footer-links">
          <li><a href="#">Our Team</a></li>
          <li><a href="#">Careers</a></li>
          <li><a href="#">Contact</a></li>
          <li><a href="#">Press</a></li>
        </ul>
      </div>

      <!-- Column 4: Connect -->
      <div class="footer-column">
        <h3 class="footer-heading">Connect</h3>
        <ul class="footer-links">
          <li><a href="#">Twitter</a></li>
          <li><a href="#">LinkedIn</a></li>
          <li><a href="#">Newsletter link</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <p class="footer-copyright">
        © 2024 Yudame Research. All rights reserved.
      </p>
      <p class="footer-dedication">
        Dedicated to advancing early childhood education through research
      </p>
    </div>
  </div>
</footer>
```

**Responsive:**
- Desktop: 4 columns
- Tablet: 2 columns (2x2 grid)
- Mobile: 1 column (stacked)

---

## Design Rules (Locked)

### Colors
- **Salmon (#E8B4A8):** Primary CTAs, accents, active states ONLY. Never for body text.
- **Black (#000000):** All text, icons (default), borders (primary)
- **Cream (#F5F1E8):** Alternate section backgrounds
- **Grays:** Secondary text, borders, backgrounds

### Typography
- **Playfair Display:** Headlines, card titles (weight 600)
- **Inter:** Body text, UI elements (weight 400-500)
- **IBM Plex Mono:** Timestamps, code, technical data (weight 400)

### Spacing
Use ONLY the locked spacing scale (8px base):
- `--space-1` through `--space-12`
- Card padding: 32px desktop, 24px mobile
- Section padding: 48px desktop, 40px mobile

### Transitions
ALL transitions use `--transition-base` (200ms ease). No other timing allowed.

### Buttons
- Primary ALWAYS before secondary in groups
- Mobile: Full width, stacked vertically
- Active state: 1px translateY down
- Focus: 2px salmon outline, 2px offset

### Forms
- Minimum height: 48px on mobile (prevents iOS zoom)
- Focus: 2px salmon border
- Font size: 16px minimum (prevents iOS zoom)

### Cards
- Padding: 32px desktop, 24px mobile
- Shadow: `--shadow-sm` default, `--shadow-md` on hover
- Border radius: 8px

### Navigation
- Header height: 80px desktop, 64px mobile (LOCKED)
- Active state: 2px salmon underline
- Sticky positioning with scroll shadow

---

## Accessibility

All components meet WCAG AA standards:

- **Color contrast:** Black text on white: 21:1 ✓
- **Keyboard navigation:** All interactive elements focusable
- **Focus indicators:** 2px salmon outline with 2px offset
- **Semantic HTML:** Proper heading hierarchy, button/link distinction
- **ARIA labels:** All icon-only buttons have labels
- **Touch targets:** Minimum 44x44px on mobile

---

## File Structure

```
components/
├── README.md                    # This file
├── foundation.css              # Required: Design tokens and base styles
├── buttons.css                 # Button components
├── buttons.html                # Button demos
├── forms.css                   # Form input components
├── cards.css                   # Card components
├── podcast-player.css          # Podcast episode cards and audio player
├── podcast-player.html         # Podcast player demo
└── navigation.css              # Header and footer
```

---

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

Uses modern CSS (custom properties, grid, flex). No IE11 support.

---

## Examples

### Basic Page Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title - Yudame Research</title>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="foundation.css">
  <link rel="stylesheet" href="navigation.css">
  <link rel="stylesheet" href="buttons.css">
  <link rel="stylesheet" href="cards.css">
</head>
<body>
  <header class="header">
    <!-- Navigation -->
  </header>

  <main>
    <div class="container">
      <!-- Page content -->
    </div>
  </main>

  <footer class="footer">
    <!-- Footer -->
  </footer>
</body>
</html>
```

---

## Next Steps

1. Copy the component CSS files to your project
2. Include `foundation.css` in all pages (required)
3. Include specific component CSS as needed
4. Use exact HTML structure from examples
5. Never modify locked values (spacing, transitions, colors)

For questions or clarifications, refer to **DESIGN-SPECIFICATION.md** in the parent directory.
