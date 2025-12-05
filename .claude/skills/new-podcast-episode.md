# New Podcast Episode Workflow

You are helping create a new podcast episode following a structured research and production workflow.

## Episode Directory Structure

Each episode follows a flat organization with 5 core markdown files at the top level:
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── prompts.md              # All prompts used during episode creation
├── research-results.md     # Raw research outputs from ChatGPT, Perplexity, etc.
├── sources.md              # Organized list of source links
├── report.md               # Final research report/show notes
├── publish.md              # RSS feed content (title, description, keywords, sources)
├── documents/              # Supporting files (PDFs, articles) - only if needed
├── review-notes.md         # Episode review for continuous improvement (optional)
├── cover.png               # Episode cover art with branding (~500KB)
├── YYYY-MM-DD-topic-slug.mp3          # Final audio file with chapters (~30MB)
├── YYYY-MM-DD-topic-slug_transcript.json  # Full Whisper transcript (~400KB)
├── YYYY-MM-DD-topic-slug_chapters.txt     # FFmpeg chapter format (~2KB)
└── YYYY-MM-DD-topic-slug_chapters.json    # Podcasting 2.0 format (~1KB)
```

### Example: Completed Episode

```
podcast/episodes/2025-11-19-stablecoin-history/
├── prompts.md                        # All prompts used during creation
├── research-results.md               # Raw outputs from ChatGPT/Perplexity
├── sources.md                        # 14 validated source links
├── report.md                         # 25KB - comprehensive research report
├── publish.md                        # RSS feed content for this episode
├── cover.png                         # Episode cover art with branding
├── 2025-11-19-stablecoin-history.mp3 # 30MB - 32:41 duration, 128kbps
├── 2025-11-19-stablecoin-history_transcript.json      # 403KB - full transcript
├── 2025-11-19-stablecoin-history_chapters.txt         # 2KB - 14 chapters
└── 2025-11-19-stablecoin-history_chapters.json        # 1KB - 14 chapters

Plus original audio files (can keep for archival):
├── Stablecoins_Global_Rules_Failure_and_Genius_Act.m4a  # Original from NotebookLM
```

## Series Episodes

For planning multi-episode series, see `.claude/skills/podcast-series.md`.

This skill focuses on standalone episodes. Series episodes follow the same workflow once the series structure is created.

## Complete Workflow

### 1. Setup Phase

**Create a todo list** to track progress through the workflow:

```
Use TodoWrite to create initial todos:
- Setup episode structure and files (status: in_progress)
- Synthesize research into report.md (status: pending)
- Generate cover art (status: pending)
- Obtain audio from NotebookLM (status: pending)
- Process audio (transcribe, chapters) (status: pending)
- Create publishing metadata (status: pending)
- Update feed.xml and commit (status: pending)
```

**Ask the user:**
1. **Is this part of a series?**
   - If YES: Ask for series name and episode number
   - If NO: Create standalone episode
2. What date should we use? (YYYY-MM-DD format) - Offer today's date or custom
3. What's the episode topic/slug? (e.g., "lifestyle", "vo2-max", "supplementation")
4. What's the episode title?
   - **For series:** "Series Name: Ep. X, Topic" (e.g., "Cardiovascular Health: Ep. 1, Lifestyle Foundations")
   - **For standalone:** Descriptive title (e.g., "Stablecoin Market: Strategies and Pitfalls")

**Create the appropriate directory structure:**

**For series episodes:**
```bash
mkdir -p ~/src/research/podcast/episodes/series-name/epX-topic-slug
```

**For standalone episodes:**
```bash
mkdir -p ~/src/research/podcast/episodes/YYYY-MM-DD-topic-slug
```

### 2. Research Phase (User-led with your support)

**Help user craft a deep research prompt:**

Before the user conducts research, help them create a focused research prompt for tools like Claude, Gemini, ChatGPT, Perplexity, Grok, or other deep research tools.

**Research prompt principles:**
- Start with the user's topic and refine it into a clear research question
- Keep the prompt concise - focus on gathering quality information, not prescribing structure
- Avoid preconceived assumptions about results or predetermined frameworks
- Emphasize research methodology over expected outcomes

**Template for research prompts:**
```
Research [topic/question].

