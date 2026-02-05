# Gold-Standard Research Workflow

---

## Status Update (2026-02-05)

### Summary

This document was created as an aspirational vision for "publication-quality research that happens to become podcasts." Since then, **Wave 1 of the podcast improvement plan** (validated Feb 4, 2026 on Stablecoin Ep. 8) has implemented many of the practical research quality improvements from this plan.

**Key finding:** The full academic rigor proposed here (16 phases, 20-35 hours, 3-4 weeks per episode) is appropriate for research publications but exceeds what's needed for podcast production. The **pragmatic subset** implemented in Wave 1 achieves significant quality gains (+16 points, 28 to 44/50) while maintaining podcast production timelines.

### What Has Been Implemented

The following goals from this document have been achieved via Wave 1 (Tasks B1.1-B1.3, B2.1-B2.2):

| Goal | Status | Implementation |
|------|--------|----------------|
| ✅ **Depth distribution analysis** | IMPLEMENTED | Wave 1 Task B1.1 - Required section in `p3-briefing-enhanced.md` |
| ✅ **Source quality tiering** | RETAINED | Already in workflow as Tier 1/2/3 source organization |
| ✅ **Evidence hierarchy awareness** | RETAINED | Synthesis agent requirements distinguish meta-analyses from case studies |
| ✅ **Contradiction surfacing** | ENHANCED | Wave 1 Task B1.2 - Counterpoint Discovery section in briefing |
| ✅ **Practical implementation audit** | IMPLEMENTED | Wave 1 Task B1.3 - "How would someone do this?" for each finding |
| ✅ **Takeaway clarity requirements** | IMPLEMENTED | Wave 1 Task B2.1 - Explicit takeaways in Notes for Synthesis Agent |
| ✅ **Story/example collection** | IMPLEMENTED | Wave 1 Task B2.2 - Story Bank with memorability ratings |
| ✅ **Bias acknowledgment** | RETAINED | AI tool bias documented in briefing template |
| ✅ **Cross-validation matrix** | RETAINED | Multi-source verification in Phase 5 |
| ✅ **Research gaps documentation** | ENHANCED | Required section in enhanced briefing template |

### What Remains Valuable (Future Enhancement)

These items from this document are NOT yet implemented but could add value for high-stakes episodes:

| Item | Value | When to Use |
|------|-------|-------------|
| **Phase 0: Research Protocol** | HIGH | For topics requiring academic defensibility (health, policy) |
| **Phase 2.5: Primary Source Collection** | MEDIUM | For regulatory/legal topics requiring original documents |
| **Phase 4.5: Expert Consultation** | HIGH | For contentious topics or when research gaps are identified |
| **Phase 5.5: External Peer Review** | HIGH | For flagship episodes or topics with public health implications |
| **Manual database searches** (PubMed, ERIC) | MEDIUM | When AI-mediated summaries miss key academic sources |
| **PRISMA flow diagram** | LOW | For formal research publications, not podcast production |
| **Newcastle-Ottawa Scale** | LOW | For formal study quality assessment beyond current tiering |
| **Complete audit trail** | MEDIUM | For reproducibility in contentious topics |

### What Is Obsolete or Superseded

| Item | Status | Reason |
|------|--------|--------|
| **16-phase workflow** | SUPERSEDED | Current 12-phase workflow with Wave 1 enhancements achieves similar quality |
| **20-35 hours per episode** | SUPERSEDED | Current workflow: ~8-15 hours including all improvements |
| **3-4 weeks calendar time** | SUPERSEDED | Current workflow: 1-3 days with automation |
| **Pre-registered protocol for every episode** | REDUCED SCOPE | Only needed for high-stakes topics |
| **External peer review for every episode** | REDUCED SCOPE | Reserve for flagship episodes |
| **FOIA requests, interlibrary loans** | IMPRACTICAL | Exceeds podcast production timelines |

### Recommended Use of This Document

1. **For standard episodes:** Use the current workflow (`.claude/skills/new-podcast-episode.md`) with Wave 1 enhancements. This document is NOT needed.

2. **For high-stakes episodes** (health claims, policy analysis, contentious topics): Selectively apply:
   - Phase 0 (Research Protocol) for methodology transparency
   - Phase 4.5 (Expert Consultation) for validation
   - Phase 5.5 (External Peer Review) for accountability

3. **For future workflow evolution:** Use the detailed templates in Phases 0, 2.5, 4.5, and 5.5 as starting points when expanding research rigor.

### References to Wave 1 Implementation

- **Enhanced briefing template:** `docs/templates/p3-briefing-enhanced.md`
- **Workflow with exit criteria:** `.claude/skills/new-podcast-episode.md` (Phase 6)
- **Synthesis agent with validation:** `.claude/agents/podcast-synthesis-writer.md`
- **Improvement plan details:** `docs/plans/podcast_episode_improvements.md` (Wave 1 section)

---

## Executive Summary

This document proposes enhancements to transform our podcast research workflow from "excellent for podcasts" to "publication-quality research that happens to become podcasts." The enhanced workflow incorporates systematic literature review methodology, primary source verification, expert consultation, formal bias assessment, and external peer review.

**Key Principle:** Every enhancement prioritizes methodological rigor over speed. Human steps are acceptable and often preferred for quality-critical decisions.

**Target Quality Level:** Research outputs should be defensible in academic peer review, citable by other researchers, and verifiable by fact-checkers.

> **Note (2026-02-05):** The full workflow below represents maximum rigor. For standard podcast production, see the Status Update above for the pragmatic subset now implemented.

---

## Current State Assessment

### Strengths (Retain These)

| Element | Description | Quality | Status (2026-02-05) |
|---------|-------------|---------|---------------------|
| Sequential question discovery | Phase 2 analyzes initial results to inform targeted followup | Excellent | ✅ RETAINED |
| Multi-tool triangulation | 5 research tools with different strengths | Excellent | ✅ RETAINED |
| Cross-validation matrix | Explicit tracking of multi-source verification | Very Good | ✅ RETAINED |
| Source quality tiering | Tier 1/2/3 hierarchy | Very Good | ✅ RETAINED |
| Evidence hierarchy awareness | Distinguishes meta-analyses from case studies | Very Good | ✅ RETAINED |
| Synthesis agent standards | Strict evidence requirements, no fabrication | Very Good | ✅ ENHANCED (Wave 1) |
| Contradiction surfacing | Explicitly flags disagreements | Very Good | ✅ ENHANCED (B1.2 Counterpoint Discovery) |

### Gaps to Address

| Gap | Current State | Target State | Status (2026-02-05) |
|-----|---------------|--------------|---------------------|
| Research protocol | Ad-hoc research questions | Pre-registered protocol with inclusion/exclusion criteria | 🔶 OPTIONAL (high-stakes only) |
| Literature search | AI-mediated summaries | Systematic database searches + AI augmentation | 🔶 OPTIONAL (when AI misses sources) |
| Primary sources | AI extracts and summarizes | Original documents archived with provenance | 🔶 OPTIONAL (regulatory topics) |
| Expert input | Secondhand via Grok/X | Direct expert consultation (email, interviews) | 🔶 FUTURE (Phase 4.5 template ready) |
| Source verification | AI cross-reference | Human spot-check of critical claims | ✅ PARTIAL (cross-validation matrix) |
| Bias assessment | Mentioned in prompts | Formal bias assessment protocol | ✅ PARTIAL (AI tool bias in template) |
| Peer review | Self-verification checklist | External expert review | 🔶 OPTIONAL (flagship episodes) |
| Audit trail | Partial (prompts.md) | Complete research log with timestamps | ✅ IMPROVED (logs/ directory) |
| Historical depth | AI knowledge cutoffs | Archive.org, historical databases, primary archives | 🔶 FUTURE (not implemented) |
| **Depth distribution** | Uneven topic coverage | Analyze and balance depth across subtopics | ✅ IMPLEMENTED (B1.1) |
| **Practical implementation** | Conceptual findings only | "How would someone do this?" audit | ✅ IMPLEMENTED (B1.3) |
| **Takeaway clarity** | Implicit conclusions | Explicit 1-3 core takeaways | ✅ IMPLEMENTED (B2.1) |
| **Story collection** | Ad-hoc examples | Curated Story Bank with memorability ratings | ✅ IMPLEMENTED (B2.2) |

