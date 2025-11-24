# Prompts Used for Episode: Cardiovascular Health Episode 2, VO2 Max.

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

---

## Setup Phase

**Episode Details:**
- Date: 2025-11-21
- Slug: cardiovascular-health-episode-2-vo2-max
- Title: Cardiovascular Health Episode 2, VO2 Max.

---

## Research Phase

### Research Prompt

**Tools Used:** ChatGPT and Perplexity (research outputs saved in research/ directory)

**Prompt:**
```
Research evidence-based strategies to maximize VO2 max in a 40-year-old man with ~10 hours/week available for training.

**SCOPE - Deep dive on:**
- What VO2 max is, how it's measured, why it's the strongest predictor of longevity
- Training protocols: HIIT vs steady-state, polarized training, periodization
- Optimal training frequency, intensity, duration, and progression
- Exercise modalities (running, cycling, rowing, swimming) and their effects
- Detraining and maintenance considerations
- Nutrition FOR PERFORMANCE: carbohydrate timing, fueling workouts, recovery nutrition
- Supplements with evidence for improving VO2 max or endurance performance:
  * Beetroot juice/dietary nitrates
  * Creatine (for high-intensity intervals)
  * Beta-alanine
  * Caffeine as ergogenic aid
- Recovery strategies specific to VO2 max improvement
- Testing and tracking VO2 max over time
- Age-related considerations (maintaining VO2 max in 40s, 50s+)

**EMPHASIS:**
- Actionable training protocols and sample programs
- Research on what training variables matter most
- Practical implementation for busy person
- Performance optimization
- Effect sizes of different training approaches

**DE-EMPHASIZE/EXCLUDE:**
- General health benefits of exercise (covered in Episode 1)
- HRV as a metric (only mention in context of training readiness/recovery)
- Heart disease prevention (mention briefly, but Episode 1 covered)
- Supplements for general heart health (omega-3, CoQ10, magnesium - Episode 4)
- Detailed nutrition patterns (Mediterranean diet, etc. - Episode 1 covered)

**CONTEXT TO PROVIDE:**
This is Episode 2 in a series. Episode 1 covered foundational lifestyle factors and cardiovascular health. This episode focuses specifically on VO2 max optimization through training and performance nutrition.

**Research methodology:**
- Prioritize peer-reviewed studies, meta-analyses, and authoritative sources
- Distinguish between correlation and causation in findings
- Report effect sizes and practical significance, not just statistical significance
- Note the study populations and whether findings generalize to 40-year-old men
- Compare individual studies against meta-analyses and systematic reviews
- Identify preliminary research vs. well-replicated findings
- Note funding sources and potential conflicts of interest when relevant
- Include contradictory findings and areas of scientific uncertainty
- Cite specific studies, researchers, and sources throughout

**OUTPUT:** Deep-dive research report with extensive citations, training protocols, and performance recommendations (~18-22KB target)
```

**Date:** 2025-11-20

---

## Audio Generation Phase

### NotebookLM Audio Overview Prompt

**Tool Used:** NotebookLM

**Format:** Deep Dive / Long

**Prompt:**
```
Combine vivid storytelling with rigorous analysis - tell compelling stories AND extract the frameworks.

What to emphasize:
• Specific stories with concrete details - the decisions people made, what happened, and why
• Pattern recognition across stories - identify the underlying frameworks and principles
• Both micro (individual decisions) and macro (systemic dynamics) perspectives
• Technical depth where relevant - don't simplify for simplicity's sake
• Counter-intuitive insights and non-obvious connections between events

Target audience: High-IQ protocol builders, founders, investors, and researchers who want both narrative understanding and analytical frameworks.

Tone: Intellectually rigorous but engaging. Use stories to illustrate concepts, then zoom out to extract the patterns. Make it vivid enough to remember the examples, and analytical enough to understand the principles. Think "This happened to Terra/Do Kwon in 2020, which illustrates a broader principle about algorithmic stability..."

Balance the concrete and the abstract - neither dumbed down nor dry.
```

**Date:** 2025-11-20

---

## Audio Processing Phase

### Transcription

**Tool Used:** Local Whisper (base model)
**Input:** 2025-11-21-cardiovascular-health-episode-2-vo2-max.mp3 (36:13, 128kbps)
**Output:** 2025-11-21-cardiovascular-health-episode-2-vo2-max_transcript.json
**Date:** 2025-11-20

### Chapter Generation

**Tool Used:** Claude / AI Assistant

**Approach:** Analyzed full transcript to identify 15 natural topic transitions

**Chapters Created:**
1. Introduction & The Longevity Link (00:00)
2. Understanding the Fick Equation (03:00)
3. Longevity Data & Mortality Risk (05:30)
4. Measurement & Testing Protocols (08:40)
5. The Polarized Training Framework (11:30)
6. The Gray Zone Problem (14:00)
7. High-Intensity Interval Training Design (16:10)
8. Volume & Expected Gains (18:00)
9. Weekly Training Structure (7-Day Blueprint) (19:40)
10. Modality Selection & Injury Prevention (23:10)
11. Recovery & Sleep Protocols (25:40)
12. Nutrition & Fueling Strategy (27:20)
13. Detraining & Maintenance (29:10)
14. Supplements for Marginal Gains (31:00)
15. Testing, Tracking & Long-Term Strategy (32:50)

**Output:**
- FFmpeg format: 2025-11-21-cardiovascular-health-episode-2-vo2-max_chapters.txt
- Podcasting 2.0: 2025-11-21-cardiovascular-health-episode-2-vo2-max_chapters.json

**Date:** 2025-11-20

---

<!-- Additional prompts will be added below as we progress through the workflow -->
