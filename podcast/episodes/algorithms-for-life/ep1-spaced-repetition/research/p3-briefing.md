# Master Research Briefing: Spaced Repetition - The Algorithm That Optimizes Memory

**Date:** 2025-12-15
**For:** podcast-synthesis-writer agent
**Episode:** Algorithms for Life: Ep. 1, Spaced Repetition

---

## VERIFIED KEY FINDINGS

### 1. Neuroscience Foundations: Why Spacing Is Biologically Non-Negotiable

**Main finding:** Spaced repetition works through specific molecular mechanisms (CREB, MAPK) that cannot be activated by massed practice.

**Evidence:**
- **CREB as molecular switch:** In *Drosophila*, massed training (10 trials, no rest) produces 3-day memory; spaced training (10 trials, 15-min intervals) produces 7+ day memory. Genetic CREB overexpression makes massed training produce long-term memory, proving CREB is rate-limiting. — Source: Perplexity (neuroscience section), Claude (molecular switches) — Quality: Well-established fruit fly research
- **MAPK temporal window:** Four spaced 3-min depolarizations (10-min rest) evoke persistent MAPK; collapsing to one 12-min pulse fails. MAPK creates ~45-min window where second trial generates long-term memory. — Source: Perplexity, Claude — Quality: Cellular-level mechanism, well-characterized
- **Hippocampal-cortical transfer:** Fast-learning hippocampus stores temporarily, then transfers to slow-learning neocortex over days/weeks during sleep. Sharp-wave ripples compress/replay information for cortical consolidation. Cannot be rushed. — Source: Perplexity (fMRI study), Claude — Quality: Systems neuroscience, neuroimaging evidence
- **74% better retention:** Meta-analysis of 839 assessments from 317 experiments shows spaced > massed across all retention intervals (<1 min to 30+ days). — Source: Perplexity (Cepeda et al. 2008) — Quality: Meta-analysis, N=very large

**Contradictions/Nuances:**
- While mechanisms are clear at molecular level, translating optimal intervals to humans remains imprecise (see Algorithms section).

**Source quality notes:**
- Fruit fly research is well-established but extrapolation to human learning has some limitations.
- fMRI studies provide systems-level validation in humans.

---

### 2. Algorithms: From SM-2 to FSRS - Prediction vs. Actual Learning

**Main finding:** Modern algorithms (FSRS) predict forgetting better than SM-2, but marginal gains in real-world retention outcomes remain unproven.

**Evidence:**
- **SM-2 (1987) remains dominant:** Used by Anki, Mnemosyne. Adaptive matrices of optimal factors, item-specific ease factor. "Remarkably durable" after 38 years. — Source: Perplexity (algorithm history), GPT-Researcher (Anki ecosystem) — Quality: Historical foundation, widely deployed
- **FSRS achieves better prediction:** 21 trainable parameters, log loss 0.3460 vs 0.4694 for Duolingo's HLR across 727M reviews from ~10K Anki users. Power-law forgetting curves fit data better than exponential. — Source: Perplexity (FSRS section), Claude (algorithm comparison), Grok (FSRS-5 in 2025) — Quality: Large-scale benchmarking data
- **Prediction ≠ learning outcomes:** "No rigorous head-to-head trials have shown that more sophisticated algorithms produce meaningfully better real-world retention over months or years." — Source: Claude (critical gap section) — Quality: Evidence gap identified
- **Optimal interval principle:** For 1-week retention, optimal gaps are 20-40% of retention interval; for 1-year retention, 5-10%. Most commercial apps don't explicitly account for desired retention interval. — Source: Perplexity (Cepeda et al. 2008), Claude — Quality: Meta-analysis (N=1,350+), robust finding

**Contradictions/Nuances:**
- Expanding vs. fixed intervals show mixed results across studies - no clear winner. Meta-analysis shows expanding only ~3% better than fixed. — Source: Perplexity (meta-analytic evidence) — Quality: Modest effect size
- Any reasonable spaced algorithm massively outperforms massed practice; algorithmic sophistication shows diminishing returns.

**Source quality notes:**
- FSRS benchmarks based on Anki user data (self-selected population, may not generalize).
- Independent validation of SM-18 limited; mostly SuperMemo internal benchmarks.

---

### 3. SRS App Ecosystem: Design Philosophies & Trade-offs