**Context:** [Specific constraints, target audience, or parameters]

**Research methodology:**
- Prioritize peer-reviewed studies, meta-analyses, and authoritative sources
- Distinguish between correlation and causation in findings
- Report effect sizes and practical significance, not just statistical significance
- Note the study populations and whether findings generalize to the target demographic
- Compare individual studies against meta-analyses and systematic reviews
- Identify preliminary research vs. well-replicated findings
- Note funding sources and potential conflicts of interest when relevant
- Include contradictory findings and areas of scientific uncertainty
- Cite specific studies, researchers, and sources throughout

**Output:** Comprehensive research report with extensive citations and source links.
```

**Key point:** Let the research lead where the evidence goes. Don't impose structure or conclusions upfront.

**Now create all episode files and directories:**

```bash
mkdir -p ~/src/research/podcast/episodes/YYYY-MM-DD-slug
```

**Create prompts.md to track all prompts used:**

Create `prompts.md` with this template:
```markdown
# Prompts Used for Episode: [Episode Title]

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

---

## Setup Phase

**Episode Details:**
- Date: YYYY-MM-DD
- Slug: topic-slug
- Title: [Episode Title]

---

## Research Phase

### Research Prompt

**Tool Used:** [e.g., Claude, Gemini, ChatGPT, Perplexity, Grok, etc.]

**Prompt:**
```
[The research prompt will be added here]
```

**Date:** YYYY-MM-DD

---

<!-- Additional prompts will be added below as we progress through the workflow -->
```

**Create research results collection file:**

Create `research-results.md` with this template:
```markdown
# Research Results for [Episode Title]

This file is for pasting research results from external tools (Claude, Gemini, ChatGPT, Perplexity, Grok, etc.).

---

## Research from ChatGPT

<!-- Paste ChatGPT research results here -->

---

## Research from Perplexity

<!-- Paste Perplexity research results here -->

---

## Research from Other Tools

<!-- Paste any other research results here -->

---

## Notes

- Research conducted: YYYY-MM-DD
- Tools used: [List tools used]
- Raw outputs saved here for reference and verification
```

**Create initial sources.md file:**

Create `sources.md` with this template:
```markdown
# Sources for [Episode Title]

## Research Tools Used
- [List tools used: ChatGPT, Perplexity, NotebookLM, etc.]

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

**Save the research prompt to prompts.md:**

Add the actual research prompt to the Research Phase section in `prompts.md`.

**Inform the user:**
"Episode structure created! You can now:
1. Paste research results into `research-results.md` as you gather them from ChatGPT, Perplexity, etc.
2. Let me know when research is complete and I'll synthesize everything into report.md"

**Update todos:**
```
Mark "Setup episode structure and files" as completed.
Mark "Synthesize research into report.md" as in_progress.
```

---

**When user provides research:**

1. **Save raw research** to `research-results.md`

2. **Immediately synthesize into report.md** - Do NOT ask the user if they want this done. Automatically consolidate the research into a cohesive report focusing on:
   - Key findings and insights
   - Storytelling opportunities (dramatic events, surprising facts, human elements)
   - Practical implications and frameworks
   - Specific examples, case studies, and real-world events
   - Data points and statistics that illustrate key concepts

   **Report structure should support podcast narrative:**
   - Lead with the most compelling/surprising elements
   - Group related topics that flow naturally in conversation
   - Highlight contrasts and comparisons (before/after, success/failure, etc.)
   - Include specific names, dates, and numbers for credibility
   - Note areas of uncertainty or debate

3. **Update `sources.md`** with sources identified from the research

4. **Immediately provide the NotebookLM prompt** - Don't wait for user to ask. After report.md is ready:
   - Add the NotebookLM prompt to `prompts.md` (Audio Generation Phase section)
   - Output the full NotebookLM prompt for the user to copy
   - List which files to upload to NotebookLM
   - User can then proceed directly to audio generation

