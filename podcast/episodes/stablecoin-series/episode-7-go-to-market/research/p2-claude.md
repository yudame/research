# Claude Research: Stablecoin Series: Ep. 7, Go-to-Market Strategy & User Adoption

**Date:** 2025-12-26
**Focus:** Comprehensive Synthesis

---

## Research Output

# Stablecoin adoption faces fundamental measurement and sustainability challenges

**Stablecoin transaction volume statistics dramatically overstate genuine user adoption**, with **70-90%** of volume attributable to automated trading depending on methodology. While survey data suggests **75%** of consumers would try stablecoins through their bank, Federal Reserve data shows actual crypto payment usage has *declined* to under 2%—revealing a significant intention-action gap. The path to sustainable adoption requires solving fundamental UX friction, building institutional trust, and avoiding the mercenary capital patterns that have undermined DeFi protocols when incentives end.

This multi-dimensional analysis examines five critical questions for stablecoin go-to-market strategy, drawing on blockchain analytics, consumer surveys, DeFi case studies, and payment network research.

---

## Bot activity dominates stablecoin volume but definitions vary substantially

The claim that **71% of stablecoin volume is bot-driven** originates from CEX.io's Q3 2025 report analyzing $15.6 trillion in stablecoin transfers using Visa/Allium Labs methodology. The finding is directionally valid but requires careful interpretation given methodological limitations.

The Visa/Allium classification system defines "organic" transactions as those from accounts initiating fewer than **1,000 transactions** and under **$10 million** in transfer volume within 30 days. Everything exceeding either threshold is classified as "inorganic." This methodology has been applied consistently since April 2024, when Visa's dashboard showed over **90%** of $2.2 trillion in monthly transactions were non-organic, with only $149 billion (approximately 7%) originating from "organic payments activity."

Multiple sources corroborate the general finding. CEX.io's 2024 annual data found **77%** of total stablecoin volume fell into the "unadjusted" category. Coinbase Institutional Research, using the same Visa methodology, found adjusted 2023 stablecoin volume was $2.3 trillion—roughly **10%** of total transaction volume. Academic research from Yale and Cornell using Benford's Law analysis found unregulated exchanges had over **70%** fake volume.

However, significant methodological critiques exist. Austin Campbell of Columbia Business School (formerly of Paxos) argues "there's significant problems with what Visa is trying to do... This means trying to exclude all of trading, so not just automated trading." The threshold-based approach excludes legitimate high-volume traders and centralizes exchange wallet addresses, including those holding stablecoins for services like prepaid cards. The 71% figure conflates several distinct types of automated activity: MEV bots extracting value from transaction ordering, legitimate arbitrage and market-making, DeFi protocol interactions, wash trading, and high-frequency trading.

Chainalysis's 2024-2025 research using two distinct heuristics identified **$2.57 billion** in potential wash trading on DEXs—representing less than 0.1% of DEX volume in November 2024. This suggests the "true" wash trading subset is substantially smaller than the 71% "bot" figure, though the methodology may significantly undercount the phenomenon.

Despite bot dominance in aggregate volume, absolute organic activity has reached all-time highs. Retail-sized transactions under $250 hit record levels in September 2025, with non-trading stablecoin activity jumping over **15%** in 2025. Visa's dashboard reports **47 million monthly active stablecoin users** across all chains—a meaningful base of genuine adoption even if dwarfed by automated volume.

---

## UX innovations show measurable friction reduction but retention remains challenging

Crypto wallet onboarding has improved dramatically through four interconnected innovations: **embedded wallets**, **account abstraction (ERC-4337)**, **MPC-based seedless authentication**, and **gas fee abstraction via paymasters**. However, quantitative data on conversion improvements remains limited to company-reported figures rather than independent audits.

**Embedded wallets** have achieved the largest scale deployment. Privy powers over **75 million accounts** across 1,000+ teams including Pump.fun, Farcaster, Zora, and Hyperliquid. These wallets are created automatically at signup using familiar authentication (email, social login, passkeys) without requiring seed phrase backup or wallet extension installation. Dynamic, acquired by Fireblocks for $90 million, offers similar functionality with mobile-first passkey authentication that "allows users to spin up a new, non-custodial wallet simply by using FaceID."