**Main finding:** Fundamental tension between "learning-first" (Anki) and "engagement-first" (Duolingo, Memrise) design philosophies, with unclear winner for real-world effectiveness.

**Evidence:**
- **Anki: Maximalist customization:** User-owned memory system, toolkit not curriculum. Active add-on ecosystem (AnkiAIUtils, custom schedulers, templates). FSRS-5 introduced early 2025, predicted default by late 2025. — Source: GPT-Researcher (strong Anki forum evidence), Grok (2025 updates) — Quality: Direct community observation, high customization documented
- **Duolingo: Guided gamification:** 500M+ users, 103.6M monthly active, ~2% paid conversion. Launched AI Video Calls/Adventures (Sept 2024), PvP/LinkedIn (Sept 2025). 7-day streak users 3.6x more engaged. — Source: Claude (business model section), Grok (2024-2025 updates) — Quality: Company-reported metrics
- **Memrise: Fragmentation concerns:** "New experience" rollout July 2025 with immersive personalization; community courses relocated to dedicated site. Mixed sentiment (relief over preserved access but frustration with fragmentation). — Source: Grok (platform evolution) — Quality: Recent changes, user forum sentiment
- **Customization vs. guided spectrum:** Anki (very high customization, low guidance, high scheduling transparency) vs. Duolingo (low customization, very high guidance, low scheduling transparency). — Source: GPT-Researcher (comparative table) — Quality: Platform design analysis

**Contradictions/Nuances:**
- Education apps have **lowest user retention rates (1.76%)** of any mobile app category. — Source: Claude (dropout section) — Quality: App analytics industry data
- Only **0.1% of Duolingo users complete a course** despite high engagement. — Source: Claude — Quality: Striking completion vs. engagement disconnect
- 102 replies / 8,594 views for Memrise2Anki migration thread suggests meaningful user demand for cross-platform workflows. — Source: GPT-Researcher (Anki forums) — Quality: Migration signal, user pain point

**Source quality notes:**
- GPT-Researcher analysis heavily weighted toward Anki community; limited direct evidence for Duolingo/Memrise/Clozemaster/LingQ internals.
- Company-reported metrics (DAU, MAU, conversions) available but learning outcomes data sparse.

---

### 4. Business Models: Engagement Metrics vs. Learning Effectiveness

**Main finding:** Structural conflict between maximizing engagement (drives revenue) and maximizing learning (may require shorter, less frequent sessions).

**Evidence:**
- **Engagement imperative:** Duolingo 500M+ users but ~2% paid conversion; retention drives revenue through ads and subscriptions. DAU/MAU/streaks are core metrics. — Source: Claude (business model analysis) — Quality: Company economics
- **Streak psychology:** 7-day streak users 3.6x more engaged. Notifications optimized by multi-armed bandit algorithms for engagement, not learning. — Source: Claude, Grok (UX innovations) — Quality: A/B testing likely, company practice
- **Heart system monetization:** Purchase hearts or watch ads to continue practicing. Monetizes mistakes. — Source: Claude — Quality: Product design observation
- **"Mixed (sometimes negatively skewed) picture":** 2021 systematic review of Duolingo effectiveness: design decisions prioritize "competition over collaboration, repetition and translation over meaningful feedback and context, and passive receptive skills over active productive skills." — Source: Claude (Taylor & Francis review) — Quality: Peer-reviewed systematic review, critical assessment
- **"Very little conclusive evidence":** Eight years after research began on Duolingo, systematic review notes lack of effectiveness evidence despite scale. — Source: Claude — Quality: Evidence gap identified by academic review

**Contradictions/Nuances:**
- Engagement ≠ learning, but zero engagement also produces zero learning. Optimal balance unknown.
- Gamification maintains attention but "cannot compensate for" design limitations once novelty wears off.

**Source quality notes:**
- Systematic review provides independent assessment; industry research may have publication bias favoring positive findings.
- Actual proficiency outcome data (not flashcard retention) remains scarce across platforms.

---

### 5. The Recognition-Production Gap: Why Flashcard Users Can't Speak

**Main finding:** Most SRS focuses on paired-associate learning (flashcard format), which builds recognition but doesn't transfer to production (speaking/writing).

