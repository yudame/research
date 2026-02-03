# Master Research Briefing: Stablecoin Series Ep. 8 - Post-Launch Operations

Date: 2026-02-02
For: podcast-synthesis-writer agent

---

## CROSS-VALIDATION MATRIX

### Critical Facts Verification

| Claim/Statistic | Perplexity | Claude | Gemini | GPT-R | Grok | Status |
|----------------|------------|--------|--------|-------|------|--------|
| Stablecoin transfer volume $27T+ (2024) | ✓ | - | - | - | - | ⚠️ SINGLE SOURCE |
| Circle USDC on 28-30 chains | - | ✓ | - | - | - | ⚠️ SINGLE SOURCE |
| Tether on 14+ chains (deprecating 5 legacy) | - | ✓ | - | - | - | ⚠️ SINGLE SOURCE |
| CCTP processed $110B across 5.3M transfers | - | ✓ | - | - | - | ⚠️ SINGLE SOURCE |
| Fireblocks processes $200B/month stablecoin txns | - | ✓ | - | - | - | ⚠️ SINGLE SOURCE |
| Tether ~150-235 employees, $93M profit/employee | - | ✓ | - | - | - | ⚠️ SINGLE SOURCE |
| Circle 815-1,200 employees, $263M personnel costs | - | ✓ (S-1) | - | - | - | ✅ VERIFIED (SEC filing) |
| Circle pays Coinbase $908M annually | - | ✓ (S-1) | - | - | - | ✅ VERIFIED (SEC filing) |
| $1-5B issuer needs 50-100 employees, $15-35M/yr | - | ✓ | - | - | - | ⚠️ ESTIMATE |
| GENIUS Act signed July 18, 2025 | ✓ | ✓ | ✓ | - | ✓ | ✅ VERIFIED |
| GENIUS effective Jan 2027 | ✓ | ✓ | ✓ | - | ✓ | ✅ VERIFIED |
| Monthly attestations required | ✓ | ✓ | ✓ | - | - | ✅ VERIFIED |
| $50B threshold for PCAOB annual audit | - | ✓ | ✓ | - | - | ✅ VERIFIED |
| Reserve assets: T-bills ≤93 days, cash, repos | ✓ | ✓ | ✓ | - | ✓ | ✅ VERIFIED |
| MiCA 30-60% bank deposit requirement | - | - | ✓ | - | - | ✅ VERIFIED (prior episodes) |
| Singapore MAS: redeem at par within 5 business days | - | ✓ | ✓ | - | - | ✅ VERIFIED |
| OCC approved 5 trust charters Dec 2025 | - | ✓ | - | - | ✓ | ✅ VERIFIED |
| Rain.xyz $250M Series C at $1.95B valuation | - | ✓ | - | - | - | ⚠️ SINGLE SOURCE |
| TRM Labs: 145% illicit crypto surge to $158B (2025) | - | - | - | - | ✓ | ⚠️ SINGLE SOURCE |
| PayPal: 40% U.S. merchants accept crypto | - | - | - | - | ✓ | ⚠️ SINGLE SOURCE |
| Chainalysis compliance: $30K-$100K/yr mid-tier | - | ✓ | - | ✓ | - | ✅ VERIFIED |
| $30M-$150M+ annual OpEx for scaled issuers | - | ✓ | - | ✓ | - | ✅ VERIFIED |
| Stripe stablecoin: US businesses only, USD settlement | - | - | - | ✓ | - | ✅ VERIFIED (Stripe docs) |
| USDT enforcement: continuous high-volume blacklists | - | - | - | ✓ | - | ⚠️ SINGLE SOURCE (AMLBot) |
| USDC enforcement: less frequent, legally constrained | - | - | - | ✓ | - | ⚠️ SINGLE SOURCE (AMLBot) |

### Coverage Analysis

