# Prompts Used for Episode: Stablecoin Series: Ep. 6, Market Making, Liquidity & Exchange Partnerships

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** If a `research-prompt.md` exists in this directory, it contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-26
- Slug: liquidity-partnerships
- Title: Stablecoin Series: Ep. 6, Market Making, Liquidity & Exchange Partnerships

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

### Phase 1: Perplexity Academic Research

**PERPLEXITY PROMPT (Phase 1 - Academic Foundation):**

```
Research stablecoin liquidity infrastructure: market maker partnerships, exchange listings, decentralized exchange (DEX) integration, and multi-chain liquidity strategies.

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
1. Market maker functions for stablecoins (continuous quotes, arbitrage, inventory management)
2. Leading institutional market makers (Wintermute, Jump Trading, Cumberland, DWF Labs) and their services
3. Centralized exchange listing requirements and costs (Coinbase, Binance, Kraken)
4. Primary vs secondary market structure (authorized participants, redemption mechanisms)
5. DEX liquidity pools and AMM mechanics (Uniswap, Curve, PancakeSwap)
6. Multi-chain deployment effects on liquidity fragmentation
7. Liquidity bootstrapping strategies and network effects
8. Trading volume data, bid-ask spreads, and market depth analysis
9. Case studies: How USDC competed against USDT's dominance
10. Regulatory requirements affecting exchange listings (MiCA, GENIUS Act)

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links.
```

---

### Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

#### What subtopics and themes emerged?
- Market maker concentration (Wintermute, Jump, Cumberland, DWF Labs, GSR, Kairon, B2C2) - extensive coverage
- Exchange listing processes (Coinbase, Binance requirements) - good coverage
- DEX mechanics (Uniswap, Curve, PancakeSwap) - solid coverage
- Multi-chain deployment (Ethereum, Tron, Solana, L2s) - excellent data
- Primary vs secondary market structure - strong academic analysis
- USDC vs USDT competition - thorough case study
- Regulatory impact (GENIUS Act, MiCA) - mentioned but not deeply explored

#### What gaps exist in the academic literature?
- Specific market making fee structures and compensation models (mentioned but not quantified)
- Actual listing costs beyond Coinbase/Binance (smaller exchanges, DEXs)
- Failed stablecoin launches due to liquidity problems (no case studies)
- Long-term sustainability of liquidity mining incentives

#### What recent developments aren't covered?
- Q4 2025 market maker dynamics and any recent partnership announcements
- Latest bridge security incidents or improvements
- New stablecoin launches and their liquidity strategies in 2025
- Any changes to exchange listing requirements post-GENIUS Act

#### What contradictions or uncertainties need more sources?
- USDT arbitrageur count (only ~6/month) vs USDC (~521) - need validation
- True costs of market making partnerships (privately negotiated)
- Whether Tron dominance is sustainable vs Ethereum/Solana growth

#### What industry/implementation questions arose?
- What do market making agreements actually specify? (compensation, exclusivity, duration)
- How do new stablecoins practically bootstrap from zero liquidity?
- What's the minimum viable capital to establish functional markets?
- Real-world case studies of liquidity bootstrapping strategies

#### What policy/regulatory angles need investigation?
- How is GENIUS Act specifically affecting exchange listing decisions?
- Are there MiCA delistings happening now, and how are projects responding?
- What regulatory clarity do market makers need to operate?

#### What practitioner perspectives are missing?
- What do traders actually experience in terms of slippage and spreads?
- Market maker perspectives on the most challenging aspects of stablecoin support
- Exchange perspectives on what makes a stablecoin listing-ready

---

### Phase 3: Targeted Followup Research

**GPT-RESEARCHER PROMPT (Automated - 6-20 min):**

```
Research stablecoin liquidity bootstrapping and market making economics, focusing on these specific questions:

**Industry Analysis:**
- What are the actual costs and compensation structures in market making agreements (trading fees, token allocations, minimum commitments)?
- How do new stablecoins overcome the cold-start problem (no users because no liquidity, no liquidity because no users)?
- What capital requirements exist to establish minimum viable liquidity?

**Case Studies & Implementation:**
- What specific liquidity bootstrapping strategies succeeded or failed? (USDC growth, PayPal USD launch, Ethena USDe)
- How did smaller stablecoins (FRAX, LUSD, GHO) build liquidity without Tether/Circle resources?
- What lessons from failed stablecoin launches relate to liquidity problems?

**Technical Implementation:**
- How do market makers technically integrate across CEXs, DEXs, and multiple chains?
- What infrastructure do projects need before approaching market makers?
- How are liquidity mining incentives structured and are they sustainable?

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis.
```

---

**GEMINI PROMPT (Automated - 3-10 min):**

```
Research regulatory impacts on stablecoin exchange listings and market making, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- How is the GENIUS Act (July 2025) specifically affecting stablecoin exchange listings in the US?
- What MiCA compliance requirements apply to market makers and liquidity providers?
- What regulatory clarity do institutional market makers need to operate (licensing, capital requirements)?

**Comparative Policy Analysis:**
- How do US (GENIUS Act), EU (MiCA), and Asian jurisdictions differ in regulating stablecoin liquidity?
- Which regulatory frameworks favor new stablecoin entrants vs incumbents?
- How are exchanges responding to regulatory fragmentation (dual listings, regional restrictions)?

**Strategic Context:**
- What policy debates are ongoing about stablecoin market concentration risks?
- How might future regulations address the USDT/USDC duopoly?
- What reforms could reduce barriers to entry for new stablecoin issuers?

Focus on: Regulatory frameworks, legislation, government policy documents, strategic plans, comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context.
```

---

**CLAUDE PROMPT (Manual - User will paste from claude.ai):**

```
Research stablecoin liquidity infrastructure, focusing on these synthesis questions that require multi-dimensional analysis:

1. What determines whether a new stablecoin achieves functional liquidity or fails despite technical soundness? Synthesize evidence across regulatory positioning, market maker relationships, exchange access, and DeFi integration.

2. How sustainable are current liquidity incentive models (liquidity mining, token rewards)? What happens when incentives end?

3. What is the relationship between multi-chain fragmentation and overall market efficiency? Does fragmenting liquidity across 20+ chains help or hurt end users?

4. How do network effects entrench USDT and USDC, and what would it take for a new entrant to compete?

5. What systemic risks exist from concentrated market making (only 6 USDT arbitrageurs vs 521 for USDC)?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

---

**GROK PROMPT (Manual - User will paste from x.com/i/grok):**

```
Research stablecoin liquidity and market making, focusing on these specific questions:

**Recent Developments (last 12 months):**
- What new market making partnerships have been announced for stablecoins in 2024-2025?
- Have any major market makers (Wintermute, Jump, DWF Labs) made news about stablecoin support?
- What bridge security incidents or cross-chain liquidity problems have occurred recently?

**Practitioner Perspectives:**
- What are traders and institutions saying about stablecoin liquidity on X/Twitter?
- Are there complaints about specific stablecoins' liquidity or exchange availability?
- What do market makers publicly discuss about challenges in the space?

**Real-Time Market Dynamics:**
- Are there current concerns about liquidity fragmentation across chains?
- What's the sentiment around newer stablecoins (PayPal USD, Ethena USDe) vs incumbents?
- Any discussions about exchange delisting or relisting of stablecoins due to MiCA/regulations?

Focus on: Recent news, industry discussions on X/Twitter, practitioner insights, real-time developments.
Provide findings with source links, publication dates, and credibility indicators.
```

---