**Evidence:**
- **Meta-analysis confirms spacing works for vocabulary:** Kim & Webb 2022 (48 experiments, N=3,411) found large effect sizes (g=1.04–2.34) for spaced vocabulary practice. BUT authors note "majority of studies focus on paired-associate learning" measured in similar formats to training. — Source: Claude (recognition-production section) — Quality: Meta-analysis, N=large
- **Recognition precedes recall developmentally:** González-Fernández 2025 study (N=314 EFL learners) found recognition knowledge precedes recall knowledge across all vocabulary components in predictable sequence. — Source: Claude — Quality: Large study, recent
- **Distinct psychometric constructs:** Stewart et al. 2024 argue recall and recognition may be "distinct psychometric constructs" - different enough to be separate abilities. — Source: Claude — Quality: Recent theoretical argument
- **Vocabulary explains 32-84% of speaking variance BUT:** "Learners with large vocabulary sizes did not necessarily produce lexically sophisticated L2 words during speech." Recognition creates "illusion of knowledge that production exposes as shallow." — Source: Claude — Quality: Critical finding on transfer failure
- **Anecdotal "Anki problem":** Practitioners describe phenomenon of users with 20,000 reviewed cards who cannot hold basic conversations. — Source: Grok (practitioner perspectives), Claude (polyglot section) — Quality: Widespread anecdotal observation, not quantified

**Contradictions/Nuances:**
- Some polyglots (Gabriel Wyner) claim "master 3,600 terms with 90% accuracy" in 4 months using SRS-centered approach. Others (Steve Kaufmann) view SRS as optional. — Source: Claude (polyglot divergence) — Quality: Practitioner experience, not controlled trials

**Theoretical explanations:**
- **Proceduralization hasn't occurred:** DeKeyser's skill acquisition theory - declarative knowledge (SRS builds) must transform to proceduralized knowledge via production practice.
- **Transfer-appropriate processing:** Encoding and retrieval processes must match; flashcard recognition ≠ conversational production neural processes.
- **Context-dependent memory:** Godden & Baddeley's underwater study - words learned underwater recalled better underwater (24.9) than on land (17). Words learned in Anki interface may not transfer to real contexts.
- **No communicative pressure:** SRS lacks time constraints and message formulation demands of real conversation.

**Source quality notes:**
- Recognition-production gap is well-established in SLA literature.
- Quantified data on "how many Anki cards until conversational fluency" doesn't exist in controlled form.

---

### 6. Integration Strategies: How Successful Learners Use SRS

**Main finding:** Polyglots converge on SRS as supplement (10-30% of study time), never replacement for authentic interaction.

**Evidence:**
- **Polyglot consensus points:**
  - SRS is supplement, never replacement for authentic language interaction
  - Personal card creation substantially outperforms pre-made decks
  - Daily consistency matters more than session length
  - Excessive SRS leads to burnout, should be moderated
  — Source: Claude (polyglot section) — Quality: Expert practitioner convergence
- **Time allocation recommendations (practitioner wisdom, not controlled trials):**
  - Beginners: 30-40% of study time to SRS
  - Intermediates: 20-30%
  - Advanced: 10-15% or less
  — Source: Claude (Refold methodology) — Quality: Community-derived heuristics, not research-based
- **Steve Kaufmann (20+ languages):** "If you like doing flash cards... then it's worth doing. If not, this kind of learning activity won't help much." Prioritizes listening/reading. — Source: Claude, Grok — Quality: High-level practitioner testimony
- **Luca Lampariello (20 languages):** Uses SRS "only for a few specific needs," prefers repeated exposure in context. — Source: Claude — Quality: Expert practitioner testimony
- **Gabriel Wyner (Fluent Forever):** SRS as central, but emphasizes: learn pronunciation first, avoid translations, personally-created cards with multiple information chunks. — Source: Claude — Quality: SRS-maximalist approach, contrasts with Kaufmann/Lampariello

**Contradictions/Nuances:**
- No controlled trials on optimal time allocation percentages - all recommendations are practitioner wisdom.
- Extensive reading shows effect sizes (d=1.32 for vocabulary, meta-analysis N=1,268) comparable to SRS, suggesting reading could substitute or complement. — Source: Claude — Quality: Meta-analysis evidence

