# GPT-Researcher Results

**Date:** 2026-02-04 12:44

**Model:** openai:gpt-5.2

**Prompt:** Research stablecoin post-launch operations, focusing on these specific questions:

**OCC Trust Charter Conditions:**
- Circle, Ripple, Paxos, Fidelity Digital Assets, and BitGo received conditional OCC trust charter approvals in December 2025. What are the CONDITIONS? What operational requirements did they agree to?

**Payment Processor Integration Architecture:**
- How do Stripe, Visa, and Mastercard technically integrate stablecoin settlements?
- Stripe's architecture for USDC payments: wallet connection methods, settlement APIs, reconciliation processes
- Visa's USDC settlement (launched December 2025): how does 7-day settlement window work operationally?
- Mastercard partnerships: which exist and what's the technical integration model?

**Multi-Chain Treasury Operations:**
- How do market makers actually rebalance USDC/USDT across chains? Profitability, gas fee costs, operational friction points?
- Hub-and-spoke treasury model: how much liquidity sits on each chain? How often is rebalancing needed?
- CCTP (Cross-Chain Transfer Protocol) real-world usage data: volume, settlement times, failure rates

**Operational Incident Case Studies:**
- Beyond SVB crisis, what operational incidents have occurred? Chain outages, custodian issues, bridge failures, smart contract pauses?
- Response playbooks and postmortems (if any exist)

**Smaller Issuer Operations ($1B-$5B scale):**
- How do mid-scale issuers differ operationally from Circle/Tether?
- What operational shortcuts or vendor dependencies exist?
- Cost structure differences and scaling challenges

**Bridge Security Playbooks:**
- Post-Wormhole and post-$2.8B bridge hacks, what operational security practices have emerged?
- Monitoring systems, validator set management, fraud detection

**Smart Contract Upgrade Procedures:**
- How do issuers handle smart contract upgrades? Governance, testing, rollback plans

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.

---

# Stablecoin Post‑Launch Operations (as of 2026‑02‑04): OCC Trust Charters, Processor Integrations, Multi‑Chain Treasury, Incidents, and Operational Controls

## Executive synthesis (my conclusions up front)

Stablecoin “post-launch operations” has converged toward a recognizable operating model: (1) regulated custody and treasury rails (increasingly bank- or trust‑charter aligned), (2) payment-processor abstractions that keep merchants in fiat while supporting on‑chain payer flows, and (3) multi‑chain liquidity operations that are *still* bottlenecked by bridges, governance, and chain reliability.

Based on the evidence available in the provided sources, the **most concrete operational shift in late 2025** is:  
- **Visa’s USDC settlement expansion into the U.S.** creates an institutional “7‑day settlement” option that is explicitly designed to integrate with existing treasury operations while improving weekend/holiday resilience—*without changing the consumer card experience* ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html); [Visa, 2025b](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21951.html)).  
- **Stripe’s stablecoin acceptance** keeps merchants operationally in USD while exposing crypto wallet payment UX through a hosted flow (crypto.stripe.com) and supports specific tokens/networks (USDC across Ethereum, Solana, Polygon, Base; plus USDP and USDG on limited networks) ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments); [Stripe, n.d.-b](https://docs.stripe.com/payments/accept-stablecoin-payments)).  
- **OCC “conditional approval” trust charters** (Circle, Ripple, Paxos, BitGo, Fidelity Digital Assets) are publicly characterized as requiring further AML/KYC and other operational/regulatory readiness steps before full operations—yet **the precise conditions are not published** in the sources provided. Operationally, that means market participants should treat these approvals as *non-final* and expect a multi-phase readiness program rather than an immediate capability upgrade ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters); [Banking Dive, 2025](https://www.bankingdive.com/news/occ-national-trust-bank-charter-approve-circle-paxos-ripple-bitgo-gould-crypto/807799/); [Yahoo Finance, 2025](https://finance.yahoo.com/news/circle-ripple-paxos-fidelity-bitgo-164313047.html)).  

Where the industry remains operationally fragile is **governance and upgrade control** in smart-contract systems and bridges. The Unleash Protocol incident (losses ~**$3.9M**) illustrates that “technically valid” on-chain actions can still be operationally unauthorized due to governance abuse via multisig/admin control, and that post-incident bridging/asset movement can complicate investigations ([Scorechain, 2025](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)). This is a direct operational lesson for stablecoin issuers, custodians, and payment firms: governance and permissions are first-class attack surfaces.

---

## OCC Trust Charter Conditions (December 2025): What is known vs. not publicly specified

### What happened (facts from sources)

In December 2025, the OCC granted **conditional approvals** for national trust bank charters to multiple digital asset firms (Circle, Ripple, Paxos, BitGo, Fidelity Digital Assets). Circle and Ripple were approved for *de novo* national trust banks; Paxos, BitGo, and Fidelity Digital Assets were conditionally approved for conversion of existing state charters to national trust charters ([Banking Dive, 2025](https://www.bankingdive.com/news/occ-national-trust-bank-charter-approve-circle-paxos-ripple-bitgo-gould-crypto/807799/); [Yahoo Finance, 2025](https://finance.yahoo.com/news/circle-ripple-paxos-fidelity-bitgo-164313047.html)).

A legal analysis source emphasizes:  
- the approvals are **not final** charters,  
- each firm must meet additional **regulatory and operational requirements**, including **AML and KYC compliance**, before commencing full operations,  
- the OCC has **not published a comprehensive list** of conditions nor a definitive timeline ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters)).

### So what are the “conditions” and operational requirements?

**The provided sources do not disclose a condition-by-condition list.** The most defensible answer—given the material—is:

1. **Conditions were imposed but not publicly enumerated**, i.e., not available as a comprehensive list in the OCC’s public messaging as cited by the legal summary. ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters))  
2. **Minimum operational themes explicitly mentioned** include:  
   - **AML program readiness** and  
   - **KYC / customer identification compliance** before full operations. ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters))  
