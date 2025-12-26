# Claude Research: Stablecoin Series - Ep. 5, Reserve Management & Custody Infrastructure

**Date:** 2025-12-26
**Focus:** Comprehensive Synthesis

---

## Research Output

# Stablecoin reserve management: A comprehensive analysis of custody infrastructure, legal protections, and verification mechanisms

The stablecoin industry has undergone a fundamental transformation in reserve management and custody infrastructure following the 2023 banking crisis and the passage of the GENIUS Act in July 2025. **Bankruptcy-remote trust structures now provide genuine legal protection** for stablecoin holders through estate exclusion and superpriority claims, though these mechanisms remain partially untested in court. The AICPA's 2025 criteria establish standardized attestation requirements, while real-time proof of reserves using zero-knowledge cryptography represents the technical frontier—but fundamental limitations persist in verifying off-chain liabilities and fiat reserves. Circle's SVB crisis exposed concentration risk that has since reshaped industry reserve practices, and the GENIUS Act's interest prohibition has created significant regulatory arbitrage through yield-bearing wrappers that exploit the distinction between issuer payments and third-party arrangements.

## Trust structures create meaningful but imperfect protection for holders

The legal architecture protecting stablecoin holders rests on bankruptcy-remote trust structures that segregate customer reserves from issuer corporate assets. Under established trust law principles confirmed in *Begier v. I.R.S.* (1990) and *In re Howard's Appliance Corp.* (1989), property held in express trust for another person is excluded from a debtor's bankruptcy estate under Section 541(d) of the Bankruptcy Code. Trust company-issued stablecoins—such as those from Paxos (USDP, formerly BUSD) and Gemini (GUSD)—provide holders with direct legal claims to segregated reserves that cannot be accessed by the issuer's general creditors.

The GENIUS Act, signed into law on July 18, 2025, significantly strengthened these protections through three key amendments to bankruptcy law. **Section 11(e) expressly excludes "required payment stablecoin reserves" from a debtor's bankruptcy estate**. Section 11(d) grants stablecoin holders superpriority status over all other claims, including administrative expenses—meaning holders would be paid before bankruptcy attorneys, professional fees, or post-petition vendor invoices. Section 11(a)(2) addresses a critical gap by deeming any person holding a payment stablecoin to hold a claim, even without direct contractual redemption rights with the issuer.

The landmark *In re Celsius Network* decision (January 2023) established that contractual terms of use ultimately determine ownership and whether assets become estate property. Chief Judge Martin Glenn ruled that Celsius's terms "unambiguously transfer title and ownership" because users had "granted Celsius all right and title" to deposited assets. However, the court distinguished Celsius's "Custody Program" accounts—where users retained title—as customer property excluded from the estate. This ruling underscores that **legal structure alone is insufficient without proper contractual documentation**.

### Jurisdictional approaches vary significantly in their protections

New York's Department of Financial Services issued comprehensive stablecoin guidance in June 2022 requiring full backing, asset segregation, reserves held only with FDIC-insured depositories or approved custodians, and monthly CPA attestations. NYDFS-regulated trust companies—including Paxos and Gemini—must hold all customer funds bankruptcy-remote in segregated accounts and process redemptions within two business days at par value.

Wyoming has enacted the most comprehensive state digital asset framework through its Special Purpose Depository Institution (SPDI) charter and 2024 cryptocurrency bankruptcy law. SPDIs must hold unencumbered liquid assets equal to 100% of fiat deposits with no fractional reserve banking permitted. The 2024 law—the first of its kind nationally—provides that "covered accounts" are not deemed assets or liabilities of the financial institution in bankruptcy or receivership, protecting staking arrangements and sub-custody structures.

Delaware Statutory Trusts offer series segregation capabilities where "debts, liabilities, obligations and expenses...shall be enforceable against the assets of such series only, and not against the assets of the statutory trust generally." However, DSTs are more commonly used in real estate syndication than stablecoin reserves.

Federal trust charters from the OCC have emerged as an increasingly attractive option. **Circle received conditional OCC approval to establish First National Digital Currency Bank in late 2024**, while Paxos converted its NYDFS charter to a national trust charter, providing unified 50-state regulation and enhanced institutional credibility.

### Significant legal uncertainties remain untested

Legal commentators have identified several concerning gaps in GENIUS Act implementation. Because reserves sit outside the estate and cannot be used for administrative expenses or debtor-in-possession financing, many issuers may be "administratively insolvent on day one." Georgetown Law professor Adam Levitin has argued the Act is "written in such a way that no trustee in their right mind would sign on to facilitate an insolvent stablecoin issuer's bankruptcy" due to the lack of compensation mechanisms for trustees.