| Topic | P | C | Ge | GPT | Gr | Coverage |
|-------|---|---|----|-----|----|----------|
| Continuous monitoring systems | ✓✓✓ | ✓ | - | ✓ | - | Strong |
| Incident response & pause mechanisms | ✓✓✓ | - | - | ✓ | - | Strong |
| Customer operations at scale | ✓✓ | ✓ | - | - | - | Moderate |
| Cross-chain management & CCTP | ✓✓ | ✓✓✓ | - | - | - | Strong |
| Attestation cycles & audit logistics | ✓✓ | ✓✓ | ✓✓ | - | - | Strong |
| Smart contract upgrades | ✓✓✓ | - | - | - | - | Moderate |
| AML/KYC/Transaction monitoring | ✓✓ | ✓ | - | ✓ | ✓✓ | Strong |
| Exchange & payment processor relationships | ✓✓ | ✓ | - | ✓✓ | ✓ | Strong |
| Profitability & cost structures | ✓✓ | ✓✓✓ | - | ✓✓ | - | Excellent |
| Vendor ecosystem | - | ✓✓✓ | - | ✓✓ | ✓ | Strong |
| Regulatory implementation timelines | ✓ | ✓✓ | ✓✓✓ | - | ✓✓ | Excellent |
| Yield-bearing stablecoin debates | ✓ | - | ✓✓✓ | - | - | Moderate |
| CBDC impact | - | - | ✓✓ | - | - | Limited |
| Enforcement operations (freeze/burn) | - | - | - | ✓✓✓ | ✓ | Strong |
| Practitioner complaints (real-time) | - | - | - | - | ✓✓✓ | Moderate |

**Legend:** P=Perplexity, C=Claude, Ge=Gemini, GPT=GPT-Researcher, Gr=Grok

---

## VERIFIED KEY FINDINGS

### 1. The Operational Economics of Running Money at Scale

**Main finding:** Operating a stablecoin at institutional scale costs $30M-$150M+ annually. Two viable models exist: Tether's lean automation (~150 employees for $115B) versus Circle's regulatory-first approach (~1,000+ employees for $60B).

**Evidence:**
- Tether: ~150-235 employees, ~$93M profit per employee annually — Source: Claude (Bridge Harris analysis) — Quality: Industry analysis
- Circle: 815-1,200 employees, $263M personnel costs, $292K average per employee — Source: Claude (Circle S-1 SEC filing) — Quality: Official SEC filing
- Circle distribution costs: $1.01B annually, with $908M paid to Coinbase — Source: Claude (S-1) — Quality: Official SEC filing
- $1-5B issuer benchmark: 50-100 employees, $15-35M annually — Source: Claude — Quality: Industry estimate
- Personnel breakdown for $1-5B issuer: 15-25 engineers, 5-10 compliance, 3-5 treasury, 5-10 support, 2-4 legal — Source: Claude — Quality: Industry estimate
- Compliance vendor subscriptions: $30K-$100K annually for mid-tier — Source: Claude, GPT-R — Quality: Multiple sources
- Node infrastructure: $1K-$5K/month basic, $7K-$30K+ enterprise — Source: Claude — Quality: Industry estimate

**Contradictions/Nuances:**
- Tether's lean model may reflect opacity rather than superior efficiency — staffing figures come from industry analysis, not Tether disclosures
- Circle's higher headcount reflects deliberate strategy for US bank charter and regulatory positioning, not inefficiency
- Compliance staffing varies dramatically: Circle has only 34 compliance staff for $60B (4% of headcount), indicating heavy automation

---

### 2. Continuous Monitoring: Four Layers of 24/7 Surveillance

**Main finding:** Institutional stablecoin operations require four interdependent monitoring layers operating 24/7: reserve composition tracking, transaction flow surveillance, counterparty health assessment, and systemic risk detection.

