# Prompts Used for Episode: Stablecoin Series - Ep. 5, Reserve Management & Custody Infrastructure

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** A `research-prompt.md` exists in this directory containing the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-26
- Slug: episode-5-reserve-management
- Title: Stablecoin Series - Ep. 5, Reserve Management & Custody Infrastructure
- Series: Stablecoin Series (Episode 5 of 6)

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

**Using all 5 tools for comprehensive coverage**

### Deep Research Prompts (Copy-Paste Ready)

**IMPORTANT:** These prompts use single newlines only to prevent accidental partial submissions when pasting into Chrome-based tools.

---

### Phase 1: Perplexity Academic Research

**PERPLEXITY PROMPT (Automated via API - 30-120s):**

```
Research stablecoin reserve management, custody infrastructure, and attestation requirements including regulatory frameworks (GENIUS Act, MiCA, Singapore MAS), qualified custodian requirements, AICPA 2025 Criteria for Stablecoin Reporting, reserve composition (Treasuries vs commercial paper vs bank deposits), bankruptcy-remote structures, and crisis management case studies (Circle/SVB, Tether reserve changes).

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

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links covering: reserve asset requirements by jurisdiction, qualified custodian definitions, attestation vs audit differences, liquidity management practices, risk mitigation structures, and transparency standards.
```

**Status:** ✅ COMPLETE (2025-12-26 15:13)
**Output:** research/p2-perplexity.md (~7,933 words)

---

## Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?
- Reserve composition frameworks across jurisdictions (GENIUS Act 6 categories, MiCA 30% deposit rule, Singapore MAS 3-month maturity)
- Qualified custodian definitions and requirements (federal/state supervised vs credit institutions)
- Attestation vs audit distinctions (AICPA 2025 Criteria, monthly vs annual)
- Bankruptcy-remote structures and priority claims (GENIUS Act Section 11)
- Crisis case studies (SVB/USDC $3.3B exposure, Tether commercial paper evolution, Terra Luna collapse)
- Real-time proof of reserves mechanisms (APIs, on-chain verification)
- Yield-bearing wrapper tensions with interest prohibition

### What gaps exist in the academic literature?
- Actual compliance costs (custody fees, attestation costs, banking relationship costs)
- Practical implementation challenges for mid-sized issuers
- How issuers are actually implementing AICPA 2025 Criteria
- Specific examples of CUSIP-level transparency in current attestations
- Cost comparison of trust company vs non-trust structures

### What recent developments aren't covered?
- GENIUS Act signed July 18, 2025 - any early compliance examples?
- AICPA 2025 Criteria released March 2025 - adoption patterns
- MiCA effective December 30, 2024 - early enforcement actions
- Real-time proof of reserves implementations (Moore Hong Kong, The Network Firm)
- RLUSD launch and transparency practices

### What contradictions or uncertainties need more sources?
- Whether 93-day maturity constraint is sufficient vs too restrictive
- Yield-bearing wrapper loopholes vs intended prohibition
- Priority claims framework workability in actual bankruptcy
- Cross-border regulatory arbitrage risks

### What industry/implementation questions arose?
- What do custody relationships actually cost at scale?
- How are issuers structuring multi-custodian arrangements?
- What does SOC 2 Type II certification cost and require?
- How do smaller issuers afford compliance?

### What policy/regulatory angles need investigation?
- How are state vs federal pathways being chosen under GENIUS Act?
- What's the European enforcement approach under MiCA?
- Singapore MAS framework expected mid-2026 - any preview guidance?

### What practitioner perspectives are missing?
- How do custody providers view the new requirements?
- What are auditors saying about AICPA criteria adoption?
- How are DeFi protocols adjusting to regulatory pressure?

---

## Phase 3: Targeted Followup Research Prompts

### GPT-RESEARCHER PROMPT (Automated - 6-20 min):

```
Research stablecoin reserve management and custody infrastructure implementation, focusing on these specific questions:

**Industry Analysis:**
- What are the actual costs of maintaining qualified custody relationships at scale (custody fees, insurance, operational overhead)?
- How are different issuers structuring multi-custodian arrangements to reduce concentration risk?
- What business models work for smaller stablecoin issuers facing high compliance costs?

**Case Studies & Implementation:**
- How is Circle implementing GENIUS Act compliance and AICPA 2025 Criteria reporting?
- What does Ripple's RLUSD transparency reporting include (CUSIP-level detail, real-time dashboards)?
- How are trust company issuers (Paxos, GUSD) structuring bankruptcy-remote reserves?
- What happened operationally when Circle faced SVB's failure - timeline, decision-making, recovery?

**Technical Implementation:**
- How do real-time proof of reserves systems work (APIs, data feeds, reconciliation frequency)?
- What SOC 2 Type II controls are required for institutional-grade custody?
- How are multi-signature custody arrangements implemented for stablecoin reserves?

Focus on: Industry reports, case studies, technical documentation, cost benchmarks, and implementation guides.
Provide comprehensive findings with citations, data sources, and comparative analysis.
```

