# Stablecoin Build & Launch Series

An 8-part podcast series exploring the end-to-end journey of building and launching a stablecoin, from market context and regulatory requirements through technical development, reserve management, and post-launch operations.

## Series Overview

This series examines what it actually takes to create a successful stablecoin in 2025—beyond the technical mechanics to the strategic, regulatory, operational, and market realities. With stablecoins surpassing $208 billion in market capitalization and projected to reach $2.8 trillion by 2028, new entrants face both tremendous opportunity and formidable challenges.

The series is grounded in evidence from real-world successes and failures: Tether's controversial rise to dominance, USDC's compliance-driven growth, Terra/UST's catastrophic collapse, and the 2025 regulatory watershed marked by the US GENIUS Act and EU MiCA regulation.

While examples draw from US and Asian contexts, the episodes focus on universal principles applicable to any jurisdiction. The goal is not to prescribe a single path, but to equip listeners with the knowledge to make informed decisions based on their specific goals, resources, and regulatory environment.

## Episode Structure

### Episode 1: "Stablecoin Market Evolution (2017-2025)" (Published)
**Status:** Published (2025-11-19)

**Focus:** Historical context, market dynamics, and lessons learned from eight years of stablecoin innovation and failure

**Key Topics:**
- Market growth from $4B (2020) to $280B+ (2025)
- Tether's controversial path to dominance (reserve scandals, regulatory fines, de-pegging events)
- USDC's compliance-first strategy vs. Tether's opacity
- Terra/UST's rise and catastrophic collapse (from $10B to zero in days)
- DeFi explosion and stablecoin composability
- 2022 crisis: de-pegging events, regulatory enforcement, market consolidation
- SVB banking crisis impact on Circle and USDC reserves
- Emergence of yield-bearing and algorithmic models

**Why This Episode First:**
Establishes the market context, demonstrates what has worked (and failed), and provides historical grounding for understanding current regulatory responses and design choices.

**Episode Link:** `/podcast/episodes/stablecoin-series/episode-1-market-evolution/`

---

### Episode 2: "Legal & Regulatory Compliance (GENIUS Act & MiCA)" (Published)
**Status:** Published (2025-11-26)

**Focus:** When and how global regulations apply, and what compliance actually requires

**Key Topics:**
- GENIUS Act (US, July 2025): reserve requirements, custody rules, monthly attestations
- MiCA (EU, June 2024): asset segregation, transaction caps, no equivalence regime
- Jurisdictional triggers (serving US/EU users, exchange listings, reserve locations)
- Reserve composition mandates (cash, treasuries, prohibited assets)
- Attestation vs. audit requirements and AICPA 2025 criteria
- Qualified custodian requirements
- Cross-border compliance challenges for Asian issuers
- Enforcement examples (Tether delisting in Europe, NYDFS actions)

**Why This Episode Second:**
After understanding market history, this establishes the regulatory baseline that shapes all subsequent design, operational, and strategic decisions.

**Episode Link:** `/podcast/episodes/stablecoin-series/episode-2-legal-compliance/`

---

### Episode 3: "Token Economic Design & Stabilization Mechanisms"
**Focus:** How stablecoins maintain price stability and what economic models prove sustainable

