# Prompts Used for Episode: Active Recovery: Ep. 3, Emerging Edges

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** The `research-prompt.md` file in this directory contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-15
- Slug: ep3-emerging
- Title: Active Recovery: Ep. 3, Emerging Edges
- Series: Active Recovery
- Episode Number: 3

---

## Deep Research Phase

### Tool Configuration
- **Perplexity:** Academic & Official Sources (Phase 1 - always used)
- **Grok:** Real-Time & Regional Sources (Phase 3 - typically used)
- **GPT-Researcher:** Industry & Technical Sources (Phase 3 - typically used, uses OpenAI GPT-5.2)
- **Gemini Deep Research:** Strategic & Policy Sources (Phase 3 - typically used)
- **Claude Deep Research:** Comprehensive Synthesis (Phase 3 - use when complex questions need multi-dimensional analysis)

**Default approach:** Use all Phase 3 tools (Grok, GPT-Researcher, Gemini, Claude) unless a tool's focus area is clearly not relevant to the topic. Omitting a tool should be rare.

### Deep Research Prompts (Copy-Paste Ready)

**IMPORTANT:** These prompts use single newlines only to prevent accidental partial submissions when pasting into Chrome-based tools.

---

## Phase 1: Perplexity Academic Foundation

**Created:** 2025-12-15

**Purpose:** Establish comprehensive academic foundation on emerging recovery technologies and advanced nutrition with rigorous methodology.

**Prompt (copy-paste ready):**

```
Research emerging recovery technologies and advanced nutrition interventions for athletic recovery, focusing on neuromuscular electrical stimulation (NMES), advanced recovery devices (infrared therapy, pneumatic compression, hyperbaric oxygen), mind-body recovery techniques (mindfulness, breathing techniques for cortisol and heart rate variability), recovery supplements (tart cherry juice, curcumin, bromelain), and comprehensive nutrition planning (protein targets, carbohydrate timing, micronutrients including vitamin D).

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
- Pay special attention to industry funding in recovery technology research
- Note when effect sizes are small even if statistically significant
- Distinguish between acute recovery markers and long-term performance outcomes

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links.
```

**Execution method:** Perplexity Deep Research API (sonar-deep-research model)

**Note:** API timeout encountered with high reasoning effort. Fallback to manual browser submission recommended.

**Manual Execution Steps:**
1. Go to https://www.perplexity.ai/
2. Enable Pro Search
3. Copy the prompt above and paste into Perplexity
4. Wait for results (typically 30-120 seconds)
5. Copy the complete output including citations
6. Paste into research/p2-perplexity.md

---

## Phase 2: Question Discovery

**Completed:** 2025-12-15

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?

**Well-covered areas:**
- NMES efficacy and limitations (meta-analyses available, mixed findings)
- Advanced recovery devices (infrared/PBM, pneumatic compression, HBOT) with industry funding concerns
- Mind-body techniques (mindfulness, breathing, HRV) with distinction between mental vs physical recovery
- Recovery supplements (tart cherry, curcumin, omega-3) with meta-analyses
- Nutrition planning (protein timing controversy, carb timing protocols, vitamin D, micronutrients)
- CWI and contrast therapy (robust meta-analyses with dose-response data)
- Sleep impact on performance (excellent evidence, largest effect sizes)
- Foam rolling and active vs passive recovery

**Briefly mentioned areas:**
- BCAAs (inferior to whey protein, well-established)
- Bromelain (minimal evidence available)
- Individual response variability (mentioned but not explored)
- Sport-specific protocols (generic protocols dominate research)
- Female athletes (substantial literature bias toward males)

### What gaps exist in the academic literature?

1. **Individual response variability**: Why do some athletes respond dramatically to interventions while others don't? Genetic/metabolic determinants unexplored.
2. **Sport-specific recovery protocols**: Most studies use generic protocols; sport-specific demands (intermittent vs endurance vs strength) not tailored.
3. **Female athletes**: Substantial bias toward male participants; sex-specific responses underexplored.
4. **Long-term performance outcomes**: Most studies measure acute biomarkers without demonstrating sustained performance improvements.
5. **Cost-effectiveness analysis**: Expensive devices vs simple interventions - ROI analysis missing.
6. **Practical integration**: How do athletes combine multiple modalities in real training environments?
7. **Elite athlete populations**: Many studies use recreationally active or untrained samples; generalization to elite athletes unclear.

### What recent developments aren't covered?

1. **2024-2025 device innovations**: What new recovery technologies hit market in last 12 months?
2. **Emerging supplements**: New recovery supplements or delivery mechanisms (e.g., liposomal curcumin, new polyphenol sources)?
3. **Wearable recovery tracking**: Integration of HRV monitors, sleep trackers, readiness scores with recovery protocols?
4. **AI-driven recovery personalization**: Any platforms using AI to customize recovery based on individual biomarkers?
5. **Post-pandemic recovery trends**: How has recovery approach evolved since COVID-19 pandemic?
6. **Professional sports team implementations**: What are NBA/NFL/Premier League teams actually using NOW?