---

## Proposed Workflow: 16 Phases

The enhanced workflow expands from 12 phases to 16 phases, adding:
- **Phase 0:** Research Protocol Development
- **Phase 2.5:** Primary Source Collection
- **Phase 4.5:** Expert Consultation
- **Phase 5.5:** External Peer Review

> **Status (2026-02-05):** The current production workflow uses 12 phases with Wave 1 enhancements. The 4 additional phases below (0, 2.5, 4.5, 5.5) are **optional** for high-stakes episodes only. Templates remain valuable as reference.

### Phase Overview

```
Phase 0:   Research Protocol Development (NEW) ← 🔶 OPTIONAL: High-stakes only
Phase 1:   Setup ← ✅ IN PRODUCTION
Phase 2:   Academic Foundation (Perplexity + Database Searches) ← ✅ IN PRODUCTION
Phase 2.5: Primary Source Collection (NEW) ← 🔶 OPTIONAL: Regulatory topics
Phase 3:   Question Discovery ← ✅ IN PRODUCTION
Phase 4:   Targeted Followup Research ← ✅ IN PRODUCTION
Phase 4.5: Expert Consultation (NEW) ← 🔶 OPTIONAL: Contentious topics
Phase 5:   Cross-Validation & Verification ← ✅ IN PRODUCTION (Enhanced with Wave 1)
Phase 5.5: External Peer Review (NEW) ← 🔶 OPTIONAL: Flagship episodes
Phase 6:   Master Research Briefing ← ✅ IN PRODUCTION (Enhanced with Wave 1 B1.1-B2.2)
Phase 7:   Synthesis ← ✅ IN PRODUCTION
Phase 8:   Cover Art ← ✅ IN PRODUCTION (now Episode Planning in current workflow)
Phase 9:   Audio from User (NotebookLM) ← ✅ IN PRODUCTION
Phase 10:  Audio Processing ← ✅ IN PRODUCTION
Phase 11:  Publishing ← ✅ IN PRODUCTION
Phase 12:  Commit & Push ← ✅ IN PRODUCTION
```

---

## Phase 0: Research Protocol Development (NEW)

> **Status (2026-02-05):** 🔶 OPTIONAL - Use for high-stakes episodes requiring academic defensibility (health claims, policy analysis, contentious topics). Not required for standard podcast production.

**Purpose:** Establish explicit research methodology before any data collection. This is the foundation of reproducible, defensible research.

**Time Required:** 30-60 minutes (human)

**Outputs:**
- `research/p0-protocol.md` - Research protocol document
- Registered in `docs/protocols/` directory for institutional memory

### Step 0.1: Define Research Question

Write a clear, answerable research question using the PICO/SPIDER framework:

**For intervention/effectiveness topics (PICO):**
- **P**opulation: Who is affected?
- **I**ntervention: What action/policy/treatment?
- **C**omparison: Compared to what alternative?
- **O**utcome: What are we measuring?

**For exploratory/qualitative topics (SPIDER):**
- **S**ample: Who/what are we studying?
- **P**henomenon of **I**nterest: What are we exploring?
- **D**esign: What type of research?
- **E**valuation: How do we assess quality?
- **R**esearch type: Qualitative, quantitative, mixed?

**Example:**
```markdown
## Research Question

**Primary Question:** What interventions effectively reduce burnout among early childhood educators, and what is the quality of evidence supporting each intervention type?

**PICO Breakdown:**
- Population: Early childhood educators (Pre-K through Grade 2)
- Intervention: Burnout reduction interventions (workload, wellness, compensation, organizational)
- Comparison: No intervention or alternative intervention types
- Outcome: Burnout measures (MBI, CBI), turnover rates, job satisfaction

**Secondary Questions:**
1. What is the current prevalence of burnout in ECE settings?
2. How do intervention effectiveness rates vary by setting type (public vs. private, center vs. home-based)?
3. What systemic/policy factors contribute to or mitigate burnout?
```

### Step 0.2: Define Inclusion/Exclusion Criteria

Specify what sources will and will not be included:

```markdown
## Inclusion Criteria

### Source Types
- Peer-reviewed journal articles (2015-present for empirical studies)
- Systematic reviews and meta-analyses (any date)
- Government reports and official statistics
- Policy documents from education agencies
- Large-scale surveys (N > 500)
- Longitudinal studies

### Geographic Scope
- Primary focus: United States, Canada, UK, Australia, EU
- Secondary: OECD countries with comparable ECE systems
- Excluded: Developing nations with fundamentally different ECE structures (unless explicitly comparative)

### Language
- English (primary)
- Translated abstracts acceptable for key studies in other languages

### Methodological Quality
- Include: RCTs, quasi-experimental designs, large observational studies, validated surveys
- Include with caveats: Small-N studies, case studies, qualitative research
- Exclude: Opinion pieces, non-peer-reviewed preprints, anecdotal accounts

## Exclusion Criteria

- Studies focused on K-12 teachers (unless explicitly including ECE)
- Studies published before 2010 (unless seminal/foundational)
- Grey literature without clear methodology
- Studies with undisclosed conflicts of interest
- Studies that cannot be located/verified
```

### Step 0.3: Define Search Strategy

Document the databases and search terms to be used:

```markdown
## Search Strategy

### Databases to Search

**Academic Databases (Manual):**
1. PubMed/MEDLINE - Health and psychology
2. ERIC (Education Resources Information Center) - Education-specific
3. PsycINFO - Psychology research
4. Google Scholar - Broad academic
5. Cochrane Library - Systematic reviews

**AI-Augmented Searches:**
1. Perplexity (sonar-deep-research) - Academic synthesis
2. GPT-Researcher - Industry and technical
3. Gemini Deep Research - Policy and regulatory
4. Claude - Comprehensive synthesis
5. Grok - Recent developments and practitioner perspectives

### Search Terms

**Primary Terms:**
- ("early childhood" OR "preschool" OR "pre-K" OR "kindergarten" OR "childcare" OR "daycare")
- AND ("educator" OR "teacher" OR "provider" OR "caregiver" OR "staff")
- AND ("burnout" OR "exhaustion" OR "stress" OR "wellbeing" OR "turnover" OR "retention")

**Intervention-Specific Terms:**
- ("intervention" OR "program" OR "support" OR "training" OR "professional development")
- ("compensation" OR "wages" OR "salary" OR "benefits")
- ("workload" OR "ratio" OR "class size" OR "administrative burden")
- ("wellness" OR "mental health" OR "self-care" OR "mindfulness")

### Search Execution Log

| Database | Date Searched | Query | Results | Screened | Included |
|----------|---------------|-------|---------|----------|----------|
| PubMed | YYYY-MM-DD | [query] | [n] | [n] | [n] |
| ERIC | YYYY-MM-DD | [query] | [n] | [n] | [n] |
| ... | ... | ... | ... | ... | ... |
```

### Step 0.4: Define Quality Assessment Framework

Specify how source quality will be evaluated:

