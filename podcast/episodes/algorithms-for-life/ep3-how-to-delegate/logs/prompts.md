# Research Prompts: How to Delegate

## Perplexity Deep Research (Academic Focus)
**Optimized for:** Academic papers, meta-analyses, systematic reviews
**Prompt:**
```
I need a comprehensive academic research synthesis on delegation effectiveness in organizations. Focus on: (1) meta-analyses of learning agility vs. IQ/experience in predicting delegation success, including De Meuse et al. and similar large-scale studies; (2) empirical validation (or lack thereof) of the "70% delegation rule" attributed to Jim Schleckser; (3) new hire failure rates and root causes from organizational psychology research, particularly attitudinal vs. technical failures; (4) knowledge transfer effectiveness for tacit vs. explicit knowledge, including OPPTY or similar frameworks; (5) situational leadership model validation (Blanchard's D1-D4/S1-S4 matching). Prioritize peer-reviewed sources, report effect sizes and correlations, distinguish correlation from causation, and note contradictory findings.
```

## Grok (Real-time Trends + Business Context)
**Optimized for:** Current debates, business cases, founder perspectives
**Prompt:**
```
Research the "Founder Mode" delegation debate sparked by Paul Graham and Brian Chesky in 2024. What does Chesky's Airbnb case study reveal about when conventional delegation advice fails? Include specific organizational changes he made (eliminating divisions, skip-level meetings, product involvement) and performance outcomes. Also investigate current AI delegation trends: what percentage of routine tasks are being delegated to AI vs. humans, what are AI delegation failure rates (McKinsey/Gartner data), and how does $20-200/month AI cost compare to $2,000-5,000/month human cost for delegatable tasks? Include real-world examples of successful and failed AI delegation.
```

## ChatGPT Deep Research (Synthesis + Psychology)
**Optimized for:** Cross-domain synthesis, psychological frameworks, practical integration
**Prompt:**
```
Synthesize research on psychological barriers to delegation and evidence-based solutions. Cover: (1) perfectionism, identity attachment, and control psychology - what organizational psychology research says about why leaders resist delegating; (2) the "feedback addiction" phenomenon where founders stay in operational details for dopamine hits rather than strategic necessity; (3) opportunity cost calculations - frameworks for quantifying the cost of not delegating (e.g., $500/hour founder time on $50/hour tasks); (4) hiring for coachability and learning agility - what interview questions or assessment methods predict delegation success, including behavioral interviewing research. Integrate psychological theory with practical frameworks.
```

## Gemini Deep Research (Systems + Frameworks)
**Optimized for:** Structured frameworks, decision systems, organizational design
**Prompt:**
```
Research evidence-based delegation frameworks and decision systems. Focus on: (1) RACI matrix effectiveness - empirical studies on decision authority boundaries and delegation success; (2) knowledge transfer protocols for expertise that can't be documented, including time requirements (9-12 week programs vs. shorter approaches); (3) decision boundary frameworks with specific thresholds (e.g., spending authority limits: <$5K independent, $5K-25K consult, >$25K approval required); (4) remote/hybrid work impact on delegation effectiveness - what research shows about supervision, autonomy, and knowledge transfer in distributed teams; (5) organizational growth correlations with delegation effectiveness (e.g., claims that mastering delegation leads to 112% higher growth rates). Include specific protocols, timelines, and quantitative data.
```

## Claude (Critical Analysis + Contradictions)
**Optimized for:** Identifying gaps, contradictions, methodological critique
**Prompt:**
```
Critically analyze delegation research and common frameworks. Identify: (1) empirical gaps - which widely-cited delegation rules lack research backing (e.g., the "70% rule," "delegate everything except X"); (2) contradictory findings - where does research on delegation vs. founder involvement conflict (compare Founder Mode narrative vs. traditional delegation advice); (3) generalizability issues - what populations were studied and what contexts might not transfer (startups vs. established firms, US vs. international, tech vs. other industries); (4) causation vs. correlation problems in delegation research - what's actually causal vs. selection effects; (5) practical applicability - which frameworks have implementation research vs. just conceptual models. Emphasize methodological rigor, effect size interpretation, and research limitations.
```

