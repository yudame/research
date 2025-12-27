# Claude Research: Stablecoin Series Ep. 6 - Market Making, Liquidity & Exchange Partnerships

**Date:** 2025-12-26
**Focus:** Comprehensive Synthesis

---

## Research Output

# Stablecoin Liquidity Infrastructure: A Multi-Dimensional Analysis

The stablecoin market's $305 billion infrastructure rests on surprisingly fragile foundations—only **6 arbitrageurs maintain USDT's peg versus 521 for USDC**, liquidity programs suffer **80-91% capital flight** when incentives end, and cross-chain bridges have lost **$3.2 billion** to exploits since 2021. This analysis synthesizes evidence across regulatory frameworks, incentive sustainability, market fragmentation, network entrenchment, and systemic risks to reveal the structural vulnerabilities and competitive dynamics shaping stablecoin markets.

USDT and USDC's combined **86% market share** reflects not merely first-mover advantage but deeply entrenched network effects across exchange pairs, DeFi integrations, and institutional infrastructure. Challengers face **$1B+ capital requirements** and a **3-5 year timeline** to achieve meaningful scale—yet regulatory moats like MiCA compliance are reshaping competitive dynamics, with USDC gaining **400 basis points** of market share in 2025 while USDT faces European delistings.

---

## What separates stablecoin liquidity winners from losers

Technical soundness is necessary but insufficient for stablecoin success. The evidence reveals a clear hierarchy of determinants: regulatory positioning and exchange access dominate, followed by market maker relationships and DeFi integration depth.

**Gemini USD (GUSD) illustrates the failure mode.** Despite receiving S&P Global's strongest asset assessment rating and maintaining monthly audits, GUSD collapsed from a **$564 million peak to $46 million**—a 93% decline—by December 2025. The stablecoin's single-chain Ethereum deployment, limited exchange support after OKX's January 2023 delisting, and MakerDAO's reduction of GUSD holdings from $500M to $110M proved fatal regardless of technical quality.

Contrast this with Circle's USDC trajectory. After the March 2023 SVB crisis temporarily trapped $3.3B of reserves and triggered a depeg to **$0.86**, USDC recovered through strategic regulatory positioning. Circle became the **first MiCA-compliant** major stablecoin issuer in July 2024, enabling exclusive access to the EU's 445 million consumers. The result: **78% year-over-year circulation growth** and market cap recovery from $24.4B to $43.9B.

The regulatory moat effect is now quantifiable. Following MiCA's December 2024 enforcement, Coinbase Europe, Binance, and Crypto.com all announced USDT delistings for EEA users. Per Federal Reserve research, "the quality and liquidity of reserve assets is critical to long-run viability"—but compliance determines whether issuers can access the markets where that viability matters.

**Exchange partnerships function as existential gatekeepers.** First Digital USD (FDUSD) demonstrates the power and peril of exchange dependency. Launching in June 2023 with less than $100M market cap, FDUSD reached $2.61 billion by January 2024—capturing fourth place among stablecoins—entirely through Binance's zero-fee BTC-FDUSD trading pair. Kaiko analysis confirms the vulnerability: "FDUSD's success is heavily reliant on Binance, as it is solely traded on the platform and closely tied to its fee policies." When Binance holds **97.48% of ERC20 FDUSD supply**, exchange policy shifts pose existential risk.

Market maker relationships control liquidity access at the infrastructure level. On Binance alone, **Wintermute claims ~50% of liquidity support** while Jump Crypto provides another 20-30%. These two firms effectively determine which tokens achieve tradeable depth. New entrants face minimum requirements including security audits, $500K-$5M initial liquidity commitments, and active community proof—barriers that favor established issuers with existing relationships.

---

## The mercenary capital problem decimates incentive programs

Liquidity mining revolutionized DeFi—Compound's June 2020 launch triggered TVL growth from $800 million to $10 billion within months—but the sustainability of token rewards remains deeply problematic. Quantified data from 2025 reveals the severity of mercenary capital dynamics.

**Unichain's incentive collapse provides the clearest evidence.** After distributing 3.5 million UNI tokens ($21 million) through a Gauntlet-managed program, the network experienced an **86% TVL collapse** when incentives ended. Tom Wan of Entropy Advisors highlighted this as demonstrating the "systemic vulnerability of incentive-dependent L2s." The pattern repeats across networks: Berachain saw **91% TVL decline** following incentive exhaustion and an exploit, while Linea stabilized at **78.9% below peak** after reward program completion.

The Curve Wars ecosystem illustrates both the sophistication and limitations of tokenomics design. Academic research by Lloyd et al. (2023) analyzing vote-escrowed CRV found **644 million tokens (46%)** locked for an average remaining **181 weeks (3.5 years)**—suggesting the veToken model does create long-term alignment. Yet bribe markets undermine this architecture. Votium has distributed **$248 million** in bribes to direct gauge votes, with a **0.99 correlation coefficient** between bribe percentage and vote allocation in mature phases.

The cost efficiency inversion reveals the model's weakness:

- Direct CRV locking (4-year commitment): **$0.051 per vote**
- Convex via vlCVX (16-week lock): **$0.022 per vote**  
- Votium bribes (no lockup): **$0.015 per vote**

When bribes cost less than commitment, the veToken model's alignment incentives erode. Frax Finance alone contributed **41% of all Votium bribes** ($103.69 million), demonstrating how well-capitalized protocols can effectively purchase governance influence without long-term stake.

**Retention rate evidence suggests 10-20% of liquidity remains** after aggressive incentive programs end—implied by the 80-91% drops observed across networks. Uniswap's weekly active wallet retention of 52% (down from 60% in late 2024) reflects healthier organic usage where fee generation rather than token emissions drives participation.

Successful tapering strategies share common elements: graduated emissions schedules rather than cliff events, multiple lockup mechanism layers creating varied commitment horizons, revenue sharing to long-term stakers, and transition to "real yield" from actual protocol fees. Aave's 2025 model—$537M annualized fees supporting proposed $1M weekly token buybacks—represents the sustainable end-state protocols should target.

---

## Fragmentation costs currently outweigh theoretical benefits

Stablecoin liquidity fragments across 20+ blockchain networks, with distribution concentrated but diversifying. Ethereum holds **~$166B (54%)** of stablecoin supply, Tron **~$78-85B (28%)**, and emerging chains—Solana, BSC, Arbitrum, Base—capture the remainder. The combined Ethereum-Tron dominance declined from 90% to 81-83% during 2024 as Layer 2s and alternative Layer 1s gained traction.

The fragmentation carries measurable costs. Cross-chain bridges have lost **$2.8-3.2 billion** to exploits since 2021, representing approximately **40% of all Web3 hacks**. Major incidents include the Ronin Bridge ($625M, March 2022), BSC Token Hub ($568M, October 2022), Wormhole ($320M, February 2022), and Multichain ($126M+, July 2023). Bridge TVL at risk currently exceeds **$50 billion** locked across protocols.

User experience suffers from fragmentation complexity. During volatility, even liquid stablecoin pairs experience slippage increases exceeding **3 basis points**. Kaiko research documents that "order book depth vanished" during stress events as market makers withdrew—creating price discrepancies between exchanges precisely when users need liquidity most. Less liquid venues showed extreme impacts: KuCoin BTC-EUR exceeded 5% slippage during the August 2024 sell-off.

**Circle's Cross-Chain Transfer Protocol (CCTP)** represents the most promising mitigation. Using burn-and-mint mechanics rather than liquidity pools, CCTP achieves 1:1 capital efficiency with zero bridge fees beyond gas costs. Version 2 improvements reduce transfer times from 13-19 minutes to under 30 seconds across 11+ supported blockchains. This eliminates wrapped token risk—a primary bridge vulnerability vector.

Intent-based protocols are abstracting fragmentation from users. 1inch Fusion+ captured **59.1% of EVM DEX aggregator volume** in Q2 2025, processing $848M daily through Dutch auctions with competing resolvers. CoW Protocol's batch auction system achieves 30% monthly retention with 50-60% returning users while providing MEV resistance. The ERC-7683 standard for cross-chain intents has attracted **73 project adoptions**, with Delphi Digital predicting 60% of interop protocols will consolidate by 2027.

The net assessment: fragmentation's theoretical resilience benefits (no single point of failure, geographic diversity, protocol-specific optimization) are currently outweighed by empirical costs. The $3.2B in bridge losses exceeds quantifiable efficiency gains, concentrated arbitrage undermines cross-chain price stability, and user experience remains prohibitively complex despite improvements.

---

## Network effects create deep structural entrenchment

USDT and USDC's combined 86% market share reflects interlocking network effects that create formidable barriers to competition. The mechanisms span direct effects (more users increase value for each user), indirect effects (exchange and DeFi integrations), and platform lock-in (smart contract dependencies and switching costs).

**Trading pair dominance quantifies the depth of entrenchment.** USDT appears in **66% of all stablecoin-based CEX trades** and controls **82.5% of global stablecoin trading volume**. In perpetual futures—crypto's largest derivatives market—USDT commands **84% of open interest** versus 2.6% for USDC. BTC/USDT alone processes over **$1.6 trillion in 24-hour volume**, making it the most traded pair across all cryptocurrency exchanges.

DeFi integration breadth reinforces this dominance. Aave holds **$14.6B+ TVL** with USDC and USDT as primary lending markets. MEV bot borrowers—the most sophisticated DeFi participants—utilize $3.11B USDC and $2.55B USDT, signaling institutional preference. Tether alone captures approximately **54% of DeFi revenue** while Circle takes ~18%—combined representing roughly **75% of total DeFi revenue generation**.

The two-sided market dynamics make displacement exceptionally difficult. Exchanges gain from listing pairs with high user demand, while users gravitate toward stablecoins with maximum exchange and DeFi acceptance. Once critical mass is achieved, this creates self-reinforcing adoption cycles. Academic research by Rochet and Tirole on platform competition confirms that such markets are "prone to tipping"—where early advantages compound rather than erode.

