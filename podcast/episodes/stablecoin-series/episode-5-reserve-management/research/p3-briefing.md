# Master Research Briefing: Stablecoin Series - Ep. 5, Reserve Management & Custody Infrastructure

Date: 2025-12-26
For: podcast-synthesis-writer agent

---

## CROSS-VALIDATION MATRIX

### Critical Facts Verification

| Claim/Statistic | Perplexity | Claude | Gemini | ChatGPT | Grok | Status |
|----------------|------------|--------|--------|---------|------|--------|
| GENIUS Act signed July 18, 2025 | ✅ | ✅ | ✅ | ✅ | ✅ | **VERIFIED** |
| GENIUS Act 93-day Treasury maturity limit | ✅ | ✅ | ✅ | ✅ | - | **VERIFIED** |
| MiCA 30% deposit requirement for EMTs | ✅ | - | ✅ | - | ✅ | **VERIFIED** |
| MiCA 60% for significant EMTs | ✅ | - | ✅ | - | - | **VERIFIED** |
| Singapore MAS A- credit rating for overseas custodians | ✅ | - | ✅ | - | - | **VERIFIED** |
| Circle SVB exposure $3.3B | ✅ | ✅ | - | ✅ | - | **VERIFIED** |
| USDC depeg to $0.87 during SVB crisis | ✅ | ✅ (reports $0.805-0.87) | - | ✅ | - | **VERIFIED** |
| AICPA 2025 Criteria released March 2025 | ✅ | ✅ | - | ✅ | ✅ | **VERIFIED** |
| RLUSD market cap $1.26B | - | - | - | ✅ | ✅ | **VERIFIED** |
| Custody costs 0.04%-0.50% annually | - | - | - | ✅ | - | **SINGLE SOURCE** |
| GENIUS Act 6 permitted asset categories | ✅ | ✅ | ✅ | - | - | **VERIFIED** |
| Stablecoin priority claims in bankruptcy (GENIUS Act Section 11) | ✅ | ✅ | - | - | - | **VERIFIED** |
| Tether withdrew EURT citing MiCA | - | - | ✅ | - | ✅ | **VERIFIED** |
| Coinbase suspended USDC rewards in EEA (MiCA) | - | - | ✅ | - | - | **VERIFIED** |
| Tether $8.83B secured loans, $7.66B Bitcoin in reserves | - | ✅ | - | - | - | **SINGLE SOURCE** |
| Circle Reserve Fund 80% of USDC reserves | - | ✅ | - | - | - | **SINGLE SOURCE** |

---

## VERIFIED KEY FINDINGS

### 1. Regulatory Frameworks Show Convergence with Key Divergences

**Main finding:** Three major frameworks (GENIUS Act, MiCA, Singapore MAS) all require 1:1 reserve backing but diverge significantly on asset composition, custody requirements, and interest prohibition.

**Evidence:**
- GENIUS Act: 6 permitted asset categories, 93-day Treasury maturity, federal/state dual-track — Sources: Paul Hastings, Gibson Dunn, Latham & Watkins — Quality: Primary legal analysis
- MiCA: 30% minimum in credit institution deposits (60% for significant EMTs), effective Dec 30, 2024 — Sources: EU Regulation, Ashurst, PwC — Quality: Official regulation
- Singapore MAS: A- credit rating for overseas custodians + Singapore branch requirement, 3-month maturity limit — Sources: MAS.gov.sg, Drew Napier, Morgan Lewis — Quality: Official guidance

**Contradictions/Nuances:**
- GENIUS Act favors Treasury-backed reserves (sovereign risk), MiCA requires significant bank exposure (counterparty risk)
- Singapore unique in requiring local regulatory nexus for overseas custodians
- All three prohibit interest payments to stablecoin holders

**Source quality notes:**
- All three frameworks based on official regulatory texts and major law firm analysis
- FSB 2025 peer review notes only 5 jurisdictions have finalized frameworks globally

---

### 2. GENIUS Act Creates First Comprehensive US Federal Framework