---

## Execution Strategy

### Phase 2A: Submit Prompts (Parallel)
1. **Perplexity**: Use `/perplexity-deep-research` skill for automated API submission
2. **Grok**: Manual submission via X.com interface
3. **ChatGPT**: Manual submission via ChatGPT interface
4. **Gemini**: Use `/gemini-deep-research` skill for automated API submission
5. **Claude**: Manual submission via claude.ai

### Phase 2B: Collection Timeline
- Perplexity: ~2-3 minutes (API)
- Gemini: ~3-10 minutes (API)
- Grok: ~5-10 minutes (manual)
- ChatGPT: ~10-20 minutes (manual)
- Claude: ~3-5 minutes (manual)

### Phase 2C: Quality Checks
- [ ] Each result includes specific citations
- [ ] Quantitative data present (effect sizes, correlations, percentages)
- [ ] Contradictions or limitations noted
- [ ] Sources are accessible and credible
- [ ] Coverage across all research objectives from p1-brief.md

---

## Key Differences by Tool

| Tool | Strength | Focus Area |
|------|----------|------------|
| Perplexity | Academic rigor | Meta-analyses, empirical validation |
| Grok | Current trends | Founder Mode debate, AI delegation |
| ChatGPT | Synthesis | Psychology + practical integration |
| Gemini | Frameworks | Systems, protocols, structured approaches |
| Claude | Critical lens | Gaps, contradictions, methodological critique |

## Counterpoint Opportunities Identified

Based on research focus, plan to create dialogue tension around:
1. **Founder Mode vs. Traditional Delegation** - Chesky success vs. research on delegation
2. **70% Rule** - Widely cited but empirically untested
3. **AI Delegation** - Promise vs. 40%+ failure rates
4. **Learning Agility vs. Experience** - Counterintuitive hiring priorities

---

## Phase 8: Content Planning (Episode Planner Skill v3.0)

**Date:** 2026-02-09
**Skill used:** `.claude/skills/podcast-episode-planner/SKILL.md`
**Template used:** `docs/templates/content_plan-enhanced.md` (Wave 2-5 enhanced)

### Classification Decisions
- **Evidence Status:** Mixed -- learning agility and empowerment meta-analyses are strong; no named delegation framework has been RCT-tested; cross-cultural reversal well-replicated
- **Content Density:** Complex -- 4+ interlocking frameworks requiring integration
- **Series Position:** Middle (Ep. 3 of ongoing series; builds on Ep. 2 strategic selection)

### Toolkit Selections
- **Hook Type:** Surprising Statistic -- "82% saw the warning signs" + "89% of failures were attitudinal, not technical"
- **Takeaway Structure:** Conditional Protocol -- context (culture, stakes, skill level) determines best delegation approach; 5 protocols with different applicability conditions
- **Contradiction Handling:** Substantive conflict -- Founder Mode vs. empowerment evidence, Western vs. cross-cultural, autonomy helps vs. autonomy hurts

### Counterpoint Moments Designed
1. **70% Rule** (~12-14 min): Practitioner resonance vs. evidence hierarchy
2. **Founder Mode** (~15-18 min): Chesky results vs. survivorship bias + Wasserman data
3. **Cross-Cultural Reversal** (~22-25 min): Western empowerment bias vs. high power-distance evidence

### Quality Gate Status
- [x] Three sections with clear focus (Foundation/Evidence/Application)
- [x] Maximum 3-4 major concepts per section
- [x] All key terms listed with definitions (8 terms)
- [x] Protocols include specific parameters (5 protocols with timelines, percentages, frameworks)
- [x] Opening hook connects to closing callback (82% stat -> "knowing what to hold on to")
- [x] Episode answers its stated core question ("What actually works in delegation?")

### Output
- `content_plan.md` created (Wave 2-5 enhanced format)
- Sections: Episode Classification, Structural Design, NotebookLM Guidance
- Duration target: 34-42 minutes
- Studies emphasized: 7 primary studies with sample sizes
- Stories selected: 5 narrative elements with timing
