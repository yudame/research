# Podcast Series Planning

This skill covers planning and organizing multi-episode podcast series. For creating individual episodes, see `new-podcast-episode.md`.

## When to Use Series Organization

**Use a series subdirectory when:**
- Creating 3+ episodes on a related topic (e.g., cardiovascular health, blockchain fundamentals)
- Planning a cohesive multi-part series with logical progression
- Want to group related episodes for better organization

**Use standalone episode structure when:**
- Creating one-off episodes on different topics
- Episode is not part of a planned series
- Topic doesn't fit into an existing series

## Series Directory Structure

```
podcast/episodes/
├── series-name/                    # Series subdirectory
│   ├── ep1-topic-slug/
│   │   ├── prompts.md
│   │   ├── research-results.md
│   │   ├── sources.md
│   │   ├── report.md
│   │   ├── publish.md
│   │   ├── documents/              # Only if needed
│   │   ├── cover.png
│   │   ├── YYYY-MM-DD-series-name-episode-1-topic.mp3
│   │   ├── YYYY-MM-DD-series-name-episode-1-topic_transcript.json
│   │   ├── YYYY-MM-DD-series-name-episode-1-topic_chapters.txt
│   │   └── YYYY-MM-DD-series-name-episode-1-topic_chapters.json
│   ├── ep2-topic-slug/
│   ├── ep3-topic-slug/
│   └── ep4-topic-slug/
└── YYYY-MM-DD-standalone-topic/    # Standalone episodes at root
```

## Series Naming Conventions

**Directory naming:**
- Series subdirectory: `series-name/` (lowercase, hyphenated, e.g., `cardiovascular-health/`)
- Episode subdirectory: `epX-topic-slug/` (e.g., `ep1-lifestyle/`, `ep2-vo2-max/`)

**Episode title format:**
```
Series Name: Ep. X, Topic
```

**Examples:**
- "Cardiovascular Health: Ep. 1, Lifestyle Foundations"
- "Cardiovascular Health: Ep. 2, VO2 Max"
- "Kindergarten First Principles: Ep. 1, The Developmental Imperative"
- "Kindergarten First Principles: Ep. 2, Play as Pedagogy"

**Audio file naming (remains date-based for chronological sorting):**
```
YYYY-MM-DD-series-name-episode-X-topic.mp3
```

## Planning a New Series

When planning a multi-episode series:

### 1. Series Planning Research

Before defining episodes, conduct a mini research phase to discover what the series should cover:

```
Research [broad topic area].

**Context:** Planning a podcast series for [target audience].

**Research questions:**
- What are the key subtopics or themes within this area?
- What logical progression would help listeners build understanding?
- What are the most important concepts to cover?
- What surprising or counterintuitive findings exist?

**Output:** Overview that would inform how to structure a multi-part series.
```

### 2. Define Series Structure

Based on research, create episode breakdown:

| Ep | Title | Core Territory |
|---|---|---|
| 1 | [Topic] | [Brief description of focus] |
| 2 | [Topic] | [Brief description of focus] |
| ... | ... | ... |

### 3. Create Episode Prompts

For each episode, write a high-level research prompt:
- Keep prompts broad and non-prescriptive
- Let deep research go where the evidence leads
- Focus on the core question, not predetermined structure

**Example:**
> Research [specific topic] from a [relevant discipline] perspective. Explore [key questions]. Investigate [areas of interest].

### 4. Create Series Directory Structure

```bash
mkdir -p ~/src/research/podcast/episodes/series-name/ep1-topic-slug
```

### 5. Create Research Prompt Files

For each episode, create `research-prompt.md`:

```markdown
# Episode X: [Title]

## Research Prompt

[The high-level research prompt]

---

## Episode Details

- **Series:** [Series Name]
- **Episode:** X of N
- **Title:** [Full Episode Title]
- **Slug:** [topic-slug]

## To Start This Episode

\`\`\`
/podcast-episode [Research prompt text]
\`\`\`
```

## Example: Cardiovascular Health Series

```
podcast/episodes/cardiovascular-health/
├── ep1-lifestyle/
│   ├── prompts.md
│   ├── research-results.md
│   ├── sources.md
│   ├── report.md
│   ├── publish.md
│   ├── cover.png
│   ├── 2025-11-21-cardiovascular-health-episode-1-lifestyle.mp3
│   └── ...
├── ep2-vo2-max/
├── ep3-hrv/
└── ep4-supplementation/
```

## Feed.xml Entry for Series Episodes

```xml
<item>
  <title>Cardiovascular Health: Ep. 4, Supplementation</title>
  <description>Episode description... Full research report: https://research.yuda.me/podcast/episodes/cardiovascular-health/ep4-supplementation/report.md</description>
  <enclosure url="https://research.yuda.me/podcast/episodes/cardiovascular-health/ep4-supplementation/2025-11-21-cardiovascular-health-episode-4-supplementation.mp3"
             length="36144828"
             type="audio/mpeg"/>
  <guid>https://research.yuda.me/podcast/episodes/cardiovascular-health/ep4-supplementation/2025-11-21-cardiovascular-health-episode-4-supplementation.mp3</guid>
</item>
```

## Migrating Standalone Episodes to Series

If standalone episodes should become a series:

1. **Create series subdirectory:**
   ```bash
   mkdir -p ~/src/research/podcast/episodes/series-name
   ```

2. **Move and rename episode directories:**
   ```bash
   mv podcast/episodes/YYYY-MM-DD-old-name podcast/episodes/series-name/ep1-topic-slug
   ```