**Complementary model reconciliation:**
- "SRS builds the vocabulary floor needed to understand input, while comprehensible input provides rich contextualized exposure needed for true acquisition."
- Metaphor: "When you make a flashcard out of something, it's like you get a cup. As you interact with your target language, you fill that cup with water."
— Source: Claude (context-dependent learning section) — Quality: Theoretical reconciliation of Krashen vs. explicit learning

**Source quality notes:**
- Time allocation research is "frustratingly sparse" (direct quote from Claude synthesis).
- Polyglot testimonies valuable but represent survivorship bias (successful learners, not failed learners).

---

### 7. Context Solutions: Richer Card Design & Sentence Mining

**Main finding:** Several evidence-backed strategies address decontextualization, but require effort most users don't invest.

**Evidence:**
- **Sentence cards vs. word cards trade-off:**
  - Sentence cards teach vocabulary + grammar simultaneously, natural context. Antimoon recommends: "isolated word is abstract—hard to remember abstract things."
  - BUT anime cards (word highlighted in context) can be reviewed **2-4x faster** than full sentence cards.
  - Word cards remain effective for concrete nouns with strong imagery.
  — Source: Claude (context solutions) — Quality: Design trade-off analysis
- **Sentence mining:** Creating cards from authentic content creates contextual associations. "1T sentence" principle: only create cards from sentences where you understand everything except one target element. — Source: Claude, Grok (practitioner strategies) — Quality: Community best practice
- **Dual-coding (Paivio):** Activating both verbal and visual mental processes facilitates retention. Self-generated mnemonics outperform provided ones: "higher posttest performance." — Source: Claude — Quality: Cognitive psychology evidence
- **AI-generated flashcards (2024-2025):** GPT-4 superior to offline LLMs for math topics, but ethical concerns over AI reliance. NotebookLM used for grounded flashcards (Sept 2025 reviews). "53% of medical students would use ChatGPT to generate Anki cards if tutorials existed" (survey quoted on forums). — Source: Grok (AI integration), GPT-Researcher (adoption barrier = lack of tutorials) — Quality: Emerging trend, adoption gated by knowledge/tutorials not capability

**Contradictions/Nuances:**
- Richer card design addresses context problem but increases creation time, potentially reducing overall practice volume.
- Quality of AI-generated cards varies; risk of "bad habits if unchecked" (Reddit January 2025).

**Source quality notes:**
- Sentence mining and dual-coding have theoretical support but limited large-scale effectiveness trials.
- AI card generation is very recent (2023-2025); long-term effectiveness unknown.

---

### 8. The 140-Year Adoption Failure: Systemic Barriers

**Main finding:** Despite being "one of the most dependable phenomena in experimental psychology," spacing has not been systematically adopted in education.

**Evidence:**
- **Dempster 1988:** Identified that neither American classrooms nor textbooks implemented spaced reviews despite robust evidence. Soviet mathematics textbooks provided more distributed presentation than American equivalents. — Source: Claude (adoption failure section) — Quality: Historical analysis
- **Judgments-of-learning paradox:** Students prefer massed learning because cramming produces stronger immediate test performance. Spacing advantage only manifests after delays. Students show "clear preference for massed repetition when judging learning effectiveness, even when spaced practice produces better outcomes." Spaced items feel "more detached from short-term memory... less effective." — Source: Claude, Perplexity (metacognitive misalignment) — Quality: Well-documented metacognitive illusion
- **Systemic barriers identified:**
  - Curriculum design favoring immediate assessment
  - Textbooks organized into incompatible blocked chapters
  - Teachers comfortable with massed practice
  - Institutional inertia
  - "Beyond what any teacher or student can reasonably arrange" without technological support (Lindsey et al.)
  — Source: Claude (systemic dysfunction), Perplexity — Quality: Implementation science analysis

**Contradictions/Nuances:**
- 83% of participants rated massed practice as equally or more effective than spaced despite objective superiority of spacing. — Source: Perplexity — Quality: Striking metacognitive failure

**Source quality notes:**
- Adoption failure well-documented but solutions remain elusive.
- Technology (SRS apps) should solve "arrangement" problem but dropout rates remain high.

---

### 9. Dropout & Review Burden: The Practical Failure Mode

**Main finding:** Skipping days causes exponential review backlog growth, creating overwhelming pile that discourages return.