**Evidence:**
- Reserve monitoring: hourly reconciliation between on-chain issuance and off-chain reserve holdings — Source: Perplexity — Quality: Industry documentation
- Transaction monitoring: stablecoin transfer volumes exceeded $27T globally in 2024 — Source: Perplexity (Fireblocks report) — Quality: Industry report
- Counterparty monitoring: continuous real-time tracking of custodial partners (BNY Mellon, Customers Bank for Circle) — Source: Perplexity — Quality: Industry documentation
- Systemic risk: Fed research shows stablecoin deposit flows could create liquidity pressures on regional banks — Source: Perplexity — Quality: Federal Reserve research
- Stablecoin issuers now hold $127B+ in U.S. Treasury securities (17th largest global holder of US debt) — Source: Perplexity, Gemini — Quality: Multiple sources

**Source quality notes:**
- Perplexity provides the most detailed monitoring architecture taxonomy
- Real-time monitoring capabilities verified through regulatory requirements (GENIUS Act mandates technical freeze/seize capability)

---

### 3. The Vendor Ecosystem Has Matured Into Critical Infrastructure

**Main finding:** A specialized vendor ecosystem now supports institutional stablecoin operations, with Fireblocks (custody), Chainalysis/TRM Labs (compliance), and emerging players like Rain.xyz (payments) forming the operational backbone.

**Evidence:**

**Custody & Treasury:**
- Fireblocks: $200B monthly stablecoin transactions, 10-15% of global USDC/USDT volume — Source: Claude — Quality: Company disclosures
- Fireblocks-Circle strategic collaboration (September 2025) — Source: Claude (PR Newswire) — Quality: Official announcement
- Squads.xyz: secures $10B in value, $3B+ stablecoin transfers on Solana — Source: Claude — Quality: Company claims
- Cobo: MPC key management, compliance screening — Source: GPT-R (StablecoinInsider) — Quality: Industry report

**Compliance & Analytics:**
- Chainalysis: clients include Tether, Circle, Paxos; launched Sentinel for stablecoin issuers — Source: Claude — Quality: Company disclosures
- TRM Labs: clients include Circle, Uniswap, FBI, IRS — Source: Claude — Quality: Company disclosures
- Elliptic: clients include Revolut, Paysafe — Source: Claude — Quality: Company disclosures
- Enterprise pricing: $30K-$100K/yr for mid-tier, scaling with volume — Source: Claude, GPT-R — Quality: Industry estimates
- Compliance platform market is rapidly expanding due to regulatory scrutiny — Source: GPT-R (DataIntelo 2024) — Quality: Market research

**Payments Infrastructure:**
- Rain.xyz: $250M Series C (Jan 2026) at $1.95B valuation, $3B+ annualized volume, Visa Principal Member — Source: Claude — Quality: Company announcement
- Crossmint: built-in compliance (Elliptic AML, Persona KYC, NotaBene Travel Rule), powers MoneyGram USDC remittance — Source: Claude — Quality: Company disclosures
- Dakota: launched Jan 29, 2026 with embedded AML/KYB for stablecoin custody/orchestration — Source: Grok (PRNewswire) — Quality: Official announcement

**Key insight:** Vendor lock-in is strongest in compliance and custody layers, not payments UI — Source: GPT-R — Quality: Analysis

---

### 4. Multi-Chain Strategy: Native Issuance Over Bridges

**Main finding:** Circle's burn-and-mint Cross-Chain Transfer Protocol (CCTP) has become the operational gold standard, processing $110B across 5.3M transfers. Multi-chain expansion must be compliance-led, not growth-led.

**Evidence:**
- Circle: 28-30 blockchain networks, native USDC issuance — Source: Claude — Quality: Company disclosures
- Tether: 14+ chains, deprecating 5 legacy networks (Omni, BCH SLP, Kusama, EOS, Algorand) in September 2025 — Source: Claude — Quality: Company announcement
- Kusama deprecation rationale: just $250K remaining of $3.5M lifetime issuance, declining 2+ years — Source: Claude — Quality: Company announcement
- CCTP V2 (March 2025): standard transfers 13-19 minutes, fast transfers in seconds with fees — Source: Claude — Quality: Company documentation
- Bridge-to-native conversions: Linea (March 2025, first successful), Sonic (May 2025, 480M+ converted = 87% ecosystem circulation) — Source: Claude — Quality: Company documentation
- Treasury operations follow hub-and-spoke model: core reserves under strong governance, operating floats per chain — Source: Claude — Quality: Industry practice
- Technical requirements per chain: full/archive nodes, real-time monitoring, multisig wallets, gas estimation — Source: Claude — Quality: Industry practice

