# Prompts Used for Episode: Cardiovascular Health, Episode 4: Supplementation

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

---

## Setup Phase

**Episode Details:**
- Date: 2025-11-21
- Slug: cardiovascular-health-episode-4-supplementation
- Title: Cardiovascular Health, Episode 4: Supplementation
- Series: Cardiovascular Optimization (Episode 4 of ongoing series)
- Previous episodes: Lifestyle factors (Ep 1), VO2 max training (Ep 2), HRV (Ep 3)

---

## Research Phase

### Research Prompt

**Tools Used:** Perplexity, ChatGPT, and other deep research tools

**Prompt:**
```
Research evidence-based supplements and medications for cardiovascular health optimization in a 40-year-old man, with focus on practical implementation, interactions, and timing.

SCOPE - Deep dive on:

- Cardiovascular medications (even if not currently taking):
  * Statins: mechanisms, timing, food/supplement interactions (grapefruit)
  * Aspirin: timing (bedtime vs morning), interactions with NSAIDs and supplements
  * When these might be appropriate (prevention thresholds)

- Evidence-based supplements with cardiovascular benefits:
  * Omega-3/Fish oil: dosing, EPA vs DHA, trial data, atrial fib risk
  * Coenzyme Q10: heart failure data, statin interactions, dosing
  * Magnesium: blood pressure effects, HRV benefits, forms and dosing
  * Vitamin D: cardiovascular evidence (or lack thereof)
  * B vitamins and homocysteine
  * Garlic, aged garlic extract
  * Plant sterols/stanols
  * Bergamot
  * Red yeast rice

- Supplements with LIMITED or NO evidence:
  * Antioxidant vitamins (C, E)
  * High-dose niacin
  * Resveratrol
  * Others that have failed trials

- Timing and interactions:
  * When to take supplements (with meals, morning vs evening)
  * Drug-supplement interactions (blood thinners + fish oil, etc.)
  * Supplement-supplement synergies
  * What to avoid

- Supplement quality and safety considerations

CONTEXT:
This is Episode 4 in a cardiovascular optimization series for a 40-year-old male demographic. Episodes 1-3 covered foundational lifestyle factors, VO2 max training, and HRV. This episode focuses specifically on supplements and medications, including interactions and optimal protocols.

RESEARCH METHODOLOGY:
- Prioritize peer-reviewed studies, meta-analyses, systematic reviews, and authoritative sources (cardiology societies, major trials)
- Distinguish between correlation and causation in findings - many supplement studies show associations without proving causal mechanisms
- Report effect sizes and practical significance, not just statistical significance - e.g., "3 mmHg blood pressure reduction" is more useful than "p<0.05"
- Note the study populations and whether findings generalize to healthy 40-year-old men vs. elderly populations with existing cardiovascular disease
- Compare individual studies against meta-analyses and systematic reviews - identify where single studies conflict with broader evidence
- Identify preliminary research vs. well-replicated findings - distinguish pilot studies from decades of consistent evidence
- Note funding sources and potential conflicts of interest when relevant - especially for supplement studies funded by manufacturers
- Include contradictory findings and areas of scientific uncertainty - where do major trials disagree? What remains unknown?
- Cite specific studies, researchers, and sources throughout - name the trials (REDUCE-IT, VITAL, etc.), not just "studies show"

EMPHASIS:
- Evidence quality: RCTs, meta-analyses, effect sizes with clinical significance
- Practical protocols: doses, timing, forms that were actually tested
- Safety and interactions: documented risks, not theoretical concerns
- Cost-benefit analysis: magnitude of benefit vs. cost/risk
- What works, what doesn't, what's uncertain

DE-EMPHASIZE/EXCLUDE:
- Performance supplements (creatine, beta-alanine, caffeine - Episode 2 covered)
- Beetroot/nitrates for VO2 max (Episode 2 covered)
- General lifestyle factors (sleep, exercise, diet - Episode 1 covered)
- HRV tracking and interpretation (Episode 3 covered)

OUTPUT: Comprehensive supplementation guide with extensive citations, dosing protocols, and interaction warnings (~18-22KB target).
```

