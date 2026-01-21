# When the Peg Breaks: Inside Stablecoin Operations Under Crisis

On Saturday morning, March 11, 2023, the stablecoin ecosystem experienced its most revealing stress test. Circle had just disclosed that $3.3 billion of USDC reserves—eight percent of total backing—sat frozen in the collapsed Silicon Valley Bank. Within hours, USDC fell to $0.86 on secondary markets. MakerDAO's DAI, which held massive USDC exposure through its Peg Stability Module, dropped to $0.88. An emergency governance vote mobilized 88,767 MKR tokens in favor versus just 47 against—passing in approximately two hours. Yet none of these defensive measures could execute: MakerDAO's mandatory 48-hour security delay meant the protocol's hands were tied until Monday. By then, the crisis had resolved—not through decentralized governance or corporate crisis management, but through a joint announcement from the Treasury, Federal Reserve, and FDIC guaranteeing all SVB depositors.

This single weekend exposed a fundamental truth about stablecoin operations: governance models, reserve structures, and crisis playbooks all ultimately converged on the same dependency—federal intervention. The $180+ billion stablecoin ecosystem, for all its technological sophistication, remains tethered to traditional financial infrastructure in ways that challenge both its promises of decentralization and its claims of operational independence.

This episode examines what happens after a stablecoin launches—the continuous operations, compliance frameworks, governance realities, and crisis responses that determine whether a stablecoin survives or collapses. We will explore the new regulatory frameworks reshaping the industry (the GENIUS Act and MiCA), use the SVB crisis as our central case study for comparing governance models, examine the uncomfortable reality of power concentration in "decentralized" governance, and translate these findings into what operational maturity actually means for issuers, regulators, and users.

---

## Section 1: The Operational Reality of Running Money at Scale

### The Scale of What We Are Discussing

Stablecoins have evolved from niche cryptocurrency trading tools into core financial infrastructure. With over $180 billion in circulation as of late 2025, stablecoins now facilitate daily transaction volumes exceeding those of major card networks (Fireblocks, 2025). Tether's USDT alone maintains approximately $140 billion in circulation, generating billions annually through reserve yield on Treasury holdings. Circle's USDC operates across 28 blockchain networks. PayPal's PYUSD has expanded to Stellar, Arbitrum, and TRON. These are not experimental tokens—they are payment rails processing billions of dollars continuously, operating 24 hours daily without banking hour interruptions.

This scale creates operational complexity that differs fundamentally from traditional payment systems. Unlike Visa or Mastercard, which process transactions through centralized infrastructure, stablecoins operate across fragmented blockchain ecosystems with varying settlement finality rules, transaction throughput, and fee structures. Tether's USDT exists on over 30 different blockchains—a transaction on Tron completes with near-instant finality and costs under one cent, while the identical transaction on Ethereum might cost several dollars and experience minutes of settlement uncertainty. Compliance teams must maintain distinct monitoring configurations for each chain, multiplying the complexity of financial crime detection.

### What Continuous Compliance Actually Requires

The passage of the GENIUS Act on July 18, 2025, and the full implementation of MiCA in the European Union fundamentally transformed stablecoin compliance requirements. These are not incremental regulatory updates—they represent the first comprehensive attempts by major economies to integrate stablecoins into the regulated financial system.

Under the GENIUS Act, which takes effect January 18, 2027, stablecoin issuers must maintain reserves equal to 100% of outstanding tokens, backed exclusively by high-quality liquid assets: U.S. dollars, demand deposits at insured depository institutions, Treasury bills with maturities of 93 days or less, repurchase agreements backed by Treasuries, or central bank reserve deposits (Congress.gov, 2025; Latham & Watkins, 2025). These reserves cannot be pledged, rehypothecated, or reused by the issuer except under very limited circumstances. Monthly public disclosures are required, along with CEO and CFO certifications of reserve adequacy.

Critically, the Act brings stablecoin transactions under Bank Secrecy Act requirements—the same anti-money laundering scrutiny as wire transfers. All issuers must establish AML and sanctions compliance programs with risk assessments, sanctions list verification, and customer identification. Beyond standard BSA requirements, issuers must possess technical capabilities to freeze, seize, or "burn" tokens when legally required (Merkle Science, 2025). This transforms stablecoin systems from passive infrastructure into active compliance enablers, embedding financial crime controls directly into token mechanics.

