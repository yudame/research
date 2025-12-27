# Claude Research: Stablecoin Series: Ep. 8, Post-Launch Operations

**Date:** 2025-12-26
**Focus:** Comprehensive Synthesis

---

## Research Output

# Stablecoin operations and governance: Crisis performance, power concentration, and systemic vulnerabilities

**Stablecoin governance models face a fundamental trilemma: speed, decentralization, and security appear mutually exclusive during crisis events.** The March 2023 SVB banking crisis provided the first real-world stress test comparing centralized (Circle, Tether) and decentralized (MakerDAO) governance responses—revealing that mandatory security delays in decentralized systems can render emergency governance ineffective, while centralized issuers depend entirely on federal intervention for crisis resolution. This report synthesizes academic research, regulatory filings, on-chain data, and incident postmortems to document operational realities across four critical dimensions: crisis governance performance, power concentration, operational security incidents, and wind-down mechanisms.

---

## The SVB crisis exposed governance model limitations across all three paradigms

The Silicon Valley Bank collapse on March 10, 2023, triggered USDC's depeg to **$0.86** when Circle disclosed **$3.3 billion** (8% of reserves) stranded at the failed bank. This event cascaded immediately to DAI, which fell to $0.88 due to its Peg Stability Module's exposure to USDC, creating an unprecedented natural experiment comparing governance models under stress.

**MakerDAO's decentralized response demonstrated both remarkable speed and structural paralysis.** The Risk Core Unit invoked MIP24 emergency procedures on Saturday morning, March 11, and a governance vote passed within approximately two hours with overwhelming support—88,767 MKR in favor versus just 47 MKR against. The proposal implemented defensive measures including raising the USDC-A PSM inflow fee from 0% to 1%, reducing the daily mint limit from 950M to 250M DAI, and dramatically expanding USDP capacity as an alternative liquidity source. However, MakerDAO's mandatory 48-hour Governance Security Module (GSM) delay meant these changes could not execute until Monday, March 13—after the federal government had already announced its SVB depositor guarantee. As Federal Reserve researchers noted, "By the time these changes were finally executed, most of the market turmoil was already resolved."

The crisis also exposed an architectural vulnerability in MakerDAO's PSM design. During the 48-hour delay, approximately **736 million DAI** was minted through the USDC-PSM as arbitrageurs exploited the depeg, and over **400 million USDP** (half the total supply) was withdrawn from its PSM. The Fed analysis concluded the PSMs "served to weaken Dai's own collateral pool... triggering a significant re-balancing from 'higher-quality' assets such as Ethereum, over-collateralized at 150%, towards distressed USDC, under-collateralized at less than 100%."

**Circle's centralized governance enabled rapid communication but ultimately required federal rescue.** CEO Jeremy Allaire disclosed SVB exposure on Friday evening, committed on Saturday to "stand behind USDC and cover any shortfall using corporate resources, involving external capital if necessary," and announced new banking partnerships by Sunday. This communication speed exceeded MakerDAO's response timeline. However, Circle's S-1 filing reveals total stockholders' equity of only $0.34 million—representing roughly 1/10,000th of the $3.3 billion at risk. Without the federal guarantee of SVB deposits announced Sunday evening, Circle lacked the resources to make USDC holders whole.

**Tether benefited from circumstantial geographic diversification rather than superior crisis management.** CTO Paolo Ardoino's March 10 tweet confirming zero SVB exposure came within hours of the collapse, and USDT traded at a slight premium throughout the crisis as funds fled from USDC. Tether's market cap grew by **$7 billion** over the following two weeks. However, this outcome reflected the absence of U.S. regional bank exposure rather than any active crisis management capability—Tether would face analogous vulnerabilities in a non-U.S. banking crisis affecting its counterparties.

