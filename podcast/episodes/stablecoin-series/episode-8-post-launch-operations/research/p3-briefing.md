# Master Research Briefing: Stablecoin Series Ep. 8 - Post-Launch Operations & Continuous Compliance

Date: 2025-12-26
For: podcast-synthesis-writer agent

---

## CROSS-VALIDATION MATRIX

### Critical Facts Verification

| Claim/Statistic | Perplexity | Gemini | Claude | Grok | GPT-R | Status |
|----------------|------------|--------|--------|------|-------|--------|
| GENIUS Act signed July 18, 2025 | ✓ | ✓ | ✓ | ✓ | ✓ | ✅ VERIFIED |
| GENIUS effective Jan 18, 2027 | ✓ | ✓ | ✓ | ✓ | - | ✅ VERIFIED |
| 1:1 reserve requirement | ✓ | ✓ | ✓ | ✓ | ✓ | ✅ VERIFIED |
| USDC depegged to $0.86 (SVB) | ✓ | - | ✓ | - | ✓ | ✅ VERIFIED |
| $3.3B Circle exposure at SVB | ✓ | - | ✓ | - | ✓ | ✅ VERIFIED |
| MiCA 60% bank deposits (significant) | ✓ | ✓ | - | - | - | ✅ VERIFIED |
| MiCA 30% bank deposits (non-sig) | ✓ | ✓ | - | - | - | ✅ VERIFIED |
| Travel Rule US $3,000 threshold | ✓ | ✓ | - | - | - | ✅ VERIFIED |
| Travel Rule EU €0 threshold | ✓ | ✓ | - | - | - | ✅ VERIFIED |
| MakerDAO Gini coefficient 0.84 | - | - | ✓ | - | - | ⚠️ SINGLE SOURCE |
| DAO participation 6-35% | - | - | ✓ | - | - | ⚠️ SINGLE SOURCE |
| USX depegged to $0.1 (2025) | ✓ | - | - | ✓ | - | ✅ VERIFIED |
| USDe depegged to $0.65 (Oct 2025) | ✓ | - | - | ✓ | - | ✅ VERIFIED |
| Beanstalk attack $182M | - | - | ✓ | - | - | ⚠️ SINGLE SOURCE |
| Stablecoin holder priority (GENIUS) | ✓ | ✓ | ✓ | - | - | ✅ VERIFIED |
| USDT delisted in EU (MiCA) | ✓ | ✓ | - | ✓ | - | ✅ VERIFIED |

### Coverage Analysis

| Topic | P | Ge | C | Gr | GPT | Coverage Level |
|-------|---|----|----|----|----|----------------|
| GENIUS Act requirements | ✓✓ | ✓✓✓ | ✓✓ | ✓ | ✓ | Excellent |
| MiCA framework | ✓✓ | ✓✓✓ | - | ✓ | - | Strong |
| SVB crisis response | ✓✓ | - | ✓✓✓ | - | ✓ | Strong |
| Governance participation | ✓ | - | ✓✓✓ | - | - | Moderate |
| De-pegging events 2025 | ✓✓ | - | ✓ | ✓✓ | - | Strong |
| Operational costs | ✓ | - | - | - | ✓ | Limited |
| Travel Rule variations | ✓ | ✓✓✓ | - | - | - | Strong |
| Security incidents | ✓ | - | ✓✓✓ | ✓ | - | Strong |
| Recovery/wind-down | ✓ | ✓ | ✓✓ | - | - | Moderate |
| Multi-chain operations | ✓ | - | - | ✓ | ✓ | Moderate |

**Legend:** P=Perplexity, Ge=Gemini, C=Claude, Gr=Grok, GPT=GPT-Researcher

---

## VERIFIED KEY FINDINGS

### 1. Regulatory Framework Evolution (2024-2025)

**Main finding:** Two landmark frameworks now govern global stablecoin operations - GENIUS Act (US) and MiCA (EU) - with fundamentally different approaches to reserve requirements and market access.