**Date:** 2025-11-20

**Research Results:**
- Perplexity research: 65KB comprehensive report saved to `research/perplexity-research.md`
- ChatGPT research: 107KB comprehensive report saved to `research/chatgpt-research.md`
- Both sources cover cardiovascular medications, evidence-based supplements, failed supplements, timing/interactions, and quality considerations
- Total research content: ~172KB

---

## Audio Generation Phase

### NotebookLM Audio Overview Prompt

**Tool Used:** NotebookLM

**Format:** Deep Dive / Long

**Files Uploaded to NotebookLM:**
- report.md
- research/perplexity-research.md
- research/chatgpt-research.md

**Prompt:**
```
Create an intellectually rigorous podcast that balances analytical depth with clear explanation.

Core principles:
• ALWAYS spell out acronyms before using them - "Eicosapentaenoic acid, or EPA" not just "EPA"
• Define technical terms immediately with plain language THEN build on them - assume intelligent but not expert audience
• Use concrete examples and stories ONLY when they exist in the source material - never fabricate or speculate
• When stories exist, include human elements: what people said, felt, decided - not just mechanics
• HIGHLIGHT surprising findings, spectacular failures, and unexpected successes - these are the memorable moments
• Extract frameworks and principles from the research findings
• Connect findings to practical implications and broader patterns
• Maintain scientific rigor: distinguish correlation from causation, note effect sizes, acknowledge uncertainties

[Full prompt used - see episode skill file for complete template]
```

**Date:** 2025-11-21

**Audio Generated:**
- Original file: Heart_Supplements.m4a
- Duration: 37:38.98
- Converted to: 2025-11-21-cardiovascular-health-episode-4-supplementation.mp3
- File size: 36,144,828 bytes (34.5 MB)
- Bitrate: 128 kbps

---

## Chapter Generation Phase

### Chapter Analysis Prompt

**Tool Used:** Claude AI Assistant / Whisper Transcript Analysis

**Prompt:**
```
Analyze the full Whisper transcript (2025-11-21-cardiovascular-health-episode-4-supplementation_transcript.json)
to identify natural topic transitions and create 10-15 chapter markers for the 37:39 episode.

Create chapters that:
- Are 2-4 minutes each
- Have descriptive titles capturing key topics
- Cover major subjects: statins, aspirin, omega-3, CoQ10, magnesium, garlic, plant sterols,
  vitamin D, B vitamins, failed supplements, red yeast rice, supplement quality/timing
```

**Output:** 12 chapters created covering all major topics

**Chapter Structure:**
1. 0:00 - Introduction: Evidence-Based Optimization Tools
2. 1:50 - Statins: The Gold Standard for LDL Reduction
3. 7:50 - Statin Timing and Grapefruit Interactions
4. 9:32 - Aspirin: The Great Reversal in Prevention
5. 11:41 - Aspirin Timing and Ibuprofen Conflicts
6. 14:04 - Omega-3 EPA: Success, Failure, and AFib Risk
7. 17:27 - CoQ10: From Muscle Pain to Heart Failure
8. 20:33 - Magnesium and Aged Garlic for Blood Pressure
9. 23:34 - Red Yeast Rice, Plant Sterols, and Bergamot
10. 27:51 - Failed Supplements: Niacin, Antioxidants, Vitamin D
11. 31:37 - Building Your Optimal Daily Protocol
12. 35:06 - Quality Assurance and Lifestyle Integration

**Date:** 2025-11-21

**Chapters Embedded:** Successfully embedded into mp3 file using FFmpeg

---

## Publishing Phase

### Episode Description Generation

**Tool Used:** Claude AI Assistant / Web Search for source validation

**Episode Description:**
```
Evidence-based guide to cardiovascular supplements and medications for 40-year-old men, covering what works, what fails spectacularly, and optimal dosing protocols. Learn why high-dose omega-3 reduces heart attacks by 25% but increases atrial fibrillation risk by 50%, how CoQ10 cut heart failure mortality by 49% in the Q-SYMBIO trial, and why vitamin D and niacin failed despite decades of hype.
```