The interaction between the automatic stay (which the GENIUS Act applies to reserves) and estate exclusion (which removes reserves from the estate) creates potential inconsistency that courts have not yet resolved. Cross-border enforcement remains uncertain—bankruptcy remoteness under U.S. law may not be recognized in foreign jurisdictions where stablecoin issuers operate. No published cases have tested whether a stablecoin issuer's reserve trust would survive a substantive consolidation motion.

## Attestations provide snapshots while audits examine the whole picture

The practical difference between reserve attestations and full audits represents a critical but often misunderstood distinction in stablecoin transparency. An attestation is a narrowly-scoped, point-in-time verification where an independent CPA firm confirms that an issuer held specific assets at a precise moment. A full audit involves objective examination and evaluation of complete financial statements, including review of internal controls, verification of data accuracy through independent record examination, assessment of risk management systems, and historical analysis across an entire reporting period.

As one industry analysis notes: "Think of an attestation as a snapshot taken by accountants saying, 'Yes, we've checked, and the money is there right now.'" Even respected accounting firms have limited responsibility in attestations—if they are fed incorrect data, they may never know. The attestor confirms that data provided appears accurate, not that it is complete or unmanipulated.

### The AICPA 2025 criteria establish the first standardized framework

The AICPA released its "2025 Criteria for the Presentation and Disclosure of Redeemable Tokens Outstanding and the Availability of Assets for Redemption: Specific to Asset-Backed Fiat-Pegged Tokens" on March 6, 2025. Developed by the Assurance Services Executive Committee (ASEC), these criteria establish three core requirements.

**Criterion #PF1 (Redeemable Tokens Outstanding)** requires disclosure of total natively minted token quantity, identification of which blockchains and smart contracts are in scope, reconciliation between minted and redeemable tokens, classification of non-redeemable tokens, and disclosure of unresolved events affecting blockchain mechanics or security.

**Redemption Assets Available** requires disclosure of counterparties holding assets and their jurisdictions, identification of related party relationships, detailed breakdown by asset type (cash, Treasury bills, money market funds), geographic location, valuation methods, nature of the issuer's rights to assets, and risk mitigation mechanisms including insurance and segregation.

**Comparison of Redemption Assets to Redeemable Tokens** requires reconciliation including surplus or deficit disclosures, timing differences, temporary differences for access-restricted tokens, material post-measurement date events, and disclosure of legal claims and market disruptions.

In June 2025, the AICPA released an exposure draft for "Proposed Criteria for Controls Supporting Token Operations" covering token generation and management, client onboarding, cryptographic key management, redemption asset management, vendor management, reporting accuracy, and IT general controls. The comment period closed in August 2025.

### Major stablecoins demonstrate vastly different transparency approaches

**Tether (USDT)** with over $145 billion in market cap relies on quarterly attestations by BDO Italia—not a Big Four firm—and publishes daily token circulation data. CEO Paolo Ardoino has acknowledged that Big Four firms "are afraid to work with Tether because they fear it will damage their reputations." Tether has promised a full audit since 2017 but has not delivered. Reserve composition concerns persist, including **$8.83 billion in secured loans and $7.66 billion in Bitcoin** rather than purely cash and Treasury equivalents. S&P assigned Tether its lowest rating, which Tether disputes.

**Circle (USDC)** with approximately $56 billion in market cap provides monthly attestations from Deloitte (Big Four, since fiscal 2022), weekly reserve holdings disclosure, and daily independent third-party reporting via BlackRock. Reserves are held 100% in cash and short-dated U.S. Treasuries through the SEC-registered Circle Reserve Fund (USDXX) managed by BlackRock and custodied at Bank of New York Mellon. Circle files annual audited financial statements with the SEC.

**PayPal USD (PYUSD)** with approximately $1 billion in market cap receives monthly attestations from KPMG (Big Four, since February 2025) and is subject to both NYDFS and OCC regulatory oversight through issuer Paxos Trust.

**DAI (MakerDAO)** operates a fundamentally different model as a decentralized, crypto-collateralized stablecoin. All collateral is visible on the Ethereum blockchain in real-time, governed by MKR token holders through DAO voting. Verification relies on smart contract security audits from Trail of Bits, PeckShield, and Runtime Verification rather than reserve attestations.

### Methodological criticisms highlight structural limitations