**Evidence:**

**GENIUS Act (United States):**
- Signed: July 18, 2025 by President Trump — Source: Gemini, Perplexity, White House — Quality: Official/verified
- Effective: January 18, 2027 (18 months after enactment) or 120 days after final regulations
- Rulemaking deadline: July 18, 2026 for Federal Reserve, OCC, FDIC
- Reserve requirements: 100% backing with US dollars, demand deposits, T-bills (≤93 days), repos, or Fed reserves
- Stablecoin holders have PRIORITY over all other creditors in insolvency
- Interest payments by issuers PROHIBITED
- Applies to bank subsidiaries, federal qualified issuers, and state issuers <$10B
- Travel Rule: $3,000 threshold (FinCEN proposed $250 for cross-border)

**MiCA (European Union):**
- Stablecoin rules: Effective June 30, 2024
- CASP rules: Effective December 30, 2024
- Reserve requirements: 30% in bank deposits (non-significant), 60% in bank deposits (significant tokens >$5B or >10M users)
- Interest payments PROHIBITED
- Led to USDT delisting: Coinbase (Dec 2024), Crypto.com (Jan 2025), Kraken (Mar 2025), Binance (Mar 2025)

**Contradictions/Nuances:**
- US approach prioritizes Treasury liquidity; EU forces banking sector integration
- US allows reserves in Treasuries (bypassing bank counterparty risk); EU mandates bank deposits (creates SVB-type exposure)
- Banking lobby argues US approach may reduce deposit funding for community banks

**Source quality notes:**
- GENIUS Act details from Congress.gov, White House fact sheet, and multiple law firm analyses
- MiCA details from official EU sources and exchange announcements

---

### 2. Travel Rule Implementation Creates Global Fragmentation

**Main finding:** FATF Recommendation 16 has been implemented with vastly different thresholds across jurisdictions, creating compliance complexity for cross-border stablecoin operations.

**Evidence:**

| Jurisdiction | Threshold | Requirements | Effective |
|--------------|-----------|--------------|-----------|
| United States | $3,000 | Full originator/beneficiary data | Existing |
| European Union | €0 | Full data ALL transactions; verification >€1,000 | Dec 30, 2024 |
| United Kingdom | £0 | Collection all; verification >£1,000 | Sept 1, 2023 |
| Singapore | SGD 1,500 | Full value transfer info above threshold | Jan 28, 2020 |
| Japan | ~$3,000 | Name, address, wallet info | June 1, 2023 |
| South Korea | 0 KRW | All transactions (expanded Nov 2025) | Nov 2025 |
| Hong Kong | HKD 8,000 | Full info above threshold | June 1, 2023 |

**Source quality notes:**
- Gemini provided comprehensive table with citations to regulatory sources
- Perplexity confirmed US and EU thresholds

---

### 3. SVB Crisis Response Revealed Governance Model Limitations

**Main finding:** The March 2023 SVB crisis provided a real-world stress test comparing centralized (Circle, Tether) and decentralized (MakerDAO) governance - all models ultimately depended on federal intervention.

**Evidence:**

**Circle (Centralized):**
- Disclosed $3.3B exposure (8% of reserves) at SVB on Friday evening March 10
- USDC depegged to $0.86 on Saturday March 11
- CEO Allaire committed to "stand behind USDC" using corporate resources
- S-1 filing reveals stockholders' equity of only $340K - insufficient to cover $3.3B shortfall
- Peg restored Monday March 13 after federal depositor guarantee announced Sunday

**MakerDAO (Decentralized):**
- DAI fell to $0.88 due to PSM exposure to USDC
- Emergency vote passed in ~2 hours on Saturday (88,767 MKR vs 47 MKR against)
- Raised USDC-A PSM inflow fee 0% → 1%
- Reduced daily mint limit 950M → 250M DAI
- BUT: 48-hour Governance Security Module delay meant changes couldn't execute until Monday
- During delay: ~736M DAI minted through USDC-PSM by arbitrageurs
- ~400M USDP (half total supply) withdrawn from PSM