The comparative verdict suggests no governance model proved independently effective. MakerDAO's decentralization enabled rapid community mobilization but security timelocks prevented timely execution. Circle's centralization enabled faster communication but insufficient capital reserves. All three major stablecoins ultimately depended on federal intervention—the joint Treasury, Fed, and FDIC announcement on March 12 resolving SVB depositor concerns was the actual stabilizing event.

---

## Governance participation and power concentration undermine the decentralization thesis

Empirical research reveals stablecoin DAO governance operates with critically low participation rates and extreme voting power concentration—conditions that enable governance attacks while creating "decentralization theater" rather than substantive distributed control.

**Voter turnout across major protocols averages between 6% and 35%**, far below thresholds needed for democratic legitimacy. Academic analysis of 638 MakerDAO governance polls between August 2019 and October 2021 found an average of just **24.59 voters per poll**, with a median of 23 and a maximum of 146. Forum participation has been characterized as "the same 30 persons discussing all the topics." Comparative research across Ethereum DAOs shows Compound at 34% participation, Uniswap at 31.4%, and ENS at 39.2%—with a cross-protocol average of only **6.3%** according to Fudan University researchers. Even Curve's significant governance votes, which determine CRV emission allocations worth hundreds of millions annually, typically see fewer than 1,000 unique voters.

**Voting power concentration rivals or exceeds traditional wealth inequality.** Analysis of MKR token distribution found a mean Gini coefficient of **0.8438** at the poll level, with individual votes reaching as high as 0.9805. The largest single voter averaged **52.66%** of voting power per poll (median 48.35%, maximum 98.51%). Across ERC-20 tokens more broadly, the top 1% of addresses hold an average of **83.2%** of externally-held funds. For Aave, the top three wallets control over 58% of total DAO votes. Research from ETH Zurich and Fudan University confirms the top decile of voters controls approximately **76.2%** of total realized voting power across major DAOs.

These concentration metrics have concrete governance implications. During MakerDAO's contentious Endgame vote, Rune Christensen's delegated voting power represented **74% of turnout influence**—as asset-liability lead Sébastien Derivaux observed, "While 122 persons have voted, only one matters." The LOVE Unit vote in June 2022 saw approximately 294,000 MKR participate (~$300 million worth), nearly one-third of circulating supply, with major VCs (a16z, Paradigm, BlockTower) aligned against Christensen's founding team—demonstrating that even "active" governance remains a contest among a handful of large stakeholders.

**Documented governance attacks demonstrate these vulnerabilities are actively exploited.** The Beanstalk flash loan attack of April 2022 remains the definitive case study: an attacker borrowed over **$1 billion** through Aave, Uniswap, and SushiSwap to acquire enough governance tokens for **79% voting power**, passed a malicious proposal in a single 13-second transaction, and drained **$182 million** in protocol value. The attack exploited Beanstalk's `emergencyCommit` function, which allowed immediate execution of proposals with supermajority support—no delay between voting and execution. Post-attack, Beanstalk removed on-chain governance entirely and replaced it with a community multisig.

The Compound "Golden Boys" attack of July 2024 showed governance manipulation without technical exploits. A group led by whale investor "Humpy" passed Proposal 289 allocating 499,000 COMP (~$24 million, 5% of treasury) to a yield protocol they controlled—passing 682,191 to 633,636 with only **57 total voters**. The proposal was ultimately cancelled through off-chain negotiation rather than on-chain mechanisms, resulting in a "peace treaty" where Compound launched a staking product sharing 30% of market reserves with COMP stakers. As Tally Protocol's CEO observed, "You can't blame people for playing by the rules"—highlighting the governance design problem rather than individual bad actors.

Build Finance DAO's February 2022 hostile takeover demonstrated that governance attacks require no code exploits whatsoever. Attacker "Suho.eth" accumulated governance tokens, disabled Discord proposal notification bots to hide activity, passed proposals granting full control of governance contracts and minting keys, minted 1.1 billion BUILD tokens, drained liquidity pools, and laundered approximately **$470,000** through Tornado Cash. As Build Finance acknowledged: "It is with deep regret that we have to inform the community of this total and irrecoverable loss."