**Challenger capital requirements are prohibitive.** FDUSD reached $2.4B market cap in approximately one year with Binance's full institutional backing. PYUSD, despite PayPal's 350 million user distribution advantage, achieved less than $1B market cap after two years—with only **~432 daily active users** on-chain. Estimated requirements for meaningful competition: $1B+ capital for liquidity bootstrapping, major exchange partnership (Binance/Coinbase-tier), 3-5 years to reach 5%+ market share, and regulatory compliance across key jurisdictions.

OMFIF analysis provides an important counterpoint: "Network effects in the stablecoin market are likely to be much weaker than most anticipate" because the core product—dollar peg maintenance—is commoditized. Unlike differentiated payment services, stablecoins compete on identical value propositions. This suggests regulatory differentiation (like MiCA compliance) and yield generation may become the new competitive vectors.

---

## Concentrated arbitrage creates deliberate fragility

The finding that only **6 arbitrageurs maintain USDT's peg versus 521 for USDC** originates from rigorous academic research by Yiming Ma (Columbia), Yao Zeng (Wharton), and Anthony Lee Zhang (Chicago Booth), published as NBER Working Paper 33882 in May 2025. Using transaction-level blockchain data across Ethereum, Avalanche, and Tron, the researchers defined arbitrageurs as wallet addresses executing direct mint/burn transactions with issuers in the primary market.

The concentration differential produces measurable price stability impacts:

| Metric | USDT | USDC |
|--------|------|------|
| Active monthly arbitrageurs | 6 | 521 |
| Top arbitrageur market share | 64-66% | 45% |
| Median price discount | 11 basis points | <1 basis point |
| Average price discount | 54 basis points | 1 basis point |

**Critically, this concentration is a deliberate design choice trading price stability for reduced run risk.** The paper's core finding states: "More efficient arbitrage improves stablecoin price stability in secondary markets, but amplifies run risks by reducing investors' price impact from selling stablecoins." With fewer arbitrageurs, secondary market sales depress prices more significantly, which discourages panic selling by increasing its cost. This creates "strategic substitutability" that reduces run incentives.

The March 2023 USDC depeg stress-tested these dynamics. When Circle announced $3.3B trapped at Silicon Valley Bank (representing ~8% of reserves), primary market redemptions peaked before the announcement, then dropped to "minimal levels" over the weekend as Circle suspended processing. USDC traded as low as **$0.86** on secondary markets—a 14% depeg. The Federal Reserve's analysis concludes: "It wasn't until primary markets shut down that USDC hit its low point, and it wasn't until Circle began processing redemptions again that USDC returned to its peg."

**The two-tiered redemption system amplifies systemic vulnerability.** MIT Digital Currency Initiative analysis confirms: "This results in a two-tiered system: institutional clients can redeem directly with stablecoin issuers while other users are left to trust that the peg will hold in public markets." Retail users cannot access primary markets—Tether requires $100,000 minimum redemptions with 0.1% fees (minimum $1,000); Circle restricts direct redemption to "Type A" institutional partners with full KYC and US bank accounts.

Market maker behavior during stress compounds these risks. Kaiko research documents that during volatility events, "there was virtually no liquidity on either side of order books simply because market makers withdrew." Jane Street and Jump Crypto announced reducing crypto exposure following 2023 regulatory enforcement, contributing to a **~50% decline in Bitcoin market depth**. This procyclical withdrawal occurs precisely when stabilizing liquidity is most needed.

Cross-stablecoin dependencies create contagion channels. During the USDC crisis, DAI—a crypto-collateralized stablecoin—depegged via Peg Stability Modules that held USDC as backing. USDP fell to ~91 cents as over 400 million was withdrawn from DAI PSMs (>50% of total supply). These interdependencies mean concentrated failures propagate through the broader ecosystem.

Key single points of failure identified: banking access termination would halt all redemptions; illiquid reserves cannot meet sudden redemption demand; compromised arbitrageurs would undermine peg maintenance; and regulatory action against key market makers could simultaneously disable stabilization mechanisms across multiple stablecoins.

---

## Conclusion

Stablecoin liquidity infrastructure exhibits structural vulnerabilities that require careful monitoring despite the market's apparent stability. The 6-versus-521 arbitrageur concentration represents a deliberate design tradeoff favoring run resistance over price stability—a choice with quantifiable consequences in basis point deviations and recovery speed during stress events.

**Four actionable insights emerge from this analysis:**

First, regulatory compliance has become the primary competitive moat. MiCA's implementation is reshaping European market access, with USDC gaining share while USDT faces delistings. The forthcoming GENIUS Act will similarly restructure US market dynamics. New entrants without clear regulatory positioning face structural disadvantage regardless of technical quality.

Second, liquidity incentive programs require fundamental redesign. The 80-91% capital flight when incentives end demonstrates current models' unsustainability. Protocols should plan for veToken lock-in mechanisms, graduated emission schedules, and transition to fee-based "real yield" from inception rather than treating incentives as permanent growth tools.

