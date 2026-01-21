# Prompts Used for Episode: Stablecoin Series: Ep. 8, Post-Launch Operations & Continuous Compliance

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** If a `research-prompt.md` exists in this directory, it contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-26
- Slug: post-launch-operations
- Title: Stablecoin Series: Ep. 8, Post-Launch Operations & Continuous Compliance

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

## Phase 1: Perplexity Academic Foundation

**Prompt (copy-paste ready):**

```
Research stablecoin post-launch operations, continuous compliance, and operational sustainability at scale.

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

**Key areas to investigate:**
1. Continuous monitoring and transparency practices (reserve attestations, public dashboards, real-time metrics)
2. Regulatory compliance infrastructure (AML/KYC, SAR reporting, cross-jurisdictional compliance under MiCA, GENIUS Act)
3. Governance mechanisms and protocol evolution (centralized vs decentralized, token voting, multi-sig, participation rates)
4. Incident response and crisis management (de-pegging events, SVB collapse response, emergency interventions)
5. De-pegging scenarios and recovery (causes, recovery mechanisms, communication strategies, permanent failures like Terra/UST)
6. Operational cost scaling (custody, compliance, staffing, infrastructure at different supply levels)
7. Security operations (continuous audits, bug bounties, threat evolution, vulnerability response)
8. Long-term sustainability (revenue models, ecosystem development, operational resilience)

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links.
```

**Result:** Saved to research/p2-perplexity.md (~8,700 words)

---

## Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?
- **Extensive coverage:** GENIUS Act and MiCA regulatory frameworks, reserve attestation requirements, SVB crisis response, de-pegging mechanics (USDe, USDX, UST), governance token mechanisms
- **Moderate coverage:** Travel Rule compliance, multi-chain operational complexity, bug bounty programs, transparency dashboards
- **Brief mentions:** Operational cost specifics, staffing requirements, infrastructure scaling economics

### What gaps exist in the academic literature?
- **No concrete operational cost data** - Perplexity mentions compliance costs "scale substantially" but provides no actual figures (headcount, infrastructure costs, audit fees)
- **Limited case studies of operational crises** - SVB well-covered but no depth on other incidents (Celsius, FTX contagion effects)
- **Missing practitioner perspectives** - No quotes from actual stablecoin operators on day-to-day challenges
- **Governance participation rates** - Mentioned as a problem but no actual data on voter turnout, whale concentration metrics

### What recent developments aren't covered?
- **2025 regulatory enforcement actions** - Are there cases of issuers being penalized under new frameworks?
- **Real-world GENIUS Act implementation** - It was signed in July 2025, what has compliance looked like 5+ months later?
- **Recent de-pegging events** - USDe and USDX mentioned but what about other recent incidents?
- **Institutional adoption progress** - How are banks actually implementing stablecoin services post-regulation?

### What contradictions or uncertainties need more sources?
- **Reserve composition safety hierarchy** - Perplexity claims Treasury bills are safest, but what about liquidity during redemption surges?
- **Centralized vs decentralized governance** - Which actually performs better during crises?
- **Operational sustainability thresholds** - At what scale does a stablecoin become profitable?

### What industry/implementation questions arose?
- **How do compliance teams actually operate?** - Daily workflows, tool stacks, team structures
- **What does incident response look like in practice?** - Real playbooks, not theoretical frameworks
- **How do issuers manage multi-chain operations?** - Monitoring 30+ chains, deploying updates, managing bridges

### What policy/regulatory angles need investigation?
- **Cross-jurisdictional conflicts** - What happens when US and EU rules conflict?
- **Enforcement actions to date** - Has any issuer been penalized under new frameworks?
- **Central bank stablecoin interactions** - How do CBDCs affect stablecoin regulatory treatment?

### What practitioner perspectives are missing?
- **Compliance officer viewpoints** - What do they actually struggle with?
- **Security team experiences** - Real-world threat landscape beyond theory
- **Treasury management challenges** - How do issuers optimize reserve yields while maintaining liquidity?

---

## Phase 3: Targeted Followup Research

### GPT-Researcher Prompt (Industry & Case Studies)

