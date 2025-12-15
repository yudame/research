# Why the Most Proven Learning Technique in Psychology Has a 99.9% Failure Rate

You can watch a fruit fly develop a seven-day memory instead of a three-day memory just by inserting fifteen-minute rest periods between training trials. You can measure the molecular switch that makes it happen. After 140 years of research across thousands of studies, the evidence for spaced repetition is so overwhelming that scientists call it "one of the most robust phenomena in experimental psychology." And yet, only 0.1% of Duolingo's 500 million users complete a course. Education apps have the lowest retention rates of any mobile app category. Formal schooling has largely ignored these findings for over a century.

This is the paradox at the heart of spaced repetition: a learning technique with unambiguous molecular mechanisms and laboratory-proven effectiveness that collapses when it meets real human behavior. The story of why this happens---and what it reveals about memory, motivation, and the business of learning---is far more interesting than another article about flashcard apps.

## The Molecular Non-Negotiable: Why Your Brain Cannot Cram

The biological case for spacing rests on discoveries that read like a molecular thriller. Inside neurons, a protein called CREB (cAMP response element-binding protein) functions as a molecular switch determining whether learning produces lasting memory or temporary recall (BrainFacts, 2021). In landmark experiments with Drosophila fruit flies, researchers delivered identical training---ten odor-shock pairings---under two different schedules. When trials came in rapid succession, flies avoided the odor for about three days. When the same ten trials included fifteen-minute rest intervals, flies remembered for seven days or more. In a creature whose entire lifespan is approximately fifty days, that difference represents a substantial portion of their lives.

The critical insight came when researchers genetically manipulated CREB levels. Overexpressing CREB in fruit flies suddenly made massed training produce long-term memory---proving that CREB activation is the rate-limiting step that spacing overcomes (PMC, 2016). Your neurons require time between learning events to run the molecular machinery of consolidation. This is not a pedagogical preference but a biological constraint.

A second molecular system provides the timing mechanism. MAPK (mitogen-activated protein kinase) activation peaks approximately 45 minutes after a learning trial, creating a temporal window during which a subsequent trial can reinforce the first (PMC, 2016). Four spaced three-minute stimulations with ten-minute rest periods evoke persistent MAPK activation; collapsing these into one twelve-minute pulse fails to produce the same effect. The brain has a molecular clock for optimal learning, and cramming ignores it.

At the systems level, the hippocampal-cortical transfer model explains why spacing intervals should expand over days and weeks. The fast-learning hippocampus temporarily stores new memories, then gradually transfers them to the slow-learning neocortex during sleep through sharp-wave ripples that compress and replay information (Nature, 2025; Perplexity neuroscience section). This transfer cannot be rushed. A 2025 fMRI study found that spaced learning induced higher neural pattern similarity in default mode network subsystems compared to massed learning, with this similarity predicting which memories would persist to a one-month delay (Nature Communications Biology, 2025).

## The Effect Size That Should Have Changed Everything

The landmark Cepeda et al. meta-analysis of 2006 and 2008 examined 839 assessments across 317 experiments spanning decades of research. The findings were unequivocal: spaced presentations led to markedly better retention than massed presentations whether the retention interval was less than one minute or exceeded thirty days (Cepeda et al., 2006). Across all 271 studies examined, only 12 comparisons (4.4%) failed to show spacing advantages. The meta-analysis established that spacing produces approximately 74% better retention compared to cramming.

But the research revealed something more nuanced: optimal spacing intervals are not fixed but proportional to how long you want to remember. For one-week retention, optimal gaps run 20-40% of the retention interval. For one-year retention, optimal gaps shrink to 5-10% in relative terms (Cepeda et al., 2008). Most flashcard apps ignore this entirely, using fixed algorithms regardless of the user's actual retention goals.

The testing effect adds another dimension. A foundational study demonstrated that students who took memory tests after studying prose passages showed substantially greater retention one week later compared to students who restudied the same material an equivalent number of times---despite the restudying group showing higher confidence in their retention abilities (Roediger & Karpicke, 2006). Testing trumps reviewing, even when reviewing feels more productive.

