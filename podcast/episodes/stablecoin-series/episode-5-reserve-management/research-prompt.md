# Episode 5: Reserve Management & Custody Infrastructure

## Core Research Question

How do you safely hold and manage the assets backing a stablecoin, and what infrastructure is required to meet regulatory standards while maintaining operational efficiency?

## Research Objectives

Investigate the full lifecycle of reserve management, from asset composition and custody arrangements to attestation processes and crisis management. Analyze regulatory requirements (GENIUS Act, MiCA, Singapore MAS) and examine how major stablecoins have structured their reserves in practice.

## Key Investigation Areas

### 1. Reserve Composition & Asset Requirements
- What assets are permitted under different regulatory frameworks (cash, bank deposits, Treasury bills, commercial paper, crypto collateral)?
- How do asset maturities affect liquidity and redemption capability?
- What does historical data show about the credit risk of different reserve compositions?
- How did Tether's commercial paper holdings create risk, and what happened when they shifted to Treasuries?
- What is the practical difference between "fully backed" and "actually redeemable" reserves?

### 2. Custody Infrastructure & Qualified Custodians
- What makes a custodian "qualified" under GENIUS Act and MiCA requirements?
- How do custody arrangements differ between fiat reserves (traditional banks) and crypto collateral (DeFi protocols, institutional custodians)?
- What segregation and bankruptcy-remote structures are required?
- How do multi-custodian arrangements reduce single-point-of-failure risks?
- What does it cost to maintain qualified custody relationships?

### 3. Attestation & Audit Requirements
- What is the difference between an attestation and a full audit?
- What do the AICPA 2025 Criteria for Stablecoin Reporting require?
- How frequently must reserves be verified (monthly, quarterly, annually)?
- Who can perform attestations (CPA firms, big four accounting firms, other qualified auditors)?
- What specific disclosures are required (asset types, custodian details, valuation methods)?
- How much do these ongoing compliance costs total?

### 4. Liquidity Management & Redemption Operations
- How do stablecoins manage the tension between holding liquid reserves (low yield) and generating returns?
- What percentage of reserves must be immediately liquid vs. short-term maturities?
- How do redemption mechanisms work in practice (direct with issuer, through exchanges, smart contract burning)?
- What happens when redemption demand spikes (bank runs, de-pegging events)?
- How did Circle manage the Silicon Valley Bank crisis when $3.3B of reserves were trapped?

### 5. Risk Management & Insurance
- What risks exist in reserve management (credit risk, custodian insolvency, operational errors, theft)?
- What insurance products are available and what do they cover?
- How do bankruptcy-remote structures protect user assets from issuer insolvency?
- What recourse do users have if reserves are lost or mismanaged?
- What does rehypothecation mean and why is it prohibited for stablecoin reserves?

### 6. Transparency & Public Reporting
- What transparency practices have different stablecoins adopted (real-time dashboards, monthly reports, quarterly audits)?
- How detailed should reserve breakdowns be (generic "US Treasuries" vs. specific CUSIP identifiers)?
- What does Ripple's RLUSD transparency reporting include?
- How do users verify claims about reserves without full audits?
- What role do blockchain analytics play in tracking supply vs. reserve growth?

## Research Methodology

- **Analyze regulatory texts**: Examine specific requirements in GENIUS Act, MiCA, Singapore MAS, UK FCA proposals
- **Compare reserve compositions**: Review actual attestation reports from USDT, USDC, BUSD, and others
- **Study crisis events**: Analyze SVB collapse, Tether's reserve issues, and other stress tests
- **Evaluate transparency levels**: Compare disclosure practices across major stablecoins
- **Calculate compliance costs**: Estimate custody fees, audit costs, and operational expenses
- **Identify best practices**: Determine what reserve management approaches have proven most resilient
- **Note conflicts of interest**: When attestation firms have relationships with issuers

## Key Questions to Answer

1. What reserve composition provides the best balance of safety, liquidity, and regulatory compliance?
2. What custody arrangements meet regulatory requirements while minimizing operational risk?
3. How often must reserves be attested, by whom, and at what cost?
4. How do stablecoins manage redemptions during bank runs or custodian failures?
5. What transparency standards are sufficient to maintain user confidence?
6. How do different jurisdictions' requirements (US vs. EU vs. Singapore) compare?
7. Can you operate a compliant stablecoin without banking relationships?

## Critical Success Factors to Evaluate

- **Reserve adequacy**: 100%+ backing at all times
- **Asset quality**: Credit rating and maturity of reserve assets
- **Custody security**: Reputation and regulatory status of custodians
- **Attestation frequency**: Monthly minimum under GENIUS Act
- **Transparency**: Public availability of reserve reports
- **Liquidity**: Ability to meet redemption demands under stress
- **Segregation**: Clear separation from issuer's corporate assets

## Sources to Prioritize

- Full text of GENIUS Act reserve and custody requirements
- MiCA asset segregation and custody rules
- AICPA 2025 Criteria for Stablecoin Reporting
- Actual attestation reports from major stablecoins (USDC monthly reports, Tether quarterly reports)
- Case studies: Silicon Valley Bank impact on Circle, Tether's commercial paper reduction
- Central bank research on stablecoin reserve risks (BIS, Fed, ECB)
- Qualified custodian lists and regulatory approvals
- Industry cost benchmarks for custody and attestation services

## Approach to Uncertainty

- Distinguish between regulatory requirements (mandatory) and industry best practices (voluntary)
- Note where regulations are still being finalized or interpreted (MiCA implementation, GENIUS Act rulemaking)
- Acknowledge that different jurisdictions have incompatible requirements
- Identify where attestations provide limited assurance vs. full audit opinions
- Report when reserve composition has changed over time and why
- Recognize that transparency claims vary widely in substance vs. marketing

## Output Goals

The research should provide evidence-based insights into:
- What reserve management practices meet global regulatory standards
- How major stablecoins have structured their custody and attestation arrangements
- What operational challenges arise in managing reserves at scale
- What the true costs of compliance are (custody, audits, banking relationships)
- How reserve management affects stablecoin resilience during crises
- What trade-offs exist between transparency, operational security, and competitive positioning
- Where regulatory requirements are converging vs. diverging globally
