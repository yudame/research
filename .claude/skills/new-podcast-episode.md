# New Podcast Episode Workflow

You are helping create a new podcast episode following a structured research and production workflow.

## Episode Directory Structure

Each episode follows this organization:
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/
│   ├── research-results.md # Raw research outputs from ChatGPT, Perplexity, etc.
│   ├── sources.md          # Organized list of source links
│   ├── documents/          # PDFs, articles, downloads
│   └── assets/             # Images, charts, data files
├── prompts.md              # All prompts used during episode creation
├── report.md               # Final research report/show notes
├── review-notes.md         # Episode review for continuous improvement (optional)
├── script.md               # Episode script/outline (optional)
├── YYYY-MM-DD-topic-slug.mp3          # Final audio file with chapters (~30MB)
├── YYYY-MM-DD-topic-slug_transcript.json  # Full Whisper transcript (~400KB)
├── YYYY-MM-DD-topic-slug_chapters.txt     # FFmpeg chapter format (~2KB)
└── YYYY-MM-DD-topic-slug_chapters.json    # Podcasting 2.0 format (~1KB)
```

### Example: Completed Episode

```
podcast/episodes/2025-11-19-stablecoin-history/
├── research/
│   ├── research-results.md           # Raw outputs from ChatGPT/Perplexity
│   ├── sources.md                    # 14 validated source links
│   ├── documents/                    # (empty - sources were web-based)
│   └── assets/                       # (empty)
├── prompts.md                        # All prompts used during creation
├── report.md                         # 25KB - comprehensive research report
├── 2025-11-19-stablecoin-history.mp3 # 30MB - 32:41 duration, 128kbps
├── 2025-11-19-stablecoin-history_transcript.json      # 403KB - full transcript
├── 2025-11-19-stablecoin-history_chapters.txt         # 2KB - 14 chapters
└── 2025-11-19-stablecoin-history_chapters.json        # 1KB - 14 chapters

Plus original audio files (can keep for archival):
├── Stablecoins_Global_Rules_Failure_and_Genius_Act.m4a  # Original from NotebookLM
```

## Complete Workflow

### 1. Setup Phase

**Create a todo list** to track progress through the workflow.

**Ask the user:**
1. What date should we use? (YYYY-MM-DD format) - Offer today's date or custom
2. What's the episode slug? (e.g., "stablecoin-history") - Suggest options based on topic
3. What's the episode title? (e.g., "Stablecoin Market: Strategies and Pitfalls")

### 2. Research Phase (User-led with your support)

**Help user craft a deep research prompt:**

Before the user conducts research, help them create a focused research prompt for tools like Grok, ChatGPT, or other deep research tools.

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
mkdir -p /Users/tomcounsell/src/research/podcast/episodes/YYYY-MM-DD-slug/research/{documents,assets}
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

**Tool Used:** [e.g., ChatGPT, Perplexity, Grok, Claude, etc.]

**Prompt:**
```
[The research prompt will be added here]
```

**Date:** YYYY-MM-DD

---

<!-- Additional prompts will be added below as we progress through the workflow -->
```

**Create research results collection file:**

Create `research/research-results.md` with this template:
```markdown
# Research Results for [Episode Title]

This file is for pasting research results from external tools (ChatGPT, Perplexity, Grok, etc.).

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

Create `research/sources.md` with this template:
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
1. Paste research results into `research/research-results.md` as you gather them from ChatGPT, Perplexity, etc.
2. When research is complete, provide the final report for `report.md`"

---

**When user provides research:**
- Save the final research report to `report.md`
- Update `research/sources.md` with any additional sources identified
- Ask user if they have specific source URLs to add to sources.md

### 3. AI Audio Generation Phase

**Generate podcast audio using NotebookLM:**

1. Upload ALL research files to NotebookLM:
   - `report.md` (overview/summary)
   - `research/perplexity-research.md` (if present)
   - `research/chatgpt-research.md` (if present)
   - Any other research files in the `research/` directory
   - Any source documents (PDFs, articles) in `research/documents/`

   **User uploads ALL files** - NotebookLM will synthesize across all sources

2. Use "Audio Overview" feature with this prompt:

```
Create an intellectually rigorous podcast that balances analytical depth with clear explanation.