**Keywords:** omega-3, EPA, DHA, statins, aspirin, CoQ10, magnesium, vitamin D, plant sterols, aged garlic extract, red yeast rice, supplement timing, drug interactions, cardiovascular health, heart disease prevention

**Sources Validated:**
1. REDUCE-IT Trial (omega-3 EPA) - https://www.ahajournals.org/doi/10.1161/JAHA.119.013543 - WebSearch + validation
2. Q-SYMBIO Trial (CoQ10 & heart failure) - https://www.ahajournals.org/doi/10.1161/circheartfailure.115.002639 - WebSearch + validation
3. VITAL Trial (vitamin D & omega-3) - https://prevmed.bwh.harvard.edu/vital/ - WebSearch + validation
4. USPSTF Aspirin Guidelines (2022) - https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/aspirin-to-prevent-cardiovascular-disease-preventive-medication - WebSearch + validation
5. JUPITER Trial (statin primary prevention) - https://www.nejm.org/doi/full/10.1056/NEJMoa0807646 - WebSearch + validation

**Date:** 2025-11-21

### Feed.xml Update

**Episode Metadata:**
- Title: Cardiovascular Health, Episode 4: Supplementation
- Duration: 37:39
- File size: 36,144,828 bytes
- Pub date: Thu, 21 Nov 2025 12:00:00 GMT
- Episode number: 6 (overall), Episode 4 (cardiovascular series)

**Date:** 2025-11-21

---

## Git Workflow

### Commit Details

**Files Committed:**
- prompts.md - Complete workflow documentation
- report.md - Research overview/summary
- research/perplexity-research.md - 65KB comprehensive report
- research/chatgpt-research.md - 107KB comprehensive report
- research/sources.md - Source organization template
- episode-description.md - Episode description with validated sources
- 2025-11-21-cardiovascular-health-episode-4-supplementation.mp3 - Final audio (36.1 MB)
- 2025-11-21-cardiovascular-health-episode-4-supplementation_transcript.json - Whisper transcript
- 2025-11-21-cardiovascular-health-episode-4-supplementation_chapters.txt - FFmpeg format chapters
- 2025-11-21-cardiovascular-health-episode-4-supplementation_chapters.json - Podcasting 2.0 format
- Updated podcast/feed.xml
- Updated .claude/skills/new-podcast-episode.md

**Commit Message:**
```
feat: Add episode on cardiovascular supplementation

- Add episode "Cardiovascular Health, Episode 4: Supplementation" covering evidence-based supplements and medications
- Include comprehensive research report (172KB across Perplexity and ChatGPT sources)
- Generate full transcript using local Whisper (base model)
- Create 12 chapter markers covering statins, aspirin, omega-3, CoQ10, magnesium, failed supplements
- Embed chapters into mp3 for podcast app support
- Update feed.xml with episode metadata and validated source links
- Episode duration: 37:39, covers REDUCE-IT, Q-SYMBIO, VITAL, JUPITER trials
- Update skill file to document NotebookLM workflow with all research files
```

**Git Operations:**
```bash
git add podcast/feed.xml podcast/episodes/2025-11-21-cardiovascular-health-episode-4-supplementation/ .claude/skills/new-podcast-episode.md
git commit -m "..."
git push
```

**Date:** 2025-11-21

**Result:** Successfully pushed to main branch. GitHub Pages will deploy in 2-3 minutes.

---

## Episode Complete

**Feed URL:** https://yudame.github.io/research/podcast/feed.xml
**Episode URL:** https://yudame.github.io/research/podcast/episodes/2025-11-21-cardiovascular-health-episode-4-supplementation/2025-11-21-cardiovascular-health-episode-4-supplementation.mp3
**Report URL:** https://yudame.github.io/research/podcast/episodes/2025-11-21-cardiovascular-health-episode-4-supplementation/report.md