### What contradictions or uncertainties need more sources?

1. **Protein timing paradox**: Schoenfeld 2013 meta-analysis vs 2025 review showing nuance - practical reconciliation needed
2. **NMES performance gap**: Molecular evidence (gene expression) vs lack of performance improvement - why?
3. **PBM industry bias**: How to separate legitimate findings from industry-sponsored hype?
4. **HBOT single vs multiple sessions**: Single sessions ineffective but multiple sessions show promise - what's the threshold?
5. **Breathing techniques for cortisol**: Popular claims vs limited peer-reviewed evidence - reality check needed
6. **Acute markers vs performance**: Why do many interventions reduce CK/lactate but not improve actual performance?

### What industry/implementation questions arose?

1. **Cost-benefit of premium devices**: NormaTec ($1000+), Therabody ($2000+), HBOT ($200/session) - worth it vs cold shower and foam roller?
2. **Compliance and practicality**: TCJ requires 2940 mL over 3 weeks - realistic for athletes? Magnesium timing 2h pre-exercise - feasible?
3. **Case studies from elite teams**: How do professional teams integrate these modalities? What's working in practice?
4. **Device usage protocols**: Optimal frequency, duration, timing for pneumatic compression, infrared devices in real training?
5. **Supplement stacking**: Do athletes combine tart cherry + curcumin + omega-3? Synergistic or redundant?
6. **Recovery business models**: Cryotherapy studios, IV lounges, compression therapy centers - business viability and efficacy?

### What policy/regulatory angles need investigation?

1. **FDA regulation of recovery devices**: What claims can/can't manufacturers make? Regulatory oversight of NMES, PBM, pneumatic devices?
2. **Supplement regulation**: Are curcumin, tart cherry, omega-3 products accurately labeled? Third-party testing requirements?
3. **Insurance coverage**: Do insurance companies cover any recovery modalities for athletes? Medical necessity criteria?
4. **Banned substances concerns**: Any recovery supplements contain substances prohibited by WADA/USADA?
5. **Professional sports league policies**: Do NBA/NFL/FIFA have guidelines on recovery device usage? Any restrictions?

### What practitioner perspectives are missing?

1. **What are strength coaches and sports scientists saying on X/Twitter about these modalities NOW?**
2. **What are elite athletes posting about their recovery stacks on social media?**
3. **What do physical therapists recommend for 40-year-old recreational athletes vs 25-year-old professionals?**
4. **Regional differences**: Are European teams using different recovery approaches than American teams?
5. **What's being discussed in sports medicine conferences in 2024-2025?**
6. **Practitioner skepticism**: What do evidence-based practitioners warn against regarding recovery hype?

---

## Phase 3: Targeted Followup Research Prompts

**Goal**: Address gaps from Phase 2 analysis with targeted research using each tool's strengths.

### Phase 3A: Grok - Recent Developments & Practitioner Perspectives

**Created:** 2025-12-15

**Prompt (copy-paste ready):**

```
Research emerging recovery technologies and practitioner perspectives on athletic recovery, focusing on these specific questions:

**Recent Developments (last 12 months):**
- What new recovery devices or technologies launched in 2024-2025 (NMES, compression, infrared, wearables)?
- How are professional sports teams (NBA, NFL, Premier League, Olympics) adapting recovery protocols post-pandemic?
- What emerging recovery supplements or delivery mechanisms appeared recently (e.g., liposomal curcumin, new polyphenol sources)?
- Are there any AI-driven recovery personalization platforms using biomarkers to customize protocols?

**Practitioner Perspectives:**
- What are strength coaches, sports scientists, and physical therapists saying on X/Twitter about recovery modalities like NormaTec, Therabody, infrared devices, NMES?
- What recovery stacks are elite athletes posting about on social media in 2024-2025?
- What do evidence-based practitioners warn against regarding recovery device hype vs reality?
- How do practitioners approach recovery differently for 40-year-old recreational athletes vs 25-year-old professionals?

**Regional/Local Context:**
- Are European teams using different recovery approaches than American teams?
- What's being discussed at sports medicine conferences in 2024-2025?

Focus on: Recent news, industry discussions on X/Twitter, practitioner insights, regional sources from last 12 months.
Provide findings with source links, publication dates, and credibility indicators.
```

**Execution method:** Manual submission to https://x.com/i/grok

---

### Phase 3B: GPT-Researcher - Industry & Case Studies

**Created:** 2025-12-15

**Prompt (copy-paste ready):**

