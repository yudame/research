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

**IMPORTANT: Always use today's actual date (2025-12-12 or current date) for all timestamps. Never use placeholder dates like "YYYY-MM-DD" in created files.**

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

**Determine episode details:**

Use today's date (YYYY-MM-DD format) unless user specifies otherwise.

**Only ask the user if missing or unclear:**
1. **Series information** (if not provided or unclear from context)
   - Series name and episode number for series episodes
   - Or confirm it's a standalone episode
2. **Episode slug** (if not provided or easily inferred from topic)
   - e.g., "lifestyle", "vo2-max", "supplementation"
3. **Episode title** (if not provided)
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

**IMPORTANT:** Replace all `YYYY-MM-DD` placeholders with today's actual date in ISO format (e.g., 2025-12-12). Never use placeholder dates in created files.

**prompts.md:**
```markdown
# Prompts Used for Episode: [Episode Title]

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** If a `research-prompt.md` exists in this directory, it contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: [Today's date in YYYY-MM-DD format]
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

**Date:** [Today's date in YYYY-MM-DD format]
**Focus:** Peer-reviewed studies, meta-analyses, official statistics

<!-- Paste Perplexity results here -->

---

## Research from Grok (Real-Time & Regional Sources)

**Date:** [Today's date in YYYY-MM-DD format]
**Focus:** Recent developments, industry news, practitioner perspectives

<!-- Paste Grok results here -->

---

## Research from ChatGPT Deep Research (Industry & Technical)

**Date:** [Today's date in YYYY-MM-DD format]
**Focus:** Industry reports, technical documentation, case studies

<!-- Paste ChatGPT results here -->

---

## Research from Gemini Deep Research (Strategic & Policy)

**Date:** [Today's date in YYYY-MM-DD format]
**Focus:** Regulatory frameworks, policy analysis, strategic frameworks

<!-- Paste Gemini results here -->

---

## Research from Claude Deep Research (Comprehensive Synthesis)

**Date:** [Today's date in YYYY-MM-DD format]
**Focus:** Multi-dimensional analysis across academic, industry, policy, and recent sources
**Duration:** ~10-20 minutes, 500+ sources accessed

### Main Research Output

<!-- Paste main research output here (from first Copy) -->

### Top Sources

<!-- Paste top sources list here (from second Copy after "list the top sources") -->

---

## Notes

- Research conducted: [Today's date in YYYY-MM-DD format]
- Tools used: [List tools actually used]
- All outputs saved for cross-validation and verification
```

**research-briefing.md (template):**
```markdown
# Master Research Briefing: [Episode Title]

Date: [Today's date in YYYY-MM-DD format]
For: podcast-synthesis-writer agent

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
- Research compiled: [Today's date in YYYY-MM-DD format]
- Sources cross-validated across multiple tools
- Conflicting sources noted in research-briefing.md
```

**Update todos:**
```
Mark "Setup episode structure and files" as completed.
Mark "Conduct parallel deep research" as in_progress.
```

---

### 2. Sequential Deep Research Phase

**CRITICAL PRINCIPLE:** Research tools gather and organize source material. They DO NOT write the final narrative. The podcast-synthesis-writer agent creates the actual report.

**Goal:** Build research progressively - start with academic foundation, identify questions, then gather targeted perspectives.

**Sequential Workflow:**
1. **Phase 1:** Perplexity academic research (comprehensive foundation)
2. **Phase 2:** Analyze results and identify questions to investigate
3. **Phase 3:** Targeted followup research with other tools based on Phase 2 questions

**Note on seed research prompts:** If a `research-prompt.md` file exists in the episode directory, treat it as context and input material - but do NOT use it directly as the deep research prompts. You must create NEW, distinct prompts optimized for the sequential workflow below.

#### **Phase 1: Perplexity - Academic Foundation**

Create a comprehensive academic research prompt with full methodology:

```
Research [TOPIC].

**Research methodology:**
- Prioritize peer-reviewed studies, meta-analyses, systematic reviews, and authoritative sources
- Distinguish between correlation and causation in findings
- Report effect sizes and practical significance, not just statistical significance
- Note the study populations and whether findings generalize to relevant demographics
- Compare individual studies against meta-analyses and systematic reviews
- Identify preliminary research vs. well-replicated findings
- Note funding sources and potential conflicts of interest when relevant
- Include contradictory findings and areas of scientific uncertainty
- Cite specific studies, researchers, and sources throughout
- Provide full source URLs for all citations

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links.
```

