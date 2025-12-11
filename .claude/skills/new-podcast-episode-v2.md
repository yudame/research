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
- Synthesize narrative report (status: pending)
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

**Check for existing episode directory:**

If the episode directory already exists, check for a `research-prompt.md` file. If present:
- Read it to understand the episode context and research objectives
- Use it to inform the deep research prompts you'll create
- DO NOT copy it as the deep research prompts - you'll create new ones in prompts.md

**Create the appropriate directory structure (if needed):**

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

**Note:** If a `research-prompt.md` exists in this directory, it contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

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
- **Claude Deep Research:** Comprehensive Synthesis (optional 5th tool)

### Deep Research Prompts (Copy-Paste Ready)

**IMPORTANT:** These prompts use single newlines only to prevent accidental partial submissions when pasting into Chrome-based tools.

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

## Research from Claude Deep Research (Comprehensive Synthesis)

**Date:** YYYY-MM-DD
**Focus:** Multi-dimensional analysis across academic, industry, policy, and recent sources
**Duration:** ~10-20 minutes, 500+ sources accessed

### Main Research Output

<!-- Paste main research output here (from first Copy) -->

### Top Sources

<!-- Paste top sources list here (from second Copy after "list the top sources") -->

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
- Claude Deep Research (Comprehensive Synthesis) [if used]

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

**Note on seed research prompts:** If a `research-prompt.md` file exists in the episode directory, treat it as context and input material - but do NOT use it directly as the deep research prompts. You must create NEW, distinct prompts optimized for each tool following the guidelines below.

**Help user craft differentiated research prompts for each tool:**

These prompts are intentionally concise - trust each tool to search broadly and use its natural strengths.

**IMPORTANT FORMATTING:** Remove all double newlines from prompts before saving to prompts.md. Single newlines only. This prevents accidental partial submissions when copy-pasting into Chrome-based tools.

#### **Perplexity - Academic & Official Sources**

```
Research [TOPIC].
Focus on peer-reviewed studies, meta-analyses, systematic reviews, and official government/regulatory sources.
Provide comprehensive findings with full citations, sample sizes, methodological details, and source URLs.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.
Focus on peer-reviewed studies, meta-analyses, systematic reviews, and official government/regulatory sources.
Provide comprehensive findings with full citations, sample sizes, methodological details, and source URLs.
```

---

#### **Grok - Real-Time & Regional Sources**

```
Research [TOPIC].
Focus on recent developments (last 12 months), regional Pacific news sources, local perspectives, and relevant discussions on X/Twitter from industry experts.
Provide findings with source links, publication dates, and credibility indicators.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.
Focus on recent developments (last 12 months), regional Pacific news sources, local perspectives, and relevant discussions on X/Twitter from industry experts.
Provide findings with source links, publication dates, and credibility indicators.
```

---

#### **ChatGPT Deep Research - Industry & Technical Sources**

```
Research [TOPIC].
Focus on industry analyst reports, market research, technical documentation, case studies, and financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.
Focus on industry analyst reports, market research, technical documentation, case studies, and financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

---

#### **Gemini Deep Research - Strategic & Policy Sources** (only for business/policy topics)

```
Research [TOPIC].
Focus on regulatory frameworks, legislation, government policy documents, strategic plans, and comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.
Focus on regulatory frameworks, legislation, government policy documents, strategic plans, and comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

---

#### **Claude Research - Comprehensive Synthesis** (optional 5th tool)

```
Research [TOPIC].
Conduct comprehensive research across academic, industry, policy, and recent sources to provide multi-dimensional analysis.
Prioritize authoritative sources, distinguish correlation from causation, note methodological limitations, and cite extensively.
```

**Example for "Solomon Islands Telecom Market":**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.
Conduct comprehensive research across academic, industry, policy, and recent sources to provide multi-dimensional analysis.
Prioritize authoritative sources, distinguish correlation from causation, note methodological limitations, and cite extensively.
```

**Save all prompts to prompts.md and inform user:**

"I've created 4-5 concise research prompts specifically optimized for each deep research tool's strengths.

**IMPORTANT:** These are distinct, copy-paste-ready prompts (3 lines each, single newlines only) - NOT the seed research-prompt.md if one exists. The prompts below are formatted to prevent accidental partial submissions when pasting into Chrome.

**Run these in parallel:**
- **Perplexity** → Academic studies, meta-analyses, official sources
- **Grok** → Recent news, regional sources, X/Twitter insights
- **ChatGPT Deep Research** → Industry reports, technical docs, case studies
- **Gemini Deep Research** → Regulatory frameworks, policy analysis (if applicable)
- **Claude Research** → Comprehensive synthesis (optional 5th source)

---

**I'll now attempt to automate submission using Chrome DevTools.** For each tool, I'll:
1. Navigate to the new chat page
2. Enable deep research mode (if applicable)
3. Submit the prompt

**Special handling for Claude Research:**
- Fully automated with 20-minute polling
- Automatically copies main output + sources list
- You'll paste both outputs into research-results.md when ready

**For other tools:**
- If automation fails, manually copy prompts from `prompts.md`
- When research completes, paste outputs into corresponding sections of `research-results.md`

When all research is complete and pasted into `research-results.md`, let me know and I'll begin cross-validation."

---

### Chrome Automation for Each Tool

**For each research tool, attempt automation in this order:**

#### 1. **Perplexity API (sonar-deep-research)**

**Use the `perplexity-deep-research` skill for API-based automation:**

```
Invoke the perplexity-deep-research skill with the Perplexity prompt from prompts.md.

