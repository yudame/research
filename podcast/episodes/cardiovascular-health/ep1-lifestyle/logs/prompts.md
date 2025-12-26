# Prompts Used for Episode: Cardiovascular Health - Ep. 1, Lifestyle Foundations

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-26 (re-research)
- Original Date: 2025-11-21
- Slug: ep1-lifestyle
- Title: Cardiovascular Health - Ep. 1, Lifestyle Foundations
- Series: Cardiovascular Health (6-part series)
- Episode: 1 of 6

---

## Deep Research Phase

### Tool Configuration

**Automated tools:**
- **Perplexity:** Academic & Official Sources (Phase 1 - API-based) ✅ COMPLETED
- **GPT-Researcher:** Industry & Technical Sources (Phase 3 - API-based)
- **Gemini Deep Research:** Strategic & Policy Sources (Phase 3 - API-based)

**Manual tools (user runs these):**
- **Claude:** Comprehensive Synthesis (Phase 3)
- **Grok:** Real-Time & Regional Sources (Phase 3)

### Phase 1: Perplexity Academic Research

**Status:** ✅ COMPLETED 2025-12-26 10:06

**Prompt:**
```
Research the foundational lifestyle factors for cardiovascular health optimization in middle-aged adults (40-year-old male focus). This is Episode 1 of a 6-part series.

**THOROUGH COVERAGE - SLEEP (no dedicated episode exists):**
1. What is the U-shaped relationship between sleep duration and cardiovascular outcomes? Specific effect sizes for short sleep (<6h) and long sleep (>9h) on CVD mortality.
2. How does sleep quality (independent of duration) affect cardiovascular health, blood pressure, and HRV?
3. What are the mechanisms linking sleep to cardiovascular health? (autonomic function, inflammation, hormones, blood pressure dipping)
4. How does sleep affect exercise recovery and training adaptation?
5. What does sleep deprivation do to HRV and autonomic balance?
6. Sleep apnea and cardiovascular risk - the connection.
7. Practical sleep optimization: what does research show about sleep hygiene interventions?

**HIGH-LEVEL INTRO ONLY (dedicated episodes exist):**
- VO2 max: Brief definition, why it predicts longevity (1-MET = 11-17% mortality reduction), conceptual only
- HRV: Brief definition, why low HRV signals cardiovascular risk, conceptual only
- Exercise: Basic volume/frequency recommendations (150-300 min/week), conceptual only - NO training protocols
- Diet: Mediterranean/DASH overview and PREDIMED effect sizes, conceptual only - NO detailed controversies

**LIFESTYLE SYNERGY:**
How do sleep, exercise, and nutrition interact? Life's Essential 8 framework. Can prevent 80%+ of cardiovascular events.

**EXPLICITLY EXCLUDE:**
- Training protocols, polarized training, intervals (Episode 2)
- HRV metrics (RMSSD vs SDNN), devices, overtraining (Episode 3)
- Supplements (Episode 4)
- Saturated fat controversy, ultra-processed foods (Episode 5)
- Meditation, sauna, cold exposure (Episode 6)
```

**Results:** Comprehensive ~7,000 word report with thorough sleep coverage. Saved to research/p2-perplexity.md

---

### Phase 2: Question Discovery

**Analysis completed:** 2025-12-26

**What Perplexity covered well:**
- Sleep duration U-shaped relationship with effect sizes (48% increased CVD risk for <6h, 38-65% for >9h)
- Sleep quality and autonomic function (HRV reduction r=-0.34)
- Mechanisms (HPA axis, sympathetic activation, inflammation, blood pressure dipping)
- Sleep apnea comprehensive (2x sudden death risk)
- CBT-I effectiveness (SMD=-0.90 for insomnia severity)
- High-level intros to VO2 max, exercise, diet (properly scoped)