**Tether (Centralized/Opaque):**
- Zero SVB exposure announced within hours
- USDT traded at slight premium throughout crisis
- Market cap grew $7B over following two weeks
- Outcome reflected geographic diversification, not superior crisis management

**Contradictions/Nuances:**
- Speed vs. security tradeoff: MakerDAO's 48-hour delay prevented timely response
- All three stablecoins ultimately depended on federal intervention (March 12 Treasury/Fed/FDIC announcement)
- Fed analysis: PSMs "served to weaken Dai's own collateral pool"

**Source quality notes:**
- Federal Reserve FEDS Notes paper (December 2024) provides authoritative analysis
- MakerDAO governance portal confirms vote details

---

### 4. Governance Participation and Power Concentration

**Main finding:** DAO governance operates with critically low participation (6-35%) and extreme power concentration (top 1% hold 83% of tokens), creating attack surfaces and "decentralization theater."

**Evidence:**

**Participation Rates:**
- MakerDAO: Average 24.59 voters per poll (638 polls, Aug 2019-Oct 2021) — Source: arXiv
- Compound: 34% participation — Source: Fudan University research
- Uniswap: 31.4% participation — Source: Fudan University research
- Cross-protocol average: 6.3% — Source: Fudan University researchers

**Power Concentration:**
- MakerDAO Gini coefficient: 0.8438 (individual votes up to 0.9805) — Source: arXiv
- Largest single voter: 52.66% average voting power per poll
- Top 1% of addresses: 83.2% of externally-held funds — Source: Glassnode
- Aave: Top 3 wallets control >58% of DAO votes

**Governance Attacks:**
- Beanstalk (April 2022): $1B flash loan → 79% voting power → $182M drained in 13 seconds
- Compound "Golden Boys" (July 2024): Proposal 289 allocated $24M (5% treasury) to attacker-controlled protocol; passed with only 57 voters
- Build Finance (Feb 2022): $470K drained via disabled notification bots, governance takeover

**Source quality notes:**
- Claude provided extensive academic citations (arXiv, Fudan University, ETH Zurich)
- Specific attack details from Immunefi, The Block, DL News

---

### 5. De-Pegging Events and Recovery Mechanisms (2025)

**Main finding:** Multiple de-pegging events in 2025 demonstrated that transparency and collateral quality directly determine recovery outcomes.

**Evidence:**

**USDe (Ethena) - October 2025:**
- Traded as low as $0.65 on Binance during US-China trade tension escalation
- Recovered to ~$0.98 within hours
- Third-party attestation confirmed 120%+ collateralization with $66M excess collateral
- Redemption mechanism remained operational throughout
- Uses delta-neutral strategy (crypto collateral + futures hedges)

**USX (Solana) - December 2025:**
- Depegged to $0.10
- Linked to liquidity fears and market panic
- Recovery uncertain

**sUSD (Synthetix) - April 2025:**
- Dropped to $0.66
- Governance and liquidity constraints

**USDX - Late 2025:**
- Massive de-peg due to questionable backing and opaque reserve management
- DeFi lending protocols (Euler) drained; borrowing rates spiked to 800%+ APY
- Addresses linked to founder Flex Yang borrowed stablecoins and transferred to exchanges
- Pattern suggests fire-sale exodus

**Hierarchy of Safety (observed):**
1. Fiat-backed (USDT, USDC) - Highest safety tier
2. Synthetic with transparent attestations (USDe) - Intermediate tier
3. Crypto-backed with limited transparency (USDX) - Lowest tier

**Source quality notes:**
- Perplexity and Grok both documented 2025 events
- Claude provided historical context (Terra/UST, HUSD, Iron Finance)

---

### 6. Operational Security Incidents Beyond Smart Contracts

