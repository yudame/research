# High-Stakes Research Protocol (Optional Enhancement)

**Source:** Extracted from `docs/plans/gold-standard-research.md` (2026-02-10)
**Purpose:** Additional research rigor for episodes with health claims, policy analysis, or contentious topics

---

## When to Use This Protocol

Use these optional phases for **high-stakes episodes only**:
- Health/medical claims that could affect listener behavior
- Policy analysis with public implications
- Contentious or politically charged topics
- Flagship episodes representing the podcast brand
- Topics where research gaps are significant

**For standard episodes:** Use the standard 12-phase workflow in `.claude/skills/new-podcast-episode.md` with Wave 1 enhancements.

---

## Phase 0: Research Protocol Development (Optional)

**When:** Topics requiring academic defensibility

**Time:** 30-60 minutes

**Output:** `research/p0-protocol.md`

### Step 0.1: Define Research Question (PICO/SPIDER)

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

### Step 0.2: Define Inclusion/Exclusion Criteria

```markdown
## Inclusion Criteria
- Source types: [e.g., peer-reviewed 2015-present, systematic reviews any date]
- Geographic scope: [e.g., OECD countries]
- Methodological quality: [e.g., RCTs, large observational studies]

## Exclusion Criteria
- [e.g., Studies before 2010, grey literature without methodology]
```

### Step 0.3: Define Search Strategy

```markdown
## Search Strategy

### Academic Databases (Manual)
1. PubMed/MEDLINE
2. ERIC
3. PsycINFO
4. Google Scholar

### Search Terms
- Primary: [keyword clusters]
- Intervention-specific: [additional terms]

### Search Execution Log
| Database | Date | Query | Results | Screened | Included |
|----------|------|-------|---------|----------|----------|
```

### Step 0.4: Conflict of Interest Declaration

```markdown
## Conflict of Interest
- Research team: [Names and disclosures]
- Funding: [Source and editorial independence]
- Topic-specific conflicts: [Any connections to disclose]
```

**Exit Criteria:**
- [ ] Research question follows PICO/SPIDER
- [ ] Inclusion/exclusion criteria documented
- [ ] Search strategy specified
- [ ] Conflicts declared
- [ ] Protocol saved to `research/p0-protocol.md`

---

## Phase 2.5: Primary Source Collection (Optional)

**When:** Regulatory/legal topics requiring original documents

**Time:** 1-3 hours

**Output:** `research/documents/primary/` with provenance

### Types of Primary Sources

| Type | Where to Find |
|------|---------------|
| Government documents | USA.gov, agency websites, govinfo.gov |
| Official statistics | BLS, Census, NCES |
| Legal documents | PACER, Google Scholar (case law), Justia |
| Historical documents | Archive.org, National Archives |

### Archive with Provenance

For each document:

```markdown
## Document: [Name]

**Provenance:**
- Source URL: [URL]
- Retrieved: YYYY-MM-DD HH:MM
- Archive.org snapshot: [Wayback URL if applicable]

**Verification:**
- Document authenticity confirmed: ✅/❌
- File hash (SHA-256): [hash]

**Local archive:** research/documents/primary/[filename]
```

**Exit Criteria:**
- [ ] Critical primary sources identified
- [ ] Documents retrieved from authoritative sources
- [ ] Provenance documented
- [ ] Sources archived locally

---

## Phase 4.5: Expert Consultation (Optional)

**When:** Contentious topics or significant research gaps

**Time:** 1-2 weeks calendar time

**Output:** `research/experts/consultation_log.md`

### Expert Identification

Identify 3-5 experts across perspectives:
- Academic researchers
- Practitioners
- Policy experts
- Industry representatives (where relevant)

### Email Template

```
Subject: Research Consultation Request - [Topic] for Yudame Research Podcast

Dear [Name],

I am researching [topic] for the Yudame Research podcast. Your expertise in [area] would be invaluable.

I seek a brief consultation (15-20 min via email/phone/video) to:
1. Validate key findings from our literature review
2. Identify potential blind spots
3. Understand practitioner perspectives

**Consultation Topics:**
1. [Specific question 1]
2. [Specific question 2]
3. [Specific question 3]

Your input would be acknowledged. Please let me know if you would participate.

Best regards,
[Name], Yudame Research
```

### Consultation Documentation

```markdown
## Expert Consultation: [Name]

**Date:** YYYY-MM-DD
**Format:** Email/Phone/Video

**Key Insights:**
1. [Insight]
2. [Insight]

**Validation of Findings:**
- [Finding 1]: Confirmed / Contested / Nuanced

**New Sources Recommended:**
- [Source]

**Quotes for Attribution:**
> "[Quote]" - [Name], [Title], [Affiliation]
```

**Exit Criteria:**
- [ ] 3+ experts consulted across perspectives
- [ ] Consultations documented
- [ ] Key findings validated or contested
- [ ] Attribution permissions confirmed

---

## Phase 5.5: External Peer Review (Optional)

**When:** Flagship episodes or topics with public health/safety implications

**Time:** 1-2 weeks calendar time

**Output:** `research/review/`

### Review Package Contents

1. Research protocol (p0-protocol.md)
2. Search results summary
3. Quality assessment summary
4. Key findings summary
5. Verification matrix
6. Expert consultation summary (if Phase 4.5 done)
7. Bias assessment
8. Specific review requests

### Reviewer Instructions

```markdown
## External Review Instructions

**Review Focus:**
1. Methodological rigor
2. Source quality
3. Evidence strength
4. Bias & limitations
5. Completeness

**Please Provide:**
1. Overall assessment (Acceptable / Minor Revisions / Major Revisions)
2. Comments on each key finding
3. Missing sources/perspectives
4. Methodological concerns
5. Suggestions

**Timeline:** [X] days
```

### Review Documentation

```markdown
## External Review Results

### Reviewer: [Name]
**Date:** YYYY-MM-DD
**Assessment:** [Acceptable with Minor Revisions]

**Key Comments:**
1. [Comment] - **Response:** [How addressed]

**Missing Sources Identified:**
- [Source] - Added / Excluded because [reason]

**Changes Made:**
1. [Change]
```

**Exit Criteria:**
- [ ] Review package prepared
- [ ] 1-2 reviewers completed review
- [ ] All comments addressed or explained
- [ ] Changes documented

---

## Quality Assessment Tools

### Newcastle-Ottawa Scale (Quantitative Studies)

**Selection (0-4 stars):**
- Representativeness of exposed cohort
- Selection of non-exposed cohort
- Ascertainment of exposure
- Outcome not present at start

**Comparability (0-2 stars):**
- Controls for most important factor
- Controls for additional factors

**Outcome (0-3 stars):**
- Assessment of outcome
- Follow-up long enough
- Adequacy of follow-up

**Quality Thresholds:**
- High: 7-9 stars
- Moderate: 4-6 stars
- Low: 0-3 stars

### Evidence Strength Classification

| Level | Description |
|-------|-------------|
| **Strong** | Multiple high-quality studies, consistent, expert consensus |
| **Moderate** | Multiple studies with some limitations, generally consistent |
| **Preliminary** | Limited studies, methodological concerns, inconsistent |
| **Limited** | Single study, poor quality, significant limitations |
| **Insufficient** | No research found |

---

## When NOT to Use This Protocol

- Standard podcast episodes (use Wave 1 enhancements)
- Topics with clear scientific consensus
- Time-sensitive production schedules
- Topics where research quality is well-established

**Time investment:** Full protocol adds 2-4 weeks to production. Use selectively.

---

*Extracted from gold-standard-research.md, 2026-02-10*
