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
- [ ] **Phase 8: Cover Art** → cover.png generated and branded
- [ ] **Phase 9: Audio Generation** → Gemini (automated) OR NotebookLM (manual)
- [ ] **Phase 10: Audio Processing** → Chapters created and embedded (transcription done in Phase 9 for Gemini)
- [ ] **Phase 11: Publishing** → feed.xml updated with episode metadata
- [ ] **Phase 12: Commit & Push** → Changes committed and pushed to GitHub

**Verification:** After Phase 12, check https://research.yuda.me/podcast/feed.xml refreshes with new episode in 2-3 minutes.

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
├── report.html                         # HTML report (series only - for index page)
├── transcript.html                     # HTML transcript (series only - for index page)
├── sources.md                          # Source documentation
├── YYYY-MM-DD-topic-slug.mp3          # Final audio file with chapters (~30MB)
└── YYYY-MM-DD-topic-slug_chapters.json # Podcasting 2.0 chapter metadata
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
- Conduct parallel deep research (status: pending)
- Cross-validate research findings (status: pending)
- Create master research briefing (status: pending)
- Synthesize narrative report (status: pending)
- Generate cover art (status: pending)
- Generate audio (Gemini or NotebookLM) (status: pending)
- Process audio (chapters, embed) (status: pending)
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
- DO NOT copy it as the deep research prompts - you'll create new ones in logs/prompts.md

**Create the appropriate directory structure (if needed):**

**For series episodes:**
```bash
mkdir -p ~/src/research/podcast/episodes/series-name/epX-topic-slug/{research/documents,logs,tmp}
```

**For standalone episodes:**
```bash
mkdir -p ~/src/research/podcast/episodes/YYYY-MM-DD-topic-slug/{research/documents,logs,tmp}
```

**Create all episode files:**

**IMPORTANT:** Replace all `YYYY-MM-DD` placeholders with today's actual date in ISO format (e.g., 2025-12-15). Never use placeholder dates in created files.

**logs/prompts.md:**
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
- Conflicting sources noted in research-briefing.md
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
                    PHASE 2-4: RESEARCH
═══════════════════════════════════════════════════════════════

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
6. Output marked research ready to paste into research-results.md

Research prompt: [insert Perplexity prompt from prompts.md]"
```

**Expected time:** 30-120 seconds (much faster than browser-based tools)

**Fallback if skill unavailable or API fails:**
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
Mark "Generate cover art" as in_progress.
Mark "Obtain audio from NotebookLM" as in_progress (user's parallel task).
```

═══════════════════════════════════════════════════════════════

---

═══════════════════════════════════════════════════════════════
                    PHASE 8: COVER ART
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ report.md created (Phase 7)
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
                    PHASE 9: AUDIO GENERATION
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ report.md created (Phase 7)
✓ sources.md created with validated citations
✓ research/p1-brief.md available (Phase 1 academic briefing)
✓ research/p3-briefing.md available (Phase 6 master briefing)
✓ Cover art generation launched (Phase 8) - can run in parallel

**Two audio generation options:**
- **Option A: Gemini Native Audio** (automated, ~15-30 min) - Uses Gemini 2.5 to generate audio locally
- **Option B: NotebookLM** (manual, user-driven) - User generates audio via Google NotebookLM

---

### Option A: Gemini Audio Generation (Recommended)

**4 Critical Input Files Required:**

| File | Location | Purpose | Required |
|------|----------|---------|----------|
| `report.md` | Episode root | Synthesized research report | **Yes** |
| `sources.md` | Episode root | Validated source citations | Recommended |
| `p1-brief.md` | `research/` | Phase 1 academic briefing | Recommended |
| `p3-briefing.md` | `research/` | Phase 3 master briefing | Recommended |

**Target context size:** 80-150KB combined for optimal 36-minute episode

**Verify input files exist:**
```bash
cd podcast/episodes/EPISODE_PATH
ls -la report.md sources.md research/p1-brief.md research/p3-briefing.md
wc -c report.md sources.md research/p1-brief.md research/p3-briefing.md
```

**Invoke Gemini audio generation:**

Use the Task tool to invoke the `podcast-audio-processing` skill with Gemini mode:

```
Generate podcast audio for this episode using the podcast-audio-processing skill with Gemini.

Episode path: podcast/episodes/YYYY-MM-DD-slug
Episode slug: YYYY-MM-DD-slug

Required input files (verify all 4 exist):
- report.md (synthesized research report)
- sources.md (validated citations)
- research/p1-brief.md (Phase 1 academic briefing)
- research/p3-briefing.md (Phase 3 master briefing)

Follow the podcast-audio-processing skill Workflow A to:
1. Verify all 4 required input files exist
2. Check combined context size (target: 80-150KB)
3. Run generate_audio.py --context-rich mode
4. Process output (transcribe, chapters, embed)
5. Log to logs/prompts.md

CRITICAL: Report back the file metadata when complete:
- Duration: MM:SS format (target: ~36:00)
- File size: bytes
```