**Example for "early childhood educator burnout interventions":**
```
Research early childhood educator burnout interventions and their effectiveness.

**Research methodology:**
- Prioritize peer-reviewed studies, meta-analyses, systematic reviews, and authoritative sources
- Distinguish between correlation and causation in findings
- Report effect sizes and practical significance, not just statistical significance
- Note the study populations and whether findings generalize to relevant demographics
- Compare individual studies against meta-analyses and systematic reviews
- Identify preliminary research vs. well-replicated findings
- Note funding sources and potential conflicts of interest when relevant
- Include contradictory findings and areas of scientific uncertainty
- Cite specific studies, researchers, and sources throughout
- Provide full source URLs for all citations

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links.
```

---

#### **Phase 2: Question Discovery & Gap Analysis**

**After Perplexity research completes, analyze the results to identify questions we should investigate.**

**Goal:** Think creatively about what questions we should be asking - don't assume we know the right questions or their answers.

**Create a structured analysis in prompts.md:**

```markdown
## Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?
- [List the major subtopics found in the research]
- [Note which got extensive coverage vs. brief mentions]

### What gaps exist in the academic literature?
- [What hasn't been studied?]
- [What populations or contexts are missing?]
- [What time periods lack coverage?]

### What recent developments aren't covered?
- [What's happened in the last 12 months that academic research hasn't caught up with?]
- [What emerging trends or events need investigation?]

### What contradictions or uncertainties need more sources?
- [Where did sources disagree?]
- [What areas showed high uncertainty?]
- [What requires additional perspectives to understand?]

### What industry/implementation questions arose?
- [How is this actually implemented in practice?]
- [What do case studies and real-world examples show?]
- [What are the business/economic considerations?]

### What policy/regulatory angles need investigation?
- [What regulations or policies apply?]
- [How do different jurisdictions approach this?]
- [What's the strategic/policy context?]

### What practitioner perspectives are missing?
- [What would people actually doing this work say?]
- [What regional or local perspectives matter?]
- [What's being discussed in professional communities?]
```

**Use this analysis to create targeted, specific prompts for Phase 3 tools.**

---

#### **Phase 3: Targeted Followup Research**

Based on Phase 2 question discovery, create specific prompts for each tool.

**Grok - Recent Developments & Practitioner Perspectives**

Template:
```
Research [TOPIC], focusing on these specific questions:

**Recent Developments (last 12 months):**
- [Specific question from Phase 2 about recent developments]
- [Specific question about emerging trends]

**Practitioner Perspectives:**
- [Specific question about implementation]
- [Specific question about professional community discussions]

**Regional/Local Context:**
- [Specific question about local perspectives if relevant]

Focus on: Recent news, industry discussions on X/Twitter, practitioner insights, regional sources.
Provide findings with source links, publication dates, and credibility indicators.
```

**Example based on "early childhood educator burnout" Phase 2 analysis:**
```
Research early childhood educator burnout, focusing on these specific questions:

**Recent Developments (last 12 months):**
- What new policies or programs have been implemented to address educator burnout?
- How has post-pandemic burnout evolved - are we seeing recovery or worsening?

**Practitioner Perspectives:**
- What are early childhood educators saying about burnout on professional X/Twitter communities?
- What coping strategies are practitioners actually using vs. what research recommends?

**Regional Variations:**
- Are there geographic differences in burnout rates or support programs?

Focus on: Recent news, industry discussions on X/Twitter, practitioner insights, regional sources.
Provide findings with source links, publication dates, and credibility indicators.
```

---

**ChatGPT Deep Research - Industry & Case Studies**

Template:
```
Research [TOPIC], focusing on these specific questions:

**Industry Analysis:**
- [Specific question from Phase 2 about market dynamics]
- [Specific question about business models or economics]

**Case Studies & Implementation:**
- [Specific question about real-world implementations]
- [Specific question about what worked/didn't work in practice]

**Technical Details:**
- [Specific question about technical implementation if relevant]
- [Specific question about comparative analysis]

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

**Example based on "early childhood educator burnout" Phase 2 analysis:**
```
Research early childhood educator burnout, focusing on these specific questions:

**Industry Analysis:**
- What are the economic costs of educator turnover in early childhood education?
- What business models or organizational structures correlate with lower burnout?