Meta-analytic evidence shows effect sizes averaging approximately d=0.50 for testing over restudying (Frontiers in Education, 2021). When spacing and testing combine, the effects compound: a large-scale study of 26,258 family physicians found that double-spaced retrieval practice yielded learning advantages of 58.03% versus 43.20% for controls, with transfer performance of 58.33% versus 52.39% at delayed testing (PubMed, 2024).

## The Algorithmic Arms Race: From SM-2 to FSRS

The story of spaced repetition algorithms begins with Piotr Wozniak's 1985 personal experiment, where he tracked his own learning and noticed that optimal intervals roughly doubled with each repetition (SuperMemo, true history documentation). This observation became Algorithm SM-0, establishing intervals of 1, 2, 4, 8, 16, and 32 days. By 1987, SM-2 introduced adaptive matrices adjusting intervals based on item difficulty---and remarkably, this 38-year-old algorithm still powers Anki and Mnemosyne today.

The current state of the art is FSRS (Free Spaced Repetition Scheduler), now integrated into Anki. FSRS tracks three components: retrievability (probability of recall), stability (the interval at which retrievability drops to 90%), and difficulty. Its 21 trainable parameters are optimized via machine learning on individual user review histories. In benchmarks across 727 million reviews from approximately 10,000 Anki users, FSRS-6 achieved a log loss of 0.3460 versus 0.4694 for Duolingo's HLR algorithm---substantially better prediction accuracy (FSRS GitHub documentation; Perplexity algorithm section).

A critical innovation in FSRS versions 4-6 was replacing exponential forgetting functions with power functions, which provide superior empirical fit to observed data. The mathematical formulation captures a key insight: the best time to review material is when you have almost but not quite forgotten it. Material retrieved with difficulty produces stronger subsequent retention than material retrieved easily (Expertium algorithm documentation).

However, the dirty secret of algorithm research is that **prediction accuracy is not the same as learning outcomes**. FSRS demonstrably predicts when users will forget better than SM-2. But no rigorous head-to-head trials have shown that more sophisticated algorithms produce meaningfully better real-world retention over months or years. Meta-analytic evidence indicates that expanding intervals produce only approximately 3% better outcomes than fixed intervals (Perplexity meta-analytic evidence). The research suggests any reasonable spaced algorithm massively outperforms massed practice, but the marginal gains from algorithmic sophistication remain unproven.

As one synthesis noted: "Innovation is currently concentrated in scheduler modernization, add-on ecosystems, and AI-assisted card generation---but adoption barriers are often not model capability but tutorial availability, workflow friction, and paywalls" (GPT-Researcher analysis). The algorithm is not the bottleneck.

## The Recognition-Production Chasm: Why Flashcard Users Cannot Speak

Here is where the research becomes uncomfortable for flashcard enthusiasts. The Kim and Webb 2022 meta-analysis of 48 experiments (N=3,411) found spaced practice consistently superior to massed practice for vocabulary retention, with large effect sizes (g=1.04 for immediate feedback, g=0.64-2.34 for delayed feedback). But the authors explicitly note that **the majority of studies focus on paired-associate learning---the flashcard format---and measure outcomes in formats similar to how material was learned** (Kim & Webb, 2022).

This matters because recognition and production appear to be distinct cognitive processes. A 2025 study of 314 EFL learners found that recognition knowledge preceded recall knowledge across all vocabulary components in a predictable developmental sequence (Gonzalez-Fernandez, 2025). Stewart et al. (2024) argue the difference between lexical recall and recognition is so pronounced that some scholars consider them "distinct psychometric constructs."

The practical implications are severe. One study found vocabulary knowledge explained 32-84% of speaking proficiency variance depending on conditions---but critically, "learners with large vocabulary sizes did not necessarily produce lexically sophisticated L2 words during speech" (Claude synthesis). Recognition creates an illusion of knowledge that production exposes as shallow.

The phenomenon of learners with thousands of reviewed cards who cannot hold basic conversations is so common it has become a meme in language learning communities. Practitioners on Reddit describe users with 20,000+ reviewed cards who struggle with basic conversation (Grok practitioner perspectives, 2024). The theoretical explanations for this gap are well-developed:

**Proceduralization failure.** DeKeyser's skill acquisition theory holds that declarative knowledge (what flashcard review builds) must transform into proceduralized knowledge through production practice over many trials. Flashcard review is controlled, deliberate processing; spontaneous speaking requires automatic processing that develops only through practice at the point of use.

