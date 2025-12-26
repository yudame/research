# New Podcast Episode Workflow

## Quick Reference: Episode Workflow Progress

**Track your progress through each phase. The workflow is complete when all phases are checked off.**

- [ ] **Phase 1: Setup** → Episode directory and initial files created
- [ ] **Phase 2: Research - Academic Foundation** → Perplexity research complete (30-120s)
- [ ] **Phase 3: Research - Question Discovery** → Phase 2 analysis complete, targeted prompts ready
- [ ] **Phase 4: Research - Targeted Followup** → Grok, GPT-Researcher, Gemini, Claude research complete
- [ ] **Phase 5: Cross-Validation** → Sources verified, contradictions identified
- [ ] **Phase 6: Master Briefing** → research/p3-briefing.md created with organized findings
- [ ] **Phase 7: Synthesis** → report.md created by podcast-synthesis-writer
- [ ] **Phase 8: Episode Planning** → content_plan.md created by podcast-episode-planner
- [ ] **Phase 9: Cover Art** → cover.png generated and branded
- [ ] **Phase 10: Audio Generation** → NotebookLM Enterprise API
- [ ] **Phase 11: Audio Processing** → Transcription and chapters
- [ ] **Phase 12: Publishing** → feed.xml updated with episode metadata
- [ ] **Phase 13: Commit & Push** → Changes committed and pushed to GitHub

**Verification:** After Phase 13, check https://research.yuda.me/podcast/feed.xml refreshes with new episode in 2-3 minutes.

---

You are helping create a new podcast episode following a structured research and production workflow with sequential deep research and multi-source verification.

## Episode Directory Structure

Each episode follows an organized structure with files grouped by purpose:

```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/                           # Research files organized by phase
│   ├── p1-brief.md                    # Research brief (topic/questions)
│   ├── p2-perplexity.md               # Perplexity academic research
│   ├── p2-grok.md                     # Grok real-time/regional research
│   ├── p2-chatgpt.md                  # GPT-Researcher industry/technical
│   ├── p2-gemini.md                   # Gemini policy/strategic research
│   ├── p2-manual.md                   # Manual research, user sources
│   ├── p3-briefing.md                 # Cross-validated synthesis for synthesis agent
│   └── documents/                     # PDFs, papers, supporting files
├── logs/                               # Process logs
│   ├── prompts.md                     # All prompts used during creation
│   └── metadata.md                    # Publishing metadata scratch
├── tmp/                                # Temporary files (optional to commit)
│   └── *_transcript.json              # Full Whisper output (large file)
├── cover.png                           # Episode cover art with branding (~500KB)
├── report.md                           # Final narrative report from synthesis agent
├── content_plan.md                     # Episode structure guide for NotebookLM
├── sources.md                          # Source documentation
├── YYYY-MM-DD-topic-slug.mp3          # Final audio file with chapters (~30MB)
├── YYYY-MM-DD-topic-slug_chapters.json # Podcasting 2.0 chapter metadata
└── transcript.txt                      # Plain text transcript from Whisper
```

**Key organizational principles:**
- **Research files use phase prefixes** (p1, p2, p3) for chronological sorting
- **Each research tool saves to its own file** (prevents race conditions, enables parallel execution)
- **Root directory contains only final outputs** (published files linked in feed.xml)
- **Logs separated from research** (prompts.md moved to logs/)
- **Temporary files isolated** (tmp/ for large transcripts, can be optionally committed)

**File naming rationale:**
- **p1-brief.md** - "Brief" describes research topic/question (not "prompt" which is tool-specific)
- **p2-[tool].md** - Individual tool outputs enable parallel execution without conflicts
- **p3-briefing.md** - Cross-validated synthesis ready for narrative creation
- **No redundant prefixes** - Files in research/ don't need "research-" prefix

## Complete Workflow

═══════════════════════════════════════════════════════════════
                    PHASE 1: SETUP
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ User has provided episode topic or research question
✓ Episode details known or easily inferred (date, slug, title, series info if applicable)

**IMPORTANT: Always use today's actual date (2025-12-15 or current date) for all timestamps. Never use placeholder dates like "YYYY-MM-DD" in created files.**

**Create a todo list** to track progress through the workflow:

```
Use TodoWrite to create initial todos:
- Setup episode structure and files (status: in_progress)
- Conduct deep research (Perplexity, then targeted followup) (status: pending)
- Cross-validate research findings (status: pending)
- Create master research briefing (status: pending)
- Synthesize narrative report (status: pending)
- Create episode content plan (status: pending)
- Generate cover art (status: pending)
- Generate audio via NotebookLM API (status: pending)
- Process audio (transcribe, chapters, embed) (status: pending)
- Update feed.xml and publish (status: pending)
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
- DO NOT copy it as the deep research prompts - you'll create new ones in logs/prompts.md

**Create the episode directory and files using setup_episode.py:**

```bash
cd ~/src/research/podcast/tools

# For standalone episodes (uses today's date automatically)
uv run python setup_episode.py --slug "topic-slug" --title "Episode Title"

# For series episodes
uv run python setup_episode.py --slug "topic-slug" --title "Series: Ep. X, Topic" \
  --series "series-name" --episode-num X

# With research context pre-filled
uv run python setup_episode.py --slug "topic-slug" --title "Episode Title" \
  --context "Research focus and key questions"