Point-in-time attestations face the "window dressing" risk where issuers could theoretically move assets into reserve accounts just before attestation dates. Former SEC official John Reed Stark noted: "Under any circumstance, an attestation report is not the same as an audit report. It is an 'unverified snapshot,' which would never pass any sort of regulatory muster."

**Proof of Reserves does not equal Proof of Liabilities**. Attestations verify that assets exist but may not fully account for off-balance-sheet liabilities, pledged or encumbered assets, related-party transactions, or rehypothecation of reserves. Attestations prepared under AICPA standards are not subject to PCAOB auditing standards or PCAOB inspection.

Continuous auditing solutions have emerged to address snapshot limitations. The Network Firm pioneered real-time attestation reporting with 30-second to daily intervals compliant with AICPA standards. LedgerLens offers automated CPA reports every 30 seconds with circuit breaker functionality for automatic discrepancy detection. Big Four firms have developed blockchain-integrated auditing: PwC reduced audit cycles from 3 months to 6 weeks using blockchain technology with 40% labor cost reduction, while EY deployed zero-knowledge proof technology for privacy-preserving reserve verification.

## Circle's SVB crisis exposed catastrophic concentration risk

The collapse of Silicon Valley Bank on March 10, 2023 triggered the most significant crisis in stablecoin history, exposing critical vulnerabilities in reserve management that have since reshaped industry practices. Circle had approximately **$3.3 billion—roughly 8% of its $40 billion USDC reserves and 34% of its cash reserves**—stuck at SVB when the bank was placed into FDIC receivership at 11:37 AM Eastern on Friday, March 10.

### The operational timeline reveals the speed of contagion

On Thursday, March 9, Circle initiated wire transfers to remove funds from SVB as the bank run accelerated. Over $40 billion in withdrawals that single day left SVB with a negative cash balance of $958 million by close of business—Circle's wires were not processed. By Friday afternoon, USDC had begun drifting below its $1 peg, trading at $0.98-0.99. At approximately 10:00 PM Friday, Circle publicly announced the $3.3 billion exposure, sparking a wave of redemption requests.

By Saturday morning, USDC reached its lowest point of **$0.805-0.87** depending on the exchange—TradingView recorded $0.80526, Bloomberg reported 81.5 cents. Binance suspended USDC-to-BUSD auto-conversion. Coinbase suspended USDC-to-USD conversions because banks were closed for the weekend. Circle issued a statement pledging to "stand behind USDC and cover any shortfall using corporate resources, involving external capital if necessary."

The crisis propagated through DeFi smart contracts with alarming speed. DAI dropped to $0.93 because approximately 40% of its reserves were tied to USDC. USDP fell to roughly $0.91 as over 400 million was withdrawn from MakerDAO's Peg Stability Module—50% of total USDP supply. FRAX dropped to $0.96-0.97. Meanwhile, USDT spiked above $1.06 as traders fled to what they perceived as a safer haven.

The joint announcement by Treasury, Federal Reserve, and FDIC at 6:15 PM on Sunday, March 12 proved decisive—all SVB depositors, both insured and uninsured, would be fully protected. USDC began recovering immediately, returning to approximately $0.99 by evening. Federal Reserve analysis citing Circle's April 2025 SEC S-1 filing revealed that **Circle's total stockholders' equity as of December 31, 2023 was just $0.34 million**—representing barely a tenth of a percent of the $3.3 billion at risk. Without the FDIC backstop, Circle faced potential insolvency.

### Reserve management practices transformed post-crisis

Circle added Cross River Bank as a new banking partner for minting and redemption operations, expanded its relationship with Bank of New York Mellon for reserve custody, and eliminated Silvergate exposure. The structural shift centered on the BlackRock Circle Reserve Fund (USDXX)—an SEC-registered 2a-7 government money market fund launched in November 2022 but significantly expanded post-crisis.

Today, approximately **80% of USDC reserves are held in the Circle Reserve Fund** invested in short-dated U.S. Treasuries and overnight reverse repurchase agreements, with the remaining 20% in cash held primarily at systemically important institutions. Circle emphasizes deposits at "globally or domestically significant financial institutions" with limited funds at transaction banking partners used only for minting and redemption operations.

