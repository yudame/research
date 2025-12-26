# Prompts Used for Episode: Stablecoin Series: Ep. 4, Technical Architecture & Smart Contract Development

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** A `research-prompt.md` file exists in this directory containing the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-26
- Slug: episode-4-technical-architecture
- Title: Stablecoin Series: Ep. 4, Technical Architecture & Smart Contract Development
- Series: Stablecoin Series
- Episode Number: 4

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

**Prompt used (completed 2025-12-26):**

```
Research stablecoin technical architecture, smart contract security, and blockchain deployment practices.

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

**Key topics to cover:**
1. Blockchain selection for stablecoins - Ethereum, Solana, Polygon comparisons (transaction costs, finality, security properties, ecosystem effects)
2. Smart contract vulnerabilities in DeFi/stablecoins - reentrancy, oracle manipulation, access control flaws, bridge exploits
3. Security audit effectiveness - how often do audited contracts still get exploited? What methodologies catch critical vulnerabilities?
4. Major stablecoin exploits and bridge hacks - Poly Network, Wormhole, Nomad, others - root causes and financial losses
5. Formal verification and automated tools vs manual expert review - comparative effectiveness
6. Key management practices - multi-signature, HSMs, threshold signing schemes, ISO/IEC 27001 requirements
7. Upgrade mechanisms - proxy patterns, governance-controlled upgrades, immutability vs upgradeability trade-offs

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links.
```

**Result:** ~7,600 words saved to research/p2-perplexity.md

---

## Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?
- **Blockchain architecture comparison** - Ethereum modular vs Solana monolithic design extensively covered
- **OWASP Smart Contract Top 10** - Quantified losses by vulnerability type ($953.2M access control, $35.7M reentrancy, etc.)
- **Bridge exploits** - Poly Network, Wormhole, Nomad, Ronin detailed with attack mechanisms
- **MPC/threshold signing** - Key management practices well documented
- **Proxy patterns** - Transparent, UUPS, Beacon patterns explained
- **Regulatory frameworks** - GENIUS Act and MiCA mentioned but not deeply analyzed

### What gaps exist in the academic literature?
- **Audit firm comparisons** - No specific data on Trail of Bits vs OpenZeppelin vs Certik effectiveness
- **Bug bounty program effectiveness** - Mentioned but not quantified
- **Real deployment decisions** - How do actual stablecoin issuers (Circle, Tether) make technical choices?
- **Testnet vs mainnet deployment failures** - What goes wrong between testing and production?
- **Recovery rates** - Only Nomad's 19% recovery mentioned; what about others?

### What recent developments aren't covered?
- **2025 exploits and incidents** - Research focuses on 2022-2024 historical data
- **Emerging L2/L3 chains** - Base, Arbitrum, Optimism for stablecoin deployment
- **AI-assisted auditing tools** - New developments in automated security
- **Post-GENIUS Act technical requirements** - What technical mandates are coming?

### What contradictions or uncertainties need more sources?
- **Audit effectiveness** - "3x less losses" claim needs verification from other sources
- **Formal verification claims** - How often does formal verification actually prevent exploits?
- **Validator centralization concerns** - Solana validator distribution needs more analysis

### What industry/implementation questions arose?
- **Cost of comprehensive security** - What does it actually cost to properly secure a stablecoin?
- **Open-source implementations** - What can we learn from USDC/DAI code?
- **Multi-chain deployment strategies** - How do issuers manage security across 10+ chains?
- **Emergency response procedures** - What happens in the first 24 hours of an exploit?

### What policy/regulatory angles need investigation?
- **GENIUS Act technical requirements** - Specific mandates for reserve attestation, auditing
- **MiCA compliance infrastructure** - What technical systems are required for EU compliance?
- **AICPA stablecoin attestation criteria** - What do auditors actually verify?
- **State-by-state licensing requirements** - Technical implications of NY BitLicense, etc.

### What practitioner perspectives are missing?
- **Auditor insights** - What do Trail of Bits/OpenZeppelin see most often?
- **Incident responders** - What happens during a hack in real-time?
- **Smart contract developers** - What security patterns do they use daily?
- **Bug bounty hunters** - What vulnerabilities are they finding in 2025?

---

## Phase 3: Targeted Research Prompts

### GPT-RESEARCHER PROMPT (Automated - 6-20 min)

