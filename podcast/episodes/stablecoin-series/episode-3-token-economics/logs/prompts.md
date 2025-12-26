# Prompts Used for Episode: Stablecoin Series: Ep. 3, Token Economic Design

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** The `research-prompt.md` file in this directory contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-26
- Slug: episode-3-token-economics
- Title: Stablecoin Series: Ep. 3, Token Economic Design & Stabilization Mechanisms
- Series: Stablecoin Series (Episode 3 of 3)

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

## Phase 1: Perplexity Academic Research

**Prompt used:**
```
Research stablecoin token economic design and stabilization mechanisms, focusing on: (1) Collateralization models - comparing fiat-backed, crypto-collateralized, algorithmic, and hybrid approaches with empirical peg stability data across market stress periods; (2) Stabilization mechanisms - how arbitrage, algorithmic minting/burning, interest rate adjustments, and dual-token systems (Terra/LUNA, Frax/FXS) function and under what conditions they fail; (3) Failure analysis - detailed examination of Terra/UST collapse, Iron Finance, and other de-pegging events including Black Thursday March 2020 and March 2023 banking crisis; (4) Monetary policy and governance - how stablecoins implement supply expansion/contraction, who holds governance rights, and what conflicts of interest exist; (5) Economic sustainability - distinguishing genuine value creation from Ponzi-like structures (e.g., Anchor Protocol's 20% APY).

**Research methodology:**
- Prioritize peer-reviewed studies, meta-analyses, systematic reviews, and authoritative sources (BIS, FSB, ECB, Federal Reserve research)
- Distinguish between correlation and causation in findings
- Report effect sizes and practical significance (specific peg deviation amounts, recovery times, collateral ratios)
- Note study populations and whether findings generalize across different market conditions (bull vs bear markets)
- Compare individual studies against meta-analyses and systematic reviews
- Identify preliminary research vs. well-replicated findings
- Note funding sources and potential conflicts of interest when relevant
- Include contradictory evidence (e.g., DAI's successful recovery vs. UST's death spiral)
- Cite specific studies, researchers, and sources throughout
- Provide full source URLs for all citations

**Output:** Comprehensive research report with extensive citations, sample sizes where applicable, methodological details, and source links covering collateralization models, stabilization mechanisms, failure modes, and economic sustainability.
```

**Status:** Completed - saved to research/p2-perplexity.md

---

## Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?
- Collateralization models (fiat-backed, crypto-collateralized, algorithmic, hybrid) with extensive empirical data
- Death spiral mechanics in algorithmic stablecoins (Terra/UST, Iron Finance)
- Liquidation mechanism design (auction vs. Stability Pool approaches)
- Governance concentration and conflicts of interest (MakerDAO MKR concentration)
- Anchor Protocol's unsustainable 19.5% yield as Ponzi-like structure
- Arbitrage concentration risk (only 6 active USDT arbitrageurs)
- March 2020 Black Thursday and March 2023 SVB crisis recovery patterns

### What gaps exist in the academic literature?
- Limited coverage of post-Terra (2024-2025) stablecoin innovations
- Ethena's USDe and other delta-neutral strategies not stress-tested
- Emerging hybrid models (Frax v2, crvUSD) need evaluation
- Long-term sustainability of new revenue models unclear

### What recent developments aren't covered?
- 2024-2025 regulatory implementation (GENIUS Act enforcement, MiCA compliance)
- New stablecoin market entrants and their design approaches
- How has the competitive landscape evolved post-Terra?
- PayPal USD (PYUSD), institutional stablecoins emergence

### What contradictions or uncertainties need more sources?
- Can hybrid models achieve stability without fiat backing?
- Is Ethena's funding rate strategy sustainable in bear markets?
- How effective is governance minimization vs. active governance?

### What industry/implementation questions arose?
- What market share shifts have occurred 2024-2025?
- How are issuers adapting to regulatory requirements?
- What technical innovations are gaining traction?
- Case studies of successful stablecoin integrations in payments

### What policy/regulatory angles need investigation?
- GENIUS Act implementation details and issuer compliance
- MiCA enforcement and European market restructuring
- Asia-Pacific approaches (Singapore, Hong Kong, UAE)
- Cross-border regulatory arbitrage dynamics

### What practitioner perspectives are missing?
- What are DeFi developers saying about design tradeoffs?
- How are stablecoin issuers responding to regulatory pressure?
- Real-time professional discourse on X/Twitter about new models

---

## Phase 3: Targeted Followup Prompts