Third, multi-chain fragmentation costs currently exceed theoretical benefits. Until intent-based protocols and standards like ERC-7683 mature, the $3.2B in bridge losses, arbitrageur concentration inefficiencies, and user experience complexity impose substantial friction. Strategic chain selection focusing on 3-5 networks with genuine user demand may outperform maximum chain distribution.

Fourth, the network effects entrenching USDT/USDC are real but potentially weaker than in traditional payment networks due to product commoditization. Differentiation through yield generation, regulatory advantage, or embedded distribution (like PayPal's merchant network) represents the viable challenger path—not direct competition on the dollar peg itself.# Stablecoin Liquidity Infrastructure: A Multi-Dimensional Analysis

The stablecoin market's $305 billion infrastructure rests on surprisingly fragile foundations—only **6 arbitrageurs maintain USDT's peg versus 521 for USDC**, liquidity programs suffer **80-91% capital flight** when incentives end, and cross-chain bridges have lost **$3.2 billion** to exploits since 2021. This analysis synthesizes evidence across regulatory frameworks, incentive sustainability, market fragmentation, network entrenchment, and systemic risks to reveal the structural vulnerabilities and competitive dynamics shaping stablecoin markets.

USDT and USDC's combined **86% market share** reflects not merely first-mover advantage but deeply entrenched network effects across exchange pairs, DeFi integrations, and institutional infrastructure. Challengers face **$1B+ capital requirements** and a **3-5 year timeline** to achieve meaningful scale—yet regulatory moats like MiCA compliance are reshaping competitive dynamics, with USDC gaining **400 basis points** of market share in 2025 while USDT faces European delistings.

---

## What separates stablecoin liquidity winners from losers

Technical soundness is necessary but insufficient for stablecoin success. The evidence reveals a clear hierarchy of determinants: regulatory positioning and exchange access dominate, followed by market maker relationships and DeFi integration depth.

**Gemini USD (GUSD) illustrates the failure mode.** Despite receiving S&P Global's strongest asset assessment rating and maintaining monthly audits, GUSD collapsed from a **$564 million peak to $46 million**—a 93% decline—by December 2025. The stablecoin's single-chain Ethereum deployment, limited exchange support after OKX's January 2023 delisting, and MakerDAO's reduction of GUSD holdings from $500M to $110M proved fatal regardless of technical quality.

Contrast this with Circle's USDC trajectory. After the March 2023 SVB crisis temporarily trapped $3.3B of reserves and triggered a depeg to **$0.86**, USDC recovered through strategic regulatory positioning. Circle became the **first MiCA-compliant** major stablecoin issuer in July 2024, enabling exclusive access to the EU's 445 million consumers. The result: **78% year-over-year circulation growth** and market cap recovery from $24.4B to $43.9B.

The regulatory moat effect is now quantifiable. Following MiCA's December 2024 enforcement, Coinbase Europe, Binance, and Crypto.com all announced USDT delistings for EEA users. Per Federal Reserve research, "the quality and liquidity of reserve assets is critical to long-run viability"—but compliance determines whether issuers can access the markets where that viability matters.

**Exchange partnerships function as existential gatekeepers.** First Digital USD (FDUSD) demonstrates the power and peril of exchange dependency. Launching in June 2023 with less than $100M market cap, FDUSD reached $2.61 billion by January 2024—capturing fourth place among stablecoins—entirely through Binance's zero-fee BTC-FDUSD trading pair. Kaiko analysis confirms the vulnerability: "FDUSD's success is heavily reliant on Binance, as it is solely traded on the platform and closely tied to its fee policies." When Binance holds **97.48% of ERC20 FDUSD supply**, exchange policy shifts pose existential risk.

Market maker relationships control liquidity access at the infrastructure level. On Binance alone, **Wintermute claims ~50% of liquidity support** while Jump Crypto provides another 20-30%. These two firms effectively determine which tokens achieve tradeable depth. New entrants face minimum requirements including security audits, $500K-$5M initial liquidity commitments, and active community proof—barriers that favor established issuers with existing relationships.

---

## The mercenary capital problem decimates incentive programs

Liquidity mining revolutionized DeFi—Compound's June 2020 launch triggered TVL growth from $800 million to $10 billion within months—but the sustainability of token rewards remains deeply problematic. Quantified data from 2025 reveals the severity of mercenary capital dynamics.

**Unichain's incentive collapse provides the clearest evidence.** After distributing 3.5 million UNI tokens ($21 million) through a Gauntlet-managed program, the network experienced an **86% TVL collapse** when incentives ended. Tom Wan of Entropy Advisors highlighted this as demonstrating the "systemic vulnerability of incentive-dependent L2s." The pattern repeats across networks: Berachain saw **91% TVL decline** following incentive exhaustion and an exploit, while Linea stabilized at **78.9% below peak** after reward program completion.

The Curve Wars ecosystem illustrates both the sophistication and limitations of tokenomics design. Academic research by Lloyd et al. (2023) analyzing vote-escrowed CRV found **644 million tokens (46%)** locked for an average remaining **181 weeks (3.5 years)**—suggesting the veToken model does create long-term alignment. Yet bribe markets undermine this architecture. Votium has distributed **$248 million** in bribes to direct gauge votes, with a **0.99 correlation coefficient** between bribe percentage and vote allocation in mature phases.

The cost efficiency inversion reveals the model's weakness:

- Direct CRV locking (4-year commitment): **$0.051 per vote**
- Convex via vlCVX (16-week lock): **$0.022 per vote**  
- Votium bribes (no lockup): **$0.015 per vote**

When bribes cost less than commitment, the veToken model's alignment incentives erode. Frax Finance alone contributed **41% of all Votium bribes** ($103.69 million), demonstrating how well-capitalized protocols can effectively purchase governance influence without long-term stake.

**Retention rate evidence suggests 10-20% of liquidity remains** after aggressive incentive programs end—implied by the 80-91% drops observed across networks. Uniswap's weekly active wallet retention of 52% (down from 60% in late 2024) reflects healthier organic usage where fee generation rather than token emissions drives participation.

Successful tapering strategies share common elements: graduated emissions schedules rather than cliff events, multiple lockup mechanism layers creating varied commitment horizons, revenue sharing to long-term stakers, and transition to "real yield" from actual protocol fees. Aave's 2025 model—$537M annualized fees supporting proposed $1M weekly token buybacks—represents the sustainable end-state protocols should target.

---

## Fragmentation costs currently outweigh theoretical benefits

Stablecoin liquidity fragments across 20+ blockchain networks, with distribution concentrated but diversifying. Ethereum holds **~$166B (54%)** of stablecoin supply, Tron **~$78-85B (28%)**, and emerging chains—Solana, BSC, Arbitrum, Base—capture the remainder. The combined Ethereum-Tron dominance declined from 90% to 81-83% during 2024 as Layer 2s and alternative Layer 1s gained traction.

The fragmentation carries measurable costs. Cross-chain bridges have lost **$2.8-3.2 billion** to exploits since 2021, representing approximately **40% of all Web3 hacks**. Major incidents include the Ronin Bridge ($625M, March 2022), BSC Token Hub ($568M, October 2022), Wormhole ($320M, February 2022), and Multichain ($126M+, July 2023). Bridge TVL at risk currently exceeds **$50 billion** locked across protocols.

User experience suffers from fragmentation complexity. During volatility, even liquid stablecoin pairs experience slippage increases exceeding **3 basis points**. Kaiko research documents that "order book depth vanished" during stress events as market makers withdrew—creating price discrepancies between exchanges precisely when users need liquidity most. Less liquid venues showed extreme impacts: KuCoin BTC-EUR exceeded 5% slippage during the August 2024 sell-off.

**Circle's Cross-Chain Transfer Protocol (CCTP)** represents the most promising mitigation. Using burn-and-mint mechanics rather than liquidity pools, CCTP achieves 1:1 capital efficiency with zero bridge fees beyond gas costs. Version 2 improvements reduce transfer times from 13-19 minutes to under 30 seconds across 11+ supported blockchains. This eliminates wrapped token risk—a primary bridge vulnerability vector.

Intent-based protocols are abstracting fragmentation from users. 1inch Fusion+ captured **59.1% of EVM DEX aggregator volume** in Q2 2025, processing $848M daily through Dutch auctions with competing resolvers. CoW Protocol's batch auction system achieves 30% monthly retention with 50-60% returning users while providing MEV resistance. The ERC-7683 standard for cross-chain intents has attracted **73 project adoptions**, with Delphi Digital predicting 60% of interop protocols will consolidate by 2027.

The net assessment: fragmentation's theoretical resilience benefits (no single point of failure, geographic diversity, protocol-specific optimization) are currently outweighed by empirical costs. The $3.2B in bridge losses exceeds quantifiable efficiency gains, concentrated arbitrage undermines cross-chain price stability, and user experience remains prohibitively complex despite improvements.

---

## Network effects create deep structural entrenchment

USDT and USDC's combined 86% market share reflects interlocking network effects that create formidable barriers to competition. The mechanisms span direct effects (more users increase value for each user), indirect effects (exchange and DeFi integrations), and platform lock-in (smart contract dependencies and switching costs).

**Trading pair dominance quantifies the depth of entrenchment.** USDT appears in **66% of all stablecoin-based CEX trades** and controls **82.5% of global stablecoin trading volume**. In perpetual futures—crypto's largest derivatives market—USDT commands **84% of open interest** versus 2.6% for USDC. BTC/USDT alone processes over **$1.6 trillion in 24-hour volume**, making it the most traded pair across all cryptocurrency exchanges.

DeFi integration breadth reinforces this dominance. Aave holds **$14.6B+ TVL** with USDC and USDT as primary lending markets. MEV bot borrowers—the most sophisticated DeFi participants—utilize $3.11B USDC and $2.55B USDT, signaling institutional preference. Tether alone captures approximately **54% of DeFi revenue** while Circle takes ~18%—combined representing roughly **75% of total DeFi revenue generation**.

The two-sided market dynamics make displacement exceptionally difficult. Exchanges gain from listing pairs with high user demand, while users gravitate toward stablecoins with maximum exchange and DeFi acceptance. Once critical mass is achieved, this creates self-reinforcing adoption cycles. Academic research by Rochet and Tirole on platform competition confirms that such markets are "prone to tipping"—where early advantages compound rather than erode.

**Challenger capital requirements are prohibitive.** FDUSD reached $2.4B market cap in approximately one year with Binance's full institutional backing. PYUSD, despite PayPal's 350 million user distribution advantage, achieved less than $1B market cap after two years—with only **~432 daily active users** on-chain. Estimated requirements for meaningful competition: $1B+ capital for liquidity bootstrapping, major exchange partnership (Binance/Coinbase-tier), 3-5 years to reach 5%+ market share, and regulatory compliance across key jurisdictions.

OMFIF analysis provides an important counterpoint: "Network effects in the stablecoin market are likely to be much weaker than most anticipate" because the core product—dollar peg maintenance—is commoditized. Unlike differentiated payment services, stablecoins compete on identical value propositions. This suggests regulatory differentiation (like MiCA compliance) and yield generation may become the new competitive vectors.

---

## Concentrated arbitrage creates deliberate fragility

The finding that only **6 arbitrageurs maintain USDT's peg versus 521 for USDC** originates from rigorous academic research by Yiming Ma (Columbia), Yao Zeng (Wharton), and Anthony Lee Zhang (Chicago Booth), published as NBER Working Paper 33882 in May 2025. Using transaction-level blockchain data across Ethereum, Avalanche, and Tron, the researchers defined arbitrageurs as wallet addresses executing direct mint/burn transactions with issuers in the primary market.

The concentration differential produces measurable price stability impacts:

| Metric | USDT | USDC |
|--------|------|------|
| Active monthly arbitrageurs | 6 | 521 |
| Top arbitrageur market share | 64-66% | 45% |
| Median price discount | 11 basis points | <1 basis point |
| Average price discount | 54 basis points | 1 basis point |

**Critically, this concentration is a deliberate design choice trading price stability for reduced run risk.** The paper's core finding states: "More efficient arbitrage improves stablecoin price stability in secondary markets, but amplifies run risks by reducing investors' price impact from selling stablecoins." With fewer arbitrageurs, secondary market sales depress prices more significantly, which discourages panic selling by increasing its cost. This creates "strategic substitutability" that reduces run incentives.

The March 2023 USDC depeg stress-tested these dynamics. When Circle announced $3.3B trapped at Silicon Valley Bank (representing ~8% of reserves), primary market redemptions peaked before the announcement, then dropped to "minimal levels" over the weekend as Circle suspended processing. USDC traded as low as **$0.86** on secondary markets—a 14% depeg. The Federal Reserve's analysis concludes: "It wasn't until primary markets shut down that USDC hit its low point, and it wasn't until Circle began processing redemptions again that USDC returned to its peg."

**The two-tiered redemption system amplifies systemic vulnerability.** MIT Digital Currency Initiative analysis confirms: "This results in a two-tiered system: institutional clients can redeem directly with stablecoin issuers while other users are left to trust that the peg will hold in public markets." Retail users cannot access primary markets—Tether requires $100,000 minimum redemptions with 0.1% fees (minimum $1,000); Circle restricts direct redemption to "Type A" institutional partners with full KYC and US bank accounts.

Market maker behavior during stress compounds these risks. Kaiko research documents that during volatility events, "there was virtually no liquidity on either side of order books simply because market makers withdrew." Jane Street and Jump Crypto announced reducing crypto exposure following 2023 regulatory enforcement, contributing to a **~50% decline in Bitcoin market depth**. This procyclical withdrawal occurs precisely when stabilizing liquidity is most needed.

Cross-stablecoin dependencies create contagion channels. During the USDC crisis, DAI—a crypto-collateralized stablecoin—depegged via Peg Stability Modules that held USDC as backing. USDP fell to ~91 cents as over 400 million was withdrawn from DAI PSMs (>50% of total supply). These interdependencies mean concentrated failures propagate through the broader ecosystem.

Key single points of failure identified: banking access termination would halt all redemptions; illiquid reserves cannot meet sudden redemption demand; compromised arbitrageurs would undermine peg maintenance; and regulatory action against key market makers could simultaneously disable stabilization mechanisms across multiple stablecoins.

---

## Conclusion

Stablecoin liquidity infrastructure exhibits structural vulnerabilities that require careful monitoring despite the market's apparent stability. The 6-versus-521 arbitrageur concentration represents a deliberate design tradeoff favoring run resistance over price stability—a choice with quantifiable consequences in basis point deviations and recovery speed during stress events.

**Four actionable insights emerge from this analysis:**

First, regulatory compliance has become the primary competitive moat. MiCA's implementation is reshaping European market access, with USDC gaining share while USDT faces delistings. The forthcoming GENIUS Act will similarly restructure US market dynamics. New entrants without clear regulatory positioning face structural disadvantage regardless of technical quality.

Second, liquidity incentive programs require fundamental redesign. The 80-91% capital flight when incentives end demonstrates current models' unsustainability. Protocols should plan for veToken lock-in mechanisms, graduated emission schedules, and transition to fee-based "real yield" from inception rather than treating incentives as permanent growth tools.

Third, multi-chain fragmentation costs currently exceed theoretical benefits. Until intent-based protocols and standards like ERC-7683 mature, the $3.2B in bridge losses, arbitrageur concentration inefficiencies, and user experience complexity impose substantial friction. Strategic chain selection focusing on 3-5 networks with genuine user demand may outperform maximum chain distribution.

Fourth, the network effects entrenching USDT/USDC are real but potentially weaker than in traditional payment networks due to product commoditization. Differentiation through yield generation, regulatory advantage, or embedded distribution (like PayPal's merchant network) represents the viable challenger path—not direct competition on the dollar peg itself.

---

## Sources

**Primary Academic Sources**

1. **Ma, Zeng & Zhang (2025)** - "Stablecoin Runs and the Centralization of Arbitrage" - NBER Working Paper 33882
   - https://www.nber.org/papers/w33882
   - https://bfi.uchicago.edu/wp-content/uploads/2025/06/BFI_WP_2025-76.pdf
   - Source of the 6 vs 521 arbitrageur finding; Columbia/Wharton/Chicago Booth researchers

2. **Federal Reserve FEDS Notes (December 2025)** - "In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html

3. **Federal Reserve FEDS Notes (February 2024)** - "Primary and Secondary Markets for Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/primary-and-secondary-markets-for-stablecoins-20240223.html

4. **Lloyd et al. (2023)** - "Emergent Outcomes of the veToken Model" - arXiv
   - https://arxiv.org/html/2311.17589

**Industry & Market Data**

5. **Kaiko Research** - Liquidity crisis and slippage analysis
   - https://bingx.com/en/news/24796/

6. **CoinDesk / JPMorgan** - USDC market share gains analysis
   - https://www.coindesk.com/markets/2025/09/30/stablecoin-market-surges-on-u-s-regulation-with-circle-s-usdc-gaining-ground-jpmorgan

7. **DL News** - State of DeFi 2025
   - https://www.dlnews.com/research/internal/state-of-defi-2025/

8. **CoinLaw** - Aave Statistics 2025
   - https://coinlaw.io/aave-statistics/

**Technical & Security**

9. **Chainlink** - Cross-Chain Bridge Vulnerabilities
   - https://chain.link/education-hub/cross-chain-bridge-vulnerabilities

10. **Cointelegraph** - Exchange listing requirements
    - https://cointelegraph.com/learn/articles/listed-on-binance-and-coinbase-token-selection-explained

**Case Studies**

11. **BeInCrypto** - FDUSD rise to fourth-largest stablecoin
    - https://beincrypto.com/fdusd-forth-largest-stablecoin/

12. **CryptoSlate** - FDUSD market cap and Binance dependency
    - https://cryptoslate.com/binances-fdusd-market-cap-hits-record-high-dethrones-usdc-in-bitcoin-trading-volume/

The NBER paper and Federal Reserve notes are the highest-authority sources for the systemic risk and arbitrage concentration analysis.**Primary Academic Sources**

1. **Ma, Zeng & Zhang (2025)** - "Stablecoin Runs and the Centralization of Arbitrage" - NBER Working Paper 33882
   - https://www.nber.org/papers/w33882
   - https://bfi.uchicago.edu/wp-content/uploads/2025/06/BFI_WP_2025-76.pdf
   - Source of the 6 vs 521 arbitrageur finding; Columbia/Wharton/Chicago Booth researchers

2. **Federal Reserve FEDS Notes (December 2025)** - "In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html

3. **Federal Reserve FEDS Notes (February 2024)** - "Primary and Secondary Markets for Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/primary-and-secondary-markets-for-stablecoins-20240223.html

4. **Lloyd et al. (2023)** - "Emergent Outcomes of the veToken Model" - arXiv
   - https://arxiv.org/html/2311.17589

**Industry & Market Data**

5. **Kaiko Research** - Liquidity crisis and slippage analysis
   - https://bingx.com/en/news/24796/

6. **CoinDesk / JPMorgan** - USDC market share gains analysis
   - https://www.coindesk.com/markets/2025/09/30/stablecoin-market-surges-on-u-s-regulation-with-circle-s-usdc-gaining-ground-jpmorgan

7. **DL News** - State of DeFi 2025
   - https://www.dlnews.com/research/internal/state-of-defi-2025/

8. **CoinLaw** - Aave Statistics 2025
   - https://coinlaw.io/aave-statistics/

**Technical & Security**

9. **Chainlink** - Cross-Chain Bridge Vulnerabilities
   - https://chain.link/education-hub/cross-chain-bridge-vulnerabilities

10. **Cointelegraph** - Exchange listing requirements
    - https://cointelegraph.com/learn/articles/listed-on-binance-and-coinbase-token-selection-explained

**Case Studies**

11. **BeInCrypto** - FDUSD rise to fourth-largest stablecoin
    - https://beincrypto.com/fdusd-forth-largest-stablecoin/

12. **CryptoSlate** - FDUSD market cap and Binance dependency
    - https://cryptoslate.com/binances-fdusd-market-cap-hits-record-high-dethrones-usdc-in-bitcoin-trading-volume/

The NBER paper and Federal Reserve notes are the highest-authority sources for the systemic risk and arbitrage concentration analysis.**Primary Academic Sources**

1. **Ma, Zeng & Zhang (2025)** - "Stablecoin Runs and the Centralization of Arbitrage" - NBER Working Paper 33882
   - https://www.nber.org/papers/w33882
   - https://bfi.uchicago.edu/wp-content/uploads/2025/06/BFI_WP_2025-76.pdf
   - Source of the 6 vs 521 arbitrageur finding; Columbia/Wharton/Chicago Booth researchers

2. **Federal Reserve FEDS Notes (December 2025)** - "In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html

3. **Federal Reserve FEDS Notes (February 2024)** - "Primary and Secondary Markets for Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/primary-and-secondary-markets-for-stablecoins-20240223.html

4. **Lloyd et al. (2023)** - "Emergent Outcomes of the veToken Model" - arXiv
   - https://arxiv.org/html/2311.17589

**Industry & Market Data**

5. **Kaiko Research** - Liquidity crisis and slippage analysis
   - https://bingx.com/en/news/24796/

6. **CoinDesk / JPMorgan** - USDC market share gains analysis
   - https://www.coindesk.com/markets/2025/09/30/stablecoin-market-surges-on-u-s-regulation-with-circle-s-usdc-gaining-ground-jpmorgan

7. **DL News** - State of DeFi 2025
   - https://www.dlnews.com/research/internal/state-of-defi-2025/

8. **CoinLaw** - Aave Statistics 2025
   - https://coinlaw.io/aave-statistics/

**Technical & Security**

9. **Chainlink** - Cross-Chain Bridge Vulnerabilities
   - https://chain.link/education-hub/cross-chain-bridge-vulnerabilities

10. **Cointelegraph** - Exchange listing requirements
    - https://cointelegraph.com/learn/articles/listed-on-binance-and-coinbase-token-selection-explained

**Case Studies**

11. **BeInCrypto** - FDUSD rise to fourth-largest stablecoin
    - https://beincrypto.com/fdusd-forth-largest-stablecoin/

12. **CryptoSlate** - FDUSD market cap and Binance dependency
    - https://cryptoslate.com/binances-fdusd-market-cap-hits-record-high-dethrones-usdc-in-bitcoin-trading-volume/

The NBER paper and Federal Reserve notes are the highest-authority sources for the systemic risk and arbitrage concentration analysis.**Primary Academic Sources**

1. **Ma, Zeng & Zhang (2025)** - "Stablecoin Runs and the Centralization of Arbitrage" - NBER Working Paper 33882
   - https://www.nber.org/papers/w33882
   - https://bfi.uchicago.edu/wp-content/uploads/2025/06/BFI_WP_2025-76.pdf
   - Source of the 6 vs 521 arbitrageur finding; Columbia/Wharton/Chicago Booth researchers

2. **Federal Reserve FEDS Notes (December 2025)** - "In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html

3. **Federal Reserve FEDS Notes (February 2024)** - "Primary and Secondary Markets for Stablecoins"
   - https://www.federalreserve.gov/econres/notes/feds-notes/primary-and-secondary-markets-for-stablecoins-20240223.html

4. **Lloyd et al. (2023)** - "Emergent Outcomes of the veToken Model" - arXiv
   - https://arxiv.org/html/2311.17589

**Industry & Market Data**

5. **Kaiko Research** - Liquidity crisis and slippage analysis
   - https://bingx.com/en/news/24796/

6. **CoinDesk / JPMorgan** - USDC market share gains analysis
   - https://www.coindesk.com/markets/2025/09/30/stablecoin-market-surges-on-u-s-regulation-with-circle-s-usdc-gaining-ground-jpmorgan

7. **DL News** - State of DeFi 2025
   - https://www.dlnews.com/research/internal/state-of-defi-2025/

8. **CoinLaw** - Aave Statistics 2025
   - https://coinlaw.io/aave-statistics/

**Technical & Security**

9. **Chainlink** - Cross-Chain Bridge Vulnerabilities
   - https://chain.link/education-hub/cross-chain-bridge-vulnerabilities

10. **Cointelegraph** - Exchange listing requirements
    - https://cointelegraph.com/learn/articles/listed-on-binance-and-coinbase-token-selection-explained

**Case Studies**

11. **BeInCrypto** - FDUSD rise to fourth-largest stablecoin
    - https://beincrypto.com/fdusd-forth-largest-stablecoin/

12. **CryptoSlate** - FDUSD market cap and Binance dependency
    - https://cryptoslate.com/binances-fdusd-market-cap-hits-record-high-dethrones-usdc-in-bitcoin-trading-volume/

The NBER paper and Federal Reserve notes are the highest-authority sources for the systemic risk and arbitrage concentration analysis.