**Main finding:** Stablecoin operational failures extend far beyond code vulnerabilities to include custody failures, banking dependencies, oracle manipulation, and regulatory enforcement.

**Evidence:**

**Custody Failures:**
- Prime Trust (June 2023): Nevada custodian "literally lost the keys to $85M" in customer crypto
- Lost access December 2021, used customer funds to buy replacement
- TrueUSD depegged to $0.993 when Nevada issued cease-and-desist

**Banking Concentration:**
- March 2023: Silvergate, Signature, and SVB failures eliminated critical crypto infrastructure in 72 hours
- Silvergate Exchange Network (SEN) and Signet payment platform terminated
- Circle forced to limit USDC operations to "business hours" temporarily

**Oracle Manipulation:**
- Compound (November 2020): DAI spiked to $1.30 on Coinbase vs $1.00 elsewhere → $46-49M largest single liquidation; attack cost ~$100K
- MakerDAO "Black Thursday" (March 2020): 43% ETH crash + 6-10x gas spike → oracle failed to update → 36.6% of liquidations won with zero bids → $8.32M losses

**Regulatory Enforcement:**
- Tether CFTC (Oct 2021): $41M penalty - "fully backed only 27.6% of days"
- Tether NYAG (Feb 2021): $18.5M settlement
- Paxos NYDFS (2025): $48.5M for BUSD issues
- Do Kwon: 15-year prison sentence (Dec 2025) for TerraUSD fraud

**Source quality notes:**
- Claude provided comprehensive incident documentation with specific figures
- Grok confirmed $3.35B total blockchain hack losses in 2025

---

### 7. Recovery and Wind-Down Requirements

**Main finding:** GENIUS Act, MiCA, and UK frameworks establish explicit wind-down requirements, but no major stablecoin has executed an orderly wind-down under new regulations.

**Evidence:**

**GENIUS Act Requirements:**
- 100% reserve backing with liquid assets
- Monthly public disclosures
- CEO/CFO certifications
- "Tested wind-down playbooks" required
- Reserves in segregated, bankruptcy-remote accounts
- Stablecoin holder priority over ALL creditors

**MiCA Requirements:**
- Recovery and redemption plans mandatory
- At least 30% of reserves in separate credit institution accounts

**UK Framework (effective October 2027):**
- 40% held as unremunerated deposits at Bank of England
- Validated wind-down plans required
- Statutory trust protection

**Hong Kong (effective August 2025):**
- 100% backing plus overcollateralization expectations
- Operating without license: up to 7 years imprisonment

**Current Issuer Preparedness:**
- Circle: Reserves in SEC-registered MMF (BlackRock), ~75% short-duration Treasuries, ~25% cash at GSIBs
- Paxos: 100% cash/equivalents in fully segregated bankruptcy-remote accounts
- Tether: Limited disclosure; relocated HQ to El Salvador (Jan 2025)

**Redemption Mechanisms (Two-Tier Access):**
- Circle: Zero-fee 1:1 for 1,819 institutional customers; retail via secondary markets
- Tether: $150 verification fee, $100K minimum, 0.1% fee, weekly limits, US citizen restrictions

**Source quality notes:**
- Gemini provided comprehensive regulatory comparison
- Claude detailed current issuer preparedness

---

### 8. Operational Changes by Major Issuers (2025)

**Main finding:** Major issuers announced significant operational changes in 2025 to align with new regulations and expand reach.

**Evidence:**

| Issuer | Key Change | Date | Rationale |
|--------|------------|------|-----------|
| Tether | Phased out USDT on Omni, Bitcoin Cash SLP, Kusama, EOS, Algorand | July 11, 2025 | Infrastructure optimization |
| Circle | Expanded USDC to 28 networks including Aptos, Base; Visa settlement integration ($3.5B pilot) | Dec 16, 2025 | Settlement efficiency |
| Paxos | Converted to OCC national trust; wound down USDL | Dec 12, 2025 | Federal regulation alignment |
| PayPal | PYUSD on Stellar, Arbitrum, TRON via LayerZero | June 11, 2025 | Multi-chain efficiency |