**Evidence:**
- **Exponential backlog growth:** Day 1 skip leaves 50 reviews, Day 2 = 120, Day 3 = 190, Day 4 = 280. "Most common mistake: learning too many new cards per day... leads to unmanageable reviews which takes away time from immersion and leads to burnout." — Source: Claude (review burden section) — Quality: SRS mechanics analysis
- **Education apps have lowest retention (1.76%)** of any mobile app category. — Source: Claude — Quality: App analytics industry benchmark
- **Only 0.1% of Duolingo users complete a course** despite high engagement. — Source: Claude — Quality: Striking completion failure
- **Immediate effort vs. delayed reward:** Cramming provides "more salient representation for immediate conscious recollection." Spaced practice benefits manifest only over weeks/months. Temporal disconnect makes SRS feel less effective than it is. — Source: Claude (psychological challenge) — Quality: Motivation/perception analysis
- **Successful calibration:** 10-20 new cards daily maximum, complete due reviews before adding new material, limit sessions to 15-30 minutes. Users who practice consistently for 3 months are **4x more likely to achieve language goals** - but reaching threshold requires surviving delayed-reward period. — Source: Claude — Quality: Best practice heuristics, 3-month threshold interesting

**Contradictions/Nuances:**
- Some platforms (Duolingo) maintain high engagement through streaks/gamification, but engagement ≠ completion or proficiency.
- "High dropout rates" widely mentioned in practitioner discussions but platform-level quantified data sparse.

**Source quality notes:**
- Review burden mechanics are well-understood theoretically.
- Actual dropout rates per platform not publicly reported by most companies.

---

### 10. Recent Developments (2024-2025): AI, Mobile UX, Algorithm Updates

**Main finding:** Innovation concentrated in (a) scheduler modernization (FSRS), (b) add-on ecosystems, (c) AI-assisted card generation. Adoption barriers often not capability but "tutorial availability, workflow friction, paywalls."

**Evidence:**
- **FSRS-5 (early 2025):** Advanced scheduling algorithm introduced to Anki, predicted default by late 2025. Community sentiment: positive for efficiency, minor complaints on lag. — Source: Grok (March 2025 forum discussions), GPT-Researcher — Quality: Active community adoption
- **Duolingo AI features (Sept 2024-Sept 2025):** AI Video Calls/Adventures (Sept 2024), PvP modes/LinkedIn integrations (Sept 2025), chess courses. — Source: Grok (company announcements) — Quality: Company-reported feature launches
- **AI flashcard generation:** GPT-4 outperforms offline LLMs for math cards. NotebookLM for grounded flashcards (Sept 2025). "53% of medical students would use ChatGPT to generate Anki cards if tutorials existed" — adoption gated by knowledge distribution, not AI capability. — Source: Grok (AI integration trends), GPT-Researcher (tutorial gap) — Quality: Survey quoted, tutorial barrier identified
- **Mobile UX: Microlearning & notifications:** Duolingo's streak mechanics and bite-sized lessons, enhanced notifications in 2025. Micro-interactions (progress animations) increase engagement by 30% (Nov 2025 reports). — Source: Grok (mobile innovations) — Quality: Industry UX trends
- **Newer entrants:** Taalhammer (AI-SRS integration, July 2025), Memozora (free flashcard maker, Oct 2025), NeuraCache (SRS + note-taking). "Second wave" prioritizing fun and integration over pure memorization. — Source: Grok (app ecosystem) — Quality: Emerging competitive landscape

**Contradictions/Nuances:**
- AI card generation quality varies; offline models lag GPT-4. "Risk of bad habits if unchecked."
- Mobile notifications optimized for engagement, not necessarily learning.

**Source quality notes:**
- 2024-2025 developments tracked via forum discussions, company announcements, Reddit/X sentiment.
- Long-term effectiveness of AI-generated cards unknown (too recent).

---

## RESEARCH GAPS & UNCERTAINTIES

**Well-established:**
- Spacing effect robustness (140+ years of research)
- Molecular mechanisms (CREB, MAPK, hippocampal-cortical transfer)
- Meta-analytic effect sizes (spacing >> massing)
- Recognition-production gap in SLA

**Preliminary/Limited evidence:**
- Optimal time allocation percentages (practitioner wisdom, not trials)
- FSRS prediction accuracy → actual learning outcomes (benchmarked prediction, not proficiency)
- AI-generated card effectiveness (too recent for long-term data)
- Platform-specific dropout rates (not publicly reported)