---

## Operational security failures extend far beyond smart contract vulnerabilities

Stablecoin operational incidents encompass custody failures, banking relationship dependencies, oracle manipulation, and regulatory enforcement—each representing attack surfaces independent of code-level security.

**Custody failures have demonstrated catastrophic potential.** Prime Trust's June 2023 collapse revealed the Nevada-regulated custodian had "literally lost the keys to $85 million" in customer cryptocurrency according to court filings. Prime Trust lost access to legacy wallets in December 2021 and subsequently used customer funds to purchase replacement crypto—a textbook case of commingling. When Nevada's Financial Institutions Division issued a cease-and-desist order, TrueUSD (then the fifth-largest stablecoin with $3 billion market cap) faced immediate redemption suspension and depegged to $0.993. The episode demonstrated that fiat-backed stablecoins face custody risk at both the asset level (lost keys) and the institutional level (custodian insolvency).

**Banking concentration creates systemic vulnerabilities.** The March 2023 banking crisis eliminated critical crypto infrastructure within 72 hours. Silvergate's closure ended the Silvergate Exchange Network (SEN), Signature Bank's seizure terminated the Signet payment platform, and SVB's failure stranded Circle's $3.3 billion. These three banks had become essential infrastructure for 24/7 fiat settlement in crypto—their simultaneous failure forced Circle to temporarily limit USDC operations to "business hours" and scramble for replacement banking relationships with Cross River Bank and expanded BNY Mellon arrangements. The event revealed that stablecoin operational resilience depends heavily on banking relationship diversification, which remains limited by crypto-friendly banks' concentration.

**Oracle manipulation attacks have caused tens of millions in damages.** The November 2020 Compound oracle attack exploited Coinbase Pro's role as Compound's primary price source. When DAI spiked to **$1.30** on Coinbase while remaining at ~$1.00 on other exchanges, Compound's Open Price Feed triggered mass liquidations—124 users lost funds, with the largest single liquidation reaching **$46-49 million**. Research determined the manipulation required only approximately **$100,000** to leverage an order book with $300,000 depth, demonstrating extreme asymmetry between attack cost and victim losses. BIS subsequently cited this as one of the largest oracle manipulation instances.

MakerDAO's "Black Thursday" on March 12, 2020, combined oracle failure with network congestion. When ETH collapsed 43% in a single day, gas prices spiked 6x-10x and MakerDAO's Medianizer oracle failed to update prices due to high gas costs. When prices finally updated, 1,461 of 3,994 liquidation auctions (36.6%) were won with **zero bids**—attackers exploited network congestion to prevent legitimate bidders from confirming transactions. Total losses reached **$8.32 million** in collateral liquidated for effectively nothing, leaving 5.67 million DAI uncollateralized and requiring emergency debt auctions.

**Regulatory enforcement has accelerated substantially.** The CFTC's October 2021 settlement with Tether found that USDT was "fully backed only 27.6% of the days" during a 26-month sample period—Tether paid **$41 million** in penalties. The New York Attorney General's February 2021 settlement required **$18.5 million** for hiding losses and misrepresenting dollar backing. NYDFS's 2023 action against Paxos for BUSD led to minting cessation and ultimately a 2025 settlement requiring **$48.5 million** in penalties and compliance investments, citing failure to conduct proper due diligence on Binance. Most significantly, Do Kwon received a **15-year prison sentence** in December 2025 for fraud related to TerraUSD's collapse—the first major criminal conviction for stablecoin failures.