**Case Studies & Implementation:**
- What specific burnout intervention programs have been implemented and evaluated?
- What does the data show about effectiveness of different intervention types (workload reduction vs. wellness programs vs. compensation)?

**Comparative Analysis:**
- How do burnout rates and interventions differ between private vs. public early childhood settings?
- What can we learn from other helping professions (nursing, social work) that reduced burnout?

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

---

**Gemini Deep Research - Policy & Strategic Context** (use for business/policy topics)

Template:
```
Research [TOPIC], focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- [Specific question from Phase 2 about regulations]
- [Specific question about policy approaches]

**Comparative Policy Analysis:**
- [Specific question about how different jurisdictions handle this]
- [Specific question about policy effectiveness]

**Strategic Context:**
- [Specific question about strategic considerations]
- [Specific question about policy debates or reforms]

Focus on: Regulatory frameworks, legislation, government policy documents, strategic plans, comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

**Example based on "early childhood educator burnout" Phase 2 analysis:**
```
Research early childhood educator burnout, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- What regulations exist around educator-to-child ratios and how do they impact workload?
- What policies have governments implemented specifically to address educator burnout?

**Comparative Policy Analysis:**
- How do different countries approach educator compensation, working conditions, and support?
- What can we learn from jurisdictions that successfully reduced burnout rates?

**Strategic Context:**
- What policy debates are ongoing about early childhood workforce sustainability?
- What systemic reforms are being proposed or tested?

Focus on: Regulatory frameworks, legislation, government policy documents, strategic plans, comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

---

**Claude Research - Comprehensive Synthesis** (optional 5th tool - use if Phase 2 reveals need for additional synthesis)

Template:
```
Research [TOPIC], focusing on these specific questions:

[List 3-5 specific questions from Phase 2 that require multi-dimensional analysis across academic, industry, policy, and recent sources]

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

**Example based on "early childhood educator burnout" Phase 2 analysis:**
```
Research early childhood educator burnout, focusing on these specific questions:

- What is the relationship between educator burnout and child outcomes (development, safety, learning)?
- How do systemic factors (compensation, ratios, administrative burden) interact to create burnout?
- What does the evidence show about the long-term sustainability of the early childhood workforce?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

**Save Phase 1 Perplexity prompt to prompts.md and inform user:**

"I've created the Phase 1 Perplexity academic research prompt with comprehensive methodology.

**Sequential Research Workflow:**

**Phase 1: Academic Foundation (Start Here)**
- Run Perplexity first with the comprehensive academic prompt
- This builds the foundation from peer-reviewed research
- When complete, paste results into research-results.md

**Phase 2: Question Discovery (After Perplexity)**
- I'll analyze Perplexity's results
- Identify what questions we should be asking
- Discover gaps, contradictions, recent developments, implementation questions
- Create Phase 2 analysis in prompts.md
- Generate targeted Phase 3 prompts based on these questions

**Phase 3: Targeted Followup (Based on Phase 2)**
- Run Grok, ChatGPT, Gemini, and/or Claude with specific questions from Phase 2
- Each tool focuses on questions that match its strengths
- Much more targeted and valuable than parallel generic research

---

**I'll now attempt to automate Phase 1 Perplexity submission using the Perplexity API.**

**Using the `perplexity-deep-research` skill:**
- API-based automation with sonar-deep-research model
- Expected time: 30-120 seconds
- Automatically formatted output ready to paste into research-results.md

**Fallback:** If API automation fails, manually run at https://www.perplexity.ai/ with Pro Search enabled.

**After Phase 1 completes:** Let me know and I'll begin Phase 2 question discovery analysis."

---

### Phase 1 Automation: Perplexity Academic Research

#### **Perplexity API (sonar-deep-research)**

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

**Update todos:**
```
Mark "Conduct parallel deep research" as in_progress (Phase 1 running).
```

---

### Phase 2: Question Discovery Analysis

**When user provides Perplexity results (Phase 1 complete):**

1. **Read and analyze Perplexity research from research-results.md**
2. **Create Phase 2 analysis in prompts.md** using the question discovery framework:
   - What subtopics and themes emerged?
   - What gaps exist in the academic literature?
   - What recent developments aren't covered?
   - What contradictions or uncertainties need more sources?
   - What industry/implementation questions arose?
   - What policy/regulatory angles need investigation?
   - What practitioner perspectives are missing?