The Federal Reserve and BIS identified critical lessons. The weekend banking hours mismatch exposed structural differences between traditional finance and 24/7 crypto markets. Circle's invocation of banking hours to suspend weekend convertibility highlighted the need for real-time payment infrastructure like FedNow. DeFi interlinkages through MakerDAO's Peg Stability Modules created automated contagion channels—smart contracts operated autonomously without human intervention while MakerDAO emergency governance changes took 48 hours, far too slow to respond. BIS research demonstrated the disclosure paradox: Circle's transparency about SVB exposure actually triggered the depeg, as "disclosure by the issuer acts as a public signal" that can precipitate runs.

## The GENIUS Act interest prohibition creates a regulatory paradox

Section 4(a)(11) of the GENIUS Act prohibits any permitted payment stablecoin issuer from paying holders "any form of interest or yield (whether in cash, tokens, or other consideration) solely in connection with the holding, use, or retention of such payment stablecoin." According to the Conference of State Bank Supervisors, this prohibition aims to "focus payment stablecoin use on payments and disincentivize the holding of large uninsured stablecoin balances," preventing deposit flight from the banking system and associated financial stability risks.

However, the Act created a significant loophole by focusing exclusively on **issuers** rather than the broader stablecoin ecosystem. It does not explicitly prohibit affiliated exchanges from offering rewards, third-party arrangements structuring yield products, or "wrapper" tokens built on top of non-yield-bearing stablecoins.

### Yield-bearing wrappers exploit the dual-asset architecture

**Savings DAI (sDAI)** represents the clearest example of compliant yield-generation. Users deposit DAI into MakerDAO's Dai Savings Rate module and receive sDAI tokens—an ERC-4626 tokenized vault representation. Yield derives from protocol revenue on stability fees from collateralized loans, currently variable between 5-8% historically with spikes to 15%. sDAI increases in value over time rather than quantity (non-rebasing), can be converted back to DAI plus accrued yield at any time, and exists entirely outside the payment stablecoin definition.

**Ethena's sUSDe** employs a delta-neutral strategy where users deposit stablecoins or ETH as collateral to mint USDe, then stake USDe to receive sUSDe. Yield derives from two sources: staking rewards from liquid staking tokens (3-6% APY) and funding/basis spreads from short perpetual futures positions (historically 5-19% APY). The product averaged approximately 18% APY in 2024 with peaks reaching 29%. This "CeDeFi hybrid" model—on-chain issuance with off-exchange custody and multi-exchange hedging—demonstrates how sophisticated DeFi structures can generate substantial yield while maintaining stablecoin-like properties.

**Ondo Finance's USDY** takes yet another approach through tokenized Treasury exposure, providing 4-5% APY backed by short-term U.S. Treasury yields. Mountain Protocol's USDM operates similarly through Treasury bill backing with a rebasing mechanism. Figure's YLDS is SEC-registered with 3.85% yield from real-world asset backing.

### Exchange rewards programs represent the most direct arbitrage

Coinbase offers up to 4.1% APY (4.5% for Coinbase One subscribers) on USDC holdings despite the GENIUS Act prohibition. CEO Brian Armstrong's legal position: "First, we are not the issuer. And second, we don't pay interest in yield, we pay rewards." SEC filings reveal that **Circle pays 50% of reserve interest to Coinbase**, which Coinbase then distributes as "rewards" rather than "interest."

PayPal offers 3.7% annual returns on PYUSD through PayPal and Venmo. Because PYUSD is issued by Paxos Trust—a third party—rather than PayPal directly, the legal separation enables yield offerings despite the prohibition.

The American Bankers Association and 52 state banking associations warned Congress about this loophole, noting that exchanges are "exploiting a loophole to offer yield-like incentives on stablecoins" that "risks disintermediating core banking activity." Treasury estimates that stablecoins could lead to **$6.6 trillion in deposit outflows** if yield programs continue through affiliates.

### Regulatory resolution remains uncertain

The Treasury Department's Advanced Notice of Proposed Rulemaking specifically sought comment on "whether, and to what extent, any indirect payments are prohibited" under Section 4(a)(11). The comment period closed October 20, 2025.

The Conference of State Bank Supervisors recommended broadly defining "pay," "interest," and "yield" to capture all direct and indirect transfers of value; treating affiliate payments as issuer payments; including disguised "rewards" or "bonuses" as prohibited interest; and prohibiting form arbitrage regardless of whether value is paid in fiat, stablecoins, or other digital assets. They specifically recommended prohibiting revenue sharing arrangements between issuers and affiliates related to fees or reserve interest.

JPMorgan analysts predict that yield-bearing stablecoins could expand from their current 6% share to as much as **50% of the total stablecoin market cap**—a projection that underscores the market demand driving regulatory arbitrage.

