# Episode Content Plan: Token Economic Design & Stabilization Mechanisms

**Series:** Stablecoin Series
**Episode:** 3 of 3
**Title:** Token Economic Design & Stabilization Mechanisms
**Date:** 2025-12-26

---

## Episode Context

This is the final episode in a three-part stablecoin series:
- Episode 1: Market structure and competitive dynamics
- Episode 2: Regulatory frameworks (GENIUS Act, MiCA, global approaches)
- Episode 3 (this episode): Token economics and stabilization mechanisms

The audience has foundational knowledge from prior episodes. This episode focuses on the technical and economic design choices that determine stablecoin stability and sustainability.

---

## Three-Section Structure

### Section 1: The Foundation of Stablecoin Stability (8-10 min)
**Theme:** Why collateralization design determines survival

**Key concepts to define:**
- Death spiral (circular collapse where redemptions accelerate price decline)
- Peg Stability Module (PSM) - MakerDAO's 1:1 exchange mechanism
- Delta-neutral hedging (offsetting long/short positions to neutralize market exposure)
- Funding rate (periodic payments between long/short perpetual futures holders)
- Over-collateralization ratio (collateral required per dollar of stablecoin)

**Core content:**
- The collateral quality hierarchy: fiat-backed (USDT, USDC) → crypto-overcollateralized (DAI) → hybrid (Ethena USDe) → algorithmic (Terra UST - failed)
- Why USDT+USDC control 93% of market share
- Tether's reserve evolution: commercial paper (65% in 2021) → Treasury bills (70%+ today, $113B+)
- Arbitrage mechanics: only 6 active USDT arbitrageurs, largest accounts for 64-66% of redemptions

**Transition:** These theoretical distinctions become concrete when we examine what happens during market stress...

### Section 2: The Evidence from Failure (12-15 min)
**Theme:** Historical failures encode specific design lessons

**Key failures to analyze:**
1. **Terra/UST (May 2022)** - $42-45B destroyed
   - MIT researchers: "not single-entity manipulation" but "growing concerns about sustainability"
   - LUNA hyperinflated from 1B to 6.5T tokens in 3 days
   - Sophisticated investors ran first; retail "bought the dip"

2. **Iron Finance (June 2021)** - TITAN crash from $64 to $0.00000006
   - 75% USDC / 25% TITAN backing
   - 10-minute oracle TWAP couldn't track rapid price decline
   - IRON stabilized at $0.75 (its USDC floor)

3. **USDC/SVB (March 2023)** - de-peg to $0.87
   - Circle's 8% exposure to SVB ($3.3B of $40B reserves)
   - DAI PSM became contagion channel
   - Resolved only by Fed/Treasury/FDIC Sunday announcement

4. **Ethena USDe (October 2025)** - $8.3B redemptions
   - Market cap: $14.8B → ~$6B
   - Temporary de-peg on secondary venues
   - Issuer redemption maintained at $1

**Revenue model sustainability:**
- Anchor Protocol: 19.5% APY unsustainable, $6M daily subsidies, 7:1 deposit-to-borrow ratio
- MakerDAO: $4.6B in Treasuries, $243M revenue 2024 (10x from 2022)
- Ethena: Only 8.84% of days with negative returns historically, but $39-60M insurance fund is limited

**Transition:** These failures reveal fundamental design principles that now inform both protocol development and regulatory response...

### Section 3: Design Principles and Regulatory Response (8-10 min)
**Theme:** How lessons from failure shaped the regulatory convergence

**Governance tradeoffs:**
- MakerDAO: 48-hour execution delay rendered SVB crisis changes moot
- Circle: Immediate communication, new Cross River Bank partnership same weekend
- Flash loan attacks: BProtocol borrowed 13,000 MKR via dYdX, passed vote, repaid in single transaction
- Frax two-governor model: FraxGovernorAlpha (40% quorum/5-day) + FraxGovernorOmega (4% quorum/2-day)

**Regulatory convergence:**
- GENIUS Act (July 2025): 1:1 backing, T-bills ≤93 days, monthly CEO/CFO certification, algorithmic stablecoin prohibition
- MiCA (June 2024): Circle achieved EMI license; Tether USDT delisted from EU exchanges
- Tether relocated to El Salvador (January 2025)
- FSOC removed digital assets from systemic risk list (December 2025)

**Design principles derived from failures:**
1. Full collateralization with liquid assets (T-bills, not commercial paper)
2. Reserve diversification (SVB concentration lesson)
3. Sustainable revenue from external sources (not token subsidies)
4. Governance mechanisms enabling rapid response without full centralization

**Closing:**
- MIT insight: Design robustness matters more than disclosure - sophisticated investors ran first despite blockchain transparency
- Market outlook: $300B market today, projected $500-750B by 2030
- The $60B+ in collapsed stablecoin value has produced the regulatory and design standards we see today

---

## NotebookLM Episode Focus Prompt

Use this exact prompt when generating the audio:

```
This is a Yudame Research podcast episode, part of our Stablecoin Series. Begin the episode by saying "Welcome to Yudame Research" and mention this is Episode 3 of the Stablecoin Series, covering Token Economic Design and Stabilization Mechanisms.

CORE PRINCIPLES:
- Spell out all acronyms on first use (e.g., "USDT, or Tether" not just "USDT")
- Define technical terms when introducing them
- When citing research, name the researchers or institutions
- Use specific numbers and data points, not vague language
- Maintain intellectual rigor while being accessible

NARRATIVE REQUIREMENTS:
1. Opening hook: The $42-45 billion Terra collapse demonstrates why stablecoin design choices determine survival
2. Three-section flow: Foundation → Evidence from Failure → Design Principles
3. Key failures to discuss: Terra/UST, Iron Finance, USDC/SVB crisis, Ethena October 2025
4. Revenue model comparison: Anchor's unsustainable 19.5% vs. MakerDAO's Treasury-backed model
5. Regulatory convergence: GENIUS Act and MiCA effectively prohibit algorithmic designs
6. Closing callback: The $60B in collapsed value produced today's standards

TERMS TO DEFINE:
- Death spiral
- Peg Stability Module
- Delta-neutral hedging
- Funding rate
- Over-collateralization

TONE:
Intellectually rigorous but accessible. This is the third episode in the series, so listeners have context from previous episodes on market structure and regulation.

Close by summarizing the key design principles and directing listeners to research.bwforce.ai for the full report.
```

---

## Key Sources to Emphasize

**Academic/Government:**
- BIS Working Paper 1164 on algorithmic stablecoin fragility
- MIT researchers Liu, Makarov, Schoar on Terra collapse
- Federal Reserve FEDS Notes on SVB stablecoin impact

**Regulatory:**
- GENIUS Act S.1582 requirements
- MiCA enforcement actions
- FSB October 2025 thematic review

**Industry:**
- TRM Labs 2025 market data (93% USDT+USDC concentration)
- ChainArgos Ethena USDe case study
- MakerDAO governance portal documentation

---

## Podcast Audio Specifications

- Target duration: 28-38 minutes
- Format: Two-host conversational (NotebookLM Deep Dive style)
- Opening: "Welcome to Yudame Research" + series context
- Closing: Summary + website URL (research.bwforce.ai)