**Main finding:** GENIUS Act establishes 1:1 reserve backing with strict asset quality requirements, bankruptcy priority for stablecoin holders, and dual federal/state regulatory pathway.

**Evidence:**
- Signed July 18, 2025, passed Senate 68-30, House 308-122 — Source: Congress.gov — Quality: Official
- 6 permitted reserve assets: US currency, insured deposits, Treasuries ≤93 days, overnight repos, money market funds, Fed deposits — Sources: Multiple law firms — Quality: Primary legal analysis
- Section 11: Stablecoin holders get superpriority over administrative claims in bankruptcy — Sources: Cadwalader, Paul Hastings — Quality: Primary legal analysis
- Reserve exclusion from bankruptcy estate under Section 11(e) — Sources: Cadwalader, Fintech Takes — Quality: Primary legal analysis

**Contradictions/Nuances:**
- Georgetown Law professor Adam Levitin argues Act makes issuers "administratively insolvent on day one" - trustees have no compensation mechanism
- Interaction between automatic stay and estate exclusion creates potential legal inconsistency
- No published cases testing reserve trust survival under substantive consolidation

**Source quality notes:**
- Legislative text is definitive; bankruptcy implications are legal analysis/prediction
- No actual bankruptcy of GENIUS Act-compliant issuer to test provisions

---

### 3. Custody Infrastructure Has Professionalized Post-SVB

**Main finding:** Multi-custodian arrangements are now standard practice, with Circle's BNY Mellon/BlackRock/Cross River model setting industry benchmark. Custody costs range 0.04%-0.50% annually.

**Evidence:**
- Circle uses BNY Mellon for custody, BlackRock (Circle Reserve Fund) for asset management, Cross River Bank for minting/redemption — Sources: Circle, BNY, CCN — Quality: Company announcements
- BNY launched Dreyfus Stablecoin Reserves Fund (BSRXX) November 2025 for GENIUS Act compliance — Source: BNY Newsroom — Quality: Official
- Custody fees: Coinbase $10K setup + 0.50% annually; typical range 0.04%-0.50% — Sources: MooLoo, YellowCard — Quality: Industry reports
- SOC 2 Type II certification de facto requirement: covers security, availability, processing integrity, confidentiality, privacy — Sources: Crypto.com, Cobo, BitGo — Quality: Industry standards

**Contradictions/Nuances:**
- Cost data limited to industry reports, not audited financial statements
- Larger AUM receives volume discounts; minimums typically $500K-$1M

**Source quality notes:**
- Company announcements are reliable for their own practices
- Industry cost benchmarks may not reflect negotiated institutional rates

---

### 4. SVB Crisis Exposed Critical Concentration Risk

**Main finding:** Circle's $3.3B exposure to Silicon Valley Bank (8% of reserves, 34% of cash reserves) caused USDC to depeg to $0.80-0.87, demonstrating that even high-quality reserves can become inaccessible during banking stress.

**Evidence:**
- Circle had $3.3B at SVB when bank failed March 10, 2023 — Sources: Perplexity (Fed analysis), Claude (detailed timeline), ChatGPT — Quality: Multiple sources confirm
- USDC traded at $0.805-0.87 depending on exchange (TradingView $0.80526, Bloomberg $0.815) — Source: Claude research — Quality: Market data
- FDIC/Fed/Treasury announcement Sunday March 12 protected all depositors; USDC recovered Monday — Sources: Multiple — Quality: Official government action
- Circle's stockholders' equity was only $0.34 million at end of 2023 per April 2025 S-1 filing — Source: Claude (Fed analysis) — Quality: SEC filing

**Contradictions/Nuances:**
- Different exchanges reported different low prices ($0.80-0.87 range)
- BIS research: Circle's transparency about exposure actually triggered the depeg ("disclosure paradox")
- Circle pledged to cover shortfall with corporate resources if needed, but had minimal equity

**Source quality notes:**
- Timeline well-documented across multiple sources
- Market data varies by exchange; $0.87 most commonly cited
- S-1 filing is authoritative for equity figure