```markdown
## Quality Assessment Framework

### For Quantitative Studies: Newcastle-Ottawa Scale (Adapted)

**Selection (0-4 stars):**
- ★ Representativeness of the exposed cohort
- ★ Selection of the non-exposed cohort
- ★ Ascertainment of exposure
- ★ Outcome not present at start

**Comparability (0-2 stars):**
- ★ Study controls for most important factor
- ★ Study controls for additional factors

**Outcome (0-3 stars):**
- ★ Assessment of outcome
- ★ Follow-up long enough
- ★ Adequacy of follow-up

**Quality Thresholds:**
- High quality: 7-9 stars
- Moderate quality: 4-6 stars
- Low quality: 0-3 stars

### For Qualitative Studies: CASP Checklist (Adapted)

1. Was there a clear statement of research aims?
2. Is qualitative methodology appropriate?
3. Was the research design appropriate?
4. Was the recruitment strategy appropriate?
5. Was data collected in a way that addressed the research issue?
6. Was the relationship between researcher and participants considered?
7. Have ethical issues been considered?
8. Was data analysis sufficiently rigorous?
9. Is there a clear statement of findings?
10. How valuable is the research?

### For Policy Documents

1. Is the issuing authority credible?
2. Is the methodology for data collection transparent?
3. Are limitations acknowledged?
4. Is there potential political bias?
5. Are sources/citations provided?
```

### Step 0.5: Protocol Registration

Save the protocol and register it:

```markdown
## Protocol Registration

**Protocol ID:** YUDAME-YYYY-MM-DD-[slug]
**Registration Date:** YYYY-MM-DD
**Status:** Registered (pre-research)

**Protocol Location:**
- Episode: podcast/episodes/YYYY-MM-DD-slug/research/p0-protocol.md
- Archive: docs/protocols/YYYY-MM-DD-slug-protocol.md

**Amendments:**
Any changes to the protocol after research begins must be documented here with rationale.

| Date | Section Changed | Original | Amended To | Rationale |
|------|-----------------|----------|------------|-----------|
```

### Step 0.6: Conflict of Interest Declaration

```markdown
## Conflict of Interest Declaration

**Research Team:**
- Primary researcher: [Name] - No conflicts to declare
- [Additional team members if applicable]

**Funding:**
- This research is self-funded / funded by [source]
- Funders have no editorial control over findings

**Topic-Specific Conflicts:**
- [Disclose any personal/professional connections to the topic]
- [Disclose any financial interests in outcomes]
```

### Protocol Template File

Create `research/p0-protocol.md` using this structure.

**Phase 0 Exit Criteria:**
- [ ] Research question defined using PICO/SPIDER framework
- [ ] Inclusion/exclusion criteria documented
- [ ] Search strategy with databases and terms specified
- [ ] Quality assessment framework selected
- [ ] Protocol registered with unique ID
- [ ] Conflicts of interest declared
- [ ] Protocol saved to both episode directory and docs/protocols/

---

## Phase 2: Academic Foundation (Enhanced)

> **Status (2026-02-05):** ✅ IN PRODUCTION - The AI-augmented research (Step 2.3) is fully implemented. Manual database searches (Steps 2.1, 2.2, 2.4, 2.5) are 🔶 OPTIONAL for when AI-mediated summaries miss key academic sources.

**Purpose:** Build comprehensive academic foundation through systematic database searches augmented by AI tools.

**Time Required:** 2-4 hours (mix of human and automated) | Current production: 30-120 seconds (API) + manual tool time

### Step 2.1: Manual Database Searches (Human) - 🔶 OPTIONAL

Perform searches in academic databases per the protocol:

**PubMed Search:**
```
1. Go to https://pubmed.ncbi.nlm.nih.gov/
2. Enter search query from protocol
3. Apply filters: Publication date, Article type, Species (humans)
4. Export results to CSV/RIS
5. Save to research/databases/pubmed_results_YYYY-MM-DD.csv
```

**ERIC Search:**
```
1. Go to https://eric.ed.gov/
2. Enter search query
3. Apply filters: Publication date, Publication type, Education level
4. Export results
5. Save to research/databases/eric_results_YYYY-MM-DD.csv
```

**Google Scholar Search:**
```
1. Go to https://scholar.google.com/
2. Enter search query
3. Use date range filter
4. For top 50 results, export citations
5. Save to research/databases/scholar_results_YYYY-MM-DD.csv
```

### Step 2.2: Abstract Screening (Human)

Screen all database results against inclusion/exclusion criteria:

```markdown
## Abstract Screening Log

**Screener:** [Name]
**Date:** YYYY-MM-DD

| Source | Title | Authors | Year | Decision | Reason |
|--------|-------|---------|------|----------|--------|
| PubMed | [Title] | [Authors] | 2023 | INCLUDE | Meets all criteria |
| PubMed | [Title] | [Authors] | 2021 | EXCLUDE | Wrong population (K-12) |
| ERIC | [Title] | [Authors] | 2022 | INCLUDE | RCT of intervention |
| ... | ... | ... | ... | ... | ... |

**Summary:**
- Total screened: [n]
- Included: [n]
- Excluded: [n]
- Unclear (full-text needed): [n]
```

### Step 2.3: AI-Augmented Academic Research

Run Perplexity with enhanced protocol-aligned prompt:

```
Research [TOPIC] following this systematic methodology:

**Scope:** [Paste inclusion criteria from protocol]

**Research methodology:**
- Prioritize systematic reviews and meta-analyses
- For individual studies, note: sample size (N), study design, effect sizes, confidence intervals
- Distinguish between correlation and causation explicitly
- Report heterogeneity in meta-analyses (I², Q-statistic if available)
- Note publication bias concerns where relevant
- Include null findings and failed interventions
- Cite specific studies with full author names and years
- Provide DOIs or URLs for all citations

**Quality indicators to note:**
- Study design (RCT, quasi-experimental, observational, case study)
- Sample characteristics and representativeness
- Validated measurement instruments used
- Funding sources and potential conflicts
- Replication status (has this been replicated?)

**Required output format:**
For each major finding, provide:
1. The claim
2. The source (Author, Year, Journal)
3. Study design and N
4. Effect size/key statistic
5. Confidence level (well-established, moderate evidence, preliminary)

Output: Comprehensive research report with extensive citations, methodological details, and quality assessments.
```

### Step 2.4: Full-Text Retrieval (Human)

For all included studies from screening:

```markdown
## Full-Text Retrieval Log

| Citation | Retrieved | Location | Method | Notes |
|----------|-----------|----------|--------|-------|
| Smith et al., 2023 | ✅ | research/documents/smith_2023.pdf | Open access | |
| Jones et al., 2022 | ✅ | research/documents/jones_2022.pdf | Sci-Hub | Published version confirmed |
| Brown et al., 2021 | ❌ | - | Paywalled | Request via ResearchGate |
| ... | ... | ... | ... | ... |

**Retrieval Methods:**
1. Open access journals
2. Institutional access (if available)
3. Author ResearchGate/Academia.edu profiles
4. Preprint servers (arXiv, SSRN, EdArXiv)
5. Sci-Hub (for verification only, cite published version)
6. Interlibrary loan request
7. Direct author contact
```

### Step 2.5: Quality Assessment of Included Studies (Human)

Apply quality assessment framework to all included studies:

```markdown
## Quality Assessment Results

### Quantitative Studies (Newcastle-Ottawa Scale)

| Study | Selection (0-4) | Comparability (0-2) | Outcome (0-3) | Total | Quality |
|-------|-----------------|---------------------|---------------|-------|---------|
| Smith et al., 2023 | ★★★★ | ★★ | ★★★ | 9/9 | High |
| Jones et al., 2022 | ★★★ | ★ | ★★ | 6/9 | Moderate |
| Brown et al., 2021 | ★★ | ★ | ★ | 4/9 | Moderate |
| ... | ... | ... | ... | ... | ... |

### Qualitative Studies (CASP)

| Study | CASP Score (0-10) | Key Strengths | Key Limitations |
|-------|-------------------|---------------|-----------------|
| Taylor et al., 2023 | 8/10 | Rich data, clear methodology | Small sample, single site |
| ... | ... | ... | ... |

### Quality Summary

- High quality studies: [n] ([%])
- Moderate quality studies: [n] ([%])
- Low quality studies: [n] ([%])

**Implication:** [How does study quality affect confidence in findings?]
```

