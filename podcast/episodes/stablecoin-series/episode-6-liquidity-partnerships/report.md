# The Hidden Infrastructure: How Stablecoins Actually Become Usable

The stablecoin market has grown to approximately $300 billion as of December 2025, with Tether's USDT and Circle's USDC controlling a combined 84% of the market. But here is a question that rarely gets asked: What transforms a stablecoin from a technical concept backed by reserves into something you can actually use to buy coffee, trade on an exchange, or send money across borders? The answer lies in an invisible infrastructure layer that most users never think about—the market makers, exchange partnerships, and liquidity networks that determine whether a stablecoin thrives or dies in obscurity.

Consider this stark reality: Tether allows only about 6 entities per month to directly redeem USDT for dollars, while Circle permits approximately 521 arbitrageurs monthly access to USDC redemptions, according to Federal Reserve research. This 87-fold difference in arbitrage access creates fundamentally different market dynamics for the two largest stablecoins. The implication is profound: the usability of a stablecoin depends not on its technical design or reserve backing alone, but on the intricate web of financial relationships that connect it to actual trading venues and users.

This episode examines the mechanisms that separate successful stablecoins from failed ones—the market making partnerships that maintain price stability, the exchange listing requirements that determine access, the decentralized exchange integrations that enable permissionless trading, and the multi-chain strategies that address liquidity fragmentation. We will explore why the cold-start problem remains the primary barrier for new entrants, what it actually costs to establish viable liquidity, and how regulatory developments like the GENIUS Act and MiCA are reshaping the competitive landscape.

---

## Section 1: Foundation—Why Liquidity Infrastructure Determines Stablecoin Success

### The Liquidity Paradox

A stablecoin's entire value proposition depends on maintaining a tight peg to its reference asset. But maintaining that peg requires something that cannot be engineered through smart contracts alone: deep, continuous liquidity across multiple trading venues. This creates what economists call the cold-start problem—no users because there is no liquidity, and no liquidity because there are no users.

Think of it like opening a currency exchange booth at an airport. You can display whatever exchange rate you want on your sign, but if you have no currency in your cash drawer, that rate is meaningless. The first traveler who walks up cannot actually exchange money, so they walk past. Word spreads that your booth has no currency, and soon nobody even checks your rates. Meanwhile, the booth next door with stacks of bills visible does brisk business, attracting even more capital as travelers trust that it can handle their transactions.

The market has evolved a sophisticated solution to this paradox: professional market making. Unlike speculative trading, market making for stablecoins involves coordinated operations that balance inventory management across exchanges, execute cross-venue arbitrage to maintain price consistency, and manage positions across multiple blockchain networks simultaneously. According to industry data, top market makers like Wintermute process approximately $2.24 billion in daily trading volume across more than 50 exchanges, while DWF Labs handles over $5 billion daily across 60 centralized and decentralized venues (Perplexity Research, December 2025).

Market makers profit from the bid-ask spread—the difference between what buyers pay and sellers receive. For stablecoins specifically, this spread tends to be extremely tight, often just a few basis points (hundredths of a percent). The margin is small, but the volumes are enormous. More importantly, market makers serve an essential infrastructure function: they ensure that price deviations from the peg remain minimal and that traders can execute transactions quickly with minimal price impact.

### The Market Maker Ecosystem

The competitive landscape of institutional market makers has crystallized around a small number of highly capitalized firms. Understanding who these players are and how they operate illuminates how stablecoin liquidity actually functions.

**Wintermute** stands out as one of the largest cryptocurrency market makers globally, recording approximately $2.24 billion in daily trading volume and maintaining partnerships with over 50 exchanges including major players like Coinbase, Kraken, and Bybit. The firm supports over 350 spot and CFD trading pairs, enhancing trading efficiency across both centralized and decentralized venues. Wintermute's business model reflects the capital-intensive nature of modern market making—the firm must maintain sufficient inventory across multiple chains, manage counterparty relationships with exchanges and issuers, and execute trades with sub-millisecond precision to capture the spreads that define profitability (Perplexity Research, December 2025).

**Jump Trading**, operating through its Jump Crypto division, brings extensive experience from traditional finance into the cryptocurrency market. Jump leverages high-frequency algorithmic trading technologies and advanced research capabilities to provide deep liquidity for both spot and derivative markets. Jump's presence in the stablecoin space is particularly significant because its traditional finance pedigree has lent credibility to institutional adoption of blockchain-based assets. The firm's ability to seamlessly move between traditional markets and decentralized protocols has established it as a critical bridge between old and new financial worlds. However, Jump has faced legal challenges—in December 2025, a $4 billion lawsuit alleged Jump profited from its role in the 2022 Terra collapse (Grok Research citing WSJ and CoinDesk, December 2025).

**Cumberland DRW**, a subsidiary of the trading firm DRW with decades of experience in traditional financial markets, has leveraged its institutional infrastructure to become a prominent crypto market maker. Cumberland provides liquidity particularly valuable for institutional investors seeking to execute large trades without moving prices dramatically. The firm's emphasis on over-the-counter (OTC) trading makes it essential for large-scale stablecoin transactions that would cause significant slippage on exchange order books.

**DWF Labs** has become one of the largest market-making service providers, maintaining partnerships with over 700 organizations and operating across 60 centralized and decentralized venues. The firm records over $5 billion in daily market-making volumes and has announced plans for Falcon Finance, a synthetic stablecoin expected to offer yields of 12-19%. DWF Labs' model emphasizes helping early-stage projects bootstrap liquidity while providing customized algorithmic strategies. Notably, DWF Labs operates as a "principal market maker"—investing its own capital rather than simply providing matching services—which creates both alignment and potential conflicts of interest (Perplexity Research and Grok Research, December 2025).

**GSR Markets** and **Kairon Labs** focus on different segments. GSR emphasizes derivatives and structured products for institutional clients, while Kairon Labs specializes in tailoring market-making services specifically to emerging token projects. **B2C2** provides 24/7 liquidity and personalized services for institutional investors, with particular emphasis on OTC trading and prime brokerage.