**Gaps identified for Phase 3:**
1. Recent developments in sleep-CVD research (2024-2025)
2. Practitioner perspectives on real-world sleep optimization barriers
3. Consumer sleep tracking technology and validation
4. Concrete examples of sleep-exercise-nutrition synergy
5. Current official guidelines on sleep for cardiovascular health

---

### Phase 3: Targeted Research Prompts

**📋 GPT-RESEARCHER PROMPT (Automated - 6-20 min):**
```
Research sleep and cardiovascular health, focusing on these specific questions:

**Industry Analysis - Sleep Tracking Technology:**
- What consumer devices (Oura, WHOOP, Apple Watch) show validated accuracy for sleep tracking relevant to cardiovascular health?
- What do sleep tracking studies show about real-world sleep patterns vs. self-reported data?

**Case Studies & Implementation:**
- What sleep intervention programs have been implemented in corporate wellness or healthcare settings?
- What practical barriers do people face in improving sleep, and what works to overcome them?

**Sleep-Exercise Interaction:**
- What specific evidence shows how poor sleep impairs next-day exercise performance or training adaptation?
- What does research show about optimal timing of exercise relative to sleep?

Focus on: Industry reports, case studies, practical implementation data, consumer technology validation.
Provide comprehensive findings with citations.
```

**📋 GEMINI PROMPT (Automated - 3-10 min):**
```
Research sleep and cardiovascular health guidelines, focusing on these specific questions:

**Official Guidelines & Recommendations:**
- What do current AHA, CDC, and WHO guidelines say about sleep duration for cardiovascular health?
- How did the AHA's Life's Essential 8 incorporate sleep? What's the scoring system?

**Healthcare System Approaches:**
- How are healthcare systems screening for sleep disorders as cardiovascular risk factors?
- What policies exist around workplace sleep/rest requirements that affect cardiovascular health?

**Comparative Analysis:**
- How do different countries approach sleep health in cardiovascular disease prevention?

Focus on: Official guidelines, policy documents, healthcare system recommendations.
Provide findings with official source citations.
```

**📋 GROK PROMPT (Manual - User will paste from x.com/i/grok):**
```
Research sleep and cardiovascular health, focusing on these specific questions:

**Recent Developments (2024-2025):**
- What new research on sleep and heart health has been published in the last 12 months?
- Any new findings about sleep tracking, sleep apnea, or sleep interventions?

**Practitioner Perspectives:**
- What are sleep medicine doctors and cardiologists saying about sleep optimization for heart health?
- What practical advice are practitioners giving patients about sleep?

**Real-World Implementation:**
- What are people discussing on social media about sleep tracking devices and cardiovascular health?
- What barriers do people report in trying to improve their sleep?

Focus on: Recent news, professional discussions, practitioner insights, real-world experiences.
Provide findings with source links and dates.
```

**📋 CLAUDE PROMPT (Manual - User will paste from claude.ai):**
```
Research the interaction between sleep and cardiovascular health optimization for middle-aged adults, focusing on:

1. How does sleep quality specifically affect the benefits of exercise training? What happens to training adaptation when sleep is compromised?

2. What is the relationship between sleep timing (chronotype, shift work) and cardiovascular risk beyond just duration?

3. How do sleep, exercise, and nutrition interact synergistically? Provide concrete examples of how optimizing one affects the others.

4. What distinguishes high-quality sleep from just adequate duration? What specific sleep architecture features matter most for cardiovascular health?

**Research methodology:**
- Synthesize across academic, clinical, and practical sources
- Prioritize authoritative sources and meta-analyses
- Note limitations and areas of uncertainty
- Cite sources with URLs where available

Focus on synthesizing the interconnections rather than isolated facts.
```

---

## Notes

- This is Episode 1 of 6 - establishes foundations with thorough sleep coverage
- Sleep is the only foundational topic without a dedicated later episode
- VO2 max, HRV, exercise, diet covered at high level only (dedicated episodes exist)
- Research compiled: 2025-12-26
