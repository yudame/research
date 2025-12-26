# Claude Research: Stablecoin Token Economics

**Date:** 2025-12-26
**Focus:** Comprehensive Synthesis

---

## Research Output

# Stablecoin token economics: collateralization, revenue, and failure mechanics

Stablecoin design choices fundamentally determine survival during market stress, with fiat-backed models demonstrating superior peg stability while algorithmic designs like Terra/UST exhibit catastrophic failure modes. The **$308.5 billion stablecoin market** (December 2024) now processes **$27.6 trillion annually**—surpassing Visa and Mastercard combined—yet remains vulnerable to bank runs, death spirals, and governance failures that have destroyed over **$60 billion in value** across notable collapses. Academic research from the BIS, Federal Reserve, and NBER reveals that full collateralization with liquid, high-quality assets (short-term Treasuries) provides the strongest stability foundation, while endogenous collateral (backing by self-issued tokens) creates inherent fragility. The March 2023 USDC de-peg to **$0.87** during the SVB crisis demonstrated that even well-collateralized stablecoins face concentration risks, while MakerDAO's governance required **48 hours** to implement emergency changes—longer than the crisis duration.

---

## Collateralization architecture determines crisis resilience

The empirical record across three major stress events—the March 2020 COVID crash, May 2022 Terra collapse, and March 2023 banking crisis—reveals a clear hierarchy of stability based on collateralization design. Fiat-backed stablecoins with high-quality reserves (primarily U.S. Treasuries) demonstrate the strongest peg maintenance, crypto-overcollateralized designs like DAI show moderate resilience with occasional premium trading during deleveraging, while algorithmic stablecoins exhibit catastrophic failure characteristics.

**USDT's reserve evolution** illustrates the stability-quality relationship: commercial paper holdings dropped from **65.39% in May 2021 to 0% by October 2022**, replaced by short-term Treasury bills now exceeding **70% of reserves**. This shift coincided with improved market perception and successful processing of **$21 billion in redemptions** during the 2022 crypto winter. Tether now holds **$113+ billion in T-bills** with maturities under 90 days, generating **$7 billion in interest income** during 2024 alone. Circle's USDC maintains **88% in Treasuries and overnight reverse repos** through the BlackRock-managed Circle Reserve Fund, though the SVB crisis exposed that even **8% concentration at a single bank** ($3.3 billion) can trigger a **13-14% de-peg**.

Crypto-overcollateralized stablecoins face different failure modes. During Black Thursday (March 12, 2020), DAI traded at a **4-5% premium** above $1 due to deleveraging demand, while network congestion prevented oracle updates and allowed some liquidation auctions to execute at **$0 bids**, creating a **$5.4 million system shortfall**. The Peg Stability Module (PSM) that later enabled 1:1 USDC-DAI exchanges proved to be a **contagion channel** during March 2023, transmitting USDC's de-peg directly to DAI, which fell to the **high $0.80s**.

The algorithmic model exemplified by Terra/UST represents the most fragile architecture. The mint/burn mechanism allowed exchange of 1 UST for $1 worth of LUNA, creating what MIT researchers described as "infinite maturity convertible debt with a face value of $1 backed by LUNA." When confidence eroded, LUNA supply hyperinflated from **1 billion to 6.5 trillion tokens** over three days as redemptions accelerated. BIS Working Paper 1164 concludes that algorithmic stablecoins backed by endogenous tokens are "inherently fragile" because both tokens' values depend circularly on each other.

---

## Revenue model sustainability separates survivors from failures

The distinction between sustainable and unsustainable yield generation represents perhaps the most critical design dimension. Sustainable models derive revenue from external sources—Treasury yields, lending interest, trading fees—while unsustainable models rely on token emissions that require continuous inflows, exhibiting Ponzi-like dynamics.

**MakerDAO's evolution** demonstrates successful adaptation. The protocol shifted from crypto-collateral stability fees (generating only **$51.4 million in 2022** against **$60.9 million in expenses**) to Real World Asset integration, now holding **$4.6 billion in U.S. Treasuries** that generate **70-80% of protocol revenue**. Annual revenue reached approximately **$243 million in 2024**, a 10x increase from 2022 levels. The DAI Savings Rate fluctuates with Treasury yields, providing sustainable returns of **5-15%** without external subsidies.