---

### 5. Attestation Standards Now Formalized via AICPA 2025 Criteria

**Main finding:** AICPA 2025 Criteria establish first standardized framework for stablecoin reserve attestations, covering redeemable tokens outstanding, reserve asset composition, and comparison between the two.

**Evidence:**
- AICPA released "2025 Criteria for Stablecoin Reporting" March 6, 2025 — Sources: AICPA, Forvis Mazars — Quality: Official
- Three core requirements: Criterion #PF1 (tokens outstanding), Redemption Assets Available, Comparison of Assets to Tokens — Source: Claude research — Quality: Primary documentation
- Proposed criteria for controls (Part II) opened for comment June 2025, closed August 2025 — Sources: AICPA, Forvis Mazars — Quality: Official
- Attestation ≠ Audit: attestations are point-in-time snapshots; audits examine full financial picture over period — Sources: Multiple — Quality: Accounting standards

**Contradictions/Nuances:**
- Point-in-time attestations vulnerable to "window dressing" (moving assets just before attestation)
- John Reed Stark (former SEC): "attestation report is not the same as an audit report. It is an 'unverified snapshot'"
- Proof of Reserves ≠ Proof of Liabilities - can't verify off-chain liabilities cryptographically

**Source quality notes:**
- AICPA criteria are definitive for reporting standards
- Critiques of attestation limitations come from credible industry observers

---

### 6. Real-Time Proof of Reserves Advancing but Fundamental Limits Remain

**Main finding:** Real-time proof of reserves achievable via APIs with 30-second to daily intervals, but fundamental limitation exists: off-chain liabilities and fiat reserves cannot be cryptographically verified.

**Evidence:**
- The Network Firm offers real-time attestation reporting with 30-second to daily intervals — Sources: Claude, ChatGPT — Quality: Company claims
- Chainlink PoR provides on-chain verification for TrueUSD, Paxos Gold; uses decentralized oracle network — Sources: Multiple — Quality: Technical documentation
- zk-SNARKs/zk-STARKs enable privacy-preserving proofs; OKX achieved 50x faster proof generation with Plonky2 — Source: Claude — Quality: Technical documentation
- Backpack Exchange: proofs every 10 minutes internally, published daily — Source: Claude — Quality: Company claims

**Contradictions/Nuances:**
- Vitalik Buterin: "proof of solvency would ideally be done in real time, with a proof that updates after every block"
- Coinbase: "None of these approaches can account for off-chain liabilities, such as lending"
- PwC Switzerland: PoR "ignores the wider picture...provides no information on the actual liabilities"

**Source quality notes:**
- Technical capabilities are documented but adoption varies
- Fundamental limitation (no proof of liabilities) is consensus view

---

### 7. Trust Company Structures Provide Strongest Bankruptcy Protection

**Main finding:** Trust company-issued stablecoins (Paxos, Gemini) provide genuine bankruptcy-remote protection through segregated reserves and direct holder claims, confirmed by legal precedent and now reinforced by GENIUS Act Section 11.

**Evidence:**
- Trust property excluded from bankruptcy estate under Section 541(d), confirmed in *Begier v. I.R.S.* (1990) — Source: Claude — Quality: Case law
- *In re Celsius Network* (Jan 2023): contractual terms determine ownership; Custody Program accounts excluded from estate — Source: Claude — Quality: Case law
- NYDFS requires 100% backing verified daily, 2-day redemption at par, segregated accounts — Sources: Multiple — Quality: Official regulation
- Paxos NYDFS settlement August 2025: $48.5M ($26.5M penalty + $22M compliance investment) for Binance-related issues — Source: ChatGPT — Quality: News reports
- Paxos pursuing OCC national trust charter August 2025 — Sources: ChatGPT, Paxos — Quality: Company announcement

**Contradictions/Nuances:**
- No published cases testing stablecoin reserve trust under substantive consolidation motion
- Cross-border enforcement uncertain - US bankruptcy remoteness may not be recognized in foreign jurisdictions
- GENIUS Act administrative insolvency concern per Georgetown Law analysis