**Transparency gaps persist despite regulatory pressure.** Tether has never completed a full third-party audit despite years of promises—General Counsel Stuart Hoegner's 2022 statement that an audit was "months, not years" away remains unfulfilled. S&P Global downgraded USDT's stability score to "weak" in November 2024, noting Bitcoin now represents 5.6% of circulation versus only 3.9% reserve buffer, and riskier assets (BTC, gold, secured loans, corporate bonds) have climbed to 24% of reserves. Former SEC enforcement chief John Reed Stark characterized Tether as "a Mammoth House of Cards." The difference between disclosed and likely unreported incidents remains significant—no public disclosure requirements exist for thwarted attacks, near-misses, or internal control failures that don't result in regulatory action.

---

## Recovery and wind-down frameworks are developing but remain untested at scale

The GENIUS Act (signed July 18, 2025), EU MiCA (effective June 30, 2024), and emerging UK regulations establish explicit wind-down requirements—but real-world stablecoin failures demonstrate that even fiat-backed issuers can collapse when operational mechanisms fail.

**The GENIUS Act creates the first comprehensive US federal framework for stablecoin wind-down.** The law requires **100% reserve backing** with liquid assets (US dollars, short-term Treasuries, repurchase agreements, government money market funds, central bank reserves), monthly public disclosures, and regular CEO/CFO certifications. Critically, **stablecoin holders have priority over ALL other creditors** in insolvency proceedings—a provision that materially changes the risk profile for holders. Issuers must maintain "tested wind-down playbooks" and hold reserves in segregated, bankruptcy-remote accounts. Banks must issue stablecoins from separate entities insulated from core banking operations. The Act takes effect 18 months after enactment or 120 days after final implementing regulations, whichever comes first.

Major issuers have prepared varying degrees of compliance infrastructure. **Circle** already maintains reserves in a SEC-registered government money market fund managed by BlackRock, with approximately 75% in short-duration Treasuries and 25% in cash at global systemically important banks. Circle's comment letter to Treasury advocated for tested wind-down playbooks, cross-border insolvency coordination, and reciprocity frameworks to avoid flight-to-safety dynamics. **Paxos**, operating under NYDFS trust charter, already maintains 100% backing in cash and cash equivalents only, with reserves held in fully segregated bankruptcy-remote accounts—customers would have priority claims on segregated assets in insolvency. **Tether** has disclosed limited wind-down preparation, announcing headquarters relocation to El Salvador in January 2025 and maintaining that over $120 billion in reserves (primarily Treasury bonds) provides sufficient cushion.

**Existing redemption mechanisms create two-tier access systems.** Circle USDC offers zero-fee 1:1 redemption to 1,819 Circle Mint institutional customers, while retail users must access secondary markets through exchanges. Tether charges a **$150 verification fee**, requires **minimum $100,000 redemptions**, applies a 0.1% redemption fee (maximum $1,000), limits withdrawals to once per week, and restricts US citizen access to Eligible Contract Participants. This effectively creates redemption at $0.999 for large amounts while directing retail to secondary markets. During the SVB crisis, Circle's primary market (institutional) maintained peg functionality while secondary markets (retail) experienced the depeg—demonstrating that crisis behavior differs by access tier.

**Stablecoin failure case studies reveal both design and operational vulnerabilities.** TerraUSD's May 2022 collapse destroyed **$40-60 billion** in value over approximately one week, demonstrating that algorithmic mechanisms without real reserves create death spiral dynamics. When approximately 72% of UST was concentrated in Anchor Protocol earning unsustainable 20% APY, withdrawal pressure triggered Luna hyperinflation (eventually reaching 6+ trillion tokens) as the burn/mint arbitrage mechanism amplified rather than dampened instability. Notably, the Luna Foundation Guard deployed approximately **$750 million** in Bitcoin reserves attempting to defend the peg—suggesting even substantial reserves may prove insufficient without appropriate mechanism design.

HUSD's October 2022 collapse demonstrated that even fiat-backed stablecoins can fail operationally. Initially depegging to $0.82-$0.92 in August due to market maker account closures, HUSD recovered within 24 hours after Huobi intervention. However, when Huobi announced HUSD delisting on October 31, prices crashed from $0.98 to **$0.28**—a 72% loss despite the stablecoin being backed by actual reserves. The failure reflected exchange dependency and liquidity constraints rather than reserve inadequacy.