**Anchor Protocol's collapse** provides the definitive case study of unsustainable yield. The protocol promised **19.5% APY** on UST deposits while actual sustainable yield from lending and staking approximated only **3-5%**. By April 2022, Anchor held **75% of all UST** with daily subsidies reaching **$6 million**. The Yield Reserve required repeated bailouts—**$70 million in July 2021** and **$450 million in February 2022**—before depleting entirely during the May collapse. The deposit-to-borrow ratio exceeded **7:1**, meaning depositor yields depended almost entirely on external subsidies rather than productive lending.

**Ethena's funding rate arbitrage model** occupies an intermediate risk position. The protocol generates yield through a delta-neutral strategy: holding ETH/BTC spot while shorting equivalent perpetual futures positions, capturing funding rates when markets trend bullish plus **3-4% ETH staking yields**. Historical data shows only **8.84% of days** experienced combined negative returns (staking plus funding), and only one quarter in three years averaged negative. However, during Q3 2024's market downturn, USDe supply dropped by **$1 billion** as the protocol shifted to **76% stablecoin allocation**. The insurance fund of **$39-60 million** provides limited runway against sustained negative funding periods.

Centralized issuers Circle and Tether operate the simplest sustainable model: earning interest on reserves. Circle generated **$1.6 billion in reserve income** (99% of total revenue) during 2024, though interest rate sensitivity means a **1% rate decrease would reduce revenue by $441 million**. Tether's profitability is more opaque but reported **$13 billion in 2024 profits**, primarily from Treasury interest plus unrealized gains on **$7.8 billion in Bitcoin** holdings.

---

## Governance speed-decentralization tradeoffs revealed during crises

Three crisis responses demonstrate the fundamental tension between decentralized governance and emergency response capability. Circle's centralized structure enabled **immediate communication and banking partner pivots** during the SVB weekend, while MakerDAO's governance required **2 hours to pass emergency votes** but faced a **48-hour execution delay** that rendered changes moot by the time they could take effect.

**Black Thursday (March 2020)** exposed MakerDAO's governance limitations under stress. The emergency governance call convened the same day, but comprehensive stabilization required **multiple votes over two weeks**: debt auctions to recapitalize the system, adding USDC as collateral (controversially centralizing the protocol), and adjusting risk parameters. A September 2020 compensation vote for affected users saw **65% vote for zero compensation**, with critics noting the vote was "delayed purposely for months." A class-action lawsuit followed, moving to arbitration.

**The March 2023 SVB crisis** tested both centralized and decentralized responses. Circle CEO Jeremy Allaire provided frequent Twitter updates and explicitly committed to "stand behind USDC" using "corporate resources, involving external capital if necessary." The company announced a new Cross River Bank partnership the same weekend. However, primary market redemptions remained suspended until Monday due to banking hours constraints—a critical limitation when secondary markets traded at **$0.87**.

MakerDAO's Risk Core Unit posted emergency proposals within hours of Circle's announcement, and governance passed parameter changes in approximately **2 hours** on Saturday. The critical changes included reducing the GSM Pause Delay from **48 to 16 hours**, increasing the PSM-USDP ceiling from **450 million to 1 billion DAI**, and adding a **1% fee** on USDC deposits to discourage inflows. However, the existing 48-hour delay meant these changes could not execute until **Monday, March 13**—after the Federal Reserve's Sunday evening announcement had already resolved the crisis. A March 23 follow-up vote saw **79% support** for retaining USDC as primary reserve despite the contagion event.

**Governance attack vectors** add complexity to decentralization benefits. In October 2020, BProtocol demonstrated flash loan governance manipulation by borrowing **13,000 MKR (~$7 million)** via dYdX, using the tokens to pass a whitelist vote, and repaying—all in a single transaction. MakerDAO acknowledged that "flash loans can and may impact system governance." Mitigations include snapshot voting at proposal creation time, time-weighted voting power, and delegation mechanisms, though each introduces new tradeoffs.

Frax's hybrid governance attempts to balance speed and decentralization through a two-governor system. **FraxGovernorAlpha** requires 40% quorum with 5-day voting and 24-hour timelock for major decisions, while **FraxGovernorOmega** uses only 4% quorum with 2-day voting for daily AMO operations. A **51% voting power threshold** can "short circuit" to bypass normal timelocks during emergencies. Ethena's committee delegation model elects specialized committees (Risk Committee members include Gauntlet, LlamaRisk, and Blockworks Research) rather than voting on all decisions, preserving efficiency while maintaining accountability through bi-annual elections.