**Account abstraction** adoption grew substantially in 2024. Safe deployed **28.7 million accounts** (6.5x 2023 deployments), while **19.7 million ERC-4337 native smart accounts** were deployed (7x 2023). Coinbase Paymaster powered **15 million+ gasless transactions** across 50+ applications. However, Rhinestone's analysis identifies a critical limitation: "One major shortcoming of the ERC-4337 ecosystem has been very low user retention rates." The gap between account growth and transaction volume reflects poor retention among new smart account users.

Quantified friction points provide context for these innovations. Coinbase Wallet data shows **69%** of Ethereum swaps encounter a "not enough gas" error when the user starts the trade. The 0x integration for gasless swaps made trades **2x more likely** to land in the next block with MEV protection. Trustee Wallet reported a **97.4% conversion rate** from started to confirmed swaps after implementing optimized UX with Changelly integration. Matcha increased daily active traders by **20%** with its Auto feature launch.

User research identifies persistent barriers beyond technical friction. RIF Technology's 2024 survey found the most desired features were ability to pay for everyday items (**35.96%**), easier onboarding and avoiding risk of losing keys (**24.56%**), and low-risk investment capabilities (**26.32%**). An ACM CHI 2021 study analyzing 25,109 app reviews found the most prevalent user misconception was that wallet developers set and receive transaction fees—users perceived high gas fees as fraudulent behavior by the app.

The fundamental tradeoff across all innovations is security versus convenience. Embedded wallets create vendor lock-in and dependence on provider infrastructure. Social recovery requires trusting guardians who may become unavailable or adversarial. MPC wallets have higher communication costs that can slow performance. Paymaster-sponsored gas creates cost centers for applications and potential abuse vectors without proper policy controls.

---

## Survey data confirms bank trust is critical but reveals major intention-action gaps

The claim that **75% of consumers would try stablecoins if offered by their bank** originates from FIS (Fidelity National Information Services) research released November 2025. The survey of 1,000 U.S. consumers (employed full-time adults, online panel, October 2025) found 74.8% would be open to trying digital currency services through their primary bank, while only **3.6%** would feel comfortable adopting from unregulated providers.

Cross-referencing reveals consistent patterns across 12+ surveys but significant conflicts between stated intent and actual behavior.

**Generational divide is stark and consistent.** Motley Fool's July 2025 survey (n=2,000) found **71%** of Gen Z and **60%** of millennials would use stablecoins for typical shopping, compared to only **31%** of Gen X and **18%** of baby boomers. Actual usage follows the same pattern: Gen Z (**42%**), millennials (**34%**), Gen X (**14%**), and baby boomers (**2%**). This generational gap may slow mainstream adoption given spending power concentration in older demographics.

**Trust in traditional financial institutions is the binding constraint.** Across multiple surveys, **63-77%** of consumers prefer accessing stablecoins through traditional banking relationships. The FIS survey found **77.4%** believe stablecoins should be regulated like traditional payment methods, and **66.3%** said FDIC-style insurance would increase likelihood of use. The EY-Parthenon survey of 350 institutional decision-makers found **63%** of corporates are looking to traditional banks for stablecoin access.

**However, a major intention-action gap exists.** The Federal Reserve SHED survey shows crypto ownership declined from **12.3%** (2021) to **8.4%** (2024), with crypto payment usage falling from approximately 3% to under **2%**. Only approximately **5.1 million** U.S. consumers used crypto for payments in 2024 (down from 6.7 million in 2021). The main reason for crypto payments shifted from benefits (privacy, speed) to "payee preference"—indicating passive rather than active adoption.

Pew Research Center's February 2024 survey (n=10,133) found **63%** of U.S. adults have little to no confidence in cryptocurrency safety and reliability, with only **5%** expressing extreme or very confidence. Among those 50 and older, **71%** lack confidence versus **55%** under 50.

**Knowledge gaps compound trust issues.** FIS found **42%** of respondents incorrectly believe stablecoins are volatile—despite their design purpose being price stability. This fundamental misunderstanding suggests consumer education is as critical as regulatory clarity.

**Methodological limitations require caution.** The FIS survey has potential conflict of interest given FIS's commercial partnership with Circle (USDC issuer). The Visa Emerging Markets survey (n=2,541) was limited to existing cryptocurrency users in five markets, making results non-generalizable. Most surveys use online-only methodology that may exclude less digitally engaged populations.

---

## DeFi case studies reveal sustainable adoption requires genuine utility, not incentives