Core principles:
• ALWAYS spell out acronyms before using them - "High-Quality Liquid Assets, or HQLA" not just "HQLA"
• Define technical terms immediately with plain language THEN build on them - assume intelligent but not expert audience
• Use concrete examples and stories ONLY when they exist in the source material - never fabricate or speculate
• When stories exist, include human elements: what people said, felt, decided - not just mechanics
• HIGHLIGHT surprising findings, spectacular failures, and unexpected successes - these are the memorable moments
• Extract frameworks and principles from the research findings
• Connect findings to practical implications and broader patterns
• Maintain scientific rigor: distinguish correlation from causation, note effect sizes, acknowledge uncertainties

What to emphasize:
• Spell-first approach: "The EU's Markets in Crypto-Assets regulation, called MiCA..." not "MiCA requires..."
• Definition-first explanations: "VO2 max - the maximum rate your body can use oxygen during exercise - is..."
• Evidence-based analysis: cite specific studies, note sample sizes, report actual effect sizes
• Human elements in stories: decisions made, emotions felt, specific quotes when available
• Practical insights: what does this mean for someone implementing these findings?
• Pattern recognition: what principles emerge across multiple studies or examples?
• Conversational check-ins: "Let me define that term..." or "To be clear, what we mean by [X] is..."

SURPRISING MOMENTS - actively look for and highlight these:
• Counter-intuitive findings: "You'd think X, but the research shows the opposite..."
• Spectacular failures: "$60 billion evaporated in 48 hours" or "The supply went from millions to trillions in days"
• Dramatic effect sizes: Not just "improved" but "300% improvement" or "cut risk in half"
• Unexpected successes: "This obscure intervention outperformed the standard approach"
• Reversals: "What everyone thought was safe turned out to be the riskiest"
• Extreme comparisons: "That's equivalent to..." (make big numbers relatable)
• Non-obvious connections: "Surprisingly, factor X affects Y through this unexpected mechanism"
• Edge cases that reveal principles: "In this one situation, the entire system breaks because..."

Signal these moments with phrases like:
• "Here's where it gets really interesting..."
• "And this is the shocking part..."
• "You wouldn't expect this, but..."
• "The numbers here are staggering..."
• "This completely flips conventional wisdom..."

What to avoid:
• Acronyms without spelling them out first (DLT, SOX, OFAC, etc.)
• Technical jargon without immediate plain-language definition
• Academic language when simpler words work ("endogenous" vs "internal", "exogenous" vs "external")
• Concept stacking - introducing 3+ new technical terms in one sentence
• Fabricated examples or hypothetical stories not in the research
• Over-simplification that loses scientific accuracy
• Excessive hedging that obscures clear findings
• Dry mechanical explanations when human stories exist in the research

Target audience: Intelligent listeners who want to deeply understand the topic and apply the insights. They appreciate technical depth but need terms defined to follow along.

Tone: Intellectually rigorous but accessible. Think "conversational expert explaining to a bright student" - maintain depth while ensuring clarity.

When presenting stories:
• Include human drama if it exists: "Do Kwon tweeted X, causing panic..." not just "The protocol experienced stress"
• Build narrative tension: "On that Friday afternoon, Circle announced..." not just "Circle had exposure"
• Make it memorable through specifics: "$3.3 billion frozen over a weekend" not "some funds were inaccessible"
• Emphasize the spectacular: "The supply didn't just increase - it went from hundreds of millions to TRILLIONS in 48 hours"
• Use reveals for surprises: Set up expectation, then flip it - "Everyone assumed X was safe. Then this happened..."

