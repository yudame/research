# New Podcast Episode Workflow (V2 - Deep Research)

You are helping create a new podcast episode following a structured research and production workflow with enhanced multi-source verification.

## Episode Directory Structure

Each episode follows a flat organization with core markdown files at the top level:
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── prompts.md              # All prompts used during episode creation
├── research-results.md     # Raw research outputs from multiple tools
├── research-briefing.md    # Master briefing for Opus 4.5 (organized by topic)
├── sources.md              # Organized list of source links
├── report.md               # Final research report/show notes (created by Opus 4.5)
├── publish.md              # RSS feed content (title, description, keywords, sources)
├── documents/              # Supporting files (PDFs, articles) - only if needed
├── review-notes.md         # Episode review for continuous improvement (optional)
├── cover.png               # Episode cover art with branding (~500KB)
├── YYYY-MM-DD-topic-slug.mp3          # Final audio file with chapters (~30MB)
├── YYYY-MM-DD-topic-slug_transcript.json  # Full Whisper transcript (~400KB)
├── YYYY-MM-DD-topic-slug_chapters.txt     # FFmpeg chapter format (~2KB)
└── YYYY-MM-DD-topic-slug_chapters.json    # Podcasting 2.0 format (~1KB)
```

**Key change from V1:** Added `research-briefing.md` as intermediate step between raw research and final report.

## Complete Workflow

### 1. Setup Phase

**Create a todo list** to track progress through the workflow:

```
Use TodoWrite to create initial todos:
- Setup episode structure and files (status: in_progress)
- Conduct parallel deep research (status: pending)
- Cross-validate research findings (status: pending)
- Create master research briefing (status: pending)
- Synthesize report with Opus 4.5 (status: pending)
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

**Create all episode files:**

**prompts.md:**
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

## Deep Research Phase

### Tool Configuration
- **Perplexity:** Academic & Official Sources
- **Grok:** Real-Time & Regional Sources
- **ChatGPT Deep Research:** Industry & Technical Sources
- **Gemini Deep Research:** Strategic & Policy Sources (when applicable)

---

<!-- Research prompts will be added as they are used -->
```

**research-results.md:**
```markdown
# Research Results for [Episode Title]

This file contains raw research outputs from multiple tools for cross-validation.

---

## Research from Perplexity (Academic & Official Sources)

**Date:** YYYY-MM-DD
**Focus:** Peer-reviewed studies, meta-analyses, official statistics

<!-- Paste Perplexity results here -->

---

## Research from Grok (Real-Time & Regional Sources)

**Date:** YYYY-MM-DD
**Focus:** Recent developments, industry news, practitioner perspectives

<!-- Paste Grok results here -->

---

## Research from ChatGPT Deep Research (Industry & Technical)

**Date:** YYYY-MM-DD
**Focus:** Industry reports, technical documentation, case studies

<!-- Paste ChatGPT results here -->

---

## Research from Gemini Deep Research (Strategic & Policy)

**Date:** YYYY-MM-DD
**Focus:** Regulatory frameworks, policy analysis, strategic frameworks

<!-- Paste Gemini results here -->

---

## Notes

- Research conducted: YYYY-MM-DD
- Tools used: [List tools actually used]
- All outputs saved for cross-validation and verification
```

**research-briefing.md (template):**
```markdown
# Master Research Briefing: [Episode Title]

Date: [Date]
For: Claude Opus 4.5 Final Synthesis

---

## VERIFIED KEY FINDINGS

### [Subtopic 1]
**Main finding:** [One sentence summary]

**Evidence:**
- [Stat/Finding] — Source: [Citation] — Quality: [Meta-analysis/RCT/etc] — N=[sample]
- [Stat/Finding] — Source: [Citation] — Quality: [Study type] — N=[sample]

**Contradictions/Nuances:**
- [If sources disagree, note here]

**Source quality notes:**
- [Methodological limitations to be aware of]

---

<!-- More subtopics as research reveals them -->