**Core Research Questions:**
- What collateralization models exist (fiat-backed, crypto-collateralized, algorithmic, hybrid) and how do they compare empirically?
- How do stabilization mechanisms work (arbitrage, algorithmic minting/burning, interest rates) and under what conditions do they fail?
- What does Terra/UST's collapse reveal about algorithmic stability limits?
- How do governance structures and monetary policy affect long-term sustainability?
- What is the difference between genuine value creation and subsidy-driven growth (Anchor Protocol's 20% APY)?
- How have different models performed during market stress (March 2020, May 2022, March 2023)?

**Why This Episode Third:**
With regulatory constraints understood, this explores the fundamental economic architecture choices that determine whether a stablecoin can actually maintain its peg and operate sustainably.

---

### Episode 4: "Technical Architecture & Smart Contract Development"
**Focus:** Critical technical decisions and security requirements for robust implementation

**Core Research Questions:**
- Which blockchain platforms (Ethereum, Solana, Polygon) offer the best balance of security, cost, speed, and ecosystem compatibility?
- What smart contract design patterns have proven secure vs. vulnerable to exploits?
- How effective are security audits and formal verification at preventing exploits?
- What key management practices meet ISO/IEC 27001 standards?
- How do projects balance upgradeability (fixing bugs) with immutability (preventing malicious changes)?
- What does historical exploit data reveal about common vulnerabilities?
- How do multi-chain deployments affect security and bridge risk?

**Why This Episode Fourth:**
After economic design, this addresses the technical implementation that brings the economic model to life while managing security risks that have caused hundreds of millions in losses.

---

### Episode 5: "Reserve Management & Custody Infrastructure"
**Focus:** Safely holding and managing backing assets while meeting regulatory standards

**Core Research Questions:**
- What reserve compositions meet regulatory requirements while maintaining liquidity?
- How do qualified custody arrangements work and what do they cost?
- What attestation and audit processes are required (GENIUS Act monthly attestations, AICPA 2025 criteria)?
- How do projects manage liquidity (redemption capability) vs. yield generation?
- How did Circle handle the Silicon Valley Bank crisis with $3.3B trapped reserves?
- What bankruptcy-remote structures protect user assets from issuer insolvency?
- How transparent should reserve reporting be, and what do major stablecoins actually disclose?

**Why This Episode Fifth:**
Technical implementation must be backed by actual reserves. This explores how to structure, secure, and report on the assets that underpin stablecoin value and user trust.

---

### Episode 6: "Market Making, Liquidity & Exchange Partnerships"
**Focus:** Ensuring the stablecoin is actually usable and tradable

**Core Research Questions:**
- What do market makers provide and what do partnerships cost?
- What do major exchanges (Coinbase, Binance, Kraken) require before listing a stablecoin?
- How do primary market (direct redemption) vs. secondary market (exchange trading) dynamics work?
- What role do DEXs and liquidity pools play vs. centralized exchanges?
- How does multi-chain deployment create liquidity fragmentation challenges?
- How did USDC overcome Tether's network effects to become second-largest stablecoin?
- What minimum liquidity thresholds are required for functional markets?

**Why This Episode Sixth:**
A technically sound, well-reserved stablecoin is worthless if users can't access it. This explores the infrastructure required to make theoretical stability into practical usability.

---

### Episode 7: "Go-to-Market Strategy & User Adoption"
**Focus:** Driving actual usage in a market dominated by incumbents

**Core Research Questions:**
- Which use cases drive adoption (B2B payments, remittances, DeFi, consumer transactions)?
- What does 2025 data show about primary drivers: speed (48% cite real-time settlement) vs. cost?
- How do payment network integrations (Visa, Mastercard) accelerate adoption?
- What UX improvements are necessary to reach mainstream users (wallet addresses, key management)?
- How do regulatory positioning and compliance affect trust and market access?
- Which geographic markets show fastest growth (Latin America 71% using stablecoins for cross-border payments)?
- How do projects overcome USDT/USDC network effects?
- What role do incentives play vs. organic utility-driven adoption?

**Why This Episode Seventh:**
After building a functional, liquid stablecoin, this addresses the go-to-market challenge of driving adoption against entrenched competitors with powerful network effects.

---

### Episode 8: "Post-Launch Operations & Continuous Compliance"
**Focus:** Operating at scale, maintaining stability, and evolving with regulations

**Core Research Questions:**
- What operational infrastructure is required to run a compliant stablecoin at scale?
- How much do ongoing compliance, custody, and operational costs total?
- How do projects respond to de-pegging events, security incidents, and crises?
- What governance structures enable protocol evolution while preventing abuse?
- How have major stablecoins handled incidents (Circle during SVB, Tether during bank runs)?
- What monitoring and transparency practices maintain user trust?
- How do operational costs scale with stablecoin supply growth?
- What does long-term sustainability look like without subsidies or speculative growth?

**Why This Episode Last:**
Launching is one challenge; operating successfully over time is another. This explores the ongoing operational realities that separate lasting success from projects that fade or fail.

---

## Series Narrative Arc

1. **Market Context** → Eight years of innovation, failure, and lessons learned establish the landscape
2. **Regulatory Foundation** → GENIUS Act and MiCA set the compliance baseline for global operation
3. **Economic Design** → Collateralization and stabilization mechanisms determine peg resilience
4. **Technical Implementation** → Smart contracts and security practices bring economics to life safely
5. **Reserve Operations** → Asset management and custody infrastructure back the token with real value
6. **Market Infrastructure** → Liquidity and exchange access make the stablecoin functionally usable
7. **User Adoption** → Go-to-market strategies overcome network effects and drive real usage
8. **Sustained Operations** → Long-term operational maturity, governance, and crisis response

## Key Strategic Themes

- **Regulatory compliance as foundation:** GENIUS Act and MiCA set minimum viability standards for global operation
- **Evidence over theory:** Analyzing what has worked (USDC transparency) vs. failed (Terra/UST algorithmic model)
- **Economic sustainability:** Distinguishing genuine value creation from subsidy-driven Ponzi dynamics
- **Security as existential risk:** Smart contract vulnerabilities and custody failures can destroy projects overnight
- **Network effects as moat:** Understanding how USDT/USDC dominance creates barriers to entry
- **Operational maturity:** Post-launch operations determine long-term success beyond initial excitement
- **Transparency and trust:** How reserve reporting and governance practices maintain or erode confidence
- **Global regulatory convergence:** How US and EU frameworks are shaping global standards

## Research Methodology Principles

All episodes follow rigorous research standards:
- **Prioritize empirical evidence** over theoretical models
- **Analyze actual market data** (transaction volumes, peg stability, adoption metrics)
- **Study both successes and failures** (USDC growth vs. Terra collapse)
- **Distinguish correlation from causation** in market dynamics
- **Report effect sizes and practical significance** (specific peg deviations, actual costs)
- **Compare individual cases against broader patterns** (is this one failure or a systemic issue?)
- **Identify preliminary vs. well-replicated findings** (new models vs. proven approaches)
- **Note conflicts of interest** (issuer claims vs. independent analysis)
- **Include contradictory evidence and uncertainties**
- **Cite specific sources** (regulatory texts, attestation reports, academic research)

## Key Questions the Series Answers

1. **Is it feasible to launch a new stablecoin in 2025?** What resources, partnerships, and capabilities are truly required?
2. **What regulatory approvals are mandatory vs. optional?** How do you navigate US, EU, and Asian requirements?
3. **Which economic model should you choose?** What does evidence show about fiat-backed vs. crypto-collateralized vs. algorithmic?
4. **What does compliance actually cost?** Custody fees, audits, attestations, legal, engineering—realistic numbers.
5. **How do you overcome incumbent network effects?** What strategies have worked for USDC, PayPal PYUSD, and others?
6. **What are the critical failure modes?** Smart contract bugs, reserve mismanagement, de-pegging spirals, regulatory enforcement.
7. **What scale is required for sustainability?** At what point do economics make sense without subsidies?
8. **How do you maintain trust long-term?** Transparency, governance, incident response, and operational excellence.

## Target Audience

- Fintech executives and entrepreneurs considering stablecoin launches
- Cryptocurrency projects adding payment functionality
- Financial institutions exploring digital asset strategies
- Regulators and policy makers understanding stablecoin ecosystems
- Investors evaluating stablecoin projects and risks
- Developers and technical architects building payment infrastructure
- Business strategists analyzing the $200B+ stablecoin market

## Research Sources (Series-Wide)

**Regulatory Documents:**
- [GENIUS Act Full Text](https://www.congress.gov/bill/119th-congress/senate-bill/1789) (US stablecoin regulation, July 2025)
- [MiCA Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1114) (EU Markets in Crypto-Assets)
- [AICPA 2025 Criteria for Stablecoin Reporting](https://www.aicpa.org/)
- Singapore MAS Stablecoin Framework
- UK FCA Stablecoin Proposals (CP25-14, CP25-15)

**Market Research & Data:**
- [Fireblocks State of Stablecoins 2025](https://www.fireblocks.com/report/state-of-stablecoins)
- [Artemis Stablecoin Payments Report 2025](https://reports.artemisanalytics.com/stablecoins/)
- CoinMarketCap, CoinGecko (market data)
- On-chain analytics (transaction volumes, unique addresses)

**Security & Technical:**
- [Smart Contract Audit Reports](https://www.certora.com/) (Trail of Bits, OpenZeppelin, Certora)
- [Blockchain Network Performance Benchmarks](https://www.blockchain.com/)
- Security incident databases and post-mortems

**Reserve Attestations:**
- [Circle USDC Reserve Reports](https://www.circle.com/en/usdc) (monthly)
- [Tether Transparency Reports](https://tether.to/en/transparency/) (quarterly)
- Paxos, Gemini, and other issuer attestations

**Academic & Policy Research:**
- Bank for International Settlements (BIS) stablecoin research
- Federal Reserve, ECB, and central bank publications
- Academic papers on stablecoin stability mechanisms and risks

**Case Studies:**
- Terra/UST collapse analysis
- Silicon Valley Bank impact on Circle/USDC
- Tether reserve controversies and regulatory settlements
- USDC market entry and growth strategy

---

## Series Status

- **Episodes 1-2:** Published
- **Episodes 3-8:** Research prompts created, ready for deep research phase

## Next Steps

For each unpublished episode:
1. Conduct deep research following the research-prompt.md methodology
2. Compile sources and research results
3. Draft comprehensive report
4. Create NotebookLM audio with chapters
5. Transcribe and publish

---

*Last Updated: 2025-12-05*
