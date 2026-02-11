# Claude Research: Algorithms for Life: Ep. 4, How to Communicate

**Date:** 2026-02-11
**Focus:** Comprehensive Synthesis — "Algorithms to Live By" connections, social protocols, neuroscience of conversational bandwidth, counterarguments

---

## Research Output

# When TCP meets talk: networking protocols as models for human communication

**Computer networking protocols offer surprisingly precise — but ultimately partial — models for understanding human communication.** From TCP's three-way handshake mirroring the universal structure of human greetings, to the brain's conscious processing bottleneck operating at just **10 bits per second** against a sensory firehose of 1 billion bits per second, the parallels between digital and human communication systems illuminate genuine structural similarities. Yet these analogies carry a critical limitation: they systematically hide what makes human communication most human — emotion, ambiguity, power, meaning co-creation, and the constitutive role of dialogue in building social reality. This report synthesizes findings across cognitive science, conversation analysis, military doctrine, organizational behavior, crisis communication research, and philosophy of language to map exactly where networking metaphors illuminate, where they mislead, and what practical wisdom they offer.

---

## The networking chapter of "Algorithms to Live By" and its intellectual ecosystem

Brian Christian and Tom Griffiths devote Chapter 10 of *Algorithms to Live By* (2016) to networking, covering packet switching, acknowledgment, exponential backoff, flow control, backchannels, and bufferbloat. Their central move is mapping TCP/IP mechanisms to daily communication with specific, actionable advice.