The most robust framework for distinguishing organic versus incentive-driven adoption comes from cohort-based retention analysis. Formo's 2025 research on Compound found users who joined during incentive periods had only **7% retention** at six months versus **12.8%** for organically-acquired users. Retained users deposited an average of **$154,000** compared to **$9,000** from inactive users—suggesting high-value users self-select for protocol utility rather than yield farming.

**Post-incentive TVL collapses follow predictable patterns.** When Uniswap's liquidity mining program ended in November 2020, TVL plunged **38-43%** within 24 hours (from $3.07B to approximately $1.75B). SushiSwap's TVL doubled in one week as liquidity providers migrated. In 2025, Unichain's TVL fell **86%** from its all-time high after incentive expiry, with similar patterns at Linea (**-83%**) and Berachain (**-91%**).

**Terra/UST represents the extreme case of unsustainable incentives.** Anchor Protocol held **75%** of all UST circulating supply with $18 billion TVL, sustained by a heavily subsidized **19.5-20% APY**. When confidence collapsed in May 2022, Anchor TVL fell from $18 billion to $280 million in seven days (**98.4%** drop). The LUNA supply hyperinflated from 343 million to 6.53 trillion. University of North Carolina research characterized the dynamics as "analogous to a bank run," while BIS analysis found "larger investors probably cashed out at the expense of smaller holders."

**Protocol-owned liquidity (POL) dramatically outperforms traditional liquidity mining.** Savvy on Arbitrum achieved approximately **95% retention** of incentive-based liquidity through bonding programs that convert incentives to protocol-owned assets, compared to near-**0% retention** for traditional mining. The Return on Efficiency (ROE) metric—how much incentive spend converts to lasting protocol value—distinguishes sustainable programs from mercenary capital attraction.

**SocialFi provides a cautionary tale for incentive-dependent models.** Friend.tech peaked at 100,000 users in 12 days with $62.2 million inflows and briefly surpassed Ethereum in daily revenue. Monthly revenue subsequently fell **90%** from peak, with daily active users dropping to "as low as a dozen." Nansen analyst Martin Lee observed: "As SocialFi networks are incentives-driven, they tend to follow the same trend... typically fizzles out before they manage to reach escape velocity."

**Blur versus OpenSea illustrates the limits of incentive-driven market share.** Blur peaked at over **50%** NFT market share in early 2023 through zero trading fees and aggressive airdrops (300M BLUR tokens worth $186M in Season 2). After Blast token launch reduced rewards, OpenSea clawed back share to **71.5%** by December 2025. Notably, **76.7%** of BLUR airdrop recipients sold their tokens, and **11%** of Blur volume was wash trading according to Dune Analytics.

**Protocols demonstrating sustainable models share common characteristics:** genuine product-market fit beyond yield, protocol-owned liquidity, revenue from actual usage (not token emissions), focus on re-engagement over pure acquisition, institutional infrastructure integration, and minimal dependence on continuous emissions. Liquity exemplifies this approach with zero-interest loans, a 0.5% one-time borrowing fee, no active governance, and no continuous token emissions required.

---

## Payment network history offers actionable playbook for overcoming incumbents

Academic research on two-sided markets, particularly Rochet and Tirole's foundational work, establishes that **price structure**—not just level—determines platform success. The "chicken-and-egg problem" where "given any pair of positive prices, no consumer joins from either side" can be overcome by subsidizing one side through monetary payments or additional services. The ability to charge different prices on two sides is key to overcoming this coordination failure.

**M-Pesa's Kenya success (2007-2010) provides the most instructive case study.** Within three years, the service reached 9 million customers (**40%** of Kenyan adults), processing $320 million monthly in P2P transfers (**10%** of Kenyan GDP annualized). Six strategies drove adoption:

- **Regulatory arbitrage**: Central Bank of Kenya "allowed Safaricom to operate M-PESA as a payments system, outside the provisions of the banking law" with a "wait and see approach."
- **Dominant platform leverage**: Safaricom's **80%** mobile market share provided brand trust, 100,000 airtime resellers as distribution, and marketing resources.
- **Agent network as infrastructure**: Two-tier structure grew to 40,000+ agents providing cash-in/cash-out—5x the combined count of PostBank branches, post offices, bank branches, and ATMs.
- **"Send money home" killer use case**: Focused on domestic remittances exploiting rural-urban migration (**17%** of households depended on remittances).
- **Two-sided market mechanics**: Free registration and deposits removed adoption barriers; sending to non-registered users (higher fee to sender, free to receiver) incentivized recipient registration.
- **Trust-building mechanisms**: Instant SMS confirmation, paper logbooks with signatures, and linkage to trusted Safaricom corporate brand.

