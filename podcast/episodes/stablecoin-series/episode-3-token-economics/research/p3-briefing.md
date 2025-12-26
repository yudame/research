# Master Research Briefing: Stablecoin Token Economic Design & Stabilization Mechanisms

Date: 2025-12-26
For: podcast-synthesis-writer agent

---

## VERIFIED KEY FINDINGS

### 1. Collateralization Models: Clear Stability Hierarchy

**Main finding:** Full fiat-backing with high-quality liquid assets provides strongest stability; algorithmic designs have 100% failure rate under stress.

**Evidence:**
- USDT+USDC control 93% market share — Source: TRM Labs 2025, Chainalysis 2025 — Quality: Industry reports
- Tether holds $113-120B+ in T-bills (<90 day maturity), generating $7B interest income (2024) — Source: Claude synthesis, Gemini — Quality: Multiple corroborating
- Circle USDC maintains 88% in Treasuries/overnight reverse repos via BlackRock-managed Reserve Fund — Source: Coin Metrics — Quality: Industry analytics
- USDT commercial paper dropped from 65.39% (May 2021) to 0% (Oct 2022), replaced by T-bills — Source: Claude, Federal Reserve — Quality: Verified shift
- Terra/UST collapse destroyed $42-45B directly, $400B+ contagion — Source: MIT researchers Liu/Makarov/Schoar, Harvard Law — Quality: Academic
- LUNA hyperinflated from 1B to 6.5 trillion tokens in 3 days — Source: Perplexity, Claude — Quality: Verified cross-source

**Contradictions/Nuances:**
- Even well-collateralized stablecoins face concentration risk: USDC's 8% SVB exposure ($3.3B) caused 13% de-peg to $0.87
- Crypto-overcollateralized (DAI) shows moderate resilience but trades at premium during deleveraging (4-5% above $1 on Black Thursday)

**Source quality notes:**
- BIS Working Paper 1164 concludes algorithmic stablecoins backed by endogenous tokens are "inherently fragile"
- MIT researchers found wealthier/sophisticated investors exited Terra first with smaller losses; retail "bought the dip"

---

### 2. Stabilization Mechanisms: Arbitrage Concentration and Liquidation Design

**Main finding:** Arbitrage is critical for peg maintenance but highly concentrated; liquidation mechanism design determines crisis resilience.

**Evidence:**
- USDT has only 6 active arbitrageurs, largest accounts for 64-66% of redemption activity — Source: Perplexity academic research — Quality: Empirical study
- Stability Pools (Liquity) outperform auction-based liquidations (Maker) — Source: Perplexity — Quality: Comparative analysis
- Liquity achieves liquidations at 110% collateralization ratio vs Maker's 150% — Source: Perplexity — Quality: Protocol documentation
- crvUSD's LLAMMA (Lending-Liquidating AMM Algorithm) implements continuous soft liquidation across price bands — Source: GPT-Researcher, Galaxy Research — Quality: Industry analysis
- DAI PSM (Peg Stability Module) enabled 1:1 USDC-DAI exchange but became contagion channel during SVB crisis — Source: Federal Reserve, Claude — Quality: Government + synthesis

**Contradictions/Nuances:**
- Iron Finance oracle (10-min TWAP) couldn't respond to rapid TITAN decline, creating arbitrage that accelerated collapse
- Ethena's delta-neutral hedging maintained issuer redemption at $1 during October 2025 crash despite secondary venue de-pegs

**Source quality notes:**
- Arbitrage concentration creates vulnerability: if primary arbitrageur faces constraints, peg defense fails precisely when needed

---

### 3. Failure Analysis: Three Distinct Failure Modes

**Main finding:** Historical failures reveal distinct mechanisms: death spirals (Terra), oracle lag (Iron Finance), concentration risk (USDC/SVB).

**Terra/UST (May 2022):**
- Two large addresses withdrew 375M UST from Anchor on May 7
- $85M UST-to-USDC swap on Curve destabilized 3-pool
- MIT researchers: "not single-entity manipulation" but "growing concerns about sustainability"
- LUNA supply hyperinflated 6,500x in 3 days
- Total losses: $42-45B direct, $400B+ contagion
- Source: Harvard Law, MIT, Perplexity — Quality: Academic + multiple sources

**Iron Finance (June 2021):**
- IRON backed 75% USDC / 25% TITAN (infinite supply governance token)
- 10-minute TWAP oracle couldn't track rapid TITAN crash from $64 to $0.00000006
- IRON stabilized at ~$0.75 (USDC backing floor)
- Federal Reserve researchers analyzed whale-initiated run
- Source: Federal Reserve, Perplexity — Quality: Government research