MiCA implements a substantially different regulatory architecture. Stablecoin issuers must obtain prior authorization from member state national competent authorities. For significant tokens—those exceeding $5 billion in reserves or 10 million users—at least 60% of reserves must be held in commercial bank deposits. Non-significant tokens must hold 30% in bank deposits. Both frameworks prohibit interest payments to token holders, though MiCA applies this prohibition more comprehensively—Coinbase terminated its USDC Rewards program in the EEA in December 2024 to comply.

### The Travel Rule Creates Global Fragmentation

The Financial Action Task Force's Recommendation 16—the "Travel Rule"—requires virtual asset service providers to collect and share originator and beneficiary information for transfers, similar to requirements for wire transfers. However, implementation varies dramatically across jurisdictions, creating compliance complexity for cross-border stablecoin operations.

| Jurisdiction | Threshold | Key Requirements | Effective |
|--------------|-----------|------------------|-----------|
| United States | $3,000 | Full originator/beneficiary data | Existing |
| European Union | 0 Euro | All transactions; verification above 1,000 Euro | December 2024 |
| United Kingdom | 0 GBP | Collection all; verification above 1,000 GBP | September 2023 |
| Singapore | SGD 1,500 | Full value transfer information | January 2020 |
| Japan | ~$3,000 | Name, address, wallet info | June 2023 |
| South Korea | 0 KRW | All transactions | November 2025 |
| Hong Kong | HKD 8,000 | Full info above threshold | June 2023 |

