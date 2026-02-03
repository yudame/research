# Prompts Used for Episode: Stablecoin Series: Ep. 8, Post-Launch Operations

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** If a `research-prompt.md` exists in this directory, it contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2026-02-02
- Slug: post-launch-operations
- Title: Stablecoin Series: Ep. 8, Post-Launch Operations

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

#### Phase 1: Perplexity - Academic Foundation

**Prompt:**

```
Research the day-to-day operational realities of running a stablecoin at scale after launch, focusing on continuous monitoring, incident response, customer operations, cross-chain management, attestation cycles, exchange relationships, smart contract upgrades, transaction monitoring, and profitability models.
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
- Continuous monitoring systems (reserve composition, transaction flow, counterparty health, systemic risk)
- Incident response protocols (pause mechanisms, custodial breaches, smart contract vulnerabilities, bridge exploits, regulatory enforcement)
- Customer operations at scale (KYC/AML, account management, dispute resolution, regulatory reporting, 24/7 support)
- Cross-chain management (multi-chain minting, liquidity fragmentation, bridge risk, reserve allocation)
- Attestation cycles (monthly reserve attestations, annual audits, regulatory examinations)
- Smart contract upgrades (proxy patterns, governance processes, testing requirements)
- Transaction monitoring and AML (KYC processes, sanctions screening, Travel Rule, suspicious activity reporting)
- Exchange relationships (listings, market-making, liquidity providers, payment processors)
- Profitability models (reserve yield, transaction fees, competitive dynamics, regulatory constraints)

**Good coverage:** Perplexity provided substantial academic/authoritative sources on monitoring systems, compliance, and governance

**Limited coverage:** Real-world implementation details, specific vendor systems, practitioner challenges, recent operational incidents beyond bridges

### What gaps exist in the academic literature?
- Specific operational metrics (what SLAs do stablecoin operators actually achieve?)
- Cost structures (how much does 24/7 monitoring actually cost? What's the staffing model?)
- Vendor ecosystem (who are the specialized service providers for monitoring, compliance, attestation?)
- Operational failures and near-misses (besides major bridge exploits, what smaller incidents happen regularly?)
- Customer support metrics (response times, resolution rates, common issue types at scale)

### What recent developments aren't covered?
- Latest smart contract upgrade incidents (last 12 months)
- Recent exchange delistings or partnership terminations
- New monitoring tools or compliance platforms launched in 2025-2026
- Recent attestation failures or audit qualifications
- Operational changes resulting from GENIUS Act implementation (effective Jan 2027)

### What contradictions or uncertainties need more sources?
- Profitability sustainability as interest rates normalize (Perplexity notes concern but needs more analysis)
- Optimal multi-chain strategy (how do operators actually decide which chains to support?)
- Customer support scalability limits (at what volume does the current model break?)
- Yield-bearing stablecoin regulatory treatment (still uncertain, needs policy analysis)

### What industry/implementation questions arose?
- What specific monitoring platforms do Circle and Tether actually use?
- How do payment processors like Stripe integrate stablecoin operations technically?
- What does the org chart look like for a stablecoin operator (how many people in each function)?
- How much does it cost to run attestation cycles monthly vs quarterly?
- What are the actual SLAs for minting/redemption operations?
- Which cross-chain bridges are considered safe enough for major issuers to use?

### What policy/regulatory angles need investigation?
- GENIUS Act implementation timeline and readiness (18-month countdown started July 2025)
- MiCA vs GENIUS operational differences (which creates more operational burden?)
- Upcoming Hong Kong and Singapore regulatory deadlines
- Yield-bearing stablecoin regulatory classification debates
- CBDC impact on stablecoin operations (competitive threat or complementary infrastructure?)

### What practitioner perspectives are missing?
- What are stablecoin operators complaining about on X/Twitter?
- What operational challenges do smaller issuers face that Perplexity didn't cover?
- What do payment processors say about stablecoin integration challenges?
- What are compliance officers saying about AML operational burden?
- What recent incidents or near-misses have practitioners discussed publicly?

---

## Phase 3: Targeted Followup Research

Based on Phase 2 analysis, creating targeted prompts for all 4 tools...

---

## Content Planning Phase

### Episode Classification
- **Series Position:** Closer (Episode 8 of 8)
- **Evidence Status:** Minor conflict (sources agree on cost ranges and operations; diverge on Tether model transparency)
- **Content Density:** Protocol-heavy (4 operational protocols, specific cost figures, vendor stacks)

### Toolkit Selections
- **Hook Type:** Surprising Statistic -- Circle's $908M annual Coinbase payment
- **Takeaway Structure:** Numbered Protocol -- 4 sequential operational protocols (monitoring, attestation, multi-chain, enforcement)
- **Contradiction Handling:** Brief acknowledgment -- Tether efficiency vs. transparency gap

### Output
- `content_plan.md` created: 2026-02-02
- Follows three-section structure: Foundation (why this is banking), Evidence (cost structures, enforcement, integration), Application (operational playbook)
- Series finale framing included with wrap-up guidance

---


#### Claude Research - Comprehensive Synthesis

**Prompt:**

```
Research stablecoin post-launch operational realities, focusing on these specific questions from Phase 2 analysis:
- What are the actual cost structures and staffing models for running 24/7 stablecoin operations? How many people does a $50-100B stablecoin operation require across monitoring, compliance, customer support, and engineering?
- What specific monitoring platforms, compliance vendors, and operational tools do major stablecoin issuers use? Who are the specialized service providers in the stablecoin operations ecosystem?
- How do stablecoin operators decide which blockchains to support multi-chain? What are the operational considerations for adding a new chain vs removing an underperforming one?
- What are the documented operational SLAs for minting/redemption operations at Circle, Tether, and other major issuers? How do they achieve rapid settlement compared to traditional banking?
- What is the timeline and operational readiness for GENIUS Act implementation (effective January 2027)? What operational changes are issuers making now to prepare?
**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