**Update todos:**
```
Mark "Synthesize research into report.md" as completed.
Mark "Generate cover art" as in_progress.
Mark "Obtain audio from NotebookLM" as in_progress (user's parallel task).
```

5. **Generate cover art while user works on audio** - Don't wait for audio to complete:
   - Invoke the cover art generation subagent
   - This can be done in parallel while NotebookLM generates audio

### 3. Cover Art Generation Phase

**Immediately invoke the cover art subagent** to work in parallel while user creates audio in NotebookLM.

Use the Task tool to invoke the `podcast-cover-art` skill:

```
Generate podcast cover art for this episode using the podcast-cover-art skill.

Episode path: podcast/episodes/YYYY-MM-DD-slug
Episode title: [Full episode title]
Series name: [Series name, or "None" for standalone episodes]
Episode text: [Text for branding overlay, e.g., "Ep 3 - Sleep & Memory"]

Follow the podcast-cover-art skill to:
1. Generate AI cover art with Gemini via OpenRouter
2. Apply podcast branding (logo, text, border)
3. Log to prompts.md
4. Report back when complete with file path and size
```

**When cover art subagent completes, update todos:**
```
Mark "Generate cover art" as completed.
```

### 4. AI Audio Generation Phase

**Generate podcast audio using NotebookLM:**

1. Upload ALL research files to NotebookLM:
   - `report.md` (overview/summary)
   - `research-results.md` (raw research outputs)
   - Any source documents (PDFs, articles) in `documents/` if present

   **User uploads ALL files** - NotebookLM will synthesize across all sources

2. Use "Audio Overview" feature with this prompt:

**IMPORTANT: This is the STANDARD TEMPLATE - use it as-is. DO NOT customize with specific content, narrative arcs, or story suggestions. The prompt defines QUALITY GUIDELINES for Yudame episodes, not content prescription. NotebookLM will synthesize the research files naturally.**

```
Create an intellectually rigorous podcast that balances analytical depth with clear explanation.

Opening: Begin with "Yudame Research" (add series name if applicable) and introduce the topic's value.

Core principles:
• Spell out acronyms first: "High-Intensity Interval Training, or HIIT" - then use acronym
• Define technical terms immediately in plain language before building on them
• Use concrete examples ONLY from source material - never fabricate
• Highlight findings that reveal strategic lessons or challenge assumptions
• Extract frameworks and connect to practical implications
• Maintain scientific rigor: distinguish correlation from causation, note effect sizes and uncertainties

Emphasis areas:
• Spell-first for acronyms, definition-first for technical terms
• Evidence-based analysis: cite studies, report effect sizes, note sample sizes
• Include human elements when they exist: decisions made, reasoning, outcomes
• Use conversational check-ins: "Let me define that term..." or "To be clear..."
• Translate findings to practical meaning and broader patterns

Highlight insights worth examining:
• Counter-intuitive findings that reveal strategic lessons
• Failures that illustrate specific mistakes or systemic issues
• Unexpected outcomes that challenge assumptions
• Make numbers meaningful through context and comparisons

Avoid:
• Undefined acronyms and jargon
• Academic language when simpler words work
• Introducing 3+ new technical terms in one sentence
• Fabricated examples or over-hedging that obscures findings
• Dry explanations when human stories exist in research
• Repeatedly restating context

Target: Intelligent listeners wanting deep understanding and practical insights. Appreciate technical depth but need terms defined.

Tone: Intellectually rigorous but accessible - "conversational expert explaining to a bright student"

When presenting stories:
• Include decision-making context: "Do Kwon announced X, which led to Y" not "The protocol experienced stress"
• Provide specific details: "On Friday afternoon, Circle announced..." not "Circle had exposure"
• Use precise numbers for context: "$3.3 billion frozen over a weekend" not "some funds were inaccessible"
• Show scale through comparisons: "Supply increased from millions to trillions - a thousand-fold change"
• Connect to lessons: Explain what the outcome reveals about systems, incentives, or strategy

When presenting research: Focus on what numbers mean, use comparisons ("like losing 5 years of profits"), translate statistics to implications.

Closing: Summarize 2-3 key takeaways, close with "Find full research and sources at research dot yuda dot me - that's Y-U-D-A dot M-E"
```