---

### GEMINI PROMPT (Automated - 3-10 min):

```
Research stablecoin reserve management regulatory frameworks and policy implementation, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- What specific asset categories does GENIUS Act Section permit, and what are the exact maturity constraints?
- How does MiCA's 30% deposit requirement interact with custody segregation rules?
- What does Singapore MAS's framework require for overseas custodian creditworthiness (A- rating)?

**Comparative Policy Analysis:**
- How do GENIUS Act, MiCA, and Singapore MAS reserve requirements compare in practice?
- What regulatory arbitrage risks exist between jurisdictions?
- How are state regulators in the US approaching GENIUS Act equivalence?

**Strategic Context:**
- What early enforcement actions or compliance guidance have regulators issued under MiCA?
- How are policymakers viewing the tension between yield-bearing wrappers and interest prohibition?
- What international coordination exists on stablecoin reserve standards (CPMI-IOSCO, FSB)?

Focus on: Regulatory frameworks, official guidance documents, policy analysis, comparative jurisdiction studies.
Provide findings with official source citations, effective dates, and policy context.
```

---

### CLAUDE PROMPT (Manual - User pastes from claude.ai):

```
Research stablecoin reserve management and custody infrastructure, focusing on these specific questions:

- How do bankruptcy-remote trust structures actually protect stablecoin holders, and what are the legal mechanisms (trust beneficiary status, estate exclusion, priority claims)?
- What is the practical difference between attestations and full audits for stablecoin reserves, and what do the AICPA 2025 Criteria specifically require?
- How did Circle's SVB crisis unfold operationally, and what lessons does it teach about reserve concentration vs. diversification?
- What tensions exist between GENIUS Act's interest prohibition and the proliferation of yield-bearing stablecoin wrappers?
- How do real-time proof of reserves mechanisms work technically, and what are their limitations?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

---

### GROK PROMPT (Manual - User pastes from x.com/i/grok):

```
Research stablecoin reserve management and custody infrastructure, focusing on these specific questions:

**Recent Developments (last 12 months):**
- How are stablecoin issuers responding to GENIUS Act passage (July 2025)? Any early compliance announcements?
- What's happening with AICPA 2025 Criteria adoption since March 2025 release?
- How is MiCA enforcement progressing since December 2024 effectiveness?
- Any new real-time proof of reserves implementations or announcements?

**Practitioner Perspectives:**
- What are custody providers (Fireblocks, Anchorage, BitGo) saying about new regulatory requirements?
- How are auditors (Deloitte, KPMG, smaller CPA firms) approaching stablecoin attestations?
- What's the industry sentiment on compliance costs and competitive impact?

**Regional/Market Insights:**
- How are Asian markets (Singapore, Hong Kong, Japan) approaching reserve requirements?
- What's happening with RLUSD, PYUSD, and other newer stablecoins on transparency?
- Any recent crisis events or near-misses affecting reserve confidence?

Focus on: Recent news, X/Twitter discussions, practitioner insights, regional developments.
Provide findings with source links, publication dates, and credibility indicators.
```

---

## Cover Art Generation Phase

**Date:** 2025-12-26

**Tool Used:** Gemini 3 Pro Image via OpenRouter

**Generation Method:** --auto from report.md

**Auto-Generated Prompt (from report.md opening):**
```
Modern podcast episode cover art for "Episode 5 Reserve Management":

Style: Clean, professional, abstract visualization
Layout: Bold visual elements suitable for square format
Color palette: Light warm cream/off-white (#F5F1E8) background with black (#000000) and warm salmon/coral (#E8B4A8) accents
Concept: On Friday, March 10, 2023, at 11:37 AM Eastern, regulators shut down Silicon Valley Bank. Within hours, Circle disclosed that $3.3 billion of USDC reserves---roughly 8% of the stablecoin's backing...
```

**Branding Applied:**
- Logo: Yudame logo (top-left, vertically centered with brand text)
- Brand: Yudame Research (Playfair Display SemiBold)
- Series: Stablecoin Series (Playfair Display Italic)
- Episode: Ep 5 - Reserve Management (Playfair Display Italic)

**Output:** cover.png (1.1MB, 1024x1024px)