**Contradictions/Nuances:**
- GPT-R notes: "operationally safe" bridging is less about bridge brand and more about issuer containment capability (freeze, KYT, coordination)
- No "official safe bridge" lists published by major issuers
- AMLBot data shows USDT's continuous enforcement across chains vs. USDC's more legally constrained model

---

### 5. Minting and Redemption: The Two-Tier Reality

**Main finding:** Redemption SLAs vary dramatically by issuer and create a two-tier system where institutional access differs materially from retail access. The fundamental tension: 24/7 blockchain operations vs. traditional banking hours.

**Evidence:**

| Issuer | Minimum | Fees | Processing | Notes |
|--------|---------|------|------------|-------|
| Circle (Basic) | None stated | Free | 2 business days | Manual opt-in |
| Circle (Standard) | None stated | Free <$2M/day; 0.03-0.1% above | Near-instant | Tiered fee structure |
| Tether | $100,000 | $150 verification + 0.1% (min $1,000) | "Several days" | No specific SLA |
| Paxos (USDP/PYUSD) | None stated | Zero issuer fees | T+1 settlement | Fiat before 3pm EST |
| Gemini (GUSD) | None stated | Fee-free in platform | Not specified | ERC-20 only, ~$46M market cap |

- No issuer publishes penalties for missing timeframes — "commercially reasonable efforts" language — Source: Claude — Quality: Company documentation
- Fiat redemptions don't process on US/UK holidays or weekends (Paxos explicit) — Source: Claude — Quality: Company documentation
- Circle uses Customers Bank CBIT platform for 24/7 instant settlement — Source: Claude — Quality: Company documentation
- Visa launched USDC settlement December 2025 with 7-day settlement windows — Source: Claude — Quality: Company announcement

---

### 6. Monthly Attestation: The Operational Calendar That Governs Everything

**Main finding:** Monthly reserve attestation cycles have evolved from cryptocurrency-era "trust us" to banking-grade verification. The process involves complex multi-party coordination across chains, custodians, and auditors within tight deadlines.

**Evidence:**
- Monthly attestations required: independent registered public accounting firms verify 1:1 backing — Source: Perplexity, Claude, Gemini — Quality: Multiple sources (GENIUS Act text)
- Process: snapshot on-chain supply across all chains + simultaneous balance confirmations from all custodians — Source: Perplexity — Quality: Industry documentation
- Auditors independently query blockchains and contact custodians directly — Source: Perplexity — Quality: Industry documentation
- Typical cycle: 5-10 business days for fieldwork after month-end cutoff — Source: Perplexity — Quality: Industry estimate
- $50B+ issuers: annual PCAOB-audited GAAP financial statements — Source: Claude, Gemini — Quality: GENIUS Act text
- Monthly CEO/CFO certifications to primary regulators — Source: Claude — Quality: GENIUS Act text
- Some issuers conduct weekly or daily informal reserve checks between monthly attestations — Source: Perplexity — Quality: Industry practice
- AICPA 2025 Criteria for Stablecoin Reporting (March 6, 2025) established first standardized framework — Source: Perplexity — Quality: Official standard

---

### 7. Enforcement Operations: Two Models for Freezing and Seizing Tokens

**Main finding:** USDT and USDC operate fundamentally different enforcement models. Tether runs a high-throughput enforcement machine (continuous freeze → investigate → burn → reissue). Circle follows a lower-frequency, legally constrained model (freeze/unfreeze without reissue).