```
Research stablecoin operational infrastructure and economics at scale, focusing on these specific questions:

**Industry Analysis:**
- What are the actual operational costs to run a compliant stablecoin at scale? (headcount, infrastructure, compliance systems, custody fees, audit costs at different supply levels from $100M to $100B+)
- What business models have proven sustainable? (comparison of Tether's reserve yield model vs Circle's institutional focus vs Ethena's yield-bearing approach)
- What does the team composition look like for major stablecoin issuers? (compliance, legal, engineering, operations, security roles and approximate headcount)

**Case Studies & Implementation:**
- How did Circle operationally respond to the SVB crisis hour-by-hour? What playbooks were executed?
- What went wrong operationally with Terra/UST, Celsius, and FTX-related stablecoin contagion?
- How do multi-chain stablecoin operations actually work? (deploying to 30+ chains, managing bridges, coordinating upgrades)

**Comparative Analysis:**
- How do operational maturity levels differ between established issuers (Tether, Circle) and newer entrants (PayPal, bank-issued tokens)?
- What infrastructure vendors power stablecoin operations? (monitoring platforms, compliance tools, custody providers)

Focus on: Industry analyst reports, market research, case studies, operational disclosures, job postings indicating team structures.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

### Gemini Deep Research Prompt (Policy & Strategic Context)

```
Research stablecoin regulatory compliance and enforcement post-GENIUS Act and MiCA implementation, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- What enforcement actions have occurred under GENIUS Act (signed July 2025) or MiCA (effective 2024)?
- What are the specific compliance deadlines and requirements issuers must meet under each framework?
- How do Travel Rule requirements differ between US (FinCEN), EU (TFR), UK (FCA), and Asia-Pacific jurisdictions?

**Comparative Policy Analysis:**
- How do stablecoin reserve requirements differ across US, EU, UK, Hong Kong, Singapore, and Japan?
- What happens when regulatory requirements conflict across jurisdictions? (e.g., MiCA interest payment restrictions vs US permissiveness)
- How are central banks treating stablecoins vs CBDCs in regulatory frameworks?

**Strategic Context:**
- What is the Federal Reserve's position on stablecoin master account access and systemic risk?
- How are banking regulators responding to deposit displacement concerns?
- What policy debates are ongoing about recovery/resolution procedures for systemic stablecoin failures?

Focus on: Regulatory frameworks, legislation, government policy documents, official guidance, enforcement actions, strategic policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

### Claude Prompt (Comprehensive Synthesis)

```
Research stablecoin post-launch operations and governance, focusing on these specific questions:

- How do stablecoin governance mechanisms actually perform during crises? Compare MakerDAO's emergency governance during SVB, Circle's centralized decision-making, and Tether's opaque response. Which model proved more effective and why?
- What is the real governance participation rate in decentralized stablecoin protocols? How concentrated is voting power among whales? What governance attacks or controversies have occurred?
- What operational security incidents have occurred at major stablecoins beyond smart contract exploits? (custody failures, key compromises, insider threats, oracle manipulations)
- How do recovery and wind-down plans actually work? What does the GENIUS Act specifically require and how are issuers implementing these plans?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

### Grok Prompt (Real-Time & Practitioner Perspectives)

```
Research stablecoin operations and compliance in practice, focusing on these specific questions:

**Recent Developments (last 12 months):**
- What operational challenges have stablecoin issuers discussed publicly since GENIUS Act passage?
- Have there been any de-pegging events, security incidents, or operational failures in 2025?
- What changes have major issuers (Tether, Circle, Paxos, PayPal) announced to their operations?

**Practitioner Perspectives:**
- What are compliance officers and operations teams at stablecoin issuers saying about day-to-day challenges?
- What discussions are happening in crypto/fintech communities about operational difficulties?
- What job postings from stablecoin issuers reveal about operational priorities and team structures?

**Industry Sentiment:**
- How are institutional users (banks, payment processors) evaluating stablecoin operational risk?
- What criticisms or concerns are being raised about transparency and governance?

Focus on: Recent news, industry discussions on X/Twitter, practitioner insights, job postings, company announcements.
Provide findings with source links, publication dates, and credibility indicators.
```

---