**Expected runtime:** 15-30 minutes depending on API latency

**What Gemini generation does:**
1. Loads ALL 4 source materials as rich context (NotebookLM-style)
2. Generates 3 parts (~12 minutes each) using Gemini 2.5 Native Audio API
3. Feeds transcript of each part into the next for continuity
4. Stitches parts together into final ~36 minute episode
5. Transcribes using local Whisper
6. Outputs: mp3 file + transcript.txt

**Output files:**
- `EPISODE_SLUG.mp3` - Final stitched audio (~30MB)
- `transcript.txt` - Full episode transcript
- `tmp/generation_metrics.json` - Generation stats

**Skip to Phase 10** for chapter creation and embedding after Gemini completes.

---

### Option B: NotebookLM Audio Generation (Manual)

**Files to upload to NotebookLM:**
1. `report.md` (narrative synthesis from podcast-synthesis-writer)
2. `research/p3-briefing.md` (organized source material)
3. `research/p2-*.md` files (individual tool research outputs for additional context)
4. Any PDFs or documents in `research/documents/` folder

**NotebookLM Prompt (Standard Template - DO NOT customize):**

```
Create an intellectually rigorous podcast that balances analytical depth with clear explanation.

Opening: Begin with "Yudame Research" (add series name if applicable) and introduce the topic's value.

Core principles:
- Spell out acronyms first: "High-Intensity Interval Training, or HIIT" - then use acronym
- Define technical terms immediately in plain language before building on them
- Use concrete examples ONLY from source material - never fabricate
- Highlight findings that reveal strategic lessons or challenge assumptions
- Extract frameworks and connect to practical implications
- Maintain scientific rigor: distinguish correlation from causation, note effect sizes and uncertainties

Emphasis areas:
- Spell-first for acronyms, definition-first for technical terms
- Evidence-based analysis: cite studies, report effect sizes, note sample sizes
- Include human elements when they exist: decisions made, reasoning, outcomes
- Use conversational check-ins: "Let me define that term..." or "To be clear..."
- Translate findings to practical meaning and broader patterns

Highlight insights worth examining:
- Counter-intuitive findings that reveal strategic lessons
- Failures that illustrate specific mistakes or systemic issues
- Unexpected outcomes that challenge assumptions
- Make numbers meaningful through context and comparisons

Avoid:
- Undefined acronyms and jargon
- Academic language when simpler words work
- Introducing 3+ new technical terms in one sentence
- Fabricated examples or over-hedging that obscures findings
- Dry explanations when human stories exist in research
- Repeatedly restating context

Target: Intelligent listeners wanting deep understanding and practical insights. Appreciate technical depth but need terms defined.

Tone: Intellectually rigorous but accessible - "conversational expert explaining to a bright student"

When presenting stories:
- Include decision-making context: "Do Kwon announced X, which led to Y" not "The protocol experienced stress"
- Provide specific details: "On Friday afternoon, Circle announced..." not "Circle had exposure"
- Use precise numbers for context: "$3.3 billion frozen over a weekend" not "some funds were inaccessible"
- Show scale through comparisons: "Supply increased from millions to trillions - a thousand-fold change"
- Connect to lessons: Explain what the outcome reveals about systems, incentives, or strategy

When presenting research: Focus on what numbers mean, use comparisons ("like losing 5 years of profits"), translate statistics to implications.

Closing: Summarize 2-3 key takeaways, close with "Find full research and sources at research dot yuda dot me - that's Y-U-D-A dot M-E"
```

**Add to logs/prompts.md under "NotebookLM Audio Generation Phase"**

**Settings:**
- Format: **Deep Dive** (or Brief/Critique/Debate as appropriate)
- Length: **Long** (or adjust based on topic complexity)

**Inform user:**
"Ready for NotebookLM audio generation:

1. Upload these files to NotebookLM:
   - report.md (narrative report)
   - research/p3-briefing.md (organized sources)
   - research/p2-*.md files (individual tool research)
   - Any research/documents/ files if present

2. Use 'Audio Overview' feature with the prompt saved in logs/prompts.md (just added)

3. Select format: Deep Dive, Length: Long

4. Generate and download the audio file

5. Return with the audio file and I'll process it (transcribe, chapters, embed)"

---

**Update todos when audio is ready:**
```
Mark "Obtain audio" as completed.
Mark "Process audio (transcribe, chapters)" as in_progress.
```

---