**Phase 2 Exit Criteria:**
- [ ] All protocol-specified databases searched
- [ ] Abstract screening complete with log
- [ ] Perplexity academic research complete
- [ ] Full texts retrieved for all included studies
- [ ] Quality assessment complete for all studies
- [ ] PRISMA-style flow diagram created
- [ ] All PDFs archived in research/documents/

---

## Phase 2.5: Primary Source Collection (NEW)

> **Status (2026-02-05):** 🔶 OPTIONAL - Use for regulatory/legal topics requiring original government documents, legislation, or court filings. Not required for standard podcast production.

**Purpose:** Obtain and archive original documents rather than relying solely on AI summaries.

**Time Required:** 1-3 hours (human)

### Step 2.5.1: Identify Primary Sources Needed

Based on Phase 2 findings, identify original documents required:

```markdown
## Primary Source Requirements

### Government/Regulatory Documents
| Document | Issuing Agency | Date | Status | Priority |
|----------|----------------|------|--------|----------|
| [Policy name] | [Agency] | YYYY | Needed | High |
| [Regulation] | [Agency] | YYYY | Needed | High |
| ... | ... | ... | ... | ... |

### Official Statistics
| Dataset | Source | Date Range | Status | Priority |
|---------|--------|------------|--------|----------|
| [Dataset name] | [Agency] | YYYY-YYYY | Needed | High |
| ... | ... | ... | ... | ... |

### Legal/Court Documents
| Case/Filing | Court | Date | Status | Priority |
|-------------|-------|------|--------|----------|
| [Case name] | [Court] | YYYY | Needed | Medium |
| ... | ... | ... | ... | ... |

### Corporate/Industry Documents
| Document | Organization | Date | Status | Priority |
|----------|--------------|------|--------|----------|
| [Report name] | [Org] | YYYY | Needed | Medium |
| ... | ... | ... | ... | ... |
```

### Step 2.5.2: Retrieve Primary Sources (Human)

**Government Sources:**
```
1. Check official agency websites (e.g., ed.gov, hhs.gov)
2. Use USA.gov for federal documents
3. Check state-level education agency sites
4. Use Government Publishing Office (govinfo.gov)
5. File FOIA request if document unavailable
```

**Official Statistics:**
```
1. Bureau of Labor Statistics (bls.gov)
2. Census Bureau (census.gov)
3. National Center for Education Statistics (nces.ed.gov)
4. State-level data portals
```

**Legal Documents:**
```
1. PACER for federal court filings
2. State court websites
3. Google Scholar (case law)
4. Justia, CourtListener
```

**Historical Documents:**
```
1. Archive.org (Wayback Machine for web sources)
2. National Archives (archives.gov)
3. State historical societies
4. University special collections
```

### Step 2.5.3: Archive with Provenance

For each primary source:

```markdown
## Primary Source Archive

### Document: [Document Name]

**Provenance:**
- Source URL: [Original URL]
- Retrieved: YYYY-MM-DD HH:MM
- Retrieval method: [Direct download / FOIA / Archive.org]
- Archive.org snapshot: [Wayback Machine URL if available]

**Verification:**
- Document authenticity confirmed: ✅
- Official source verified: ✅
- File hash (SHA-256): [hash]

**Local archive:**
- Path: research/documents/primary/[filename]
- Format: [PDF/HTML/CSV]
- Size: [bytes]

**Citation:**
[Full citation in appropriate format]
```

### Step 2.5.4: Create Source Inventory

```markdown
## Primary Source Inventory

| ID | Document | Type | Date | Provenance | Verified | Location |
|----|----------|------|------|------------|----------|----------|
| PS-001 | [Name] | Government | YYYY | [URL] | ✅ | research/documents/primary/ps-001.pdf |
| PS-002 | [Name] | Statistics | YYYY | [URL] | ✅ | research/documents/primary/ps-002.csv |
| ... | ... | ... | ... | ... | ... | ... |

**Total primary sources archived:** [n]
**Verification rate:** [%] verified
```

**Phase 2.5 Exit Criteria:**
- [ ] All critical primary sources identified
- [ ] Documents retrieved from authoritative sources
- [ ] Archive.org snapshots captured for web sources
- [ ] Provenance documented for each source
- [ ] All documents archived locally with consistent naming
- [ ] Source inventory complete

---

## Phase 4.5: Expert Consultation (NEW)

> **Status (2026-02-05):** 🔶 OPTIONAL - HIGH VALUE for contentious topics or when significant research gaps are identified. Templates below ready for use. Consider for flagship episodes or topics with public health/safety implications.

**Purpose:** Obtain direct expert input to validate findings, identify blind spots, and capture practitioner knowledge not available in published sources.

**Time Required:** 1-2 weeks (calendar time for responses)

### Step 4.5.1: Expert Identification

Identify 5-10 experts across different perspectives:

```markdown
## Expert Panel

### Academic Researchers
| Name | Affiliation | Expertise | Contact | Priority |
|------|-------------|-----------|---------|----------|
| Dr. [Name] | [University] | [Specialty] | [email] | High |
| ... | ... | ... | ... | ... |

### Practitioners
| Name | Organization | Role | Contact | Priority |
|------|--------------|------|---------|----------|
| [Name] | [Organization] | [Role] | [email] | High |
| ... | ... | ... | ... | ... |

### Policy Experts
| Name | Organization | Focus | Contact | Priority |
|------|--------------|-------|---------|----------|
| [Name] | [Think tank/Agency] | [Focus] | [email] | Medium |
| ... | ... | ... | ... | ... |

### Industry Representatives
| Name | Organization | Role | Contact | Priority |
|------|--------------|------|---------|----------|
| [Name] | [Company/Association] | [Role] | [email] | Medium |
| ... | ... | ... | ... | ... |

**Selection Criteria:**
- Diverse perspectives (academic, practitioner, policy, industry)
- Geographic diversity where relevant
- Mix of established and emerging voices
- Avoidance of single ideological perspective
```

### Step 4.5.2: Consultation Protocol

**Email Template:**

```
Subject: Research Consultation Request - [Topic] for Yudame Research Podcast

Dear Dr./Mr./Ms. [Name],

I am conducting research on [topic] for the Yudame Research podcast, which produces evidence-based educational content. Your expertise in [specific area] would be invaluable.

I am seeking a brief consultation (15-20 minutes via email, phone, or video) to:
1. Validate key findings from our systematic literature review
2. Identify potential blind spots in our research
3. Understand practitioner perspectives not captured in published literature
4. Discuss areas of ongoing debate or uncertainty

Our research protocol and preliminary findings are attached for your review.

**Consultation Topics:**
1. [Specific question 1]
2. [Specific question 2]
3. [Specific question 3]

Your input would be acknowledged in our published report. Please let me know if you would be willing to participate and your preferred format.

Best regards,
[Name]
Yudame Research
research.yuda.me
```

### Step 4.5.3: Interview Protocol (If Live Consultation)