---

#### Grok Research - X/Twitter Discourse & Real-Time Developments

**Prompt:**

```
Search X/Twitter and recent news for stablecoin post-launch operations discussion (last 30 days).
**Active X/Twitter Debates:**
- Who are stablecoin operators, compliance officers, or payment processors discussing operational challenges? (Names, handles, credentials)
- What are practitioners complaining about regarding AML compliance burden, cross-chain complexity, or regulatory preparation?
- Quote specific posts about operational incidents, near-misses, or challenges
**Recent Operational Incidents (last 30 days):**
- Any smart contract upgrades, pause events, or operational issues at major stablecoins?
- Exchange delistings or partnership terminations announced?
- Attestation or audit issues disclosed?
**News from the Last 30 Days:**
- GENIUS Act implementation updates or guidance?
- New monitoring/compliance platform launches?
- Payment processor stablecoin integration announcements (Stripe, PayPal, etc.)?
**Practitioner Perspectives:**
- What are smaller stablecoin issuers saying about operational burden compared to Circle/Tether?
- What do DeFi protocols say about stablecoin integration challenges?
**Output format:**
- Name every source (person + handle + credential + date)
- Tag credibility: [HIGH] industry leader, [MED] informed practitioner, [LOW] random account
- Include X post URLs where possible
```

---

#### GPT-Researcher - Industry & Implementation Details

**Prompt:**

```
Research stablecoin post-launch operational realities, focusing on these specific questions:
**Industry Analysis & Cost Structures:**
- What are the actual operational costs for running a stablecoin at scale? Break down by monitoring infrastructure, compliance systems, staffing, attestation/audit fees, and technology platforms.
- What is the vendor ecosystem for stablecoin operations? Who provides monitoring platforms, compliance tools, attestation services, custody solutions, and cross-chain infrastructure?
- What are the documented SLAs and operational metrics for major stablecoin issuers (minting/redemption times, customer support response times, system uptime)?
**Implementation & Technical Details:**
- How do payment processors like Stripe and PayPal technically integrate stablecoin acceptance? What APIs, settlement processes, and operational workflows are involved?
- Which cross-chain bridges are considered operationally safe by major issuers? What monitoring and risk management practices do they use for multi-chain operations?
- What are the operational org structures for major stablecoin issuers? How many people in each function (monitoring, compliance, customer support, engineering, etc.)?
**Case Studies & Recent Incidents:**
- Document recent operational incidents beyond major bridge exploits (smart contract upgrades, pause events, attestation issues, exchange problems) in the last 12 months.
- What operational challenges have smaller stablecoin issuers faced that the major players have overcome through scale?
Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis, vendor websites, company announcements.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

---

#### Gemini Deep Research - Policy & Strategic Context

**Prompt:**

```
Research stablecoin post-launch operational realities, focusing on these specific policy and strategic questions:
**Regulatory Implementation & Timeline:**
- What is the detailed implementation timeline for the GENIUS Act (signed July 2025, effective January 2027)? What operational preparations are stablecoin issuers making now?
- What are the specific operational differences between GENIUS Act (US) and MiCA (EU) requirements? Which framework creates greater operational burden for issuers?
- What are the upcoming regulatory deadlines in Hong Kong, Singapore, and other major jurisdictions? How do their operational requirements compare?
**Yield-Bearing Stablecoin Regulatory Debates:**
- What is the current regulatory classification debate around yield-bearing stablecoins? Are they securities, deposits, or something else?
- How are different jurisdictions treating yield-bearing vs non-yield-bearing stablecoins operationally?
- What operational compliance requirements would apply if yield-bearing stablecoins are classified as securities vs deposits?
**CBDC Impact Analysis:**
- How could wholesale CBDC development change stablecoin operational requirements?
- What are central banks saying about stablecoin operations vs CBDC operations?
- Will CBDCs replace, compete with, or complement private stablecoin operations?
**Strategic Context:**
- What policy debates are ongoing about appropriate reserve management, attestation frequency, and operational oversight for stablecoins?
- How are regulators evaluating the systemic risk from stablecoin operations at current scale ($250B+)?
Focus on: Regulatory frameworks, legislation, government policy documents, strategic plans, comparative policy analysis, central bank research.
Provide findings with official source citations, effective dates, and policy context.
```

---