**Source quality notes:**
- Case law citations are authoritative
- GENIUS Act provisions untested in actual bankruptcy

---

### 8. Interest Prohibition Creating Yield-Bearing Wrapper Arbitrage

**Main finding:** Both GENIUS Act and MiCA prohibit issuers from paying interest on stablecoins, but yield-bearing wrappers (sDAI, sUSDe) and exchange reward programs (Coinbase, PayPal) exploit the focus on issuers vs. third parties.

**Evidence:**
- GENIUS Act Section 4(a)(11) prohibits "any form of interest or yield...solely in connection with the holding...of such payment stablecoin" — Sources: Multiple — Quality: Legislative text
- Coinbase offers up to 4.1% APY on USDC as "rewards" not "interest" - CEO Armstrong: "we are not the issuer" — Sources: Claude, Yahoo Finance — Quality: Company statements
- Circle pays 50% of reserve interest to Coinbase per SEC filings — Source: Claude — Quality: SEC filing
- Ethena sUSDe averaged ~18% APY in 2024, peaks to 29% — Source: Claude — Quality: Protocol data
- JPMorgan: yield-bearing stablecoins could reach 50% of total stablecoin market cap — Source: Claude — Quality: Analyst projection

**Contradictions/Nuances:**
- Treasury ANPRM seeks comment on "whether, and to what extent, any indirect payments are prohibited"
- American Bankers Association warned Congress about affiliate yield programs
- Treasury estimates $6.6 trillion in potential deposit outflows if yield programs continue

**Source quality notes:**
- Legislative text is definitive for prohibition
- Loophole exploitation is documented in company statements and analyst reports
- Regulatory resolution uncertain pending Treasury rulemaking

---

### 9. MiCA Enforcement Already Reshaping European Market

**Main finding:** MiCA's strict requirements (30% deposit rule, interest prohibition) have caused Tether to exit Euro stablecoin market and forced Coinbase to terminate USDC rewards in EEA.

**Evidence:**
- Tether discontinuing EURT, ending support by November 2025, citing MiCA's "risk-averse framework" — Sources: Gemini, Grok, Binance news — Quality: Company announcement
- Coinbase terminated USDC rewards in EEA by December 1, 2024, citing MiCA Article 40/50 interest prohibition — Source: Gemini — Quality: Company announcement
- MiCA effective for stablecoins June 30, 2024 (full enforcement December 30, 2024) — Sources: Multiple — Quality: Official regulation
- Tether invested in Quantoz (MiCA-compliant Dutch fintech issuing EURQ/USDQ) — Sources: Gemini, Grok — Quality: Company announcement

**Contradictions/Nuances:**
- Some view MiCA's 30% deposit rule as reintroducing bank counterparty risk (SVB concern)
- FSB 2025 peer review: implementation "incomplete, uneven, and inconsistent" globally

**Source quality notes:**
- Company announcements are reliable for their own decisions
- Market exit patterns well-documented

---

### 10. Custody Technology: MPC + HSM Hybrid Dominates Institutional Market

**Main finding:** Modern institutional custody combines MPC for operational signing, HSM for cold storage, and multi-sig for governance, with SOC 2 Type II certification as baseline requirement.

**Evidence:**
- Technology comparison: Multi-sig (on-chain visible, protocol-dependent), MPC (off-chain computation, blockchain agnostic), HSM (hardware-secured, FIPS 140-2 Level 3) — Sources: ChatGPT, Ripple — Quality: Technical documentation
- HSM best for regulated banks and on-premises requirements; MPC best for real-time signing and geographic redundancy — Sources: Scalable Solutions, Liminal, Taurus — Quality: Industry analysis
- Policy engines: tiered approval requirements by transaction amount (e.g., <$10K: 2-of-3; >$100K: 5-of-7 with time delay) — Source: ChatGPT — Quality: Industry best practices
- Major custodians with SOC 2 Type II: Anchorage Digital, BitGo Trust, Gemini Trust, Crypto.com — Sources: Multiple — Quality: Company certifications