The skill will:
1. Verify PERPLEXITY_API_KEY exists in .env file
2. Create Python script for API call
3. Submit to sonar-deep-research model with reasoning_effort=high
4. Wait 30-120 seconds for completion
5. Extract and format research report with citations
6. Output marked research ready to paste into research-results.md

Expected time: 30-120 seconds (much faster than browser-based tools)
```

**Fallback:** If API automation fails, inform user to manually:
- Go to https://www.perplexity.ai/
- Enable Pro Search
- Paste prompt from prompts.md
- Copy output to research-results.md

**Note:** API requires PERPLEXITY_API_KEY in .env. Get key at https://www.perplexity.ai/settings/api

---

#### 2. **Grok (https://x.com/i/grok)**
```
1. List Chrome pages to check if Grok is already open
2. If not open, navigate to: https://x.com/i/grok
3. Take snapshot to identify UI elements
4. Look for deep research mode toggle (if available) and enable it
5. Find the main textarea/input element
6. Fill with the Grok prompt from prompts.md
7. Submit the prompt
8. Inform user that Grok research is running
9. Open in a new tab/page if multiple tools need to run in parallel
```

**Fallback:** If automation fails, inform user to manually:
- Go to https://x.com/i/grok
- Enable any deep research features
- Paste prompt from prompts.md

---

#### 3. **ChatGPT Deep Research (https://chatgpt.com/)**

**Use the `chatgpt-deep-research` skill to automate this:**

```
Invoke the chatgpt-deep-research skill with the ChatGPT prompt from prompts.md.

The skill will:
1. Navigate to or select ChatGPT page
2. Ensure Research mode is enabled
3. Fill and submit the research prompt
4. Handle potential clarifying questions (may require manual user response)
5. Wait 5 minutes before first completion check
6. Poll every 2 minutes if needed (max 5 attempts = 10 more minutes)
7. Copy research output when complete
8. Inform user output is ready to paste into research-results.md

Expected time: 5-10 minutes (5 min wait + up to 10 min polling)
Note: May require manual intervention if ChatGPT asks clarifying questions
```

**Fallback (if skill automation fails):**
- Go to https://chatgpt.com/
- Select research-capable model (o1, o1-mini, or Research)
- Ensure Research mode is enabled
- Paste prompt from prompts.md
- Answer any clarifying questions
- Wait 5-10 minutes for completion
- Copy research output to research-results.md

---

#### 4. **Gemini Deep Research (https://gemini.google.com/)**

**Use the `gemini-deep-research` skill to automate this:**

```
Invoke the gemini-deep-research skill with the Gemini prompt from prompts.md.

The skill will:
1. Select or navigate to Gemini page
2. Switch to Fast mode (required for Deep Research)
3. Enable Deep Research from Tools menu
4. Fill and submit the prompt
5. Wait for research plan generation
6. Click "Start research" to begin
7. Confirm research is running

If automation succeeds: Inform user "Gemini Deep Research running, 3-5 minutes"
If automation fails: Provide manual fallback instructions from the skill
```

**Fallback (if skill automation fails):**
- Go to https://gemini.google.com/
- Ensure "Fast" mode (not "Thinking")
- Tools → Deep Research
- Paste prompt from prompts.md
- Review plan → Click "Start research"

---

#### 5. **Claude Research (https://claude.ai/new)** (Optional)

**Use the `claude-deep-research` skill to automate this:**

```
Invoke the claude-deep-research skill with the Claude prompt from prompts.md.

The skill will:
1. Navigate to or select Claude.ai page
2. Enable Research mode from tools menu
3. Fill and submit the research prompt
4. Wait 20 minutes before first completion check
5. Poll every 2 minutes if needed (max 5 attempts = 10 more minutes)
6. Copy main research output when complete
7. Submit followup prompt: "list the top sources"
8. Wait 1 minute for sources response
9. Copy sources list
10. Inform user both outputs are ready to paste into research-results.md