3. The approvals imply a **pre-opening supervision and readiness plan** (typical for conditional bank approvals), but **the specific supervisory protocols are not disclosed** in the cited material. ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters))

### Practical operational interpretation (opinion grounded in the evidence)
Because the conditions are not public, **treat conditional approval as a signal of regulatory trajectory rather than immediate operational capability**. The operational commitment is best understood as: the firms accepted a set of pre-opening requirements (policy, controls, auditability, and staffing) with *at least* AML/KYC explicitly called out, and potentially broader governance/risk-management obligations typical of trust banks—yet **you cannot responsibly claim the full list without additional primary OCC documents** beyond what’s provided here.

#### Table: What is knowable now (from the sources) vs. unknowable without additional OCC documentation

| Topic | What the sources support | What is not specified in sources |
|---|---|---|
| Conditional approval status | Approvals are conditional, not final charters ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters)) | Exact condition list |
| Core conditions mentioned | Must meet additional regulatory/operational requirements including AML/KYC ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters)) | Detailed requirements: capital, policies, exams, model risk, vendor mgmt, etc. |
| Timeline | No definitive timeline provided ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters)) | Milestones/dates |

---

## Payment Processor Integration Architecture: Stripe, Visa, and Mastercard

### Stripe: architecture for stablecoin payments (USDC focus)

#### Supported assets/networks and product surface
Stripe documents explicitly describe stablecoin acceptance under the **Crypto payment method**. Supported presentment includes **USDC on Ethereum, Solana, Polygon, and Base** (plus USDP and USDG on select networks). Stripe supports recurring payments and refunds/partial refunds; disputes are not supported ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)).

**Integration surfaces:** Payment Links, Checkout, Elements, Payment Intents API—behind which the customer is redirected to a hosted crypto experience ([Stripe, n.d.-b](https://docs.stripe.com/payments/accept-stablecoin-payments)).

#### Wallet connection & payment flow (customer UX and control plane)
Operationally, the payer flow is:
1. Customer selects Crypto payment option at checkout.
2. Customer is redirected to **crypto.stripe.com** to **connect a crypto wallet**, select currency, and select payment network.
3. Stripe confirms payment and notifies completion, with optional redirect back to merchant confirmation ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)).

This is a critical architectural choice: **Stripe controls the wallet connection and chain selection UX via a hosted domain**, reducing merchant exposure to wallet fragmentation and signing flows.

#### Settlement and reconciliation model (merchant ops)
Stripe’s docs state: **completed stablecoin payments settle in the merchant’s Stripe balance in USD**, meaning merchants are generally not holding USDC on their own balance sheet for these flows ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)). This implies:
- Stripe bears the conversion/settlement complexity (token receipt, confirmations, conversion to USD),
- Merchants reconcile like normal Stripe payments (USD ledger entries) rather than reconciling on-chain events directly.