```

**What setup_episode.py creates:**
```
podcast/episodes/{path}/
├── research/
│   ├── documents/
│   └── p1-brief.md      # Research brief with date/title
├── logs/
│   └── prompts.md       # Prompt tracking with date/title
├── tmp/
└── sources.md           # Source template
```

The script automatically uses today's date and fills in all templates.

**logs/prompts.md (created by script):**
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

**Automated tools:**
- **Perplexity:** Academic & Official Sources (Phase 1 - always used, API-based)
- **GPT-Researcher:** Industry & Technical Sources (Phase 3 - API-based, uses OpenAI GPT-5.2)
- **Gemini Deep Research:** Strategic & Policy Sources (Phase 3 - API-based)

**Manual tools (user runs these):**
- **Claude:** Comprehensive Synthesis (Phase 3 - user pastes from https://claude.ai)
- **Grok:** Real-Time & Regional Sources (Phase 3 - user pastes from https://x.com/i/grok)

**🚨 DEFAULT APPROACH: USE ALL 5 TOOLS FOR EVERY EPISODE**

All episodes should use all 5 research sources by default:
1. ✅ **Perplexity** - Academic foundation (always runs first)
2. ✅ **GPT-Researcher** - Industry/technical analysis
3. ✅ **Gemini** - Policy/regulatory frameworks
4. ✅ **Claude** - Comprehensive cross-dimensional synthesis
5. ✅ **Grok** - Real-time developments and practitioner perspectives

**Omitting a tool should be rare** and only for a specific reason (e.g., "This topic has zero policy/regulatory angle, skipping Gemini"). When in doubt, use all 5 tools.

### Deep Research Prompts (Copy-Paste Ready)

**IMPORTANT:** These prompts use single newlines only to prevent accidental partial submissions when pasting into Chrome-based tools.

---

<!-- Research prompts will be added as they are used -->
```

**research/p1-brief.md:**
```markdown
# Research Brief: [Episode Title]

**Date:** [Today's date in YYYY-MM-DD format]
**Episode:** [Episode Title]

---

## Research Topic

[High-level description of what this episode will research]

## Key Questions

- [Question 1]
- [Question 2]
- [Question 3]

## Context

[Any relevant context or background for the research]

---

**Next Steps:**
1. Create Phase 1 academic research prompt for Perplexity
2. Run Perplexity research → save to research/p2-perplexity.md
3. Analyze results for question discovery
4. Create targeted Phase 3 prompts for other tools
```

**research/p2-perplexity.md (template - created after Phase 1 research):**
```markdown
# Perplexity Research: [Episode Title]

**Date:** [Today's date in YYYY-MM-DD format]
**Focus:** Academic & Official Sources
**Duration:** 30-120 seconds

---

## Research Output

[Paste Perplexity results here]

---

## Sources

[List key sources cited in the research]
```

**research/p2-grok.md, p2-chatgpt.md, p2-gemini.md (created as needed for Phase 3 tools)**

Each follows the same pattern:
```markdown
# [Tool Name] Research: [Episode Title]

**Date:** [Today's date in YYYY-MM-DD format]
**Focus:** [Tool's focus area]

---

## Research Output

[Paste results here]

---

## Sources

[List key sources]
```

**research/p3-briefing.md (template - created after cross-validation):**
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
- Perplexity (Academic & Official - automated)
- Grok (Real-Time & Regional - manual)
- GPT-Researcher (Industry & Technical - OpenAI GPT-5.2 - automated)
- Gemini Deep Research (Strategic & Policy - automated) [if used]

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
- Conflicting sources noted in research/p3-briefing.md
```

**VERIFY SETUP COMPLETE - File State Check:**

```bash
# Verify directory structure created
ls -la podcast/episodes/YYYY-MM-DD-slug/

# Expected: research/, logs/, tmp/ subdirectories present
```

**Expected directory structure:**
```
podcast/episodes/YYYY-MM-DD-slug/
├── research/
│   └── documents/
├── logs/
│   ├── prompts.md (exists, ~500 bytes)
│   └── [p1-brief.md will be created if user provides research prompt]
├── tmp/
└── sources.md (exists, ~300 bytes)
```

**File State - AFTER Phase 1:**
- ✅ Directory structure created (research/, logs/, tmp/)
- ✅ logs/prompts.md exists with episode details
- ✅ sources.md template created
- ✅ research/p1-brief.md created if user provided research context

---

**EXIT CRITERIA (all must be true to proceed):**
✓ Episode directory created with correct naming
✓ Subdirectories created: research/, research/documents/, logs/, tmp/
✓ logs/prompts.md exists with episode details logged
✓ sources.md template exists
✓ Today's actual date used (not placeholder YYYY-MM-DD)
✓ All file templates use correct paths (research/, logs/)

**Update todos:**
```
Mark "Setup episode structure and files" as completed.
Mark "Conduct parallel deep research" as in_progress.
```

═══════════════════════════════════════════════════════════════

---

═══════════════════════════════════════════════════════════════
                    PHASES 2-6: RESEARCH & BRIEFING
═══════════════════════════════════════════════════════════════

This section covers:
- **Phase 2:** Academic Foundation (Perplexity)
- **Phase 3:** Question Discovery
- **Phase 4:** Targeted Followup Research
- **Phase 5:** Cross-Validation
- **Phase 6:** Master Briefing Creation

---

### Sequential Deep Research Phase

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

**Important:** Default to using all four Phase 3 tools (Grok, ChatGPT, Gemini, Claude). Each tool provides a unique perspective that strengthens the research. Only omit a tool if its focus area is genuinely not applicable to the topic - this should be rare.

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

**GPT-Researcher - Industry & Case Studies**

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

**Gemini Deep Research - Policy & Strategic Context**

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

**Claude Research - Comprehensive Synthesis**

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

**Display the Phase 1 Perplexity prompt to user, then save to logs/prompts.md:**

"I've created the Phase 1 Perplexity academic research prompt with comprehensive methodology.

**📋 PERPLEXITY PROMPT (Phase 1 - Academic Foundation):**

```
[DISPLAY THE FULL PROMPT HERE - user needs to see exactly what will be researched]
```

This prompt will now be saved to logs/prompts.md and used for Phase 1 research.

---

**Sequential Research Workflow:**

**Phase 1: Academic Foundation (Start Here)**
- Run Perplexity first with the comprehensive academic prompt
- This builds the foundation from peer-reviewed research
- When complete, paste results into research/p2-perplexity.md

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
- Automatically formatted output ready to paste into research/p2-perplexity.md

**Fallback:** If API automation fails, manually run at https://www.perplexity.ai/ with Pro Search enabled.

**After Phase 1 completes:** Let me know and I'll begin Phase 2 question discovery analysis."

---

### Phase 1 Automation: Perplexity Academic Research

#### **Perplexity API (sonar-deep-research)**

**Invoke the perplexity-deep-research skill via Task tool:**

```
Use the Task tool with subagent_type='general-purpose':