A stablecoin transfer from a U.S. exchange customer to a European recipient might involve the U.S. exchange (subject to FinCEN's $3,000 threshold), a decentralized exchange swap on Ethereum, movement to a European exchange, and final conversion to euros. Each step potentially involves different Travel Rule requirements, necessitating compliance infrastructure that can track the transaction across multiple custody points and regulatory regimes. The European Union's zero-threshold requirement effectively means full identity verification for every single transaction—a fundamentally different compliance burden than the U.S. approach (Gemini, 2025).

### The Transatlantic Divide on Reserve Composition

The philosophy governing stablecoin reserves differs fundamentally between the U.S. and EU approaches, reflecting divergent views on systemic risk and the role of stablecoins in the financial system.

The GENIUS Act prioritizes liquidity and safety by permitting—indeed, encouraging—reserves held in Treasury bills and repos rather than bank deposits. This allows issuers to bypass commercial bank counterparty risk by holding Treasuries directly. If an issuer's banking partner fails, as Silicon Valley Bank did, Treasury holdings remain accessible and liquid. The U.S. framework treats stablecoins as a mechanism for extending dollar dominance globally while insulating issuers from the fragility of the banking system.

MiCA takes the opposite approach, mandating that significant stablecoins hold at least 60% of reserves in commercial bank deposits. This forces a symbiotic relationship between stablecoins and banks—and creates precisely the SVB-type exposure that nearly collapsed USDC. European regulators prioritized protecting the banking sector's deposit base and ensuring stablecoin stability depends on the stability of regulated banks. Critics argue this approach concentrates risk rather than diversifying it: if a major European bank holding stablecoin reserves fails, the contagion to stablecoins becomes immediate and severe.

This regulatory divergence has practical consequences. The EU's approach led to widespread delisting of USDT across European exchanges—Coinbase removed it in December 2024, Kraken followed by March 2025, and Binance restricted it to sell-only mode by March 31, 2025. Tether never obtained an Electronic Money Institution license in an EU member state, making USDT effectively prohibited for trading on MiCA-compliant platforms. Global crypto businesses must now maintain dual liquidity pools: USDC or EURC for Europe, and USDT for Asia and global markets.

The transition from the "Wild West" era of minimal oversight to comprehensive regulatory frameworks represents the most significant operational transformation in stablecoin history. Issuers that once operated with little more than a website and a wallet must now build institutional-grade compliance infrastructure, maintain relationships with multiple regulated banking partners, implement real-time transaction monitoring across dozens of blockchains, and prepare tested wind-down plans for potential failure scenarios.

---

## Section 2: What Crisis Reveals About Governance and Security

### The SVB Weekend: Three Governance Models Tested Simultaneously

The March 2023 Silicon Valley Bank collapse created an unprecedented natural experiment comparing centralized, decentralized, and opaque governance models under identical stress conditions. The timeline reveals both the strengths and limitations of each approach.

Circle, the issuer of USDC, disclosed its $3.3 billion SVB exposure on Friday evening, March 10, 2023. This represented approximately 8% of total USDC reserves—a significant but not catastrophic exposure for a token backed by $41.5 billion at the time. USDC immediately began trading below its $1.00 peg on secondary markets, reaching a low of $0.86 on Saturday, March 11 (Federal Reserve FEDS Notes, December 2024).

Circle CEO Jeremy Allaire's Saturday tweet committed the company to "stand behind USDC and cover any shortfall using corporate resources, involving external capital if necessary." This rapid communication demonstrated a key advantage of centralized governance—decision-making authority and public-facing communication could happen in hours rather than days. However, Circle's S-1 filing reveals that stockholders' equity totaled only approximately $340,000—roughly 1/10,000th of the $3.3 billion at risk. Without federal intervention, Circle lacked the capital to make USDC holders whole.

MakerDAO's response demonstrated both the speed and paralysis of decentralized governance. The Risk Core Unit invoked MIP24 emergency procedures on Saturday morning. A governance vote passed within approximately two hours with overwhelming support—88,767 MKR in favor versus just 47 MKR against. The proposal implemented defensive measures: raising the USDC-A Peg Stability Module inflow fee from 0% to 1%, reducing the daily mint limit from 950 million to 250 million DAI, and dramatically expanding USDP capacity as an alternative liquidity source.

However, MakerDAO's mandatory 48-hour Governance Security Module delay meant these changes could not execute until Monday, March 13. As Federal Reserve researchers later noted, "By the time these changes were finally executed, most of the market turmoil was already resolved" (Federal Reserve FEDS Notes, December 2024). During the 48-hour delay, approximately 736 million DAI was minted through the USDC-PSM as arbitrageurs exploited the depeg. Over 400 million USDP—half the total supply—was withdrawn from its PSM. The Fed analysis concluded that the PSMs "served to weaken Dai's own collateral pool... triggering a significant re-balancing from 'higher-quality' assets such as Ethereum, over-collateralized at 150%, towards distressed USDC, under-collateralized at less than 100%."

Tether's response contrasted sharply with both Circle and MakerDAO. CTO Paolo Ardoino's tweet confirming zero SVB exposure came within hours of the collapse. USDT traded at a slight premium throughout the crisis as funds fled from USDC, and Tether's market cap grew by $7 billion over the following two weeks (CoinDesk, March 2023). This outcome reflected geographic diversification—Tether's banking relationships were concentrated outside the U.S. regional banking system—rather than superior crisis management capabilities.

The comparative verdict is sobering: no governance model proved independently effective. The peg was restored Monday, March 13, not through protocol mechanisms or corporate rescue, but through the joint Treasury, Federal Reserve, and FDIC announcement on Sunday evening guaranteeing all SVB depositors. All three major stablecoins ultimately depended on federal intervention. The decentralization thesis, the centralized crisis response thesis, and the geographic diversification thesis all converged on the same dependency: traditional government backstops.

### The Reality of Decentralized Governance: Participation and Power Concentration

The SVB crisis exposed structural limitations in decentralized governance. But the problems run deeper than crisis response timing. Empirical research reveals that stablecoin DAO governance operates with critically low participation rates and extreme voting power concentration—conditions that undermine claims of distributed control.

Voter turnout across major protocols averages between 6% and 35%, far below thresholds for meaningful democratic legitimacy. Academic analysis of 638 MakerDAO governance polls between August 2019 and October 2021 found an average of just 24.59 voters per poll, with a median of 23 and a maximum of 146 (arXiv, 2022). Forum participation has been characterized by researchers as "the same 30 persons discussing all the topics." Comparative research across Ethereum DAOs shows Compound at 34% participation, Uniswap at 31.4%, and ENS at 39.2%—with a cross-protocol average of only 6.3% according to Fudan University researchers.

Voting power concentration rivals or exceeds traditional wealth inequality. Analysis of MKR token distribution found a mean Gini coefficient of 0.8438 at the poll level, with individual votes reaching as high as 0.9805 (arXiv, 2022). To contextualize that number: a Gini coefficient of 1.0 would mean one person holds all voting power. At 0.84, we are approaching plutocracy dressed as democracy. The largest single voter averaged 52.66% of voting power per poll (median 48.35%, maximum 98.51%). Across ERC-20 tokens more broadly, the top 1% of addresses hold an average of 83.2% of externally-held funds (Glassnode). For Aave, the top three wallets control over 58% of total DAO votes.

These concentration metrics have concrete governance implications. During MakerDAO's contentious Endgame vote, Rune Christensen's delegated voting power represented 74% of turnout influence. As asset-liability lead Sebastien Derivaux observed, "While 122 persons have voted, only one matters."

### Governance Attacks: The Vulnerabilities Are Being Exploited

Low participation and high concentration create attack surfaces that are actively exploited. The Beanstalk flash loan attack of April 2022 remains the definitive case study. An attacker borrowed over $1 billion through Aave, Uniswap, and SushiSwap to acquire enough governance tokens for 79% voting power. They passed a malicious proposal and drained $182 million in protocol value—all in a single 13-second transaction (Immunefi, 2022). The attack exploited Beanstalk's emergencyCommit function, which allowed immediate execution of proposals with supermajority support. Post-attack, Beanstalk removed on-chain governance entirely and replaced it with a community multisig.

The Compound "Golden Boys" attack of July 2024 demonstrated governance manipulation without technical exploits. A group led by whale investor "Humpy" passed Proposal 289, allocating 499,000 COMP (approximately $24 million, 5% of treasury) to a yield protocol they controlled. The proposal passed 682,191 to 633,636—with only 57 total voters (The Block, 2024). The proposal was ultimately cancelled through off-chain negotiation, resulting in a "peace treaty" where Compound launched a staking product sharing 30% of market reserves with COMP stakers. As Tally Protocol's CEO observed, "You can't blame people for playing by the rules"—highlighting that this was a governance design problem rather than individual bad actors.

Build Finance DAO's February 2022 hostile takeover required no code exploits whatsoever. Attacker "Suho.eth" accumulated governance tokens, disabled Discord proposal notification bots to hide activity, passed proposals granting full control of governance contracts and minting keys, minted 1.1 billion BUILD tokens, drained liquidity pools, and laundered approximately $470,000 through Tornado Cash. Build Finance's post-mortem acknowledged: "It is with deep regret that we have to inform the community of this total and irrecoverable loss."

### Operational Security Beyond Smart Contracts

Stablecoin operational incidents extend far beyond code vulnerabilities to encompass custody failures, banking dependencies, oracle manipulation, and regulatory enforcement. Each represents an attack surface independent of smart contract security.

Custody failures have demonstrated catastrophic potential. Prime Trust's June 2023 collapse revealed the Nevada-regulated custodian had "literally lost the keys to $85 million" in customer cryptocurrency, according to court filings. Prime Trust lost access to legacy wallets in December 2021 and subsequently used customer funds to purchase replacement crypto—a textbook case of commingling. When Nevada's Financial Institutions Division issued a cease-and-desist order, TrueUSD faced immediate redemption suspension and depegged to $0.993.

Banking concentration creates systemic vulnerabilities. The March 2023 banking crisis eliminated critical crypto infrastructure within 72 hours: Silvergate's closure ended the Silvergate Exchange Network (SEN), Signature Bank's seizure terminated the Signet payment platform, and SVB's failure stranded Circle's $3.3 billion. These three banks had become essential infrastructure for 24/7 fiat settlement in crypto. Their simultaneous failure forced Circle to temporarily limit USDC operations to "business hours" while scrambling for replacement banking relationships.

Oracle manipulation attacks have caused tens of millions in damages. The November 2020 Compound oracle attack exploited Coinbase Pro's role as Compound's primary price source. When DAI spiked to $1.30 on Coinbase while remaining at approximately $1.00 on other exchanges, Compound's Open Price Feed triggered mass liquidations—124 users lost funds, with the largest single liquidation reaching $46-49 million. Research determined the manipulation required only approximately $100,000 to leverage an order book with $300,000 depth, demonstrating extreme asymmetry between attack cost and victim losses (BIS).

MakerDAO's "Black Thursday" on March 12, 2020, combined oracle failure with network congestion. When ETH collapsed 43% in a single day, gas prices spiked 6-10x and MakerDAO's Medianizer oracle failed to update prices due to high gas costs. When prices finally updated, 1,461 of 3,994 liquidation auctions (36.6%) were won with zero bids—attackers exploited network congestion to prevent legitimate bidders from confirming transactions. Total losses reached $8.32 million in collateral liquidated for effectively nothing.

### De-Pegging Events: What Determines Recovery or Collapse

The 2025 market environment generated multiple de-pegging incidents that illuminate different failure modes and recovery mechanisms.

Ethena's USDe traded as low as $0.65 on Binance in October 2025 following U.S.-China trade tension escalation. USDe uses delta-neutral strategies to maintain stability—backing stablecoins with cryptocurrency collateral while hedging through futures positions. When volatility spiked, capital naturally migrated toward safety, flowing from high-risk synthetic coins like USDe to fiat-backed stalwarts like USDT and USDC. However, USDe recovered to approximately $0.98 within hours. The critical factor: Ethena Labs' third-party reserve attestation confirmed collateralization above 120%, backed by $66 million in excess collateral, and the redemption mechanism remained fully operational throughout.

Compare this to the USDX de-pegging event in late 2025. USDX, a synthetic stablecoin relying on crypto-collateral and off-chain hedging, experienced a massive de-peg reflecting questionable backing and opaque reserve management. On DeFi lending protocols such as Euler, nearly all assets that could be borrowed against USDX were drained while borrowing rates spiked past 800% APY. On-chain addresses linked to Stables Labs founder Flex Yang began aggressively borrowing other stablecoins and transferring them to exchanges—a fire-sale exodus pattern suggesting the true reserve backing of USDX was inadequate. The contrast illustrates a hierarchy of safety: transparency and collateral quality directly determine outcomes during market stress.

Solana-based USX depegged to $0.10 in December 2025 amid liquidity fears. Synthetix's sUSD dropped to $0.66 in April 2025 due to governance and liquidity constraints. These events reinforce the pattern: fiat-backed stablecoins with transparent attestations survive de-peg events through functional redemption mechanisms; synthetic stablecoins with opaque reserves and questionable backing collapse entirely.

| Stablecoin | Date | Low Price | Root Cause | Outcome |
|------------|------|-----------|------------|---------|
| USDC | March 2023 | $0.86 | SVB banking exposure | Recovered (federal guarantee) |
| DAI | March 2023 | $0.88 | USDC PSM exposure | Recovered |
| USDe | October 2025 | $0.65 | Market panic | Recovered (transparent reserves) |
| USX | December 2025 | $0.10 | Liquidity crisis | Uncertain |
| sUSD | April 2025 | $0.66 | Governance issues | Partial recovery |
| USDX | Late 2025 | Severe | Opaque reserves | Collapse |
| Terra/UST | May 2022 | ~$0.00 | Algorithmic failure | Total collapse ($40-60B destroyed) |

---

## Section 3: What Operational Maturity Requires Going Forward

### Wind-Down Requirements: Preparing for Failure Before It Happens

The GENIUS Act creates the first comprehensive U.S. federal framework for stablecoin wind-down. The law requires stablecoin holders to have priority over all other creditors in insolvency proceedings—a provision that materially changes the risk profile for holders (Congress.gov, 2025). Issuers must maintain "tested wind-down playbooks" and hold reserves in segregated, bankruptcy-remote accounts. Banks must issue stablecoins from separate entities insulated from core banking operations.

MiCA requires recovery and redemption plans with at least 30% of reserves in separate credit institution accounts. The UK's proposed framework (effective October 2027) mandates 40% held as unremunerated deposits at the Bank of England, validated wind-down plans, and statutory trust protection. Hong Kong's framework (effective August 2025) requires 100% backing plus overcollateralization expectations, with operating without a license carrying up to seven years imprisonment.

Major issuers have prepared varying degrees of compliance infrastructure:

**Circle** already maintains reserves in an SEC-registered government money market fund managed by BlackRock, with approximately 75% in short-duration Treasuries and 25% in cash at global systemically important banks. Circle's comment letters to Treasury advocated for tested wind-down playbooks, cross-border insolvency coordination, and reciprocity frameworks.

**Paxos**, operating under NYDFS trust charter and now converting to an OCC-regulated national trust (approved December 12, 2025), maintains 100% backing in cash and cash equivalents only, with reserves held in fully segregated bankruptcy-remote accounts.

**Tether** has disclosed limited wind-down preparation. The company relocated headquarters to El Salvador in January 2025 and maintains that over $120 billion in reserves (primarily Treasury bonds) provides sufficient cushion. However, S&P Global downgraded USDT's stability score to "weak" in November 2024, noting that riskier assets (Bitcoin, gold, secured loans, corporate bonds) have climbed to 24% of reserves while the reserve buffer is only 3.9% (S&P Global, 2024).

### Protocol-Level Requirements for Crisis Resilience

Governance security requires fundamental architectural changes. Flash loan resistance is non-negotiable—any system counting votes in real-time is vulnerable to the Beanstalk attack pattern. Time delays between voting and execution protect against manipulation but create the MakerDAO SVB problem. Solutions may require emergency bypass mechanisms with elevated thresholds or off-chain coordination with on-chain verification.

For governance reform:
- Implement minimum voting periods of 48-72 hours regardless of supermajority threshold
- Require token lockup periods (7+ days) before voting power activates to prevent flash loan attacks
- Consider quadratic voting mechanisms that scale voting power less than proportionally with token quantity
- Enable delegation to expert token holders for users who lack time or expertise to vote directly

Participation rates averaging 6% create attack surfaces that no amount of technical security can address. Protocols must either incentivize broader participation through explicit rewards or accept that governance remains effectively centralized among large stakeholders.

Operational security requires banking diversification and custody redundancy. The SVB crisis demonstrated that even conservative reserve management (Circle's 8% SVB exposure) can create existential threats when banking relationships are concentrated. Issuers should:
- Maintain relationships with multiple systemically important banks across jurisdictions
- Avoid dependency on crypto-specialized banks, which proved fragile during the 2023 banking crisis
- Implement custody across multiple providers with no single point of failure
- Establish contingency settlement arrangements for periods when primary banking partners are unavailable

### The Two-Tier Redemption Reality

Current redemption mechanisms create two-tier access systems that behave differently under stress. Circle USDC offers zero-fee 1:1 redemption to 1,819 Circle Mint institutional customers, while retail users must access secondary markets through exchanges. Tether charges a $150 verification fee, requires minimum $100,000 redemptions, applies a 0.1% redemption fee (maximum $1,000), limits withdrawals to once per week, and restricts U.S. citizen access to Eligible Contract Participants.

During the SVB crisis, Circle's primary market (institutional) maintained peg functionality while secondary markets (retail) experienced the depeg. This means that:
- Institutional users with direct redemption access face materially different risk profiles than retail users
- Retail holders effectively bear the price volatility risk during de-peg events
- The "1:1 backing" promise applies differently depending on which tier of access a holder possesses

For users evaluating stablecoin risk:
- Determine whether you have primary market access (direct redemption) or secondary market access (exchange-dependent)
- Understand minimum redemption thresholds and fees
- Consider that de-peg events primarily affect secondary market participants
- Maintain diversification across multiple stablecoins and issuers

### What the Evidence Suggests for Different Stakeholders

**For Stablecoin Issuers:** The GENIUS Act's 18-month implementation window (effective January 2027) requires immediate preparation. Issuers must establish or strengthen relationships with banking partners across multiple jurisdictions, build compliance infrastructure capable of real-time transaction monitoring across all supported blockchains, develop and test wind-down playbooks before they are needed, and ensure reserve composition meets the strict asset requirements (93-day or shorter Treasury bills, repos, cash, demand deposits).

The July 18, 2026 deadline for federal regulators to promulgate final implementing rules provides the timing constraint. Issuers operating at less than $10 billion in circulation may pursue state-level regulation with "substantially similar" standards, though this pathway remains undefined until federal rules are finalized.

**For Regulators:** The Financial Stability Board's October 2025 thematic review found "significant gaps and inconsistencies" in implementing global stablecoin recommendations across jurisdictions (FSB, 2025). Few jurisdictions have finalized regulatory frameworks for global stablecoins, and even where frameworks are finalized, full alignment with FSB recommendations remains limited. Regulatory arbitrage opportunities persist—Tether's relocation to El Salvador exemplifies the pattern.

Cross-border coordination mechanisms remain underdeveloped despite the global nature of stablecoin markets. The GENIUS Act prohibits the offer or sale of payment stablecoins in the U.S. unless the issuer is a "Permitted Payment Stablecoin Issuer," creating barriers for foreign issuers (even MiCA-compliant ones) to access the U.S. market without establishing a U.S. subsidiary.

**For Users and Institutions:** Evaluate stablecoins through the hierarchy demonstrated by 2025 de-peg events:
1. Fiat-backed stablecoins with transparent, frequent attestations and direct redemption access (USDC, Paxos-issued tokens) represent the highest safety tier
2. Fiat-backed stablecoins with less transparent attestations or limited redemption access (USDT) represent intermediate risk
3. Synthetic stablecoins with crypto-collateral and transparent reserve attestations (USDe) occupy a lower tier but can survive de-peg events if redemption mechanisms function
4. Synthetic stablecoins with opaque reserves and off-chain hedging (USDX-type tokens) represent the highest risk tier

For institutional treasury management, maintain diversification across at least two major fiat-backed stablecoins from different issuers, ensure direct redemption access rather than depending on exchange liquidity, and monitor attestation reports (Circle publishes monthly Deloitte attestations; Tether publishes quarterly reports).

### The Unresolved Questions

Several critical uncertainties remain that affect how we should think about stablecoin operational maturity:

**Wind-down effectiveness under stress is untested.** No major stablecoin has executed an orderly wind-down following the new regulatory frameworks. The GENIUS Act's stablecoin holder priority provision represents a significant theoretical improvement, but its interaction with cross-border insolvency regimes remains unknown. Circle's advocacy for "tested wind-down playbooks" reflects recognition that untested plans fail under stress—but regulators have not yet required simulation exercises.

**Tether's full reserves composition and counterparty exposure remain incompletely disclosed** despite quarterly attestations. S&P Global's downgrade cited the growth in riskier assets to 24% of reserves. Former SEC enforcement chief John Reed Stark characterized Tether as "a Mammoth House of Cards." Whether this assessment is accurate or hyperbolic depends on information that remains unavailable to outside analysts.

**The actual contagion pathways between stablecoins and traditional financial markets remain debated.** The Federal Reserve noted that had the SVB run "unfolded differently, the pressure for USDC redemptions might have forced Circle to liquidate backing assets (for example, U.S. Treasury securities), with potential knock-on effects on traditional financial markets" (Federal Reserve FEDS Notes, 2024). At $180+ billion in circulation, stablecoins are large enough that forced selling of Treasury holdings during a crisis could affect Treasury market liquidity.

**The Federal Reserve's position on non-bank stablecoin issuer access to master accounts remains restrictive.** The GENIUS Act explicitly does not grant non-bank issuers direct access to Fed master accounts—they remain reliant on custodial banks to hold cash reserves. This preserves the tiered banking system but also means stablecoin stability depends on commercial banking system stability, as the SVB crisis demonstrated.

### Key Takeaways

**Operational Recommendation 1: Diversify counterparty risk across multiple dimensions.** Do not concentrate reserves in a single banking partner, single blockchain, single custody provider, or single regulatory jurisdiction. The SVB crisis demonstrated that even 8% exposure to a single counterparty can create existential risk.

**Operational Recommendation 2: Prepare for regulatory convergence around the GENIUS Act and MiCA templates.** Hong Kong, Singapore, and the UK are implementing substantially similar frameworks. Issuers building compliance infrastructure should design for the most stringent requirements (100% liquid reserves, real-time transaction monitoring, tested wind-down procedures) rather than minimum viable compliance.

**Operational Recommendation 3: Recognize that governance model choice involves tradeoffs, not solutions.** Centralized governance enables rapid crisis communication but concentrates single points of failure. Decentralized governance distributes control but cannot respond faster than security timelocks permit. No governance model proved independently effective during the SVB crisis—all converged on federal intervention.

**User Recommendation 1: Understand which tier of redemption access you actually have.** Direct institutional access provides materially different protection than secondary market access through exchanges. During de-peg events, the difference between $1.00 direct redemption and $0.86 secondary market pricing represents a 14% loss for holders without primary market access.

**User Recommendation 2: Monitor attestation reports and reserve composition.** Monthly attestations (Circle/Deloitte) provide more actionable transparency than quarterly reports. Reserve composition matters: short-duration Treasuries and repos represent lower risk than commercial paper, secured loans, or cryptocurrency holdings.

The March 2023 weekend when USDC broke its peg revealed something important about the entire stablecoin ecosystem. Despite $180+ billion in circulation, despite sophisticated governance mechanisms, despite years of operational maturity building, the system's stability ultimately depended on a Sunday evening announcement from the Treasury, Federal Reserve, and FDIC. The stablecoins recovered—but they recovered because traditional financial infrastructure intervened, not because their own mechanisms proved sufficient.

What operational maturity means going forward is accepting this reality while building resilience for the scenarios where government backstops may not arrive in time, or may not arrive at all. That means diversified counterparties, tested wind-down procedures, transparent reserves, functional redemption mechanisms, and governance structures that can respond at the speed of crisis. The $180 billion question is whether the industry will build these capabilities before the next stress test, or after.

---

## Sources

### Tier 1: Primary & Authoritative Sources

**Federal Reserve FEDS Notes.** "In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins." December 2024. https://www.federalreserve.gov/econres/notes/feds-notes/

**Congress.gov.** S.1582 - GENIUS Act of 2025. 119th Congress. https://www.congress.gov/bill/119th-congress/senate-bill/1582

**White House.** "Fact Sheet: President Donald J. Trump Signs GENIUS Act into Law." July 18, 2025. https://www.whitehouse.gov/fact-sheets/

**Financial Stability Board.** "FSB Finds Significant Gaps and Inconsistencies in Implementation of Crypto and Stablecoin Recommendations." October 16, 2025. https://www.fsb.org/

**arXiv.** MakerDAO governance analysis (academic research on DAO voting participation and concentration). 2022. https://arxiv.org/pdf/2203.16612

**Fudan University.** "Centralized Governance in Decentralized Organizations." (Power concentration metrics across Ethereum DAOs). https://www.fdsm.fudan.edu.cn/

### Tier 2: Academic & Industry Analysis

**Latham & Watkins.** "The GENIUS Act of 2025: Stablecoin Legislation Adopted in the US." 2025. https://www.lw.com/

**Brookings Institution.** "Stablecoins: Issues for Regulators as They Implement GENIUS Act." October 21, 2025. https://www.brookings.edu/

**McKinsey.** "Stablecoins Payments Infrastructure for Modern Finance." July 21, 2025. https://www.mckinsey.com/

**Fireblocks.** "State of Stablecoins" Report. 2025. https://www.fireblocks.com/report/state-of-stablecoins

**TRM Labs.** "Global Crypto Policy Review Outlook 2025/26." December 3, 2025. https://www.trmlabs.com/

**Glassnode.** "Assessing the Distribution of ERC20 Tokens on the Ethereum Network." https://insights.glassnode.com/

### Tier 3: Incident Documentation & News

**Immunefi.** "Hack Analysis: Beanstalk Governance Attack, April 2022." https://medium.com/immunefi/

**The Block.** "$24 Million Compound Finance Proposal Passed by Whale Over DAO Objections." 2024. https://www.theblock.co/

**CoinDesk.** "Tether Stability Made It the Safest Stablecoin Bet Amid U.S. Banking Crisis." March 2023. https://www.coindesk.com/

**Crypto Briefing.** "Tether to End USDT Support for Omni, Bitcoin Cash SLP, Kusama, EOS, Algorand." July 11, 2025. https://cryptobriefing.com/

**Circle.** "2025 Year in Review." December 2025. https://www.circle.com/

**Paxos.** "OCC Approves Paxos Application to Convert to OCC Trust." December 12, 2025. https://www.paxos.com/

**S&P Global.** USDT Stability Assessment Downgrade. November 2024.

**MakerDAO Governance Portal.** Emergency Parameter Changes Vote. March 11, 2023. https://vote.makerdao.com/
