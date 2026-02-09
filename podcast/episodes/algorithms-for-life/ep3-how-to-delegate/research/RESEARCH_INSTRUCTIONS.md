# Manual Research Instructions

Perplexity Deep Research has been completed automatically. The following research prompts need to be submitted manually to their respective tools.

## ✅ COMPLETED: Perplexity Deep Research
**Status:** Complete - results saved to `p2-perplexity.md`

---

## 🔄 MANUAL SUBMISSION REQUIRED

### 1. Grok (via X.com)

**Where to submit:** https://x.com/i/grok

**Prompt to copy:**
```
Research the "Founder Mode" delegation debate sparked by Paul Graham and Brian Chesky in 2024. What does Chesky's Airbnb case study reveal about when conventional delegation advice fails? Include specific organizational changes he made (eliminating divisions, skip-level meetings, product involvement) and performance outcomes. Also investigate current AI delegation trends: what percentage of routine tasks are being delegated to AI vs. humans, what are AI delegation failure rates (McKinsey/Gartner data), and how does $20-200/month AI cost compare to $2,000-5,000/month human cost for delegatable tasks? Include real-world examples of successful and failed AI delegation.
```

**Save results to:** `research/p2-grok.md`

**Estimated time:** 5-10 minutes

---

### 2. ChatGPT Deep Research (via ChatGPT interface)

**Where to submit:** https://chatgpt.com (use Deep Research mode if available, or standard GPT-4)

**Prompt to copy:**
```
Synthesize research on psychological barriers to delegation and evidence-based solutions. Cover: (1) perfectionism, identity attachment, and control psychology - what organizational psychology research says about why leaders resist delegating; (2) the "feedback addiction" phenomenon where founders stay in operational details for dopamine hits rather than strategic necessity; (3) opportunity cost calculations - frameworks for quantifying the cost of not delegating (e.g., $500/hour founder time on $50/hour tasks); (4) hiring for coachability and learning agility - what interview questions or assessment methods predict delegation success, including behavioral interviewing research. Integrate psychological theory with practical frameworks.
```

**Save results to:** `research/p2-chatgpt.md`

**Estimated time:** 10-20 minutes (if using Deep Research mode)

---

### 3. Gemini Deep Research (via Google AI Studio)

**Where to submit:** https://aistudio.google.com or https://gemini.google.com

**Prompt to copy:**
```
Research evidence-based delegation frameworks and decision systems. Focus on: (1) RACI matrix effectiveness - empirical studies on decision authority boundaries and delegation success; (2) knowledge transfer protocols for expertise that can't be documented, including time requirements (9-12 week programs vs. shorter approaches); (3) decision boundary frameworks with specific thresholds (e.g., spending authority limits: <$5K independent, $5K-25K consult, >$25K approval required); (4) remote/hybrid work impact on delegation effectiveness - what research shows about supervision, autonomy, and knowledge transfer in distributed teams; (5) organizational growth correlations with delegation effectiveness (e.g., claims that mastering delegation leads to 112% higher growth rates). Include specific protocols, timelines, and quantitative data.
```

**Save results to:** `research/p2-gemini.md`

**Estimated time:** 3-10 minutes (if using Gemini 2.0 Deep Research)

**Note:** Gemini API automation is available but requires GOOGLE_AI_API_KEY in `/Users/valorengels/.env`. To set up:
```bash
echo 'GOOGLE_AI_API_KEY=your-key-here' >> /Users/valorengels/.env
```
Get API key from: https://aistudio.google.com/apikey

---

### 4. Claude (via claude.ai)

**Where to submit:** https://claude.ai

**Prompt to copy:**
```
Critically analyze delegation research and common frameworks. Identify: (1) empirical gaps - which widely-cited delegation rules lack research backing (e.g., the "70% rule," "delegate everything except X"); (2) contradictory findings - where does research on delegation vs. founder involvement conflict (compare Founder Mode narrative vs. traditional delegation advice); (3) generalizability issues - what populations were studied and what contexts might not transfer (startups vs. established firms, US vs. international, tech vs. other industries); (4) causation vs. correlation problems in delegation research - what's actually causal vs. selection effects; (5) practical applicability - which frameworks have implementation research vs. just conceptual models. Emphasize methodological rigor, effect size interpretation, and research limitations.
```

**Save results to:** `research/p2-claude.md`

**Estimated time:** 3-5 minutes

---

## Instructions for Saving Results

1. **Copy the full output** from each research tool
2. **Create a new file** in the `research/` directory with the naming pattern `p2-[tool].md`
3. **Paste the raw output** - don't edit or summarize yet
4. **Add a header** at the top of each file:
   ```markdown
   # Research Results: [Tool Name]

   **Date:** YYYY-MM-DD
   **Prompt:** [Copy the prompt used]

   ---

   [Paste research output here]
   ```

## Next Steps After Collection

Once all 5 research results are collected (Perplexity ✅ + Grok + ChatGPT + Gemini + Claude):

1. **Cross-validate findings** - identify consensus, contradictions, and gaps
2. **Create master briefing** (`p3-briefing.md`) - synthesize all sources by topic
3. **Extract validated sources** - create `sources.md` with working links
4. **Generate narrative report** - use Opus 4.5 for synthesis into `report.md`

## Quality Checklist

Before proceeding to cross-validation, verify each research result includes:

- [ ] **Specific citations** - Not just "research shows" but "Smith et al. 2023 found..."
- [ ] **Quantitative data** - Effect sizes, correlations, percentages, sample sizes
- [ ] **Contradictory evidence** - Not just supporting evidence
- [ ] **Study limitations** - Generalizability, methodological concerns
- [ ] **Source links** - URLs or DOIs for further investigation
- [ ] **Recent research** - Include 2020-2025 studies where relevant

## Estimated Total Time

- Perplexity: ✅ Complete (~2 minutes)
- Grok: ~5-10 minutes
- ChatGPT: ~10-20 minutes
- Gemini: ~3-10 minutes
- Claude: ~3-5 minutes

**Total:** ~25-50 minutes for manual collection
