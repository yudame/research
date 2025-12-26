# Stablecoin Reserve Management & Custody Infrastructure Research

**Date:** 2025-12-26

**Research Method:** Web Search Compilation (GPT-Researcher framework encountered API issues; supplemented with comprehensive web search)

**Focus:** Industry analysis, case studies, technical implementation for stablecoin reserve management and custody infrastructure

---

## Executive Summary

The stablecoin industry has undergone significant regulatory and operational transformation in 2024-2025, culminating in the passage of the GENIUS Act in July 2025 - the first comprehensive U.S. federal framework for payment stablecoins. This research covers custody cost structures, multi-custodian arrangements, Circle's GENIUS Act compliance, Ripple's RLUSD transparency reporting, trust company bankruptcy-remote structures, the SVB crisis response, proof of reserves technology, SOC 2 Type II requirements, and multi-signature custody implementations.

---

## Part 1: Industry Analysis

### Custody Costs at Scale

Qualified custodian relationships involve multiple cost categories:

**Fee Structures:**
- **Coinbase Custody**: $10,000 setup fee + 0.50% annual fee on AUC (Assets Under Custody), minimum $1M balance
- **Cactus Custody**: 0.5% annually (cold storage), 0.8% annually (hot storage)
- **Bitcoin Suisse**: 0.3%-0.6% per annum, calculated daily
- **Typical Range**: 0.04% to 0.50% annualized, with volume-based discounts

**Fee Breakdown (Institutional):**
- 10 bps (0.10%) on $10M AUM = $10,000/year
- 50 bps (0.50%) on $10M AUM = $50,000/year
- Larger AUM typically receives lower basis point rates
- Most custodians require $500K-$1M minimum balance

**Insurance Coverage:**
- Gemini maintains $75 million in cold storage insurance coverage
- Insurance costs are typically embedded in custody fees or charged separately
- Coverage types include theft, loss, and misuse protection

**Operational Overhead:**
- SOC 1/SOC 2 Type II audit compliance
- Segregated account maintenance
- 24/7 monitoring and incident response
- Multi-signature or MPC key management infrastructure

