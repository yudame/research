# Research Pipeline

The research pipeline aggregates information from multiple AI sources, cross-validates findings, and synthesizes them into comprehensive, evidence-based reports.

## Overview

The Yudame Research Podcast uses a multi-source research methodology to ensure accuracy and comprehensiveness. Each episode aggregates research from 5 different AI tools, cross-validates findings, and produces a narrative report suitable for audio consumption.

---

## Research Tools Comparison

| Tool | Speed | Academic | Policy | Technical | Cost | Primary Use |
|------|-------|----------|--------|-----------|------|-------------|
| Perplexity | 30-120s | High | Low | Medium | $$$ | Peer-reviewed papers, meta-analyses |
| Gemini | 3-10min | Low | High | Medium | $$ | Regulatory frameworks, policy analysis |
| GPT-Researcher | 6-20min | Medium | Medium | High | $ | Technical deep-dives, 100+ sources |
| Claude | Variable | High | Medium | High | Variable | Synthesis, nuanced analysis |
| Grok | Variable | Low | Low | Low | Variable | Real-time data, regional context |

---

## Phase-Based Research Process

### Phase 1: Topic Briefing

Create `research/p1-brief.md` with:

- Topic overview and scope
- Core research questions (3-5)
- Special focus areas
- Definitions to clarify
- Important context
- Quality standards

**Quality Standards to Emphasize:**
- Peer-reviewed sources preferred
- Meta-analyses over single studies
- Effect sizes and practical significance
- Population generalizability
- Funding source transparency
- Contradictory findings

### Phase 2: Academic Foundation

**Tool:** Perplexity Deep Research
**Output:** `research/p2-perplexity.md`
**Duration:** 30-120 seconds

Perplexity excels at:
- Finding peer-reviewed papers
- Locating meta-analyses
- Identifying systematic reviews
- Academic citation chains

### Phase 3: Question Discovery

After initial research, identify gaps:
- What questions emerged from Phase 2?
- What areas need deeper exploration?
- What contradictions require resolution?

Update research questions for Phase 4.

### Phase 4: Targeted Research

Run multiple tools in parallel for efficiency.

**Tool A: Gemini Deep Research**
**Output:** `research/p2-gemini.md`
**Duration:** 3-10 minutes

Best for:
- Policy and regulatory analysis
- Strategic frameworks
- Government documents
- Industry standards

**Tool B: GPT-Researcher**
**Output:** `research/p2-chatgpt.md`
**Duration:** 6-20 minutes

Best for:
- Technical specifications
- Implementation details
- Cross-referencing 100+ sources
- Industry reports

**Tool C: Manual Research (Claude/Grok)**
**Output:** `research/p2-manual.md`
**Duration:** Variable

Best for:
- Filling specific gaps
- Real-time information (Grok)
- Nuanced analysis (Claude)
- Regional context

### Phase 5: Cross-Validation

**Output:** `research/cross-validation.md`

Compare findings across all sources:

1. **Agreement Matrix** - Which sources agree on key claims?
2. **Contradiction Analysis** - Where do sources disagree?
3. **Source Quality Assessment** - How reliable is each finding?
4. **Evidence Hierarchy Application** - Meta-analysis > RCT > observational > case study
5. **Gap Identification** - What wasn't covered?

### Phase 6: Master Briefing

**Output:** `research/p3-briefing.md`

Organize validated findings into a structured briefing:

- Executive summary
- Key findings by topic
- Evidence quality for each claim
- Contradictions with context
- Research gaps acknowledged
- Source citations

---

## Research Methodology Standards

### Evidence Hierarchy (Non-Negotiable)

1. **Systematic reviews/Meta-analyses** - Highest confidence
2. **Randomized controlled trials (RCTs)** - High confidence
3. **Observational studies** - Moderate confidence
4. **Case studies** - Lower confidence
5. **Expert opinion** - Contextual only

### Citation Requirements