```
Research stablecoin smart contract security and deployment practices, focusing on these specific questions:

**Industry Analysis:**
- What are the actual costs of comprehensive security programs (audits, bug bounties, formal verification, monitoring)?
- How do different audit firms (Trail of Bits, OpenZeppelin, CertiK, Halborn) compare in methodology and track record?
- What percentage of audited stablecoins/DeFi protocols have still been exploited?

**Case Studies & Implementation:**
- How did Circle implement USDC security across 15+ blockchains? What went right/wrong?
- What can we learn from MakerDAO/DAI's security evolution over 5+ years?
- What multi-chain deployment strategies minimize bridge risk?

**Technical Details:**
- What testing methodologies (unit tests, fuzzing, testnets, mainnet canaries) are standard practice in 2025?
- How do emergency response and incident recovery typically work for major stablecoins?
- What specific security tools and libraries are most widely used (OpenZeppelin, Foundry, Slither)?

Focus on: Industry analyst reports, audit firm publications, case studies, GitHub repositories, security postmortems.
Provide comprehensive findings with citations, data sources, and comparative analysis.
```

---

### GEMINI PROMPT (Automated - 3-10 min)

```
Research stablecoin regulatory technical requirements, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- What specific technical mandates does the GENIUS Act impose (reserve attestation frequency, audit requirements, cybersecurity standards)?
- What are MiCA's technical requirements for e-money token issuers (reserve composition, segregation, redemption systems)?
- What AICPA criteria apply to stablecoin reserve attestations?

**Comparative Policy Analysis:**
- How do US vs EU vs Singapore vs Hong Kong technical requirements differ for stablecoin issuers?
- What blockchain selection or smart contract requirements are regulators beginning to mandate?
- How do reserve transparency requirements (Chainlink Proof of Reserve, third-party attestations) work?

**Strategic Context:**
- What technical infrastructure investments are stablecoin issuers making to meet 2025-2027 deadlines?
- What compliance technology providers (Chainalysis, TRM, Elliptic) are required for regulatory approval?
- How are regulators approaching multi-chain and cross-border stablecoin operations?

Focus on: Regulatory frameworks, legislation, government policy documents, compliance guidance, official attestation reports.
Provide findings with official source citations, effective dates, and policy context.
```

---

### CLAUDE PROMPT (Manual - User pastes from claude.ai)

```
Research stablecoin technical architecture and smart contract security, focusing on these questions that require multi-dimensional analysis:

1. How do the security trade-offs between Ethereum, Solana, and other chains (Polygon, Arbitrum, Base) actually affect stablecoin implementations in practice?

2. What is the relationship between audit investment levels and actual security outcomes? Does spending more on security (audits, bounties, formal verification) correlate with fewer exploits?

3. What lessons from the $2.8B in bridge hacks (Poly Network, Wormhole, Nomad, Ronin) should inform multi-chain stablecoin architecture decisions?

4. How do key management practices (MPC, multisig, HSMs) differ between major issuers (Circle, Tether, Paxos) and what trade-offs are they making?

5. What technical decisions are regulatory frameworks (GENIUS Act, MiCA) beginning to mandate, and how are issuers adapting their architecture?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
```

---

### GROK PROMPT (Manual - User pastes from x.com/i/grok)

```
Research stablecoin smart contract security and technical architecture, focusing on these specific questions:

**Recent Developments (last 12 months):**
- What major stablecoin or bridge exploits have occurred in 2024-2025? What were root causes?
- What new security tools, audit methodologies, or formal verification advances have emerged?
- How have Circle, Tether, and other issuers updated their technical practices recently?

**Practitioner Perspectives:**
- What are smart contract auditors and security researchers saying about current vulnerabilities on X/Twitter?
- What are developers discussing about secure stablecoin implementation patterns?
- What are bug bounty hunters finding and disclosing in 2025?

**Industry Trends:**
- Are there emerging L2/L3 chains that stablecoins are adopting? What security considerations apply?
- What AI-assisted security tools are gaining traction in smart contract auditing?
- What are the hot debates in stablecoin security (upgradeability vs immutability, centralization concerns)?

Focus on: Recent news, X/Twitter discussions, security researcher insights, developer community perspectives.
Provide findings with source links, publication dates, and credibility indicators.
```