---

## RESEARCH GAPS & UNCERTAINTIES

- **Well-established:** [What we know with confidence]
- **Preliminary/Limited evidence:** [What has some support but needs more]
- **Unknown/Unstudied:** [What we don't know]

---

## SOURCE INVENTORY

### Tier 1 Sources (Meta-analyses, Systematic Reviews, Official Statistics)
1. [Full citation] — [Key contribution] — [URL]

### Tier 2 Sources (RCTs, Large Studies, Government Reports)
1. [Full citation] — [Key contribution] — [URL]

### Tier 3 Sources (Case Studies, Industry Reports, News)
1. [Full citation] — [Key contribution] — [URL]

---

## COMPARISON TABLES
[Tables comparing similar markets/programs/implementations]

---

## TIMELINE OF DEVELOPMENTS
[Chronological key events for topics with recent changes]

---

## PRACTITIONER PERSPECTIVES
[Direct quotes or summaries from practitioners/experts]

---

## NOTES FOR OPUS 4.5

**Strongest evidence for:**
- [Topic areas with robust sources]

**Weaker evidence for:**
- [Topic areas with limited or conflicting sources]

**Interesting tensions/contradictions:**
- [Where sources disagree - worth exploring why]

**Missing context:**
- [Gaps that should be acknowledged]
```

**sources.md:**
```markdown
# Sources for [Episode Title]

## Research Tools Used
- Perplexity (Academic & Official)
- Grok (Real-Time & Regional)
- ChatGPT Deep Research (Industry & Technical)
- Gemini Deep Research (Strategic & Policy) [if used]

## Verified Sources by Tier

### Tier 1: Meta-analyses, Systematic Reviews, Official Statistics
<!-- Add after cross-validation -->

### Tier 2: RCTs, Large Studies, Government Reports
<!-- Add after cross-validation -->

### Tier 3: Case Studies, Industry Reports, News
<!-- Add after cross-validation -->

---

## Notes
- Research compiled: YYYY-MM-DD
- Sources cross-validated across multiple tools
- Conflicting sources noted in research-briefing.md
```

**Update todos:**
```
Mark "Setup episode structure and files" as completed.
Mark "Conduct parallel deep research" as in_progress.
```

---

### 2. Parallel Deep Research Phase

**CRITICAL PRINCIPLE:** Research tools gather and organize source material. They DO NOT write the final narrative. Claude Opus 4.5 creates the actual report.

**Goal:** Comprehensive, verified, organized source material with breadth of coverage.

**Help user craft differentiated research prompts for each tool:**

These prompts are intentionally concise - trust each tool to search broadly and use its natural strengths.

#### **Perplexity - Academic & Official Sources**

```
Research [TOPIC].

Focus on peer-reviewed studies, meta-analyses, systematic reviews, and official
government/regulatory sources.

Provide comprehensive findings with full citations, sample sizes, methodological
details, and source URLs.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.

Focus on peer-reviewed studies, meta-analyses, systematic reviews, and official
government/regulatory sources.

Provide comprehensive findings with full citations, sample sizes, methodological
details, and source URLs.
```

---

#### **Grok - Real-Time & Regional Sources**

```
Research [TOPIC].

Focus on recent developments (last 12 months), regional Pacific news sources,
local perspectives, and relevant discussions on X/Twitter from industry experts.

Provide findings with source links, publication dates, and credibility indicators.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.

Focus on recent developments (last 12 months), regional Pacific news sources,
local perspectives, and relevant discussions on X/Twitter from industry experts.

Provide findings with source links, publication dates, and credibility indicators.
```

---

#### **ChatGPT Deep Research - Industry & Technical Sources**

```
Research [TOPIC].

Focus on industry analyst reports, market research, technical documentation,
case studies, and financial/business analysis.

Provide comprehensive findings with citations, data sources, and comparative analysis
where relevant.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.

Focus on industry analyst reports, market research, technical documentation,
case studies, and financial/business analysis.

Provide comprehensive findings with citations, data sources, and comparative analysis
where relevant.
```

---

#### **Gemini Deep Research - Strategic & Policy Sources** (only for business/policy topics)

```
Research [TOPIC].

Focus on regulatory frameworks, legislation, government policy documents,
strategic plans, and comparative policy analysis.

Provide findings with official source citations, effective dates, and policy context.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.

Focus on regulatory frameworks, legislation, government policy documents,
strategic plans, and comparative policy analysis.

Provide findings with official source citations, effective dates, and policy context.
```

---

#### **Claude Research - Comprehensive Synthesis** (optional 5th tool)

```
Research [TOPIC].

Conduct comprehensive research across academic, industry, policy, and recent
sources to provide multi-dimensional analysis.

Prioritize authoritative sources, distinguish correlation from causation, note
methodological limitations, and cite extensively.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.

Conduct comprehensive research across academic, industry, policy, and recent
sources to provide multi-dimensional analysis.

Prioritize authoritative sources, distinguish correlation from causation, note
methodological limitations, and cite extensively.
```

**Save all prompts to prompts.md and inform user:**

"I've created 4-5 concise research prompts optimized for each tool's strengths.

**Run these in parallel:**
- **Perplexity** → Academic studies, meta-analyses, official sources
- **Grok** → Recent news, regional sources, X/Twitter insights
- **ChatGPT Deep Research** → Industry reports, technical docs, case studies
- **Gemini Deep Research** → Regulatory frameworks, policy analysis (if applicable)
- **Claude Research** → Comprehensive synthesis (optional 5th source)

Each prompt is 3-4 lines - they trust the tool to search broadly and organize findings naturally.

**Copy the prompts from `prompts.md` and run them now.** When all research completes, paste each tool's full output into the corresponding section of `research-results.md`, then let me know and I'll begin cross-validation."

**Update todos:**
```
Mark "Conduct parallel deep research" as completed when user provides results.
Mark "Cross-validate research findings" as in_progress.
```

---

### 3. Cross-Validation Phase

**When user provides all research results, create a verification matrix:**

**Create a spreadsheet or markdown table:**

```markdown
# Cross-Validation Matrix

## Critical Facts Verification

| Claim/Statistic | Perplexity | Grok | ChatGPT | Gemini | Status | Notes |
|----------------|------------|------|---------|--------|--------|-------|
| [Fact 1] | Source A | Source A | Source A | N/A | ✅ VERIFIED | 3 sources confirm |
| [Fact 2] | Source B (53%) | Source C (55%) | Source B (53%) | N/A | ⚠️ REVIEW | Minor variance, different years |
| [Fact 3] | Source D | Not found | Not found | N/A | ⚠️ SINGLE SOURCE | Only Perplexity found this |
| [Fact 4] | Source E says X | Source F says Y | Source E says X | N/A | ⚠️ CONFLICT | Note discrepancy for Opus |

**Validation Status:**
- ✅ **VERIFIED** - 2+ independent sources confirm
- ⚠️ **NEEDS REVIEW** - Only 1 source OR conflicting data
- ❌ **REJECTED** - Unverifiable or contradicted
```

**Source Quality Assessment:**

For key sources, document:
- Primary vs secondary vs tertiary
- Sample size (for studies)
- Methodology (RCT, observational, meta-analysis, case study, opinion)
- Year published
- Funding source (conflicts of interest?)
- Peer-reviewed? Official? Industry? News? Opinion?

**Coverage Map:**

```markdown
## Topic Coverage Analysis

Topic: [Main Topic]
├─ [Subtopic 1] [P, C, G] ✅ Well covered, multiple sources
├─ [Subtopic 2] [P, C] ✅ Well covered
├─ [Subtopic 3] [G] ⚠️ Limited sources, only Grok found recent info
├─ [Subtopic 4] [P] ⚠️ Only Perplexity, single study
└─ [Subtopic 5] [P, C, Ge] ✅ Well covered with strategic analysis

**Legend:** P=Perplexity, C=ChatGPT, G=Grok, Ge=Gemini

**Action needed:** [List any gaps requiring additional research]
```

**Update todos:**
```
Mark "Cross-validate research findings" as completed.
Mark "Create master research briefing" as in_progress.
```

---

### 4. Master Research Briefing Creation

**Compile research-briefing.md organized by topic, not by tool:**

**Structure:**
1. Verified key findings (by subtopic)
2. Research gaps & uncertainties
3. Source inventory (tiered by quality)
4. Comparison tables
5. Timeline of developments (if applicable)
6. Practitioner perspectives
7. Notes for Opus 4.5

**Key principles:**
- Organize by TOPIC, not by which tool found it
- Include evidence hierarchy (what's well-established vs preliminary)
- Surface contradictions explicitly
- Note methodological limitations
- Provide direct quotes for color/authority
- Flag gaps that Opus should acknowledge

**Example structure for a subtopic:**

```markdown
### Burnout Prevalence in Early Childhood Education

**Main finding:** Burnout affects 45-72% of ECE professionals depending on setting type.

**Evidence:**
- 53.2% burnout prevalence among preschool teachers — Source: Wang et al. (2020),
  Chinese study, N=1,795 — Quality: Large observational study — Maslach Burnout Inventory
- 64% emotional burnout — Source: European 8-country study — Quality: Multi-national survey
- 72% high burnout among ABA therapists — Source: [Citation] — Quality: [Study type] —
  Highest among all settings

**Contradictions/Nuances:**
- Different studies use different burnout instruments (MBI vs CBI), making direct
  comparison difficult
- Variation by setting type suggests context matters more than profession alone

**Source quality notes:**
- Wang study is largest single-country sample but limited to China
- European study covers multiple countries but sample sizes per country not reported
- ABA therapist study is smaller N but consistent across multiple smaller studies
```

**Update sources.md with verified sources organized by tier.**

**Update todos:**
```
Mark "Create master research briefing" as completed.
Mark "Synthesize report with Opus 4.5" as in_progress.
```

---

### 5. Opus 4.5 Synthesis Phase

**USER ACTION REQUIRED:** The user must now use Claude Opus 4.5 (via claude.com or API) to create the final report.

**Provide the user with this prompt for Opus 4.5:**

```
NARRATIVE SYNTHESIS: [Episode Title]

Create a comprehensive research report for a podcast episode based on the verified
research briefing below.

[Paste the complete research-briefing.md here]

**Your role:** Transform this organized research material into an engaging, podcast-ready
narrative report.

**Requirements:**

1. **Narrative Structure:**
   - Lead with the most compelling/surprising elements
   - Create clear section headers that flow naturally
   - Build arguments from evidence, not opinions
   - Use specific examples, case studies, and real-world events
   - Highlight contrasts and comparisons that illustrate key points

2. **Evidence Standards:**
   - Every factual claim must reference a specific source from the briefing
   - When citing statistics, note sample size and study type
   - Distinguish correlation from causation explicitly
   - Note research quality (meta-analysis > RCT > observational)
   - When only one source exists, state: "According to [Source], though this wasn't
     corroborated across other sources..."
   - When sources conflict, present both views and explain possible reasons

3. **Storytelling for Podcast:**
   - Include human elements: decisions made, reasoning, outcomes
   - Make numbers meaningful through context and comparisons
   - Use concrete examples from the research (never fabricate)
   - Translate findings to practical implications
   - Note areas of uncertainty and scientific debate

4. **Accessibility:**
   - Define technical terms on first use
   - Explain mechanisms, not just outcomes
   - Use analogies when helpful (but only evidence-based ones)
   - Keep sentences clear and conversational

**Deliverable Format:**
- Markdown document with clear section headers
- Inline citations throughout
- Comparison tables where useful
- Key takeaways or implications sections
- "Sources" section at end with full citations organized by tier

**DO NOT:**
- Make claims without source citations
- Ignore contradictory findings
- Add speculative content beyond the research
- Use academic jargon without explanation
- Create examples not grounded in the research

**DO:**
- Explain what findings mean and why they matter
- Connect individual findings to broader patterns
- Acknowledge limitations and gaps
- Make the research come alive through storytelling
- Maintain scientific rigor while being engaging
```

**Add this prompt to prompts.md under "Opus 4.5 Synthesis Phase"**

**Inform user:**
"I've created the master research briefing in `research-briefing.md`. Please use Claude Opus 4.5 to synthesize this into the final report:

1. Go to claude.com or use the API with model `claude-opus-4.5-20251101`
2. Copy the Opus 4.5 prompt from `prompts.md` (just added)
3. Paste the complete `research-briefing.md` content where indicated
4. Save Opus 4.5's output as `report.md` in the episode directory
5. Return here when complete and I'll proceed with cover art and NotebookLM"

**Update todos:**
```
Mark "Synthesize report with Opus 4.5" as completed when user provides report.
Mark "Generate cover art" as in_progress.
Mark "Obtain audio from NotebookLM" as in_progress (user's parallel task).
```

---

### 6. Cover Art Generation Phase

**When user provides report.md from Opus 4.5, immediately invoke cover art subagent:**

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

**Update todos when complete:**
```
Mark "Generate cover art" as completed.
```

---

### 7. NotebookLM Audio Generation Phase

**Provide NotebookLM prompt immediately after cover art is launched:**

**Files to upload to NotebookLM:**
1. `report.md` (Opus 4.5's narrative synthesis)
2. `research-briefing.md` (organized source material)
3. `research-results.md` (raw research for additional context)
4. Any PDFs or documents in `documents/` folder

**NotebookLM Prompt (Standard Template - DO NOT customize):**

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

**Add to prompts.md under "NotebookLM Audio Generation Phase"**

**Settings:**
- Format: **Deep Dive** (or Brief/Critique/Debate as appropriate)
- Length: **Long** (or adjust based on topic complexity)

**Inform user:**
"Ready for NotebookLM audio generation:

1. Upload these files to NotebookLM:
   - report.md (Opus narrative)
   - research-briefing.md (organized sources)
   - research-results.md (raw research)
   - Any documents/ files if present

2. Use 'Audio Overview' feature with the prompt saved in prompts.md (just added)

3. Select format: Deep Dive, Length: Long

4. Generate and download the audio file

5. Return with the audio file and I'll process it (transcribe, chapters, embed)"

**Update todos when user returns:**
```
Mark "Obtain audio from NotebookLM" as completed.
Mark "Process audio (transcribe, chapters)" as in_progress.
```

---

### 8. Audio Processing Phase

**When user provides audio file, invoke audio processing subagent:**

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

**Update todos when complete:**
```
Mark "Process audio (transcribe, chapters)" as completed.
Mark "Create publishing metadata" as in_progress.
```

---

### 9. Publishing Phase

**Generate episode description, keywords, and source links:**

a. **Create compelling 1-2 sentence description (plain text):**
   - Based on report.md and transcript
   - Highlight key topics, major stories/events covered, and main takeaways
   - Focus on what makes this episode valuable and what listeners will learn
   - Keep this version plain text for the `<description>` tag
   - Include link to full research report: `https://research.yuda.me/podcast/episodes/YYYY-MM-DD-slug/report.md`

b. **Generate episode-specific keywords (5-10 keywords):**
   - Analyze report.md, transcript, and chapter titles
   - Extract the most important concepts, terms, protocols, people, events mentioned
   - Prioritize: specific technical terms, proper nouns, key concepts, frameworks
   - Format as comma-separated list for iTunes keywords field

c. **Add validated source links (3-5 sources):**
   - Use sources from research-briefing.md (Tier 1 and Tier 2 prioritized)
   - Verify links are still accessible with WebFetch when possible
   - Prioritize: official legislation/regulation, academic analysis, primary sources
   - These will be formatted as clickable HTML links in `<content:encoded>`

**Create publish.md:**

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

**Update feed.xml following RSS specification in `docs/RSS-specification.md`**

**Invoke feed validation subagent:**

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

---

### 10. Git Workflow

**Commit and push the episode:**

1. Check status and review changes:
   ```bash
   git status
   git diff feed.xml
   ```

2. Add all episode files and updated feed:
   ```bash
   git add podcast/feed.xml podcast/episodes/YYYY-MM-DD-slug/
   ```

   **Files to include:**
   - `prompts.md` - All prompts used during creation
   - `research-results.md` - Raw research outputs from all tools
   - `research-briefing.md` - Master briefing for Opus (organized by topic)
   - `sources.md` - Source links organized by tier
   - `report.md` - Final narrative report from Opus 4.5
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
   - Conduct parallel deep research across 4 tools with cross-validation
   - Create master research briefing organized by topic
   - Synthesize final narrative report with Claude Opus 4.5
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

---

## Key Improvements in V2

### **Enhanced Research Quality:**
✅ **Multi-source verification** - Facts verified across 4 different tools
✅ **Source diversity** - Academic, real-time, industry, and strategic perspectives
✅ **Cross-validation matrix** - Explicit fact-checking before synthesis
✅ **Evidence hierarchy** - Clear tiers of source quality

### **Better Organization:**
✅ **Topic-based briefing** - Organized by subject, not by which tool found it
✅ **Separation of concerns** - Research gathering vs narrative creation
✅ **Opus 4.5 synthesis** - Dedicated narrative creation phase with specialized model
✅ **Contradictions surfaced** - Conflicting sources explicitly noted

### **Improved Workflow:**
✅ **Parallel research** - Multiple tools run simultaneously
✅ **Reduced redundancy** - Each tool has differentiated focus
✅ **Faster synthesis** - Organized briefing easier to work with than 3-5 raw narratives
✅ **Quality gates** - Validation step before narrative creation

### **Better Documentation:**
✅ **All prompts tracked** - Complete reproducibility
✅ **Research provenance** - Clear record of what each tool contributed
✅ **Verification record** - Cross-validation matrix preserved
✅ **Source quality notes** - Methodological limitations documented

## Role Division

**User handles:**
- Running parallel research in 4 tools (Perplexity, Grok, ChatGPT Deep Research, Gemini Deep Research)
- Running Opus 4.5 synthesis
- NotebookLM audio generation

**You handle:**
- File organization and directory setup
- Creating differentiated research prompts
- Cross-validation matrix creation
- Master research briefing compilation
- Providing Opus 4.5 synthesis prompt
- Audio conversion (ffmpeg)
- Cover art generation (Gemini via OpenRouter) and branding
- Transcription (local Whisper)
- Chapter generation from transcript analysis
- Description, keywords, source validation for publish.md
- feed.xml updates
- Git workflow and commits
- Logging all prompts used throughout

## Getting Started

When user wants to create a new episode with V2 workflow:

1. **Create todo list** with TodoWrite tool
2. Ask for episode date, slug, and title
3. **Create all episode files** including the new research-briefing.md
4. **Provide differentiated research prompts** for parallel execution
5. User runs research in 4 tools simultaneously
6. User pastes results into research-results.md
7. **Create cross-validation matrix** when research is complete
8. **Compile master research briefing** organized by topic
9. **Provide Opus 4.5 prompt** for narrative synthesis
10. User runs Opus 4.5 and saves output as report.md
11. **Launch cover art subagent** in parallel with NotebookLM
12. **Provide NotebookLM prompt** for audio generation
13. User generates audio in NotebookLM
14. **Invoke audio processing subagent** when user returns with audio
15. Guide through publishing phase
16. Git commit and push

**Key:** Update TodoWrite at every phase transition. The V2 workflow has more steps but produces higher quality, better verified research.