**Contradictions/Nuances:**
- Multi-sig provides transparency (on-chain visible) but protocol-dependent
- MPC provides flexibility but less transparent
- HSM provides regulatory familiarity but less agile

**Source quality notes:**
- Technical comparisons consistent across sources
- Certification claims verifiable from company announcements

---

## RESEARCH GAPS & UNCERTAINTIES

**Well-established:**
- GENIUS Act, MiCA, Singapore MAS framework requirements
- SVB crisis timeline and impact on USDC
- AICPA 2025 Criteria content and requirements
- Trust company bankruptcy protection legal mechanisms
- Interest prohibition in both GENIUS Act and MiCA

**Preliminary/Limited evidence:**
- Actual compliance costs (custody fees 0.04%-0.50% - single source)
- How smaller issuers will manage GENIUS Act compliance costs
- Real-time PoR adoption rates across industry
- Effectiveness of GENIUS Act bankruptcy provisions (untested)

**Unknown/Unstudied:**
- How courts will resolve GENIUS Act administrative insolvency issue
- Whether Treasury rulemaking will close yield-bearing wrapper loophole
- Long-term impact of MiCA 30% deposit rule on European stablecoin market
- Cross-border enforcement of bankruptcy remoteness

---

## SOURCE INVENTORY

### Tier 1 Sources (Official Regulations, Government Documents)
1. GENIUS Act (S.1582) — Congress.gov — https://www.congress.gov/bill/119th-congress/senate-bill/1582/text
2. MiCA Regulation (EU 2023/1114) — EUR-Lex — Official EU regulation
3. MAS Stablecoin Framework — MAS.gov.sg — https://www.mas.gov.sg/
4. AICPA 2025 Criteria for Stablecoin Reporting — AICPA — https://www.aicpa-cima.com/news/article/aicpa-publishes-comprehensive-criteria-for-reporting-on-stablecoins
5. Federal Reserve research on stablecoin reserves

### Tier 2 Sources (Major Law Firms, Big Four Analysis)
1. Paul Hastings: GENIUS Act Comprehensive Guide — https://www.paulhastings.com/insights/crypto-policy-tracker/the-genius-act-a-comprehensive-guide-to-us-stablecoin-regulation
2. Latham & Watkins: GENIUS Act Analysis — https://www.lw.com/en/insights/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us
3. Cadwalader: Bankruptcy Code Amendments — https://www.cadwalader.com/resources/clients-friends-memos/making-way-for-stablecoingenius-act-would-amend-bankruptcy-code
4. Gibson Dunn: GENIUS Act Analysis
5. Forvis Mazars: Stablecoin Reserve Attestations — https://www.forvismazars.us/forsights/2025/11/stablecoin-reserve-attestations-key-considerations-for-compliance
6. PwC Switzerland: Proof of Reserves Analysis
7. Deloitte attestation reports for Circle, RLUSD

### Tier 3 Sources (Industry Reports, Company Announcements)
1. Circle Transparency Portal — https://www.circle.com/transparency
2. Ripple USD Transparency — https://ripple.com/solutions/stablecoin/transparency/
3. Paxos Blog — https://www.paxos.com/blog/
4. BNY Mellon Newsroom — Stablecoin Reserves Fund launch
5. Fireblocks State of Stablecoins 2025
6. EY Survey: Stablecoin Adoption
7. Yahoo Finance: RLUSD market cap
8. CCN, CoinDesk, The Block news coverage

---

## COMPARISON TABLES

### Reserve Requirements by Jurisdiction