Every factual claim must include:
- Source identification
- Study methodology (if applicable)
- Sample size and population
- Effect sizes (not just p-values)
- Publication date
- Potential conflicts of interest

### Handling Contradictions

When sources disagree:
1. Present both perspectives with equal weight
2. Note methodology differences
3. Consider population differences
4. Acknowledge uncertainty explicitly
5. Never resolve contradictions by picking sides

### Quality Indicators

**Green Flags:**
- Peer-reviewed publication
- Large sample sizes
- Replication by independent teams
- Pre-registered methodology
- Transparent data sharing

**Red Flags:**
- Industry-funded without disclosure
- Small, non-representative samples
- Unreplicated findings
- Methodology not disclosed
- Extraordinary claims without extraordinary evidence

---

## Research File Organization

```
episode-directory/
└── research/
    ├── p1-brief.md           # Topic and questions
    ├── p2-perplexity.md      # Academic research
    ├── p2-gemini.md          # Policy research
    ├── p2-chatgpt.md         # Technical research
    ├── p2-grok.md            # Real-time/regional
    ├── p2-manual.md          # Claude/manual research
    ├── cross-validation.md   # Source comparison
    ├── p3-briefing.md        # Organized synthesis
    └── documents/            # PDFs, papers
```

---

## Research Prompting Best Practices

### Structure Template

```markdown
# Research Request: [Topic]

## Scope
[Brief description of what to investigate]

## Core Questions
1. [Specific, answerable question]
2. [Specific, answerable question]
3. [Specific, answerable question]

## Focus Areas
- [Specific aspect to emphasize]
- [Specific aspect to emphasize]

## Quality Requirements
- Prioritize peer-reviewed sources
- Include effect sizes, not just significance
- Note sample populations and generalizability
- Distinguish correlation from causation
- Report contradictory findings

## Context
[Any relevant background information]
```

### Avoid These Prompting Mistakes

- Asking for predetermined conclusions
- Requesting only supporting evidence
- Ignoring contradictory findings
- Conflating correlation with causation
- Overgeneralizing from specific populations

---

## Synthesis to Report

After cross-validation, the synthesis agent (Claude) transforms the master briefing into `report.md`.

### Report Requirements

1. **Narrative Architecture** - Story-driven structure
2. **Evidence Grounding** - Every claim cited
3. **Accessibility** - Optimized for audio consumption
4. **Balance** - Contradictions presented fairly
5. **Takeaways** - Actionable conclusions
6. **Sources** - Complete reference list

### Report Structure

```markdown
# [Episode Title]

## Introduction
[Hook and overview]

## Section 1: [Topic]
[Narrative with citations]

## Section 2: [Topic]
[Narrative with citations]

## Key Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

## Sources
- [Full citation list]
```

---

## Tool-Specific Guidance

### Perplexity Deep Research

- Use for: Academic foundation
- Model: `sonar-deep-research`
- Reasoning effort: `high` for complex topics
- Auto-saves to timestamped files
- Returns with inline citations

### Gemini Deep Research

- Use for: Policy and regulatory analysis
- Uses polling mechanism (check every 30s)
- May take 3-10 minutes to complete
- Returns structured reports with sources
- Best for government and institutional sources

### GPT-Researcher

- Use for: Technical depth
- Searches 100+ sources in parallel
- Report types: `research_report`, `detailed_report`, `quick_report`, `deep`
- Multiple LLM backends supported
- Returns comprehensive technical analysis

### Manual Research

- Use for: Gap filling
- Claude for synthesis and nuanced analysis
- Grok for real-time and regional data
- Document all prompts in `logs/prompts.md`
- Maintain source links for verification

---

## Quality Assurance Checklist

Before proceeding to synthesis:

- [ ] All 5 research sources completed
- [ ] Cross-validation matrix documented
- [ ] Contradictions explicitly identified
- [ ] Evidence hierarchy applied to all claims
- [ ] Source quality assessed
- [ ] Gaps acknowledged
- [ ] Master briefing organized
- [ ] All prompts logged
