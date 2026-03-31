# Content Plan: Stablecoin Series - Ep. 5, Reserve Management & Custody Infrastructure

## Episode Metadata

| Field | Value |
|-------|-------|
| **Series** | Stablecoin Series |
| **Episode** | 5 of 6 |
| **Title** | Reserve Management & Custody Infrastructure |
| **Slug** | episode-5-reserve-management |
| **Target Duration** | 35-45 minutes |
| **Target Word Count** | 4,500-6,000 words (report) |
| **Actual Word Count** | 4,864 words |

---

## Episode Summary

This episode examines how stablecoin issuers safely hold and manage the assets backing their tokens, exploring the custody infrastructure, regulatory frameworks, and verification mechanisms that determine whether stablecoins can survive a banking crisis. Opening with Circle's $3.3 billion SVB exposure and the "disclosure paradox," we trace how 2025's regulatory frameworks (GENIUS Act, MiCA, Singapore MAS) attempt to prevent the next crisis—and where significant uncertainties remain.

---

## Key Themes

### Primary Theme
**Trust Architecture**: How do we build systems that maintain confidence in digital money when the underlying assets can become inaccessible overnight?

### Secondary Themes
1. **Regulatory Divergence**: Three frameworks, three philosophies—sovereign risk vs. bank exposure vs. local nexus requirements
2. **Transparency Paradox**: Circle's honesty about SVB exposure triggered the run—disclosure as both protection and vulnerability
3. **Legal Untested Waters**: GENIUS Act bankruptcy provisions are innovative but no court has tested them
4. **Yield Prohibition Arbitrage**: The loophole economy of wrappers and "rewards" vs. "interest"
5. **Cryptographic Limits**: Real-time proof of reserves advances, but off-chain liabilities remain unknowable

---

## Narrative Structure

### Opening (Hook)
The SVB crisis story: $3.3 billion frozen, USDC at $0.87, Circle's $0.34M equity, and the Sunday evening federal announcement that saved everything.

### Act 1: Foundation (WHY)
- SVB crisis timeline and operational vulnerabilities
- Three regulatory philosophies compared
- Key terminology (attestation vs. audit, bankruptcy remoteness, proof of reserves, MPC)

### Act 2: Evidence (WHAT)
- Reserve requirements comparison table
- GENIUS Act bankruptcy provisions and Levitin critique
- AICPA 2025 Criteria breakdown
- Major stablecoin transparency comparison (USDT, USDC, RLUSD, PYUSD)