**Evidence:**
- USDT: continuous blacklist updates with large monthly volumes; supports burn-and-reissue mechanism — Source: GPT-R (AMLBot 2025 data) — Quality: Data-backed analysis
- USDT enforcement spikes: September and November 2025 exceeding $25-30M in destroyed tokens — Source: GPT-R — Quality: AMLBot data
- USDC: blacklist actions cluster around Oct-Nov 2024 and Mar-May 2025; no burn/reissue; judicially anchored — Source: GPT-R — Quality: AMLBot data
- GENIUS Act requires technical capability to freeze, seize, or burn tokens when legally required — Source: Perplexity, Gemini — Quality: Legislative text
- Operational implication: USDT model requires larger investigations/ops team; USDC model requires heavier legal/compliance review per action — Source: GPT-R — Quality: Analysis

**Key insight:** Different enforcement models create distinct staffing, legal, and controls implications — neither is "better," they are different operating models — Source: GPT-R

---

### 8. Incident Response: Pause Mechanisms and Operational Resilience

**Main finding:** Stablecoin operators maintain automated pause functionality that can halt minting, burning, and transfers within seconds. Governance safeguards prevent misuse while enabling rapid response.

**Evidence:**
- Emergency pause authority segregated from other administrative functions — Source: Perplexity — Quality: Industry documentation
- Multi-signature requirements: 2+ parties must independently authorize a pause — Source: Perplexity — Quality: Industry documentation
- Time delays: 1-72 hours depending on severity level — Source: Perplexity — Quality: Industry estimate
- Layered custody: reserves across multiple geographically distributed custodians with failover procedures — Source: Perplexity — Quality: Industry practice
- No major pause events or smart contract failures documented in Jan 2026 — Source: Grok — Quality: Real-time monitoring

**Practitioner perspective:**
- Issuers treat operational disruptions as "private market infrastructure events" communicated through partners rather than public postmortems — Source: GPT-R — Quality: Analysis
- This opacity increases counterparty due diligence burden for enterprises

---

### 9. Payment Processor Integration: Stripe as Reference Architecture

**Main finding:** Stripe's stablecoin payment integration demonstrates how processors abstract away all crypto complexity for merchants — redirecting wallet flow through crypto.stripe.com and settling in USD.

**Evidence:**
- Stripe: customer redirected to crypto.stripe.com to connect wallet and choose currency/network — Source: GPT-R (Stripe Docs) — Quality: Official documentation
- Settlement: funds settle in merchant's Stripe balance in USD — Source: GPT-R — Quality: Official documentation
- Scope: only US businesses can accept; customers can pay globally — Source: GPT-R — Quality: Official documentation
- Supported: USDC on Ethereum, Solana, Polygon, Base; USDP on Ethereum/Solana; USDG on Ethereum — Source: GPT-R — Quality: Official documentation
- Limitations: no disputes, manual capture not supported, refunds supported — Source: GPT-R — Quality: Official documentation
- PayPal: 40% of U.S. merchants now accept crypto (Jan 27, 2026) — Source: Grok (PayPal Newsroom) — Quality: Official report

**Key insight:** Stripe acts as orchestration, consumer UX, and settlement conversion layer — shifting operational burden entirely away from merchants and onto Stripe — Source: GPT-R

---

### 10. Regulatory Implementation Timeline: The January 2027 Countdown

**Main finding:** The GENIUS Act creates an 18-month implementation window with staggered deadlines. Industry leaders are already aggressively building compliance infrastructure.

**Evidence:**

**Timeline:**
- July 18, 2025: GENIUS Act signed into law — Source: All 5 sources — Quality: Official
- September 2025: Treasury ANPRM published — Source: Grok, Claude — Quality: Federal Register
- October 2025: ANPRM comment period closed — Source: Grok, Claude — Quality: Federal Register
- December 2025: FDIC application process issued; OCC approved 5 trust charters — Source: Claude, Grok — Quality: Official
- July 18, 2026: Deadline for federal regulators to issue final implementing rules — Source: Claude, Gemini — Quality: Legislative text
- January 18, 2027: Effective date (or 120 days after final rules) — Source: All sources — Quality: Legislative text