Stripe also provides a B2B framing: Stripe Billing can confirm USDC payments “on the blockchain” and settle fiat into the account so AR teams do not need blockchain explorers—another statement of Stripe’s intent to abstract chain operations away from enterprise finance teams ([Stripe, 2025](https://stripe.com/en-sg/resources/more/b2b-stablecoin-payments)).

#### Stripe Connect: stablecoin payouts (two-ledger model)
In Connect stablecoin payouts (private preview), Stripe states:
- Platform balance remains **fiat**,  
- Stripe handles conversion and payout in **USDC** to a linked wallet.  
Operationally, connected users link a wallet in Express Dashboard; they see a USDC balance like other local balances; transfers created in USD automatically convert to recipient’s preferred currency (USDC) ([Stripe, n.d.-c](https://docs.stripe.com/connect/stablecoin-payouts)).

**Limitations**: US-only Connect platforms; payouts only to individuals/sole proprietors in supported countries; no companies/nonprofits yet ([Stripe, n.d.-c](https://docs.stripe.com/connect/stablecoin-payouts)).

#### Stripe operational implications (opinion)
Stripe’s model is best characterized as **“crypto at the edge, fiat at the core”**:
- It minimizes enterprise treasury disruption (books remain USD),
- It centralizes chain risk and operational burden at Stripe,
- It creates a clean reconciliation story (Stripe ledger vs. on-chain TXIDs as supplemental audit artifacts).

This is *operationally* more mature than direct on-chain merchant acceptance, but it increases concentration risk in the processor (availability, sanctions screening, chain support decisions).

---

### Visa: USDC settlement in the U.S. (launched Dec 2025) and 7‑day settlement operations

#### What Visa launched (facts)
Visa announced USDC settlement in the United States, enabling U.S. issuer and acquirer partners to settle VisaNet obligations using **Circle’s USDC** rather than only fiat. Settlement occurs on “supported blockchains.” Visa cited **more than $3.5B in annualized stablecoin settlement volume** and named initial banking participants **Cross River Bank** and **Lead Bank** ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)).

Visa claims benefits:
- faster funds movement over blockchains,
- seven-day availability (weekends/holidays),
- enhanced operational resilience,
- no change to consumer card experience ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)).

#### 7-day settlement window: what it means operationally
Visa describes “7-day settlement windows” as enabling banks/fintechs to settle seven days a week instead of traditional five-business-day windows, alongside “modernized liquidity and treasury management” and interoperability ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html); [Visa, 2025b](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21951.html)).

Operationally, that implies:
- **Treasury operations must support weekend/holiday staffing or automation** (even if reduced headcount) because liquidity movement is available daily.
- **Cutoff schedules** become *policy-based* rather than bank-calendar constrained. Participants likely define daily settlement cycles, exception handling, and liquidity buffers.
- **Collateral and prefunding** could be optimized; Visa’s FAQ explicitly mentions collateral reduction “consideration” for parties settling 7 days/week and “predictability from a fully reserved” asset ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)).

Visa also emphasizes “integrate seamlessly with existing treasury operations,” suggesting participant banks plug USDC flows into standard treasury tooling (cash positioning, reconciliations), but with a new rail (blockchain) ([Visa, 2025b](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21951.html)).

#### Visa integration architecture (what’s specified vs. unspecified)
What’s specified:
- Settlement uses **USDC** and occurs on supported blockchains, for select issuer/acquirer partners ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)).
- This is about **VisaNet settlement obligations**, not consumer payments UX changes ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)).

What’s not specified in the provided material:
- which blockchains are supported in the U.S. launch,
- wallet/custody model (self-custody vs. qualified custodian),
- message formats / APIs for settlement instructions,
- reconciliation mechanism (on-chain TXIDs to Visa settlement reports).

#### Visa operational interpretation (opinion)
Visa is institutionalizing stablecoins as a **back-end settlement asset**, not a consumer payment method. That distinction matters: Visa can gain resilience and speed in inter-institution settlement while preserving the card network’s established risk and dispute layers for end users. The 7‑day window is a real operational step-change: it pushes banks to treat blockchain settlement as **always-on liquidity infrastructure**, which will favor participants with automation, mature treasury controls, and robust compliance monitoring.

---

### Mastercard partnerships: what exists and integration model (limits of provided sources)

**No Mastercard-specific sources were included** in the provided information set. Therefore, I cannot responsibly list Mastercard partnerships or a technical model with citations from your dataset.

What can be said (methodologically):
- To answer this section to your requested standard (“industry analyst reports, market research, technical documentation”), you would need Mastercard press releases, developer docs (e.g., Mastercard Crypto Credential, Multi-Token Network), partnership announcements (issuers, exchanges, settlement providers), or analyst coverage—none of which are present here.

---

## Multi‑Chain Treasury Operations (USDC/USDT rebalancing, hub-and-spoke liquidity, CCTP usage)

