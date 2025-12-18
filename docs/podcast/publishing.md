# Publishing

This document describes the RSS feed structure, publishing process, and GitHub Pages deployment.

## Overview

The Yudame Research Podcast is self-hosted on GitHub Pages with an RSS 2.0 feed that includes iTunes and Podcasting 2.0 extensions for maximum platform compatibility.

**Feed URL:** `https://research.yuda.me/podcast/feed.xml`

**Website:** `https://research.yuda.me/`

---

## RSS Feed Structure

### XML Namespaces

The feed declares these namespaces:

| Namespace | URI | Purpose |
|-----------|-----|---------|
| itunes | http://www.itunes.com/dtds/podcast-1.0.dtd | Apple Podcasts compatibility |
| content | http://purl.org/rss/1.0/modules/content/ | Rich HTML content |
| podcast | https://podcastindex.org/namespace/1.0 | Podcasting 2.0 features |
| research | https://research.yuda.me/namespace/1.0 | Custom series tracking |

### Channel Metadata

Required channel-level elements:

| Element | Value |
|---------|-------|
| `<title>` | Yudame Research Podcast |
| `<link>` | https://research.yuda.me/ |
| `<description>` | Podcast description |
| `<language>` | en-us |
| `<copyright>` | (c) 2025 Yudame Inc. |
| `<managingEditor>` | valor@yuda.me (Valor Engels) |
| `<webMaster>` | valor@yuda.me (Valor Engels) |
| `<lastBuildDate>` | RFC 2822 date |
| `<ttl>` | 1440 (daily refresh) |
| `<itunes:author>` | Valor Engels |
| `<itunes:owner>` | Contact information |
| `<itunes:explicit>` | no |
| `<itunes:category>` | Science, Education, Technology |
| `<itunes:image>` | Channel cover art URL |
| `<itunes:type>` | episodic |

### Episode Item Structure

Each `<item>` must contain:

**Core Elements:**

| Element | Description |
|---------|-------------|
| `<title>` | Episode title |
| `<description>` | Plain text with report link |
| `<content:encoded>` | HTML CDATA with clickable links |
| `<author>` | valor@yuda.me (Valor Engels) |
| `<pubDate>` | RFC 2822 format date |
| `<enclosure>` | Audio file URL, length, type |
| `<guid>` | Episode audio file URL |

**iTunes Elements:**

| Element | Description |
|---------|-------------|
| `<itunes:author>` | Valor Engels |
| `<itunes:duration>` | HH:MM:SS or MM:SS |
| `<itunes:explicit>` | no |
| `<itunes:episodeType>` | full |
| `<itunes:image>` | Episode cover URL |
| `<itunes:keywords>` | Comma-separated keywords |

**Series Elements (for series episodes):**

| Element | Description |
|---------|-------------|
| `<itunes:season>` | Season number |
| `<itunes:episode>` | Episode number |
| `<research:series>` | Series name string |
| `<podcast:chapters>` | Chapters JSON URL |

---

## Episode Item Template

```xml
<item>
  <title>Series Name: Ep. N, Episode Topic</title>
  <description>
    Episode description text...
    Full research report: https://research.yuda.me/podcast/episodes/path/report.md
  </description>
  <content:encoded><![CDATA[
    <p>Episode description with HTML formatting...</p>
    <p><strong>Key Sources:</strong></p>
    <ul>
      <li><a href="https://example.com">Source Name</a></li>
    </ul>
  ]]></content:encoded>
  <author>valor@yuda.me (Valor Engels)</author>
  <pubDate>Mon, 16 Dec 2025 09:00:00 GMT</pubDate>
  <enclosure
    url="https://research.yuda.me/podcast/episodes/path/filename.mp3"
    length="30608776"
    type="audio/mpeg"/>
  <guid>https://research.yuda.me/podcast/episodes/path/filename.mp3</guid>
  <itunes:author>Valor Engels</itunes:author>
  <itunes:duration>31:53</itunes:duration>
  <itunes:explicit>no</itunes:explicit>
  <itunes:episodeType>full</itunes:episodeType>
  <itunes:image href="https://research.yuda.me/podcast/episodes/path/cover.png"/>
  <itunes:season>1</itunes:season>
  <itunes:episode>4</itunes:episode>
  <itunes:keywords>keyword1, keyword2, keyword3</itunes:keywords>
  <research:series>Series Name</research:series>
  <podcast:chapters
    url="https://research.yuda.me/podcast/episodes/path/filename_chapters.json"
    type="application/json+chapters"/>
</item>
```

---

## Publishing Process

### Step 1: Gather Metadata

Collect required information:

| Metadata | Source | Format |
|----------|--------|--------|
| File size | File system | Bytes (integer) |
| Duration | FFmpeg output | MM:SS or HH:MM:SS |
| Episode title | Report/planning | Text |
| Description | Report | Text |
| Keywords | Report content | Comma-separated |
| Sources | Report | URLs |

### Step 2: Create Episode Item

Build the `<item>` XML block with all required elements:

1. Write title following naming convention
2. Create plain text description with report link
3. Create HTML content:encoded with source links
4. Set pubDate in RFC 2822 format
5. Set enclosure with exact file size
6. Use audio URL as guid
7. Add all iTunes elements
8. Add series elements if applicable
9. Add chapters link if available

### Step 3: Insert Into Feed

Insert the new `<item>` block:

- Location: After `<channel>` metadata, before existing episodes
- Feed type is episodic (newest first)
- Update `<lastBuildDate>` to current date

### Step 4: Validate Feed

Before committing, validate:

- Valid XML structure (no syntax errors)
- All required elements present
- File size matches actual file (in bytes)
- Duration format correct
- pubDate in RFC 2822 format
- All URLs accessible
- Source links functional

### Step 5: Commit and Push

Commit changes with descriptive message:

```
feat: Add Episode Title to podcast feed

- Add new episode: Series Name Ep. N
- Duration: MM:SS, Size: XX MB
- Includes chapters and cover art
```

### Step 6: Verify Deployment

After pushing:

1. Wait 2-3 minutes for GitHub Pages deployment
2. Check feed URL loads correctly
3. Verify new episode appears
4. Test audio file accessibility
5. Check cover art displays

---

## GitHub Pages Configuration

### Setup

| Setting | Value |
|---------|-------|
| Source | Main branch |
| Folder | Root (/) |
| Custom domain | research.yuda.me |
| HTTPS | Enforced |

### Configuration Files

| File | Purpose |
|------|---------|
| `.nojekyll` | Disable Jekyll processing |
| `CNAME` | Custom domain configuration |

### Deployment

- Automatic on push to main branch
- Typically completes in 2-3 minutes
- Check Actions tab for deployment status

---

## Date Formatting

### RFC 2822 Format

All dates in feed must use RFC 2822 format:

```
Day, DD Mon YYYY HH:MM:SS GMT
```

Examples:
- `Mon, 16 Dec 2025 09:00:00 GMT`
- `Thu, 05 Dec 2025 12:00:00 GMT`

### Duration Format

Use HH:MM:SS or MM:SS:

- `44:05` for 44 minutes 5 seconds
- `1:15:30` for 1 hour 15 minutes 30 seconds

---

## URL Structure

### Base URL

`https://research.yuda.me/`

### Feed URL

`https://research.yuda.me/podcast/feed.xml`

### Episode URLs

**Audio:**
`https://research.yuda.me/podcast/episodes/[path]/[filename].mp3`

**Cover Art:**
`https://research.yuda.me/podcast/episodes/[path]/cover.png`

**Chapters:**
`https://research.yuda.me/podcast/episodes/[path]/[filename]_chapters.json`

**Report:**
`https://research.yuda.me/podcast/episodes/[path]/report.md`

---

## Feed Validation

### Validation Tools

- Cast Feed Validator: castfeedvalidator.com
- Podbase Validator: podba.se/validate/
- Apple Podcasts Connect: Built-in validation

### Manual Validation Checklist

**XML Structure:**
- [ ] Valid XML syntax
- [ ] All tags properly closed
- [ ] CDATA sections formatted correctly
- [ ] Special characters escaped

**Channel Level:**
- [ ] All required elements present
- [ ] lastBuildDate current
- [ ] Image URL accessible

**Episode Level:**
- [ ] Title follows convention
- [ ] Description includes report link
- [ ] content:encoded has clickable sources
- [ ] pubDate is RFC 2822
- [ ] enclosure length matches file
- [ ] Duration is accurate
- [ ] GUID is unique

---

## Description Best Practices

### Plain Text Description

```
Brief episode hook (1-2 sentences).
Full research report: https://research.yuda.me/podcast/episodes/[path]/report.md
```

### HTML Content (content:encoded)

```html
<p>Episode description with more detail...</p>
<p><strong>Key Sources:</strong></p>
<ul>
  <li><a href="https://official-source.com">Official Source Name</a></li>
  <li><a href="https://academic-paper.com">Academic Paper Title</a></li>
  <li><a href="https://government-doc.gov">Government Document</a></li>
</ul>
```

### Source Selection

Prioritize for Key Sources section:
1. Official legislation/regulation
2. Peer-reviewed academic papers
3. Government documents
4. Primary sources
5. Authoritative industry reports

Validate all URLs before publishing.

---

## Subscription Support

### Platform Instructions

Provide subscription instructions for:

- Apple Podcasts (direct RSS support)
- Overcast
- Pocket Casts
- Castro
- Podcast Addict (Android)
- AntennaPod (Android)
- Web RSS readers

### Subscription Page

`podcast/subscribe.html` provides:
- Platform-specific instructions
- RSS URL display with copy button
- Troubleshooting guidance

---

## Troubleshooting

### Feed Not Updating

**Problem:** New episode doesn't appear
**Solution:** Check GitHub Pages deployment status, wait 2-3 minutes, hard refresh

### Invalid XML

**Problem:** Feed validator shows errors
**Solution:** Check for unescaped special characters, verify all tags closed

### Audio Not Playing

**Problem:** Episode won't play in apps
**Solution:** Verify enclosure URL is correct and accessible, check file permissions

### Image Not Displaying

**Problem:** Cover art missing
**Solution:** Check image URL, verify file was committed, check file size