---

## Use-case optimization varies dramatically across stablecoin designs

Different stablecoin architectures excel at different functions—payments, DeFi collateral, and value storage—with no single design optimizing all three simultaneously. Understanding these tradeoffs enables appropriate stablecoin selection for specific applications.

**Payment infrastructure** heavily favors USDT on Tron for cost-effectiveness. Tron processes approximately **$20-24 billion in daily USDT transfers**, accounting for **29% of global stablecoin volume** and **67% of all USDT transactions**. Transfer costs range from **$0.00 to $0.50** compared to Ethereum's **$0.50 to $7.00+**, with Tron's August 2025 update reducing fees by approximately 50%. However, Solana offers faster finality at **400 milliseconds** with costs under **$0.01**, making it increasingly competitive for high-frequency payments. Layer-2 networks (Arbitrum, Base) saw stablecoin market cap surge **218%** in 2024, eroding Ethereum's dominance from **90% (with Tron)** to **83%** of total stablecoin supply.

Merchant adoption accelerated significantly through 2024-2025. Visa's stablecoin partnerships grew **46% year-over-year**, enabling spending at **80+ million merchant locations**. Stripe reintroduced crypto payments in October 2024 after a six-year hiatus, supporting USDC across Ethereum, Solana, Polygon, and Base with a **1.5% transaction fee**. The company reports AI companies shifting **~20% of payment volume** to stablecoins. Cross-border remittances represent a particularly strong use case: Brazilian stablecoin transactions grew **207.7% year-over-year** in 2024, with stablecoins comprising **70% of local-to-global exchange flows**.