**Source quality notes:**
- Grok provided table with specific dates and sources
- Company announcements cited directly

---

## RESEARCH GAPS & UNCERTAINTIES

**Well-established:**
- GENIUS Act and MiCA regulatory requirements
- SVB crisis timeline and stablecoin responses
- Travel Rule thresholds across major jurisdictions
- Governance concentration metrics
- Major de-pegging events 2025

**Preliminary/Limited evidence:**
- Specific operational costs (headcount, infrastructure, compliance systems at different scales)
- Team composition and staffing levels at major issuers
- Exact compliance burden increase post-GENIUS Act
- Wind-down plan testing procedures

**Unknown/Unstudied:**
- Effectiveness of new wind-down provisions under stress (untested)
- Full Tether reserves composition and counterparty exposure
- Contagion pathways between stablecoins and traditional financial markets
- Actual enforcement actions under GENIUS Act (takes effect 2027)

---

## SOURCE INVENTORY

### Tier 1 Sources (Official, Regulatory, Academic)
1. Federal Reserve FEDS Notes: "In the Shadow of Bank Runs" (Dec 2024) — SVB crisis analysis — https://www.federalreserve.gov/econres/notes/feds-notes/
2. Congress.gov: S.1582 GENIUS Act text — Official legislation — https://www.congress.gov/bill/119th-congress/senate-bill/1582
3. White House Fact Sheet: GENIUS Act signing (July 18, 2025) — https://www.whitehouse.gov/fact-sheets/
4. arXiv: MakerDAO governance analysis — Academic research on DAO voting
5. Fudan University: "Centralized Governance in Decentralized Organizations" — Power concentration metrics

### Tier 2 Sources (Industry Reports, Law Firms, Market Research)
1. Latham & Watkins: "The GENIUS Act of 2025" — Legal analysis — https://www.lw.com/
2. Brookings Institution: "Issues for regulators as they implement GENIUS Act" (Oct 2025)
3. Financial Stability Board: "Gaps and inconsistencies in crypto recommendations" (Oct 2025)
4. Fireblocks: "State of Stablecoins" report — Industry trends
5. TRM Labs: "Global Crypto Policy Review" (Dec 2025)
6. McKinsey: "Stablecoins payments infrastructure" (July 2025)

### Tier 3 Sources (News, Company Announcements, Community)
1. Circle Year in Review 2025 — Company announcement
2. Paxos OCC approval announcement (Dec 12, 2025)
3. PayPal PYUSD Stellar announcement (June 11, 2025)
4. Crypto Briefing: Tether blockchain changes (July 2025)
5. Yahoo Finance: USX depeg (Dec 2025)

---

## COMPARISON TABLES

### Regulatory Framework Comparison

| Element | GENIUS Act (US) | MiCA (EU) | UK Framework |
|---------|-----------------|-----------|--------------|
| Effective | Jan 2027 | Dec 2024 | Oct 2027 |
| Reserve requirement | 100% | 100% | 100% |
| Asset composition | Treasuries, repos, cash | 30-60% bank deposits | 40% BoE, 60% other |
| Interest allowed | No | No | No |
| Holder priority | Yes (super-priority) | Yes | Statutory trust |
| Fed/CB access | No (non-banks) | N/A | Required |

### De-Pegging Event Comparison

| Stablecoin | Date | Low Price | Root Cause | Outcome |
|------------|------|-----------|------------|---------|
| USDC | Mar 2023 | $0.86 | SVB exposure | Recovered (federal guarantee) |
| DAI | Mar 2023 | $0.88 | USDC PSM exposure | Recovered |
| USDe | Oct 2025 | $0.65 | Market panic | Recovered (transparent reserves) |
| USX | Dec 2025 | $0.10 | Liquidity crisis | Uncertain |
| sUSD | Apr 2025 | $0.66 | Governance issues | Partial recovery |
| USDX | Late 2025 | Severe | Opaque reserves | Collapse |
| Terra/UST | May 2022 | ~$0.00 | Algorithmic failure | Total collapse |