**Industry preparation:**
- Circle pursuing federal trust bank charter (conditionally approved Dec 2025 as "First National Digital Currency Bank") — Source: Claude — Quality: Company announcement
- OCC conditionally approved five trust charters: Circle, Ripple, Paxos, Fidelity Digital Assets, BitGo — Source: Claude, Grok — Quality: Official
- Applications pending: Coinbase, Crypto.com, Stripe (Bridge), Nubank — Source: Claude — Quality: Industry reporting
- Tether launched USAT (Jan 27, 2026) via Anchorage for GENIUS compliance — Source: Grok — Quality: Industry reporting

**Comparative jurisdictions:**
- EU MiCA: in force since June 30, 2024 for stablecoins — Source: Gemini — Quality: Official
- Singapore MAS: expected mid-2026, 5 business day redemption requirement — Source: Claude, Gemini — Quality: Official
- Hong Kong: stablecoin licenses from March 2026 — Source: Grok — Quality: Industry reporting

---

## RESEARCH GAPS & UNCERTAINTIES

- **Well-established:** Regulatory frameworks (GENIUS, MiCA, Singapore), operational cost ranges, vendor ecosystem players, attestation requirements, multi-chain strategies
- **Preliminary/Limited evidence:** Exact staffing numbers for non-Circle issuers, operational incident frequency, bridge safety assessments, precise vendor pricing
- **Unknown/Unstudied:** State certification criteria for sub-$10B GENIUS Act issuers, foreign stablecoin "substantially similar" determinations, CBDC operational impact on stablecoin business models

---

## SOURCE INVENTORY

### Tier 1 Sources (Official/Regulatory)
1. GENIUS Act legislative text — Congress.gov — https://www.congress.gov/bill/119th-congress/senate-bill/394/text
2. Circle S-1 SEC filing — SEC.gov — https://www.sec.gov/Archives/edgar/data/1876042/000119312525070481/d737521ds1.htm
3. Federal Register GENIUS Act Implementation — https://www.federalregister.gov/documents/2025/09/19/2025-18226/genius-act-implementation
4. MAS Singapore Stablecoin Framework — https://www.mas.gov.sg/news/media-releases/2023/mas-finalises-stablecoin-regulatory-framework
5. Stripe Stablecoin Payments Documentation — https://docs.stripe.com/payments/stablecoin-payments
6. AICPA 2025 Criteria for Stablecoin Reporting (March 2025) — Referenced in Perplexity

### Tier 2 Sources (Industry Analysis/Company Disclosures)
1. Fireblocks-Circle Strategic Collaboration — PRNewswire — https://www.prnewswire.com/news-releases/fireblocks-and-circle-strategically-collaborate-302550848.html
2. Rain.xyz $250M Series C — https://www.rain.xyz/resources/rain-raises-250m-series-c
3. AMLBot Stablecoin Freezes 2023-2025 — https://blog.amlbot.com/stablecoin-freezes-2023-2025-a-data-backed-analysis-of-usdt-vs-usdc-by-amlbot/
4. Latham & Watkins GENIUS Act Analysis — https://www.lw.com/en/insights/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us
5. Bridge Harris Tether profitability analysis — https://bridgeharris.substack.com/p/the-most-profitable-business-per
6. Tanay Jaipuria Circle S-1 breakdown — https://www.tanayj.com/p/circle-s-1-breakdown
7. DataIntelo Stablecoin Compliance Platforms Market — https://dataintelo.com/report/stablecoin-issuer-compliance-platforms-market/amp

### Tier 3 Sources (News/Practitioner)
1. TRM Labs Crypto Crime Report 2025 — via CoinDesk/Decrypt — Referenced in Grok
2. PayPal Newsroom on merchant crypto acceptance — https://newsroom.paypal-corp.com/2026-01-27-Crypto-Goes-Mainstream
3. Dakota platform launch — PRNewswire — https://www.prnewswire.com/news-releases/dakota-unveils-stablecoin-infrastructure-platform-302674011.html
4. Elliptic 2026 Regulatory Outlook — https://www.elliptic.co/blog/elliptics-2026-regulatory-and-policy-outlook-us-sets-the-pace