**DeFi collateral** applications favor established stablecoins with deep protocol integration. DeFi lending TVL reached an all-time high of **$55 billion** in December 2024, with stablecoins accounting for **89% ($655 million)** of borrowed assets in liquidated Aave V3 positions. USDC and USDT dominate collateral usage due to broad integration across Aave, Compound, and Curve. Newer entrants face adoption challenges: GHO (Aave's stablecoin, launched July 2023) has **persistently traded at $0.96-$0.98**, struggling with peg maintenance and limited DeFi integration. By contrast, Curve's crvUSD has **maintained its $1 peg since launch** through its innovative LLAMMA mechanism (soft liquidations across price bands), though limited by scalability constraints requiring overcollateralized volatile collateral.

**Value storage** introduces censorship resistance considerations that algorithmic designs theoretically optimize but practically fail. Both USDC and USDT maintain smart contract "blacklist" functions—Circle froze **$75,000+ in 81 Tornado Cash-associated addresses** in August 2022, while USDT has frozen **653+ addresses** on Ethereum. DAI's censorship resistance depends entirely on its collateral composition; when **50%+ was backed by USDC**, it inherited USDC's censorship properties. Only purely crypto-collateralized designs (crvUSD, theoretical algorithmic stablecoins) offer genuine censorship resistance, but algorithmic designs' demonstrated fragility undermines their value storage function entirely.

---

## Historical failures encode specific design lessons

Three catastrophic failures—Terra/UST, Iron Finance, and the USDC/SVB de-peg—each demonstrate distinct failure mechanics with specific implications for stablecoin architecture.

**Terra/UST's May 2022 collapse** represents the definitive algorithmic stablecoin failure. MIT researchers Liu, Makarov, and Schoar concluded the run was **not the result of single-entity market manipulation** but stemmed from "growing concerns about sustainability of the system." Key events unfolded rapidly: on May 7, two large addresses withdrew **375 million UST from Anchor**; an **$85 million UST-to-USDC swap** on Curve destabilized the 3-pool; and by May 12, LUNA supply had hyperinflated **6,500x** as the death spiral accelerated. Total losses exceeded **$42-45 billion** directly, with **$400 billion+** in broader crypto market contagion. Critically, the researchers found that **wealthier, sophisticated investors ran first** with smaller losses, while retail investors "bought the dip" with larger losses—blockchain transparency did not level the playing field due to information processing differences.

**Iron Finance's June 2021 collapse** demonstrated partial collateralization vulnerability. The IRON stablecoin was backed **75% by USDC and 25% by TITAN** (a governance token with infinite supply). Federal Reserve researchers found that large "whale" liquidity providers initiated the run by removing liquidity from the IRON/USDC pool, then selling TITAN for IRON and IRON for USDC (bypassing the redemption mechanism). TITAN crashed from **$64 to $0.00000006** within hours, while IRON stabilized at approximately **$0.75**—its USDC backing floor. The key design flaw: the **10-minute weighted average price oracle** couldn't respond to rapid TITAN price decline, creating arbitrage that accelerated collapse.

**The March 2023 USDC de-peg** revealed concentration risk in traditional finance dependencies. Circle's **$3.3 billion exposure to SVB** (8% of reserves) triggered a de-peg to **$0.87** when SVB entered receivership. Federal Reserve analysis found that MakerDAO's Peg Stability Module (PSM) amplified contagion: the **950 million USDC daily cap** was hit on both March 10 and 11, with over **1 billion USDC deposited each day** as holders fled to DAI (which promptly de-pegged in tandem). Over **400 million USDP (50%+ of supply)** was withdrawn via PSM. The decisive intervention was the **Federal Reserve/Treasury/FDIC joint announcement** at 6:15 PM ET Sunday protecting all SVB depositors—without this, continued redemption pressure could have forced Treasury securities liquidation, creating traditional financial system spillovers.

**Early warning indicators** derived from these failures include: yield reserve depletion rate exceeding **$1 million/day**; deposit-to-borrow ratios above **3:1**; stablecoin supply approaching **50% of backing asset market cap**; peg deviations greater than **3% for 24+ hours**; daily redemptions exceeding **5% of supply**; and single counterparty exposure above **10% of reserves**. Academic research using machine learning (XGBoost, random forest) has demonstrated predictive capability for de-pegging events, while on-chain liquidity pool analysis shows DEX market events can predict CEX activity by approximately **2 days**.

---

## Regulatory frameworks crystallize around reserve requirements

Global regulatory convergence emphasizes full 1:1 collateralization with liquid, high-quality assets, effectively prohibiting algorithmic designs while establishing disclosure, audit, and redemption requirements.

The **EU's Markets in Crypto-Assets Regulation (MiCA)** took effect for stablecoins on June 30, 2024, requiring **1:1 liquid reserve backing**, authorization from National Competent Authorities before issuance, monthly transparency reports on reserve composition, and regular independent audits. Algorithmic stablecoins without explicit reserves cannot qualify as Asset-Referenced Tokens (ARTs) or E-Money Tokens (EMTs), effectively banning Terra-style designs. USDC became the only major stablecoin fully MiCA-compliant at launch. Significant tokens designated by the European Banking Authority face enhanced oversight, and non-EU currency stablecoins encounter strict usage caps.

The **U.S. GENIUS Act of 2025** (signed into law July 2025) establishes similar requirements: **100% reserve backing at minimum 1:1 ratio**; permitted reserves limited to U.S. coins/currency, insured deposits, Treasury bills (≤93 days maturity), repos/reverse repos, and government money market funds; monthly public disclosure of reserve composition; and executive certification with accounting firm examination. Issuers above **$50 billion** must provide audited annual financial statements. The act **prohibits interest payments** to stablecoin holders (maintaining currency-like rather than security-like treatment) and requires **technical capability to freeze/seize tokens** on lawful orders. Crucially, stablecoin holders receive **first-claim bankruptcy priority** over all other creditors.

The **Financial Stability Board's July 2023 recommendations** provide a global framework emphasizing governance structures, risk management, disclosure requirements, redemption rights, and AML/CFT compliance. An October 2025 thematic review found that while jurisdictions have made progress, "significant gaps and inconsistencies remain." Approximately **70% of central banks** had developed or were developing stablecoin regulatory frameworks by end-2024, with the FSB reporting that **80% of stablecoins** now follow at least one regulation (up from 60% in 2023).

---

## Conclusion: Design principles for stablecoin resilience

The empirical record establishes several non-negotiable design principles for stablecoin resilience. Full collateralization with liquid, high-quality assets (short-term Treasuries, diversified across counterparties) provides the strongest stability foundation—partial or algorithmic backing creates inherent bank-run vulnerability. Revenue models must generate yield from external sources; yields requiring token emission subsidies exhibit Ponzi-like dynamics and inevitable collapse. Governance structures face fundamental speed-decentralization tradeoffs: MakerDAO's 48-hour execution delay rendered emergency responses moot during the SVB crisis, while centralized issuers can respond within hours but introduce single points of failure.

The most significant insight from academic research concerns the **asymmetry of information processing** during crises. MIT researchers found sophisticated investors consistently exited algorithmic stablecoins earlier with smaller losses, while retail investors bought the dip—blockchain transparency did not equalize outcomes. This suggests that design robustness matters more than disclosure requirements: a stablecoin that cannot fail catastrophically protects unsophisticated users better than one with excellent transparency that can.

Future stablecoin design should prioritize: reserve diversification across multiple regulated counterparties (the SVB concentration lesson); real-time reserve attestation rather than monthly snapshots; governance mechanisms enabling rapid parameter adjustment without full centralization (Frax's two-governor model represents one approach); and yield generation exclusively from productive external sources (Treasury yields, lending interest) rather than circular token dynamics. The regulatory convergence around full reserve backing and prohibition of algorithmic designs reflects hard-won lessons from **$60+ billion** in collapsed stablecoin value.

---

## Sources

**Primary Sources from the Stablecoin Research**

**Central Bank & Regulatory Research**
1. Federal Reserve FEDS Notes - "In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins" (December 2025)
   https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html

2. St. Louis Fed - "Regulated Payment Stablecoins Become a Reality in the U.S." (December 2025)
   https://www.stlouisfed.org/on-the-economy/2025/dec/regulated-payment-stablecoins-become-reality-us

3. BIS Working Paper 1164 - Algorithmic stablecoin fragility analysis (referenced in report)

**Academic Research**
4. Harvard Law School Forum on Corporate Governance - "Anatomy of a Run: The Terra Luna Crash" (May 2023)
   https://corpgov.law.harvard.edu/2023/05/22/anatomy-of-a-run-the-terra-luna-crash/

**Industry Analytics**
5. Coin Metrics - "Unpacking Circle's IPO Filing and USDC's On-Chain Footprint"
   https://coinmetrics.substack.com/p/state-of-the-network-issue-307

6. Glassnode Insights - "What Really Happened To MakerDAO?"
   https://insights.glassnode.com/what-really-happened-to-makerdao/

**News & Market Coverage**
7. CNBC - USDC/SVB de-peg coverage (March 2023)
   https://www.cnbc.com/2023/03/13/usdc-nearly-regains-1-peg-after-circle-says-svb-deposit-is-available.html

8. Yahoo Finance - Tether $13B profit report (2024)
   https://finance.yahoo.com/news/tether-reports-13b-profit-2024-152626399.html

9. CoinDesk - MakerDAO governance votes, flash loan attacks
   https://www.coindesk.com/business/2023/03/23/stablecoin-issuer-makerdao-votes-to-retain-usdc-as-primary-reserve-even-after-depeg

**Protocol Documentation**
10. MakerDAO Governance Portal - Emergency Parameter Changes (March 2023)
    https://vote.makerdao.com/executive/template-executive-vote-emergency-parameter-changes-march-11-2023

11. Flywheel DeFi - Frax Governance 2.0 (frxGov) documentation
    https://www.flywheeldefi.com/article/frax-101-paging-frxgov-bravo-over/

**Regulatory Frameworks**
12. Hacken - MiCA Regulation compliance guide
    https://hacken.io/discover/mica-regulation/

13. 21 Analytics - MiCA Stablecoin Rules (EMT/ART requirements)
    https://www.21analytics.ch/blog/stablecoins-in-the-eu/

**Corporate/Institutional**
14. Visa Corporate - Stablecoin payments infrastructure
    https://corporate.visa.com/en/solutions/crypto/stablecoins.html

**Methodological Note:** The Federal Reserve FEDS Notes paper and Harvard Law analysis represent the most rigorous academic sources with clear methodology. Industry reports from Coin Metrics and Glassnode provide on-chain data but should be cross-referenced. News sources (CNBC, Yahoo Finance) provide contemporaneous reporting but lack analytical depth. Protocol documentation offers primary source material for governance mechanics.
