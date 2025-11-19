# New Podcast Episode Workflow

You are helping create a new podcast episode following a structured research and production workflow.

## Episode Directory Structure

Each episode follows this organization:
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/
│   ├── sources.md          # Organized list of source links
│   ├── raw-notes.md        # NotebookLM/research tool outputs (optional)
│   ├── documents/          # PDFs, articles, downloads
│   └── assets/             # Images, charts, data files
├── report.md               # Final research report/show notes
├── script.md               # Episode script/outline (optional)
└── YYYY-MM-DD-topic-slug.mp3  # Final audio file
```

## Complete Workflow

### 1. Setup Phase

**Create a todo list** to track progress through the workflow.

**Ask the user:**
1. What date should we use? (YYYY-MM-DD format) - Offer today's date or custom
2. What's the episode slug? (e.g., "stablecoin-history") - Suggest options based on topic
3. What's the episode title? (e.g., "Stablecoin Market: Strategies and Pitfalls")

**Then create the directory structure:**
```bash
mkdir -p /Users/tomcounsell/src/protocols/podcast/episodes/YYYY-MM-DD-slug/research/{documents,assets}
```

### 2. Research Phase (User-led with your support)

**When user provides research:**
- Save the research report to `report.md`
- Create `research/sources.md` with this template:

```markdown
# Sources for [Episode Title]

## Research Tools Used
- Deep research tools
- NotebookLM

## Key Sources

### Primary Sources
<!-- Add links to regulatory documents, whitepapers, official announcements -->

### News & Analysis
<!-- Add links to news articles, analysis pieces, market reports -->

### Academic & Research Papers
<!-- Add links to academic papers, research reports -->

### Data Sources
<!-- Add links to market data, on-chain analytics, statistical sources -->

### Other References
<!-- Add any other relevant sources -->

---

## Notes
- Research compiled: YYYY-MM-DD
- Sources to be added as references are identified
```

**Ask user** if they have specific source URLs to add to sources.md.

### 3. AI Audio Generation Phase

**Generate podcast audio using NotebookLM:**

1. Upload research materials to NotebookLM (report.md and any source documents)

2. Use "Audio Overview" feature with this prompt:

```
Combine vivid storytelling with rigorous analysis - tell compelling stories AND extract the frameworks.

What to emphasize:
• Specific stories with concrete details - the decisions people made, what happened, and why
• Pattern recognition across stories - identify the underlying frameworks and principles
• Both micro (individual decisions) and macro (systemic dynamics) perspectives
• Technical depth where relevant - don't simplify for simplicity's sake
• Counter-intuitive insights and non-obvious connections between events

Target audience: High-IQ protocol builders, founders, investors, and researchers who want both narrative understanding and analytical frameworks.

Tone: Intellectually rigorous but engaging. Use stories to illustrate concepts, then zoom out to extract the patterns. Make it vivid enough to remember the examples, and analytical enough to understand the principles. Think "This happened to Terra/Do Kwon in 2020, which illustrates a broader principle about algorithmic stability..."

