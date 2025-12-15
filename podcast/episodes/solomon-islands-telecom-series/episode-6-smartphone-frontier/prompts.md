# Prompts Used for Episode: Solomon Islands Telecom Series - Ep. 6, The Smartphone Frontier

This document tracks all prompts used during the creation of this episode for reproducibility and learning.

**Note:** The `research-prompt.md` in this directory contains the seed research ideas and objectives. The prompts below are the actual copy-paste-ready prompts used with deep research tools.

---

## Setup Phase

**Episode Details:**
- Date: 2025-12-14
- Series: Solomon Islands Telecom Series
- Episode: 6 of 6
- Slug: episode-6-smartphone-frontier
- Title: Solomon Islands Telecom Series: Ep. 6, The Smartphone Frontier - First-Time Users and Device Strategy

**Previous Episodes Context:**
- Ep. 1: Financial ecosystem (75% unbanked, 70% mobile ownership with mostly feature phones)
- Ep. 2: Duopoly competitive landscape (no number portability creates switching friction)
- Ep. 3: SATSOL partnership (fiber + Starlink infrastructure)
- Ep. 4: IumiCash integration (mobile money requiring smartphones vs. M-SELEN's USSD)
- Ep. 5: Launch execution (regulatory, network, distribution, customer acquisition)

---

## Deep Research Phase

### Tool Configuration
- **Perplexity:** Academic & Official Sources (Phase 1 - always used)
- **Grok:** Real-Time & Regional Sources (Phase 3 - typically used)
- **ChatGPT Deep Research:** Industry & Technical Sources (Phase 3 - typically used)
- **Gemini Deep Research:** Strategic & Policy Sources (Phase 3 - typically used)
- **Claude Deep Research:** Comprehensive Synthesis (Phase 3 - use when complex questions need multi-dimensional analysis)

**Default approach:** Use all Phase 3 tools (Grok, ChatGPT, Gemini, Claude) unless a tool's focus area is clearly not relevant to the topic.

### Deep Research Prompts (Copy-Paste Ready)

**IMPORTANT:** These prompts use single newlines only to prevent accidental partial submissions when pasting into Chrome-based tools.

---

## Phase 1: Perplexity - Academic Foundation

**Perplexity Prompt (Pro Search enabled):**

```
Research smartphone adoption and device provisioning strategies in emerging markets, with focus on Pacific island nations and markets similar to Solomon Islands (70% mobile ownership, mostly feature phones, 75% unbanked, low smartphone penetration).

**Research methodology:**
- Prioritize peer-reviewed studies, meta-analyses, systematic reviews, and authoritative sources
- Distinguish between correlation and causation in findings
- Report effect sizes and practical significance, not just statistical significance
- Note the study populations and whether findings generalize to relevant demographics
- Compare individual studies against meta-analyses and systematic reviews
- Identify preliminary research vs. well-replicated findings
- Note funding sources and potential conflicts of interest when relevant
- Include contradictory findings and areas of scientific uncertainty
- Cite specific studies, researchers, and sources throughout
- Provide full source URLs for all citations

**Output:** Comprehensive research report with extensive citations, sample sizes, methodological details, and source links.
```

---

## Phase 2: Question Discovery

**After analyzing Perplexity's academic research, here are the questions we should investigate:**

### What subtopics and themes emerged?
- **Multidimensional barriers beyond cost:** Affordability, infrastructure gaps, digital literacy, gender inequality, content/language barriers
- **Device provisioning models:** PAYGO financing, BNPL models, government subsidies, device trade-ins
- **Mobile money-smartphone nexus:** How mobile money adoption drives smartphone demand and vice versa
- **Infrastructure paradox:** Coverage-usage divide (86% coverage, 27% usage in Pacific)
- **Feature phone persistence:** Why feature phones persist despite smartphone availability
- **Gender-specific barriers:** Women face 2x cost burden relative to income
- **Research methodology limitations:** Almost no Pacific island-specific RCTs

**Coverage depth:**
- EXTENSIVE: Affordability barriers, PAYGO models, infrastructure gaps, gender inequality
- MODERATE: Government subsidies (China case study), mobile money nexus, digital literacy
- BRIEF: Content/language barriers, device trade-ins, circular economy models

### What gaps exist in the academic literature?
- **Geographic gap:** Virtually no peer-reviewed RCTs in Pacific island contexts specifically
- **Solomon Islands specificity:** Research cites SI statistics but draws conclusions from Uganda, Malawi, India RCTs
- **Cultural factors:** Limited research on how Pacific cultural dynamics affect adoption (kastom, kinship networks, communal ownership)
- **Island-specific logistics:** Delivery costs 5x higher in archipelagos mentioned but not deeply analyzed
- **Mobile money timing:** Research predates Solomon Islands' mobile money launch (early 2023) - how has it actually affected smartphone demand?
- **Feature phone to smartphone transition:** What triggers the switch? What's the tipping point?
- **Device sustainability:** Phone attrition rates, longevity in tropical/island environments, repair ecosystems

### What recent developments aren't covered?
- **Solomon Islands mobile money reality (2023-2025):** Our Telekom's IumiCash launched early 2023 - what's actual adoption? Does it drive smartphone demand as theory predicts?
- **SATSOL fiber+Starlink impact:** New infrastructure dramatically changes coverage reality - how does this affect smartphone viability?
- **Regional device programs:** Are there ANY current device provisioning programs in Pacific nations? PNG? Fiji? Vanuatu?
- **Post-pandemic dynamics:** COVID accelerated digital adoption globally - did this reach Solomon Islands?
- **China subsidy program lessons:** Research shows 5% YoY decline by week 11 despite subsidies - what does this mean for SI subsidy viability?
- **Current device costs:** Research cites historical affordability data - what are entry-level smartphones actually costing in SI market TODAY?
- **Operator strategies:** What are Our Telekom and bmobile/Vodafone actually doing re: device financing in 2024-2025?

### What contradictions or uncertainties need more sources?
- **Subsidy effectiveness paradox:** China's subsidies drove 3-5x initial surge but 5% YoY decline by week 11 - when do subsidies work vs. fail?
- **Income effects uncertainty:** Roessler et al. found significant weekly income gains but null monthly effects - sustainability question unresolved
- **Digital literacy threshold:** What level of literacy is actually required for smartphone utility? 42% digital literacy in SI - is that sufficient or barrier?
- **Infrastructure causality:** Does infrastructure enable adoption, or does adoption demand pull infrastructure? Which comes first in island contexts?
- **PAYGO vs BNPL superiority:** Research says PAYGO "generally most suitable" for unbanked, but limited empirical comparison in island markets
- **Gender gap interventions:** What actually works to close the 25% smartphone gender gap? Research describes problem well but solutions less so

### What industry/implementation questions arose?
- **Actual device provisioning programs:** Who's running PAYGO/BNPL in similar markets? What are the business models? Success rates?
- **Operator economics:** What's the unit economics for telcos financing devices to unbanked customers? Risk models? Default rates?
- **Supply chain practicalities:** How do you actually GET devices to outer islands? Distribution partnerships? Costs?
- **Handset ecosystem:** What brands/models work in SI price point? Chinese brands (Tecno, Infinix)? Refurbished devices?
- **After-sales support:** Repair, warranty, replacement in island contexts where devices might take weeks to reach users
- **M-SELEN vs IumiCash dynamics:** Feature phone USSD (M-SELEN) vs smartphone-based (IumiCash) - does this create natural upgrade path?
- **Platform lock-in:** If users get devices from one carrier, does lack of number portability lock them in? Strategic implications?

### What policy/regulatory angles need investigation?
- **Government subsidy feasibility:** SI government budget constraints - can they afford subsidy programs? Political will?
- **Universal service obligations:** Does SI have USO requirements that could fund device programs?
- **Import duties/taxes:** What taxes apply to device imports? Could reduction improve affordability?
- **Consumer protection:** Regulations around device financing, repossession, credit reporting in markets with limited financial infrastructure
- **Regional policy coordination:** Pacific Islands Forum or regional approaches to device access?
- **Digital inclusion strategies:** Is smartphone access part of SI's national digital strategy? Official targets?
- **Competition policy:** Could regulators mandate number portability to reduce device lock-in? (Episode 2 context)

### What practitioner perspectives are missing?
- **Telco operators:** What are Our Telekom and bmobile/Vodafone actually planning/doing for devices?
- **Mobile money providers:** How are IumiCash and M-SELEN thinking about device barriers to their services?
- **Retailers/distributors:** What are device sellers in Honiara seeing? Demand patterns? Financing requests?
- **Development organizations:** What are GSMA, World Bank, ADB recommending/funding for Pacific device access?
- **Regional telcos:** What are operators in Fiji, PNG, Vanuatu doing that could inform SI strategy?
- **MNO executives:** Digicel (regional player) - any device programs in other Pacific markets?
- **First-time smartphone users:** What do people transitioning from feature phones actually experience? Barriers? Value?

---

## Phase 3: Targeted Followup Research

Based on the Phase 2 question discovery, here are the specific prompts for each research tool:

### Grok - Recent Developments & Practitioner Perspectives

```
Research smartphone adoption and device provisioning in Solomon Islands and Pacific island nations, focusing on these specific questions:

**Recent Developments (2023-2025):**
- What is the actual adoption and usage of Our Telekom's IumiCash mobile money service since its early 2023 launch? Has it driven smartphone demand?
- How has the SATSOL fiber and Starlink infrastructure deployment (2023-2024) affected smartphone viability and adoption in Solomon Islands?
- What device provisioning or financing programs are currently operating in Pacific nations (Solomon Islands, PNG, Fiji, Vanuatu)? Any operator-led or government programs?
- What are Our Telekom and bmobile/Vodafone actually doing regarding device financing or subsidies in 2024-2025?

**Practitioner Perspectives:**
- What are telco operators, mobile money providers, and device retailers in Solomon Islands and Pacific markets saying about device barriers and strategies?
- What are regional telcos (Digicel, Vodafone Pacific) doing for device access in other Pacific markets that could inform Solomon Islands?
- What are development organizations (GSMA, World Bank, ADB, Pacific Islands Forum) recommending or funding for Pacific device access?

**Market Reality:**
- What are entry-level smartphones actually costing in Solomon Islands retail market today?
- What device brands and models are popular in Pacific island markets at affordable price points (Chinese brands like Tecno, Infinix, refurbished devices)?

Focus on: Recent news, industry discussions on X/Twitter, practitioner insights, regional sources, Pacific telecom developments.
Provide findings with source links, publication dates, and credibility indicators.
```

---

### GPT-Researcher - Industry & Case Studies

```
Research smartphone device provisioning and financing models in emerging markets, focusing on these specific questions:

**Industry Analysis & Business Models:**
- What are the actual business models, unit economics, and success rates of PAYGO and BNPL device financing programs in unbanked emerging markets?
- What are the default rates, risk models, and profitability for telcos financing smartphones to unbanked customers?
- How do operators handle device lock-in, repossession, and credit assessment without traditional banking infrastructure?

**Case Studies & Implementation:**
- Which telcos are running successful device financing programs in markets similar to Solomon Islands (island nations, high unbanked rates, low smartphone penetration)?
- What specific programs exist in African markets (M-Pesa ecosystem, Safaricom, Vodacom), Asian markets, and any Pacific examples?
- What are the supply chain and distribution strategies for getting devices to remote island communities? Partnership models? Costs?

**Technical & Operational Details:**
- What device brands and models work best at sub-$100 price points for emerging markets? Chinese brands (Tecno, Infinix), refurbished devices, feature brands?
- How do operators handle after-sales support, repair, warranty, and replacement in island contexts with difficult logistics?
- What role do mobile money platforms play in device financing repayment? Integration between services?

**Comparative Analysis:**
- How does the China 2025 subsidy program's failure (5% YoY decline by week 11) inform subsidy viability in small island markets?
- What's the relationship between feature phone-based mobile money (USSD like M-SELEN) and smartphone-based services (apps like IumiCash) in driving device upgrades?

Focus on: Industry analyst reports, market research, case studies, technical documentation, financial/business analysis, operator earnings calls.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

---

### Gemini Deep Research - Policy & Strategic Context

```
Research smartphone access policy and regulatory frameworks in Pacific island nations and similar emerging markets, focusing on these specific questions:

**Regulatory & Policy Frameworks:**
- What are Solomon Islands' national digital inclusion strategies, ICT policies, and official targets regarding smartphone or internet access?
- Does Solomon Islands have Universal Service Obligations (USO) that could fund device access programs? How are USO funds currently allocated?
- What import duties, taxes, and tariffs apply to smartphone imports in Solomon Islands? Could reductions improve affordability?
- What consumer protection regulations exist around device financing, credit, repossession in markets with limited financial infrastructure?

**Comparative Policy Analysis:**
- What policies have Pacific island nations (PNG, Fiji, Vanuatu, Samoa) implemented to improve device affordability and access?
- Are there regional approaches through Pacific Islands Forum, Pacific Community (SPC), or regional telecom organizations?
- What can Solomon Islands learn from successful device access policies in other small island developing states (SIDS) globally?

**Strategic Context:**
- How does lack of number portability (Episode 2 context) interact with device financing to create platform lock-in? Could regulators address this?
- What is the Solomon Islands government's budget capacity and political will for device subsidy programs?
- How do development partners (World Bank, ADB, GSMA) recommend Pacific nations approach device access as infrastructure challenge vs. market solution?

**Regulatory Considerations:**
- What regulations govern mobile network operators offering credit or financing in Solomon Islands?
- Are there financial inclusion mandates or targets that smartphone access affects?
- How do gender equality commitments intersect with the 25% smartphone gender gap in policy frameworks?

Focus on: Regulatory frameworks, legislation, government policy documents, strategic plans, comparative policy analysis, development organization recommendations.
Provide findings with official source citations, effective dates, and policy context.
```

---

### Claude Deep Research - Comprehensive Synthesis

```
Research smartphone adoption barriers and device provisioning strategies in Pacific island contexts (specifically Solomon Islands), focusing on these specific questions requiring multi-dimensional analysis:

- What is the relationship between mobile money adoption (IumiCash launched early 2023) and smartphone demand in Solomon Islands context, given the theoretical mobile money-smartphone nexus identified in academic research but actual Pacific implementation data gap?
- How do the five co-equal adoption barriers (affordability, infrastructure, digital literacy, gender, content/language) interact systemically in island archipelagos like Solomon Islands, and which interventions address multiple barriers simultaneously?
- What does the evidence reveal about the effectiveness of different device provisioning models (PAYGO, BNBL, subsidies) specifically in contexts with 75% unbanked population, extreme geographic dispersion, and limited logistics infrastructure?
- How does the infrastructure-adoption causality question play out in island markets—does infrastructure enable adoption (build it and they'll come) or does adoption demand pull infrastructure investment, and what does this mean for Solomon Islands' SATSOL fiber+Starlink deployment strategy?
- What triggers the feature phone to smartphone transition in emerging markets, and how do feature phone-based services (USSD like M-SELEN) vs smartphone-required services (apps like IumiCash) create upgrade incentives or barriers?

**Research methodology:**
- Conduct comprehensive research across academic, industry, policy, and recent sources
- Prioritize authoritative sources and distinguish correlation from causation
- Note methodological limitations and conflicts of interest
- Include contradictory findings and areas of uncertainty
- Cite specific studies, reports, and sources extensively with URLs
- Focus on evidence applicable to Pacific island contexts and small island developing states (SIDS)
```

---


## Cover Art Generation

**Tool Used:** OpenRouter - google/gemini-3-pro-image-preview

**Original Prompt:**
```
Modern podcast episode cover art for "Episode 6 Smartphone Frontier":

Style: Clean, professional, abstract visualization
Layout: Bold visual elements suitable for square format
Color palette: Deep navy blues and dark blues as the dominant theme throughout
Concept: The mobile towers are standing. The signals are broadcasting. Across the Pacific islands, 86% of the population lives within range of a mobile broadband network. Yet only 27% actually use mobile inter

Design as square format (1024x1024px) with space for text overlay.
Professional, minimalist aesthetic suitable for Apple Podcasts.
No text in the image - pure visual design.
```

**Enhanced Prompt:**
```
Modern podcast episode cover art for "Episode 6 Smartphone Frontier":

Style: Clean, professional, abstract visualization
Layout: Bold visual elements suitable for square format
Color palette: Deep navy blues and dark blues as the dominant theme throughout
Concept: The mobile towers are standing. The signals are broadcasting. Across the Pacific islands, 86% of the population lives within range of a mobile broadband network. Yet only 27% actually use mobile inter

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

**Branding Applied:**
- Position: top-left
- Brand: Yudame Research
- Series: Solomon Islands Telecom
- Episode: Ep 6 - Smartphone Frontier
- Border: 20px, #FFC20E

**Final Dimensions:** 1064x1064px (with 20px border)
**File Size:** ~1.2MB

**Date:** 2025-12-14

---

## Audio Processing Phase

**Audio File:** Towers_Stand_But_Devices_Stay_Dark.m4a
**Converted to:** episode-6-smartphone-frontier.mp3
**Duration:** 36:49
**File Size:** 35,359,483 bytes (~33.7 MB)

**Transcription:**
- Tool: Local Whisper (openai-whisper)
- Model: base
- Output: episode-6-smartphone-frontier_transcript.json
- Date: 2025-12-15

**Chapters:**
- Count: 12 chapters
- Created by analyzing transcript for natural topic transitions
- Formats: FFmpeg metadata (.txt) and Podcasting 2.0 (.json)
- Embedded into mp3 file

**Chapter List:**
1. Introduction: The 59-Point Coverage-Usage Gap (0:00-4:00)
2. The Ecosystem Framework: Five Co-Equal Barriers (4:00-8:00)
3. Barrier One: Affordability and the 30% Income Burden (8:00-11:00)
4. Barrier Two: Infrastructure - The $170/Month Data Cost (11:00-14:00)
5. Barriers Three & Four: Digital Literacy and Content (14:00-17:00)
6. Barrier Five: Gender Inequality as Multiplier (17:00-20:00)
7. China's Subsidy Experiment: Week 11 Failure (20:00-25:00)
8. Pay-As-You-Go Financing: The M-KOPA Model (25:00-30:00)
9. The Circular Dependency: Mobile Money Lock (30:00-35:00)
10. Regulatory Lock-In: Absence of Number Portability (35:00-40:00)
11. Policy Choice: Vanuatu's 98% vs Solomon Islands' 42% (40:00-45:00)
12. Stepping Stones & Strategic Lessons (45:00-46:49)

**Date:** 2025-12-15
