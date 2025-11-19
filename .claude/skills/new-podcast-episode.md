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
├── YYYY-MM-DD-topic-slug.mp3          # Final audio file with chapters
├── YYYY-MM-DD-topic-slug_transcript.json  # Full Whisper transcript
├── YYYY-MM-DD-topic-slug_chapters.txt     # FFmpeg chapter format
└── YYYY-MM-DD-topic-slug_chapters.json    # Podcasting 2.0 format
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

4. **Generate transcript and chapters with local Whisper + Claude analysis**

   **First-time setup only:**
   ```bash
   cd /Users/tomcounsell/src/protocols/podcast/tools

   # Fix SSL certificates (macOS Python)
   /Applications/Python\ 3.12/Install\ Certificates.command

   # Install dependencies
   pip install -r requirements.txt
   ```

   **Transcription workflow:**

   a. Run local Whisper transcription (no API key needed):
   ```bash
   cd /Users/tomcounsell/src/protocols/podcast/tools
   python transcribe_only.py ../episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3 --model base
   ```

   **Whisper model options:**
   - `tiny`: Fastest (~1-2 min for 30 min audio), basic accuracy
   - `base`: **[recommended]** Fast (~5-10 min), good accuracy
   - `small`: Slower (~15-20 min), better accuracy

   b. Once transcription completes, analyze the transcript to identify major topic transitions and create 10-15 chapter markers

   c. Create chapter files in the episode directory:
      - `YYYY-MM-DD-slug_chapters.txt` - FFmpeg metadata format
      - `YYYY-MM-DD-slug_chapters.json` - Podcasting 2.0 format

   d. Embed chapters into the mp3 file:
   ```bash
   cd /Users/tomcounsell/src/protocols/podcast/episodes/YYYY-MM-DD-slug
   ffmpeg -i YYYY-MM-DD-slug.mp3 -i YYYY-MM-DD-slug_chapters.txt -map_metadata 1 -codec copy YYYY-MM-DD-slug_with_chapters.mp3 -y
   mv YYYY-MM-DD-slug_with_chapters.mp3 YYYY-MM-DD-slug.mp3
   ```

   **Chapter creation guidelines:**
   - Aim for 10-15 chapters for a 30-40 minute episode
   - Each chapter should be 2-4 minutes long
   - Chapter titles should be descriptive and capture the key topic/story
   - Include subtitles or key concepts after the main title when helpful
   - Analyze the full transcript to identify natural topic transitions

   **Note:**
   - Transcription runs 100% locally (free, private, no API)
   - The transcript JSON file can be large (300-400KB) - read in sections if needed
   - Chapters will appear in podcast apps that support them (Overcast, Pocket Casts, Apple Podcasts)

### 5. Publishing Phase

**Generate episode description with source links:**

a. Create compelling 1-2 sentence description:
   - Based on the research report and transcript
   - Highlight key topics, major stories/events covered, and main takeaways
   - Focus on what makes this episode valuable and what listeners will learn
   - Include link to full research report: `https://yudame.github.io/protocols/podcast/episodes/YYYY-MM-DD-slug/report.md`

b. Add validated source links:
   - Search for and validate 3-5 key official sources mentioned in the episode
   - Prioritize: official legislation/regulation, academic analysis, primary sources
   - Use WebSearch to find official URLs
   - Verify links are accessible with WebFetch when possible
   - Add "Key Sources:" section with validated links

   Example sources to validate:
   - Official legislation (congress.gov, official government sites)
   - Regulatory frameworks (ESMA, SEC, FSB, etc.)
   - Academic/central bank analysis (Fed papers, university research)
   - Primary documents (whitepapers, official announcements)

**Ask user for episode-specific keywords:**
- What are 5-10 specific keywords for this episode?
- Examples: technology names, protocols, key concepts, events covered
- These improve discoverability in podcast apps

**Update feed.xml:**

Add a new `<item>` block after the opening `<channel>` metadata and before the closing `</channel>` tag:

```xml
<!-- Episode N: Short Description -->
<item>
  <title>Episode Title Here</title>
  <description>Compelling 1-2 sentence description (full report: https://yudame.github.io/protocols/podcast/episodes/YYYY-MM-DD-slug/report.md) covering key topics and takeaways.

Key Sources:
• Official Source 1: [validated URL]
• Official Source 2: [validated URL]
• Official Source 3: [validated URL]
• Analysis/Research: [validated URL]</description>
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

2. Add all episode files (research, audio, transcript, chapters) and updated feed:
   ```bash
   git add podcast/feed.xml podcast/episodes/YYYY-MM-DD-slug/
   ```

   **Files to include:**
   - `report.md` - Research report
   - `research/sources.md` - Source links
   - `YYYY-MM-DD-slug.mp3` - Final audio with embedded chapters
   - `YYYY-MM-DD-slug_transcript.json` - Full transcript
   - `YYYY-MM-DD-slug_chapters.txt` - FFmpeg chapter format
   - `YYYY-MM-DD-slug_chapters.json` - Podcasting 2.0 format
   - Updated `feed.xml`

3. Commit with descriptive message using heredoc:
   ```bash
   git commit -m "$(cat <<'EOF'
   feat: Add episode on [topic]

   - Add episode "[title]" covering [key topics]
   - Include comprehensive research report with [main sections]
   - Generate full transcript using local Whisper (base model)
   - Create [N] chapter markers covering key topics
   - Embed chapters into mp3 for podcast app support
   - Update feed.xml with episode metadata
   - Episode duration: MM:SS, covers [key highlights]
   EOF
   )"
   ```

4. Push to GitHub:
   ```bash
   git push
   ```

5. GitHub Pages will automatically deploy changes in 2-3 minutes

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
- **Transcription** - Always generate transcript and chapters for every episode
- **Chapters** - Aim for 10-15 chapters, each 2-4 minutes, with descriptive titles
- **Episode descriptions** - Generate compelling 1-2 sentence descriptions based on research and transcript
- **Commit messages** - use heredoc format for multi-line messages
- **User handles** - research (deep research tools, NotebookLM) and audio creation
- **You handle** - file organization, format conversion, transcription, chapter generation, feed.xml updates, git workflow

## Getting Started

When user wants to create a new episode, start with:
1. Create a todo list for tracking
2. Ask for episode date, slug, and title
3. Create directory structure
4. Wait for user's research materials
5. Guide through each subsequent phase