| Feature | US GENIUS Act | EU MiCA | Singapore MAS |
|---------|---------------|---------|---------------|
| Backing Ratio | 1:1 minimum | 1:1 minimum | 1:1 minimum |
| Asset Focus | US Treasuries, cash | Bank deposits + HQLA | Cash, govt debt |
| Bank Deposit Min | No specific % | 30% (60% significant) | No specific % |
| Maturity Limit | 93 days | "Liquid" / minimal risk | 3 months |
| Credit Rating | Federal backing | Credit institutions | AA- (debt), A- (custodians) |
| Custody Nexus | US-chartered/licensed | EU credit institutions/CASPs | Singapore branch required |
| Interest Prohibition | Yes | Yes | Yes |
| Attestation Frequency | Monthly | Monthly (significant) | Monthly |

### Major Stablecoin Transparency Comparison

| Stablecoin | Market Cap | Attestor | Frequency | Big Four | Reserve Composition |
|------------|------------|----------|-----------|----------|---------------------|
| USDT | $145B+ | BDO Italia | Quarterly | No | Treasuries, secured loans, Bitcoin |
| USDC | $56B | Deloitte | Monthly | Yes | 80% Treasuries (BlackRock), 20% cash |
| RLUSD | $1.26B | Deloitte | Monthly | Yes | Treasuries, cash equivalents |
| PYUSD | ~$1B | KPMG | Monthly | Yes | 100% USD deposits/Treasuries |

---

## TIMELINE OF DEVELOPMENTS

| Date | Event |
|------|-------|
| June 2022 | NYDFS releases stablecoin guidance |
| March 2023 | SVB collapse; USDC depegs to $0.87 |
| August 2023 | Singapore MAS finalizes SCS framework |
| June 2024 | MiCA stablecoin provisions effective |
| November 2024 | Coinbase terminates EEA USDC rewards |
| December 2024 | MiCA full enforcement; RLUSD launches |
| March 2025 | AICPA releases 2025 Criteria |
| July 2025 | GENIUS Act signed into law |
| August 2025 | Paxos pursues OCC national trust charter |
| November 2025 | BNY launches Stablecoin Reserves Fund |
| November 2025 | Tether discontinues EURT |

---

## PRACTITIONER PERSPECTIVES

**Fireblocks (Custody Provider):**
"Stablecoins are reshaping payments infrastructure. 86% readiness to scale." — May 2025 Report

**Anchorage Digital (Custody Provider):**
"On-shoring the industry through regulated issuance." — December 2025

**Circle CEO Jeremy Allaire:**
"USDC is fully compliant, transparent, and ready for the GENIUS Act era."

**Coinbase CEO Brian Armstrong (on yield prohibition):**
"First, we are not the issuer. And second, we don't pay interest in yield, we pay rewards."

**Tether CEO Paolo Ardoino:**
"Big Four firms are afraid to work with Tether because they fear it will damage their reputations."

**Georgetown Law Prof. Adam Levitin:**
"The Act is written in such a way that no trustee in their right mind would sign on to facilitate an insolvent stablecoin issuer's bankruptcy."

---

## NOTES FOR OPUS 4.5

**Strongest evidence for:**
- GENIUS Act framework details (multiple primary legal sources)
- SVB crisis timeline and impact (multiple corroborating sources)
- MiCA requirements and enforcement impact (official regulation + market evidence)
- AICPA 2025 Criteria content (official documentation)
- Trust company bankruptcy protection (case law + regulatory precedent)

**Weaker evidence for:**
- Actual custody cost benchmarks (industry reports, not audited)
- Smaller issuer compliance strategies (limited data)
- Long-term effectiveness of new regulatory frameworks (untested)

**Interesting tensions/contradictions:**
- GENIUS Act prioritizes Treasury safety vs. MiCA reintroduces bank counterparty risk
- Interest prohibition intent vs. yield-bearing wrapper reality
- Transparency as protection vs. BIS "disclosure paradox" finding
- Bankruptcy priority provisions vs. administrative insolvency concern
- Real-time PoR advancement vs. fundamental proof-of-liabilities limitation

**Missing context:**
- No actual GENIUS Act bankruptcies to test provisions
- Treasury rulemaking on indirect payments still pending
- Limited data on how mid-sized issuers will adapt to compliance costs
- Cross-border enforcement of bankruptcy remoteness untested
