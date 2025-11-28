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

**Create a todo list** to track progress through the workflow.

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

Create `research-results.md` with this template:
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

### 3. AI Audio Generation Phase

**Generate podcast audio using NotebookLM:**

1. Upload ALL research files to NotebookLM:
   - `report.md` (overview/summary)
   - `research-results.md` (raw research outputs)
   - Any source documents (PDFs, articles) in `documents/` if present

   **User uploads ALL files** - NotebookLM will synthesize across all sources

2. Use "Audio Overview" feature with this prompt:

```
Create an intellectually rigorous podcast that balances analytical depth with clear explanation.

Opening:
• For series episodes: Begin with "Yudame Research [series name]" and introduce the episode topic
• For standalone episodes: Begin with "Yudame Research" and introduce the episode topic
• Pronunciation: "Yudame" is pronounced "you-duh-may" (three syllables, emphasis on first)
• Set up what makes this topic interesting or valuable to explore

Core principles:
• Spell out acronyms on first use: "High-Intensity Interval Training, or HIIT"
• For short, clear terms like HIIT, prefer saying the full phrase in speech when natural
• Medical/technical acronyms (VO2, HRV, etc.) can remain as acronyms after introduction
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
• Repeatedly restating context or target listener details - establish once, then focus on content

Target audience: Intelligent listeners who want to deeply understand the topic and apply the insights. They appreciate technical depth but need terms defined to follow along.

Tone: Intellectually rigorous but accessible. Think "conversational expert explaining to a bright student" - maintain depth while ensuring clarity.

Closing:
• Summarize 2-3 key takeaways or practical implications
• Close with information about learning more: "Find full research and sources at research dot yuda dot me - that's Y-U-D-A dot M-E"

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

**Log to prompts.md:** Note the files uploaded and any customizations to the default prompt.

### 4. Audio File Processing Phase

**When user adds the generated audio file:**

1. **Check the format** - if it's .m4a, convert to .mp3:
   ```bash
   cd ~/src/research/podcast/episodes/YYYY-MM-DD-slug
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
   cd ~/src/research/podcast/tools

   # Fix SSL certificates (macOS Python)
   /Applications/Python\ 3.12/Install\ Certificates.command

   # Install dependencies
   pip install -r requirements.txt
   ```

   **Transcription workflow:**

   a. Run local Whisper transcription (no API key needed):
   ```bash
   cd ~/src/research/podcast/tools
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

   **Log to prompts.md:** Note the number of chapters created.

   d. Embed chapters into the mp3 file:
   ```bash
   cd ~/src/research/podcast/episodes/YYYY-MM-DD-slug
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

### 5. Cover Art Generation Phase

**Generate AI cover art and add branding:**

This is a two-step process: first generate the base image with DALL-E 3, then add podcast branding (logo, text, border).

**Step 1: Generate base cover art**

```bash
cd ~/src/research/podcast/tools

# Generate cover art from report.md (recommended)
python generate_cover.py ../episodes/YYYY-MM-DD-slug --auto

# OR use custom prompt
python generate_cover.py ../episodes/YYYY-MM-DD-slug --prompt "Your custom image prompt"
```

**generate_cover.py features:**
- Uses OpenAI DALL-E 3 API (requires OPENAI_API_KEY environment variable)
- Auto-generates prompts by analyzing report.md content
- Automatically enforces dark navy/blue color theme throughout the image
- Automatically blocks unwanted text, icons, logos, and annotations
- Outputs to `cover.png` in the episode directory
- Logs all prompts to `prompts.md` for reproducibility

**Step 2: Add branding to cover art**

```bash
cd ~/src/research/podcast/tools

# For series episodes (with series and episode text)
python add_logo_watermark.py ../episodes/series-name/epX-slug/cover.png \
  --position top-left \
  --brand "Yudame Research" \
  --series "Series Name" \
  --episode "Ep X - Topic" \
  --border 20 \
  --border-color "#FFC20E"

# For standalone episodes (no series text)
python add_logo_watermark.py ../episodes/YYYY-MM-DD-slug/cover.png \
  --position top-left \
  --brand "Yudame Research" \
  --episode "Episode Topic" \
  --border 20 \
  --border-color "#FFC20E"
