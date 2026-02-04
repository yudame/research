# Prompts Used for Episode: Stablecoin Series: Ep. 8, Post-Launch Operations

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** If a `research-prompt.md` exists in this directory, it contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2026-02-04
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

**Submitted:** 2026-02-04
**Model:** sonar-deep-research
**Focus:** Academic & Official Sources

```
Research the operational infrastructure, cost structures, and daily operations required to run a stablecoin issuer at scale (multi-billion dollar circulation).

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

**Specific operational areas to investigate:**

1. **Monitoring Infrastructure**: What continuous monitoring systems do stablecoin issuers operate? (Reserve composition tracking, transaction surveillance, counterparty health monitoring, systemic risk detection)

2. **Staffing Models**: How many employees does it take to run a stablecoin at $1B, $10B, $60B+ scale? What roles are critical? Compare Circle (reported via S-1 SEC filing) vs. Tether (estimated via industry analysis) staffing levels and organizational structure.

3. **Vendor Ecosystem**: What third-party infrastructure is required? Identify key vendors for custody (Fireblocks, etc.), compliance analytics (Chainalysis, TRM Labs, Elliptic), node infrastructure, and payment integration. Include pricing where available.

4. **Cost Structures**: What are total annual operating costs for stablecoin issuers at different scales? Break down by: personnel, technology infrastructure, compliance/AML vendors, legal/regulatory, banking/custody fees, attestation/audit costs. Use Circle's S-1 filing as the primary source for transparent cost data.

5. **Multi-Chain Operations**: What is required to operate native issuance across 15-30 blockchains? Node infrastructure costs, treasury management models (hub-and-spoke), bridge protocols. Research Circle's CCTP (Cross-Chain Transfer Protocol) mechanics and Tether's 2025 chain deprecation decisions.

6. **Enforcement Operations**: How do freeze/blacklist operations work? Compare USDT enforcement model vs. USDC enforcement model using AMLBot 2023-2025 freeze/burn data. What staffing and legal infrastructure supports each model?

7. **Attestation Requirements**: What is the operational process for monthly reserve attestation under GENIUS Act requirements? Timeline, parties involved (auditors, custodians), AICPA 2025 Criteria for Stablecoin Reporting standards. Distinguish attestations from full PCAOB audits.

8. **Redemption Operations**: What are documented redemption SLAs across major issuers (Circle, Tether, Paxos, etc.)? Minimum amounts, fees, processing times, penalties for delays. How do issuers handle 24/7 blockchain vs. business-hours banking mismatch?

9. **Payment Processor Integration**: How do processors like Stripe integrate stablecoin payments? Research Stripe's documented architecture for USDC payments - merchant UX, settlement flows, risk abstraction.

10. **Regulatory Compliance Burden**: Beyond framework requirements (GENIUS Act, MiCA), what is the day-to-day operational compliance burden? KYC/AML vendor costs, transaction monitoring systems, regulatory reporting frequency.

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links covering the operational reality of running a stablecoin issuer from a banking-infrastructure perspective rather than a software perspective.
```

**Results:** → research/p2-perplexity.md

---

## Phase 3: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?