**Transfer-appropriate processing.** Memory is strongest when encoding and retrieval processes match. The neural processes engaged during flashcard recognition differ from those required for conversational production. Words studied in one context may simply fail to activate in another.

**Context-dependent memory.** Godden and Baddeley's classic underwater study showed that words learned underwater were recalled significantly better underwater (mean 24.9) than on land (mean 17). Words learned in Anki's interface---white cards, specific fonts, the rhythm of the review session---may not transfer to the sights, sounds, and pressures of real-world contexts.

**Absence of communicative pressure.** Real conversation requires real-time lexical access under communicative demand. SRS provides no practice formulating messages under time constraints or managing the cognitive load of simultaneous comprehension and production.

## The Polyglot Consensus: A Supplement, Never a Replacement

When you examine how expert language learners actually use SRS, a pattern emerges despite surface disagreements. Steve Kaufmann, founder of LingQ and speaker of 20+ languages, is skeptical: "If you like doing flash cards, using spaced repetition systems, then it's worth doing. If not, this kind of learning activity won't help much" (Grok polyglot section). He prioritizes extensive listening and reading. Luca Lampariello, having learned 20 languages, reports using SRS "only for a few specific needs" and prefers repeated exposure in context (Claude polyglot section).

Gabriel Wyner's Fluent Forever method takes the opposite view, positioning SRS as central. His approach: learn pronunciation first, avoid translations where possible, and use personally-created flashcards connecting multiple information chunks---spelling, pronunciation, picture, personal connection, grammatical gender. He claims learners can "master 3,600 terms with approximately 90% accuracy" in four months (Claude polyglot section).

Despite divergent prescriptions, polyglots converge on several points:

- SRS is a supplement, never a replacement for authentic language interaction
- Personal card creation substantially outperforms pre-made decks
- Daily consistency matters more than session length
- Excessive SRS leads to burnout and should be moderated

The Refold methodology suggests beginners allocate 30-40% of study time to SRS, intermediates 20-30%, and advanced learners 10-15% or less. These recommendations derive from practitioner wisdom rather than controlled trials---research on optimal time allocation remains "frustratingly sparse" (Claude synthesis). But a meta-analysis of 21 extensive reading studies (N=1,268) found effect sizes of d=1.32 for vocabulary gains from reading alone---comparable to SRS effect sizes and suggesting reading could substitute or complement flashcard work (Claude meta-analysis reference).

The reconciliation between Krashen's comprehensible input hypothesis and explicit SRS learning may be that they serve different functions: SRS builds the vocabulary floor needed to understand input, while comprehensible input provides the rich contextualized exposure needed for true acquisition. As one framework describes it: "When you make a flashcard out of something, it's like you get a cup. As you interact with your target language, you fill that cup with water" (Claude context section).

## Context Solutions: Why Card Design Matters More Than Algorithm Choice

Several evidence-backed strategies address the decontextualization problem, though each carries trade-offs.

**Sentence cards versus word cards.** Sentence cards teach vocabulary and grammar simultaneously, showing words in natural context. Antimoon recommends them because "an isolated word is abstract---it's hard to remember abstract things." However, anime cards (target word highlighted within context) can be reviewed 2-4 times faster than full sentence cards, and word cards remain effective for concrete nouns with strong imagery (Claude context solutions). The trade-off is between depth and throughput.

**Sentence mining.** Creating cards from authentic content you are consuming---books, shows, podcasts---builds contextual associations between words and their sources. The "1T sentence" principle suggests only creating cards from sentences where you understand everything except one target element (Claude and Grok practitioner strategies). This ensures cards remain comprehensible and personally meaningful.

**Dual-coding approaches.** Paivio's research showed that activating both verbal and visual mental processes facilitates retention. Self-generated mnemonics outperform provided ones: "Participants who generated their own mnemonics demonstrated higher posttest performance" (Claude dual-coding section). The effort of creation produces stronger memory traces than passive consumption.

