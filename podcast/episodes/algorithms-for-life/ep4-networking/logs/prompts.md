# Prompts Used for Episode: Algorithms for Life: Ep. 4, How to Communicate

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** If a `research-prompt.md` exists in this directory, it contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2026-02-10
- Slug: networking
- Title: Algorithms for Life: Ep. 4, How to Communicate
- Series: Algorithms for Life
- Episode Number: 4 of 10

---

## Deep Research Phase

### Tool Configuration

**Automated tools:**
- **Perplexity:** Academic & Official Sources (Phase 1 - always used, API-based)
- **GPT-Researcher:** Industry & Technical Sources (Phase 3 - API-based, uses OpenAI GPT-5.2)
- **Gemini Deep Research:** Strategic & Policy Sources (Phase 3 - API-based)

**Manual tools (user runs these):**
- **Claude:** Comprehensive Synthesis (Phase 3 - user pastes from https://claude.ai)
- **Grok:** Real-Time & Regional Sources (Phase 3 - user pastes from https://x.com/i/grok)

### Deep Research Prompts (Copy-Paste Ready)

**IMPORTANT:** These prompts use single newlines only to prevent accidental partial submissions when pasting into Chrome-based tools.

---

### Phase 1: Perplexity (Academic Foundation)

**Model:** sonar-deep-research
**Submitted:** 2026-02-11 (restarted)
**Status:** Complete (~5628 words, 138s async)

```
Research how computer networking protocols and algorithms provide models for human communication and social coordination. Cover these specific areas:

1. TCP/IP and flow control as models for conversation management — how acknowledgment systems (ACKs), retransmission, and windowing map to feedback loops in human dialogue. What does research in communication theory say about "conversational flow control"?

2. Congestion control and exponential backoff — how TCP's congestion avoidance algorithms (AIMD, slow start, congestion window) parallel strategies for managing information overload, conflict de-escalation, and social communication under stress. What psychology research exists on "backing off" in conversations?

3. Packet switching vs circuit switching as communication paradigms — how these map to asynchronous vs synchronous human communication (email/messaging vs phone calls/meetings). What does research show about effectiveness of each mode?

4. Network topology and social network structure — hub-and-spoke vs mesh vs peer-to-peer networks as models for organizational communication. What does social network analysis research reveal about information flow, bottlenecks, and resilience in human networks?

5. Routing algorithms (shortest path, load balancing, BGP) as models for how information propagates through social groups, how we choose communication channels, and how "routing around damage" applies to organizational resilience.

6. Bandwidth, latency, and the end-to-end principle — what these concepts reveal about communication channel capacity, the cost of indirection (intermediaries), and keeping intelligence at the endpoints.

7. Buffering and queuing theory — how network buffers relate to cognitive load, message queuing in organizations, and the tradeoff between throughput and latency in human information processing.

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

## Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?
- TCP acknowledgment/flow control ↔ conversational turn-taking (extensive coverage, strong evidence)
- Congestion control/backoff ↔ de-escalation and information overload (good coverage, some experimental data)
- Packet vs circuit switching ↔ async vs sync communication (strong healthcare study, UK survey)
- Network topology ↔ organizational structure (extensive Burt structural holes research)
- Routing algorithms ↔ information propagation (moderate coverage, mostly theoretical)
- Bandwidth/latency/end-to-end principle ↔ cognitive capacity (good Shannon theory, 10 bits/sec finding)
- Buffering/queuing ↔ cognitive load and throughput-latency tradeoffs (strong queuing theory coverage)

### What gaps exist in the academic literature?
- Very few controlled experiments directly testing networking-to-communication analogies
- Limited cross-cultural research on these communication patterns
- Missing: how these principles apply to human-AI communication specifically
- No direct research on "Algorithms to Live By" style practical frameworks for networking

### What recent developments aren't covered?
- Post-COVID remote/hybrid work communication patterns and "Zoom fatigue"
- Slack/Teams/Discord overload research (2023-2026)
- AI-mediated communication tools and their impact on information flow
- "No meeting" policies, async-first workplace culture experiments (Basecamp, GitLab, etc.)
- Rise of "deep work" movement (Cal Newport) and its connection to buffering/queuing

### What contradictions or uncertainties need more sources?
- Sync vs async: Perplexity found async 58.8% faster but also found face-to-face stronger for complex tasks — where's the crossover?
- Centralized vs distributed: structural holes research shows individual advantage but organizational vulnerability
- Is exponential backoff actually used in conflict resolution research by name, or is this an analogy?

### What industry/implementation questions arose?
- What real companies have explicitly applied networking principles to communication design?
- How do tools like Slack, Teams implement (or violate) these principles?
- What does the "async-first" movement look like in practice? Case studies?
- How do meeting-free days/focus time policies map to bandwidth management?

### What policy/regulatory angles need investigation?
- Right to disconnect laws and their relationship to "bandwidth management"
- Remote work policies and communication infrastructure requirements
- Organizational communication standards/frameworks (ISO, industry bodies)

### What practitioner perspectives are missing?
- Communication coaches who use technical metaphors
- Organizational designers applying network topology to team structure
- Remote work consultants on async vs sync best practices
- The "Algorithms to Live By" community and how they discuss networking chapter

---

## Phase 3: Targeted Followup Prompts

### GPT-Researcher (Industry & Technical)

**Focus:** Industry implementation, case studies, practical frameworks
**Submitted:** 2026-02-11

```
Research how networking and communication protocol concepts are applied to improve human communication in organizations and daily life, focusing on these specific questions:

**Industry Analysis:**
- What companies or organizations have explicitly applied computer networking principles (TCP-style acknowledgments, congestion control, async-first protocols) to redesign workplace communication? Document specific case studies with outcomes.
- How do modern communication tools (Slack, Teams, Discord, Basecamp) implement or violate networking principles like flow control, buffering, and congestion management? What does research show about their effectiveness?

**Case Studies & Implementation:**
- What happened when companies adopted "async-first" communication policies (e.g., GitLab, Basecamp, Automattic)? Document specific productivity metrics, employee satisfaction data, and implementation challenges.
- How has the post-COVID shift to remote/hybrid work changed communication patterns? What does 2023-2026 research show about "Zoom fatigue," meeting overload, and the shift toward asynchronous tools?

**Technical Details:**
- How does Cal Newport's "deep work" framework connect to network buffering and queuing theory? What evidence supports dedicated focus time vs. interrupt-driven communication?
- What practical frameworks exist for individuals to apply networking concepts (bandwidth management, latency reduction, congestion avoidance) to personal communication habits?

Focus on: Industry analyst reports, case studies, workplace research, communication tool analysis, productivity studies published 2020-2026.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

### Gemini Deep Research (Policy & Strategic)

**Focus:** Workplace policy, regulatory frameworks, organizational design
**Submitted:** 2026-02-11

```
Research how networking and communication protocol concepts relate to workplace communication policy and organizational design, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- What "right to disconnect" laws exist globally (France, Portugal, Australia, etc.) and how do they function as bandwidth management for workers? What evidence exists about their effectiveness?
- What organizational communication standards or frameworks exist (ISO, industry bodies) for managing information flow in teams?

**Comparative Policy Analysis:**
- How do different organizations (tech companies, healthcare, military, distributed teams) structure their communication policies? Compare async-first (GitLab), hybrid (Google), and sync-heavy (trading floors) approaches.
- What does research show about "meeting-free days" and "focus time" policies as organizational congestion control? Document specific implementations and measured outcomes.

**Strategic Context:**
- How are organizations redesigning team topology and communication architecture in the age of remote/hybrid work? What frameworks (Team Topologies book, Spotify model) apply networking principles?
- What is the strategic case for treating organizational communication as a network design problem rather than a cultural issue?

Focus on: Regulatory frameworks, organizational policy documents, strategic analyses, comparative studies across industries and countries.
Provide findings with official source citations, effective dates, and policy context.
```

### Claude (Comprehensive Synthesis)

**Focus:** Cross-dimensional analysis connecting networking theory to practical communication
**Submitted:** 2026-02-11

```
Research how computer networking protocols provide practical models for human communication, focusing on these specific questions:

- What does "Algorithms to Live By" (Brian Christian & Tom Griffiths) and similar works say about applying networking concepts to daily life? What specific networking principles do they highlight and what practical advice do they derive? Are there other books or frameworks that make similar connections?
- How does the concept of "protocol" in networking (agreed-upon rules for communication) map to social norms, etiquette, and communication contracts in relationships and teams? What research exists on explicit vs implicit communication protocols in groups?
- What is the neuroscience of "conversational bandwidth" — how many simultaneous conversation threads can humans track, what is the cognitive cost of context-switching between conversations, and how does this compare to network packet processing?
- How do networking concepts like "graceful degradation," "quality of service (QoS)," and "best effort delivery" apply to communication under stress? When should we accept "lossy" communication vs. insisting on "lossless" delivery?
- What are the strongest counterarguments against using networking metaphors for human communication? Where do the analogies break down, and what important aspects of human communication have no networking equivalent?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

### Grok (X/Twitter Discourse & Real-Time)

**Focus:** Recent discussions, practitioner perspectives, popular culture connections
**Submitted:** 2026-02-11

```
Search X/Twitter and recent news for discussions about applying computer networking concepts to human communication and social skills.

**Active X/Twitter Debates (last 30 days):**
- Who is discussing "Algorithms to Live By" networking concepts, communication protocols as social metaphors, or TCP/IP analogies for relationships? Quote specific posts.
- What are tech workers, communication coaches, or organizational designers saying about async vs sync communication in 2026? What's the sentiment?
- Any viral threads or posts about networking metaphors for social skills, introversion/extroversion as bandwidth, or "social protocols"?

**Practitioner Complaints & Frustrations:**
- What are remote workers complaining about regarding Slack/Teams overload, meeting fatigue, or communication burnout?
- What do communication coaches or therapists say about using technical metaphors to explain relationship dynamics?
- What are organizational consultants saying about team topology and communication design?

**News from the Last 30 Days:**
- Any new research, books, or frameworks published about networking-inspired communication strategies?
- Any workplace policy changes related to async-first communication, meeting reduction, or "right to disconnect"?

**Contrarian Takes:**
- Who argues that networking metaphors for human communication are reductive or harmful? What's their case?
- Who defends purely synchronous, high-bandwidth communication against the async-first movement?

**Output format:**
- Name every source (person + handle + credential + date)
- Tag credibility: [HIGH] industry leader, [MED] informed practitioner, [LOW] random account
- Include X post URLs where possible
```