Expected time: 10-20 minutes (20 min wait + up to 10 min polling)
```

**Fallback (if skill automation fails):**
- Go to https://claude.ai/new
- Enable Research mode from tools menu
- Paste prompt from prompts.md
- Wait for research to complete (10-20 minutes, 500+ sources)
- Click Copy button for main output
- Send followup: "list the top sources"
- Click Copy button for sources
- Paste both into research-results.md

---

**After attempting automation for all tools:**
- Inform user which tools were successfully automated
- For Gemini: Use the `gemini-deep-research` skill for complete automation including the two-step confirmation process
- For Claude: Fully automated - waits 20 min, then polls every 2 min if needed, automatically copies main output + sources
- Provide manual instructions for any failed automations
- Remind user to paste completed research into research-results.md when done
- Note: Gemini takes 3-5 minutes; Claude takes 10-20 minutes (20 min wait + polling up to 10 more min)

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

### 5. Report Synthesis Phase

**Invoke the podcast-synthesis-writer agent to create report.md:**

Use the Task tool with subagent_type='podcast-synthesis-writer':

```
Transform the research materials into a narrative podcast report.

Episode directory: podcast/episodes/YYYY-MM-DD-slug/
Episode title: [Episode Title]

The podcast-synthesis-writer agent will:
1. Read research-briefing.md and research-results.md
2. Transform organized research into engaging narrative report
3. Apply evidence standards and podcast storytelling principles
4. Create report.md with proper citations and source hierarchy
5. Verify all quality requirements are met

Required files must exist:
- research-briefing.md (master briefing with verified findings)
- research-results.md (raw research outputs for additional context)
```

**The agent handles all synthesis requirements:**
- Narrative architecture and storytelling
- Evidence standards and citation format
- Podcast-optimized writing
- Accessibility without oversimplification
- Source organization and verification
- Quality checklist validation

**Update todos:**
```
Mark "Synthesize narrative report" as completed when agent finishes.
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
✅ **Chrome automation** - Automated submission to research tools (Perplexity, Grok, ChatGPT, Gemini, Claude)
✅ **Parallel research** - Multiple tools run simultaneously
✅ **Reduced redundancy** - Each tool has differentiated focus
✅ **Faster synthesis** - Organized briefing easier to work with than 3-5 raw narratives
✅ **Quality gates** - Validation step before narrative creation
✅ **Single-newline prompts** - Prevents accidental partial submissions in Chrome

### **Better Documentation:**
✅ **All prompts tracked** - Complete reproducibility
✅ **Research provenance** - Clear record of what each tool contributed
✅ **Verification record** - Cross-validation matrix preserved
✅ **Source quality notes** - Methodological limitations documented

## Role Division

**User handles:**
- NotebookLM audio generation
- Manual research submission if Chrome automation fails

**You handle:**
- File organization and directory setup
- Reading seed research-prompt.md if present
- Creating differentiated research prompts (3 lines, single newlines)
- **Attempting Chrome automation** to submit prompts to Perplexity, Grok, ChatGPT, Gemini, Claude
- **Claude automation includes:** Wait 20 min, poll every 2 min if needed, copy main output + sources automatically
- Cross-validation matrix creation
- Master research briefing compilation
- **Invoking podcast-synthesis-writer agent** to create report.md from research materials
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
3. **Check for existing research-prompt.md** (seed document) and read if present
4. **Create all episode files** including the new research-briefing.md
5. **Create differentiated deep research prompts** (3 lines each, single newlines) for parallel execution - distinct from any seed research-prompt.md
6. **Attempt Chrome automation** to submit prompts to each research tool (Perplexity, Grok, ChatGPT, Gemini, Claude)
7. **Claude automation:** Wait 20 min, poll every 2 min if needed, automatically copy main output + sources
8. User manually submits prompts if automation fails for any tools (except Claude)
9. User pastes results into research-results.md when research completes (Claude outputs already copied)
10. **Create cross-validation matrix** when research is complete
11. **Compile master research briefing** organized by topic
12. **Invoke podcast-synthesis-writer agent** to transform research into narrative report.md
13. **Launch cover art subagent** in parallel with NotebookLM
14. **Provide NotebookLM prompt** for audio generation
15. User generates audio in NotebookLM
16. **Invoke audio processing subagent** when user returns with audio
17. Guide through publishing phase
18. Git commit and push

**Key:** Update TodoWrite at every phase transition. The V2 workflow has more steps but produces higher quality, better verified research.