When presenting research:
• Focus on what the numbers mean and why they matter
• Use comparisons: "That's like losing 5 years of profits from one fine"
• Translate statistics to implications: "A 20% effect size means..."

Balance precision with engagement - neither dumbed down nor unnecessarily complex.
```

3. Select format: **Deep Dive** (or Brief/Critique/Debate as appropriate)
4. Select length: **Long** (or adjust based on topic complexity)
5. Generate and download the audio file

**Save the NotebookLM prompt to prompts.md:**

Append to `prompts.md`:
```markdown
## Audio Generation Phase

### NotebookLM Audio Overview Prompt

**Tool Used:** NotebookLM

**Format:** Deep Dive / Long

**Files Uploaded to NotebookLM:**
- report.md
- research/perplexity-research.md
- research/chatgpt-research.md
- [List any other research files or documents uploaded]

**Prompt:**
```
[Copy the exact prompt used for NotebookLM Audio Overview]
```

**Customizations:** [Note any customizations to the default prompt]

**Date:** YYYY-MM-DD
```

### 4. Audio File Processing Phase

**When user adds the generated audio file:**

1. **Check the format** - if it's .m4a, convert to .mp3:
   ```bash
   cd /Users/tomcounsell/src/research/podcast/episodes/YYYY-MM-DD-slug
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
   cd /Users/tomcounsell/src/research/podcast/tools

   # Fix SSL certificates (macOS Python)
   /Applications/Python\ 3.12/Install\ Certificates.command

   # Install dependencies
   pip install -r requirements.txt
   ```

   **Transcription workflow:**

   a. Run local Whisper transcription (no API key needed):
   ```bash
   cd /Users/tomcounsell/src/research/podcast/tools
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

   **Save the chapter analysis prompt to prompts.md:**

   Append to `prompts.md`:
   ```markdown
   ## Chapter Generation Phase

   ### Chapter Analysis Prompt

   **Tool Used:** Claude / AI Assistant

   **Prompt:**
   ```
   [Copy the exact prompt used to analyze the transcript and generate chapters]
   ```

   **Output:** [Number] chapters created covering [brief description of coverage]

   **Date:** YYYY-MM-DD
   ```

   d. Embed chapters into the mp3 file:
   ```bash
   cd /Users/tomcounsell/src/research/podcast/episodes/YYYY-MM-DD-slug
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

**Generate episode description, keywords, and source links:**

a. **Create compelling 1-2 sentence description:**
   - Based on the research report and transcript
   - Highlight key topics, major stories/events covered, and main takeaways
   - Focus on what makes this episode valuable and what listeners will learn
   - Include link to full research report: `https://yudame.github.io/research/podcast/episodes/YYYY-MM-DD-slug/report.md`

b. **Generate episode-specific keywords (5-10 keywords):**
   - Analyze the research report, transcript, and chapter titles
   - Extract the most important concepts, terms, protocols, people, events mentioned
   - Prioritize: specific technical terms, proper nouns, key concepts, frameworks
   - Examples: "VO2 max", "HRV", "stablecoins", "Terra Luna", "GENIUS Act", "sleep quality"
   - Format as comma-separated list for iTunes keywords field

c. **Add validated source links:**
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
   - Peer-reviewed studies (PubMed, academic journals)

**Save the episode description generation process to prompts.md:**

Append to `prompts.md`:
```markdown
## Publishing Phase

### Episode Description Generation

**Tool Used:** Claude / AI Assistant

**Prompt:**
```
[Copy the exact prompt used to generate the episode description]
```

**Final Description:**
```
[Copy the final episode description that will be used in feed.xml]
```

**Keywords:** [List of episode-specific keywords]

**Date:** YYYY-MM-DD

### Source Link Validation

**Sources Validated:**
1. [Source name] - [URL] - [Validation method: WebSearch, WebFetch, manual]
2. [Source name] - [URL] - [Validation method]
3. [Source name] - [URL] - [Validation method]
[etc.]

**Date:** YYYY-MM-DD
```

