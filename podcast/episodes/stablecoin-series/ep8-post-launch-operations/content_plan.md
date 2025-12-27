# Episode Plan: Stablecoin Series Ep. 8 - Post-Launch Operations & Continuous Compliance

## Episode Metadata
- **Series:** Stablecoin Series
- **Position:** Closer (Episode 8 of 8)
- **Core Question:** What does it take to operate a stablecoin at scale, and how do projects maintain stability, security, and regulatory compliance over time?
- **Episode Type:** Major conflict (governance models contested) + Balanced (regulatory frameworks + case studies)

## Toolkit Selections
- **Hook Type:** Stakes Establishment (SVB crisis as immediate, high-stakes opener)
- **Takeaway Structure:** Tiered Recommendations (safety hierarchy depends on access tier and issuer)
- **Contradiction Handling:** Substantive conflict (centralized vs decentralized governance, US vs EU regulatory approaches)

---

## NotebookLM Guidance

### Opening Instructions
Open with the March 11, 2023 Saturday morning scene: Circle discloses $3.3 billion frozen at Silicon Valley Bank. USDC falls to $0.86. MakerDAO's emergency vote passes in 2 hours with 88,767 MKR in favor—but the 48-hour security delay means nothing can execute until Monday. By then, the crisis resolved through federal intervention, not protocol mechanisms. This weekend exposed the fundamental truth: all governance models ultimately depended on the same thing—traditional government backstops.

Tone: Investigative, data-driven, intellectually honest about limitations. This is the series closer—synthesize what we've learned about stablecoin operations.

### Key Terms to Define
| Term | Definition | Pronunciation |
|------|------------|---------------|
| GENIUS Act | Guiding and Establishing National Innovation for U.S. Stablecoins Act, signed July 18, 2025, effective January 2027. Creates federal framework for stablecoin regulation requiring 100% reserves in high-quality liquid assets. | "genius act" |
| MiCA | Markets in Crypto-Assets Regulation—the EU's comprehensive crypto framework effective December 2024, requiring 60% of significant stablecoin reserves in bank deposits. | "my-kah" |
| Peg Stability Module (PSM) | MakerDAO mechanism allowing 1:1 exchanges between DAI and other stablecoins like USDC, which transmitted SVB contagion to DAI. | "P-S-M" |
| Travel Rule | FATF Recommendation 16 requiring identity information sharing for crypto transfers, with thresholds varying from $3,000 (US) to zero (EU, Korea). | |
| Gini coefficient | Measure of inequality from 0 to 1, where 1 means one person holds everything. MakerDAO governance averages 0.84—approaching plutocracy. | "jee-nee" |
| Flash loan attack | Borrowing massive funds, executing an attack, and repaying within a single transaction. Beanstalk lost $182 million in 13 seconds. | |
| Wind-down playbook | Required emergency plan for orderly stablecoin redemption if issuer fails. GENIUS Act mandates tested playbooks. | |

### Studies to Emphasize
1. **Federal Reserve FEDS Notes, "In the Shadow of Bank Runs" (December 2024)** - Authoritative analysis of SVB crisis impact on stablecoins
   - Finding: MakerDAO's security delays prevented timely response; PSMs "served to weaken Dai's own collateral pool"
   - Why it matters: Official Fed analysis of stablecoin vulnerabilities

2. **Fudan University DAO Governance Research (2025)** - Academic study of voting power concentration
   - Finding: Cross-protocol average participation is only 6.3%; top 1% hold 83.2% of tokens
   - Sample: Multiple DAOs including Compound, Uniswap, ENS

3. **arXiv MakerDAO Analysis (2022)** - Governance concentration study
   - Finding: Gini coefficient of 0.8438; largest voter averaged 52.66% of voting power
   - Sample: 638 governance polls

4. **Financial Stability Board Thematic Review (October 2025)** - Global regulatory gaps
   - Finding: "Significant gaps and inconsistencies" in implementing stablecoin recommendations
   - Why it matters: Official acknowledgment that regulatory arbitrage persists

### Narrative Arc

**Section 1: Foundation - The Operational Reality**
- Primary focus: Scale and regulatory transformation
- Key context: $180B+ in circulation, daily volumes exceeding card networks
- GENIUS Act vs MiCA: Opposite approaches to reserve composition (Treasuries vs bank deposits)
- Travel Rule fragmentation table: US $3,000 vs EU zero threshold
- Analogy: "Running a stablecoin is like operating a bank that never closes, across 30 different jurisdictions, each with different rules"
- Transition hook: "But what happens when the system faces its first real stress test?"