**AI-assisted card generation.** By 2024-2025, tools like GPT-4 are being used to generate flashcards from PDFs and texts. A comparison found GPT-4 superior to offline LLMs for math topics, though ethical concerns exist over AI reliance (Grok AI integration, 2024). Forum discussions quote a medical student survey claiming 53% would use ChatGPT to generate Anki cards if tutorials existed---suggesting adoption is gated by knowledge distribution and UX packaging, not AI capability (Anki Forums, 2024).

The tension is real: richer card design addresses context problems but increases creation time, potentially reducing overall practice volume. Quality versus quantity remains an unresolved optimization problem.

## The 140-Year Adoption Catastrophe: Why Education Ignored the Evidence

In 1988, Frank Dempster published "The Spacing Effect: A Case Study in the Failure to Apply the Results of Psychological Research," documenting that despite the spacing effect being one of the most dependable findings in experimental psychology, neither American classrooms nor textbooks implemented spaced reviews systematically. He noted, remarkably, that Soviet mathematics textbooks provided more distributed presentation than American equivalents. Nearly four decades later, the situation has barely improved.

The core problem is metacognitive misalignment. Students prefer massed learning because cramming produces stronger immediate test performance---the spacing advantage only manifests after delays. In controlled studies, 83% of participants rated massed practice as equally or more effective than spaced practice, despite spacing producing objectively superior delayed retention (Perplexity metacognitive misalignment). Spaced items feel "more detached from short-term memory and not readily available for immediate retrieval," creating the illusion that spacing is less effective.

This creates a judgments-of-learning paradox: students systematically mispredict their own learning. The study techniques that feel most productive (rereading, highlighting, cramming) produce weaker long-term retention than techniques that feel harder (spacing, testing, interleaving). Without external guidance, learners naturally gravitate toward ineffective methods.

Systemic barriers compound individual metacognition:

- Curriculum design favoring immediate assessment over long-term retention
- Textbooks organized into incompatible blocked chapters with no built-in review
- Teachers comfortable with massed practice and unfamiliar with spacing implementation
- Institutional inertia resistant to pedagogical change
- Assessment systems that reward short-term performance

As Lindsey et al. argued, providing optimal spaced practices "is beyond what any teacher or student can reasonably arrange" without technological support (Claude adoption section). Technology should solve this---yet app-based SRS faces its own implementation crisis.

## The Dropout Catastrophe: Why 1.76% Retention Dooms Apps

Education apps have the lowest user retention rates (1.76%) of any mobile app category (Claude dropout section). Only 0.1% of Duolingo users complete a course despite the platform's 500 million total users and 103.6 million monthly active users. These numbers reveal that the problem is not getting users to download learning apps but getting them to persist.

The mechanics of SRS create a specific failure mode. Skipping days causes exponential review backlog growth: Day 1 leaves 50 remaining reviews, Day 2 leaves 120, Day 3 leaves 190, Day 4 leaves 280 (Claude review burden section). The pile becomes overwhelming, discouraging return. "Learning too many new cards per day is the most common mistake people make when getting started with an SRS. This leads to an unmanageable number of reviews which takes away time from immersion and leads to burnout."

The psychological challenge is immediate effort versus delayed reward. Cramming provides "more salient representation for immediate conscious recollection." Spaced practice benefits manifest only over weeks or months. This temporal disconnect makes SRS feel less effective than it actually is---undermining persistence at the precise moment when persistence matters most.

Successful SRS use requires calibration that few users implement:

- 10-20 new cards daily maximum
- Completing due reviews before adding new material
- Limiting sessions to 15-30 minutes
- Accepting that three months of consistent practice is the threshold where benefits become visible

Users who practice consistently for three months are 4x more likely to achieve their language goals (Claude calibration data). But reaching that threshold requires surviving the delayed-reward period with nothing but faith in the science.

## The Business Model Conflict: Engagement vs. Learning

A 2021 systematic review of Duolingo effectiveness published in Taylor & Francis painted "a mixed (and sometimes negatively skewed) picture." The authors concluded that once novelty effects wear off, gamification cannot compensate for "design decisions prioritizing competition over collaboration, repetition and translation over meaningful feedback and context, and passive receptive skills (listening and reading) over active productive skills (speaking and writing)" (Claude business model section).