Balance the concrete and the abstract - neither dumbed down nor dry.
```

3. Select format: **Deep Dive** (or Brief/Critique/Debate as appropriate)
4. Select length: **Long** (or adjust based on topic complexity)
5. Generate and download the audio file

### 4. Audio File Processing Phase

**When user adds the generated audio file:**

1. **Check the format** - if it's .m4a, convert to .mp3:
   ```bash
   cd /Users/tomcounsell/src/protocols/podcast/episodes/YYYY-MM-DD-slug
   ffmpeg -i "original-file.m4a" -codec:a libmp3lame -b:a 128k "YYYY-MM-DD-slug.mp3" -y
   ```

2. **Get file metadata:**
   - File size in bytes: `ls -l file.mp3 | awk '{print $5}'`
   - Duration is shown in ffmpeg output (format: HH:MM:SS)

3. **Note the metadata** - you'll need:
   - File size (bytes)
   - Duration (MM:SS or HH:MM:SS format)

4. **Optional: Generate chapters with local Whisper transcription**

   Run the chapter generation tool (requires first-time setup of dependencies):

   ```bash
   cd /Users/tomcounsell/src/protocols/podcast/tools

   # First time only: install dependencies
   pip install -r requirements.txt

   # Generate chapters (runs Whisper locally, uses Claude for titles)
   python generate_chapters.py ../episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3 --model base
   ```

   This will:
   - Transcribe the audio locally using Whisper (no API calls)
   - Generate chapter titles using Claude
   - Output chapter files for embedding in MP3

   **Whisper model options:**
   - `tiny`: Fastest, basic accuracy (~1-2 min for 30 min audio)
   - `base`: Fast, good accuracy (~5-10 min for 30 min audio) **[recommended]**
   - `small`: Slower, better accuracy (~15-20 min for 30 min audio)

   **Note:** This step requires `ANTHROPIC_API_KEY` to be set for chapter title generation. The transcription itself runs entirely locally.

### 5. Publishing Phase

**Ask user for episode-specific keywords:**
- What are 5-10 specific keywords for this episode?
- Examples: technology names, protocols, key concepts, events covered

**Update feed.xml:**

Add a new `<item>` block after the opening `<channel>` metadata and before the closing `</channel>` tag:

```xml
<!-- Episode N: Short Description -->
<item>
  <title>Episode Title Here</title>
  <description>Compelling 1-2 sentence description covering key topics and takeaways.</description>
  <pubDate>Day, DD Mon YYYY 12:00:00 GMT</pubDate>
  <enclosure url="https://yudame.github.io/protocols/podcast/episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3"
             length="FILE_SIZE_IN_BYTES"
             type="audio/mpeg"/>
  <guid>https://yudame.github.io/protocols/podcast/episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3</guid>
  <itunes:duration>MM:SS</itunes:duration>
  <itunes:explicit>no</itunes:explicit>
  <itunes:keywords>keyword1, keyword2, keyword3, specific-protocol, specific-concept</itunes:keywords>
</item>
```

**Date format for pubDate:** Use RFC 2822 format (e.g., "Tue, 19 Nov 2025 12:00:00 GMT")

**Note:** Podcast-level categories are Technology and Education. Each episode has unique keywords for discoverability.

### 6. Git Workflow

**Commit and push the episode:**

1. Check status and review changes:
   ```bash
   git status
   git diff feed.xml
   ```

2. Add files:
   ```bash
   git add podcast/feed.xml podcast/episodes/
   ```

3. Commit with descriptive message using heredoc:
   ```bash
   git commit -m "$(cat <<'EOF'
   feat: Add episode on [topic]

   - Add episode "[title]" covering [key topics]
   - Include comprehensive research report with [main sections]
   - Update feed.xml with episode metadata
   - Episode duration: MM:SS, covers [key highlights]
   EOF
   )"
   ```

4. Push to GitHub:
   ```bash
   git push
   ```

### 7. Verify Publishing

**Remind user to:**
1. Ensure GitHub Pages is enabled at: `https://github.com/yudame/protocols/settings/pages`
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)

2. Feed URL will be: `https://yudame.github.io/protocols/podcast/feed.xml`

3. Wait 2-3 minutes for GitHub Pages to deploy

## Important Notes

- **Always use TodoWrite** to track progress through these phases
- **Mark tasks complete** immediately after finishing each step
- **Use ffmpeg** for audio conversion (128kbps mp3 is recommended)
- **File sizes** - aim to keep episodes under 100MB
- **Commit messages** - use heredoc format for multi-line messages
- **User handles** - research (deep research tools, NotebookLM) and audio creation
- **You handle** - file organization, format conversion, feed.xml updates, git workflow

## Getting Started

When user wants to create a new episode, start with:
1. Create a todo list for tracking
2. Ask for episode date, slug, and title
3. Create directory structure
4. Wait for user's research materials
5. Guide through each subsequent phase