═══════════════════════════════════════════════════════════════
                    PHASE 10: AUDIO PROCESSING
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ Audio generated (Phase 9) - either via Gemini or NotebookLM
✓ Audio file is in episode directory (.mp3 for Gemini, .m4a/.mp3 for NotebookLM)
✓ Transcript available (transcript.txt for Gemini, needs creation for NotebookLM)

**Processing differs based on Phase 9 audio source:**

---

### If Gemini Audio (Phase 9 Option A)

Gemini already produced:
- `EPISODE_SLUG.mp3` - Final audio file
- `transcript.txt` - Full transcript

**Remaining work:** Create chapters and embed them

```bash
cd podcast/episodes/EPISODE_PATH

# 1. Verify files exist
ls -la *.mp3 transcript.txt

# 2. Get file metadata
ls -l *.mp3 | awk '{print $5}'  # File size in bytes
ffmpeg -i *.mp3 2>&1 | grep Duration  # Duration
```

**Create chapters from transcript:**
- Read transcript.txt and identify 10-15 natural topic transitions
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
                    PHASE 11: PUBLISHING
═══════════════════════════════════════════════════════════════

**ENTRY REQUIREMENTS:**
✓ Audio processing complete (Phase 10)
✓ Duration known (MM:SS format)
✓ File size known (exact bytes)
✓ Transcript exists (tmp/*_transcript.json)
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

**Update feed.xml following RSS specification in `docs/RSS-specification.md`**

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
                    PHASE 12: COMMIT & PUSH
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
- NotebookLM audio generation (if using Option B in Phase 9)

**You handle:**
- File organization and directory setup
- Reading seed research-prompt.md if present
- **Phase 1:** Creating comprehensive Perplexity academic research prompt
- **Phase 2:** Attempting Perplexity API automation (30-120 seconds)
- **Phase 3:** Analyzing Perplexity results and conducting question discovery
- **Phase 4:** Generating targeted Phase 3 prompts based on discovered questions
- **Phase 5:** Attempting automation for ChatGPT, Gemini research as needed
- **Phase 6:** Cross-validation matrix creation across all research sources
- **Phase 7:** Master research briefing compilation organized by topic
- **Phase 8:** **Invoking podcast-synthesis-writer agent** to create report.md
- **Phase 9:** Cover art generation (Gemini via OpenRouter) and branding
- **Phase 10:** Audio generation via Gemini Native Audio (Option A - automated) OR processing NotebookLM audio (Option B)
- **Phase 11:** Chapter generation from transcript analysis
- **Phase 12:** Description, keywords, source validation for metadata
- **Phase 13:** feed.xml updates
- **Phase 14:** Git workflow and commits

**Audio Generation Options:**
- **Option A (Gemini - Recommended):** Fully automated using `generate_audio.py --context-rich`. Requires 4 input files: report.md, sources.md, research/p1-brief.md, research/p3-briefing.md (80-150KB combined). Produces ~36-minute episode.
- **Option B (NotebookLM):** User manually generates audio via NotebookLM. You process the resulting m4a/mp3 file.


## Getting Started

When user wants to create a new episode:

1. **Create todo list** with TodoWrite tool
2. **Determine episode details** (use today's date; only ask about series/slug/title if not provided)
3. **Check for existing research-prompt.md** (seed document) and read if present
4. **Create all episode files** including research-briefing.md
5. **Phase 1:** Creating comprehensive Perplexity academic research prompt
6. **Phase 2:** Attempting Perplexity API automation (30-120 seconds)
7. User pastes Perplexity results into research-results.md when complete
8. **Phase 3:** Analyzing Perplexity results and conducting question discovery
9. **Phase 4:** Generating targeted Phase 3 prompts based on discovered questions
10. **Phase 5:** Attempting automation for ChatGPT, Gemini research as needed
11. User collects all Phase 3 research into research-results.md
12. **Phase 6:** Cross-validation matrix creation across all research sources
13. **Phase 7:** Master research briefing compilation organized by topic
14. **Phase 8:** Invoking podcast-synthesis-writer agent to create report.md from research materials
15. **Phase 9:** Cover art generation (Gemini via OpenRouter) and branding
16. **Phase 10:** Audio generation:
    - **Option A (Recommended):** Gemini Native Audio via `generate_audio.py --context-rich`
      - Uses 4 critical files: report.md, sources.md, research/p1-brief.md, research/p3-briefing.md
      - Produces ~36-minute episode automatically
    - **Option B:** NotebookLM (user generates manually, you process the file)
17. **Phase 11:** Chapter generation and embedding
18. **Phase 12:** Description, keywords, source validation for metadata
19. **Phase 13:** feed.xml updates
20. **Phase 14:** Git workflow and commits

**Key:** Update TodoWrite at every phase transition. The sequential workflow builds research progressively: academic foundation → question discovery → targeted followup, producing higher quality, better verified, non-redundant research.