```

**add_logo_watermark.py features:**
- Adds yellow "A" logo (from `podcast/cover.png`) to specified position
- Adds text overlays: brand name, series name (optional), episode info
- Series text uses BIGGER font (6.5% of image width) to be prominent
- Episode text uses SMALLER font (5% of image width) to handle long topic names
- Series text is optional - omit `--series` for standalone episodes
- Adds yellow border (#FFC20E) matching logo color
- Recommended border width: 20px (15-25px range)
- Logo positioned top-left with brand text beside it
- Series/episode text positioned below logo with proper margin
- Replaces original cover.png with branded version

**Cover art specifications:**
- Base size: 1024x1024px (DALL-E 3 output)
- With 20px border: 1064x1064px total
- Color scheme: Dark navy/blue dominant, teal/white/silver accents
- File size: ~500KB PNG format
- Clean abstract visualization without text from AI

**Log to prompts.md:** Note the prompt used (auto or custom) and branding settings applied.

**First-time setup (if not already done):**
```bash
cd ~/src/research/podcast/tools
pip install -r requirements.txt
export OPENAI_API_KEY='your-api-key'  # Add to ~/.zshrc or ~/.bashrc
```

**Note:**
- DALL-E 3 costs ~$0.04 per image generation
- Cover art appears in podcast apps and directories
- Each episode can have unique cover art or reuse podcast-level cover

**Regenerating existing cover art:**

If cover art needs to be updated (quality issues, theme mismatch, etc.):

1. **Regenerate with DALL-E 3 and apply branding** (same commands as initial generation):
   ```bash
   cd ~/src/research/podcast/tools
   export OPENAI_API_KEY="your-key"  # If not already in environment
   python generate_cover.py ../episodes/YYYY-MM-DD-slug --auto
   python add_logo_watermark.py ../episodes/YYYY-MM-DD-slug/cover.png \
     --position top-left \
     --brand "Yudame Research" \
     [--series "Series Name"] \
     --episode "Ep X - Topic" \
     --border 20 \
     --border-color "#FFC20E"
   ```

2. **Update the version parameter in feed.xml** for affected episodes:
   - Change `cover.png?v=1` to `cover.png?v=2`
   - Increment for each regeneration: `?v=3`, `?v=4`, etc.
   - This ensures podcast apps fetch the new images immediately

3. **Commit and push changes:**
   - Note in commit message which episodes had covers regenerated
   - Example: "feat: Regenerate cover art for episodes 1, 2, and 4"

### 6. Publishing Phase

**Generate episode description, keywords, and source links:**

a. **Create compelling 1-2 sentence description:**
   - Based on the research report and transcript
   - Highlight key topics, major stories/events covered, and main takeaways
   - Focus on what makes this episode valuable and what listeners will learn
   - Include link to full research report: `https://research.yuda.me/podcast/episodes/YYYY-MM-DD-slug/report.md`

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

**Create publish.md with all RSS feed content:**

Create `publish.md` in the episode directory with this template:
```markdown
# Episode Publishing Info

## Title
[Episode Title]

## Publication Date
[Day, DD Mon YYYY HH:MM:SS GMT - RFC 2822 format]

## Audio
- **Duration:** [MM:SS]
- **File Size:** [bytes]
- **Format:** audio/mpeg

## Description
[1-2 sentence compelling description covering key topics and takeaways.]

Full Report: https://research.yuda.me/podcast/episodes/[path]/report.md
Sources: https://research.yuda.me/podcast/episodes/[path]/sources.md

## Key Sources
- [Source Name]: [URL]
- [Source Name]: [URL]
- [Source Name]: [URL]
- [Source Name]: [URL]

## Keywords
[keyword1, keyword2, keyword3, specific-term, specific-concept]
```

**Update feed.xml using content from publish.md:**

Add a new `<item>` block to feed.xml, copying all content from publish.md:
- Title, description, keywords from publish.md
- Audio metadata (duration, file size) from publish.md
- Cover image URL with version parameter (`cover.png?v=1`)
- Use RFC 2822 date format for pubDate (e.g., "Tue, 19 Nov 2025 12:00:00 GMT")

See existing episodes in feed.xml for XML structure reference.

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
   - Generate AI cover art with DALL-E 3 and apply podcast branding
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
- Research using deep research tools (Grok, ChatGPT, Perplexity)
- NotebookLM audio generation

**You handle:**
- File organization and directory setup
- Report synthesis from raw research
- Audio conversion (ffmpeg)
- Cover art generation (DALL-E 3) and branding
- Transcription (local Whisper)
- Chapter generation from transcript analysis
- Description, keywords, source validation for publish.md
- feed.xml updates
- Git workflow and commits
- Logging prompts used throughout

## Getting Started

When user wants to create a new episode, start with:
1. Create a todo list for tracking
2. Ask for episode date, slug, and title
3. **Help craft the research prompt** - work with user to refine their topic into a clear, methodology-focused research prompt
4. **Immediately create all episode files:**
   - Create episode directory
   - Create the 4 core files at top level: prompts.md, research-results.md, sources.md, report.md (empty template)
   - Only create documents/ subdirectory when needed for supporting files
5. User conducts research using ChatGPT/Perplexity/Grok/other tools
   - User can paste interim results into research-results.md
6. Once research is complete, **automatically synthesize into report.md** (don't ask - just do it)
   - Focus on key points, storytelling opportunities, and podcast narrative flow
   - **Then immediately provide the NotebookLM prompt** - save to prompts.md AND output for user to copy
   - List files to upload to NotebookLM
7. Guide through each subsequent phase (audio generation, processing, publishing)
8. Track all prompts in prompts.md as you go