```markdown
## Semi-Structured Interview Guide

**Introduction (2 min):**
- Thank participant
- Explain purpose and how input will be used
- Confirm consent for attribution
- Note if they prefer to remain anonymous

**Validation Questions (5 min):**
1. We found [key finding]. Does this align with your experience/research?
2. Are there important nuances or caveats we should add?
3. Is there recent work we may have missed?

**Gap Identification (5 min):**
1. What aspects of [topic] are under-researched?
2. What do you wish more people understood about this issue?
3. What questions should we be asking that we haven't?

**Practitioner Perspective (5 min):**
1. How does the research translate (or fail to translate) to practice?
2. What implementation challenges exist?
3. What works in practice that hasn't been formally studied?

**Closing (3 min):**
1. Is there anyone else you'd recommend we speak with?
2. Any resources or documents you'd recommend?
3. May we follow up with clarifying questions?
```

### Step 4.5.4: Expert Input Documentation

```markdown
## Expert Consultation Log

### Consultation: Dr. [Name]
**Date:** YYYY-MM-DD
**Format:** [Email/Phone/Video]
**Duration:** [minutes]

**Key Insights:**
1. [Insight 1]
2. [Insight 2]
3. [Insight 3]

**Validation of Findings:**
- [Finding 1]: Confirmed / Contested / Nuanced
- [Finding 2]: Confirmed / Contested / Nuanced

**New Sources Recommended:**
- [Source 1]
- [Source 2]

**Suggested Contacts:**
- [Name, affiliation]

**Quotes for Attribution:**
> "[Direct quote]" - Dr. [Name], [Title], [Affiliation]

**Confidential Notes (not for publication):**
[Any off-the-record context]

---

### Summary Across All Consultations

| Expert | Perspective | Key Contribution | Agrees with Findings | New Insights |
|--------|-------------|------------------|---------------------|--------------|
| Dr. [Name] | Academic | [Summary] | 4/5 | [Summary] |
| [Name] | Practitioner | [Summary] | 5/5 | [Summary] |
| ... | ... | ... | ... | ... |

**Consensus Points:**
- [Point where all/most experts agree]

**Points of Disagreement:**
- [Point where experts disagree, with positions]

**Novel Insights Not in Literature:**
- [Insight 1]
- [Insight 2]
```

**Phase 4.5 Exit Criteria:**
- [ ] 3-5+ experts consulted across different perspectives
- [ ] All consultations documented with quotes
- [ ] Key findings validated or contested by experts
- [ ] New sources/leads identified
- [ ] Points of expert disagreement documented
- [ ] Attribution permissions confirmed

---

## Phase 5: Cross-Validation & Verification (Enhanced)

> **Status (2026-02-05):** ✅ IN PRODUCTION - Cross-validation matrix and multi-source verification are implemented in the current workflow. Human spot-check (Step 5.3) and formal bias assessment (Step 5.4) are 🔶 OPTIONAL for high-stakes episodes.

**Purpose:** Rigorous verification of all claims through multiple methods.

**Time Required:** 2-4 hours | Current production: ~30-60 minutes (automated cross-validation)

### Step 5.1: Claim Extraction

Extract all factual claims that will appear in the final report:

```markdown
## Claim Registry

| ID | Claim | Category | Confidence | Sources | Verified |
|----|-------|----------|------------|---------|----------|
| C-001 | "53% of ECE teachers report burnout" | Statistic | High | Smith 2023, Jones 2022 | Pending |
| C-002 | "Workload reduction most effective" | Finding | Medium | Meta-analysis (Lee 2023) | Pending |
| ... | ... | ... | ... | ... | ... |

**Claim Categories:**
- Statistic: Specific numbers, percentages, rates
- Finding: Research conclusions
- Causal: Claims about cause-effect relationships
- Comparative: Claims comparing groups/interventions
- Trend: Claims about changes over time
- Policy: Claims about regulations/policies
```

### Step 5.2: Multi-Source Verification Matrix (Enhanced)

```markdown
## Verification Matrix

### Statistical Claims

| Claim ID | Claim | Perplexity | Grok | GPT-R | Gemini | Primary Source | Expert | Status |
|----------|-------|------------|------|-------|--------|----------------|--------|--------|
| C-001 | 53% burnout | ✅ 53% | ✅ 53% | ✅ 53% | ✅ 53% | ✅ Smith 2023 p.12 | ✅ Dr. X confirms | VERIFIED |
| C-002 | 45% turnover | ✅ 45% | ⚠️ 42% | ✅ 45% | ✅ 45% | ✅ BLS data | - | MINOR VARIANCE |
| C-003 | 72% stress | ✅ 72% | ❌ Not found | ✅ 72% | ❌ Not found | ⚠️ Cannot locate | - | NEEDS REVIEW |

**Verification Status:**
- ✅ VERIFIED: 3+ independent sources agree, primary source confirmed
- ⚠️ MINOR VARIANCE: Sources agree within 10%, explainable difference
- ⚠️ NEEDS REVIEW: Fewer than 3 sources or cannot verify primary
- ❌ UNVERIFIED: Cannot confirm from primary sources
- ❌ CONTESTED: Sources actively disagree

### Causal Claims

| Claim ID | Claim | Evidence Type | Confounders Addressed | Replication | Status |
|----------|-------|---------------|----------------------|-------------|--------|
| C-010 | "X causes Y" | RCT | ✅ Randomization | ✅ 3 studies | VERIFIED CAUSAL |
| C-011 | "A leads to B" | Observational | ⚠️ Some controls | ❌ Single study | CORRELATION ONLY |

### Policy Claims

| Claim ID | Claim | Official Source | Current Status | Last Verified | Status |
|----------|-------|-----------------|----------------|---------------|--------|
| C-020 | "Policy X enacted" | ✅ Gov source | Active | YYYY-MM-DD | VERIFIED |
```

### Step 5.3: Human Spot-Check Protocol (Human)

**For every report, manually verify 5-10 critical claims:**

```markdown
## Human Verification Log

**Verifier:** [Name]
**Date:** YYYY-MM-DD

### Claim: C-001 "53% of ECE teachers report burnout"

**Original source cited:** Smith et al., 2023, Journal of Educational Psychology

**Verification steps:**
1. Located original paper: ✅ research/documents/smith_2023.pdf
2. Found claim in text: ✅ Page 12, paragraph 2
3. Exact quote: "53.2% of participants (N=1,795) met criteria for burnout on the MBI"
4. Context matches: ✅ Preschool teachers in urban China
5. Methodology sound: ✅ Validated instrument (MBI), large sample

**Verification result:** ✅ VERIFIED
**Notes:** Should specify this is China-specific data; may not generalize to US/Europe

---

### Claim: C-007 "Compensation increases reduce turnover by 30%"

**Original source cited:** Brown et al., 2022, Early Childhood Research Quarterly

**Verification steps:**
1. Located original paper: ✅ research/documents/brown_2022.pdf
2. Found claim in text: ⚠️ Found related claim, Page 8
3. Exact quote: "A 15% wage increase was associated with 28% lower turnover intent (p<.05)"
4. Context matches: ⚠️ "Turnover intent" not actual turnover
5. Methodology sound: ⚠️ Observational study, limited controls

**Verification result:** ⚠️ NEEDS CORRECTION
**Notes:** Original says "turnover intent" not actual turnover, and effect size is 28% not 30%. Must correct in report.
```

### Step 5.4: Bias Assessment