The concentration of market-making activity among a small number of firms creates both efficiency and risk. For efficiency, the specialization and capital density of major market makers enables tight spreads and deep liquidity that benefits all market participants. For risk, this concentration means that disruptions to key market makers could have cascading effects across multiple exchanges and trading venues.

### Primary Markets vs. Secondary Markets

Understanding stablecoin liquidity requires grasping a critical distinction: the difference between primary markets and secondary markets. The primary market is where stablecoins are originally issued and redeemed directly with the issuer at par value—exactly one dollar for one stablecoin, or vice versa. The secondary market encompasses all the trading venues where stablecoins change hands at market-determined prices.

Most fiat-backed stablecoin issuers restrict direct primary market access to a small set of institutional participants who meet strict know-your-customer and anti-money-laundering requirements, agree to minimum transaction thresholds (often $100,000 or more), and operate in approved jurisdictions (Federal Reserve FEDS Notes, 2025). Tether is particularly restrictive, reportedly requiring a minimum of $100,000 USDT per mint transaction on-chain. Circle allows institutional customers to mint and redeem USDC directly but restricts the process to banking hours during the U.S. business day.

This restriction proved problematic during the March 2023 crisis when Circle's primary market operations were suspended over a weekend due to SVB exposure. Retail users discovered they had no contractual right to redemption at $1—they could only sell in secondary markets. As the weekend stretched on and uncertainty mounted, USDC traded as low as $0.88 on some exchanges. Institutional users with direct Circle relationships knew they could redeem at par value when banking hours resumed, but retail users had no such assurance and faced the full risk of market prices.

This creates a two-tiered system. Institutional users with direct redemption rights face a hard ceiling of $1 on what they would pay (why pay more when you can redeem directly?) and a hard floor of $1 on what they would accept (why sell for less when you can mint directly?). This creates automatic arbitrage opportunities for privileged participants but offers no such protections for retail users who can only trade on secondary markets. During stress events, retail users face the full risk of market prices diverging from par value.

### The Arbitrage Mechanism: How Pegs Are Maintained

The connection between primary and secondary markets is maintained by arbitrageurs—specialized traders who profit from price discrepancies. When a stablecoin trades at a discount in secondary markets (say, $0.99 instead of $1.00), arbitrageurs can purchase it cheaply in secondary markets and redeem it for exactly $1.00 from the issuer, pocketing the difference minus transaction costs. When it trades at a premium ($1.01), arbitrageurs can mint new stablecoins from the issuer at $1.00 and sell them in secondary markets at the higher price.

This mechanism sounds simple, but its effectiveness depends entirely on who has access to primary markets. The Federal Reserve research finding that USDT has approximately 6 active arbitrageurs monthly while USDC has approximately 521 reveals a fundamental difference in market structure. Concentrated arbitrage (Tether's model) creates a "squeezed" situation where major arbitrageurs capture outsized spreads, while distributed arbitrage (Circle's model) keeps secondary market prices tightly pegged to par value.

The empirical evidence supports this interpretation. USDT secondary market prices show a median discount of 11 basis points (0.11%) compared to just 1 basis point (0.01%) for USDC, according to Federal Reserve analysis. On large transactions, this difference matters: moving $10 million through USDT might cost $11,000 more in spread than the same transaction in USDC.

This reveals a counterintuitive dynamic: concentrated arbitrage is efficient for peg maintenance but fragile for price stability during stress. When few arbitrageurs control primary market access, they can quickly move large volumes to capitalize on small deviations, keeping prices in secondary markets tightly pegged. However, this same concentration means that if reserve assets become questioned or difficult to liquidate, the arbitrageurs lose their ability to execute redemptions, and the peg breaks suddenly. Distributed arbitrage like USDC's model provides somewhat less pressure for peg maintenance under normal conditions but proves more resilient during stress because many independent arbitrageurs can respond to discourage runs.

### Capital Requirements for Viable Liquidity

What does it actually cost to establish minimum viable liquidity for a new stablecoin? The research reveals a clear capital hierarchy:

| Stage | Minimum Capital Requirement |
|-------|----------------------------|
| DEX Launch | $1 million per major trading pair |
| Professional Market Maker Engagement | $1-5 million per trading pair |
| Centralized Exchange Listing Ready | $10-50 million guaranteed depth |
| Institutional Adoption Threshold | $100 million+ 24-hour volume, spreads under 10 basis points |

These figures represent working capital that must be deployed and maintained, not one-time costs. A market maker providing liquidity for a stablecoin needs sufficient inventory on both sides of the order book across multiple venues. If the stablecoin trades on five major exchanges and three DEX platforms, the capital requirements multiply accordingly.

Market making agreements typically involve multiple compensation mechanisms. Trading fee rebates range from 0.01% to 0.05% per transaction, with exchanges offering maker-taker fee structures that favor liquidity providers. For new stablecoin projects, token allocations of 1-5% of total supply are common, with vesting schedules stretching 12 to 48 months and performance-based bonus allocations tied to liquidity metrics.

Industry best practice now recommends that investment contracts should be separated from market-making agreements to avoid conflicts of interest—though not all firms follow this guideline. When a market maker both invests in a project and provides liquidity, they may have incentives to manipulate prices in ways that benefit their investment position rather than maintain stable spreads. The DWF Labs model, which explicitly combines investment and market-making, has attracted both praise for alignment and criticism for potential conflicts (Perplexity Research, December 2025).

---

## Section 2: Evidence—How Liquidity Infrastructure Actually Works

### The Exchange Listing Gauntlet

Centralized exchanges remain the primary venue where retail and institutional traders interact with stablecoins. Listing on major exchanges like Coinbase and Binance represents a critical milestone, but the process is far more rigorous than most realize.

