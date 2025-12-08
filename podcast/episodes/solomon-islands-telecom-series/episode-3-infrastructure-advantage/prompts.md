# Prompts Used for Episode: Solomon Islands Telecom Series - Ep. 3, Infrastructure Without Capital

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

---

## Setup Phase

**Episode Details:**
- Series: Solomon Islands Telecom Launch Series
- Episode Number: 3
- Date: TBD
- Slug: episode-3-infrastructure-advantage
- Title: Solomon Islands Telecom Series: Ep. 3, Infrastructure Without Capital

---

## Research Phase

### Research Prompt

**Tool Used:** [To be specified by user - e.g., Claude, Gemini, ChatGPT, Perplexity, Grok]

**Date:** 2025-12-08 (prompt created)

**Prompt:**
```
Research the infrastructure economics and technical architecture for launching mobile networks across archipelagos, with specific focus on satellite backhaul vs. traditional submarine cable approaches and the impact of infrastructure partnerships on capital requirements and deployment timelines.

**Context:**
This research is for a podcast episode examining how partnering with an established infrastructure provider (SATSOL - with fiber, Starlink access, and ISO certifications) solves the capital and geographic challenges of launching a mobile network across Solomon Islands' 1,000+ islands. Target audience: infrastructure investors, telecom executives, development finance institutions, and network engineers.

**Key areas to investigate:**

1. **Infrastructure Economics**
   - Typical capital requirements for mobile network launches in Pacific island nations (spectrum, towers, backhaul, core network, power systems)
   - How infrastructure partnerships vs. build-from-scratch change capital requirements and deployment timelines
   - Tower sharing, backhaul leasing, and infrastructure partnership models with cost/timeline trade-offs

2. **Satellite vs. Traditional Backhaul**
   - Starlink satellite backhaul vs. submarine cable + microwave solutions: cost, performance (latency, bandwidth, reliability), deployment speed, scalability
   - Real-world examples of Starlink for cellular backhaul in remote areas
   - Technical limitations and capacity constraints of each approach
   - Hybrid architectures combining fiber (urban) + Starlink (remote islands)

3. **Network Architecture & Deployment**
   - Tower deployment strategies for 85% rural population across dispersed islands
   - SINBIP (Solomon Islands National Broadband Infrastructure Project): 161 tower sites by 2026 - operator access, infrastructure sharing regulations
   - Core network architecture options (cloud vs. on-premise), spectrum strategies (low-band vs. mid-band for island coverage)
   - Technical approaches for low-density rural coverage

4. **Resilience & Climate**
   - Infrastructure hardening for cyclone/earthquake-prone regions
   - Satellite advantages for disaster recovery vs. damaged cable/terrestrial infrastructure
   - Case studies: cyclone impacts on telecom in Pacific (Fiji, Vanuatu, Tonga volcanic eruption)
   - Redundancy strategies and backup power requirements

5. **Regulatory Framework**
   - TCSI spectrum allocation: available frequencies, auction/allocation process, licensing costs
   - Tower siting requirements: land ownership, environmental approvals, community consultation
   - Infrastructure sharing mandates and terms

**Research methodology:**
- Prioritize technical documentation, industry reports from ITU/GSMA/World Bank, and regulatory filings
- Quantify capital and operational costs with specific examples where data exists
- Distinguish between vendor marketing claims and real-world deployment data
- Compare individual case studies against broader industry trends
- Report technical specifications (latency, bandwidth, costs) with sources
- Note funding sources and conflicts of interest in industry analyses
- Include both successful deployments and failed approaches or ongoing challenges
- Cite specific studies, projects, companies, and sources throughout

**Output:** Comprehensive research report with quantitative cost/timeline analysis, technical specifications, regulatory framework details, real-world case studies, and extensive source links for verification.
```

**Note:** See also `research-prompt.md` in this directory for the detailed planning document with additional context and considerations.

---

## Audio Generation Phase

### NotebookLM Prompt

**Date:** 2025-12-08

**Files to Upload to NotebookLM:**
1. `report.md` - Comprehensive research synthesis
2. `research-results.md` - Raw research outputs from Claude, Perplexity, Gemini
3. `sources.md` - Organized source links

**Audio Overview Settings:**
- Format: Deep Dive
- Length: Long

**Prompt:**
```
Create an intellectually rigorous podcast that balances analytical depth with clear explanation.

Opening: Begin with "Yudame Research, Solomon Islands Telecom Launch Series" and introduce the topic's value.

Core principles:
• Spell out acronyms first: "Low Earth Orbit, or LEO satellites" - then use acronym
• Define technical terms immediately in plain language before building on them
• Use concrete examples ONLY from source material - never fabricate
• Highlight findings that reveal strategic lessons or challenge assumptions
• Extract frameworks and connect to practical implications
• Maintain scientific rigor: distinguish correlation from causation, note effect sizes and uncertainties

Emphasis areas:
• Spell-first for acronyms, definition-first for technical terms
• Evidence-based analysis: cite studies, report effect sizes, note sample sizes
• Include human elements when they exist: decisions made, reasoning, outcomes
• Use conversational check-ins: "Let me define that term..." or "To be clear..."
• Translate findings to practical meaning and broader patterns

Highlight insights worth examining:
• Counter-intuitive findings that reveal strategic lessons
• Failures that illustrate specific mistakes or systemic issues
• Unexpected outcomes that challenge assumptions
• Make numbers meaningful through context and comparisons

Avoid:
• Undefined acronyms and jargon
• Academic language when simpler words work
• Introducing 3+ new technical terms in one sentence
• Fabricated examples or over-hedging that obscures findings
• Dry explanations when human stories exist in research
• Repeatedly restating context

Target: Intelligent listeners wanting deep understanding and practical insights. Appreciate technical depth but need terms defined.

Tone: Intellectually rigorous but accessible - "conversational expert explaining to a bright student"

When presenting stories:
• Include decision-making context: "KDDI deployed Starlink to 1,200 towers across Japan's islands" not "A company used satellite"
• Provide specific details: "SINBIP's 161 tower sites funded by CNY 448.9 million" not "A government project"
• Use precise numbers for context: "$15-30 million versus $100+ million traditional deployment" not "much cheaper"
• Show scale through comparisons: "50-80% CAPEX reduction" not "significant savings"
• Connect to lessons: Explain what the outcome reveals about infrastructure economics, partnerships, or resilience strategies

When presenting research: Focus on what numbers mean, use comparisons ("like cutting deployment time from years to months"), translate statistics to implications.

Closing: Summarize 2-3 key takeaways, close with "Find full research and sources at research dot yuda dot me - that's Y-U-D-A dot M-E"
```