**USDC/SVB (March 2023):**
- Circle's $3.3B SVB exposure (8% of $40B reserves) triggered de-peg to $0.87
- DAI PSM hit 950M USDC daily cap on March 10 and 11
- Over 400M USDP (50%+ of supply) withdrawn via PSM
- Resolved by Fed/Treasury/FDIC joint announcement protecting all SVB depositors
- Source: Federal Reserve FEDS Notes, Claude — Quality: Government + synthesis

**Ethena USDe (October 2025):**
- $8.3B redemptions reduced market cap from $14.8B to ~$6B
- Temporary de-peg on secondary venues but issuer redemption maintained at $1
- Demonstrates delta-neutral hedging resilience but also contraction risk
- Source: Grok, ChainArgos — Quality: Real-time + analytics

---

### 4. Revenue Model Sustainability: External vs. Token-Subsidy Yields

**Main finding:** Sustainable models derive yield from external sources (Treasury interest, lending fees); subsidy-dependent models collapse.

**Sustainable Models:**
- MakerDAO: $4.6B in Treasuries, $243M revenue 2024 (10x from 2022), 70-80% from RWA — Source: Claude — Quality: Synthesis
- Circle: $1.6B reserve income 2024 (99% of revenue), interest rate sensitive — Source: Coin Metrics — Quality: Industry
- Tether: $13B profit 2024, primarily Treasury interest + $7.8B BTC gains — Source: Yahoo Finance, Gemini — Quality: News + policy

**Unsustainable Models:**
- Anchor Protocol: 19.5% APY while sustainable yield was 3-5%, held 75% of all UST
- Daily subsidies: $6M, deposit-to-borrow ratio: 7:1
- Yield Reserve bailouts: $70M (July 2021), $450M (February 2022)
- Source: Claude, Perplexity — Quality: Multiple academic + synthesis

**Intermediate Risk (Ethena USDe):**
- Delta-neutral strategy: spot ETH/BTC + short perpetual futures + 3-4% staking yield
- Only 8.84% of days experienced combined negative returns historically
- Insurance fund: $39-60M (limited runway)
- Q3 2024: Supply dropped $1B, shifted to 76% stablecoin allocation
- Source: Claude, Grok, ChainArgos — Quality: Multiple sources

---

### 5. Governance: Speed-Decentralization Tradeoffs

**Main finding:** Decentralized governance too slow for crisis response; MakerDAO's 48-hour execution delay rendered SVB crisis changes moot.

**Evidence:**
- MakerDAO: Emergency votes passed in 2 hours but 48-hour execution delay
- SVB crisis: GSM Pause Delay reduction from 48→16 hours couldn't execute until Monday (after Fed Sunday announcement resolved crisis)
- MakerDAO: Top 3 MKR holders control 58% voting weight, single largest 27%+
- Flash loan attack: BProtocol borrowed 13,000 MKR (~$7M) via dYdX, passed vote, repaid in single tx (October 2020)
- Circle: Immediate communication, new Cross River Bank partnership same weekend
- Source: Claude, Perplexity, MakerDAO Governance Portal — Quality: Protocol docs + synthesis

**Alternative Governance Models:**
- Frax: Two-governor system (FraxGovernorAlpha: 40% quorum/5-day; FraxGovernorOmega: 4% quorum/2-day)
- 51% voting power can "short circuit" to bypass timelocks in emergencies
- Ethena: Committee delegation (Gauntlet, LlamaRisk, Blockworks Research), bi-annual elections
- Source: Claude, Flywheel DeFi — Quality: Protocol documentation

---

### 6. Regulatory Frameworks: Global Convergence on Full Backing

**Main finding:** Regulators converging on 1:1 reserve requirements, effectively prohibiting algorithmic designs.

**GENIUS Act (US, July 2025):**
- 100% reserve backing minimum 1:1 ratio
- Permitted reserves: USD, insured deposits, T-bills (≤93 days), repos, government money market funds
- Monthly disclosure, CEO/CFO certification, annual audits ($50B+ issuers)
- Algorithmic stablecoin prohibition
- Stablecoin holders: first-claim bankruptcy priority
- Prohibits interest payments to holders
- Three pathways: Insured Depository, Federal-Qualified Nonbank, State-Qualified
- Source: Gemini, Claude, Congress.gov — Quality: Government + synthesis

**MiCA (EU, June 30, 2024):**
- E-Money Institution license required for stablecoins
- Circle achieved EMI license (France, July 2024), first global compliant
- Tether USDT delisted from Coinbase, Kraken, OKX, Bitstamp for EEA users
- Transaction caps on non-Euro stablecoins
- Source: Gemini — Quality: Government/policy research

**Asia-Pacific:**
- Hong Kong Stablecoin Ordinance (August 2025): HK$25M capital, physical presence required
- Singapore MAS: "MAS-regulated" label, S$1M capital, 5-day redemption
- UAE: CBUAE Payment Token regulation, first AED stablecoin AE Coin (January 2025)
- Source: Gemini — Quality: Policy research