Coinbase operates a formal application process that captures the institutional standards now expected in the ecosystem. Project teams submit questionnaires covering whitepapers, team backgrounds, tokenomics, source code, block explorers, and third-party security audits. The application then undergoes business evaluation assessing market demand, community traction, and technical integration requirements. Most critically, each asset faces a core review process encompassing three dimensions: legal assessment of whether trading the token would constitute a securities transaction, compliance and risk mitigation review for financial crime risks, and technical security evaluation of contract code and operational risks (Perplexity Research citing Coinbase listing documentation).

On average, due diligence takes approximately one week, and trading can be enabled within two weeks of approval. However, timelines vary dramatically based on token complexity, whether Coinbase already supports the network, project team responsiveness, and technical work required for custody and trading. Tokens on supported networks—which as of late 2025 include Ethereum, Base, Solana, Arbitrum, Optimism, Polygon, and Avalanche—can be supported faster than new chains, since adding blockchain support requires dedicated engineering teams to build custom node infrastructure.

The evaluation framework reveals the institutional gatekeeping that now characterizes CEX participation. Beyond core legal, compliance, and technical reviews, Coinbase also assesses market factors including trading demand, market capitalization, liquidity, traction measured through holder numbers and active wallets, and qualitative signals such as community sentiment and team track record. These evaluations involve product, legal, and technical specialists who collectively assess whether a token represents a sound addition to the exchange's offering.

Common reasons for delays or rejections include incomplete applications, lack of information on governance or tokenomics, failure to notify Coinbase of major project changes, and issues related to the degree of centralized control in protocol architecture. This emphasis on decentralization and distributed governance reflects institutional recognition that highly centralized tokens present both technical and regulatory risks.

Binance operates a similar but somewhat more opaque process, having received thousands of applications annually and declining to charge fixed listing fees. The exchange explicitly recommends against spamming their team or relying on third-party "agents" to expedite approval, suggesting past practice had created problems. Achieving listing on tier-one exchanges requires not only sound technical architecture and legal compliance but also that project teams have invested substantially in market-making partnerships to ensure liquidity on day one.

Listing costs remain largely undisclosed for major exchanges, though they can range from free (merit-based listings) to millions in "marketing fees." Mid-tier exchanges typically charge $50,000 to $500,000. DEXs, by contrast, require only gas costs plus initial liquidity provision—often making them the starting point for new stablecoins before pursuing centralized exchange listings.

### The DEX Ecosystem: Where Stablecoins Achieve Composability

Decentralized exchanges have emerged as critical infrastructure for permissionless trading and integration with the broader DeFi ecosystem. Uniswap dominates the landscape, accounting for approximately 55% of all DEX transactions as of 2024 (Perplexity Research). The protocol operates across multiple networks including Ethereum, Arbitrum, Optimism, Polygon, and Base.

Uniswap V3's concentrated liquidity mechanism transformed the economics of stablecoin liquidity provision. Rather than having capital locked across the entire price spectrum even when trading occurs only in a narrow band, concentrated liquidity allows providers to concentrate their capital in the range where trading actually occurs. A provider might deposit USDC and USDT into a pool but specify that their capital will only be active in the range of $0.9999 to $1.0001, capturing fees from that narrow but heavily-traded band. This innovation potentially increases capital efficiency by up to 4,000 times compared to earlier AMM designs.

The mechanics of concentrated liquidity are particularly important for stablecoin pairs where price ranges are predictable and narrow. When price movements exceed the provider's specified range, the position effectively exits (all USDC with no USDT if price rises, or all USDT with no USDC if price falls), requiring active management by the provider to maintain exposure. This active management requirement represents friction compared to passive liquidity provision, but for professional market makers and sophisticated liquidity providers, the enhanced fee capture justifies the operational complexity.

**Curve Finance** occupies a specialized but critically important role as a low-slippage trading platform optimized specifically for pegged assets. Curve's bonding curve algorithm—what the protocol calls the StableSwap invariant—enables efficient trades between assets with similar prices. For stablecoins paired with stablecoins, Curve delivers minimal price impact even on large trades, making it the dominant venue for stablecoin-to-stablecoin swaps and essential infrastructure for arbitrage operations that maintain peg stability (Perplexity Research, December 2025).

The platform that minimizes slippage for a particular use case tends to capture disproportionate volume and liquidity for that use case. Because Curve specializes in low-slippage stablecoin swaps, traders and arbitrageurs have strong incentives to route orders through Curve rather than general-purpose DEXs. This has evolved into a governance dynamic where stablecoin issuers and associated entities compete to influence Curve governance through accumulation of its governance token (CRV) to direct liquidity incentives toward their preferred stablecoins—a phenomenon known as the "Curve Wars."

Major protocols including Convex Finance, Yearn Finance, and StakeDAO have raced to accumulate voting power, recognizing that controlling Curve's incentive distribution translates directly to controlling where liquidity flows. For stablecoin issuers, securing Curve gauge allocations can mean the difference between deep liquidity and shallow markets. Curve's TVL has historically peaked at $19 billion and has remained substantial even during crypto winter periods, reflecting the stability of revenues from stablecoin trading fees.

**PancakeSwap** and other chain-specific DEXs provide regional liquidity infrastructure, with PancakeSwap dominating BNB Chain trading and offering competitive yields for liquidity providers through its token incentive system. The existence of these regional DEXs reflects the reality that each blockchain network has distinct user bases, fee structures, and community preferences, making a one-size-fits-all approach to DEX infrastructure impossible.

### Multi-Chain Fragmentation: The Liquidity Distribution Problem

The distribution of stablecoin liquidity across blockchain networks has become one of the defining challenges of the modern ecosystem. As of late 2025, major stablecoins operate across Ethereum, BNB Chain, Solana, Tron, Arbitrum, Optimism, Base, Polygon, and dozens of others.

The empirical reality is stark:

| Chain | Monthly Stablecoin Volume | Key Stablecoins | Primary Use Case |
|-------|---------------------------|-----------------|------------------|
| Ethereum | $2.8 trillion | USDC, USDT, DAI | DeFi, institutional treasury |
| Tron | $600+ billion (75% USDT) | USDT dominant | Retail remittances, payments |
| Solana | $500 billion | USDC, PYUSD | Consumer payments, trading |
| BSC | $200+ billion | USDT, USDC | Retail trading, gaming |
| L2s (Arbitrum, Optimism, Base) | Growing rapidly | USDC native | DeFi, scaling |