### Act 3: Application (HOW)
- Multi-custodian arrangements (Circle's model)
- Custody technology (HSM, MPC, multi-sig)
- Interest prohibition loopholes (Coinbase rewards, Ethena yields)
- Real-time proof of reserves and fundamental limitations

### Closing (Callback)
Return to SVB theme—the new frameworks represent genuine progress, but "structural protections + cryptographic verification + regulatory compliance = complete safety" remains an unsolved equation.

---

## Key Data Points

| Statistic | Source |
|-----------|--------|
| Circle SVB exposure: $3.3B (8% of reserves, 34% of cash) | Fed analysis, multiple sources |
| USDC low: $0.805-$0.87 | TradingView, Bloomberg |
| Circle stockholders' equity end 2023: $0.34M | SEC S-1 filing |
| GENIUS Act Treasury maturity limit: 93 days | Legislative text |
| MiCA deposit requirement: 30% (60% significant) | EU Regulation |
| Singapore MAS custodian credit rating: A- | MAS guidance |
| RLUSD market cap: $1.26B | Yahoo Finance |
| Tether reserves include $8.83B secured loans, $7.66B Bitcoin | Claude research |
| Custody costs: 0.04%-0.50% annually | Industry reports |
| Coinbase USDC rewards: up to 4.1% APY | Company announcement |
| Ethena sUSDe average yield 2024: ~18% APY | Protocol data |
| JPMorgan projection: yield-bearing stablecoins could reach 50% market share | Analyst report |

---

## Practitioner Quotes

1. **Adam Levitin (Georgetown Law)**: "The Act is written in such a way that no trustee in their right mind would sign on to facilitate an insolvent stablecoin issuer's bankruptcy."

2. **Brian Armstrong (Coinbase CEO)**: "First, we are not the issuer. And second, we don't pay interest in yield, we pay rewards."

3. **Paolo Ardoino (Tether CEO)**: "Big Four firms are afraid to work with Tether because they fear it will damage their reputations."

4. **John Reed Stark (former SEC)**: "An attestation report is not the same as an audit report. It is an 'unverified snapshot,' which would never pass any sort of regulatory muster."

5. **BIS Research**: Disclosure of SVB exposure "acted as a public signal" that precipitated the crisis (disclosure paradox).

---

## Cover Art Direction

**Visual Concept**: A vault door or safe, partially open, revealing layers of security infrastructure—but with subtle cracks or question marks suggesting uncertainty.

**Alternative Concepts**:
- A digital balance scale weighing different reserve assets (Treasuries vs. bank deposits vs. crypto)
- A transparent glass vault showing stacked assets, some accessible, some frozen/inaccessible
- A bridge spanning between traditional banking (bank building) and digital (blockchain nodes)

**Color Palette**: Institutional trust colors (dark blue, gold) with subtle warning elements (amber accents)

**Text Elements**:
- Series: "Stablecoin Series"
- Episode: "Episode 5"
- Title: "Reserve Management"

---

## NotebookLM Prompt

**Standard template from skill file - DO NOT CUSTOMIZE:**

```
Create an engaging podcast discussion about this research that:
- Uses conversational, accessible language while maintaining accuracy
- Explains technical concepts with helpful analogies
- Highlights the most surprising or counterintuitive findings
- Maintains a balanced perspective on controversial topics
- Includes natural back-and-forth between hosts exploring different angles
- Builds toward actionable insights listeners can apply
```

---

## Episode Feed Entry Template

```xml
<item>
  <title>Stablecoin Series - Ep. 5: Reserve Management &amp; Custody Infrastructure</title>
  <description><![CDATA[
    How do stablecoin issuers safely hold billions in assets? This episode examines the custody infrastructure, regulatory frameworks (GENIUS Act, MiCA, Singapore MAS), and verification mechanisms that determine whether your stablecoins can survive a banking crisis—opening with Circle's $3.3 billion SVB exposure and the "disclosure paradox."

    Full report: https://research.yuda.me/podcast/episodes/stablecoin-series/episode-5-reserve-management/report

    Key Sources:
    • GENIUS Act (S.1582) - congress.gov
    • AICPA 2025 Stablecoin Criteria - aicpa-cima.com
    • Circle Transparency Portal - circle.com/transparency
    • Ripple USD Transparency - ripple.com/solutions/stablecoin/transparency
  ]]></description>
  <link>https://research.yuda.me/podcast/episodes/stablecoin-series/episode-5-reserve-management/</link>
  <guid isPermaLink="false">stablecoin-series-ep5-reserve-management-2025-12-26</guid>
  <pubDate>[RFC 2822 DATE]</pubDate>
  <enclosure url="https://research.yuda.me/podcast/episodes/stablecoin-series/episode-5-reserve-management/[FILENAME].mp3" length="[FILE_SIZE_BYTES]" type="audio/mpeg"/>
  <itunes:duration>[DURATION]</itunes:duration>
  <itunes:explicit>false</itunes:explicit>
  <itunes:episode>5</itunes:episode>
  <itunes:episodeType>full</itunes:episodeType>
  <podcast:chapters url="https://research.yuda.me/podcast/episodes/stablecoin-series/episode-5-reserve-management/[FILENAME]_chapters.json" type="application/json+chapters"/>
</item>
```

---

## Workflow Status

| Phase | Status | Notes |
|-------|--------|-------|
| 1. Episode Setup | ✅ Complete | Directory structure created |
| 2. Research Prompts | ✅ Complete | 5 tools used |
| 3. Deep Research | ✅ Complete | ~164KB across 5 sources |
| 4. Question Discovery | ✅ Complete | Targeted followup created |
| 5. Cross-Validation | ✅ Complete | p3-briefing.md created |
| 6. Report Synthesis | ✅ Complete | 4,864 words |
| 7. Content Plan | ✅ Complete | This file |
| 8. Cover Art | ⏳ Pending | Ready to generate |
| 9. Audio Generation | ⏳ Pending | NotebookLM API |
| 10. Audio Processing | ⏳ Pending | Transcribe, chapters |
| 11. Publishing | ⏳ Pending | Feed update |

---

## Files Created

```
episode-5-reserve-management/
├── research-prompt.md (seed ideas)
├── sources.md
├── content_plan.md (this file)
├── report.md (4,864 words)
├── research/
│   ├── p1-brief.md
│   ├── p2-perplexity.md (65KB)
│   ├── p2-claude.md (31KB)
│   ├── p2-gemini.md (32KB)
│   ├── p2-chatgpt.md (24KB)
│   ├── p2-grok.md (12KB)
│   └── p3-briefing.md (master briefing)
├── logs/
│   └── prompts.md
└── tmp/
```
