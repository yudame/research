# Series Management

This document describes how to plan, organize, and manage multi-episode podcast series.

## Overview

A series is a collection of related episodes that explore a topic area in depth. Series provide structure for listeners and enable deeper exploration than standalone episodes.

---

## Series Structure

### Directory Organization

```
podcast/episodes/
└── series-name/
    ├── README.md              # Series overview (optional)
    ├── ep1-topic-slug/        # Episode 1
    │   ├── research/
    │   ├── logs/
    │   ├── report.md
    │   ├── cover.png
    │   └── ep1-topic-slug.mp3
    ├── ep2-topic-slug/        # Episode 2
    │   └── ...
    └── epN-topic-slug/        # Episode N
        └── ...
```

### Naming Conventions

**Series Directory:**
- Format: `series-name` (lowercase, hyphenated)
- Examples: `cardiovascular-health`, `solomon-islands-telecom-series`

**Episode Directory:**
- Format: `epN-topic-slug`
- Examples: `ep1-foundations`, `ep2-therapies`

**Episode Title:**
- Format: `Series Name: Ep. N, Topic Title`
- Example: `Cardiovascular Health: Ep. 2, VO2 Max`

---

## Planning a Series

### Step 1: Discovery Research

Before creating episodes, research the topic area:

1. Identify key subtopics
2. Determine logical progression
3. Assess content depth needed
4. Estimate episode count (4-8 recommended)

### Step 2: Episode Planning

For each planned episode, define:

| Element | Description |
|---------|-------------|
| Episode number | Position in series |
| Title | Topic focus |
| Core questions | 3-5 research questions |
| Dependencies | What must come before |
| Unique angle | What makes this episode distinct |

### Step 3: Series Architecture

Determine the narrative arc:

**Linear Progression:**
- Episode 1: Foundations
- Episode 2-N-1: Deep dives
- Episode N: Integration/conclusion

**Topic Clusters:**
- Related topics grouped
- Can be consumed in any order
- Each episode stands alone

**Problem-Solution:**
- Episodes 1-2: Problem definition
- Episodes 3-N-1: Solutions
- Episode N: Synthesis

---

## Series Metadata in RSS Feed

### iTunes Tags

For series episodes, use season/episode numbering:

| Element | Usage |
|---------|-------|
| `<itunes:season>` | Series number (1, 2, 3...) |
| `<itunes:episode>` | Episode within series |
| `<itunes:episodeType>` | "full" for standard episodes |

### Custom Tags

Track series identity:

| Element | Usage |
|---------|-------|
| `<research:series>` | Series name string |

### Example

```xml
<itunes:season>2</itunes:season>
<itunes:episode>4</itunes:episode>
<research:series>Active Recovery Series</research:series>
```

---

## Season Numbering

### Assigning Season Numbers

Each distinct series gets a unique season number:

| Season | Series |
|--------|--------|
| 1 | Kindergarten First Principles |
| 2 | Active Recovery |
| 3 | Cardiovascular Health |
| 4 | Solomon Islands Telecom |
| 5 | Stablecoin Series |
| ... | ... |

### Benefits

- Podcast apps group episodes by season
- Users can easily find series
- Clear organization in player interfaces

---

## Series Visual Identity

### Cover Art Consistency

Maintain visual consistency across series:

| Element | Consistency |
|---------|-------------|
| Color palette | Same for all episodes |
| Logo placement | Consistent position |
| Typography | Same fonts |
| Style | Unified visual language |

### Episode Differentiation

Distinguish episodes while maintaining series identity:

- Episode number in text overlay
- Topic-specific imagery
- Same color scheme, different subject

---

## Creating Series Episodes

### Workflow Modification

When creating series episodes:

1. **Use series directory** - Place in `podcast/episodes/series-name/`
2. **Follow episode naming** - Use `epN-topic-slug` format
3. **Include series metadata** - Add season, episode, series tags
4. **Maintain consistency** - Reference previous episodes

### Research Continuity

For series episodes:

- Review previous episode reports
- Build on established findings
- Avoid redundant research
- Cross-reference within series

---

## Example Series Structures

### Educational Series (Kindergarten First Principles)

```
1. Development overview
2. Physical development
3. Cognitive development
4. Socialization
5. Language & literacy
6. Educational frameworks
```

Progression: Foundation to application

### Technical Series (Stablecoin)

```
1. Market evolution
2. Legal compliance
3. Token economics
4. Technical architecture
5. Reserve management
6. Liquidity partnerships
7. Go-to-market
8. Post-launch operations
```

Progression: Concept to implementation to operation

### Health Series (Cardiovascular)

```
1. Lifestyle foundations
2. VO2 Max
3. Heart rate variability
4. Supplementation
```

Progression: Basic to advanced, general to specific

### Regional Series (Solomon Islands Telecom)

```
1. Financial infrastructure
2. Breaking duopoly
3. Infrastructure advantage
4. Mobile money
5. Launch execution
6. Smartphone frontier
```

Progression: Context to strategy to execution to future

---

## Managing Multiple Series

### Interleaving Episodes

When publishing from multiple series:

- Maintain consistent publishing schedule
- Don't abandon series mid-stream
- Complete series before starting new ones (preferred)
- Or explicitly plan interleaved releases

### Series Status Tracking

Track each series:

| Series | Episodes Planned | Episodes Published | Status |
|--------|------------------|-------------------|--------|
| Active Recovery | 4 | 4 | Complete |
| Stablecoin | 8 | 8 | Complete |
| New Series | 6 | 2 | In Progress |

---

## Series Planning Workflow

Entry point: `/podcast-series [topic-area]`

### Phase 1: Discovery

1. Research topic area broadly
2. Identify 4-8 subtopics
3. Determine logical sequence
4. Draft episode outlines

### Phase 2: Structure

1. Create series directory
2. Create subdirectories for each episode
3. Write episode briefs
4. Plan research approach per episode

### Phase 3: Execution

1. Create episodes sequentially
2. Maintain continuity between episodes
3. Cross-reference previous findings
4. Build toward series conclusion

---

## Series Completion Checklist

Before marking series complete:

- [ ] All planned episodes published
- [ ] Consistent naming across episodes
- [ ] Season/episode numbers correct
- [ ] Series name consistent in all metadata
- [ ] Visual identity maintained
- [ ] Cross-references between episodes
- [ ] Final episode provides conclusion/integration