### What the provided sources contain
The supplied sources **do not include** market maker playbooks, multi-chain rebalancing cost data, or CCTP metrics (volume/settlement time/failure rates). As a result, I cannot present quantified, cited findings on:
- chain-by-chain liquidity allocations,
- rebalancing frequency distributions,
- net profitability after gas/bridge fees,
- CCTP production telemetry.

### Operational reality (bounded, evidence-driven inference)
Even without direct market-maker data in the sources, the Scorechain incident analysis is relevant: it highlights how governance abuse can lead to funds being bridged out rapidly using third-party infrastructure, and emphasizes the need for “network-level context” and that exposure can materialize before transactions look suspicious ([Scorechain, 2025](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)). This supports a conservative operational view:

- **Bridging is operationally central** to multi-chain treasury, and also a high-risk zone (investigation complexity, asset flight speed).
- **Operational monitoring must incorporate governance/admin actions**, not just transactional heuristics.

### Practical recommendations (opinion)
Given the lack of hard data here, the safest operational stance for multi-chain treasury is:
- minimize bridge dependence where possible,
- prefer native mint/burn or issuer-supported cross-chain mechanisms where available,
- maintain automated exposure alerts for governance/admin events and privileged operations (multisig changes, upgrades), because those can precede fund movements.

---

## Operational Incident Case Studies (beyond SVB): governance failures, contract upgrades, bridging

### Unleash Protocol incident (Dec 2025): governance as an operational attack surface
Unleash reported unauthorized activity leading to estimated losses of **~$3.9M**, where an attacker gained administrative control via Unleash’s multisig governance and executed an unauthorized contract upgrade enabling withdrawals. Affected assets included USDC and others; after withdrawals, assets were bridged using third-party infrastructure and moved to external addresses ([Scorechain, 2025](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)).

Key operational takeaways explicitly stated:
- governance structures are a primary attack surface,
- risk can materialize before transactions appear suspicious,
- technical authorization does not eliminate downstream exposure,
- network-level context is essential for timely investigations ([Scorechain, 2025](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)).

### Incident response playbooks (what exists in sources)
No full postmortem or formal playbook document is included in the dataset. However, the Scorechain analysis implies an effective response posture should include:
- governance/permission monitoring,
- early exposure identification rather than transaction-only alerting,
- investigative capability across bridges and cross-chain hops ([Scorechain, 2025](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)).

### My operational view (opinion)
The Unleash case is not merely “a DeFi exploit”; it is an *operations failure mode* that also threatens stablecoin ecosystems because stablecoins are often among the stolen/bridged assets. For stablecoin issuers and payment processors, the lesson is to treat:
- governance events (admin changes, upgrades),
- bridge usage spikes,
- unusual cross-chain dispersal patterns  
as core risk signals integrated into compliance and treasury monitoring—not as “security team only” concerns.

---

## Smaller Issuer Operations ($1B–$5B scale): how they differ (limits + constrained analysis)

### Source limitations
None of the included sources provide detailed operating models or cost structures for mid-scale issuers.

### What can still be concluded from the ecosystem signals available
- Regulatory trajectory: OCC conditional approvals suggest a direction of travel toward trust-bank-like operational rigor for major issuers/custodians; mid-scale issuers may face comparatively higher per-dollar compliance overhead due to less scale leverage, making vendor dependence more likely ([Buchanan Ingersoll & Rooney, 2025](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters)).
- Payment processor abstraction (Stripe) lowers the need for merchants—and potentially smaller issuers working with merchants—to run direct on-chain reconciliation systems, but it also centralizes product access through a few processors ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)).

### My view (opinion)
At $1B–$5B, issuers likely optimize for speed-to-market via:
- custodians, KYT/AML vendors, and managed reserve administrators,
- narrower chain support to reduce operational surface area,
- heavier reliance on processors/exchanges for distribution.

This is operationally rational but creates correlated vendor and concentration risks, and can degrade resilience during provider outages or policy changes.

---

## Bridge Security Playbooks and Smart Contract Upgrade Procedures (post-hack operational controls)

### What is directly evidenced in the sources
The Scorechain analysis details how governance abuse enables “technically valid” but unauthorized upgrades and notes that transaction-level monitoring may miss misuse of admin authority ([Scorechain, 2025](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)).

### Operational controls implied by the incident (playbook elements)
From the described failure mode, the emergent “playbook” should include:

1. **Privileged access hardening**
   - minimize admin keys,
   - enforce multisig with robust signer hygiene,
   - strict separation between emergency roles and upgrade roles.