**Packet switching** — breaking data into independent chunks rather than holding an entire circuit open — maps to the principle that effective communicators chunk ideas into digestible segments rather than monologuing. **Acknowledgment signals** (TCP's ACK packets) map directly to conversational backchannels: the "uh-huh," "I see," and "mm-hmm" that regulate conversational flow. Christian and Griffiths note these serve the same function as TCP acknowledgments — confirming receipt and enabling the sender to calibrate. Without them, communication degrades, just as TCP connections stall without ACKs.

Their most celebrated analogy is **exponential backoff as "the algorithm of forgiveness."** Originally developed for ALOHAnet to handle radio signal collisions, exponential backoff has each sender wait progressively longer intervals before retrying after failure. Applied socially: if a friend repeatedly flakes on plans, doubling the interval between attempts (rather than either giving up entirely or calling daily) represents an optimal strategy. The algorithm balances persistence with self-protection.

The chapter's most provocative insight concerns **bufferbloat**. Christian and Griffiths argue the core problem with modern connectivity is not being "always connected" but being **"always buffered."** Historically, a missed phone call was a dropped packet — if important, the sender retried. Today, every missed message enters a buffer (inbox, notification queue) that grows endlessly. Their prescription: **"the tactical dropping of balls is a critical part of getting things done under overload."** Some messages should simply be dropped rather than queued, because latency — not throughput — is the critical variable in communication. This "Better Never Than Late" principle challenges the default assumption that all messages deserve processing.

An intellectual ecosystem surrounds this work. Alexander Galloway's *Protocol: How Control Exists after Decentralization* (MIT Press, 2004) takes a fundamentally different approach, arguing technical protocols ARE mechanisms of social control in the network age, not merely analogies. Galloway traces how the word "protocol" migrated from diplomatic etiquette to computing and back, noting that TCP/IP, DNS, and HTML function as instruments of distributed power. Duncan Watts's *Six Degrees* (2003) demonstrates through formal network science that computer, biological, and social networks share genuine mathematical properties — small-world topology, scale-free distributions, cascade dynamics — making the parallels structural rather than merely metaphorical. Daniel Graham's 2022 paper in *Frontiers in Computer Science*, "Nine insights from internet engineering that help us understand brain network communication," provides peer-reviewed validation that packet switching, routing, flow control, and error handling have genuine structural parallels in neural function.

**The evidence base spans a spectrum from rigorous to illustrative.** Watts's work represents formal mathematical correspondence. Conversation analysis research (detailed below) provides empirical validation of protocol-like structures in human interaction. Christian and Griffiths' specific prescriptions — use exponential backoff with flaky friends, drop messages rather than buffer them — remain intuitive wisdom rather than tested interventions. The analogies illuminate real structural parallels but have not been empirically validated as behavioral prescriptions.

---

## How networking handshakes map to the universal grammar of conversation

The strongest evidence for networking-to-communication parallels comes not from computer scientists looking outward but from linguists who independently discovered protocol-like structures in conversation. The seminal work is Sacks, Schegloff, and Jefferson's 1974 paper "A Simplest Systematics for the Organization of Turn-Taking for Conversation" (*Language*, Vol. 50), which established that conversation operates on a rule-governed system remarkably analogous to networking protocols.

Their turn-taking system is **"locally managed, party-administered, interactionally controlled, and sensitive to recipient design"** — participants dynamically allocate speaking rights in real-time, functioning like flow control in TCP/IP. Turn Constructional Units (sentences, phrases, words) function as data packets. Transition Relevance Places — moments where turn-transfer can occur — parallel acknowledgment windows. The system produces the principle "one speaker at a time," directly analogous to collision avoidance. A 2009 study by Stivers et al. in *PNAS* confirmed this system is **near-universal across 17 languages**, with only small quantitative differences in gap duration — suggesting something approaching a species-wide communication protocol.

**Adjacency pairs** map with striking precision to networking request-response patterns. Schegloff's analysis of telephone openings identified four sequential adjacency pairs that parallel the TCP/TLS handshake:

- **Summons/Answer** (phone rings → "Hello?") maps to SYN
- **Identification/Recognition** maps to authentication/certificate exchange  
- **Greeting tokens** map to SYN-ACK
- **Initial inquiries** ("How are you?") map to parameter negotiation

Conversational **repair mechanisms**, documented by Schegloff, Jefferson, and Sacks (1977), function as error handling. Self-initiated repair ("I mean, she went to the store, not the bank") parallels sender-side error detection. Other-initiated repair ("Did you say store or bank?") parallels NACK/retransmission requests. The "progressivity principle" — absence of evidence of misunderstanding is treated as sufficient to proceed — directly parallels TCP's assumption of successful delivery unless timeout occurs.

Amy Edmondson's psychological safety research reframes team dynamics through a protocol lens. Her 1999 paper in *Administrative Science Quarterly* showed that psychologically safe teams reported **more errors but performed better** — because the implicit "protocol" allowed error messages to be transmitted and processed rather than suppressed. Google's Project Aristotle validated this across **180+ teams**, finding psychological safety was the single strongest predictor of team effectiveness. Teams with high psychological safety had lower turnover, more diverse ideas, and were rated effective twice as often by management. The framework maps cleanly: psychological safety defines what messages can be sent (error reports, dissent, vulnerability), how errors are handled (productively acknowledged versus punished), and what acknowledgment signals leaders provide.

**The cost of "protocol mismatch"** — when people operate under different implicit communication rules — is well-documented. Judee Burgoon's Expectancy Violations Theory (1978, 1993) formalized this: people carry implicit expectations (protocol specifications) about communication behavior, and violations trigger arousal and evaluation. Deborah Tannen's work on conversational style demonstrates this concretely: her "high-involvement" speakers (overlapping speech, rapid pace) operate under a different protocol configuration than "high-considerateness" speakers (waiting for clear turn signals). When these styles collide, Tannen notes, "whoever is expecting the longer pause will find that they can't get the floor" — a direct flow-control mismatch. Cross-cultural examples are dramatic: Walmart's American greeting protocols were interpreted as "flirtatious" by German customers, contributing to the chain's withdrawal from Germany. An American supervisor's public criticism of an Indonesian employee — violating the implicit protocol against public shaming — reportedly resulted in a mob response.

Thomas Malone and Kevin Crowston's Coordination Theory (1994, *ACM Computing Surveys*) provides the most explicit bridge between networking and organizational coordination: coordination is "managing dependencies between activities," with specific mechanisms (scheduling, notification, synchronization) paralleling networking protocols. Research on implicit versus explicit coordination shows that **teams transition from explicit (TCP-like, with handshakes and acknowledgments) to implicit (connectionless, relying on shared mental models) as they develop shared understanding** — analogous to protocol optimization where established connections require less overhead.

---

## The brain processes 10 bits per second through a billion-bit firehose

The neuroscience of "conversational bandwidth" reveals quantitative constraints that give networking metaphors genuine explanatory power. A landmark 2025 paper by Zheng and Meister in *Neuron* — "The unbearable slowness of being" — established that **conscious human thought operates at approximately 10 bits per second**, a figure consistent across over a century of measurements spanning typing, reading, speech, and decision-making. This occurs against sensory input of roughly **1 billion bits per second** — a compression ratio of 10^8 with no engineering equivalent. An advanced typist at 120 words per minute produces approximately 10 bits per second. Recommended narration rate (160 wpm) yields about 13 bits per second. The authors note that a single neuron can match the entire organism's behavioral output — the bottleneck is at the level of conscious processing, not neural hardware.

This bottleneck echoes Donald Broadbent's 1958 filter model, the first formal information-processing model of attention, which explicitly drew on Shannon's engineering framework. Broadbent proposed that a high-capacity sensory system feeds into a severely limited conscious processor through a selective filter — functioning as a bandwidth management system. Subsequent revisions (Treisman's attenuation theory, Lavie's load theory) refined the mechanism but preserved the core insight: attention manages a bottleneck where throughput vastly exceeds conscious processing capacity.

**Working memory capacity defines conversational threading limits.** George Miller's famous "7±2" (1956) is now considered an overestimate that conflated storage capacity with rehearsal strategies. Nelson Cowan's rigorous revision (2001, *Behavioral and Brain Sciences*) established that true working memory capacity, with chunking and rehearsal controlled, averages **about 4 chunks** (range 3-5). This aligns with research showing humans struggle to track more than 3-5 conversation threads simultaneously. Research on multi-party communication by Yoon et al. (2023) found that tracking "who knows what" in multiparty conversation — a demanding working memory task — was significantly impaired in patients with hippocampal damage, and Wardlow (2024) showed that under high cognitive load, speakers fail at audience design entirely, defaulting to egocentric communication.

A remarkable finding from Coupé et al. (2019, *Science Advances*) demonstrates a language-universal bandwidth constraint: across **17 languages studied**, all converge on approximately **39 bits per second** of information transmission despite dramatic differences in syllable rates and information density. Languages with high information density per syllable are spoken slower; low-density languages are spoken faster. This ~39 bits/second rate aligns with the brain's theta wave frequency (4-8 Hz), crucial for speech processing, suggesting a fundamental cognitive bottleneck analogous to Shannon's channel capacity.

**Context-switching costs are severe and well-documented.** Sophie Leroy's attention residue research (2009, *Organizational Behavior and Human Decision Processes*) demonstrated that when switching tasks, part of attention remains with the prior task — cognitive activity about Task A persists even when performing Task B. Critically, simply completing a task before switching is necessary but **not sufficient** for clean transitions. Rubinstein, Meyer, and Evans (2001) found task switching involves two distinct stages — goal shifting and rule activation — with costs increasing with task complexity. Meyer estimated multitasking reduces productivity by up to **40%**. Gloria Mark's extensive workplace observation research found that attention spans on screens have declined to approximately **47 seconds**, workers switch "working spheres" every **10.5 minutes**, and about **50% of interruptions are self-inflicted**. Task switching correlates with increased stress markers including elevated cortisol.

The parallel to networking is meaningful but imperfect. Short-term memory functions as a buffer; attention operates as a priority queue (the cocktail party effect demonstrates priority-based filtering); information processing has measurable throughput limits. However, network packet processing is fundamentally parallel while conscious human thought is fundamentally serial. Human "packet size" (chunks) varies with expertise and context. And the 10^8 compression ratio between sensory input and behavioral output — where massive information is discarded rather than preserved — has no engineering equivalent. Networks aim to preserve data; brains aim to extract gist.

---

## Commander's intent, SBAR, and the science of "lossy" communication

Networking concepts of graceful degradation, Quality of Service, and lossy versus lossless transmission find their most compelling real-world parallels in crisis communication, military doctrine, and healthcare. These domains have independently developed frameworks that functionally replicate networking QoS mechanisms for human communication under stress.

**Fuzzy Trace Theory** (Valerie Reyna and Charles Brainerd) provides the scientific foundation for understanding "lossy" human communication. FTT's central insight: people encode **verbatim** (exact surface form) and **gist** (bottom-line meaning) memories separately and in parallel, and these are stochastically independent — gist is NOT derived from verbatim memory. Verbatim traces decay faster than gist traces. Most remarkably, **experts preferentially use gist processing** — "adults and individuals with specialized expertise tend to rely on the least precise memory representations needed when making judgments." This inverts the networking analogy: in data transmission, lossy compression always loses quality; in human cognition, gist extraction can produce **better** decision-making than verbatim processing. Reyna's 2020 PNAS paper demonstrates this in health communication: people were willing to pay more for a safer product when safety was expressed relatively ("product A is safer than product B") than when expressed with precise statistics — lossy communication outperformed lossless.

**Military communication doctrine** represents the most systematic application of QoS-like principles to human communication:

- **Brevity codes** (ATP 1-02.1) function as pre-negotiated compression dictionaries — both parties know the codebook, enabling extreme information compression without ambiguity. "WINCHESTER" (no ordnance remaining) compresses a complex status report into a single word. These provide no security benefit; they exist purely to reduce bandwidth requirements.

- **PACE plans** (Primary, Alternate, Contingency, Emergency) implement graceful degradation by specifying independent fallback communication methods. CISA's 2024 extension of PACE to civilian agencies explicitly acknowledges that "what may be unacceptable during normal operations may become acceptable under the C or E steps" — a direct statement of graceful degradation policy.

- **Commander's intent** is perhaps the strongest networking analogy of all. Described as "the simplest possible story of what must be done and why" (Fletcher & Gaines, 2023, Modern War Institute), it functions as radical lossy compression of complex operational plans into actionable gist. Air Force doctrine (AFDP 1-1, 2023) states that "greater competence and trust enable more concise commander's intent" — shared context acts as a pre-negotiated compression dictionary, reducing needed bandwidth. However, Shattuck and Woods (2000) found company commanders matched battalion commander's intent in only **34% of cases** — demonstrating that extreme lossy compression carries significant reconstruction error rates.

**Healthcare's SBAR framework** (Situation, Background, Assessment, Recommendation) functions as a standardized message format specification, originating from US Navy nuclear submarine procedures and adapted for clinical use by Michael Leonard at Kaiser Permanente in 2002. The Joint Commission identified communication errors as the leading cause of medication errors, delays in treatment, and wrong-site surgeries — making this a domain where lossy communication kills. Aviation's readback/hearback protocol implements TCP-like closed-loop communication with error detection, though FAA research found hearback error rates of **37-40%** during high-traffic periods, demonstrating that even lossless protocols degrade under load.

The CDC's Crisis and Emergency Risk Communication framework explicitly acknowledges that crisis degrades human processing capacity: "Under intense stress and possible information overload, we tend to miss the nuances... not fully hearing information... not remembering as much as we should." The response is intentional message compression — reducing bandwidth requirements to match degraded receiver capacity. The radiation emergency instruction "Get inside. Stay inside. Stay tuned" exemplifies extreme lossy compression optimized for stressed receivers.

Ritz, Wild, and Johnsrude (2022, *Journal of Neuroscience*) provided neural evidence for graceful degradation in speech processing: fMRI showed that even mildly degraded but perfectly intelligible speech requires substantially more cognitive control than clear speech. Under cognitive load, processing of degraded speech was blocked entirely at trivial load levels, while clear speech processing declined linearly — a graceful degradation curve.

---

## Where the metaphor breaks: emotion, ambiguity, and the constitution of meaning

The strongest counterarguments against networking metaphors for human communication come from three directions: the conduit metaphor critique, the constitutive view of communication, and documented harms from over-engineering human systems.

**Michael Reddy's 1979 landmark essay** identified that 70% of English metalingual expressions rely on a "conduit metaphor" — the assumption that communication works by packaging thoughts into word-containers, sending them through a language-conduit, and having receivers extract meaning. Reddy demonstrated this is fundamentally wrong: meaning cannot be "transferred" but must be actively reconstructed by receivers using their own cognitive resources and context. His alternative "Toolmakers Paradigm" shows communicators as people in fundamentally different experiential environments — one in a forest, another in a desert — who must reconstruct each other's meaning from inadequate signals. The conduit metaphor, which networking analogies reinforce, encourages the false belief that "if the words are right, meaning transfer is automatic."

**Shannon explicitly excluded meaning from his information theory.** "Information" in Shannon's sense is a measure of statistical surprise, not semantic content — a message with high Shannon entropy might be meaningless gibberish, while a simple "yes" might answer a life-changing question. Warren Weaver's popularization inflated the theory's scope beyond Shannon's careful mathematical work, and many critiques of the "Shannon-Weaver model" actually target this extrapolation.

Several aspects of human communication have no networking equivalent whatsoever:

**Strategic ambiguity is a feature, not a bug.** Eric Eisenberg's 1984 paper in *Communication Monographs* argued that clarity is "neither normative nor a sensible standard" for organizational communication. Ambiguity promotes unified diversity (fostering agreement on abstractions without limiting interpretations), preserves deniability, facilitates organizational change, and enables face-saving. In networking, ambiguity is noise; in human communication, it is often essential to cooperation and diplomacy.

**Communication constitutes social reality rather than merely describing it.** J.L. Austin's speech act theory showed that utterances like "I now pronounce you married" or "You're fired" don't transmit information — they **create** states of affairs. The Communication as Constitutive of Organizations (CCO) theory holds that organizations don't merely use communication; they are constituted by it. As Kuhn, Ashcraft, and Cooren (2017) state: "Meaning resides neither in the messages actors exchange, nor in those actors' cognition, but in the practices in which an array of participants engage." This is fundamentally incompatible with a packet-transmission model.

**Gregory Bateson's multi-level communication** has no protocol equivalent. Every human utterance operates simultaneously at content and relationship levels, carrying digital (verbal) and analogic (nonverbal) dimensions. Bateson's double bind theory demonstrated that conflicting messages at different logical levels — a parent saying "I love you" while displaying hostile body language — can produce profound psychological distress. Network protocols operate at clearly separated, non-contradictory layers; human communication layers routinely contradict each other, and this contradiction carries meaning.

**Hubert Dreyfus's phenomenological critique** argues that human understanding depends on embodied, situated, unconscious processes irreducible to formal rule-following. His five-stage skill acquisition model shows that only novices operate via explicit rules (like computers); experts perceive situations holistically through embodied engagement. **Bakhtin's dialogism** insists every utterance is fundamentally responsive and anticipatory — language is not a neutral conduit but a site of ideological struggle containing multiple social voices in tension.

**Documented harms from over-engineering human systems** provide concrete warnings. Taylorism's treatment of workers as interchangeable machine components — "In our scheme, we do not ask for the initiative of our men" (Taylor, 1906) — produced labor unrest, creativity suppression, and the eventual corrective of the human relations movement. Modern algorithmic management research documents increased burnout, reduced prosocial behavior, and worker commodification. Australia's "Robodebt" automated debt assessment scandal was documented by the UN Special Rapporteur as producing "systemic errors, biases and discrimination" in "a virtually human rights free-zone." The replication crisis in social psychology is partly attributable to overly mechanistic stimulus-response models that assumed context-free determinism.

---

## Conclusion: a useful lens with dangerous blind spots

Networking metaphors illuminate genuine structural parallels in human communication. Turn-taking operates on locally managed protocol rules. Adjacency pairs mirror request-response patterns. Working memory imposes real bandwidth constraints at approximately **4 chunks**. Cognitive processing bottlenecks at **10 bits per second** create measurable throughput limits. Teams transition from explicit to implicit coordination as shared mental models develop — protocol optimization in action. Military and healthcare communication frameworks independently reinvented networking concepts like compression, graceful degradation, and error correction.

Three novel insights emerge from this synthesis. First, **Fuzzy Trace Theory inverts the lossy compression analogy**: unlike data networks, where lossy transmission always degrades quality, human gist processing is the preferred mode of expert cognition — "lossy" human communication often outperforms "lossless." Second, **the ~39 bits/second language universal** suggests a species-wide channel capacity constraint that shapes all human languages equivalently, regardless of their surface characteristics. Third, **the strongest parallels come from researchers who never intended them**: conversation analysts like Sacks, Schegloff, and Jefferson discovered protocol-like structures in conversation through empirical observation, not through analogy — suggesting these structural similarities are genuine rather than imposed.

The critical limitation is not that the metaphor is wrong but that it is **radically partial**. As Lakoff and Johnson demonstrated, every metaphor highlights some aspects of reality and hides others. The networking metaphor highlights efficiency, throughput, and error correction. It hides meaning-making, power dynamics, embodiment, strategic ambiguity, emotional resonance, and the constitutive role of communication in creating social reality. The practical lesson: use networking concepts as diagnostic tools for communication problems — congestion, protocol mismatch, buffer overflow, missing acknowledgments — but never mistake the map for the territory. Human communication is not information transfer with noise; it is the collaborative construction of shared worlds.

---

## Sources

Here are the key sources from the report, grouped by topic:

**Networking-to-life frameworks**
- Christian & Griffiths, *Algorithms to Live By* (2016), Ch. 10 — [Amazon](https://www.amazon.com/Algorithms-Live-Computer-Science-Decisions/dp/1627790365)
- Galloway, *Protocol: How Control Exists after Decentralization* (MIT Press, 2004) — [MIT Press](https://mitpress.mit.edu/9780262572330/protocol/)
- Watts, *Six Degrees: The Science of a Connected Age* (2003) — [Goodreads](https://www.goodreads.com/book/show/818170.Six_Degrees)
- Graham (2022), "Nine insights from internet engineering that help us understand brain network communication" — [Frontiers](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.976801/full)

**Conversation analysis & turn-taking protocols**
- Sacks, Schegloff & Jefferson (1974), "A Simplest Systematics for the Organization of Turn-Taking" — [Project MUSE](https://muse.jhu.edu/article/452679/summary)
- Dingemanse et al., "Repair: The Interface Between Interaction and Cognition" — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6849777/)
- Conversation analysis overview — [Simply Psychology](https://www.simplypsychology.org/conversation-analysis.html)

**Psychological safety & team protocols**
- Edmondson's psychological safety framework — [Lab Manager summary](https://www.labmanager.com/psychological-safety-in-the-lab-amy-edmondson-s-blueprint-for-open-communication-34041)
- Malone's Coordination Theory — [MIT Sloan faculty page](https://mitsloan.mit.edu/faculty/directory/thomas-w-malone)
- Implicit vs. explicit coordination in teams — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8215207/)

**Neuroscience of bandwidth & processing limits**
- Zheng & Meister (2025), "The Unbearable Slowness of Being: Why do we live at 10 bits/s?" — [Neuron/ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0896627324008080) | [arXiv](https://arxiv.org/abs/2408.10234)
- Coverage in [Scientific American](https://www.scientificamerican.com/article/the-human-brain-operates-at-a-stunningly-slow-pace/)
- Coupé et al. (2019), universal ~39 bits/s language rate — [Richard Brooks analysis](https://richard-brooks.com/the-universal-speed-limit-of-human-language-and-what-it-means-for-ai/)
- Cowan's working memory capacity (4±1) — [Journal of Cognition](https://journalofcognition.org/articles/10.5334/joc.387)
- Broadbent's filter model — [Routledge Encyclopedia](https://www.rep.routledge.com/articles/thematic/attention/v-1/sections/broadbents-filter-theory-and-the-early-late-selection-debate)

**Context-switching costs**
- Leroy's attention residue research — [ABLE summary](https://able.ac/blog/switch-cost-effect/)
- Mark's workplace attention research — [This Is Your Brain podcast](https://thisisyourbrain.com/2024/03/our-incredible-shrinking-attention-span-with-dr-gloria-mark/)
- Cocktail party effect — [Wikipedia](https://en.wikipedia.org/wiki/Cocktail_party_effect)

**Crisis communication & graceful degradation**
- Fuzzy Trace Theory — [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4979567/) | [Wikipedia](https://en.wikipedia.org/wiki/Fuzzy-trace_theory)
- Military brevity codes — [ALSSA](https://www.alssa.mil/mttps/brevity/)
- PACE plans — [CISA 2024](https://www.cisa.gov/sites/default/files/2024-10/2024_NCSWICPTE_Leveraging_PACE_Plan_Emergency_Comms_Ecosystems.pdf)
- Commander's intent — [Modern War Institute](https://mwi.westpoint.edu/the-commanders-path-to-victory-communication-without-comms/) | [Wikipedia](https://en.wikipedia.org/wiki/Intent_(military))
- SBAR framework — [EBSCO](https://www.ebsco.com/research-starters/health-and-medicine/situation-background-assessment-recommendation-sbar)
- Ritz, Wild & Johnsrude (2022), neural cost of degraded speech — [J. Neuroscience](https://www.jneurosci.org/content/42/23/4619)
- CDC CERC framework — [CDC](https://www.cdc.gov/radiation-emergencies/php/communication-resources/cerc-rad.html)

**Counterarguments & metaphor limits**
- Reddy's conduit metaphor critique — [Wikipedia](https://en.wikipedia.org/wiki/Conduit_metaphor)
- Eisenberg (1984), "Ambiguity as Strategy in Organizational Communication" — [Semantic Scholar](https://www.semanticscholar.org/paper/Ambiguity-as-strategy-in-organizational-Eisenberg/98795ca55521444cdf651b072812041ea65bc796)
- CCO theory — [Sage Journals](https://journals.sagepub.com/doi/full/10.1177/0170840618782284)
- Tannen on conversational style — [Wikipedia](https://en.wikipedia.org/wiki/Deborah_Tannen)
- Algorithmic management harms — [HBR](https://hbr.org/2024/02/the-social-cost-of-algorithmic-management)