**Strongly covered (extensive evidence):**
- Cost structure breakdowns ($7.5-16.3M annually for $75B issuer)
- Staffing models (Tether: 150 employees/$93M per employee vs. Circle: 500-600 employees/$292K per employee)
- Vendor ecosystem (Fireblocks $500K-$2M, Chainalysis $30K-$50K, node infrastructure $500K-$1M)
- Reserve composition (GENIUS Act constraints, T-bills vs. demand deposits, Tether's Bitcoin/gold allocation)
- Attestation requirements (AICPA 2025 standards, monthly process with 2-3 week auditor fieldwork)
- Enforcement models (USDT: 7,268 addresses frozen/$3.3B vs. USDC: 372 addresses frozen/$109M)
- Multi-chain operations (CCTP mechanics, hub-and-spoke treasury, Tether 2025 chain deprecations)
- Redemption operations (Circle 0.05% fee, Tether 0.1% + $100K minimum)
- Payment integration (Stripe 1.5% processing fee vs. 2.9% credit card)

**Moderate coverage (some evidence, needs depth):**
- Circle Payments Network (CPN) operational burden - 29 institutions enrolled, 55 under review, 500 in discussions
- Incident response practices - SVB crisis mentioned, but no broader incident taxonomy
- KYC/AML friction points - transaction monitoring scale, but limited practitioner pain points
- Cross-chain bridge security - $2.8B in bridge-related hacks mentioned, but limited operational playbooks

**Brief mentions (needs significant expansion):**
- Daily operational tempo and monitoring center operations
- Customer support at scale for institutional clients
- Smart contract upgrade procedures and governance
- Competitive positioning and market share dynamics post-GENIUS Act
- Profitability sustainability in declining interest rate environment (Fed cuts 2026)
- Real-world payment processor integration beyond Stripe (Visa, Mastercard partnerships)

### What gaps exist in the academic literature?

1. **No operational incident postmortems** - Perplexity mentions SVB crisis but provides no SRE-style failure analysis, no documentation of chain outages, custodian issues, or bridge failures beyond Wormhole 2022
2. **Limited practitioner voice** - All data is from official sources (S-1, GENIUS Act, vendor docs) but no quotes from actual operators about pain points
3. **No comparative analysis of operational models** - Tether vs. Circle comparison on staffing/costs exists, but no analysis of which model is sustainable long-term under regulatory pressure
4. **Missing granular workflow details** - Monthly attestation "timeline" is described but no day-by-day operational checklist
5. **No discussion of automation vs. manual processes** - Which operational tasks are automated vs. requiring human oversight?
6. **Limited coverage of scaling challenges** - How does operational burden scale from $1B to $10B to $60B+ circulation?

### What recent developments aren't covered?

**Perplexity data cutoff appears to be Q3 2025 (latest Circle S-1 data). Recent developments to investigate (Q4 2025 - Feb 2026):**

1. **Circle's conditional OCC trust charter approval** (December 2025) - Perplexity doesn't mention this milestone
2. **Tether's USAT launch** (January 27, 2026 via Anchorage for GENIUS compliance) - Not mentioned
3. **Rain.xyz $250M Series C** (January 2026 at $1.95B valuation) - Not mentioned
4. **Dakota platform launch** (January 29, 2026) with embedded AML/KYB - Not mentioned
5. **PayPal cryptocurrency merchant acceptance data** (40% of US merchants, January 2026) - Not mentioned
6. **Hong Kong stablecoin licensing** (began March 2026) - Not mentioned
7. **Sonic bridge-to-native USDC conversion** (May 2025, 480M+ USDC, 87% of ecosystem) - Not mentioned
8. **Current Fed rate outlook** (economists project 100-150 bps of additional cuts through 2026) - Mentioned but needs current market data

### What contradictions or uncertainties need more sources?

1. **Tether staffing and profit figures** - Perplexity cites $93M profit per employee from external analysis, not verified Tether disclosures. Need more sources on whether this reflects efficiency or opacity.

2. **Circle operating margin** - Perplexity says "15-20%" but this requires validation against Q4 2025/Q1 2026 data

3. **Enforcement model effectiveness** - USDT freezes 7,268 addresses vs. USDC 372 addresses, but no data on which model is more effective at preventing illicit activity

4. **Reserve yield assumptions** - Perplexity uses 4% Treasury yield assumption, but Fed rate cuts in 2024-2026 mean current yields are lower. Need current yield curve data.

5. **Vendor pricing accuracy** - Fireblocks "$500K-$2M annually" and Chainalysis "$30K-$50K" are broad ranges. Need more granular enterprise pricing data.

6. **Attestation cost estimates** - "$1.2-$2.4M annually" for monthly attestations seems high compared to "$100K-$250K annually" mentioned elsewhere in the same report. Which is accurate?

### What industry/implementation questions arose?

1. **What does a 24/7 monitoring center actually look like?** - Perplexity describes WHAT is monitored (4 layers) but not HOW. Staffing shifts? Alert thresholds? Response playbooks?

2. **How do issuers operationalize multi-chain treasury?** - Hub-and-spoke model described conceptually, but how do market makers actually rebalance? What are the gas fee costs?

3. **What specific tools do compliance teams use daily?** - Chainalysis and TRM Labs are mentioned, but what does a compliance analyst's actual workflow look like?

4. **How do issuers handle smart contract upgrades?** - Governance process, testing procedures, rollback plans not covered

5. **What are the SLAs for different operational processes?** - Redemption SLAs covered, but what about attestation turnaround time, freeze execution time, customer support response time?

6. **How do payment processors like Stripe technically integrate USDC?** - High-level architecture described, but need technical details: wallet connection methods, settlement APIs, reconciliation processes

7. **What are the failure modes and contingency plans?** - Chain outages, custodian failures, bridge exploits mentioned as risks, but what are the documented response procedures?

8. **How do smaller issuers ($1B-$5B) differ operationally from Circle/Tether?** - Cost structure and staffing estimates provided, but what specific operational shortcuts or vendor dependencies exist?

### What policy/regulatory angles need investigation?

1. **OCC trust charter conditional approvals** (December 2025) - What are the CONDITIONS? What operational requirements did Circle, Ripple, Paxos, Fidelity, BitGo agree to?

2. **GENIUS Act implementation timeline** - Final rules due July 2026, effective January 2027, but what intermediate milestones exist? What guidance has Treasury issued since September 2025 ANPRM?

3. **State-level SQPSI frameworks** - Which states have "substantially similar" frameworks certified for sub-$10B issuers? What are operational differences vs. federal FQPSI path?

4. **International regulatory arbitrage** - How do issuers choose operational jurisdictions? Singapore vs. Hong Kong vs. EU vs. US - what are the comparative compliance burdens?

5. **MiCA reserve composition differences** - EU MiCA requires 30-60% in bank deposits for significant tokens. How does this operational requirement differ from GENIUS Act's permissible asset categories?

6. **Cross-border settlement coordination** - How do issuers handle redemptions for users in jurisdictions with capital controls or banking restrictions?

### What practitioner perspectives are missing?

**Key voices we need from X/Twitter and professional forums:**

1. **Compliance officers at stablecoin issuers** - What's the actual daily operational burden? What are the biggest pain points?

2. **Treasury managers** - How do you actually manage $60B+ in T-bills? What are the operational challenges of weekly/biweekly rebalancing to maintain 93-day maximum maturity?

3. **Customer support teams** - What are the most common institutional client issues? Where do users get stuck in redemption processes?

4. **Engineers maintaining multi-chain infrastructure** - Which chains are operationally hardest to maintain? What causes the most operational incidents?

5. **Smaller issuer operators** - How do $500M-$2B issuers compete with Circle/Tether network effects? What operational shortcuts are necessary at smaller scale?

6. **Market makers providing cross-chain liquidity** - What's the actual profitability of rebalancing USDC/USDT across chains? What are the operational friction points?

7. **Payment processor integration teams** - What are the integration challenges when adding stablecoin support? Where do merchants get stuck?

8. **Critics and skeptics** - Who's arguing that current operational models are unsustainable? What are the counterarguments to "stablecoins are just banks"?

### Research Tool Assignment

Based on these gaps and questions, here's how we'll assign Phase 4 targeted research:

**GPT-Researcher (Industry & Technical):**
- Circle's OCC trust charter conditions and operational implications
- Technical architecture of payment processor integration (Stripe, Visa, Mastercard)
- Multi-chain treasury operations and market maker mechanics
- Operational incident case studies beyond SVB
- Smaller issuer operational models ($1B-$5B scale)
- Bridge security operational playbooks
- Smart contract upgrade procedures

**Gemini (Policy & Strategic):**
- OCC conditional trust charter requirements (December 2025)
- GENIUS Act implementation timeline and intermediate guidance
- State SQPSI framework certifications and compliance differences
- International regulatory arbitrage analysis (Singapore vs. Hong Kong vs. EU vs. US)
- MiCA vs. GENIUS Act operational requirement comparison
- Hong Kong and Singapore stablecoin licensing operational requirements (2026)

**Claude (Comprehensive Synthesis):**
- Operational sustainability of Tether's lean model vs. Circle's compliance-heavy model
- Profitability dynamics in declining interest rate environment (2026 Fed cuts)
- Scaling challenges from $1B to $10B to $60B+ circulation
- Real-world operational incident taxonomy and response playbooks
- Automation vs. manual process decisions across operational domains

**Grok (X/Twitter Discourse & Recent Developments):**
- Practitioner complaints about KYC/AML operational burden
- Treasury manager perspectives on reserve rebalancing challenges
- Payment processor integration pain points from merchant/developer perspective
- Recent developments (Q4 2025 - Feb 2026): OCC charters, Tether USAT, Rain.xyz funding, Dakota launch, PayPal data, Hong Kong licensing
- Debates about operational model sustainability (Tether lean vs. Circle compliance-heavy)
- Contrarian takes on "stablecoins are banks disguised as software"

---


## Phase 4: Targeted Followup Research Prompts

### MANUAL PROMPTS - Submit these now while automation runs

#### Claude Research Prompt (paste at https://claude.ai)

**Submitted:** 2026-02-04
**Focus:** Comprehensive Synthesis

```
Research stablecoin post-launch operations, focusing on these specific questions:
- What is the operational sustainability of Tether's lean model (150 employees, $93M profit per employee) vs. Circle's compliance-heavy model (500-600 employees, 15-20% operating margin)? Which model survives long-term under GENIUS Act pressure?
- How do profitability dynamics change in a declining interest rate environment? Fed has cut rates from 5.25%-5.50% peak to 4.25%-4.50% (early 2026) with projections of 100-150 bps additional cuts through 2026. What happens to stablecoin issuer revenue and operating margins?
- What are the scaling challenges from $1B to $10B to $60B+ circulation? How does operational burden scale (personnel, vendor costs, compliance infrastructure)?
- Create a real-world operational incident taxonomy beyond SVB crisis. What chain outages, custodian issues, bridge failures, smart contract bugs, or compliance incidents have occurred? What were the response playbooks?
- Which operational tasks are automated vs. requiring manual human oversight? Where is the automation/human boundary across monitoring, compliance, redemptions, attestations?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

---

#### Grok Research Prompt (paste at https://x.com/i/grok)

**Submitted:** 2026-02-04
**Focus:** X/Twitter Discourse & Recent Developments (Opinion/Sentiment)

```
Search X/Twitter and recent news for stablecoin operational challenges and recent developments.

**Practitioner Complaints (last 60 days):**
- What are compliance officers, treasury managers, and engineers at stablecoin issuers complaining about?
- Specific pain points: KYC/AML operational burden, reserve rebalancing challenges, multi-chain maintenance headaches
- Payment processor integration complaints from merchants and developers

**Recent Developments (Q4 2025 - Feb 2026):**
- Circle's conditional OCC trust charter approval (December 2025) - what were the conditions?
- Tether's USAT launch (January 27, 2026 via Anchorage) - why now? GENIUS compliance strategy?
- Rain.xyz $250M Series C (January 2026, $1.95B valuation) - what do they do?
- Dakota platform launch (January 29, 2026) - embedded AML/KYB, what's the value prop?
- PayPal data: 40% of US merchants accept crypto (January 2026) - is this real adoption or marketing?
- Hong Kong stablecoin licensing (began March 2026) - who's applying?

**Active Debates:**
- Tether lean model vs. Circle compliance-heavy model - which is sustainable?
- "Stablecoins are banks disguised as software" - who's making this argument? Who's pushing back?
- Profitability concerns as Fed cuts rates - is the business model breaking?

**Output format:**
- Name every source (person + handle + credential + date)
- Tag credibility: [HIGH] industry leader, [MED] informed practitioner, [LOW] random account
- Include X post URLs where possible
```

---

### AUTOMATED PROMPTS - Launching parallel research

#### GPT-Researcher Prompt

**Submitted:** 2026-02-04
**Focus:** Industry & Technical Sources
**Model:** OpenAI GPT-5.2 (via gpt-researcher framework)

```
Research stablecoin post-launch operations, focusing on these specific questions:

**OCC Trust Charter Conditions:**
- Circle, Ripple, Paxos, Fidelity Digital Assets, and BitGo received conditional OCC trust charter approvals in December 2025. What are the CONDITIONS? What operational requirements did they agree to?

**Payment Processor Integration Architecture:**
- How do Stripe, Visa, and Mastercard technically integrate stablecoin settlements?
- Stripe's architecture for USDC payments: wallet connection methods, settlement APIs, reconciliation processes
- Visa's USDC settlement (launched December 2025): how does 7-day settlement window work operationally?
- Mastercard partnerships: which exist and what's the technical integration model?

**Multi-Chain Treasury Operations:**
- How do market makers actually rebalance USDC/USDT across chains? Profitability, gas fee costs, operational friction points?
- Hub-and-spoke treasury model: how much liquidity sits on each chain? How often is rebalancing needed?
- CCTP (Cross-Chain Transfer Protocol) real-world usage data: volume, settlement times, failure rates

**Operational Incident Case Studies:**
- Beyond SVB crisis, what operational incidents have occurred? Chain outages, custodian issues, bridge failures, smart contract pauses?
- Response playbooks and postmortems (if any exist)

**Smaller Issuer Operations ($1B-$5B scale):**
- How do mid-scale issuers differ operationally from Circle/Tether?
- What operational shortcuts or vendor dependencies exist?
- Cost structure differences and scaling challenges

**Bridge Security Playbooks:**
- Post-Wormhole and post-$2.8B bridge hacks, what operational security practices have emerged?
- Monitoring systems, validator set management, fraud detection

**Smart Contract Upgrade Procedures:**
- How do issuers handle smart contract upgrades? Governance, testing, rollback plans

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

---

#### Gemini Deep Research Prompt

**Submitted:** 2026-02-04
**Focus:** Policy & Strategic Context

```
Research stablecoin post-launch operations, focusing on these specific questions:

**OCC Conditional Trust Charter Requirements:**
- What are the specific operational conditions attached to Circle, Ripple, Paxos, Fidelity Digital Assets, and BitGo's December 2025 OCC trust charter approvals?
- What capital requirements, operational requirements, or compliance obligations were imposed?

**GENIUS Act Implementation Timeline:**
- What intermediate milestones exist between now and January 2027 effective date?
- What guidance has Treasury issued since September 2025 ANPRM?
- What are the operational compliance checkpoints for issuers?

**State SQPSI Framework Certifications:**
- Which states have "substantially similar" frameworks certified for sub-$10B issuers?
- What are the operational differences between state SQPSI path vs. federal FQPSI path?
- Which states are most favorable for stablecoin issuers operationally?

**International Regulatory Arbitrage:**
- Compare operational compliance burden: Singapore vs. Hong Kong vs. EU (MiCA) vs. US (GENIUS Act)
- How do issuers choose operational jurisdictions? What are the trade-offs?
- Which jurisdiction has the most favorable cost/benefit for different issuer profiles?

**MiCA vs. GENIUS Act Operational Comparison:**
- MiCA requires 30-60% in bank deposits for significant tokens vs. GENIUS Act's permissible asset categories
- How do these different reserve composition requirements affect operational complexity?
- What are the cost implications of each framework?

**Hong Kong and Singapore Licensing (2026):**
- What are the operational requirements for Hong Kong stablecoin licensing (began March 2026)?
- Singapore MAS framework operational requirements
- Who has applied? What's the timeline?

**Cross-Border Settlement Coordination:**
- How do issuers handle redemptions for users in jurisdictions with capital controls or banking restrictions?
- What operational challenges exist for global stablecoin operations?

Focus on: Regulatory frameworks, legislation, government policy documents, strategic plans, comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

---