---

<!-- Additional prompts will be added below as we progress through the workflow -->


## Cover Art Generation

**Tool Used:** OpenRouter - google/gemini-3-pro-image-preview

**Original Prompt:**
```
Modern podcast episode cover art for "Episode 3 Infrastructure Advantage":

Style: Clean, professional, abstract visualization
Layout: Bold visual elements suitable for square format
Color palette: Deep navy blues and dark blues as the dominant theme throughout
Concept: **Series:** Solomon Islands Telecom Launch Series **Episode:** 3 of 6 **Focus:** How infrastructure partnerships solve the capital and geographic challenges of archipelago mobile network deployment

Design as square format (1024x1024px) with space for text overlay.
Professional, minimalist aesthetic suitable for Apple Podcasts.
No text in the image - pure visual design.
```

**Enhanced Prompt:**
```
Modern podcast episode cover art for "Episode 3 Infrastructure Advantage":

Style: Clean, professional, abstract visualization
Layout: Bold visual elements suitable for square format
Color palette: Deep navy blues and dark blues as the dominant theme throughout
Concept: **Series:** Solomon Islands Telecom Launch Series **Episode:** 3 of 6 **Focus:** How infrastructure partnerships solve the capital and geographic challenges of archipelago mobile network deployment

Design as square format (1024x1024px) with space for text overlay.
Professional, minimalist aesthetic suitable for Apple Podcasts.
No text in the image - pure visual design.

IMPORTANT VISUAL REQUIREMENTS:
- The ENTIRE canvas from edge to edge must be deep navy blue and dark blue tones - no borders, frames, or light backgrounds
- Dark blue fills the complete image area - not just a section or inner frame
- Use bright teal, white, and silver only as accent colors on top of the dark blue theme
- Pure abstract visualization only
- Absolutely no text, no numbers, no labels, no annotations, no icons, no logos, no symbols, no letterforms of any kind
- Clean visual design without any typography or graphic elements

COMPOSITION:
- Visual interest and detail should be concentrated in the LOWER 2/3 of the image
- Keep the TOP 1/3 relatively simple and uncluttered for text overlay placement
- Main graphic elements should flow from center to bottom
- Avoid placing busy patterns or focal points in the upper third
```

**Aspect Ratio:** 1:1

**Output:** cover.png

**Date:** 2025-12-08

**Branding Applied:**
- Position: top-left
- Brand: Yudame Research
- Series: Solomon Islands Telecom Launch Series
- Episode: Ep 3 - Infrastructure Without Capital
- Border: 20px, #FFC20E

**Final Specifications:**
- Base size: 1024x1024px
- With 20px border: 1064x1064px total
- Color scheme: Dark navy/blue dominant, teal/white/silver accents
- File format: PNG
- Clean abstract visualization with podcast branding overlay

---

## Audio Processing Phase

**Audio File:** Financing_Telecoms_in_Remote_Island_Nations.m4a
**Converted to:** episode-3-infrastructure-advantage.mp3
**Duration:** 35:25
**File Size:** 34,006,967 bytes

**Transcription:**
- Tool: Local Whisper (openai-whisper)
- Model: base
- Output: episode-3-infrastructure-advantage_transcript.json
- Segments: 693 total
- Date: 2025-12-08

**Chapters:**
- Count: 14 chapters
- Created by analyzing transcript for natural topic transitions
- Formats: FFmpeg metadata (.txt) and Podcasting 2.0 (.json)
- Embedded into mp3 file
- Chapter breakdown:
  1. Introduction: The Connectivity Paradox (0:00-2:00)
  2. CapEx vs OpEx: Understanding the Economics (2:00-5:00)
  3. The Historical Benchmark: $850M in PNG (5:00-8:00)
  4. Solomon Islands Cost Premium: 35% More Expensive (8:00-11:00)
  5. SINBIP: Government's $66M Infrastructure Investment (11:00-14:00)
  6. The Land Dispute Bottleneck (14:00-17:00)
  7. Backhaul Economics: The False Binary (17:00-20:00)
  8. LEO Satellites Break the Trade-off (20:00-23:00)
  9. KDDI Japan: 1200 Towers on Starlink (23:00-26:00)
  10. Hybrid Architecture: Fiber, Microwave, and LEO (26:00-29:00)
  11. 700 MHz Spectrum: The Coverage Multiplier (29:00-32:00)
  12. Tonga Disaster: 38 Days Without Connectivity (32:00-34:00)
  13. Market Analysis: Duopoly and Partnership Strategy (34:00-35:00)
  14. NPV Analysis: The Blueprint for Success (35:00-35:25)

**Date:** 2025-12-08

---