This divergence reflects fundamentally different use cases. Ethereum serves sophisticated DeFi applications, tokenized assets, and institutional treasury management. Tron serves retail-driven remittances and cross-border payments for emerging markets.

**Tron's emergence as a dominant stablecoin settlement layer** merits particular attention because it illustrates how infrastructure evolution is driven by economic incentives rather than technical sophistication alone. Tron reduced its transaction fees by 60% in August 2025, bringing average stablecoin transfer costs down to $0.72 from $4.28, and enabled gas-free USDT transfers through a specialized service. These operational improvements, combined with mobile-wallet accessibility and deep integration with centralized exchanges in Asia, have made Tron the de facto settlement rail for retail users in developing economies.

By Q3 2025, Tron hosted over 46% of global USDT supply (approximately $78 billion) and processed more than 75% of all worldwide USDT transfers. Daily active users reached approximately 2.92 million, with 68% accessing through mobile wallets—a critical statistic for regions where smartphones are the primary gateway to financial services (Grok Research citing Morgan Stanley and McKinsey reports).

This concentration on Tron has systemic implications. Tron's validator structure, heavy reliance on USDT, and limited DeFi ecosystem mean the chain's dominance reflects efficiency and accessibility rather than technical decentralization or composability. The opacity of Tron's activity—most flows originate or terminate in centralized exchanges rather than remaining on-chain—limits the ability of regulators and analysts to assess what economic activities are actually being conducted.

**Solana** has emerged as another critical liquidity hub, with approximately $16 billion in stablecoin supply and roughly $500 billion in monthly trading volume. Solana's value proposition rests on sub-second finality and fees measured in fractions of a cent, making it attractive for high-volume, low-margin payment applications. Major institutions including Visa have specifically designated Solana as a venue for stablecoin settlement, while PayPal launched PYUSD natively on Solana for consumer payments.

**Fragmentation creates specific problems:** scattered capital leads to shallow markets on individual venues, users face complex journeys across bridges when they need to move between chains, pricing becomes inefficient with higher slippage, and bridge security vulnerabilities create ongoing risks. The November 2025 YU stablecoin exploit resulted in a $7.7 million depeg, exposing cross-chain vulnerabilities. A 2025 study noted bridges as major attack vectors, with Elliptic's risk guide highlighting technical and regulatory risks (Grok Research citing OKX and Elliptic reports).