```markdown
## Bias Assessment

### Publication Bias

**Assessment Method:** Visual inspection of effect sizes + consideration of grey literature

**Findings:**
- Are there studies with null findings? [Yes/No]
- Are there unpublished studies or grey literature? [Yes/No]
- Do effect sizes seem unusually consistent? [Yes/No]
- Are there registered studies that weren't published? [Unknown/Check OSF]

**Publication bias risk:** [Low/Medium/High]

### Funding Bias

| Study | Funder | Potential Conflict | Risk |
|-------|--------|-------------------|------|
| Smith 2023 | NIH | None apparent | Low |
| Industry Report 2022 | [Industry group] | Vested interest | High |
| ... | ... | ... | ... |

### Geographic/Demographic Bias

**Populations studied:**
- [ ] US samples
- [ ] European samples
- [ ] Other OECD
- [ ] Non-OECD

**Populations underrepresented:**
- [Population 1]
- [Population 2]

### AI Tool Bias

| Tool | Known Biases | Mitigation |
|------|--------------|------------|
| Perplexity | Favors recent, SEO-optimized content | Cross-reference with database searches |
| GPT-Researcher | OpenAI training data biases | Use multiple tools |
| Gemini | Google search index biases | Include primary sources |
| Grok | X/Twitter community biases | Validate with other sources |
| Claude | Training data cutoff | Supplement with recent sources |

### Overall Bias Assessment

**Key bias concerns:**
1. [Concern 1]
2. [Concern 2]

**Mitigation steps taken:**
1. [Step 1]
2. [Step 2]

**Remaining limitations to acknowledge:**
1. [Limitation 1]
2. [Limitation 2]
```

**Phase 5 Exit Criteria:**
- [ ] All claims extracted and categorized
- [ ] Multi-source verification matrix complete
- [ ] 5-10 critical claims manually verified against primary sources
- [ ] Any discrepancies corrected
- [ ] Publication bias assessed
- [ ] Funding bias documented
- [ ] AI tool biases acknowledged
- [ ] Remaining limitations documented for disclosure

---

## Phase 5.5: External Peer Review (NEW)

> **Status (2026-02-05):** 🔶 OPTIONAL - HIGH VALUE for flagship episodes or topics with public health/safety/policy implications. Templates below ready for use. Consider when making claims that could significantly impact listener behavior or decisions.

**Purpose:** Independent expert review of research findings before synthesis.

**Time Required:** 1-2 weeks (calendar time)

### Step 5.5.1: Prepare Review Package

Create a review package for external reviewers:

```markdown
## Review Package Contents

1. **Research Protocol** (p0-protocol.md)
   - Research questions
   - Inclusion/exclusion criteria
   - Search strategy
   - Quality assessment methods

2. **Search Results Summary**
   - Databases searched
   - Number of sources screened/included
   - PRISMA flow diagram

3. **Quality Assessment Summary**
   - Studies by quality level
   - Key limitations

4. **Key Findings Summary**
   - 10-15 key findings
   - Evidence supporting each
   - Confidence levels

5. **Verification Matrix**
   - Multi-source verification results
   - Unresolved discrepancies

6. **Expert Consultation Summary**
   - Key insights from experts
   - Points of agreement/disagreement

7. **Bias Assessment**
   - Identified biases
   - Mitigation steps

8. **Specific Review Requests**
   - "Please evaluate whether Finding X is adequately supported"
   - "Please identify any sources we may have missed"
   - "Please flag any methodological concerns"
```

### Step 5.5.2: Reviewer Selection

Select 1-2 external reviewers:

```markdown
## External Reviewer Selection

**Criteria:**
- Subject matter expertise in [topic]
- No conflict of interest with research team or funders
- Track record of rigorous research
- Available within timeline

**Selected Reviewers:**

| Reviewer | Affiliation | Expertise | COI Check | Status |
|----------|-------------|-----------|-----------|--------|
| Dr. [Name] | [University] | [Specialty] | ✅ None | Invited |
| [Name] | [Organization] | [Specialty] | ✅ None | Confirmed |
```

### Step 5.5.3: Review Process

**Reviewer Instructions:**

```markdown
## External Review Instructions

Thank you for agreeing to review this research package.

**Review Focus:**
1. **Methodological Rigor:** Are the methods appropriate for the research questions?
2. **Source Quality:** Are the sources authoritative and appropriately evaluated?
3. **Evidence Strength:** Are findings adequately supported by evidence?
4. **Bias & Limitations:** Are biases properly identified and acknowledged?
5. **Completeness:** Are there important sources, perspectives, or findings missing?

**Please Provide:**
1. Overall assessment (Acceptable / Minor Revisions / Major Revisions / Reject)
2. Specific comments on each key finding
3. List of any missing sources or perspectives
4. Methodological concerns
5. Suggestions for improvement

**Timeline:** Please return review within [X] days.
**Format:** Use the attached review template.

**Confidentiality:** This research is pre-publication. Please do not share.
```

### Step 5.5.4: Review Documentation

```markdown
## External Review Results

### Reviewer 1: Dr. [Name]

**Date Received:** YYYY-MM-DD
**Overall Assessment:** [Acceptable with Minor Revisions]

**Key Comments:**
1. [Comment 1]
   - **Our Response:** [How we addressed this]
2. [Comment 2]
   - **Our Response:** [How we addressed this]

**Missing Sources Identified:**
- [Source 1] - Added to research
- [Source 2] - Noted but excluded because [reason]

**Methodological Concerns:**
- [Concern 1]
   - **Resolution:** [How resolved]

---

### Reviewer 2: [Name]

[Same structure]

---

### Review Summary

**Changes Made Based on Review:**
1. [Change 1]
2. [Change 2]
3. [Change 3]

**Reviewer Concerns Not Addressed:**
1. [Concern] - Reason: [Why not addressed]

**Final Status:** Ready for Synthesis
```

**Phase 5.5 Exit Criteria:**
- [ ] Review package prepared and sent
- [ ] 1-2 external reviewers completed review
- [ ] All reviewer comments addressed or explained
- [ ] Changes documented
- [ ] Research updated based on feedback
- [ ] Reviewers acknowledged (with permission)

---

## Phase 6: Master Research Briefing (Enhanced)

> **Status (2026-02-05):** ✅ IN PRODUCTION - Significantly enhanced via Wave 1 (Tasks B1.1-B1.3, B2.1-B2.2). The production template is `docs/templates/p3-briefing-enhanced.md`. The template below represents maximum rigor; the production template is the pragmatic subset.
>
> **Wave 1 additions now in production:**
> - ✅ Depth Distribution Analysis (B1.1)
> - ✅ Counterpoint Discovery (B1.2)
> - ✅ Practical Implementation Audit (B1.3)
> - ✅ Takeaway Clarity Requirements (B2.1)
> - ✅ Story Bank (B2.2)

**Purpose:** Create the definitive research compilation for synthesis, incorporating all verification and review findings.

### Enhanced Briefing Structure