3. **Generate targeted Phase 3 prompts** for the appropriate tools based on the questions:
   - **Grok** - If we need recent developments, practitioner perspectives, regional insights
   - **ChatGPT** - If we need industry analysis, case studies, implementation details
   - **Gemini** - If we need policy analysis, regulatory frameworks, comparative analysis
   - **Claude** - If we need comprehensive multi-dimensional synthesis

4. **Save all Phase 3 prompts to prompts.md** with the specific questions from Phase 2

5. **Inform user which tools to run and attempt automation**

**Update todos:**
```
Mark "Conduct parallel deep research" as in_progress (Phase 2 analysis complete, Phase 3 ready).
```

---

### Phase 3 Automation: Targeted Followup Research

**After Phase 2 question discovery, attempt to automate Phase 3 research tools as needed:**

**Available automation skills:**
- `chatgpt-deep-research` - Automates ChatGPT with 5-10 min wait + polling
- `gemini-deep-research` - Automates Gemini with 3-5 min execution
- `claude-deep-research` - Automates Claude with 10-20 min wait + polling

**For Grok:** Manual submission (no automation skill yet)
- Go to https://x.com/i/grok
- Paste Phase 3 Grok prompt from prompts.md

**Fallback for all tools:** Manual submission with prompts from prompts.md

**Update todos:**
```
Mark "Conduct parallel deep research" as completed when all Phase 3 results are collected.
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
   - Conduct sequential deep research: Perplexity academic foundation → question discovery → targeted followup with [tools used]
   - Create master research briefing organized by topic
   - Synthesize final narrative report with podcast-synthesis-writer agent
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

## Role Division

**User handles:**
- NotebookLM audio generation
- Manual research submission if Chrome automation fails

**You handle:**
- File organization and directory setup
- Reading seed research-prompt.md if present
- **Phase 1:** Creating comprehensive Perplexity academic research prompt
- **Phase 2:** Attempting Perplexity API automation (30-120 seconds)
- **Phase 3:** Analyzing Perplexity results and conducting question discovery
- **Phase 4:** Generating targeted Phase 3 prompts based on discovered questions
- **Phase 5:** Attempting automation for ChatGPT, Gemini, Claude as needed
- **Phase 6:** Cross-validation matrix creation across all research sources
- **Phase 7:** Master research briefing compilation organized by topic
- **Phase 8:** **Invoking podcast-synthesis-writer agent** to create report.md from research materials
- **Phase 9:** Audio conversion (ffmpeg)
- **Phase 10:** Cover art generation (Gemini via OpenRouter) and branding
- **Phase 11:** Transcription (local Whisper)
- **Phase 12:** Chapter generation from transcript analysis
- **Phase 13:** Description, keywords, source validation for publish.md
- **Phase 14:** feed.xml updates
- **Phase 15:** Git workflow and commits


## Getting Started

When user wants to create a new episode with V2 workflow:

1. **Create todo list** with TodoWrite tool
2. **Determine episode details** (use today's date; only ask about series/slug/title if not provided)
3. **Check for existing research-prompt.md** (seed document) and read if present
4. **Create all episode files** including research-briefing.md
5. **Phase 1:** Creating comprehensive Perplexity academic research prompt
6. **Phase 2:** Attempting Perplexity API automation (30-120 seconds)
7. User pastes Perplexity results into research-results.md when complete
8. **Phase 3:** Analyzing Perplexity results and conducting question discovery
9. **Phase 4:** Generating targeted Phase 3 prompts based on discovered questions
10. **Phase 5:** Attempting automation for ChatGPT, Gemini, Claude as needed
11. User collects all Phase 3 research into research-results.md
12. **Phase 6:** Cross-validation matrix creation across all research sources
13. **Phase 7:** Master research briefing compilation organized by topic
14. **Phase 8:** Invoking podcast-synthesis-writer agent to create report.md from research materials
15. **Phase 9:** Audio conversion (ffmpeg)
16. **Phase 10:** Cover art generation (Gemini via OpenRouter) and branding
17. **Phase 11:** Transcription (local Whisper)
18. **Phase 12:** Chapter generation from transcript analysis
19. **Phase 13:** Description, keywords, source validation for publish.md
20. **Phase 14:** feed.xml updates
21. **Phase 15:** Git workflow and commits

**Key:** Update TodoWrite at every phase transition. The V2 sequential workflow builds research progressively: academic foundation → question discovery → targeted followup, producing higher quality, better verified, non-redundant research.