## Real-time proof of reserves advances technically but faces fundamental constraints

Proof of Reserves has evolved dramatically from Gregory Maxwell's original 2013 Merkle tree proposal to sophisticated zero-knowledge implementations. The core technical architecture requires two components: proof of assets (demonstrating control of cryptocurrency holdings) and proof of liabilities (demonstrating total customer balances owed). True proof of solvency requires assets greater than or equal to liabilities.

### Cryptographic approaches have matured significantly

**Merkle trees** in the original Maxwell protocol structure each leaf node as a hash of balance, customer ID hash, and nonce. Parent nodes store the hash of the sum plus child hashes and aggregate balance. Users verify inclusion by receiving their nonce plus sibling nodes on the path to the published root, allowing reconstruction and verification without seeing other users' data. Kraken's implementation follows this approach with third-party audit verification from Mazars Group.

**zk-SNARKs** enable privacy-preserving proofs with constant proof size regardless of user count and millisecond verification times. Binance's February 2023 implementation combines zk-SNARKs with Merkle trees to prove that all leaf nodes contribute to total user balance, no user has negative total net balance, and Merkle tree root changes are valid. The source code is published on GitHub.

**zk-STARKs** eliminate the trusted setup requirement of zk-SNARKs while maintaining strong privacy properties. OKX's zk-STARK v2 implementation using the Plonky2 framework achieved 50x faster proof generation than previous versions—3 hours on a single 10-core machine versus 36 hours on nine 64-core machines. GPU acceleration provides an additional 30% reduction.

**Backpack Exchange** has achieved near real-time verification with proofs generated every 10 minutes internally and published daily, using Plonky2 zero-knowledge proofs in partnership with OtterSec. This represents the current frontier of continuous verification.

### Chainlink Proof of Reserve bridges on-chain and off-chain verification

Chainlink PoR operates through the Decentralized Oracle Network where external adapters query off-chain reserve data via APIs, Chainlink nodes aggregate and verify the data, and aggregator contracts publish on-chain data feeds. The system supports two reserve types: off-chain reserves sourced through APIs from third-party auditor attestations or self-reported data, and cross-chain reserves where node operators query source-chain clients directly.

The Secure Mint mechanism provides cryptographic guarantees that minting only occurs when reserves are verified sufficient, preventing infinite mint attacks through circuit breakers that halt minting when reserves fall below thresholds. Current implementations include TrueUSD (TUSD) with continuous third-party attestation and on-chain updates every 24 hours or 5% balance change, PoundToken, Cache Gold for tokenized gold reserves, and Backed Finance for tokenized securities.

### Fundamental limitations constrain all approaches

**Point-in-time snapshots** remain the dominant model despite advances. As Vitalik Buterin noted in his November 2022 analysis: "Ideally, proof of solvency would be done in real time, with a proof that updates after every block." Exchanges could theoretically borrow funds just before audit dates and return them afterward; flash loan exploitation remains technically possible.

**The proof of liabilities problem** represents the most fundamental limitation. On-chain assets are cryptographically verifiable, but off-chain liabilities are not. As Coinbase acknowledged: "None of these approaches can account for off-chain liabilities, such as lending." Hidden loans, creditor obligations, and operational debts are excluded from cryptographic verification.

**Off-chain asset verification** for fiat reserves requires what Vitalik terms "fiat trust models"—bank attestations and auditor reports that inherently require trust. No cryptographic verification of bank account balances is possible. Chainlink documentation explicitly warns that "reserve data reported by an asset issuer's self-reported addresses carries additional risks."

**Collateral dual-use** enables exchanges to pledge the same assets as collateral elsewhere or shuttle collateral between exchanges to pass individual proofs while maintaining collective insolvency. Control does not equal unencumbered ownership. The Provisions protocol addresses this through deterministic "anti-collusion" values requiring synchronized proofs to detect, but implementation remains limited.

PwC Switzerland's critique captures the broader limitation: "The PoR approach limits its scope to compare the clients' assets recorded with information directly from the respective blockchains. This approach ignores the wider picture of the custodian or exchange as a group or organisation and provides no information on the actual liabilities beyond assets held for customers."

## Conclusion: Progress amid persistent structural challenges

Stablecoin reserve management has advanced substantially through the GENIUS Act's bankruptcy protections, AICPA's standardized attestation criteria, sophisticated cryptographic verification mechanisms, and industry practices reformed after the SVB crisis. Trust company structures now provide meaningful holder protections through estate exclusion and superpriority claims, though significant untested areas remain around cross-border enforcement and substantive consolidation risk.