**Only customization allowed:** Update the series name in "Opening" and "Closing" sections if this is a series episode.

3. Select format: **Deep Dive** (or Brief/Critique/Debate as appropriate)
4. Select length: **Long** (or adjust based on topic complexity)
5. Generate and download the audio file

**Log to prompts.md:** Note the files uploaded and any customizations to the default prompt.

**User returns with the generated audio file from NotebookLM** - Now proceed to audio processing.

**Update todos:**
```
Mark "Obtain audio from NotebookLM" as completed.
Mark "Process audio (transcribe, chapters)" as in_progress.
```

### 5. Audio File Processing Phase

**When user provides audio file, invoke the audio processing subagent.**

Use the Task tool to invoke the `podcast-audio-processing` skill:

```
Process the podcast audio file for this episode using the podcast-audio-processing skill.

Episode path: podcast/episodes/YYYY-MM-DD-slug
Audio filename: [filename user provided, e.g., 'Original_Audio.m4a']
Episode slug: YYYY-MM-DD-slug

Follow the podcast-audio-processing skill to:
1. Convert to mp3 if needed (m4a → mp3)
2. Get file metadata (size in bytes, duration)
3. Transcribe with local Whisper (base model)
4. Analyze transcript and create 10-15 chapter markers
5. Embed chapters into mp3
6. Log to prompts.md

CRITICAL: Report back the file metadata when complete:
- Duration: MM:SS format
- File size: bytes
This metadata is needed for the publishing phase.
```

**When audio processing subagent completes, update todos:**
```
Mark "Process audio (transcribe, chapters)" as completed.
Mark "Create publishing metadata" as in_progress.
```

### 6. Publishing Phase

**Generate episode description, keywords, and source links:**

a. **Create compelling 1-2 sentence description (plain text):**
   - Based on the research report and transcript
   - Highlight key topics, major stories/events covered, and main takeaways
   - Focus on what makes this episode valuable and what listeners will learn
   - Keep this version plain text for the `<description>` tag
   - Include link to full research report: `https://research.yuda.me/podcast/episodes/YYYY-MM-DD-slug/report.md`

b. **Generate episode-specific keywords (5-10 keywords):**
   - Analyze the research report, transcript, and chapter titles
   - Extract the most important concepts, terms, protocols, people, events mentioned
   - Prioritize: specific technical terms, proper nouns, key concepts, frameworks
   - Examples: "VO2 max", "HRV", "stablecoins", "Terra Luna", "GENIUS Act", "sleep quality"
   - Format as comma-separated list for iTunes keywords field

c. **Add validated source links (3-5 sources):**
   - Search for and validate 3-5 key official sources mentioned in the episode
   - Prioritize: official legislation/regulation, academic analysis, primary sources
   - Use WebSearch to find official URLs
   - Verify links are accessible with WebFetch when possible
   - These will be formatted as clickable HTML links in `<content:encoded>`

   Example sources to validate:
   - Official legislation (congress.gov, official government sites)
   - Regulatory frameworks (ESMA, SEC, FSB, etc.)
   - Academic/central bank analysis (Fed papers, university research)
   - Primary documents (whitepapers, official announcements)
   - Peer-reviewed studies (PubMed, academic journals)

**Create publish.md with all RSS feed content:**