**Regulatory Arbitrage:**
- Tether relocated to El Salvador (January 2025)
- FSOC removed digital assets from systemic risk list (December 2025)
- Source: Gemini, Straits Times — Quality: News + policy

---

### 7. Market Evolution 2024-2025: Growth and Consolidation

**Main finding:** Market grew to ~$300B with 93% dominance by USDT/USDC; new entrants (PYUSD, institutional stablecoins) gaining traction.

**Market Share:**
- USDT + USDC: 93% combined market cap — Source: TRM Labs, Chainalysis
- EURC: 76% month-over-month growth — Source: Chainalysis
- PYUSD: $785M → $4.8B — Source: Chainalysis
- Total market: ~$250-300B, projected $500-750B by 2030 — Source: Citi, Grok

**New Entrants 2024-2025:**
- Ethena USDe (Feb 2024): Delta-neutral, peaked $15B, now ~$6B
- Roughrider Coin (Oct 2025): First US state stablecoin (North Dakota)
- SoFiUSD (Dec 2025): Bank-issued for enterprise settlements
- USDf (DWF Labs): RWA-integrated yield-bearing
- Source: Grok, GPT-Researcher — Quality: Industry + real-time

**Institutional Integration:**
- Visa stablecoin partnerships: 46% YoY growth, 80M+ merchants
- Stripe: Reintroduced crypto payments October 2024, 1.5% fee
- 15% institutions offer stablecoin services, 57% planning
- Source: Claude, GPT-Researcher, McKinsey — Quality: Multiple industry

---

### 8. Use Case Optimization: Payments, DeFi, Value Storage

**Main finding:** Different designs excel at different functions; no single stablecoin optimizes all three.

**Payments:**
- USDT on Tron: $20-24B daily, 67% of all USDT transactions, 29% global volume
- Tron fees: $0.00-$0.50 vs Ethereum $0.50-$7.00+
- Solana: 400ms finality, <$0.01 fees
- Layer-2 surge: 218% stablecoin market cap growth 2024
- Brazil: 207.7% YoY growth, 70% of local-to-global exchange flows
- Source: Claude — Quality: Synthesis

**DeFi Collateral:**
- DeFi lending TVL: $55B all-time high (December 2024)
- Stablecoins: 89% of borrowed assets in liquidated Aave V3 positions
- GHO (Aave): Persistently $0.96-$0.98, struggling with peg
- crvUSD (Curve): Maintained $1 peg since launch via LLAMMA
- Source: Claude, GPT-Researcher — Quality: Industry

**Value Storage / Censorship Resistance:**
- USDC: Froze $75,000+ in 81 Tornado Cash addresses (August 2022)
- USDT: Frozen 653+ addresses on Ethereum
- DAI: Inherited USDC censorship when 50%+ backed by USDC
- Only crypto-collateralized designs offer genuine censorship resistance
- Source: Claude — Quality: Synthesis

---

## RESEARCH GAPS & UNCERTAINTIES

**Well-established:**
- Full fiat-backing with T-bills provides strongest stability
- Algorithmic stablecoins without external collateral fail under stress
- Arbitrage concentration creates systemic vulnerability
- 48-hour governance delays insufficient for crisis response

**Preliminary/Limited evidence:**
- Ethena USDe sustainability during prolonged bear markets with negative funding rates
- crvUSD LLAMMA effectiveness at scale beyond current constraints
- Long-term viability of state-issued stablecoins (Roughrider Coin)
- Whether regulatory convergence will stifle beneficial innovation

**Unknown/Unstudied:**
- Optimal governance speed-decentralization balance
- Systemic implications of $3T+ stablecoin market connected to Treasury markets
- Full effects of GENIUS Act prohibition on algorithmic experimentation
- Whether committee-based governance (Ethena model) scales

---

## SOURCE INVENTORY

### Tier 1 Sources (Meta-analyses, Government Research, Academic)
1. BIS Working Paper 1164 — Algorithmic stablecoin fragility analysis
2. Federal Reserve FEDS Notes — SVB failure and stablecoin impact (December 2025)
3. MIT Liu/Makarov/Schoar — "Anatomy of a Run: Terra Luna Crash"
4. FSB July 2023 recommendations + October 2025 thematic review
5. SEC Terraform Labs $4.5B settlement (June 2024)
6. Congress.gov — GENIUS Act (S.1582)

### Tier 2 Sources (RCTs, Large Studies, Government Reports)
1. TRM Labs 2025 — Crypto Adoption and Stablecoin Usage Report
2. Chainalysis 2025 — Global Adoption Index
3. CFTC enforcement order — Tether reserve backing (27.6% fully backed 2016-2019)
4. NYDFS — Paxos $26.5M fine (August 2025)
5. MakerDAO Governance Portal — Emergency parameter changes
6. Ethena Foundation Governance — USDe October volatility analysis