```
Research emerging recovery technologies and nutrition for athletic recovery, focusing on these specific questions:

**Industry Analysis & Cost-Benefit:**
- What is the cost-benefit analysis of premium recovery devices (NormaTec $1000+, Therabody JetBoots $2000+, HBOT $200/session, cryotherapy) versus simple interventions (cold showers, foam rollers, sleep optimization)?
- What is the business viability of recovery centers (cryotherapy studios, IV lounges, compression therapy centers)?
- How do supplement manufacturers market recovery products (tart cherry, curcumin, omega-3) and what are realistic ROI expectations?

**Case Studies & Implementation:**
- What specific recovery protocols are professional sports teams (NBA, NFL, Premier League, Olympic teams) actually using?
- Are there documented case studies of elite athletes or teams successfully implementing recovery technology stacks?
- How do athletes integrate multiple recovery modalities (e.g., tart cherry + curcumin + omega-3 supplement stacking - synergistic or redundant)?
- What are realistic compliance rates for interventions requiring high volume (e.g., 2940 mL tart cherry juice over 3 weeks)?

**Technical & Comparative Analysis:**
- How do wearable recovery tracking devices (HRV monitors, sleep trackers, readiness scores) integrate with recovery protocols?
- What optimal usage protocols exist for pneumatic compression, infrared devices, NMES in real training environments (frequency, duration, timing)?
- What evidence exists for individual response variability to recovery interventions - who responds vs who doesn't?

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis, practical implementation data.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

**Execution method:** GPT-Researcher skill (local multi-agent framework with OpenAI GPT-5.2)

---

### Phase 3C: Gemini Deep Research - Policy & Regulatory Context

**Created:** 2025-12-15

**Prompt (copy-paste ready):**

```
Research regulatory and policy frameworks for emerging recovery technologies and supplements, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- How does the FDA regulate recovery devices (NMES, photobiomodulation, pneumatic compression, infrared devices, HBOT)?
- What claims can/cannot manufacturers legally make for recovery devices?
- How are recovery supplements (curcumin, tart cherry, omega-3, bromelain) regulated for accurate labeling and third-party testing?
- What WADA/USADA policies exist regarding recovery supplements and banned substances concerns?

**Insurance & Medical Policy:**
- Do insurance companies cover any recovery modalities for athletes (HBOT, compression therapy, cryotherapy)?
- What are medical necessity criteria for coverage of recovery interventions?
- Are there any reimbursement codes for recovery therapies in athletic populations?

**Professional Sports League Policies:**
- Do NBA, NFL, FIFA, Olympic committees have official guidelines or restrictions on recovery device usage?
- What policies exist around recovery supplement use in professional sports?
- Are there competitive fairness considerations for expensive recovery technologies?

**Safety & Standards:**
- What safety standards exist for recovery devices (electrical stimulation, compression pressure limits, temperature controls)?
- Have there been any regulatory actions or warnings against specific recovery device manufacturers?
- What international standards (ISO, CE marking) apply to recovery technologies?

Focus on: Regulatory frameworks, legislation, government policy documents, professional sports league policies, safety standards, insurance policies.
Provide findings with official source citations, effective dates, and policy context.
```

**Execution method:** Gemini Deep Research API

---

### Phase 3D: Claude Deep Research - Comprehensive Synthesis

**Created:** 2025-12-15

**Prompt (copy-paste ready):**

```
Research emerging recovery technologies and advanced nutrition for athletic recovery, focusing on these complex multi-dimensional questions:

**Complex Questions Requiring Cross-Domain Synthesis:**

1. **Individual response variability paradox**: Why do some athletes respond dramatically to recovery interventions (e.g., tart cherry improving half-marathon time by 13%, NormaTec improving agility) while others show no benefit? What genetic, metabolic, or training status determinants explain this variability, and how can athletes predict whether they'll be responders?

2. **Acute biomarker vs performance outcome gap**: Many interventions reduce creatine kinase, lactate, and soreness but fail to improve actual performance in subsequent training or competition. What explains this disconnect? Are we measuring the wrong outcomes, or do acute recovery markers not translate to functional performance?

3. **Industry funding bias impact**: How do we practically separate legitimate scientific findings from industry-sponsored hype in recovery technology research? What framework can practitioners use to critically evaluate recovery device claims when much research is funded by manufacturers (Therabody, Compex, NormaTec)?

4. **Cost-effective recovery hierarchy for 40-year-old recreational athlete**: Given budget constraints, what is the evidence-based priority ranking of recovery investments? Is it sleep optimization > protein/carb timing > cold water > supplements > devices? How does this hierarchy change for elite vs recreational athletes?

5. **Sport-specific recovery protocol design**: How should recovery protocols differ for intermittent sports (basketball, soccer) vs endurance (marathon, cycling) vs strength (powerlifting, CrossFit)? What evidence exists for tailoring modalities to specific metabolic demands?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent practitioner sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations, industry funding, and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
- Synthesize findings to address each complex question with practical recommendations

**Output:** Comprehensive synthesis addressing each question with evidence from multiple domains (academic research, industry analysis, policy context, practitioner experience).
```

**Execution method:** Claude Deep Research (Chrome DevTools automation)

---

<!-- Additional results and analysis will be added as Phase 3 research completes -->