The potential conflict of interest is structural. Duolingo's metrics reveal the engagement imperative: 500+ million total users but only approximately 2% conversion to paid subscribers. Revenue depends on daily active users, session length, and advertising impressions. Users maintaining 7-day streaks are 3.6x more likely to remain engaged---explaining why streak mechanics dominate the user experience.

Engagement metrics (DAU, streaks, session length) drive revenue through advertising and conversions. Learning outcomes are harder to measure and may require shorter, less frequent sessions than engagement metrics reward. The heart system monetizes mistakes---users can purchase hearts or watch ads to continue practicing. Push notifications are optimized by multi-armed bandit algorithms for engagement, not learning.

Eight years after research began on Duolingo, the systematic review noted "we still have very little conclusive evidence about its effectiveness"---a striking admission given the company's scale and resources.

The Anki ecosystem represents the opposite philosophy: user-owned memory system, toolkit rather than curriculum, radical customization over guided paths. Active add-on development (AnkiAIUtils, custom schedulers, templates) demonstrates a platform-plus-plugin-economy model rather than locked-down learning product (GPT-Researcher Anki analysis). FSRS-5 was introduced to Anki in early 2025, with community sentiment largely positive for efficiency gains (Grok platform updates, 2025).

The trade-off is real. Anki's openness enables faster innovation but shifts onboarding and quality control burdens to users. Duolingo's guided experience reduces friction but may dilute pure SRS properties through overemphasis on recognition, short sessions, and variable review rigor. Neither approach has solved the 1.76% retention problem.

## What the Evidence Actually Supports

The synthesis exposes a fundamental mismatch between SRS capabilities and SRS usage patterns. The spacing effect is real, well-characterized at molecular and systems levels, and produces large effect sizes under laboratory conditions. Modern algorithms predict forgetting with impressive accuracy. Yet real-world outcomes disappoint for interconnected reasons:

**SRS trains recognition, not production.** The vast majority of flashcard systems build receptive knowledge that does not automatically transfer to speaking or writing ability. Users accumulate large passive vocabularies that feel like competence but collapse under productive demands.

**Context-dependent memory undermines transfer.** Words learned in one interface may not activate in conversational contexts. Richer card designs partially address this but require effort most users never invest.

**Business models misalign with learning science.** Engagement metrics dominate product design decisions. Gamification maintains user attention but may interfere with optimal spacing by encouraging over-practice of mastered material and under-practice of difficult items.

**The adoption paradox remains unsolved.** Despite 140 years of evidence, formal education has not systematically implemented spacing. Individual learners prefer massed practice because it feels more effective. Institutions lack infrastructure for distributed review.

**Polyglot wisdom converges on balance.** Expert language learners treat SRS as one component---typically 10-30% of study time---within systems emphasizing comprehensible input, production practice, and authentic interaction. SRS alone, no matter how optimized, cannot produce fluency.

## Key Takeaways

- The spacing effect is one of the most robust findings in psychology, producing approximately 74% better retention than cramming, with clear molecular mechanisms (CREB, MAPK) explaining why spacing works at the cellular level

- Modern algorithms like FSRS predict forgetting better than older methods, but no rigorous trials prove this translates to better real-world learning outcomes---any reasonable spaced algorithm massively outperforms cramming, with diminishing returns from further sophistication

- The recognition-production gap means flashcard mastery does not automatically transfer to speaking ability; users with thousands of reviewed cards may still struggle with basic conversation due to transfer-appropriate processing failures and context-dependent memory

- Optimal spacing intervals are proportional to desired retention (20-40% of retention interval for one-week goals, 5-10% for one-year goals), but most commercial apps ignore this entirely

- Expert language learners converge on using SRS as 10-30% of study time, never as a replacement for authentic input and production practice

- Education apps have the lowest retention rates (1.76%) of any app category; business models optimizing for engagement may actively conflict with optimal learning

- The 140-year failure to implement spacing in formal education reflects metacognitive misalignment (cramming feels more effective), systemic barriers (curriculum design), and individual preferences that override research evidence

- The path forward requires integration: combining vocabulary building with extensive reading/listening, production practice under communicative pressure, and recognition that flashcard competence is a means to comprehension, not an end in itself

## Sources

### Tier 1: Meta-Analyses and Systematic Reviews

