# Prompts Used for Episode: Algorithms for Life: Ep. 1, Spaced Repetition

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** The `research-prompt.md` file contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-15
- Slug: ep1-spaced-repetition
- Title: Algorithms for Life: Ep. 1, Spaced Repetition - The Algorithm That Optimizes How We Remember
- Series: Algorithms for Life
- Episode Number: 1

---

## Deep Research Phase

### Tool Configuration

**Automated tools:**
- **Perplexity:** Academic & Official Sources (Phase 1 - always used, API-based)
- **GPT-Researcher:** Industry & Technical Sources (Phase 3 - API-based, uses OpenAI GPT-5.2)
- **Gemini Deep Research:** Strategic & Policy Sources (Phase 3 - API-based)

**Manual tools (user runs these):**
- **Grok:** Real-Time & Regional Sources (Phase 3 - user pastes from https://x.com/i/grok)

**Default approach:** Use all Phase 3 tools (Grok, GPT-Researcher, Gemini) unless a tool's focus area is clearly not relevant to the topic. Omitting a tool should be rare.

### Deep Research Prompts (Copy-Paste Ready)

**IMPORTANT:** These prompts use single newlines only to prevent accidental partial submissions when pasting into Chrome-based tools.

---

## Phase 1: Perplexity Academic Research

**Prompt created:** 2025-12-15

**Phase 1 Perplexity Prompt (Academic Foundation):**

```
Research spaced repetition as an algorithmic approach to learning and memory optimization, covering neuroscience foundations, algorithmic implementations, effectiveness evidence, and limitations.

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

## Phase 2: Question Discovery Analysis

**Date:** 2025-12-15

After analyzing Perplexity's comprehensive academic research (~6,500 words, 10,721 tokens), here are the key questions we should investigate with targeted Phase 3 research:

### What subtopics and themes emerged from Phase 1?

**Strongly covered areas:**
- Neuroscience foundations (molecular mechanisms, CREB, MAPK, synaptic plasticity, hippocampal-cortical transfer)
- Cognitive theories (study-phase retrieval, encoding variability, deficient processing)
- Algorithm history (SM-0 through SM-18, FSRS with power functions)
- Meta-analytic evidence (effect sizes, optimal intervals matching retention interval)
- Domain applications (vocabulary learning, medical education, motor skills)
- Testing effects and interleaving
- Individual differences (working memory, age, prior knowledge)
- Metacognitive misalignment (learners prefer massed despite spaced being better)

**Brief mentions needing expansion:**
- Specific SRS applications (Anki, Duolingo, Memrise mentioned in seed prompt but not in Perplexity results)
- Mobile/UX considerations (notifications, streaks, microlearning)
- Recognition vs production gap in language learning
- Context-dependent memory problems
- Integration with comprehensible input approaches
- AI-enhanced flashcard generation

### What gaps exist in the academic literature (per Perplexity)?

- **Long-term retention beyond months** - Most studies measure days to months, not years or decades
- **Far transfer** - Studies focus on near transfer (same items), not application to novel contexts
- **Implementation science** - Why doesn't spaced repetition get adopted despite strong evidence?
- **Prerequisite dependencies** - Algorithms don't model hierarchical knowledge structures
- **Domain differences** - Why do mathematics show smaller spacing effects?
- **Mental rehearsal** - Proposed but not directly measured during spacing intervals
- **Working memory integration** - Algorithms don't assess/adapt to individual WM capacity

### What recent developments aren't covered by academic research?

- **Mobile-first SRS design** (last 5-10 years) - Perplexity covered algorithms but not mobile UX evolution
- **Duolingo's streak psychology and gamification research** - Company research may not be in peer-reviewed literature
- **FSRS v4-v6 recent developments** - Perplexity covered it, but recent 2024-2025 updates may exist
- **AI-generated flashcards** - LLM-based content generation for SRS (very recent, post-2023)
- **NotebookLM and podcast-based learning combined with SRS** - Audio learning + spaced repetition integration
- **Community discussions** - What are actual SRS users saying about limitations on forums, Reddit, X?

### What contradictions or uncertainties need more investigation?

- **Expanding vs fixed intervals** - Mixed results, no clear winner
- **Optimal interval formulas** - "10-20% of retention interval" is vague guidance
- **Mathematics spacing effects** - Why smaller effects than other domains?
- **Motor learning** - Some studies show blocked > random, contradicting contextual interference literature
- **Transfer limitations** - How severe is the recognition-production gap in real language use?

### What industry/implementation questions arose?

- **Duolingo vs Anki design philosophy** - Guided gamified vs customizable power-user tool
- **Actual retention rates in the wild** - What do real user data show (not lab studies)?
- **Business model effects** - Does freemium/subscription model affect algorithm design?
- **User retention and dropout** - What percentage of SRS users abandon the system and why?
- **Integration patterns** - How do successful polyglots combine SRS with immersion/conversation?

### What policy/regulatory angles need investigation?

**Verdict: Not applicable for this topic.** Spaced repetition is not a regulated domain, no government policy frameworks apply. Skip Gemini Deep Research for Phase 3.

### What practitioner perspectives are missing?

- **Language learning community views** - What do polyglots and teachers say about SRS limitations?
- **The "Anki problem"** - People with 20,000 cards reviewed but can't hold conversations
- **Supplementation debates** - How much time on SRS vs reading vs speaking vs listening?
- **App comparison discussions** - Real user experiences with different SRS apps
- **Context solutions** - What strategies do practitioners use to overcome decontextualization?

---

## Phase 3: Targeted Research Approach

Based on this analysis, we'll create targeted prompts for:

1. **Grok** (Real-Time & Practitioner Perspectives)
   - Recent SRS app developments and AI integrations (2024-2025)
   - Community discussions on X/Twitter about SRS limitations
   - Polyglot practitioners' views on SRS role in language learning
   - Debates about recognition-production gap and context problems

2. **GPT-Researcher** (Industry & Implementation Analysis)
   - SRS app ecosystem (Anki, Duolingo, Memrise, Clozemaster, LingQ design philosophies)
   - User retention data and dropout rates from app analytics
   - Business models and their influence on algorithm design
   - Integration patterns - how successful learners combine SRS with other methods
   - Case studies of SRS effectiveness in real-world learning

3. **Gemini Deep Research** (Strategic & Policy)
   - **SKIP** - No policy/regulatory angle for this topic

---

## Phase 3: Targeted Followup Research Prompts

### Grok - Recent Developments & Practitioner Perspectives

**Focus:** Real-time discussions, community insights, practitioner experiences (last 12-24 months)

```
Research spaced repetition systems focusing on recent developments and practitioner perspectives:

**Recent Developments (2024-2025):**
- What are the latest developments in SRS apps like Anki, Duolingo, Memrise, and newer entrants?
- How are AI and LLMs being integrated into flashcard generation and spaced repetition systems?
- What mobile UX innovations have emerged (notifications, microlearning, streak mechanics)?

**Practitioner Perspectives:**
- What are language learning communities on X/Twitter saying about SRS effectiveness and limitations?
- What's the current debate about the "recognition vs production gap" - people who can review flashcards but can't speak?
- How do successful polyglots describe integrating SRS with immersion, reading, and conversation practice?
- What criticisms of SRS are prominent in language learning communities?

**Context & Transfer Problems:**
- What strategies do practitioners recommend for overcoming decontextualized flashcard learning?
- What's being discussed about SRS dropout rates and why people abandon daily review habits?

Focus on: Recent discussions on X/Twitter, language learning forums, polyglot insights, app feature announcements.
Provide findings with source links, dates, and community sentiment indicators.
```

---

### GPT-Researcher - Industry & Implementation Analysis

**Focus:** SRS app ecosystem, business models, user data, integration strategies

```
Research spaced repetition systems focusing on industry implementation and real-world effectiveness:

**SRS App Ecosystem:**
- What are the design philosophies and algorithmic approaches of major SRS apps (Anki, Duolingo, Memrise, Clozemaster, LingQ)?
- How do these apps differ in their balance between customization vs guided experience?
- What are the documented user retention and dropout rates for different SRS platforms?

**Business Models & Design:**
- How do freemium/subscription models affect algorithm design and user experience?
- What does Duolingo's published research reveal about streak mechanics, gamification, and long-term engagement?
- What trade-offs exist between maximizing learning effectiveness vs maximizing engagement metrics?

**Integration & Effectiveness:**
- What case studies exist of successful SRS integration into language learning programs?
- How do successful learners combine SRS with other methods (immersion, conversation, reading)?
- What data exists on actual language proficiency outcomes (not just flashcard retention) for SRS users?
- What's the documented evidence on the "recognition-production gap" in real language use?

**Innovation & AI:**
- How are modern apps using AI for personalized flashcard generation and content recommendations?
- What technical innovations have improved SRS effectiveness in the past 5 years?

Focus on: Industry reports, app analytics, published research from companies, case studies, technical documentation, comparative analyses.
Provide comprehensive findings with citations, data sources, and credibility assessment.
```

---

### Claude Research - Comprehensive Synthesis

**Focus:** Multi-dimensional synthesis across academic, industry, and practitioner perspectives

```
Research spaced repetition systems, focusing on comprehensive synthesis questions:

**Bridging Science and Implementation:**
- How do the neuroscience mechanisms of memory consolidation (CREB, MAPK, hippocampal-cortical transfer) translate into the design decisions of modern SRS algorithms like FSRS and SM-18?
- What's the relationship between algorithmic sophistication (adaptive personalization, power-law forgetting curves) and actual learning outcomes in real-world use?
- How does the academic evidence on optimal spacing intervals map to the actual interval schedules used in commercial apps?

**The Recognition-Production Gap:**
- What is the documented evidence on the "recognition vs production gap" in language learning with SRS?
- How severe is the transfer problem from flashcard review performance to actual speaking/writing ability?
- What explains the phenomenon of learners with thousands of reviewed cards who still can't hold basic conversations?

**Integration and Complete Learning Systems:**
- How do successful language learners (polyglots, fluent L2 speakers) describe integrating SRS into broader learning systems?
- What does the evidence show about optimal time allocation between SRS, immersion, conversation practice, and reading for language acquisition?
- What strategies have been proposed or tested for overcoming context-dependent memory limitations in SRS?

**Implementation Paradoxes:**
- Why does strong academic evidence for spacing effects not translate into widespread educational adoption?
- How do business models (freemium, subscription, engagement metrics) affect algorithm design and learning effectiveness?
- What explains the high dropout rates from SRS systems despite demonstrated effectiveness for those who persist?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

---

<!-- Gemini skipped - no policy angle for this topic -->

## Phase 3 Execution Plan

**Tools to run:**
1. ✅ **Grok** (Manual - user will paste from https://x.com/i/grok)
2. ✅ **GPT-Researcher** (Automated - local multi-agent framework with OpenAI GPT-5.2)
3. ✅ **Claude Research** (Manual - user will run via web interface)
4. ❌ **Gemini Deep Research** (SKIP - no policy/regulatory angle applies)

**Next steps:**
1. GPT-Researcher running now (automated)
2. User to run Grok manually
3. User to run Claude Research manually

---

## Cover Art Generation Phase

**Date:** 2025-12-15

**Tool Used:** Gemini 3 Pro Image via OpenRouter

**Generation Method:** --auto from report.md

The cover art was automatically generated by analyzing the report.md content and creating a visual representation of the spaced repetition concept. The AI emphasized dark navy/blue tones with abstract visualization.

**Branding Applied:**
- Position: top-left
- Brand: Yudame Research
- Series: Algorithms for Life
- Episode: Ep 1 - Spaced Repetition
- Border: 20px, #FFC20E (yellow)

**Output:**
- File: cover.png
- Base size: 1024x1024px
- With border: 1064x1064px
- File size: ~593KB PNG

---

## Audio Processing Phase

**Audio File:** Spaced_Repetition_Is_Failing_99_Percent.m4a
**Converted to:** ep1-spaced-repetition.mp3
**Duration:** 43:38.60 (43 minutes, 39 seconds)
**File Size:** 41,898,872 bytes (~40MB)

**Transcription:**
- Tool: Local Whisper (openai-whisper)
- Model: base
- Output: ep1-spaced-repetition_transcript.json (560KB)
- Date: 2025-12-15

**Chapters:**
- Count: 13 chapters
- Created by analyzing transcript for natural topic transitions
- Chapter length: ~3-4 minutes each
- Formats: FFmpeg metadata (.txt) and Podcasting 2.0 (.json)
- Embedded into mp3 file successfully

**Chapter List:**
1. 00:00 - Introduction: The 99.9% Failure Paradox
2. 03:00 - Molecular Switches: CREB and the Biology of Memory
3. 07:00 - MAPK: The 45-Minute Temporal Window
4. 10:00 - Hippocampal-Cortical Transfer: The Long-Term Archive
5. 13:00 - Algorithm History: From SM-0 to SM-2
6. 15:00 - FSRS: Modern Machine Learning Scheduling
7. 18:00 - Prediction vs. Learning: The Critical Gap
8. 21:00 - Anki vs. Duolingo: Two Opposing Philosophies
9. 25:00 - Business Models: Engagement vs. Learning
10. 29:00 - The 140-Year Adoption Failure
11. 33:00 - Recognition-Production Gap: Why Users Can't Speak
12. 37:00 - Polyglot Integration: SRS as Supplement
13. 41:00 - Key Takeaways: Trust Desirable Difficulty

**Date:** 2025-12-15

---