```markdown
# Master Research Briefing: [Episode Title]

**Protocol ID:** YUDAME-YYYY-MM-DD-[slug]
**Briefing Date:** YYYY-MM-DD
**Research Status:** Externally Reviewed

---

## METHODOLOGY SUMMARY

### Research Protocol
- Research question: [PICO/SPIDER format]
- Databases searched: [List]
- Date range: [Range]
- Inclusion criteria: [Summary]
- Exclusion criteria: [Summary]

### Source Statistics
- Total sources screened: [n]
- Sources included: [n]
- Primary sources archived: [n]
- Experts consulted: [n]
- External reviewers: [n]

### Quality Distribution
- High quality studies: [n] ([%])
- Moderate quality: [n] ([%])
- Low quality: [n] ([%])

---

## VERIFIED KEY FINDINGS

### Finding 1: [Title]

**Claim:** [One sentence summary]

**Evidence Strength:** [Strong / Moderate / Preliminary / Limited]

**Verification Status:** ✅ VERIFIED
- Multi-source: 4/5 tools confirm
- Primary source: ✅ Verified (Smith 2023, p.12)
- Expert validation: ✅ Confirmed by Dr. [Name]
- Human spot-check: ✅ YYYY-MM-DD

**Supporting Evidence:**
| Source | Finding | Study Design | N | Effect Size | Quality |
|--------|---------|--------------|---|-------------|---------|
| Smith et al., 2023 | 53.2% burnout | Cross-sectional | 1,795 | - | High |
| Meta-analysis (Lee, 2023) | 48-58% range | Meta-analysis | 12 studies | - | High |

**Contradictions/Nuances:**
- European studies show lower rates (42%) - possible cultural factors
- Definition of "burnout" varies across studies

**Confidence:** HIGH - Multiple high-quality sources, externally validated

---

### Finding 2: [Title]

**Claim:** [One sentence summary]

**Evidence Strength:** [Strong / Moderate / Preliminary / Limited]

**Verification Status:** ⚠️ VERIFIED WITH CAVEATS
- Multi-source: 3/5 tools confirm
- Primary source: ✅ Verified
- Expert validation: ⚠️ One expert contested methodology
- Human spot-check: ✅ YYYY-MM-DD

[Continue structure for each finding]

---

## RESEARCH GAPS & UNCERTAINTIES

### Well-Established (High Confidence)
- [Finding 1]
- [Finding 2]

### Moderate Evidence (Use with Caveats)
- [Finding 3] - Caveat: [Limitation]
- [Finding 4] - Caveat: [Limitation]

### Preliminary/Limited Evidence (Acknowledge Uncertainty)
- [Finding 5] - Only 1-2 studies, small samples
- [Finding 6] - Methodological concerns noted

### Unknown/Unstudied (Gaps to Acknowledge)
- [Topic 1] - No research found
- [Topic 2] - Research needed

---

## BIAS & LIMITATIONS DISCLOSURE

### Known Biases
1. **Publication bias:** [Assessment]
2. **Funding bias:** [Studies with potential conflicts]
3. **Geographic bias:** [Underrepresented populations]
4. **AI tool bias:** [Tool-specific limitations]

### Study Limitations
1. [Limitation 1]
2. [Limitation 2]

### Our Methodological Limitations
1. [What we couldn't do]
2. [What we had to assume]

---

## SOURCE INVENTORY

### Tier 1: Meta-analyses, Systematic Reviews, Official Statistics
| Citation | Key Contribution | Quality Score | Verified | Location |
|----------|------------------|---------------|----------|----------|
| [Full citation] | [Contribution] | 9/9 | ✅ | research/documents/[file] |

### Tier 2: RCTs, Large Studies, Government Reports
[Same structure]

### Tier 3: Observational Studies, Case Studies, Industry Reports
[Same structure]

### Expert Sources
| Expert | Affiliation | Contribution | Attribution Permission |
|--------|-------------|--------------|------------------------|
| Dr. [Name] | [Affiliation] | [Key insight] | ✅ Granted |

---

## EXTERNAL REVIEW SUMMARY

**Reviewers:** Dr. [Name 1], [Name 2]
**Overall Assessment:** Acceptable with Minor Revisions
**Key Changes Made:** [Summary of changes from review]

---

## NOTES FOR SYNTHESIS AGENT

### Strongest Evidence For:
- [Topic 1] - Multiple high-quality sources, expert consensus
- [Topic 2] - RCT evidence, replicated

### Present with Caution:
- [Topic 3] - Moderate evidence, some methodological concerns
- [Topic 4] - Expert disagreement exists

### Acknowledge Uncertainty:
- [Topic 5] - Preliminary research only
- [Topic 6] - Known research gap

### Contradictions to Present Fairly:
- [Topic 7] - Source A says X, Source B says Y, possible reason for difference

### Do NOT Claim:
- [Topic 8] - Insufficient evidence
- [Topic 9] - Correlation only, not causation
```

**Phase 6 Exit Criteria:**
- [ ] All verified findings documented with evidence strength
- [ ] Verification status explicit for each claim
- [ ] Research gaps clearly identified
- [ ] Bias and limitations disclosed
- [ ] All sources inventoried with quality scores
- [ ] External review summary included
- [ ] Clear guidance for synthesis agent

---

## Full Audit Trail

### Research Log Structure

Maintain `research/audit-log.md` throughout the process:

```markdown
# Research Audit Log

**Protocol ID:** YUDAME-YYYY-MM-DD-[slug]
**Episode:** [Title]

---

## Chronological Research Log

### YYYY-MM-DD HH:MM - Phase 0: Protocol Development
- Created research protocol
- Defined research question using PICO framework
- Established inclusion/exclusion criteria
- Registered protocol as YUDAME-YYYY-MM-DD-slug

### YYYY-MM-DD HH:MM - Phase 2: Database Searches
- PubMed search: [n] results
- ERIC search: [n] results
- Google Scholar search: [n] results
- Total unique sources: [n]

### YYYY-MM-DD HH:MM - Phase 2: Abstract Screening
- Screened [n] abstracts
- Included: [n]
- Excluded: [n]
- Full text retrieval needed: [n]

[Continue for each step...]

---

## Decision Log

| Date | Decision | Rationale | Made By |
|------|----------|-----------|---------|
| YYYY-MM-DD | Excluded [study] | Wrong population | [Name] |
| YYYY-MM-DD | Changed search terms to include X | Missing key studies | [Name] |
| YYYY-MM-DD | Added Tier 3 source despite limitations | Only source on [topic] | [Name] |

---

## Amendments to Protocol

| Date | Section | Original | Changed To | Rationale |
|------|---------|----------|------------|-----------|
| YYYY-MM-DD | Inclusion criteria | 2015-present | 2010-present | Foundational study from 2012 identified |

---

## Time Tracking

| Phase | Start | End | Hours | Notes |
|-------|-------|-----|-------|-------|
| Phase 0 | YYYY-MM-DD | YYYY-MM-DD | 1.5 | Protocol development |
| Phase 2 | YYYY-MM-DD | YYYY-MM-DD | 4.0 | Database searches + screening |
| Phase 2.5 | YYYY-MM-DD | YYYY-MM-DD | 2.0 | Primary source retrieval |
| ... | ... | ... | ... | ... |
| **TOTAL** | | | **[X]** | |
```

---

## Quality Checklist: Pre-Synthesis

Before proceeding to synthesis (Phase 7), verify:

```markdown
## Pre-Synthesis Quality Checklist

### Protocol & Methodology
- [ ] Research protocol registered with unique ID
- [ ] Research question follows PICO/SPIDER framework
- [ ] Inclusion/exclusion criteria documented
- [ ] Search strategy documented and executed

### Source Quality
- [ ] Academic databases searched (PubMed, ERIC, etc.)
- [ ] AI tools used with protocol-aligned prompts
- [ ] All included studies quality-assessed
- [ ] Primary sources retrieved and archived
- [ ] Source inventory complete with quality scores

### Verification
- [ ] All claims extracted to claim registry
- [ ] Multi-source verification matrix complete
- [ ] 5-10 critical claims manually verified
- [ ] Discrepancies resolved or noted
- [ ] Bias assessment complete

### Expert Input
- [ ] 3+ experts consulted
- [ ] Expert validation documented
- [ ] Points of disagreement noted

### External Review
- [ ] Review package prepared
- [ ] 1-2 external reviewers completed review
- [ ] All feedback addressed or explained

### Documentation
- [ ] Master research briefing complete
- [ ] Audit log up to date
- [ ] All sources archived locally

### Transparency
- [ ] Limitations acknowledged
- [ ] Biases disclosed
- [ ] Research gaps identified
- [ ] Conflicts of interest declared

**Certification:**
I certify that this research meets gold-standard quality requirements and is ready for synthesis.

Researcher: _________________ Date: _____________
```

---

## Episode Directory Structure (Enhanced)