Sources:
- [MooLoo Crypto Custody Comparison](https://mooloo.net/crypto-custody-providers-comparison/)
- [YellowCard Top Crypto Custodians 2025](https://yellowcard.io/blog/top-crypto-custodians-2025-market-leaders-comparison/)

---

### Multi-Custodian Arrangements for Concentration Risk Reduction

**Circle's Multi-Custodian Strategy:**

Circle's approach demonstrates industry best practices for diversification:

| Function | Partner |
|----------|---------|
| Cash Reserves Custody | BNY Mellon (primary) |
| Treasury Management | BlackRock (Circle Reserve Fund - $66B) |
| Minting/Redemption | Cross River Bank (added post-SVB) |
| Additional Cash | Multiple large U.S. banks |

**BNY Mellon's Central Role:**
- Primary banking partner for Circle and Ripple
- Custodian for USDC, RLUSD, and Societe Generale's USDCV
- November 2025: Launched BNY Dreyfus Stablecoin Reserves Fund (BSRXX) specifically for GENIUS Act compliance

**Key Principles:**
- Spread cash reserves across multiple custodians
- Separate asset management (BlackRock) from custody (BNY Mellon)
- Maintain redundant banking relationships for minting/redemption
- Use qualified custodians with SOC 2 Type II certification

Sources:
- [BNY Stablecoin Reserves Fund Launch](https://www.bny.com/corporate/global/en/about-us/newsroom/press-release/bny-launches-stablecoin-reserves-fund-expanding-bnys-leadership-digital-assets-130451.html)
- [CCN: BNY Mellon Stablecoin Reserves](https://www.ccn.com/news/business/bny-mellon-stablecoin-reserves-circle-ripple/)
- [TreasuryUp: Stablecoins for Banks 2025](https://treasurup.com/stablecoins-for-banks-strategic-playbook-2025/)

---

### Business Models for Smaller Stablecoin Issuers

**Compliance Cost Challenges:**

Under the GENIUS Act, stablecoin issuers face substantial compliance requirements:
- Monthly reserve attestations by registered public accounting firms
- Annual independent audits (size-dependent)
- SOC 2 Type II controls implementation
- Qualified custodian relationships
- AML/KYC infrastructure

**Viable Business Models:**

1. **White-Label Infrastructure Partnerships:**
   - Partner with Paxos or similar regulated infrastructure providers
   - Paxos offers stablecoin-as-a-service under their NYDFS trust charter
   - Reduces compliance burden to the infrastructure provider

2. **Regional/Niche Focus:**
   - Target specific geographic markets (emerging economies)
   - Focus on particular use cases (remittances, B2B payments)
   - Lower volumes but potentially higher margins

3. **Bank Subsidiary Model:**
   - FDIC-supervised institutions can issue stablecoins through subsidiaries
   - December 2025: FDIC proposed application procedures for IDI subsidiaries
   - Leverages existing banking compliance infrastructure

4. **Revenue Sources:**
   - Interest income on reserve assets (primary)
   - Transaction/redemption fees
   - Enterprise API licensing
   - Float on pending redemptions

Sources:
- [Whiteford Law: GENIUS Act Compliance Roadmap](https://www.whitefordlaw.com/news-events/client-alert-the-genius-act-a-compliance-roadmap-for-stablecoin-issuers-in-2025)
- [Mayer Brown: FDIC Stablecoin Application Process](https://www.mayerbrown.com/en/insights/publications/2025/12/fdic-proposes-genius-act-application-process-for-idi-subsidiary-stablecoin-issuers)
- [ShamlaTech: Stablecoin Business Models](https://shamlatech.com/how-stablecoin-issuers-make-money-usdt-usdc-industry/)

---

## Part 2: Case Studies & Implementation

### Circle: GENIUS Act Compliance and AICPA 2025 Criteria

**Compliance Positioning:**

Circle claims USDC is "fully compliant, transparent, and ready" for the GENIUS Act era.

**Reserve Management Structure:**
- Portfolio: Short-dated U.S. Treasuries, overnight Treasury repos, and cash
- Custody: The Bank of New York Mellon
- Asset Management: BlackRock (Circle Reserve Fund)

**Attestation Practices:**
- Monthly attestation reports (previously, continues under GENIUS Act)
- Independent examination by Deloitte
- February 2025 attestation confirmed reserves >= USDC in circulation

**GENIUS Act Requirements Met:**
| Requirement | Circle Implementation |
|-------------|----------------------|
| 1:1 Reserve Backing | 100% USD/Treasury backing |
| Monthly Examinations | Deloitte attestations |
| Qualified Custodian | BNY Mellon (NYDFS regulated) |
| No Rehypothecation | Reserves cannot be pledged |
| Eligible Assets | U.S. currency, short-term Treasuries |

**AICPA 2025 Criteria Integration:**

The AICPA's 2025 Criteria for Stablecoin Reporting provides standardized framework for:
1. **Redeemable tokens outstanding** - Count and valuation
2. **Availability and composition of redemption assets** - Reserve breakdown
3. **Comparison between the two** - Sufficiency verification

Circle's existing practices align with this framework. The upcoming Proposed Criteria for Controls Supporting Token Operations will add controls attestation requirements.

Sources:
- [Circle GENIUS Act Page](https://www.circle.com/genius-act)
- [AICPA: GENIUS Act Creates Oversight](https://www.aicpa-cima.com/professional-insights/article/genius-act-creates-oversight-and-opportunity-for-stablecoins)
- [Forvis Mazars: Stablecoin Reserve Attestations](https://www.forvismazars.us/forsights/2025/11/stablecoin-reserve-attestations-key-considerations-for-compliance)
- [Grant Thornton: GENIUS Act for Banks](https://www.grantthornton.com/insights/articles/banking/2025/genius-act-means-for-banks)

---

### Ripple RLUSD Transparency Reporting

**Overview:**
- Launched: December 2024
- Issuer: Standard Custody & Trust Company (SCTC), Ripple subsidiary
- Charter: New York State trust charter
- Market Cap: $1.26 billion (as of late 2025), third-largest U.S.-regulated stablecoin

**Reserve Composition:**
- 1:1 backing by U.S. dollar deposits, U.S. Treasuries, and cash equivalents
- Reserves held in segregated, bankruptcy-remote accounts
- Market value determined at trade-date, fair value at report date

**Attestation Framework:**
- Monthly attestation reports by independent CPA (Deloitte & Touche LLP)
- Adheres to AICPA attestation standards
- Follows NYDFS Guidance (June 8, 2022) on USD-backed stablecoins

**Transparency Dashboard:**

Ripple publishes monthly reserve reports including:
- Circulating supply verification
- Reserve asset composition breakdown
- CPA attestation letter

**Note on CUSIP-Level Detail:**

While Ripple commits to "full transparency," publicly available reports do not disclose CUSIP-level identifiers for individual Treasury securities. The attestation confirms aggregate compliance rather than security-by-security holdings. Real-time dashboards show overall metrics but not granular asset details.

**December 2025 Development:**
Ripple secured federal approval to establish a National Trust Bank, positioning for enhanced regulatory status under GENIUS Act.

Sources:
- [Ripple USD Transparency Page](https://ripple.com/solutions/stablecoin/transparency/)
- [U.Today: Deloitte RLUSD Attestation](https://u.today/first-deloitte-backed-ripple-usd-rlusd-attestation-goes-live)
- [Yahoo Finance: RLUSD Hits $1.26B](https://finance.yahoo.com/news/ripple-rlusd-hits-1-26b-182210135.html)
- [Standard Custody April 2025 Reserve Report (PDF)](https://assets.ctfassets.net/st43jm402pmo/2YWLcImkdiTnUe8JdZlgPJ/0e0d3d8c9da9d823de79b61f8f2d1f26/Standard_Custody_and_Trust_LLC_April_2025_RLUSD_Reserve_Report.pdf)

---

### Trust Company Issuers: Bankruptcy-Remote Reserves (Paxos, GUSD)

**Regulatory Framework:**

Trust companies regulated by NYDFS (Paxos, Gemini) and OCC operate under bankruptcy-remote structures:

**Key Safeguards:**
| Protection | Implementation |
|------------|----------------|
| Bankruptcy Remoteness | Reserves held in trust, segregated from issuer balance sheet |
| Direct Legal Claim | Stablecoin holders have direct claim to reserves |
| Insolvency Protection | Par value recovery guaranteed in bankruptcy |
| Asset Segregation | Corporate assets legally separated from client funds |

**Reserve Requirements (NYDFS):**
- 100% backing verified at end of every business day
- Approved reserve assets only:
  - U.S. Treasury Bills
  - Repo agreements fully collateralized by Treasury securities
  - Government money market funds
  - FDIC-insured cash deposits
- Short-term maturity requirements (typically <13 weeks)

**Paxos 2024-2025 Developments:**

1. **SEC Investigation Closed (July 2024):** No enforcement action for BUSD
2. **NYDFS Settlement (August 2025):** $48.5M settlement for historical Binance-related compliance issues ($26.5M penalty + $22M compliance investment)
3. **National Trust Charter Application (August 2025):** Converting from NYDFS to OCC supervision

**Contrast with Non-Trust Issuers:**
- USDC and Tether reserves are not comprehensively regulated
- Not held bankruptcy-remote under applicable law
- SVB crisis demonstrated vulnerability: USDC fell to $0.87 when $3.3B was trapped at failed bank

Sources:
- [Paxos: Trust Company-Issued Stablecoins](https://www.paxos.com/blog/why-trust-company-issued-stablecoins-are-the-safest-path-for-global-finance)
- [CryptoSlate: NY Stablecoin Guidelines](https://cryptoslate.com/ny-stablecoin-issuers-gemini-paxos-have-to-ensure-100-reserves-daily-under-new-guidelines/)
- [Paxos: National Trust Charter Announcement](https://www.paxos.com/newsroom/paxos-to-pursue-national-trust-charter-with-the-office-of-the-comptroller-of-the-currency)

---

### Circle and the SVB Crisis: Operational Response

**Background:**
Silicon Valley Bank collapsed on March 10, 2023, with Circle holding approximately $3.3 billion of USDC reserves at the failed institution.

**Timeline:**

| Date | Event |
|------|-------|
| **March 10, 2023 (Friday)** | SVB shut down by regulators; Circle discloses $3.3B exposure |
| **March 10-11** | USDC depegs, falling to $0.87-$0.88 on exchanges |
| **March 11-12 (Weekend)** | Panic selling; Circle reassures users of backup plan |
| **March 12 (Sunday evening)** | Treasury, Fed, FDIC announce all SVB depositors made whole |
| **March 13 (Monday)** | USDC recovers peg; Circle confirms SVB fund access |

**Decision-Making and Recovery:**

1. **Immediate Response:** Circle publicly disclosed SVB exposure within hours of bank closure
2. **Contingency Planning:** Circle indicated willingness to cover any shortfall if necessary
3. **Resolution:** Full recovery of $3.3B once government guaranteed all deposits
4. **Lessons Applied:**
   - Expanded relationship with BNY Mellon as primary custodian
   - Added Cross River Bank for redundant minting/redemption
   - Diversified cash holdings across multiple banks

**Industry Impact:**
- Highlighted concentration risk in single banking relationships
- Demonstrated importance of multi-custodian arrangements
- Led to increased focus on bankruptcy-remote trust structures
- Accelerated regulatory discussions culminating in GENIUS Act

---

## Part 3: Technical Implementation

### Real-Time Proof of Reserves Systems

**Current State (2025):**
- 60-75% of leading stablecoins publish real-time or near real-time proof-of-reserves dashboards
- Some protocols (e.g., Ethena) offer on-chain proof showing all collateral positions and hedge ratios

**Technical Architecture:**

**Data Sources and Reporting Intervals:**
| Data Source | Typical Interval |
|-------------|------------------|
| API/automated extraction | 30 seconds |
| Hourly data feeds | 1 hour |
| Daily reconciliation | 24 hours |
| Traditional attestation | 30 days |

**Implementation Components:**

1. **Data Aggregation Layer:**
   - Bank API integrations for cash balances
   - Custody platform APIs for asset holdings
   - Blockchain queries for token supply

2. **Verification Layer:**
   - Cryptographic proofs (Merkle trees for user balances)
   - Oracle networks (e.g., Chainlink) for on-chain publication
   - Third-party auditor feeds

3. **Reporting Layer:**
   - Public dashboards (real-time metrics)
   - Monthly attestation reports (CPA-verified)
   - On-chain data for DeFi integration

**GENIUS Act Requirements:**
- Monthly reserve composition reports
- Third-party accountant examination
- Publication of reserve holdings by asset class

**Chainlink Proof of Reserves:**
- Oracles aggregate data from custodians, banks, and auditors
- Data published on-chain for smart contract verification
- Notable implementations: TrueUSD (TUSD), Paxos Gold (PAXG)

Sources:
- [The Network Firm: Real-Time Reserves](https://www.thenetworkfirm.com/real-time-reserves-for-crypto-blockchain-auditing-the-network-firm)
- [Hacken: Proof of Reserves Explained](https://hacken.io/discover/proof-of-reserves-explained-from-key-mechanics-to-verification/)
- [The Accountant Quits: PoR for Stablecoins](https://www.theaccountantquits.com/articles/proof-of-reserves-for-stablecoin-issuers)
- [PWC: Stablecoin Reporting Turning Point](https://www.pwc.com/us/en/tech-effect/emerging-tech/stablecoin-reporting.html)

---

### SOC 2 Type II Controls for Institutional-Grade Custody

**Framework Overview:**

SOC 2 (System and Organization Controls 2) evaluates organizational controls based on five Trust Services Criteria:
1. **Security** - Protection against unauthorized access
2. **Availability** - System uptime and accessibility
3. **Processing Integrity** - Complete, accurate, timely processing
4. **Confidentiality** - Information protected as committed
5. **Privacy** - Personal information handling

**Type I vs. Type II:**
- **Type I:** Point-in-time assessment of control design
- **Type II:** Extended period assessment (typically 6-12 months) of control operating effectiveness

**Required Controls for Crypto Custody:**

| Control Area | Implementation |
|--------------|----------------|
| Access Management | Multi-factor authentication, role-based access |
| Key Management | HSM or MPC for private key protection |
| Segregation | Client assets separated from proprietary holdings |
| Change Management | Documented approval for system changes |
| Incident Response | 24/7 monitoring and response procedures |
| Business Continuity | Redundant systems and disaster recovery |
| Physical Security | Secure facilities, access logging |
| Vendor Management | Third-party risk assessment |

**GENIUS Act Implications:**

Stablecoin issuers must use custodians that are:
- Federally or state-regulated financial institutions
- Subject to examination by primary federal payment stablecoin regulator
- Prohibited from commingling customer assets and stablecoin reserves

**Major Custodians with SOC 2 Type II:**
- Crypto.com Custody Trust Company
- Anchorage Digital
- BitGo Trust Company
- Gemini Trust Company

**SEC Guidance:**
RIAs must ensure a State Trust Company's SOC report covers key custody controls before using as qualified custodian for crypto assets.

Sources:
- [Crypto.com SOC Compliance Announcement](https://crypto.com/us/company-news/custody-soc1-soc2)
- [Cobo: Evaluating Crypto Custody Firms](https://www.cobo.com/post/the-definitive-guide-to-evaluating-crypto-custody-firms-for-institutional-investors)
- [Astraea Law: Qualified Crypto Custodians](https://astraea.law/insights/qualified-crypto-custodians-regulatory-requirements-2025)
- [BitGo: Institutional Custody Provider Guide](https://www.bitgo.com/resources/blog/what-to-look-for-in-an-institutional-crypto-custody-provider/)

---

### Multi-Signature Custody Arrangements for Stablecoin Reserves

**Technology Options Comparison:**

| Feature | Multi-Sig | MPC (TSS) | HSM |
|---------|-----------|-----------|-----|
| **Key Storage** | Multiple complete keys | Distributed key shares | Hardware-secured single key |
| **Signing** | On-chain coordination | Off-chain computation | Hardware-secured signing |
| **Blockchain Support** | Protocol-dependent | Blockchain agnostic | Universal |
| **Transparency** | Publicly visible | Off-chain (private) | Off-chain (private) |
| **Recovery** | Standard key backup | Threshold recovery | Hardware-based |

**Hardware Security Modules (HSMs):**

Best for:
- Highly regulated banks and traditional custodians
- On-premises key storage requirements
- Cold storage for passive portfolios
- Integration with existing enterprise infrastructure

Certifications:
- FIPS 140-2 Level 3
- Common Criteria EAL4+

**Multi-Party Computation (MPC):**

Best for:
- Real-time signing requirements
- Geographic redundancy (distributed key shares)
- DeFi integration
- Cloud-native environments

Key Features:
- No single point of failure
- Key never fully reconstructed during signing
- Threshold schemes (t-of-n quorums)

**Multi-Signature Wallets:**

Best for:
- Maximum transparency (on-chain visible)
- Protocol-native security
- Decentralized governance

Common Configurations:
- 2-of-3 for operational accounts
- 3-of-5 for treasury operations
- 5-of-7 with time delays for large transfers

**Hybrid Approaches:**

Modern institutional custody typically combines:
- MPC for operational signing
- HSM for cold storage reserves
- Multi-sig for governance transactions

**Policy Engine Implementation:**

Enterprise platforms offer configurable approval requirements:
- Transaction amount thresholds
- Destination address whitelisting
- Asset type restrictions
- Time-based delays for large transfers

Example Configuration:
- <$10K: 2-of-3 approvals
- $10K-$100K: 3-of-5 approvals
- >$100K: 5-of-7 with mandatory time delay

Sources:
- [Scalable Solutions: MPC vs HSM](https://scalablesolutions.io/blog/posts/mpc-hsm-custody)
- [Liminal Custody: HSM, MPC, Multi-Sig Differences](https://www.liminalcustody.com/blog/key-differences-between-hsm-mpc-and-multi-sig-wallets-explained/)
- [Ripple: MPC and HSM for Key Management](https://ripple.com/insights/mpc-and-hsm-for-key-management-part-1-demystifying-technology-options-for-digital-asset-custody/)
- [Taurus: HSM vs MPC for Banks](https://www.taurushq.com/blog/what-should-a-bank-choose-between-tss-mpc-and-hsm-for-digital-asset-custody)
- [Cobo: Institutional Crypto Security](https://www.cobo.com/post/is-your-crypto-custody-institution-ready-a-security-benchmark)

---

## Key Findings Summary

### Industry Analysis
1. **Custody costs** range from 0.04%-0.50% annually, with $10K+ setup fees and $500K-$1M minimums
2. **Multi-custodian arrangements** are now standard practice post-SVB, with Circle exemplifying separation of custody (BNY Mellon), asset management (BlackRock), and banking (Cross River)
3. **Smaller issuers** face significant compliance burdens under GENIUS Act; white-label partnerships and bank subsidiary models offer viable paths

### Case Studies
4. **Circle** is well-positioned for GENIUS Act compliance with existing BNY Mellon/BlackRock/Deloitte infrastructure
5. **Ripple's RLUSD** provides monthly Deloitte attestations following NYDFS guidance, with bankruptcy-remote trust structure
6. **Trust company structures** (Paxos, Gemini) offer strongest bankruptcy protections through segregated, regulated reserves
7. **SVB crisis** demonstrated concentration risk; Circle recovered fully but market temporarily lost confidence (USDC to $0.87)

### Technical Implementation
8. **Real-time PoR** achievable with 30-second intervals via API; most issuers still use monthly attestation cycles
9. **SOC 2 Type II** certification is de facto requirement for institutional custody, covering security, availability, and processing integrity
10. **MPC + HSM hybrid** approaches dominate institutional custody, with multi-sig for governance and on-chain transparency

---

## Sources

### Regulatory & Compliance
- [AICPA: GENIUS Act Creates Oversight](https://www.aicpa-cima.com/professional-insights/article/genius-act-creates-oversight-and-opportunity-for-stablecoins)
- [Circle GENIUS Act Compliance](https://www.circle.com/genius-act)
- [WilmerHale: GENIUS Act Guide](https://www.wilmerhale.com/en/insights/client-alerts/20250718-what-the-genius-act-means-for-payment-stablecoin-issuers-banks-and-custodians)
- [Federal Register: FDIC Stablecoin Procedures](https://www.federalregister.gov/documents/2025/12/19/2025-23510/approval-requirements-for-issuance-of-payment-stablecoins-by-subsidiaries-of-fdic-supervised-insured)

### Industry Reports
- [YellowCard: Top Crypto Custodians 2025](https://yellowcard.io/blog/top-crypto-custodians-2025-market-leaders-comparison/)
- [McKinsey: Stablecoins Payments Infrastructure](https://www.mckinsey.com/industries/financial-services/our-insights/the-stable-door-opens-how-tokenized-cash-enables-next-gen-payments)
- [Fireblocks: State of Stablecoins](https://www.fireblocks.com/report/state-of-stablecoins)

### Company Sources
- [Ripple USD Transparency](https://ripple.com/solutions/stablecoin/transparency/)
- [Paxos: Trust Company Stablecoins](https://www.paxos.com/blog/why-trust-company-issued-stablecoins-are-the-safest-path-for-global-finance)
- [BNY Stablecoin Reserves Fund](https://www.bny.com/corporate/global/en/about-us/newsroom/press-release/bny-launches-stablecoin-reserves-fund-expanding-bnys-leadership-digital-assets-130451.html)

### Technical Documentation
- [Hacken: Proof of Reserves Explained](https://hacken.io/discover/proof-of-reserves-explained-from-key-mechanics-to-verification/)
- [Ripple: MPC and HSM Key Management](https://ripple.com/insights/mpc-and-hsm-for-key-management-part-1-demystifying-technology-options-for-digital-asset-custody/)
- [Cobo: Evaluating Crypto Custody Firms](https://www.cobo.com/post/the-definitive-guide-to-evaluating-crypto-custody-firms-for-institutional-investors)