---

## PRACTITIONER PERSPECTIVES

- Daniel Mottice (@mottice, founder ModernTreasury, ex-Visa [HIGH]): stablecoins' "instant, global" promise falters at legacy rail interfaces, creating liquidity management complexities — Source: Grok
- Spicy (@spicyxbt [MED]): DeFi leader surveys identify KYC/AML verification as primary operational barrier — Source: Grok
- Multiple practitioners call for portable identity solutions to address repetitive KYC across applications — Source: Grok

---

## PUBLIC DISCOURSE (Opinion - NOT Evidence)

⚠️ **For podcast context only** — Use to contrast "what people believe" vs "what research shows"

### What X/Twitter Is Saying
- KYC/AML verification is the dominant complaint among practitioners
- Calls for portable identity solutions (idOS, reusable credentials)
- Concerns about GENIUS Act enabling freezes without victim returns (regulatory capture claims)
- Estimated $2-20B in annual slippage losses for retail in stablecoin pools
- Smaller issuers expressing frustration at steeper capital/audit demands vs. Circle/Tether

### Popular Misconceptions to Address
- **Belief:** Running a stablecoin is primarily a technical/engineering challenge
- **Reality:** Compliance, attestation, and banking relationships dominate operational costs and complexity
- **Podcast angle:** Show how the operational reality is closer to running a bank than running a software company

---

## NOTES FOR OPUS 4.5

**CRITICAL INSTRUCTION — DIFFERENTIATION FROM PREVIOUS EPISODES:**

This is Episode 8 in a series. Previous episodes already covered extensively:
- SVB crisis and its aftermath (Episode 5 central case study)
- GENIUS Act and MiCA regulatory framework details (Episodes 5, 6, 7)
- MakerDAO governance participation and power concentration (Episode 7)
- De-pegging events and market mechanics (Episode 6)
- Reserve composition debates (Episode 5)

**DO NOT REPEAT THESE STORIES.** If referencing them, use one sentence maximum and say "as we covered in earlier episodes."

**THIS EPISODE'S UNIQUE FOCUS must be operational — the day-to-day realities:**
- What does the operations center look like? (Monitoring, staffing, vendor stack)
- What does the monthly attestation calendar look like? (Logistics, coordination)
- How do multi-chain operations actually work? (CCTP, hub-and-spoke treasury)
- What does enforcement look like operationally? (USDT vs USDC models)
- What are the cost structures? (Circle S-1 data, $30-150M estimates)
- How do payment processors integrate? (Stripe's architecture)
- What are practitioners actually complaining about? (KYC burden, portable identity)

**Strongest evidence for:**
- Operational cost structures (Circle S-1 provides rare transparency)
- Vendor ecosystem maturity (multiple sources confirm key players)
- Multi-chain strategy (CCTP data, deprecation patterns)
- Enforcement model comparison (AMLBot data-backed analysis)
- Regulatory timeline (legislative text, multiple confirmations)

**Weaker evidence for:**
- Exact staffing at non-Circle issuers
- Operational incident frequency (issuers treat as private)
- Customer support metrics at scale
- Bridge safety assessments

**Interesting tensions/contradictions:**
- Tether's lean model ($93M/employee) vs Circle's heavy model (~$200K/employee) — both viable at scale
- Only 34 compliance staff at Circle for $60B — heavy automation or understaffed?
- "Instant, global" promise vs reality of banking hours and fiat settlement delays
- USDT's proactive enforcement vs USDC's legally constrained model
- No published SLA penalties — all "commercially reasonable efforts"

**Missing context:**
- No public incident postmortems from major issuers
- State certification criteria still undefined
- CBDC impact analysis is speculative