```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/
│   ├── p0-protocol.md                 # Research protocol (NEW)
│   ├── p1-brief.md                    # Research brief
│   ├── p2-perplexity.md               # Perplexity academic research
│   ├── p2-grok.md                     # Grok real-time research
│   ├── p2-chatgpt.md                  # GPT-Researcher industry research
│   ├── p2-gemini.md                   # Gemini policy research
│   ├── p2-claude.md                   # Claude comprehensive research
│   ├── p3-briefing.md                 # Master research briefing
│   ├── databases/                     # Database search results (NEW)
│   │   ├── pubmed_results_YYYY-MM-DD.csv
│   │   ├── eric_results_YYYY-MM-DD.csv
│   │   └── screening_log.md
│   ├── documents/                     # Full-text PDFs
│   │   ├── primary/                   # Primary sources with provenance (NEW)
│   │   │   ├── ps-001_policy_document.pdf
│   │   │   └── provenance.md
│   │   ├── smith_2023.pdf
│   │   └── jones_2022.pdf
│   ├── quality/                       # Quality assessments (NEW)
│   │   ├── quality_assessment.md
│   │   └── bias_assessment.md
│   ├── verification/                  # Verification documents (NEW)
│   │   ├── claim_registry.md
│   │   ├── verification_matrix.md
│   │   └── human_verification_log.md
│   ├── experts/                       # Expert consultations (NEW)
│   │   ├── consultation_log.md
│   │   └── interview_notes/
│   ├── review/                        # External review (NEW)
│   │   ├── review_package.md
│   │   ├── reviewer_1_comments.md
│   │   └── response_to_reviewers.md
│   └── audit-log.md                   # Complete research audit trail (NEW)
├── logs/
│   ├── prompts.md
│   └── metadata.md
├── tmp/
│   └── *_transcript.json
├── cover.png
├── report.md
├── sources.md
├── YYYY-MM-DD-topic-slug.mp3
└── YYYY-MM-DD-topic-slug_chapters.json
```

---

## Implementation Timeline

### For a Standard Episode

| Day | Phase | Activities | Hours |
|-----|-------|------------|-------|
| 1 | Phase 0 | Protocol development | 1-2 |
| 1-2 | Phase 1 | Setup, initial file creation | 0.5 |
| 2-3 | Phase 2 | Database searches, AI research, screening | 3-5 |
| 3-4 | Phase 2.5 | Primary source collection | 2-3 |
| 4-5 | Phase 3 | Question discovery | 1-2 |
| 5-7 | Phase 4 | Targeted followup research | 2-4 |
| 7-14 | Phase 4.5 | Expert consultation (calendar time) | 2-4 |
| 7-10 | Phase 5 | Cross-validation, verification | 3-5 |
| 10-21 | Phase 5.5 | External peer review (calendar time) | 1-2 |
| 21-22 | Phase 6 | Master briefing | 2-3 |
| 22-23 | Phase 7 | Synthesis | 2-3 |
| 23-24 | Phase 8-12 | Cover art, audio, publishing | 2-4 |

**Total Active Hours:** 20-35 hours
**Total Calendar Time:** 3-4 weeks

---

## Appendices

### Appendix A: PRISMA Flow Diagram Template

```
                    Records identified through
                    database searching
                         (n = _____)
                              │
                              ▼
                    Additional records identified
                    through AI tools
                         (n = _____)
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Records after     │
                    │ duplicates removed  │
                    │     (n = _____)     │
                    └─────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐     ┌─────────────────────┐
                    │  Records screened   │────▶│  Records excluded   │
                    │     (n = _____)     │     │     (n = _____)     │
                    └─────────────────────┘     └─────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐     ┌─────────────────────┐
                    │ Full-text articles  │────▶│ Full-text excluded  │
                    │  assessed for       │     │   with reasons      │
                    │  eligibility        │     │     (n = _____)     │
                    │     (n = _____)     │     └─────────────────────┘
                    └─────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Studies included in │
                    │ qualitative synthesis│
                    │     (n = _____)     │
                    └─────────────────────┘
```

### Appendix B: Newcastle-Ottawa Scale Quick Reference

**Selection (max 4 stars):**
1. Representativeness of exposed cohort (★ truly representative, ☆ somewhat representative)
2. Selection of non-exposed cohort (★ same community, ☆ different source)
3. Ascertainment of exposure (★ secure record, ☆ structured interview)
4. Demonstration outcome not present at start (★ yes, ☆ no)

**Comparability (max 2 stars):**
1. Study controls for most important factor (★)
2. Study controls for additional factor (★)

**Outcome (max 3 stars):**
1. Assessment of outcome (★ independent blind, ☆ record linkage)
2. Follow-up long enough (★ yes, ☆ no)
3. Adequacy of follow-up (★ complete, ☆ low attrition)

### Appendix C: Evidence Strength Classification

| Level | Description | Examples |
|-------|-------------|----------|
| **Strong** | Multiple high-quality studies, consistent findings, expert consensus | Meta-analyses of RCTs, large RCTs with replication |
| **Moderate** | Multiple studies with some limitations, generally consistent | Large observational studies, single RCT, consistent case-control studies |
| **Preliminary** | Limited studies, methodological concerns, or inconsistent findings | Small studies, pilot studies, conflicting results |
| **Limited** | Single study, poor quality, or significant limitations | Case studies, expert opinion, grey literature |
| **Insufficient** | No research found, or evidence too weak to draw conclusions | Absence of evidence |

### Appendix D: External Reviewer Template

```markdown
# External Review: [Episode Title]

**Reviewer:** [Name]
**Date:** YYYY-MM-DD

## Overall Assessment

[ ] Acceptable - Ready for synthesis
[ ] Minor Revisions - Address specific issues
[ ] Major Revisions - Significant concerns require resolution
[ ] Reject - Fundamental methodological flaws

## Methodological Rigor

**Comments:**

## Source Quality

**Comments:**

## Evidence Strength

| Finding | Assessment | Comments |
|---------|------------|----------|
| Finding 1 | [Adequate/Inadequate] | |
| Finding 2 | [Adequate/Inadequate] | |

## Bias & Limitations

**Comments:**

## Missing Sources/Perspectives

1.
2.
3.

## Specific Recommendations

1.
2.
3.

## Confidential Comments (for research team only)

```

---

## Summary

This enhanced workflow transforms podcast research from "good AI-assisted research" to "publication-quality systematic research that becomes podcasts." Key additions:

1. **Pre-registered research protocol** (Phase 0) - 🔶 OPTIONAL for high-stakes
2. **Systematic database searches** with PRISMA reporting - 🔶 OPTIONAL when AI misses sources
3. **Primary source collection** with provenance tracking (Phase 2.5) - 🔶 OPTIONAL for regulatory topics
4. **Formal quality assessment** using established tools - 🔶 OPTIONAL (current tiering suffices)
5. **Expert consultation** with structured protocols (Phase 4.5) - 🔶 OPTIONAL for contentious topics
6. **External peer review** (Phase 5.5) - 🔶 OPTIONAL for flagship episodes
7. **Complete audit trail** for reproducibility - ✅ PARTIAL (logs/ directory)
8. **Bias assessment** at multiple levels - ✅ PARTIAL (AI tool bias acknowledged)

**Wave 1 Pragmatic Subset (now in production):**
1. ✅ **Depth Distribution Analysis** - Ensures balanced coverage across subtopics
2. ✅ **Counterpoint Discovery** - Identifies disagreements for dialogue dynamics
3. ✅ **Practical Implementation Audit** - "How would someone do this?" for each finding
4. ✅ **Takeaway Clarity Requirements** - Explicit 1-3 core takeaways
5. ✅ **Story Bank** - Curated examples with memorability ratings

The result is research that achieves significant quality gains (+16 points, 28 to 44/50 on quality scorecard) while maintaining podcast production timelines (1-3 days vs. 3-4 weeks).

**For maximum rigor:** Use the full 16-phase workflow for academic publications or high-stakes episodes.
**For standard production:** Use the 12-phase workflow with Wave 1 enhancements (see `.claude/skills/new-podcast-episode.md`).