"Automate Perplexity Deep Research API for Phase 1 academic research.

Read and follow the instructions in .claude/skills/perplexity-deep-research/SKILL.md:
1. Check for PERPLEXITY_API_KEY in .env file
2. Create Python script for API call
3. Submit to sonar-deep-research model with reasoning_effort=high
4. Wait 30-120 seconds for completion
5. Extract and format research report with citations
6. Output marked research ready to save to research/p2-perplexity.md

Research prompt: [insert Perplexity prompt from prompts.md]"
```

**Expected time:** 30-120 seconds (much faster than browser-based tools)

**Fallback if skill unavailable or API fails:**
- Go to https://www.perplexity.ai/
- Enable Pro Search
- Paste prompt from prompts.md
- Copy output to research/p2-perplexity.md

**Note:** API requires PERPLEXITY_API_KEY in .env. Get key at https://www.perplexity.ai/settings/api

**Update todos:**
```
Mark "Conduct parallel deep research" as in_progress (Phase 1 running).
```

---

### Phase 2: Question Discovery Analysis

**When user provides Perplexity results (Phase 1 complete):**

1. **Read and analyze Perplexity research from research/p2-perplexity.md**
2. **Create Phase 2 analysis in prompts.md** using the question discovery framework:
   - What subtopics and themes emerged?
   - What gaps exist in the academic literature?
   - What recent developments aren't covered?
   - What contradictions or uncertainties need more sources?
   - What industry/implementation questions arose?
   - What policy/regulatory angles need investigation?
   - What practitioner perspectives are missing?

3. **Generate targeted Phase 3 prompts for ALL 5 TOOLS** based on the questions discovered:
   - **GPT-Researcher** - Industry analysis, case studies, implementation details, technical documentation, market dynamics (automated)
   - **Gemini** - Policy analysis, regulatory frameworks, comparative policy analysis, strategic context, official documents (automated)
   - **Claude** - Comprehensive synthesis across academic, industry, policy, and recent sources (manual)
   - **Grok** - Recent developments (last 12 months), practitioner perspectives, regional insights, real-time discussions (manual)

   **🚨 DEFAULT: CREATE PROMPTS FOR ALL 4 PHASE 3 TOOLS**

   Omitting a tool should be rare and only for a specific reason. Examples of valid reasons to skip:
   - Skip Gemini if topic truly has zero policy/regulatory/strategic angles
   - Skip GPT-Researcher if topic has no industry/technical implementation aspects
   - Skip Claude if other tools provide sufficient cross-dimensional coverage
   - Skip Grok if topic has no recent developments or practitioner perspectives

   **In practice:** Most topics benefit from all perspectives. Use all 4 tools unless you have a specific reason not to.

4. **Display all Phase 3 prompts to the user, then save to logs/prompts.md**

   **IMPORTANT:** Show the user each prompt in the conversation so they can review what will be researched. Format like this:

   ```
   📋 PHASE 3 RESEARCH PROMPTS (All 4 tools)

   **GPT-RESEARCHER PROMPT (Automated - 6-20 min):**
   ```
   [Full GPT-Researcher prompt here]
   ```

   **GEMINI PROMPT (Automated - 3-10 min):**
   ```
   [Full Gemini prompt here]
   ```

   **CLAUDE PROMPT (Manual - User will paste from claude.ai):**
   ```
   [Full Claude prompt here]
   ```

   **GROK PROMPT (Manual - User will paste from x.com/i/grok):**
   ```
   [Full Grok prompt here]
   ```

   These prompts will now be saved to logs/prompts.md and used for Phase 3 research.
   ```

   After displaying the prompts, save them to logs/prompts.md with the Phase 2 analysis

5. **Create empty research files for Phase 3 results:**

```bash
# Create placeholder files for research results
cd podcast/episodes/YYYY-MM-DD-slug/research

# GPT-Researcher (automated - will be populated by script)
touch p2-chatgpt.md

# Gemini (automated - will be populated by script)
touch p2-gemini.md

# Claude (manual - user will paste here)
cat > p2-claude.md << 'EOF'
# Claude Research: [Episode Title]