- **Cepeda et al. (2006, 2008)** - Landmark meta-analysis of 317 experiments, 839 assessments establishing spacing effect robustness and optimal interval principles. [https://augmentingcognition.com/assets/Cepeda2006.pdf](https://augmentingcognition.com/assets/Cepeda2006.pdf)

- **Kim & Webb (2022)** - Meta-analysis of 48 experiments (N=3,411) on spaced vocabulary practice, effect sizes g=1.04-2.34. [SAGE Journals - Second Language Acquisition]

- **Taylor & Francis (2021)** - Systematic review of Duolingo effectiveness with critical assessment of gamification limitations.

- **Frontiers in Education (2021)** - Meta-analysis ranking distributed practice and testing as most effective learning techniques. [https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.581216/full](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.581216/full)

### Tier 2: Primary Research Studies

- **BrainFacts (2021)** - Neuroscience of spacing effect, CREB and MAPK mechanisms. [https://www.brainfacts.org/thinking-sensing-and-behaving/learning-and-memory/2021/the-neuroscience-behind-the-spacing-effect-030421](https://www.brainfacts.org/thinking-sensing-and-behaving/learning-and-memory/2021/the-neuroscience-behind-the-spacing-effect-030421)

- **PMC (2016)** - Molecular mechanisms of spaced learning including CREB, MAPK, and synaptic plasticity. [https://pmc.ncbi.nlm.nih.gov/articles/PMC5126970/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5126970/)

- **Nature Communications Biology (2025)** - fMRI study on neural integration differences between spaced and massed learning. [https://www.nature.com/articles/s42003-025-07964-6](https://www.nature.com/articles/s42003-025-07964-6)

- **PubMed (2024)** - American Board of Family Medicine study of 26,258 physicians on spaced retrieval practice. [https://pubmed.ncbi.nlm.nih.gov/39250798/](https://pubmed.ncbi.nlm.nih.gov/39250798/)

- **Gonzalez-Fernandez (2025)** - Study of 314 EFL learners on recognition-recall developmental sequence.

- **Stewart et al. (2024)** - Theoretical argument on recall vs. recognition as distinct psychometric constructs.

- **Roediger & Karpicke (2006)** - Testing effect study showing retrieval practice superiority over restudying. [https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x)

### Tier 3: Algorithm Documentation and Technical Sources

- **SuperMemo Algorithm Documentation** - History and technical specifications of SM-2 through SM-18. [https://help.supermemo.org/wiki/SuperMemo_Algorithm](https://help.supermemo.org/wiki/SuperMemo_Algorithm); [https://www.supermemo.com/en/blog/the-true-history-of-spaced-repetition](https://www.supermemo.com/en/blog/the-true-history-of-spaced-repetition)

- **FSRS GitHub Documentation** - Technical specifications and benchmarks for FSRS algorithm. [https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm)

- **Expertium Algorithm Documentation** - FSRS mathematical formulation and power-law forgetting curves. [https://expertium.github.io/Algorithm.html](https://expertium.github.io/Algorithm.html)

### Tier 4: Community and Practitioner Sources

- **Anki Forums** - Community discussions on FSRS-5, AI integration, and migration workflows. [https://forums.ankiweb.net/](https://forums.ankiweb.net/); [https://forums.ankiweb.net/t/collection-of-anki-resources/60044](https://forums.ankiweb.net/t/collection-of-anki-resources/60044)

- **Reddit Language Learning Communities** - Practitioner discussions on SRS limitations, recognition-production gap, and integration strategies. [https://www.reddit.com/r/Anki/comments/1jafkya/the_ultimate_2025_anki_settings_latest_updates/](https://www.reddit.com/r/Anki/comments/1jafkya/the_ultimate_2025_anki_settings_latest_updates/)

- **Duolingo Company Announcements** - Product updates and platform metrics. [http://investors.duolingo.com/news-releases/news-release-details/duolingo-unveils-major-product-updates-turn-learning-into-real-world](http://investors.duolingo.com/news-releases/news-release-details/duolingo-unveils-major-product-updates-turn-learning-into-real-world)

- **Carl Hendrick Substack** - Mental rehearsal theory of spacing benefits. [https://carlhendrick.substack.com/p/what-makes-spaced-practice-so-powerful](https://carlhendrick.substack.com/p/what-makes-spaced-practice-so-powerful)
