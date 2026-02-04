# Research Brief: Stablecoin Series: Ep. 8, Post-Launch Operations

**Date:** 2026-02-04
**Episode:** Stablecoin Series: Ep. 8, Post-Launch Operations

---

## Research Topic

The operational machinery required to run a stablecoin issuer day-to-day after launch. This episode focuses on the "bank-like" operations that most people don't see: 24/7 monitoring centers, staffing models, vendor ecosystems, enforcement operations, and the actual cost structures of running a stablecoin at scale.

## Key Questions

**Operational Infrastructure:**
1. What does the 24/7 monitoring stack actually look like? What layers must be monitored continuously (reserve composition, transaction flows, counterparty health, systemic risk)?
2. What staffing models exist? How many people does it take to run a $1B, $10B, or $60B stablecoin, and what roles are critical?
3. What is the vendor ecosystem that makes stablecoin operations possible? (Custody, compliance analytics, node infrastructure, payment rails)
4. What are actual operating costs? Personnel, technology infrastructure, compliance vendors, legal, attestation fees?

**Cost Transparency:**
5. What does Circle's S-1 SEC filing reveal about stablecoin economics? Revenue, distribution costs, personnel costs, compliance costs?
6. How does Tether's operating model differ? Staffing levels, profit per employee, transparency vs. opacity?
7. What are the hidden costs in distribution, exchange partnerships, and market maker relationships?

**Multi-Chain Operations:**
8. What does it take to operate native issuance across 15-30 blockchains? Node infrastructure, monitoring, treasury management?
9. How does Circle's CCTP (Cross-Chain Transfer Protocol) work operationally? Burn-and-mint logistics, settlement times, failure modes?
10. When and why do issuers deprecate chains? What does Tether's 2025 chain deprecation reveal about long-term operational burden?

**Enforcement & Compliance Operations:**
11. How do freeze/blacklist operations actually work? What are the two dominant enforcement models (USDT vs. USDC)?
12. What does AMLBot freeze/burn data from 2023-2025 reveal about enforcement frequency, volume, and operational tempo?
13. How do issuers coordinate with law enforcement and exchanges during enforcement actions?
14. What is the staffing and legal infrastructure required for each enforcement model?

**Attestation Cycles:**
15. What is the operational process for monthly reserve attestation under GENIUS Act requirements?
16. Who are the key parties (auditors, custodians, blockchain validators)? What is the timeline and coordination burden?
17. How do attestations differ from full audits? What do AICPA 2025 Criteria for Stablecoin Reporting require?
18. What are the actual costs of attestation and audit for issuers of different sizes?

**Redemption Operations:**
19. What are actual redemption SLAs across major issuers? Minimum amounts, fees, processing times, documented penalties for delays?
20. How do issuers handle the 24/7 blockchain vs. business-hours banking tension?
21. What happens operationally when redemption requests spike? Liquidity management, counterparty coordination?

**Payment Integration:**
22. How do payment processors like Stripe actually integrate stablecoins? What does the architecture look like from merchant to customer to settlement?
23. What operational risks do processors abstract away from merchants vs. what remains merchant responsibility?
24. How do instant settlement systems (Visa USDC settlement, Customers Bank CBIT) work behind the scenes?

**Incident Response:**
25. What operational incidents have occurred beyond the well-known SVB crisis? Smart contract pauses, chain outages, custodian issues, bridge failures?
26. How do issuers communicate during operational incidents? What is the playbook?
27. Why are there no public SRE-style postmortems from major issuers, and what does this opacity mean for enterprise evaluation?

## Context

This is **Episode 8 of 8** in the Stablecoin Series — the **finale** focusing on the operational reality that persists after all the strategic decisions have been made.

**Previous episodes established:**
- Ep 1: Market evolution and competitive landscape
- Ep 2: Legal compliance and regulatory frameworks (GENIUS Act, MiCA details)
- Ep 3: Token economics and monetary design
- Ep 4: Technical architecture and smart contract security
- Ep 5: Reserve management and transparency (SVB crisis, attestation requirements, custody infrastructure)
- Ep 6: Market making, liquidity, and exchange partnerships (market maker costs, liquidity incentives)
- Ep 7: Go-to-market strategy and user adoption (Libra failure, Stripe/Visa partnerships, KYC friction)

**This episode deliberately AVOIDS repeating:**
- SVB crisis narrative and reserve composition debates (covered in Ep 5)
- MakerDAO governance and DAO operational challenges (covered in Ep 5)
- GENIUS Act and MiCA regulatory framework details (covered in Ep 2 and Ep 5)
- Market maker concentration and liquidity incentive mechanisms (covered in Ep 6)
- Go-to-market partnerships and adoption strategies (covered in Ep 7)

**This episode ADD unique operational depth on:**
- The actual cost structure of running a stablecoin (using Circle's S-1 as the transparency benchmark)
- Staffing models and organizational design (Circle's 815-1,200 employees vs. Tether's ~150-235)
- The vendor ecosystem that makes operations possible (Fireblocks, Chainalysis, TRM Labs, etc.)
- Multi-chain operational logistics (CCTP mechanics, hub-and-spoke treasury, deprecation decisions)
- Two enforcement models revealed through AMLBot data (USDT high-throughput vs. USDC judicially-anchored)
- Monthly attestation cycle mechanics (timeline, parties, coordination burden)
- Redemption operations and the fiat-crypto timing mismatch
- Payment processor integration architecture (Stripe as reference implementation)

**Research priorities:**
1. Circle S-1 SEC filing - the only fully transparent cost benchmark in the industry
2. AMLBot 2023-2025 enforcement data - reveals operational differences between USDT and USDC enforcement models
3. Tether's 2025 chain deprecation announcement - shows the long-tail operational burden of multi-chain support
4. AICPA 2025 Criteria for Stablecoin Reporting - defines the attestation standard
5. Stripe stablecoin payment documentation - reveals payment processor integration architecture
6. Industry staffing estimates and cost ranges from market research (DataIntulo, GPT-Researcher analyses)
7. Practitioner complaints from X/Twitter about KYC friction and operational pain points

---

**Next Steps:**
1. Create Phase 1 academic research prompt for Perplexity
2. Run Perplexity research → save to research/p2-perplexity.md
3. Analyze results for question discovery
4. Create targeted Phase 3 prompts for other tools