### GPT-RESEARCHER PROMPT (Automated - 6-20 min)

```
Research stablecoin token economics and market evolution 2024-2025, focusing on these specific questions:

**Industry Analysis:**
- What market share shifts have occurred among major stablecoins (USDT, USDC, DAI, PYUSD, others) in 2024-2025?
- How are stablecoin issuers (Circle, Tether, Paxos) adapting their revenue models to regulatory requirements?
- What is the current state of institutional stablecoin adoption and integration with traditional finance?

**Case Studies & Implementation:**
- How has Ethena's USDe performed under various market conditions and what are its design vulnerabilities?
- What specific technical innovations (crvUSD liquidation mechanisms, Frax v2 hybrid design) have emerged?
- Case studies of successful stablecoin payment integrations (Stripe, PayPal, Visa partnerships)

**Technical Details:**
- How do modern liquidation mechanisms compare (Stability Pools vs. auctions vs. Ethena's delta-neutral)?
- What oracle improvements have been implemented post-Iron Finance to prevent manipulation?
- How are new stablecoins addressing the capital efficiency vs. stability tradeoff?

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

### GEMINI PROMPT (Automated - 3-10 min)

```
Research stablecoin regulatory frameworks and policy implementation 2024-2025, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- What are the specific reserve requirements, audit obligations, and licensing conditions under the GENIUS Act?
- How is MiCA being enforced and which stablecoins have achieved or lost European market access?
- What regulatory actions have been taken against non-compliant stablecoin issuers since 2024?

**Comparative Policy Analysis:**
- How do Singapore (MAS), Hong Kong (HKMA), UAE (VARA), and other jurisdictions approach stablecoin regulation?
- What regulatory arbitrage dynamics are emerging as issuers choose jurisdictions strategically?
- How are different countries balancing innovation encouragement vs. consumer protection?

**Strategic Context:**
- How is the GENIUS Act reshaping stablecoin issuer behavior and market structure?
- What policy debates are ongoing about central bank digital currencies (CBDCs) vs. private stablecoins?
- How are regulators addressing systemic risk concerns from stablecoin-Treasury market connections?

Focus on: Regulatory frameworks, legislation, government policy documents, strategic plans, comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

### CLAUDE PROMPT (Manual - User will paste from claude.ai)

```
Research stablecoin token economics, focusing on these specific cross-dimensional questions:

- What is the relationship between collateralization model choice and long-term peg stability across market cycles?
- How do revenue model sustainability (Maker fees vs. Anchor subsidies vs. Ethena funding rates) predict failure?
- What governance structures have proven most effective at adapting to market stress without centralization?
- How do different stablecoin designs perform as payment infrastructure vs. DeFi collateral vs. value storage?
- What lessons from Terra/UST, Iron Finance, and March 2023 banking crisis should inform future stablecoin design?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

### GROK PROMPT (Manual - User will paste from x.com/i/grok)

```
Research stablecoin token economics and stabilization mechanisms, focusing on these specific questions:

**Recent Developments (last 12 months):**
- What new stablecoin designs or significant protocol updates have launched since January 2024?
- How has Ethena's USDe performed during recent market volatility and what are practitioners saying about its risks?
- What regulatory enforcement actions or issuer responses have shaped the market in 2024-2025?

**Practitioner Perspectives:**
- What are DeFi developers and stablecoin issuers saying about design tradeoffs on Crypto Twitter/X?
- How are traders and market makers discussing arbitrage efficiency and de-pegging risks?
- What controversies or debates are ongoing about specific stablecoin designs (Ethena, crvUSD, PYUSD)?

**Real-Time Market Intelligence:**
- What stablecoins are gaining or losing market traction and why?
- How are institutional players (banks, payment processors) discussing stablecoin integration?
- What warning signs or concerns are practitioners raising about current market conditions?

Focus on: Recent news, industry discussions on X/Twitter, practitioner insights, real-time market commentary.
Provide findings with source links, publication dates, and credibility indicators.
```

---

## Cover Art Generation Phase

**Tool Used:** Gemini 3 Pro Image via OpenRouter

**Generation Method:** --auto from report.md

**Branding Applied:**
- Logo: Yudame logo (top-left, vertically centered with brand text)
- Brand: Yudame Research (Playfair Display SemiBold)
- Series: Stablecoin Series (Playfair Display Italic)
- Episode: Ep 3 - Token Economics (Playfair Display Italic)

**Output:** cover.png (1.2MB, 1024x1024)

**Date:** 2025-12-26