### Tier 3 Sources (Case Studies, Industry Reports, News)
1. J.P. Morgan Global Research — Stablecoins
2. Citi — Stablecoins 2030 Report
3. McKinsey — Tokenized cash payments infrastructure
4. Galaxy Research — crvUSD analysis
5. ChainArgos — Ethena USDe risk case study
6. Coin Metrics — Circle IPO filing analysis
7. CoinGecko — State of Stablecoins 2024

---

## COMPARISON TABLES

### Collateralization Model Comparison
| Model | Examples | Stability | Capital Efficiency | Decentralization | Crisis Resilience |
|-------|----------|-----------|-------------------|------------------|-------------------|
| Fiat-backed | USDT, USDC | Highest | Low (1:1) | Lowest | High (if diversified) |
| Crypto-over | DAI, crvUSD | Moderate | Low (150%+) | High | Moderate |
| Algorithmic | UST (dead) | Failed | Theoretically high | High | None demonstrated |
| Delta-neutral | USDe | Untested long-term | High | Moderate | Mixed signals |

### De-Pegging Events Comparison
| Event | Stablecoin | De-Peg | Duration | Cause | Resolution |
|-------|------------|--------|----------|-------|------------|
| May 2022 | UST | $1→$0.30 | Permanent | Death spiral | Collapse |
| March 2020 | DAI | $1→$0.85 | ~24 hours | Liquidation cascade | Market recovery |
| March 2023 | USDC | $1→$0.87 | ~48 hours | Bank exposure | Fed backstop |
| October 2025 | USDe | Temporary | Hours | Deleveraging | Issuer redemption |

---

## TIMELINE OF DEVELOPMENTS

**2020:**
- March 12-13: Black Thursday, DAI de-pegs to $0.85, $5.4M system shortfall
- October: BProtocol flash loan governance attack on MakerDAO

**2021:**
- June: Iron Finance collapse, TITAN $64→$0
- July: Anchor Yield Reserve first bailout ($70M)

**2022:**
- February: Anchor second bailout ($450M)
- May 7-12: Terra/UST collapse, $42-45B destroyed
- October: USDT eliminates all commercial paper from reserves

**2023:**
- March 10-13: SVB crisis, USDC de-pegs to $0.87, DAI to $0.80s
- July: FSB releases global stablecoin recommendations

**2024:**
- February: Ethena USDe launches
- June 30: MiCA fully effective for stablecoins
- July: Circle achieves EMI license (France)
- October: Stripe reintroduces crypto payments
- December: Tether delisted from EU exchanges for EEA users

**2025:**
- January: Tether relocates to El Salvador
- July: GENIUS Act signed into law
- August: Hong Kong Stablecoin Ordinance effective
- October 10-11: Market crash, USDe $8.3B redemptions
- December: FSOC removes digital assets from systemic risk list

---

## PRACTITIONER PERSPECTIVES

**On design tradeoffs:**
> "Stablecoins are 'productive dollars' but fragmentation across chains leads to idle capital" — X/DeFi developers

**On Ethena:**
> "USDe is a 'tokenized hedge fund' rather than a true stablecoin" — OKX CEO Star, October 2025

**On arbitrage:**
> "Arbitrage is key peg stabilizer but inefficiencies in fragmented liquidity pools amplify risks" — Traders on X

**On regulatory impact:**
> "80% of stablecoins now follow at least one regulation, up from 60% in 2023" — FSB October 2025 review

---

## NOTES FOR OPUS 4.5

**Strongest evidence for:**
- Full collateralization with liquid assets provides stability (multiple academic, government sources)
- Algorithmic stablecoins fail under stress (100% failure rate, BIS, Fed research)
- Revenue model sustainability predicts survival (Anchor vs. Maker comparison)
- Governance speed matters in crises (SVB 48-hour delay documented)

**Weaker evidence for:**
- Optimal collateralization ratio for crypto-backed (varies 110%-150%)
- Long-term viability of delta-neutral strategies (only ~2 years of data)
- Whether state-issued stablecoins will gain adoption

**Interesting tensions/contradictions:**
- Decentralization vs. crisis response speed (no good solution yet)
- Capital efficiency vs. stability (fundamental tradeoff)
- Transparency vs. run prevention (MIT found sophisticated investors run first)
- Innovation vs. regulatory prohibition (GENIUS Act bans algorithmic)

**Missing context:**
- How GENIUS Act will be enforced in practice
- Whether Ethena can survive prolonged negative funding
- Long-term effects of Tether's El Salvador relocation
- Impact of 93% market concentration on systemic risk