**M-Pesa's Tanzania failure illustrates context-dependence.** Vodacom had only **41%** market share (versus 80% in Kenya), a smaller agent network concentrated in cities, and a less collaborative regulatory relationship. "Send money home" didn't resonate with Tanzanian consumers.

**Alipay and WeChat Pay demonstrate platform ecosystem integration.** Alipay launched in 2003 as escrow for Taobao, solving the fundamental trust problem in Chinese e-commerce ("Alibaba held the money until the buyer signed off on receiving the goods"). WeChat Pay embedded payments in a dominant messaging app with 900+ million users. Both leveraged QR codes for near-zero merchant adoption costs (no POS terminal required). They now hold combined **93%+** of China's mobile payment segment with over **$5.5 trillion** in annual mobile payments.

**Zelle demonstrates that late entry can succeed through incumbent partnerships.** Launched seven years after Venmo, Zelle surpassed competitors in transaction volume (**$806 billion** in 2023) by integrating into 2,100+ bank apps with existing customer relationships rather than requiring a separate download. Zelle leveraged existing bank trust instead of building it from scratch.

**Wise (TransferWise) built infrastructure as competitive moat.** The company processes **$154 billion** annually with **63%** of cross-border payments completed in under 20 seconds. The key insight: "The money never actually crosses borders"—balancing funds between accounts in different countries eliminates correspondent banking costs. Wise Platform now offers white-label infrastructure to 85+ partners including Morgan Stanley, Standard Chartered, Nubank, and Monzo.

**Directly applicable strategies for stablecoins include:**
1. **Subsidize one side to bootstrap networks**: Merchant acceptance subsidies (lower fees than cards) can build acceptance before consumer demand materializes.
2. **Leverage existing platforms**: Integration with crypto exchanges, fintech apps, or traditional banks provides distribution and trust transfer.
3. **Identify specific killer use cases**: Cross-border B2B payments or specific remittance corridors with high incumbent fees offer entry points.
4. **Build infrastructure for others**: A "Wise Platform" model allowing banks/fintechs to use stablecoin rails reduces friction for institutional adoption.
5. **Solve trust through transparency**: Regular attestations, clear reserve backing, and audit transparency mirror Alipay's escrow trust-building.

**Unique stablecoin challenges include:** no existing user base to leverage (unlike Alipay/Taobao or WeChat Pay/messaging), more hostile regulatory environments than M-Pesa faced, technical complexity requiring wallets and key management, crypto volatility perception even for stablecoins, and competition from CBDCs and real-time payment rails (FedNow, PIX, UPI).

---

## Conclusion: Adoption requires solving trust, friction, and sustainability simultaneously

The evidence reveals a stablecoin market with **substantial automated activity masking limited genuine user adoption**, strong latent consumer interest contingent on bank involvement, significant UX friction despite recent innovations, and persistent challenges with sustainable growth beyond incentives.

**The 71% bot volume figure is directionally accurate but methodologically imprecise**—conflating wash trading, legitimate market-making, and high-frequency arbitrage. True wash trading likely represents a smaller subset, though precise measurement remains elusive.

**Consumer trust hinges on institutional intermediation.** The consistent finding across surveys that 63-77% of consumers prefer bank-mediated stablecoin access suggests go-to-market strategies should prioritize financial institution partnerships over direct-to-consumer approaches—a significant departure from crypto's disintermediation ethos.

**UX innovations address necessary but insufficient conditions.** Embedded wallets, account abstraction, and gas abstraction meaningfully reduce friction, but retention data suggests technical accessibility alone doesn't drive sustainable engagement. The **69%** gas error rate problem has solutions; the **63%** consumer confidence gap requires different interventions.

**Incentive-driven growth exhibits predictable collapse patterns.** The **7% versus 12.8%** retention differential between incentive-acquired and organic users, combined with **80%+** TVL drops post-incentive, suggests sustainable adoption requires genuine utility—not emissions programs.

**Payment network history offers actionable precedent.** M-Pesa, Alipay, and Wise succeeded through regulatory navigation, platform leverage, killer use case identification, and infrastructure building for third parties. Stablecoins face unique challenges including technical complexity and regulatory uncertainty, but the two-sided market playbook remains applicable.