---

## TIMELINE OF DEVELOPMENTS

| Date | Event |
|------|-------|
| Mar 2020 | MakerDAO "Black Thursday" - $8.32M losses from oracle failure |
| Nov 2020 | Compound oracle attack - $49M largest liquidation |
| Feb 2021 | Tether NYAG $18.5M settlement |
| Oct 2021 | Tether CFTC $41M penalty |
| Apr 2022 | Beanstalk governance attack - $182M drained |
| May 2022 | Terra/UST collapse - $40-60B value destroyed |
| Oct 2022 | HUSD collapse - depegged to $0.28 |
| Mar 2023 | SVB crisis - USDC depeg to $0.86 |
| June 2023 | Prime Trust collapse - $85M keys lost |
| June 2024 | MiCA stablecoin rules effective |
| July 2024 | Compound "Golden Boys" governance attack |
| Dec 2024 | MiCA CASP rules effective; USDT delistings begin |
| Jan 2025 | Tether HQ moves to El Salvador |
| Apr 2025 | sUSD depeg to $0.66 |
| June 2025 | PayPal PYUSD on Stellar |
| July 2025 | GENIUS Act signed; Tether phases out chains |
| Oct 2025 | USDe depeg scare (recovered) |
| Nov 2025 | South Korea expands Travel Rule to all transactions |
| Dec 2025 | Paxos OCC conversion; USX depeg; Do Kwon 15-year sentence |

---

## PRACTITIONER PERSPECTIVES

**Compliance Officers (from Grok/industry interviews):**
- "Daily hurdles in wallet screening, regulatory playbooks"
- Licensing burdens and readiness for 2026 rules major concerns
- AML/KYC implementation at scale creates friction

**Community Discussions (Reddit, X):**
- Cross-border payment delays persist despite blockchain solutions
- Onboarding fragmentation remains frustrating
- Concerns about centralization and freeze capabilities

**Institutional Users:**
- Banks viewing stablecoins through "de-pegging and liquidity impact" lens
- Some see opportunities in regulated frameworks
- McKinsey notes potential for tokenized cash in payments

---

## NOTES FOR OPUS 4.5

**Strongest evidence for:**
- GENIUS Act and MiCA regulatory requirements (multiple official sources)
- SVB crisis timeline and responses (Fed analysis + multiple corroborating sources)
- De-pegging events and outcomes (verifiable on-chain data)
- Governance concentration metrics (academic research)

**Weaker evidence for:**
- Operational cost specifics (limited public disclosure)
- Day-to-day operational challenges (practitioner interviews limited)
- Wind-down plan effectiveness (untested)

**Interesting tensions/contradictions:**
- Decentralization vs. crisis response speed (MakerDAO's 48-hour delay)
- US Treasury-focused reserves vs. EU bank-deposit mandate (different risk profiles)
- Transparency claims vs. actual disclosure (Tether audit promises unfulfilled)
- Holder priority vs. untested bankruptcy frameworks

**Missing context:**
- How GENIUS Act enforcement will actually work post-2027
- Tether's full reserves composition and counterparty exposure
- Real operational costs at different scales
- Cross-border coordination mechanisms between US/EU/Asia regulators

**Narrative arc suggestion:**
1. Open with scale/importance of stablecoin operations ($180B+ in circulation)
2. Contrast old "Wild West" era with new regulatory frameworks
3. Use SVB crisis as central case study (all models tested)
4. Examine governance reality (participation, concentration, attacks)
5. Detail operational security beyond code (custody, banking, oracles)
6. Compare regulatory approaches (GENIUS vs. MiCA)
7. Close with what "operational maturity" means going forward