2. **Governance anomaly monitoring**
   - alert on signer changes,
   - alert on timelock bypass or unexpected upgrade execution,
   - correlate governance events with subsequent asset movements (especially bridge interactions).

3. **Upgrade safety procedure**
   - staged deployments,
   - formal approvals (off-chain policy) and on-chain enforcement (timelocks),
   - rollback-ready architecture (or pause/guardrails) with clear operational authority.

4. **Cross-chain flight monitoring**
   - detect bridging to third-party infrastructure soon after an admin event,
   - pre-arranged coordination with exchanges/custodians for rapid tracing/freezing where possible.

These are not “nice-to-haves”; the Unleash scenario shows governance abuse can cause immediate loss before conventional fraud systems trigger ([Scorechain, 2025](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)).

---

## Comparative analysis: Processor-led vs network-led stablecoin operations

### Table: Stripe vs Visa (and what cannot be concluded about Mastercard from this dataset)

| Dimension | Stripe stablecoin payments | Visa USDC settlement (U.S.) | Mastercard |
|---|---|---|---|
| Primary use case | Customer pays with stablecoin; merchant settles in USD | Issuer/acquirer settles VisaNet obligations in USDC | Not supported by provided sources |
| Wallet UX | Hosted redirect to crypto.stripe.com for wallet connect and network selection ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)) | Not described (back-end settlement) | — |
| Merchant/partner treasury impact | Merchant stays in fiat; Stripe abstracts chain operations ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)) | Partner treasuries integrate USDC settlement; 7-day windows improve liquidity timing ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)) | — |
| Availability | Depends on blockchain and Stripe processing; payout timing varies by network ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)) | 7-day settlement windows; weekend/holiday resilience ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)) | — |
| Disputes | No dispute support ([Stripe, n.d.-a](https://docs.stripe.com/payments/stablecoin-payments)) | Card experience unchanged (implies existing consumer protections remain) ([Visa, 2025a](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)) | — |

---

## What you should do next (to complete the missing parts to analyst-report standard)

Several of your questions require sources not present here (Mastercard integration models, market maker rebalancing economics, CCTP production statistics, bridge hack “post-$2.8B” comparative analysis, and issuer cost structures). To complete those sections with citations and numbers, you would need to add:
- Mastercard developer/press materials and partner announcements,
- Circle CCTP telemetry or dashboards / third-party analytics,
- institutional prime broker / MM writeups and on-chain analytics reports,
- bridge postmortems and security firm reports.

---

## References (APA; unique URLs only)

Banking Dive. (2025, December 12). *OCC green-lights Circle, Ripple, Paxos for national trust bank charters*. [url website](https://www.bankingdive.com/news/occ-national-trust-bank-charter-approve-circle-paxos-ripple-bitgo-gould-crypto/807799/)

Buchanan Ingersoll & Rooney PC. (2025). *OCC Grants Conditional Approval to Crypto Firms for National Trust Bank Charters*. [url website](https://www.bipc.com/occ-grants-conditional-approval-to-crypto-firms-for-national-trust-bank-charters)

Scorechain. (2025, December 30). *Unleash Protocol Incident Shows How Governance Failures Escalate Risk*. [url website](https://www.scorechain.com/blog/unleash-protocol-incident-shows-how-governance-failures-escalate-risk)

Stripe. (n.d.-a). *Stablecoin payments | Stripe Documentation*. [url website](https://docs.stripe.com/payments/stablecoin-payments)

Stripe. (n.d.-b). *Accept stablecoin payments | Stripe Documentation*. [url website](https://docs.stripe.com/payments/accept-stablecoin-payments)

Stripe. (n.d.-c). *Stablecoin payouts for Connect | Stripe Documentation*. [url website](https://docs.stripe.com/connect/stablecoin-payouts)

Stripe. (2025). *How B2B stablecoin payments work*. [url website](https://stripe.com/en-sg/resources/more/b2b-stablecoin-payments)

Visa. (2025a, December 16). *Visa Launches Stablecoin Settlement in the United States, Marking a Breakthrough for Stablecoin Integration*. [url website](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)

Visa. (2025b). *Visa Launches Stablecoin Settlement in the United States, Marking a Breakthrough for Stablecoin Integration | Press Release*. [url website](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21951.html)

Yahoo Finance. (2025, December 12). *Circle, Ripple, Paxos, Fidelity and BitGo Get Banking Charters Approved by OCC*. [url website](https://finance.yahoo.com/news/circle-ripple-paxos-fidelity-bitgo-164313047.html)