3. **Update feed.xml:**
   - Change all episode paths to `episodes/series-name/epX-topic-slug/`
   - Normalize all titles to "Series Name: Ep. X, Topic" format

4. **Commit with descriptive message:**
   ```bash
   git add -A
   git commit -m "refactor: Organize [series name] episodes into series subdirectory"
   git push
   ```

## Cover Art for Series

For series episodes, use the branding script with series text:

```bash
cd ~/src/research/podcast/tools

python add_logo_watermark.py ../episodes/series-name/epX-slug/cover.png \
  --position top-left \
  --brand "Yudame Research" \
  --series "Series Name" \
  --episode "Ep X - Topic" \
  --border 20 \
  --border-color "#FFC20E"
```

## Series Index Page

Each series should have an `index.html` landing page showcasing all episodes with embedded audio players.

**Location:** `podcast/episodes/series-name/index.html`

**URL:** `https://research.yuda.me/podcast/episodes/series-name/`

### Creating a Series Index Page

Use the same theme as the main site (`index.html`). Reference existing series pages:
- `podcast/episodes/cardiovascular-health/index.html` - Complete series with audio
- `podcast/episodes/kindergarten-first-principles/index.html` - Upcoming series template

### Page Structure

Reference existing implementations for full CSS:
- `podcast/episodes/cardiovascular-health/index.html` - Complete series with audio
- `podcast/episodes/kindergarten-first-principles/index.html` - Upcoming series template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Use same CSS variables as main index.html -->
    <title>[Series Name] - Yudame Research</title>
</head>
<body>
    <!-- Breadcrumb -->
    <p class="breadcrumb"><a href="../../../">Yudame Research</a> / Podcast Series</p>

    <!-- Header with logo and series title -->
    <div class="header">
        <img src="../../../podcast/cover.png" alt="Yudame Research" class="logo">
        <h1>[Series Name]</h1>
    </div>
    <p class="tagline">[Series description]</p>

    <!-- Spotify link -->
    <div class="subscribe-section">
        <p><strong>Subscribe to the full podcast</strong></p>
        <a href="https://open.spotify.com/show/32xUME8x4FN1DcNwBOrYfc" class="spotify-button">Listen on Spotify</a>
    </div>

    <h2>Episodes</h2>

    <!-- Episode cards -->
    <div class="episode-list">
        <div class="episode available">  <!-- or just "episode" for coming soon -->
            <div class="episode-header">
                <span class="episode-number">Ep 1</span>
                <span class="episode-title">[Title]</span>
                <span class="episode-duration">[Duration or "Coming soon"]</span>
            </div>
            <div class="episode-summary">[1-sentence summary]</div>
            <details class="episode-details">
                <summary>More</summary>
                <div class="episode-full-description">[Full description]</div>
            </details>
            <div class="episode-links">
                <a href="ep1-slug/report.md">Full Report</a>
                <a href="ep1-slug/sources.md">Sources</a>
            </div>
            <audio controls preload="none">
                <source src="ep1-slug/[audio-file].mp3" type="audio/mpeg">
            </audio>
        </div>
        <!-- More episodes... -->
    </div>

    <a href="../../../" class="back-link">Back to Yudame Research</a>
</body>
</html>
```

### Episode Card States

**Available episode:**
```html
<div class="episode available">
    <!-- teal left border, full opacity -->
    <div class="episode-header">
        <span class="episode-number">Ep 1</span>
        <span class="episode-title">Topic</span>
        <span class="episode-duration">36:13</span>
    </div>
    <div class="episode-summary">Short description.</div>
    <details class="episode-details">
        <summary>More</summary>
        <div class="episode-full-description">Full description.</div>
    </details>
    <!-- Include links and audio player -->
</div>
```

**Coming soon episode:**
```html
<div class="episode">
    <!-- gray left border, slight opacity reduction (0.85) -->
    <div class="episode-header">
        <span class="episode-number">Ep 1</span>
        <span class="episode-title">Topic</span>
        <span class="episode-duration">Coming soon</span>
    </div>
    <div class="episode-summary">Short description.</div>
    <details class="episode-details">
        <summary>More</summary>
        <div class="episode-full-description">Full description.</div>
    </details>
    <!-- Omit links and audio player -->
</div>
```

### Styling Conventions

- **Available episodes:** `.episode.available` class, teal left border
- **Coming soon:** `.episode` class only, gray left border, 0.85 opacity
- **Episode header:** Flexbox row with number, title, and duration (duration uses `margin-left: auto` to align right)
- **Episode summary:** 1-sentence description visible by default
- **Expandable details:** Native HTML `<details>` element with "More" summary text
- **Audio players:** Use `preload="none"` to keep page lightweight
- **Coming soon badge:** Yellow background with navy text, shown next to "Episodes" header for upcoming series

### Updating When Episodes Are Published

When an episode goes live:

1. Add `.available` class to the episode div
2. Change `.episode-duration` text from "Coming soon" to actual duration (e.g., "36:13")
3. Add the episode-links div with report and sources links
4. Add the audio element with correct source path
5. Remove "Coming Soon" badge from h2 when all episodes are available

## Working on Series Episodes

Once a series is planned with `research-prompt.md` files in each episode folder:

1. Open the episode's `research-prompt.md`
2. Copy the `/podcast-episode` command
3. Run the command to start the standard episode workflow
4. The episode will be created within the series directory structure
5. Update the series `index.html` to mark the episode as available