Create `publish.md` in the episode directory with this template:
```markdown
# Episode Publishing Info

## Title
[Episode Title]

## Publication Date
[Day, DD Mon YYYY HH:MM:SS GMT - RFC 2822 format]

## Series Info (if applicable)
- **Series Name:** [Series Name]
- **Season Number:** [N]
- **Episode Number:** [N]

## Audio
- **Duration:** [HH:MM:SS or MM:SS]
- **File Size:** [bytes]
- **Format:** audio/mpeg

## Description (Plain Text)
[1-2 sentence compelling description covering key topics and takeaways.]

Full research report: https://research.yuda.me/podcast/episodes/[path]/report.md

## Key Sources (for HTML show notes)
- [Source Name]: [URL]
- [Source Name]: [URL]
- [Source Name]: [URL]
- [Source Name]: [URL]
- [Source Name]: [URL]

## Keywords
[keyword1, keyword2, keyword3, specific-term, specific-concept]
```

**Update feed.xml using Yudame RSS standards:**

Add a new `<item>` block to feed.xml following the specification in `docs/RSS-specification.md`:

**Required elements for ALL episodes:**
- `<title>` - Episode title
- `<description>` - Plain text description (from publish.md)
- `<content:encoded>` - HTML-formatted show notes with clickable source links (CDATA wrapped)
- `<author>valor@yuda.me (Valor Engels)</author>`
- `<pubDate>` - RFC 2822 format
- `<enclosure>` - url, length (bytes), type="audio/mpeg"
- `<guid>` - Episode audio file URL
- `<itunes:author>Valor Engels</itunes:author>`
- `<itunes:duration>` - HH:MM:SS format
- `<itunes:explicit>no</itunes:explicit>`
- `<itunes:episodeType>full</itunes:episodeType>` (or trailer/bonus)
- `<itunes:keywords>` - From publish.md
- `<itunes:image>` - Episode cover art with version param

**Additional for SERIES episodes:**
- `<itunes:season>N</itunes:season>`
- `<itunes:episode>N</itunes:episode>`
- `<research:series>Series Name</research:series>`

**Format content:encoded with HTML:**
```xml
<content:encoded><![CDATA[
  <p>[Description paragraph]</p>
  <p><strong>Full research report:</strong> <a href="https://research.yuda.me/podcast/episodes/path/report.md">report.md</a></p>
  <p><strong>Key Sources:</strong></p>
  <ul>
    <li><a href="url">Source Name</a></li>
    <li><a href="url">Source Name</a></li>
  </ul>
]]></content:encoded>
```

**Invoke feed validation subagent:**

After updating feed.xml, use the Task tool to validate against standards:

```
Validate the podcast feed against RSS specification standards using the podcast-feed-validator skill.

Feed path: podcast/feed.xml
Specification path: docs/RSS-specification.md

Follow the podcast-feed-validator skill to:
1. Read the RSS specification quality checklist (Section 8)
2. Validate the new episode entry against all requirements
3. Check for: required tags, proper formatting, series metadata (if applicable), content:encoded HTML structure
4. Verify file sizes and durations match actual files
5. Report any missing or incorrect elements
6. Confirm feed is valid XML
```

**Update todos:**
```
Mark "Create publishing metadata" as completed.
Mark "Update feed.xml and commit" as in_progress.
```

### 7. Git Workflow

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
   - `prompts.md` - All prompts used during creation
   - `research-results.md` - Raw research outputs
   - `sources.md` - Source links
   - `report.md` - Research report
   - `publish.md` - RSS feed content
   - `cover.png` - Episode cover art with branding
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
   - Generate AI cover art with Gemini via OpenRouter and apply podcast branding
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

**Update todos:**
```
Mark "Update feed.xml and commit" as completed.
All episode workflow tasks complete!
```

### 8. Verify Publishing

**Remind user to:**
1. Ensure GitHub Pages is enabled at: `https://github.com/yudame/research/settings/pages`
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)

2. Feed URL will be: `https://research.yuda.me/podcast/feed.xml`

3. Wait 2-3 minutes for GitHub Pages to deploy

### 9. Episode Review (Optional - for continuous improvement)

**After listening to the episode, optionally create a review file to track improvements:**