**Unknown/Unstudied:**
- Long-term retention beyond months/years (most studies measure days to months)
- Far transfer from flashcard mastery to real-world fluency (recognized problem, limited quantified data)
- Optimal SRS:immersion ratio for different proficiency levels (no controlled trials)
- Why mathematics shows smaller spacing effects than other domains (identified but unexplained)

---

## SOURCE INVENTORY

### Tier 1 Sources (Meta-analyses, Systematic Reviews)

1. **Cepeda et al. 2008** — Landmark meta-analysis of 317 experiments, 839 assessments, spacing effect across retention intervals — [URL in Perplexity references]
2. **Kim & Webb 2022** — Meta-analysis of 48 experiments (N=3,411) on spaced vocabulary practice — [URL in Claude references]
3. **Taylor & Francis 2021 systematic review** — Critical assessment of Duolingo effectiveness — [URL in Claude references]

### Tier 2 Sources (Large Studies, Company Research)

1. **González-Fernández 2025** — N=314 EFL learners, recognition-recall developmental sequence — [URL in Claude references]
2. **Stewart et al. 2024** — Theoretical argument on recall vs. recognition as distinct constructs — [URL in Claude references]
3. **Duolingo company metrics** — 500M+ users, 103.6M MAU, ~2% paid conversion, 7-day streak correlation — [URL in Claude references]
4. **FSRS benchmarks** — 727M reviews from ~10K Anki users, log loss comparisons — [URLs in Perplexity, Claude references]

### Tier 3 Sources (Community Forums, Practitioner Testimony)

1. **Anki Forums (forums.ankiweb.net)** — FSRS-5 discussions (March 2025), add-on ecosystem, migration threads — [URLs in GPT-Researcher, Grok]
2. **Reddit language learning communities** — Practitioner discussions (2024-2025) on SRS limitations, dropout, context problems — [URLs in Grok]
3. **X/Twitter language community** — Recent developments, polyglot perspectives, sentiment indicators — [URLs in Grok]
4. **Polyglot testimonies** — Steve Kaufmann, Luca Lampariello, Gabriel Wyner integration strategies — [URLs in Claude]

---

## NOTES FOR OPUS 4.5

**Strongest evidence for:**
- Neuroscience mechanisms (CREB, MAPK) - molecular level well-characterized
- Spacing effect robustness - meta-analytic consensus across 140 years
- Recognition-production gap - well-documented in SLA literature
- Metacognitive misalignment - replicated finding (users prefer massing despite spacing superiority)

**Weaker evidence for:**
- Algorithmic sophistication → learning outcomes (prediction accuracy benchmarked, not proficiency gains)
- Optimal time allocation ratios (practitioner heuristics, no controlled trials)
- Platform-specific dropout rates (widely discussed, not quantified publicly)
- AI-generated card long-term effectiveness (too recent for validation)

**Interesting tensions/contradictions:**
- **Engagement vs. learning:** Duolingo 103.6M MAU but 0.1% completion rate - high engagement, low completion
- **Algorithmic sophistication diminishing returns:** FSRS predicts better than SM-2, but ~3% marginal improvement over simpler algorithms
- **Polyglot divergence:** Some (Wyner) center SRS, others (Kaufmann) view as optional supplement
- **Adoption paradox:** 140 years of evidence, robust effect sizes, yet formal education has not systematically implemented spacing

**Missing context to acknowledge:**
- Long-term retention studies (years/decades) sparse - most studies measure days to months
- Real-world proficiency outcomes (conversation fluency) vs. flashcard performance gap not well-quantified
- Individual difference moderators (working memory, prior knowledge) identified but not incorporated into algorithms
- Transfer mechanisms from flashcard mastery to communicative competence under-researched

---

**Synthesis guidance:** The research reveals a paradox - spaced repetition has unambiguous molecular mechanisms and robust laboratory evidence, yet struggles with real-world implementation. Success requires integration into complete learning systems (SRS + immersion + production practice), but most users either over-rely on SRS alone or abandon it due to review burden. Business models may incentivize engagement over learning effectiveness. The recognition-production gap means flashcard mastery ≠ speaking fluency. Modern algorithmic improvements (FSRS) are impressive but marginal; the bigger challenges are metacognitive (spacing feels less effective), motivational (delayed rewards), and systemic (education hasn't adopted spacing despite 140 years of evidence).