The path to stablecoin adoption runs through traditional finance, not around it.

---

## Sources

Here are the primary sources from the research, organized by category:

**Blockchain Analytics & Industry Reports**
- CEX.io Q3 2025 Stablecoin Report — [TradingView](https://www.tradingview.com/news/cointelegraph:7ef5b41d2094b:0-over-70-of-stablecoin-transactions-in-q3-linked-to-bots-report-finds/)
- Visa/Allium Labs Stablecoin Dashboard — [Visa](https://corporate.visa.com/en/sites/visa-perspectives/trends-insights/making-sense-of-stablecoins.html)
- Chainalysis 2025 Wash Trading Analysis — [Chainalysis](https://www.chainalysis.com/blog/crypto-market-manipulation-wash-trading-pump-and-dump-2025/)
- TRM Labs 2025 Crypto Adoption Report — [TRM Labs](https://www.trmlabs.com/reports-and-whitepapers/2025-crypto-adoption-and-stablecoin-usage-report)
- Coinbase Institutional Stablecoin Research — [Coinbase](https://www.coinbase.com/institutional/research-insights/research/market-intelligence/stablecoins-new-payments-landscape)

**Academic Research**
- NBER Working Paper on Crypto Wash Trading — [NBER](https://www.nber.org/papers/w30783)
- Management Science (INFORMS) Wash Trading Study — [INFORMS](https://pubsonline.informs.org/doi/10.1287/mnsc.2021.02709)
- Rochet & Tirole Two-Sided Markets — [Oxford Academic](https://academic.oup.com/jeea/article/1/4/990/2280902)
- Northwestern Two-Sided Markets & Network Effects — [Northwestern](https://faculty.wcas.northwestern.edu/apa522/Two-Sided-Market-and-Network-Effects.pdf)

**Consumer Surveys**
- FIS Stablecoin Adoption Survey (Nov 2025) — [FIS](https://www.fisglobal.com/about-us/media-room/press-release/2025/fis-research-banks-hold-the-key-to-stablecoin-adoption)
- Motley Fool Stablecoin Usage Survey — [Motley Fool](https://www.fool.com/research/stablecoin-usage-trends-survey/)
- Pew Research Crypto Confidence Survey — [Pew Research](https://www.pewresearch.org/short-reads/2024/10/24/majority-of-americans-arent-confident-in-the-safety-and-reliability-of-cryptocurrency/)
- Federal Reserve SHED Crypto Payments Data — [Kansas City Fed](https://www.kansascityfed.org/research/payments-system-research-briefings/us-consumers-use-of-cryptocurrency-for-payments/)
- EY-Parthenon Institutional Stablecoin Survey — [EY PDF](https://www.ey.com/content/dam/ey-unified-site/ey-com/en-us/insights/financial-services/documents/cs-eyp-stablecoin-survey.pdf)

**UX & Wallet Infrastructure**
- Privy Embedded Wallets — [Privy](https://www.privy.io/)
- RIF Technology Crypto Entry Barriers Research — [RIF](https://rif.technology/content-hub/crypto-entry-barriers/)

**Payment Network Case Studies**
- World Bank M-Pesa Case Study — [World Bank PDF](https://documents1.worldbank.org/curated/en/638851468048259219/pdf/543380WP0M1PES1BOX0349405B01PUBLIC1.pdf)
- CGAP China Digital Payments Revolution — [CGAP](https://www.cgap.org/research/publication/china-digital-payments-revolution)
- CGAP Alipay/WeChat Pay Rural Users — [CGAP PDF](https://www.cgap.org/sites/default/files/Brief-Chinas-Alipay-and-WeChat-Pay-Dec-2017.pdf)
- Zelle Transaction Volume Analysis — [Tearsheet](https://tearsheet.co/data-snacks/venmo-and-cash-app-competitor-zelle-is-closing-in-on-its-1-trillion-payments-volume-target/)
- Wise Cross-Border Payments Model — [PYMNTS](https://www.pymnts.com/news/payments-innovation/2020/transferwise-future-of-cross-border-payments/)

**DeFi Retention & Incentives**
- Friend.tech Collapse Analysis — [DL News](https://www.dlnews.com/articles/defi/socialfi-rose-in-popularity-last-year-before-falling/)
- CoinDesk Visa Methodology Critique — [CoinDesk](https://www.coindesk.com/opinion/2024/05/07/what-visas-organic-stablecoin-report-misses)