Iron Finance's June 2021 collapse illustrated oracle-timing vulnerabilities. When large holders began selling TITAN governance tokens, the protocol's 10-minute time-weighted average price oracle lagged real-time prices. Arbitrage became unprofitable when the Effective Collateralization Ratio fell too low, the TITAN minting acceleration created a death spiral, and the smart contract ultimately blocked redemptions when TITAN hit $0. IRON stabilized around $0.70-$0.94, never recovering full peg. Federal Reserve researchers concluded that "design flaws in the no-arbitrage mechanism contributed to the failure."

---

## Regulatory convergence and methodological considerations

Global regulatory frameworks are converging toward common requirements: 100% liquid reserve backing, segregated bankruptcy-remote assets, stablecoin holder priority in insolvency, and explicit wind-down planning. The EU MiCA requires recovery and redemption plans with at least 30% of reserves in separate credit institution accounts. The UK's proposed framework (effective October 2027) mandates 40% held as unremunerated deposits at the Bank of England, validated wind-down plans, and statutory trust protection. Hong Kong's framework (effective August 2025) requires 100% backing plus overcollateralization expectations, with operating without a license carrying up to seven years imprisonment.

**Methodological limitations apply to the research underlying these findings.** Gini coefficient calculations for token distribution often include exchange wallets, potentially inflating concentration metrics. Token distribution does not equal active voting power distribution—many tokens remain dormant or locked in contracts. On-chain data provides transparency but requires interpretation; some researchers exclude smart contract holdings while others include them. Cross-chain tokens exist across multiple chains with different holder bases, complicating analysis. Anonymous wallets mean true concentration may be higher due to single entities controlling multiple addresses.

**Areas of genuine uncertainty remain.** The effectiveness of wind-down provisions under stress has not been tested—no major stablecoin has executed an orderly wind-down following the new regulatory frameworks. Tether's reserves composition and counterparty exposure remain incompletely disclosed despite quarterly attestations. The actual contagion pathways between stablecoins and traditional financial markets remain debated; the Federal Reserve noted that had the SVB run "unfolded differently, the pressure for USDC redemptions might have forced Circle to liquidate backing assets (for example, U.S. Treasury securities), with potential knock-on effects on traditional financial markets." The degree to which governance attacks represent market inefficiency versus rational exploitation of design flaws lacks consensus.

---

## Conclusion: Structural reforms needed across governance, operations, and regulation

The evidence assembled here points toward several actionable conclusions for stablecoin operators, regulators, and market participants.

**Governance security requires fundamental architectural changes.** Flash loan resistance is non-negotiable—any system counting votes in real-time is vulnerable to the Beanstalk attack pattern. Time delays between voting and execution protect against manipulation but create the MakerDAO SVB problem; solutions may require emergency bypass mechanisms with elevated thresholds or off-chain coordination with on-chain verification. Participation rates averaging 6% create attack surfaces that no amount of technical security can address; protocols must either incentivize broader participation or accept that governance remains effectively centralized among large stakeholders.