**Date:** [Today's date]
**Focus:** Comprehensive Synthesis

---

## Research Output

[Paste Claude results here from https://claude.ai]

---

## Sources

[Key sources will be extracted after pasting]
EOF

# Grok (manual - user will paste here)
cat > p2-grok.md << 'EOF'
# Grok Research: [Episode Title]

**Date:** [Today's date]
**Focus:** Real-Time & Regional Sources

---

## Research Output

[Paste Grok results here from https://x.com/i/grok]

---

## Sources

[Key sources will be extracted after pasting]
EOF
```

6. **Inform user which tools to run and attempt automation**

**Update todos:**
```
Mark "Conduct parallel deep research" as in_progress (Phase 2 analysis complete, Phase 3 ready).
```

---

### Phase 3 Automation: Targeted Followup Research

**After Phase 2 question discovery, invoke research skills as needed:**

**Available automation skills (invoke via Task tool):**
- `gpt-researcher` - Local multi-agent research with OpenAI GPT-5.2, 6-20 min, 100+ sources, no browser required
- `gemini-deep-research` - Official API automation, 3-10 min polling, no browser required
- `perplexity-deep-research` - Official API automation, 30-120s, academic focus

**How to invoke:**
```
Use the Task tool with subagent_type='general-purpose':

"Automate [ChatGPT/Gemini] Deep Research for Phase 3 research.

Read and follow the instructions in .claude/skills/[skill-name]/SKILL.md to:
1. Execute automation (API or local tool)
2. Wait for research completion
3. Extract and format results
4. Save to research/p2-[tool].md

Research prompt: [insert Phase 3 prompt from prompts.md]"
```

This offloads the automation work to a subagent, keeping the main context clean.

**For Grok:** Manual submission (no automation available yet)
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

**Immediately after all Phase 3 research is collected, proceed automatically to cross-validation.**

**⚠️ DO NOT STOP AND WAIT FOR USER - CONTINUE AUTOMATICALLY**

**Create a verification matrix:**

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

**After completing cross-validation, immediately proceed to create research/p3-briefing.md.**

**⚠️ DO NOT STOP AND WAIT FOR USER - CONTINUE AUTOMATICALLY**

**Compile research/p3-briefing.md organized by topic, not by tool:**

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
Mark "Synthesize narrative report" as in_progress.
```

---

═══════════════════════════════════════════════════════════════
                    PHASE 7: SYNTHESIS
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ research/p3-briefing.md created with organized findings (Phase 6)
✓ All research/p2-*.md files present
✓ Sources cross-validated and verified
✓ Ready for narrative creation

**⚠️ DO NOT STOP AND WAIT FOR USER - INVOKE AGENT AUTOMATICALLY**

**WORK TO DO:** Invoke the podcast-synthesis-writer agent to create report.md:

Use the Task tool with subagent_type='podcast-synthesis-writer':

```
Transform the research materials into a narrative podcast report.

Episode directory: podcast/episodes/YYYY-MM-DD-slug/
Episode title: [Episode Title]

The podcast-synthesis-writer agent will:
1. Read research/p3-briefing.md and individual research/p2-*.md files
2. Transform organized research into engaging narrative report
3. Apply evidence standards and podcast storytelling principles
4. Create report.md with proper citations and source hierarchy
5. Verify all quality requirements are met

Required files must exist:
- research/p3-briefing.md (master briefing with verified findings)
- research/p2-*.md files (individual tool outputs for additional context)
```

**The agent handles all synthesis requirements:**
- Narrative architecture and storytelling
- Evidence standards and citation format
- Podcast-optimized writing
- Accessibility without oversimplification
- Source organization and verification
- Quality checklist validation

**VERIFY SYNTHESIS COMPLETE:**

```bash
# Check report.md exists and has content
ls -lh podcast/episodes/YYYY-MM-DD-slug/report.md
wc -w podcast/episodes/YYYY-MM-DD-slug/report.md
```

**Expected output:**
- ✅ report.md exists
- ✅ File size: 15-25KB
- ✅ Word count: 5,000-8,000 words (typical for 30-40 min episode)

---

**EXIT CRITERIA (all must be true to proceed):**
✓ report.md created in episode root directory
✓ File size 15-25KB (~5,000-8,000 words)
✓ Narrative structure (not bullet points)
✓ All claims have source citations
✓ Citations link to verified sources from research/p3-briefing.md

**Update todos:**
```
Mark "Synthesize narrative report" as completed.
Mark "Create episode content plan" as in_progress.
```

═══════════════════════════════════════════════════════════════

---

═══════════════════════════════════════════════════════════════
                    PHASE 8: EPISODE PLANNING
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ report.md created (Phase 7)
✓ sources.md created with validated citations
✓ Ready to create episode structure guidelines for NotebookLM

**⚠️ DO NOT STOP AND WAIT FOR USER - INVOKE SKILL AUTOMATICALLY**

**WORK TO DO:** Invoke the podcast-episode-planner skill to create content_plan.md:

Use the Task tool with subagent_type='general-purpose':

```
Create episode content plan using the podcast-episode-planner skill.

Episode directory: podcast/episodes/YYYY-MM-DD-slug/
Episode title: [Episode Title]
Series name: [Series name or "Standalone"]

Follow .claude/skills/podcast-episode-planner/SKILL.md to:
1. Read report.md and sources.md
2. Classify episode type (evidence status, content density, series position)
3. Select toolkit elements (hook type, takeaway structure, etc.)
4. Create content_plan.md with three-section structure and NotebookLM guidance
5. Log to logs/prompts.md

Required files must exist:
- report.md (narrative synthesis)
- sources.md (validated citations)
```

**The skill produces:**
- `content_plan.md` - Episode structure guide with NotebookLM instructions (8-12KB)

**What content_plan.md provides for NotebookLM:**
- Three-section structure (Foundation → Evidence → Application)
- Key terms that must be defined
- Specific studies/findings to emphasize
- Narrative arc and transitions
- Opening hook and closing callback guidance

**VERIFY EPISODE PLANNING COMPLETE:**

```bash
# Check file exists and has content
ls -lh podcast/episodes/YYYY-MM-DD-slug/content_plan.md
```

**Expected output:**
- ✅ content_plan.md exists (8-12KB)

---

**EXIT CRITERIA (all must be true to proceed):**
✓ content_plan.md created with three-section structure
✓ Key terms to define listed
✓ Studies/findings to emphasize identified
✓ Narrative arc guidance included

**Update todos:**
```
Mark "Create episode content plan" as completed.
Mark "Generate cover art" as in_progress.
```

═══════════════════════════════════════════════════════════════

---

═══════════════════════════════════════════════════════════════
                    PHASE 9: COVER ART
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ report.md created (Phase 7)
✓ content_plan.md created (Phase 8)
✓ Ready to generate cover art based on episode content

**WORK TO DO:** Immediately invoke cover art subagent:

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
3. Log to logs/prompts.md
4. Report back when complete with file path and size
```

**VERIFY COVER ART COMPLETE:**

```bash
ls -lh podcast/episodes/YYYY-MM-DD-slug/cover.png
```

**Expected output:**
- ✅ cover.png exists
- ✅ File size: ~400-600KB
- ✅ Dimensions: 3000x3000px (podcast standard)

---

**EXIT CRITERIA (all must be true to proceed):**
✓ cover.png created in episode root directory
✓ File size appropriate (~400-600KB)
✓ Branding applied (logo, series/episode text, yellow border)
✓ Image dimensions: 3000x3000px
✓ Logged to logs/prompts.md

**Update todos:**
```
Mark "Generate cover art" as completed.
```

═══════════════════════════════════════════════════════════════

---

═══════════════════════════════════════════════════════════════
                    PHASE 10: AUDIO GENERATION
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ report.md created (Phase 7)
✓ research/p3-briefing.md exists
✓ sources.md exists
✓ Cover art generation launched (Phase 9) - can run in parallel

**Primary Method: NotebookLM Enterprise API**

Uses the Discovery Engine API to automate the NotebookLM workflow:
- Two-host conversational "Deep Dive" format
- Uploads 4 source files automatically
- Custom episodeFocus prompt for Yudame Research branding
- Typical output: 20-40 minute episodes

---

### Generate Audio with NotebookLM API

**Verify source files exist:**
```bash
cd podcast/episodes/EPISODE_PATH
ls -lh research/p1-brief.md report.md research/p3-briefing.md sources.md content_plan.md
```

**Run the API script:**
```bash
cd podcast/tools
uv run python notebooklm_api.py ../episodes/YYYY-MM-DD-slug/ --series "Series Name" --cleanup
```

**Arguments:**
- `episode_dir` - Path to episode directory (required)
- `--series` - Series name for audio intro (optional)
- `--title` - Episode title, defaults to directory name (optional)
- `--cleanup` - Delete notebook after generation (optional)
- `--timeout` - Timeout in minutes, default 30 (optional)

**What the script does:**
1. Creates notebook via Discovery Engine API
2. Uploads 5 source files (p1-brief.md, report.md, p3-briefing.md, sources.md, content_plan.md)
3. Generates audio with episodeFocus prompt (Yudame Research branding)
4. Polls for completion (typically 5-15 minutes)
5. Downloads MP3 to episode directory

**Output files:**
- `EPISODE_SLUG.mp3` - Final audio (typically 20-40 min)

**Expected runtime:** 5-15 minutes

---

### Fallback: Manual NotebookLM

If API is unavailable, use the manual workflow:

1. **Go to** https://notebooklm.google.com/
2. **Create new notebook**
3. **Upload 5 source files:**
   - `research/p1-brief.md`
   - `report.md`
   - `research/p3-briefing.md`
   - `sources.md`
   - `content_plan.md`

4. **Use the STANDARD TEMPLATE below** (replace `[EPISODE TITLE]` and `[SERIES NAME]` only):

```
Create a two-host podcast episode on: [EPISODE TITLE] from our [SERIES NAME] series

IMPORTANT: Follow the structure and guidance in content_plan.md - it contains:
- The opening hook to use
- Key terms to define (with pronunciations)
- Studies to emphasize
- Three-section narrative arc (Foundation → Evidence → Application)
- Closing callback and sign-off

Brand elements:
- Producer: Valor Engels
- Open with: "Welcome to Yuda Me Research from our [SERIES NAME] series by Valor Engels..."
- Close with: "Find full research and sources at research dot yuda dot me - that's Y-U-D-A dot M-E"

Tone: Intellectually rigorous but accessible - two experts having a genuine conversation, making complex research understandable.

Style guidelines:
- Spell out acronyms on first use: "High-Intensity Interval Training, or HIIT"
- Define technical terms before building on them
- Use specific numbers with context (sample sizes, effect sizes, percentages)
- Distinguish correlation from causation
- Make statistics meaningful through comparisons
- Include human elements when the research contains them

Avoid:
- Undefined jargon
- Fabricated examples (use only what's in the source material)
- Over-hedging that obscures findings
- Repeating context unnecessarily
```

5. **Settings:** Format: Deep Dive, Length: Long
6. **Generate and download audio**

**⚠️ CRITICAL: Do NOT customize the prompt with episode-specific content arcs, story prescriptions, or topic details. The content_plan.md file contains all the episode-specific guidance that NotebookLM needs. The prompt above is a quality/style template only.**

After manual generation, process the audio with `podcast-audio-processing` skill for transcription.

---

**Update todos when audio is ready:**
```
Mark "Generate audio" as completed.
Mark "Process audio (chapters)" as in_progress.
```

---

═══════════════════════════════════════════════════════════════
                    PHASE 11: AUDIO PROCESSING
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ Audio generated (Phase 10) via NotebookLM API
✓ Audio file is in episode directory (.mp3)

---

### Transcribe and Create Chapters

**NotebookLM output requires transcription:**

```bash
cd podcast/episodes/EPISODE_PATH

# 1. Verify files exist
ls -la *.mp3 transcript.txt

# 2. Get file metadata
ls -l *.mp3 | awk '{print $5}'  # File size in bytes
ffmpeg -i *.mp3 2>&1 | grep Duration  # Duration
```

**Create chapters from transcript/script:**
- Read script.md or transcript.txt and identify 10-15 natural topic transitions
- Use `[TRANSITION: new section]` markers as primary chapter boundaries
- Create `EPISODE_SLUG_chapters.txt` (FFmpeg format) and `EPISODE_SLUG_chapters.json` (Podcasting 2.0)
- See chapter format templates in podcast-audio-processing skill

**Embed chapters:**
```bash
ffmpeg -i EPISODE_SLUG.mp3 -i EPISODE_SLUG_chapters.txt -map_metadata 1 -codec copy temp.mp3 -y
mv temp.mp3 EPISODE_SLUG.mp3
```

---

### If NotebookLM Audio (Phase 9 Option B)

**Invoke audio processing subagent:**

Use the Task tool to invoke the `podcast-audio-processing` skill:

```
Process the podcast audio file for this episode using the podcast-audio-processing skill.

Episode path: podcast/episodes/YYYY-MM-DD-slug
Audio filename: [filename user provided, e.g., 'Original_Audio.m4a']
Episode slug: YYYY-MM-DD-slug

Follow the podcast-audio-processing skill Workflow B to:
1. Convert to mp3 if needed (m4a → mp3)
2. Get file metadata (size in bytes, duration)
3. Transcribe with local Whisper (base model) → save to tmp/
4. Analyze transcript and create 10-15 chapter markers
5. Embed chapters into mp3
6. Log to logs/prompts.md

CRITICAL: Report back the file metadata when complete:
- Duration: MM:SS format
- File size: bytes
This metadata is needed for the publishing phase.
```

---

**VERIFY AUDIO PROCESSING SUCCEEDED:**

After processing completes, check:

```bash
# 1. Verify mp3 exists with correct name
ls -lh podcast/episodes/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp3

# 2. Check file size and duration
ffmpeg -i YYYY-MM-DD-slug.mp3 2>&1 | grep -E "Duration|bitrate"

# 3. Verify transcript exists
ls -lh podcast/episodes/YYYY-MM-DD-slug/transcript.txt  # Gemini
ls -lh podcast/episodes/YYYY-MM-DD-slug/tmp/*_transcript.json  # NotebookLM

# 4. Verify chapters JSON exists
ls -lh podcast/episodes/YYYY-MM-DD-slug/*_chapters.json

# 5. Verify chapters are embedded in mp3
ffmpeg -i YYYY-MM-DD-slug.mp3 -f ffmetadata - 2>/dev/null | grep CHAPTER
```

**Expected outputs:**

| Source | mp3 | Duration | Transcript | Chapters |
|--------|-----|----------|------------|----------|
| Gemini | ~30MB | ~36:00 | transcript.txt (~15KB) | 10-15 |
| NotebookLM | ~30-40MB | 30-40 min | tmp/*_transcript.json (~400KB) | 10-15 |

**⚠️ Common issues:**

| Issue | Diagnosis | Solution |
|-------|-----------|----------|
| Gemini audio short (<20 min) | Context too small | Check 4 input files total 80KB+ |
| Conversion failed | Check ffmpeg installed | `brew install ffmpeg` |
| Transcription slow | Normal for base model | Wait 5-10 min for 30-40 min audio |
| No chapters found | Check transcript exists | Verify transcript file present |
| Chapters not embedded | FFmpeg metadata error | Re-run embed command manually |

---

**EXIT CRITERIA (all must be true to proceed):**
✓ Final mp3 file exists with correct naming (YYYY-MM-DD-slug.mp3)
✓ File size known (exact bytes)
✓ Duration known (MM:SS or HH:MM:SS format)
✓ Transcript exists (transcript.txt OR tmp/*_transcript.json)
✓ Chapters JSON created (*_chapters.json)
✓ Chapters embedded in mp3 (verified with ffmpeg)
✓ Chapter count: 10-15 chapters
✓ All steps logged to logs/prompts.md

**⚠️ DO NOT PROCEED TO PHASE 11 UNTIL FILE METADATA IS CONFIRMED**

**Update todos:**
```
Mark "Process audio (transcribe, chapters)" as completed.
Mark "Create publishing metadata" as in_progress.
```

═══════════════════════════════════════════════════════════════

---

═══════════════════════════════════════════════════════════════
                    PHASE 12: PUBLISHING
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ Audio processing complete (Phase 11)
✓ Duration known (MM:SS format)
✓ File size known (exact bytes)
✓ Transcript exists (transcript.txt)
✓ report.md and research/p3-briefing.md available

**WORK TO DO:** Generate episode description, keywords, and source links:

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
   - Use sources from research/p3-briefing.md (Tier 1 and Tier 2 prioritized)
   - Verify links are still accessible with WebFetch when possible
   - Prioritize: official legislation/regulation, academic analysis, primary sources
   - These will be formatted as clickable HTML links in `<content:encoded>`

**Create logs/metadata.md:**

```markdown
# Episode Publishing Metadata

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

**Update feed.xml using update_feed.py:**

```bash
cd ~/src/research/podcast/tools

# Preview changes (dry-run)
uv run python update_feed.py ../episodes/EPISODE_PATH/ --dry-run

# Apply changes
uv run python update_feed.py ../episodes/EPISODE_PATH/
```

**What update_feed.py does:**
1. Reads logs/metadata.md for title, description, keywords, sources
2. Auto-detects audio file, cover.png, chapters JSON
3. Gets duration/size from file if not in metadata
4. Generates complete `<item>` XML with plain text + HTML content
5. Inserts into feed.xml at correct position
6. Updates `<lastBuildDate>`

🚨 **CRITICAL: Validate feed.xml**

**Invoke feed validation subagent via Task tool:**

```
Use the Task tool with subagent_type='general-purpose':

"Validate the podcast feed against RSS specification standards using the podcast-feed-validator skill.

Feed path: podcast/feed.xml
Specification path: docs/RSS-specification.md
Episode to validate: Most recent episode only

Follow the podcast-feed-validator skill to:
1. Read docs/RSS-specification.md (Sections 1, 2, 3, and 8)
2. Read podcast/feed.xml and identify the most recent episode
3. Validate channel-level metadata (Section 1 requirements)
4. Validate episode metadata (Section 2 & 3 requirements)
5. Verify file metadata accuracy (actual file size and duration match feed)
6. Check XML structure validity
7. Perform content quality checks (report links, source URLs, HTML formatting)
8. Provide validation report with specific issues and fixes needed

Return comprehensive validation report showing:
- ✅ Passed checks
- ❌ Failed checks with specific fixes
- ⚠️ Warnings for optional elements

If validation fails, DO NOT proceed to Phase 12 until issues are fixed."
```

**VERIFY FEED.XML UPDATE:**
```bash
git diff podcast/feed.xml | head -50
```

**Expected output:**
- New `<item>` entry visible
- `<lastBuildDate>` updated in channel metadata
- Duration matches file: MM:SS format
- File size matches: exact bytes
- pubDate in RFC 2822 format

**⚠️ Common issues:**
- Duration mismatch → Re-check with `ffmpeg -i file.mp3 2>&1 | grep Duration`
- File size wrong → Re-check with `ls -l file.mp3 | awk '{print $5}'`
- Invalid XML → Check for unclosed tags, improper escaping

---

**EXIT CRITERIA (all must be true to proceed):**
✓ logs/metadata.md created with all fields
✓ Episode description written (1-2 sentences + report link)
✓ Keywords generated (5-10 episode-specific terms)
✓ Key sources validated (3-5 Tier 1/2 sources with working URLs)
✓ feed.xml updated with new `<item>` entry
✓ `<lastBuildDate>` updated in feed.xml channel metadata
✓ All metadata accurate (duration matches file, size matches file, pubDate is RFC 2822)
✓ 🚨 **Feed validator reports VALID or VALID WITH WARNINGS** (not INVALID)
✓ All ❌ failed checks from validator have been fixed
✓ File metadata verification passed (size and duration match actual files)

**⚠️ DO NOT PROCEED TO PHASE 12 UNTIL ALL EXIT CRITERIA MET**

**Update todos:**
```
Mark "Create publishing metadata" as completed.
Mark "Update feed.xml and commit" as in_progress.
```

═══════════════════════════════════════════════════════════════

---

═══════════════════════════════════════════════════════════════
                    PHASE 13: COMMIT & PUSH
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ feed.xml updated with episode metadata
✓ All episode files present in episode directory
✓ Publishing metadata complete (logs/metadata.md)

**CRITICAL:** This phase publishes your episode. Without completing BOTH commit AND push, the episode stays local and never goes live.

---

### Step 1: Review Changes

```bash
git status
git diff feed.xml
```

**VERIFY:**
- All episode files show as untracked or modified
- feed.xml shows new `<item>` entry
- No unexpected changes to other files

---

### Step 2: Stage All Files

```bash
git add podcast/feed.xml podcast/episodes/YYYY-MM-DD-slug/
```

**Files being added:**
- `research/p1-brief.md` - Research brief
- `research/p2-*.md` - Individual tool research outputs
- `research/p3-briefing.md` - Master briefing (organized by topic)
- `research/documents/` - Any PDFs or supporting files (if present)
- `logs/prompts.md` - All prompts used during creation
- `logs/metadata.md` - Publishing metadata
- `tmp/*_transcript.json` - Full Whisper transcript (optional - large file)
- `sources.md` - Source links organized by tier
- `report.md` - Final narrative report from synthesis agent
- `report.html` - HTML report (series only)
- `transcript.html` - HTML transcript (series only)
- `cover.png` - Episode cover art with branding
- `YYYY-MM-DD-slug.mp3` - Final audio with embedded chapters
- `YYYY-MM-DD-slug_chapters.json` - Podcasting 2.0 format
- Updated `feed.xml`

**Note:** .m4a source files are gitignored automatically (see .gitignore line 23)

**VERIFY FILES STAGED:**
```bash
git status
```

**Expected output:** All episode files should show in "Changes to be committed" (green)

---

### Step 3: Commit Changes

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

**VERIFY COMMIT SUCCEEDED:**
```bash
git log -1 --oneline
git status
```

**Expected output:**
- `git log` shows your commit message
- `git status` shows "nothing to commit, working tree clean"

**❌ If commit fails:** Check error message. Common issues:
- "nothing to commit" → Files weren't staged, run `git add` again
- Hook failures → Fix issues and retry commit

---

### Step 4: 🚨 **CRITICAL - Push to GitHub** 🚨

```bash
git push
```

**⚠️ WHY THIS MATTERS:**
Without push, the episode stays on your local machine and **NEVER goes live** on GitHub Pages. The workflow is NOT complete until this step succeeds.

**VERIFY PUSH SUCCEEDED:**
```bash
git log -1 --oneline
git ls-remote origin main | grep main
```

**Expected output:**
- Both commands show the SAME commit hash
- Example: `a1b2c3d feat: Add episode on topic`

**✅ If hashes match:** Push succeeded
**❌ If hashes don't match:** Push failed, run `git push` again

**Common push failures:**

| Error | Solution |
|-------|----------|
| "Updates were rejected (non-fast-forward)" | `git pull --rebase origin main` then `git push` |
| "Permission denied" | Check GitHub authentication |
| "Could not resolve host" | Check internet connection |

---

### Step 5: ✅ **FINAL VERIFICATION - Episode is Live**

Wait 2-3 minutes for GitHub Pages deployment, then verify:

```bash
curl -s https://research.yuda.me/podcast/feed.xml | grep -A 5 "YYYY-MM-DD-slug"
```

**Expected output:** Should return the episode title and enclosure URL

**Alternative verification:** Visit https://research.yuda.me/podcast/feed.xml in browser and search for episode title

**✅ Episode is live when:**
- feed.xml shows new episode
- Episode appears in podcast players (may take 30-60 min for refresh)

**❌ If not found after 5 minutes:**
- Check GitHub Actions: https://github.com/[user]/research/actions
- Look for failed workflows
- Check Pages settings: Settings → Pages → Source should be "main" branch

---

**EXIT CRITERIA (all must be true to complete workflow):**
✓ Commit created successfully
✓ Push completed successfully
✓ Commit hash matches on local and remote
✓ feed.xml updated on live site (after 2-3 min)
✓ Episode appears in feed.xml

**Update todos:**
```
Mark "Update feed.xml and commit" as completed.
Mark "Commit & Push" as completed.
ALL EPISODE WORKFLOW TASKS COMPLETE! ✅
```

═══════════════════════════════════════════════════════════════

## Role Division

**User handles:**
- Manual research submission for web-based tools (Grok, Claude)

**You handle:**
- File organization and directory setup
- Reading seed research-prompt.md if present
- **Phase 1:** Setup - Creating episode directory and initial files
- **Phase 2:** Perplexity API automation for academic research (30-120 seconds)
- **Phase 3:** Analyzing Perplexity results and conducting question discovery
- **Phase 4:** Generating targeted prompts and running GPT-Researcher, Gemini research
- **Phase 5:** Cross-validation matrix creation across all research sources
- **Phase 6:** Master research briefing compilation (research/p3-briefing.md)
- **Phase 7:** **Invoking podcast-synthesis-writer agent** to create report.md
- **Phase 8:** **Invoking podcast-episode-planner** to create content_plan.md
- **Phase 9:** Cover art generation (Gemini via OpenRouter) and branding
- **Phase 10:** Audio generation via NotebookLM Enterprise API
- **Phase 11:** Transcription (Whisper), chapter creation and embedding
- **Phase 12:** Description, keywords, source validation, feed.xml update
- **Phase 13:** Git commit and push (publishes episode)

**Audio Generation:**
- **Primary:** NotebookLM Enterprise API (`.claude/skills/notebooklm-enterprise-api/`) - Two-host conversational format, automated via Discovery Engine API
- **Manual fallback:** NotebookLM web interface (`.claude/skills/notebooklm-audio/`) - Use when API unavailable


## Getting Started

When user wants to create a new episode:

1. **Create todo list** with TodoWrite tool
2. **Determine episode details** (use today's date; only ask about series/slug/title if not provided)
3. **Check for existing research-prompt.md** (seed document) and read if present
4. **Phase 1:** Create episode directory and initial files (research/, logs/, tmp/, sources.md)
5. **Phase 2:** Run Perplexity API for academic foundation (30-120 seconds)
6. **Phase 3:** Analyze Perplexity results, conduct question discovery
7. **Phase 4:** Run targeted research (GPT-Researcher, Gemini automated; Grok, Claude manual)
8. **Phase 5:** Create cross-validation matrix across all sources
9. **Phase 6:** Compile master briefing (research/p3-briefing.md organized by topic)
10. **Phase 7:** Invoke podcast-synthesis-writer agent to create report.md
11. **Phase 8:** Invoke podcast-episode-planner to create content_plan.md
12. **Phase 9:** Generate cover art (Gemini via OpenRouter) and apply branding
13. **Phase 10:** Generate audio via NotebookLM Enterprise API (~5-15 min)
14. **Phase 11:** Transcribe with Whisper, create chapters, and embed in mp3
15. **Phase 12:** Create metadata, update feed.xml, validate with podcast-feed-validator
16. **Phase 13:** Git commit and push to publish (EPISODE LIVE)

**Key:** Update TodoWrite at every phase transition. The sequential workflow builds research progressively: academic foundation → question discovery → targeted followup, producing higher quality, better verified, non-redundant research.