The attestation-versus-audit distinction remains critical—monthly Big Four attestations from Circle represent industry best practice, while Tether's quarterly non-Big Four attestations with unclear reserve composition continue to raise concerns. Real-time proof of reserves using zero-knowledge proofs has reached production scale at major exchanges, yet the fundamental proof of liabilities problem—that off-chain liabilities cannot be cryptographically verified—means that full proof of solvency remains aspirational rather than achievable.

The GENIUS Act's interest prohibition has inadvertently created a two-tier market: compliant payment stablecoins that cannot offer yield, and yield-bearing wrappers and exchange reward programs that exploit the narrow focus on issuers. Treasury rulemaking will determine whether this loophole persists or whether the yield-bearing stablecoin market—projected by JPMorgan to potentially reach 50% of total market cap—faces existential regulatory constraints.

Circle's SVB experience demonstrated that even well-structured reserves face concentration risk when held with non-systemically-important banks, that 24/7 crypto markets create dangerous mismatches with traditional banking hours, and that transparency itself can precipitate runs. The industry's shift toward Treasury-based money market funds, systemically important custodians, and diversified banking relationships represents genuine progress—but the equation of structural protections plus cryptographic verification plus regulatory compliance equals complete safety remains unsolved.

---

## Sources

Here are the primary sources from the research:

**Legal & Regulatory**
- Cadwalader: GENIUS Act Bankruptcy Code Amendments Analysis — https://www.cadwalader.com/resources/clients-friends-memos/making-way-for-stablecoingenius-act-would-amend-bankruptcy-code-to-accommodate-certain-crypto-assets
- Paul Hastings: GENIUS Act Comprehensive Guide — https://www.paulhastings.com/insights/crypto-policy-tracker/the-genius-act-a-comprehensive-guide-to-us-stablecoin-regulation
- Latham & Watkins: GENIUS Act of 2025 Analysis — https://www.lw.com/en/insights/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us
- CSBS: GENIUS Act Implementation Comment Letter — https://www.csbs.org/csbs-genius-act-implementation-comment-letter
- McDermott Will & Emery: Wyoming Cryptocurrency Bankruptcy Law — https://www.mwe.com/media/wyoming-protects-cryptocurrency-and-fiat-customers-with-first-of-its-kind-cryptocurrency-bankruptcy-law/

**Attestation & Audit Standards**
- AICPA: 2025 Stablecoin Reporting Criteria Announcement — https://www.aicpa-cima.com/news/article/aicpa-publishes-comprehensive-criteria-for-reporting-on-stablecoins
- Forvis Mazars: Stablecoin Reserve Attestations Compliance Guide — https://www.forvismazars.us/forsights/2025/11/stablecoin-reserve-attestations-key-considerations-for-compliance
- PwC Switzerland: Proof of Reserves Trust & Transparency Analysis — https://www.pwc.ch/en/insights/digital/does-proof-of-reserves-provide-meaningful-trust-and-transparency.html

**Issuer Primary Sources**
- Circle Transparency Portal — https://www.circle.com/transparency
- Paxos: Bankruptcy Protection Explainer — https://www.paxos.com/blog/how-paxos-protects-customer-assets-from-bankruptcy
- Paxos: Trust Company Safety Analysis — https://www.paxos.com/blog/why-trust-company-issued-stablecoins-are-the-safest-path-for-global-finance
- Coinbase: Proof of Reserves Methodology — https://www.coinbase.com/blog/how-crypto-companies-can-provide-proof-of-reserves
- Coinbase: GENIUS Act USDC Implications — https://www.coinbase.com/blog/the-genius-act-passed-here-is-what-it-means-for-usdc

**Industry Analysis**
- DL News: Tether CEO on Big Four Audit Challenges — https://www.dlnews.com/articles/markets/tether-ceo-just-told-us-why-the-big-4-wont-audit-its-books/
- Fintech Takes: GENIUS Act Bankruptcy Framework Critique — https://fintechtakes.com/articles/2025-06-06/stablecoin-bankruptcy/
- Yahoo Finance: Coinbase/PayPal Yield Workarounds — https://finance.yahoo.com/news/coinbase-paypal-press-forward-stablecoin-211059146.html

**Technical Architecture**
- Rock'n'Block: Ethena USDe Architecture Deep Dive — https://rocknblock.io/blog/stablecoin-architecture-how-ethena-usde-works