Create `review-notes.md` in the episode directory:
```markdown
# Episode Review: [Episode Title]

## Listen Date
YYYY-MM-DD

## What Worked Well
- [Specific examples of good explanations, storytelling, pacing, etc.]

## Areas for Improvement
- [Specific examples where definitions were missing, jargon was confusing, etc.]

## Technical Term Analysis
**Terms that needed better definition:**
- [Term] - First mentioned at [timestamp] without clear definition
- [Term] - Used multiple times but never defined

**Terms that were well explained:**
- [Term] - Good clear definition when introduced

## Story/Example Quality
**Effective examples:**
- [Description and why it worked]

**Missing opportunities:**
- [Where a concrete example would have helped]

**Fabricated or speculative content:**
- [Any content that wasn't grounded in the research]

## Prompt Improvements for Next Time
Based on this episode, consider adjusting:
- [Specific prompt modifications]
- [Research focus areas]
- [NotebookLM guidance]

## Action Items
- [ ] Update NotebookLM prompt if needed
- [ ] Adjust research prompt template
- [ ] Note patterns for future episodes
```

**Use transcript for detailed analysis:**
- The `_transcript.json` file contains full text with timestamps
- Review sections where technical terms were introduced
- Identify patterns in explanation quality
- Compare against the NotebookLM prompt to see what worked/didn't work

## Role Division

**User handles:**
  - Research using deep research tools (Claude, Gemini, ChatGPT, Perplexity, Grok)
- NotebookLM audio generation

**You handle:**
- File organization and directory setup
- Report synthesis from raw research
- Audio conversion (ffmpeg)
- Cover art generation (Gemini via OpenRouter) and branding
- Transcription (local Whisper)
- Chapter generation from transcript analysis
- Description, keywords, source validation for publish.md
- feed.xml updates
- Git workflow and commits
- Logging prompts used throughout

## Getting Started

When user wants to create a new episode, start with:

1. **Create a todo list** with TodoWrite tool for tracking all phases:
   - Setup episode structure and files
   - Synthesize research into report.md
   - Generate cover art
   - Obtain audio from NotebookLM
   - Process audio (transcribe, chapters)
   - Create publishing metadata
   - Update feed.xml and commit

2. Ask for episode date, slug, and title

3. **Help craft the research prompt** - work with user to refine their topic into a clear, methodology-focused research prompt

4. **Immediately create all episode files:**
   - Create episode directory
   - Create the 4 core files at top level: prompts.md, research-results.md, sources.md, report.md (empty template)
   - Only create documents/ subdirectory when needed for supporting files
   - **Update todos:** Mark setup as completed, mark research synthesis as in_progress

5. User conducts research using Claude, Gemini, ChatGPT, Perplexity, Grok, or other tools
   - User can paste interim results into research-results.md

6. Once research is complete, **automatically synthesize into report.md** (don't ask - just do it)
   - Focus on key points, storytelling opportunities, and podcast narrative flow
   - **Then immediately provide the NotebookLM prompt** - save to prompts.md AND output for user to copy
   - List files to upload to NotebookLM
   - **Update todos:** Mark research synthesis as completed, mark cover art and NotebookLM as in_progress

7. **Immediately invoke cover art subagent** while user works on NotebookLM audio
   - Launch podcast-cover-art agent with episode details
   - This happens in parallel with audio generation
   - **Update todos:** Mark cover art as completed when subagent reports back

8. When user returns with audio file, **invoke audio processing subagent**
   - **Update todos:** Mark NotebookLM as completed, mark audio processing as in_progress
   - Launch podcast-audio-processing agent with audio file details
   - Subagent handles: convert, transcribe, chapters, embed
   - Subagent reports back metadata (duration, size) for publishing
   - **Update todos:** Mark audio processing as completed, mark publishing as in_progress

9. Guide through publishing phase (description, keywords, feed.xml, git commit)
   - **Update todos:** Mark publishing as completed, mark git workflow as in_progress

10. After git commit completes
    - **Update todos:** Mark git workflow as completed

**Key:** Update TodoWrite at every phase transition to maintain visibility and prevent forgotten steps.