**Update feed.xml:**

Add a new `<item>` block after the opening `<channel>` metadata and before the closing `</channel>` tag:

```xml
<!-- Episode N: Short Description -->
<item>
  <title>Episode Title Here</title>
  <description>Compelling 1-2 sentence description (full report: https://yudame.github.io/research/podcast/episodes/YYYY-MM-DD-slug/report.md) covering key topics and takeaways.

Key Sources:
• Official Source 1: [validated URL]
• Official Source 2: [validated URL]
• Official Source 3: [validated URL]
• Analysis/Research: [validated URL]</description>
  <pubDate>Day, DD Mon YYYY 12:00:00 GMT</pubDate>
  <enclosure url="https://yudame.github.io/research/podcast/episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3"
             length="FILE_SIZE_IN_BYTES"
             type="audio/mpeg"/>
  <guid>https://yudame.github.io/research/podcast/episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3</guid>
  <itunes:duration>MM:SS</itunes:duration>
  <itunes:explicit>no</itunes:explicit>
  <itunes:keywords>keyword1, keyword2, keyword3, specific-protocol, specific-concept</itunes:keywords>
</item>
```

**Date format for pubDate:** Use RFC 2822 format (e.g., "Tue, 19 Nov 2025 12:00:00 GMT")

**Note:**
- Podcast-level categories are Technology and Education
- Episode keywords are automatically generated from content analysis
- Description and keywords are created without user input - just review and update feed.xml

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
   - `prompts.md` - All prompts used during creation
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
1. Ensure GitHub Pages is enabled at: `https://github.com/yudame/research/settings/pages`
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)

2. Feed URL will be: `https://yudame.github.io/research/podcast/feed.xml`

3. Wait 2-3 minutes for GitHub Pages to deploy

### 8. Episode Review (Optional - for continuous improvement)

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

## Important Notes

- **Always use TodoWrite** to track progress through these phases
- **Mark tasks complete** immediately after finishing each step
- **Create files immediately** after research prompt - create all episode directories and template files right away
- **research-results.md** - Provide this file for user to paste raw research outputs from ChatGPT/Perplexity as they work
- **Track all prompts** in `prompts.md` throughout the workflow for reproducibility
- **Save prompts immediately** after using them - don't batch at the end
- **Use ffmpeg** for audio conversion (128kbps mp3 is recommended)
- **File sizes** - aim to keep episodes under 100MB
- **Transcription** - Always generate transcript and chapters for every episode
- **Chapters** - Aim for 10-15 chapters, each 2-4 minutes, with descriptive titles
- **Episode descriptions and keywords** - Auto-generate both from research report, transcript, and chapters - no user input needed
- **Source validation** - Use WebSearch and WebFetch to find and validate 3-5 official source links
- **Commit messages** - use heredoc format for multi-line messages
- **User handles** - research (deep research tools, NotebookLM) and audio creation
- **You handle** - file organization, format conversion, transcription, chapter generation, description/keyword generation, source validation, feed.xml updates, git workflow, prompt tracking

## Getting Started

When user wants to create a new episode, start with:
1. Create a todo list for tracking
2. Ask for episode date, slug, and title
3. **Help craft the research prompt** - work with user to refine their topic into a clear, methodology-focused research prompt
4. **Immediately create all episode files and directories:**
   - Create directory structure (research/documents/, research/assets/)
   - Create prompts.md with episode details and research prompt
   - Create research/research-results.md for pasting ChatGPT/Perplexity outputs
   - Create research/sources.md template
5. User conducts research using ChatGPT/Perplexity/Grok/other tools
   - User can paste interim results into research/research-results.md
6. Once research is complete, save final report to report.md
7. Guide through each subsequent phase (audio generation, processing, publishing)
8. Track all prompts in prompts.md as you go