**Section 2: Evidence - Crisis Reveals Governance Reality**
- Evidence cluster A: SVB crisis comparing three models (Circle, MakerDAO, Tether)
  - Circle: Fast communication but insufficient capital ($340K equity vs $3.3B exposure)
  - MakerDAO: Fast vote but 48-hour execution delay
  - Tether: Geographic diversification, not superior management
  - All three depended on federal intervention

- Evidence cluster B: Governance concentration data
  - 6-35% participation rates
  - 0.84 Gini coefficient
  - "While 122 persons have voted, only one matters"

- Evidence cluster C: Governance attacks
  - Beanstalk: $1B flash loan → $182M drained in 13 seconds
  - Compound Golden Boys: $24M allocation with only 57 voters
  - Build Finance: Complete takeover via Discord bot manipulation

- Evidence cluster D: De-pegging hierarchy
  - USDe recovered (transparent reserves, working redemption)
  - USDX collapsed (opaque reserves, fire-sale pattern)
  - Terra/UST destroyed $40-60B

- Callback opportunity: "Remember the 48-hour delay that prevented MakerDAO from responding? This tension between security and speed remains unsolved."

**Section 3: Application - What Operational Maturity Requires**
- Protocol 1: Governance reform requirements
  - 48-72 hour minimum voting periods
  - 7+ day token lockup before voting power activates
  - Quadratic voting or delegation mechanisms
  - Target: Prevent flash loan attacks

- Protocol 2: Banking diversification
  - Multiple GSIB relationships across jurisdictions
  - Avoid crypto-specialized banks (Silvergate, Signature failed)
  - Contingency settlement arrangements
  - Target: Prevent SVB-type concentration risk

- Protocol 3: User risk evaluation hierarchy
  - Tier 1: Fiat-backed with transparent attestations + direct redemption (USDC)
  - Tier 2: Fiat-backed with less transparency (USDT)
  - Tier 3: Synthetic with transparent reserves (USDe)
  - Tier 4: Synthetic with opaque reserves (avoid)

- Caveats: Wind-down provisions untested; Tether reserves incompletely disclosed; cross-border coordination underdeveloped

### Closing Instructions
- Callback to opening: "We opened with that March 11 Saturday morning when USDC fell to 86 cents. What saved it wasn't Circle's crisis management or MakerDAO's emergency vote—it was a Sunday evening press release from the Treasury, Fed, and FDIC. The $180 billion stablecoin ecosystem, for all its technological sophistication, remained tethered to traditional financial infrastructure."
- Key takeaway: "Operational maturity means accepting this dependency while building redundancy—multiple banking partners, tested wind-down plans, transparent reserves, and governance mechanisms that balance security with crisis response speed."
- Series wrap: "This concludes our eight-part series on stablecoins. From market evolution to legal compliance, token economics to technical architecture, reserve management to liquidity partnerships, go-to-market strategy to post-launch operations—we've traced the complete lifecycle. The core insight across all eight episodes: stablecoins that survive are those that build institutional-grade infrastructure while maintaining transparency about their actual dependencies."
- Sign-off: "Find the full research and sources at research dot yuda dot me—that's Y-U-D-A dot M-E."

---

## Specificity Standards

The hosts should use specific parameters throughout:

| Category | Vague (Avoid) | Specific (Use) |
|----------|---------------|----------------|
| Thresholds | "different by region" | "$3,000 in US, zero in EU and Korea" |
| Concentrations | "very concentrated" | "Gini coefficient of 0.84—the top voter averaged 52% of voting power" |
| Timelines | "soon" | "GENIUS Act effective January 18, 2027; rulemaking deadline July 18, 2026" |
| Losses | "significant attack" | "$182 million drained in 13 seconds via Beanstalk flash loan" |
| Participation | "low turnout" | "average 24.59 voters per poll across 638 MakerDAO governance votes" |
| De-peg events | "fell significantly" | "USDC reached $0.86; USDe hit $0.65; USX collapsed to $0.10" |

---

## Attention Maintenance Notes

Remind hosts to:
- Rotate content types every 5-7 minutes (regulation → crisis case study → governance data → attacks → recommendations)
- Use pattern interrupts every 7-10 minutes (tables, attack timelines, hierarchy lists)
- Signpost major transitions ("Now let's look at what the crisis actually revealed...", "This brings us to the governance reality...")
- Close open loops before episode end (SVB resolution, Beanstalk aftermath, what happened to USDX)
- As series closer, reference earlier episodes: "As we discussed in our reserve management episode...", "The legal compliance frameworks we covered in episode two..."