**Solutions being explored** include native issuance on each chain (Circle's approach with USDC), cross-chain messaging protocols (LayerZero, Axelar, Wormhole), unified liquidity standards, and intent-based bridging through platforms like LI.FI and Socket. Circle's Cross-Chain Transfer Protocol (CCTP) enables USDC to be burned on source chains and minted on destination chains, eliminating liquidity pool requirements entirely. Stargate Finance, leveraging LayerZero's messaging protocol, offers unified liquidity pools across 15+ chains with instant finality and native asset support.

### Case Study: USDC's Institutional Ascent

USDC's growth trajectory illustrates what successful liquidity infrastructure looks like in practice. Launched in 2018 with a market cap of approximately $500 million, USDC reached $77 billion by December 2025—representing 75% year-over-year growth.

**Phase 1 (2018-2019): Institutional Foundation.** Circle established the Coinbase partnership from launch, providing immediate access to a major exchange's user base. This was not merely a listing agreement—Coinbase was a founding member of the Centre Consortium that governs USDC. The alignment of incentives meant Coinbase promoted USDC as its preferred stablecoin, integrating it deeply into the exchange's trading pairs and products.

The company implemented full reserve attestations with Grant Thornton as auditor, establishing a transparency standard that would become increasingly valuable as regulatory scrutiny intensified. Circle obtained state money transmitter licenses across the U.S., positioning USDC as a regulated financial instrument rather than merely a crypto token. These moves established credibility that would prove essential for later institutional adoption.

**Phase 2 (2020-2021): DeFi Explosion.** USDC integrated with Compound, Aave, and Uniswap during the yield farming boom. The stablecoin became a primary unit of account in DeFi, driving organic demand beyond speculative trading. When users deposited assets to earn yield or provide liquidity, they needed stablecoins for pairing—and USDC's regulatory clarity made it the preferred choice for risk-conscious participants.

Circle expanded to multiple chains during this period, ensuring USDC was available wherever developers were building. The multi-chain strategy required coordinated liquidity provision across networks, but the payoff was that USDC became the default stablecoin for many DeFi applications regardless of which chain they deployed on.

**Phase 3 (2022-2025): Institutional Integration.** Circle secured partnerships that transformed USDC from a crypto-native asset to infrastructure integrated with traditional finance:

- **BlackRock integration** for tokenized real-world assets, positioning USDC as the settlement currency for institutional tokenization
- **Visa and Mastercard** enabled USDC settlement on their networks, allowing payment processors to settle in stablecoins rather than traditional fiat rails
- **ICE/NYSE partnership** (March 2025) marked entry into traditional exchange infrastructure
- **OCC conditional approval** for Circle to establish First National Digital Currency Bank, N.A., enhancing regulatory standing
- Real-world asset inflows reached $940 million in H1 2025

Circle's regulatory strategy proved particularly consequential. The company pursued MiCA compliance proactively, positioning USDC as the regulatory standard for compliant stablecoins in the EU. When MiCA implementation in December 2024 forced exchanges to delist non-compliant stablecoins, USDC gained market share that might otherwise have been impossible to capture. The company's market cap grew from approximately $42.4 billion at the end of January 2025 to $77 billion by December—a 75% increase driven substantially by regulatory positioning (Perplexity Research and Grok Research, December 2025).

### Case Study: PayPal USD—Platform Leverage Strategy

PayPal's entry into the stablecoin market with PayPal USD (PYUSD) demonstrates a different path to liquidity: leveraging an existing user base rather than building liquidity from scratch.

PYUSD launched in August 2023 with immediate access to PayPal's 400+ million user accounts. Rather than needing to convince users to try a new product, PayPal could offer PYUSD as an option within an app users already trusted and used regularly. The stablecoin gained traction not through DeFi integration or exchange listings but through commerce integration—users could pay merchants with PYUSD, hold it in PayPal wallets, and transfer it to friends through Venmo.

The strategy accelerated in 2025 when PayPal launched PYUSD natively on Solana for consumer payments. The blockchain's sub-second finality and minimal fees made it suitable for retail transactions. PYUSD grew 378% on Solana, partly driven by reward programs offering 4% returns for holding the stablecoin. Market cap expanded from approximately $500 million to $1.4 billion during 2025, representing substantial growth though still small relative to USDT and USDC (Grok Research citing QuickNode, November 2025).

The platform leverage approach solves the cold-start problem differently. Instead of asking "how do we attract users to provide liquidity," PayPal asked "how do we give our existing users a reason to use stablecoins?" The answer was integration with existing payment flows rather than standalone crypto applications. The tradeoff: PYUSD has limited DeFi integration compared to USDC, making it less attractive for sophisticated crypto-native use cases.

### Case Study: Ethena USDe—Innovation and Volatility

Ethena's USDe represents a fundamentally different approach: a synthetic stablecoin backed by delta-neutral hedging rather than traditional reserves. The mechanism works by holding ETH and stETH as collateral while taking offsetting short positions in perpetual futures. The short positions hedge against ETH price movements, creating a theoretically stable position. Yield comes from two sources: staking rewards on stETH and funding rate arbitrage (when longs pay shorts to maintain perpetual futures positions).

The results have been impressive and volatile:

| Period | USDe APY | Market Conditions |
|--------|----------|-------------------|
| 2021 | ~18% | Bull market, positive funding |
| March 2024 (peak) | 67.2% | Extreme bullish sentiment |
| Late 2024 | 11-12% | Market normalization |
| October 2025 | Negative/crash | Funding rate inversion |

USDe rapidly grew to a $9.5 billion market cap at its peak, demonstrating that yield-based strategies can bootstrap liquidity quickly. When traditional stablecoins offer no yield (prohibited under GENIUS Act for payment stablecoins), a product offering 10-20% returns attracts capital rapidly.

However, October 2025 brought a crash that erased $8.3 billion in market cap—a "loss of confidence" event that illustrated the risks of this model. Yield sustainability depends entirely on market conditions—specifically, funding rates remaining positive on perpetual futures. When market sentiment shifts and funding rates invert (shorts pay longs instead of longs paying shorts), the yield disappears and can turn negative. This triggers rapid outflows as holders move to alternatives offering positive returns (Grok Research and Cointelegraph, December 2025).

Importantly, USDe would not qualify as a "payment stablecoin" under the GENIUS Act due to its yield-bearing nature and algorithmic collateral mechanism. The regulatory classification constrains its potential use cases, particularly in jurisdictions implementing the new frameworks. DWF Labs has announced Falcon Finance, a similar synthetic stablecoin expected to offer yields of 12-19%, suggesting continued interest in this model despite regulatory constraints.

### Case Study: The Terra/UST Collapse—Liquidity Lessons

The 2022 Terra/UST collapse provides essential lessons about liquidity infrastructure failures. UST was an algorithmic stablecoin that maintained its peg through arbitrage with the LUNA token rather than traditional reserves. The system concentrated liquidity in a single protocol—Anchor—which offered approximately 20% yields on UST deposits.

At its peak, Terra's ecosystem appeared robust. UST reached $18.7 billion in market cap, making it the third-largest stablecoin. The Anchor protocol held approximately 75% of all UST, generating yields through a combination of borrowing fees and subsidies from the Luna Foundation Guard. But this concentration created fragility that became apparent when confidence broke.

**When the collapse began, several liquidity-related factors proved fatal:**

**Insufficient depth to absorb selling pressure.** Unlike USDT or USDC with institutional market makers committed to maintaining spreads, UST had no formal backstop agreements. When large holders began exiting (starting with withdrawals of approximately $2 billion from Anchor in early May 2022), there was no capital committed to absorbing the selling. Market makers who might have provided liquidity for other stablecoins had no relationship with Terra and no incentive to deploy capital.

**Concentrated liquidity in single protocol.** Anchor held approximately 75% of all UST. When withdrawals accelerated, the lack of diversified trading venues meant selling pressure concentrated rather than dispersed. The Curve pool for UST became severely unbalanced within hours, with the stablecoin side growing to 90%+ of the pool as sellers dumped UST.

**No formal market maker relationships.** The Terra ecosystem lacked the institutional partnerships that characterize successful stablecoins. Wintermute, Jump, Cumberland—none had formal agreements to maintain liquidity for UST. When the peg slipped below $0.98, no professional market makers were positioned or incentivized to defend it by buying UST and redeeming it through arbitrage.

**Death spiral dynamics.** The algorithmic mechanism that was supposed to maintain the peg instead accelerated its collapse. As UST fell below $1, arbitrageurs could mint LUNA by burning UST, theoretically capturing the discount. But this flooded the market with LUNA, crashing its price and reducing the effective backing for remaining UST. The mechanism that should have restored the peg instead became a weapon against it.

Jump Trading is now facing a $4 billion lawsuit alleging it profited from the collapse through its role as a market maker that allegedly helped prop up LUNA prices before the crash while positioning to profit from the inevitable failure (Grok Research citing WSJ, December 2025).

### Case Study: Smaller Stablecoins—Alternative Strategies

Several smaller stablecoins have built liquidity without the resources of Tether or Circle, offering lessons for new entrants:

**FRAX** uses a partially algorithmic approach, maintaining reserves that back a portion of supply while using algorithmic mechanisms for the remainder. This hybrid model reduces capital requirements while maintaining stability. FRAX has focused on DeFi integration, becoming deeply embedded in protocols like Curve and Convex. Rather than competing for general payment use, FRAX carved a niche as DeFi infrastructure.

**LUSD** (Liquity USD) takes a maximally decentralized approach, backed entirely by ETH collateral with no centralized entity controlling redemptions. The protocol operates without governance, making it censorship-resistant but also inflexible. LUSD maintains liquidity through incentivized stability pools where users can deposit LUSD to earn ETH from liquidations. This community-driven model has sustained approximately $500 million in circulation without institutional market maker agreements.

**GHO** (Aave's stablecoin) leverages existing protocol infrastructure. Users mint GHO against their Aave deposits, instantly creating utility for the stablecoin within Aave's existing ecosystem. AAVE token holders receive discounts on GHO borrowing rates, aligning incentives between governance token holders and stablecoin users. This protocol-owned liquidity model bootstraps demand through existing user relationships rather than external partnerships.

---

## Section 3: Application—Navigating the New Liquidity Landscape

### Regulatory Frameworks Reshaping Market Structure

The regulatory environment underwent a fundamental transformation in 2025, with direct implications for liquidity infrastructure.

**The GENIUS Act (United States, enacted July 18, 2025)** creates a comprehensive framework for "payment stablecoins." The Act represents the most significant intervention in the digital asset market by the United States government to date. Key provisions include:

- **Permitted Issuers Only:** Only regulated entities can issue payment stablecoins: OCC-chartered non-bank issuers, subsidiaries of insured depository institutions, or approved state entities
- **Reserve Requirements:** One-to-one reserve backing with high-quality liquid assets (U.S. dollars, short-term Treasury bills, certain government-backed repo agreements)
- **Algorithmic Ban:** Prohibition on algorithmic stablecoins (moratorium pending Treasury study)
- **No Yield:** Prohibition on yield or interest payments to holders—differentiating stablecoins from securities or deposits
- **Transparency:** Monthly public attestations and annual independent audits required
- **Foreign Issuer Rules:** Foreign issuers must register with OCC and meet U.S. comparability standards

The Act makes it unlawful for any digital asset service provider to facilitate trading of non-compliant stablecoins in the United States after the transition period ends (January 18, 2027, or 120 days after final regulations). This provision effectively bans listing of offshore, unregulated stablecoins on U.S. platforms.

**Extraterritorial reach** creates particular challenges for foreign issuers. Foreign stablecoins can only be listed if the issuer is subject to a foreign regulatory regime deemed "comparable" by the U.S. Treasury and if the issuer registers with the OCC. This creates a high barrier for offshore issuers like Tether to maintain U.S. listings without submitting to direct U.S. federal oversight (Gemini Research citing Latham & Watkins and Arnold Porter analyses).

**MiCA (European Union, fully effective December 30, 2024)** establishes a comprehensive licensing regime for Crypto-Asset Service Providers (CASPs):

| CASP Class | Minimum Capital | Activities Covered |
|------------|-----------------|-------------------|
| Class 1 | 50,000 euros | Advisory, order transmission |
| Class 2 | 125,000 euros | Custody, administration |
| Class 3 | 150,000 euros | Trading platforms |

Beyond base capital, MiCA imposes operational burdens that impact market-making strategies. CASPs must maintain own funds equal to the higher of minimum capital requirements or one-quarter of fixed overheads from the preceding year. This "fixed overhead" rule significantly increases capital costs for market makers with high operational expenses.

MiCA also requires market makers to implement systems to detect and report market abuse, including surveillance technology to monitor for wash trading or manipulation. This increases the technological barrier to entry. Significant stablecoins are supervised by the European Banking Authority, with additional requirements for reserve management and liquidity.

MiCA introduces friction for USD-denominated stablecoins in the EU. While not strictly banned, "significant" non-Euro stablecoins face potential transaction caps if used widely as a means of payment. This has led some EU exchanges to delist non-compliant USD stablecoins or restrict their use to professional traders. The delisting of USDT and DAI on European platforms following MiCA implementation demonstrated regulatory power to reshape market structure (Gemini Research citing KPMG and Dechert analyses).

**Basel III Standards (effective January 2025)** create bifurcated capital treatment for banks holding stablecoins:

- **Group 1b (compliant stablecoins):** Capital requirements based on risk weights of underlying assets (e.g., Treasury bills)
- **Group 2 (non-compliant):** 1,250% risk weight, effectively requiring dollar-for-dollar capital

This bifurcation means institutional market makers (banks) will only provide liquidity for Group 1b assets, deepening liquidity for compliant tokens while starving non-compliant ones. A bank providing $100 million in liquidity for a Group 2 stablecoin must hold $100 million in regulatory capital against that exposure—an impossible economics for market making (Gemini Research citing BIS standards).

### Comparative Regulatory Analysis

| Feature | United States (GENIUS Act) | European Union (MiCA) | Hong Kong/Singapore |
|---------|---------------------------|----------------------|---------------------|
| Primary Focus | Dollar dominance, banking integration | Consumer protection, monetary sovereignty | Innovation hubs, regional competitiveness |
| Reserve Rules | 1:1 Cash/Treasuries, strict segregation | Significant portion in EU bank deposits | 100% backing required |
| Algorithmic | Banned pending study | Marginalized, strict disclosure | Excluded from stablecoin licensing |
| Yield-Bearing | Prohibited | Restricted | Case-by-case |
| Foreign Issuers | Must register with OCC | Passporting within EU | Local licensing required |
| Market Access | Closed system | Passporting across 27 states | Regional only |

**Entrenchment risk:** High compliance costs may paradoxically entrench the USDT/USDC duopoly. Only well-capitalized incumbents can afford monthly audits, 1:1 Treasury management, multi-jurisdiction licensing, and the legal infrastructure required for compliance. A new stablecoin issuer must now effectively become a bank subsidiary or federally qualified non-bank—a barrier that protects incumbents from competition.

**USDT-specific challenge:** The GENIUS Act requirement for foreign issuers to register with OCC and meet U.S. comparability standards creates significant uncertainty for Tether, which is domiciled in the British Virgin Islands. However, Tether's Q2 2025 attestation showed assets exceeding liabilities and holdings of over $127 billion in U.S. Treasury securities—positioning the firm as one of the largest holders of U.S. government debt globally. This transparency improvement, potentially driven by regulatory pressure, enhances market confidence in USDT's backing.

### Exchange Responses to Regulatory Fragmentation

Exchanges are responding to regulatory divergence through three primary strategies:

**Geofencing and Delisting:** Exchanges are segregating user bases by jurisdiction. EU users on major platforms have lost access to unauthorized USD stablecoins, while U.S. users face restrictions on foreign stablecoins not registered with the OCC. Coinbase planned delistings of non-compliant stablecoins by year-end 2024; Binance restricted access to USDT for EU users in March 2025.

**Dual Entities:** Exchanges are establishing separate legal entities for different jurisdictions—MiCA-licensed entities in Europe, GENIUS-compliant entities in the U.S.—to ring-fence liability and liquidity. This approach increases operational complexity but allows continued operation across regulatory boundaries.

**Liquidity Segmentation:** The global liquidity pool is fracturing into regionally regulated segments. This creates arbitrage opportunities between U.S.-compliant and EU-compliant stablecoin pairs, but also reduces cross-border capital efficiency and increases costs for global operations.

### Protocols for Evaluating Stablecoin Liquidity

For practitioners assessing stablecoin liquidity, these metrics provide actionable guidance:

**Spread Analysis:**
- Measure bid-ask spreads across major venues during both normal and volatile periods
- USDC benchmark: median spreads approximately 1 basis point
- USDT benchmark: median spreads approximately 11 basis points
- Spreads above 20 basis points suggest inadequate market maker coverage
- Check spreads at different order sizes: $10K, $100K, $1M, $10M

**Depth Analysis:**
- Check 1% and 2% market depth on major exchanges
- For institutional use: require at least $10 million available within 1% of current price
- Distributed depth across multiple venues is more valuable than concentrated depth on single exchange
- Assess depth recovery time after large trades

**Arbitrageur Activity:**
- Look for evidence of active arbitrage: healthy stablecoins maintain tight pegs even during volatile periods
- Extended deviations above 50 basis points from par suggest insufficient arbitrage access
- Check primary market accessibility: who can redeem, at what minimums, during what hours?

**Multi-Chain Coverage:**
- Assess native issuance vs. bridged tokens
- Native issuance (Circle's CCTP) is generally safer than third-party bridges
- Check which chains the stablecoin supports natively vs. through bridges
- Evaluate bridge security history and audit status

**Regulatory Compliance:**
- Verify compliance with relevant frameworks for your jurisdiction
- GENIUS Act compliance required for U.S. exchange listings by January 2027
- MiCA compliance required for EU operations as of December 2024
- Basel III Group 1b classification required for bank-provided liquidity

### Building Liquidity for New Projects: A Sequenced Approach

For teams launching new stablecoins, the research suggests a sequenced approach:

**Phase 1: DEX Foundation (Months 1-3)**
- Launch on Curve with minimum $1 million per major trading pair
- Establish governance relationships for gauge voting (Curve incentives)
- Target tight spreads (under 5 basis points) before proceeding
- Build organic trading volume through DeFi integrations
- Estimated capital requirement: $2-5 million

**Phase 2: Market Maker Engagement (Months 3-6)**
- Engage professional market makers (Wintermute, GSR, Kairon Labs)
- Minimum commitment: $1-5 million per trading pair
- Structure token allocations with 12-48 month vesting
- Separate investment contracts from market-making agreements to avoid conflicts
- Establish 24/7 liquidity provision with defined spread targets
- Estimated capital requirement: $5-15 million

**Phase 3: CEX Expansion (Months 6-12)**
- Pursue mid-tier exchange listings once DEX liquidity is established
- Prepare for tier-one exchange due diligence: security audits, reserve attestations, compliance documentation
- Ensure $10-50 million guaranteed depth before approaching Coinbase/Binance
- Budget for listing fees ($50K-$500K for mid-tier; undisclosed for tier-one)
- Estimated capital requirement: $15-50 million

**Phase 4: Multi-Chain Deployment (Ongoing)**
- Prioritize native issuance over bridges where possible
- Launch on chains with organic demand for your use case
- Coordinate liquidity provision across chains to avoid fragmentation
- Consider cross-chain messaging protocols (LayerZero, Axelar) for unified liquidity
- Estimated capital requirement: Additional $5-10 million per major chain

**Total estimated capital for institutional-grade liquidity:** $50-100 million over 18-24 months.

### Key Takeaways

**Minimum viable liquidity has a quantifiable threshold.** Approximately $10-50 million in deployed capital is required for credible CEX listings, with $100 million+ for institutional adoption. Projects without this capital should focus on niche use cases—DeFi-native applications, specific protocol integrations, regional markets—rather than competing for general payment stablecoin status.

**Arbitrage access determines peg stability.** The 87-fold difference between USDT's 6 arbitrageurs and USDC's 521 creates measurable differences in market efficiency. Projects should structure redemption access to enable distributed arbitrage rather than concentrated access—even if this means sacrificing some control and potentially some profitability for market makers.

**Regulatory compliance is now competitive advantage.** The GENIUS Act and MiCA create compliance requirements that double as competitive moats. Early compliance investment—like Circle's MiCA strategy—pays dividends when regulations take effect and non-compliant competitors face delisting. The cost of compliance is high, but the cost of non-compliance is exclusion from regulated markets.

**Multi-chain deployment requires coordination, not just availability.** Simply deploying on multiple chains creates fragmentation that harms all users. Effective multi-chain strategy requires unified liquidity through native issuance protocols (Circle's CCTP), coordinated market maker coverage across chains, and careful attention to where organic demand actually exists.

**Yield-based bootstrapping works but faces sustainability and regulatory questions.** Ethena's USDe demonstrates that high yields can rapidly build market cap—$9.5 billion at peak. But the October 2025 crash shows the risks when yield conditions change, and the GENIUS Act prohibition on yield for payment stablecoins constrains this model's applicability for regulated use cases. Projects using yield incentives should plan explicit transitions to organic demand.

**The cold-start problem is solvable through three paths:**
1. **Institutional-first (USDC model):** Regulatory compliance, exchange partnerships, gradual DeFi integration
2. **Platform leverage (PYUSD model):** Existing user base, commerce integration, limited DeFi presence
3. **Protocol integration (GHO model):** Leverage existing DeFi protocol users, governance incentives, niche positioning

Each path requires different capital structures and timeline expectations. The USDC model takes 5-7 years to achieve dominance; the PYUSD model can achieve meaningful scale in 2-3 years with platform support; the GHO model may never achieve mainstream adoption but can sustain valuable niche positions.

### Looking Forward: The Maturing Infrastructure

The stablecoin liquidity infrastructure that has evolved over the past seven years represents genuine financial innovation—a system capable of processing over $15 trillion in quarterly transactions while maintaining price stability measured in basis points. This infrastructure did not emerge accidentally; it reflects deliberate choices by issuers, exchanges, market makers, and regulators.

The 2025-2026 regulatory cycle marks what industry observers call the end of the "wild west" era. The GENIUS Act and MiCA have erected walls around the U.S. and EU markets that prioritize stability and monetary sovereignty over unrestricted innovation. For exchanges, this means rigorous compliance strategies involving geofencing and selective delisting. For market makers, it means higher capital requirements and a shift toward compliant assets. For users, it means clearer protections but potentially reduced choice.

The most immediate challenge facing stablecoin liquidity infrastructure is maintaining efficiency as volumes continue to scale. Current infrastructure has handled growth from roughly $500 billion in Q1 2025 to over $1 trillion by mid-year, but further multiples would require continued innovation in market-making, DEX design, and cross-chain protocols.

The resolution of regulatory fragmentation will likely reshape market structure further. Nine major European banks formed a consortium in September 2025 to launch a euro-denominated stablecoin, recognizing that regulatory frameworks are creating opportunities for new entrants to challenge U.S. dollar stablecoin dominance. The long-term market structure may include multiple dominant stablecoins pegged to different currencies, each serving regional markets and institutional customer bases.

The fundamental drivers of stablecoin adoption—the need for stable payment instruments, the advantages of 24/7 settlement, and the programmability enabled by blockchain infrastructure—appear structural rather than cyclical. The infrastructure built to provision stablecoin liquidity will likely remain essential infrastructure for global finance for decades to come.

And that 87-fold difference in arbitrage access between USDT and USDC? It turns out to be one of the most consequential design decisions in financial infrastructure—determining not just spreads and efficiency, but the fundamental resilience of the entire system under stress. The lesson is clear: liquidity infrastructure is not a technical afterthought. It is the mechanism through which stablecoins become usable, trustworthy, and ultimately successful.

---

## Sources

### Tier 1: Primary and Authoritative Sources

Federal Reserve FEDS Notes on Primary/Secondary Markets for Stablecoins (2025). Analysis of arbitrage mechanisms and market structure, including data on redemption access concentration.

Federal Reserve. "Banks in the Age of Stablecoins: Some Possible Implications for Deposits, Credit, and Financial Intermediation." December 2025.

U.S. Treasury / GENIUS Act. Guiding and Establishing National Innovation for U.S. Stablecoins Act, enacted July 18, 2025. Implementation deadline: January 18, 2027.

European Securities and Markets Authority (ESMA). Markets in Crypto-Assets Regulation (MiCA), fully effective December 30, 2024.

Bank for International Settlements (BIS). Basel III Crypto Asset Standards, effective January 1, 2025.

### Tier 2: Academic and Industry Analysis

Morgan Stanley Infrastructure Report. "Modernizing Financial Infrastructure Through Stablecoins." September 2025.

McKinsey. "The Stable Door Opens: How Tokenized Cash Enables Next-Gen Payments." July 2025.

TRM Labs. "Global Crypto Policy Review & Outlook 2025-26." December 2025.

Latham & Watkins. GENIUS Act Analysis and Implementation Guide. July 2025.

Arnold Porter. GENIUS Act Compliance Framework. 2025.

KPMG. MiCA Implementation Guide for CASPs. 2024-2025.

Dechert LLP. MiCA Prudential Requirements Analysis. 2025.

Rapyd. "The 2025 Stablecoin Market Leaders Payment Teams Must Know." August 2025.

Chainalysis. "2025 Crypto Regulatory Round-Up." December 2025.

State Street. "The Stablecoin Moment." 2025.

S&P Global. Crypto Asset Liquidity Metrics Analysis. 2025.

### Tier 3: Supporting and Context

Visa Onchain Analytics Dashboard. Stablecoin settlement volume data, 2025.

Circle. USDC partnership announcements, reserve attestations, and CCTP documentation, 2025.

Tether. Q2 2025 Reserve Attestation Report showing $127 billion in Treasury holdings.

Coinbase. Token listing process documentation and supported networks.

OKX. "YU Stablecoin Depeg Exploit Vulnerabilities." November 2025.

Elliptic. "Stablecoin 2025 Risk Assessment Guide." September 2025.

Cointelegraph. "Ethena USDe Market Cap Drops Following October Crash." December 2025.

Wall Street Journal. "Jump Trading Sued for $4 Billion in Connection to Terra Collapse." December 2025.

Wintermute Research via The Block. Crypto liquidity channel analysis. November 2025.

DWF Labs. Falcon Finance announcement and RWA growth report. 2025.

QuickNode. "Stablecoin Adoption 2025." November 2025.

World Economic Forum. "Stablecoins: Cryptocurrency on the Rise in Financial Systems." March 2025.

IMF. "How Stablecoins Can Improve Payments and Global Finance." December 2025.

Axelar Network. "Stablecoin Liquidity Distribution." November 2025.