**Operational security requires banking diversification and custody redundancy.** The SVB crisis demonstrated that even conservative reserve management (Circle's 8% SVB exposure) can create existential threats when banking relationships are concentrated. Issuers should maintain relationships with multiple systemically important banks across jurisdictions, avoid dependency on crypto-specialized banks (which proved fragile), and implement custody across multiple providers with no single point of failure.

**Regulatory frameworks should distinguish algorithmic from asset-backed stablecoins.** The TerraUSD and Iron Finance collapses both involved mechanisms that amplified rather than dampened instability—contrasting sharply with HUSD's failure, which reflected operational/liquidity issues despite adequate backing. MiCA's effective prohibition on algorithmic stablecoins (by requiring explicit reserves) may prove justified, though this forecloses potential innovation in mechanism design.

**Wind-down provisions must be tested before crises occur.** Circle's advocacy for "tested wind-down playbooks" reflects recognition that untested plans fail under stress. Regulators should require simulation exercises analogous to bank stress tests, with public disclosure of results. The GENIUS Act's stablecoin holder priority provision materially improves holder protection, but its interaction with cross-border insolvency regimes remains untested.

The stablecoin ecosystem has evolved from experimental technology to critical financial infrastructure with **$180+ billion** in circulation. The governance, operational, and regulatory challenges documented here are not merely academic—they directly affect the stability of interconnected DeFi protocols, the viability of crypto payment systems, and increasingly, the functioning of traditional financial markets. Addressing these challenges requires sustained attention from issuers, regulators, and researchers alike.

---

## Sources

Here are the primary sources from the research:

**Regulatory & Government Sources**
- Federal Reserve FEDS Notes: "In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins" (December 2024) — https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html
- Congress.gov CRS Report: "Stablecoin Legislation: An Overview of S. 1582, GENIUS Act of 2025" — https://www.congress.gov/crs-product/IN12553
- White House Fact Sheet: "President Donald J. Trump Signs GENIUS Act into Law" — https://www.whitehouse.gov/fact-sheets/2025/07/fact-sheet-president-donald-j-trump-signs-genius-act-into-law/
- Latham & Watkins: "The GENIUS Act of 2025: Stablecoin Legislation Adopted in the US" — https://www.lw.com/en/insights/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us

**Academic Research**
- arXiv: "Democracy for DAOs: An Empirical Study of Decentralized Governance and Dynamics" — https://arxiv.org/pdf/2507.20234
- Fudan University: "Centralized Governance in Decentralized Organizations" (Cong et al.) — https://www.fdsm.fudan.edu.cn/abr2025/ABR_2025_010_full%20paper.pdf
- arXiv: MakerDAO governance analysis paper — https://arxiv.org/pdf/2203.16612

**On-Chain & Industry Sources**
- MakerDAO Governance Portal: Emergency Parameter Changes vote (March 11, 2023) — https://vote.makerdao.com/executive/template-executive-vote-emergency-parameter-changes-march-11-2023
- Chainalysis: "Crypto Market Reaction to Silicon Valley Bank and USDC Depeg" — https://www.chainalysis.com/blog/crypto-market-usdc-silicon-valley-bank/
- Glassnode: "Assessing the Distribution of ERC20 Tokens on the Ethereum Network" — https://insights.glassnode.com/assessing-the-distribution-of-erc20-tokens-on-the-ethereum-network/
- a16z Crypto: "DAO governance attacks, and how to avoid them" — https://a16zcrypto.com/posts/article/dao-governance-attacks-and-how-to-avoid-them/

**Incident Documentation**
- Immunefi: "Hack Analysis: Beanstalk Governance Attack, April 2022" — https://medium.com/immunefi/hack-analysis-beanstalk-governance-attack-april-2022-f42788fc821e
- The Block: "$24 million Compound Finance proposal passed by whale over DAO objections" — https://www.theblock.co/post/307943/24-million-compound-finance-proposal-passed-by-whale-over-dao-objections
- DL News: "How Compound got back $25m after a governance attack" — https://www.dlnews.com/articles/defi/humpy-returns-compound-dao-tokens-in-return-for-fee-sharing/

**Market Analysis**
- CoinDesk: "Tether Stability Made It the Safest Stablecoin Bet Amid U.S. Banking Crisis" — https://www.coindesk.com/markets/2023/03/22/tether-stability-made-it-the-safest-stablecoin-bet-amid-us-banking-crisis-analysts-say
- Sky Forum (MakerDAO): Governance whale concentration discussion — https://forum.sky.money/t/governance-forget-about-whales/4995

The Federal Reserve FEDS Notes paper and the Fudan academic research on DAO governance concentration were particularly valuable for quantitative metrics.
