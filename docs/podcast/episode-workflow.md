# Episode Workflow

This document describes the complete 12-phase workflow for creating a podcast episode from topic selection to publication.

## Overview

The episode creation process is divided into 12 phases:

| Phase | Name | Owner | Duration |
|-------|------|-------|----------|
| 1 | Setup | Claude | 2-5 min |
| 2 | Academic Research | Claude | 2-3 min |
| 3 | Question Discovery | Claude | 5-10 min |
| 4 | Targeted Research | Claude | 10-30 min |
| 5 | Cross-Validation | Claude | 10-20 min |
| 6 | Master Briefing | Claude | 10-15 min |
| 7 | Synthesis | Claude | 15-30 min |
| 8 | Cover Art | Claude | 5-10 min |
| 9 | Audio Creation | User | 30-60 min |
| 10 | Audio Processing | Claude | 20-40 min |
| 11 | Publishing | Claude | 10-15 min |
| 12 | Deployment | Claude | 5 min |

---

## Phase 1: Setup

**Purpose:** Create directory structure and initial files.

### Actions

1. Create episode directory with standard structure
2. Initialize research subdirectory
3. Initialize logs subdirectory
4. Create p1-brief.md with topic and questions

### Directory Structure Created

```
podcast/episodes/[series-name/]YYYY-MM-DD-slug/
├── research/
│   └── p1-brief.md
├── logs/
│   └── prompts.md
└── tmp/
```

### Phase Completion

- [ ] Episode directory exists
- [ ] research/ subdirectory created
- [ ] logs/ subdirectory created
- [ ] p1-brief.md contains topic and initial questions

---

## Phase 2: Academic Research

**Purpose:** Establish academic foundation with peer-reviewed sources.

### Actions

1. Run Perplexity Deep Research with p1-brief.md
2. Save results to research/p2-perplexity.md
3. Log prompt to logs/prompts.md

### Tool Configuration

- Model: sonar-deep-research
- Reasoning effort: high
- Focus: Academic papers, meta-analyses, systematic reviews

### Phase Completion

- [ ] Perplexity research complete
- [ ] Results saved to p2-perplexity.md
- [ ] Prompt logged

---

## Phase 3: Question Discovery

**Purpose:** Identify gaps and additional research questions.

### Actions

1. Analyze Phase 2 results
2. Identify knowledge gaps
3. Formulate new research questions
4. Prioritize questions for Phase 4

### Output

Updated research questions to guide targeted research.

### Phase Completion

- [ ] Initial results analyzed
- [ ] Gaps identified
- [ ] Additional questions formulated
- [ ] Phase 4 research priorities set

---

## Phase 4: Targeted Research

**Purpose:** Deep-dive into specific topics with multiple tools.

### Actions (Run in Parallel)

**4A: Policy Research**
1. Run Gemini Deep Research
2. Focus: Regulatory, policy, strategic context
3. Save to research/p2-gemini.md

**4B: Technical Research**
1. Run GPT-Researcher
2. Focus: Technical depth, 100+ sources
3. Save to research/p2-chatgpt.md

**4C: Manual Research (as needed)**
1. Claude for synthesis/analysis
2. Grok for real-time/regional data
3. Save to research/p2-manual.md or p2-grok.md

### Phase Completion

- [ ] Gemini research complete
- [ ] GPT-Researcher complete
- [ ] Manual research complete (if needed)
- [ ] All prompts logged

---

## Phase 5: Cross-Validation

**Purpose:** Verify findings across sources and identify contradictions.

### Actions

1. Create agreement matrix across sources
2. Identify contradictions
3. Assess source quality
4. Apply evidence hierarchy
5. Document in cross-validation.md

### Evidence Hierarchy

1. Meta-analyses/systematic reviews
2. Randomized controlled trials
3. Observational studies
4. Case studies
5. Expert opinion

### Phase Completion

- [ ] Agreement matrix complete
- [ ] Contradictions documented
- [ ] Source quality assessed
- [ ] Evidence hierarchy applied
- [ ] cross-validation.md complete

---

## Phase 6: Master Briefing

**Purpose:** Organize validated findings for synthesis.

### Actions

1. Compile findings from all sources
2. Organize by topic/theme
3. Include evidence quality ratings
4. Note contradictions with context
5. Acknowledge gaps
6. Create p3-briefing.md

### Briefing Structure

```markdown
# Master Research Briefing

## Executive Summary

## Section 1: [Topic]
### Key Findings
### Evidence Quality
### Contradictions

## Section 2: [Topic]
...

## Research Gaps

## Source Summary
```

### Phase Completion

- [ ] All findings compiled
- [ ] Organized by topic
- [ ] Evidence quality noted
- [ ] Contradictions contextualized
- [ ] Gaps acknowledged
- [ ] p3-briefing.md complete

---

## Phase 7: Synthesis

**Purpose:** Transform research into narrative report.

### Actions

1. Invoke synthesis agent
2. Transform briefing into narrative
3. Ensure all claims cited
4. Create engaging story structure
5. Add key takeaways
6. Generate report.md

### Report Requirements

- Narrative architecture (story-driven)
- Every claim cited
- Accessible for audio consumption
- Contradictions presented fairly
- Actionable takeaways
- Complete source list

### Phase Completion

- [ ] Synthesis agent invoked
- [ ] Narrative structure created
- [ ] All claims cited
- [ ] Takeaways included
- [ ] Sources listed
- [ ] report.md complete

---

## Phase 8: Cover Art

**Purpose:** Generate AI cover art with branding.

### Actions

1. Auto-generate prompt from report.md (or use custom)
2. Generate base image via Gemini/OpenRouter
3. Apply Yudame branding (logo, text, border)
4. Save as cover.png
5. Log prompt

### Branding Elements

- Yudame logo (top-left)
- Series/episode text (if applicable)
- Yellow border (#FFC20E, 20px)

### Phase Completion

- [ ] Image prompt generated
- [ ] Base image created
- [ ] Branding applied
- [ ] cover.png saved
- [ ] Prompt logged

---

## Phase 9: Audio Creation

**Purpose:** Create podcast audio (USER TASK).

### User Actions

1. Upload report.md to NotebookLM
2. Generate audio podcast
3. Download M4A file
4. Provide file path to Claude

### NotebookLM Notes

- Upload report.md as source
- Use "Audio Overview" feature
- Download generated audio
- Typical output: 30-40 minutes

### Phase Completion

- [ ] Report uploaded to NotebookLM
- [ ] Audio generated
- [ ] M4A file downloaded
- [ ] File path provided

---

## Phase 10: Audio Processing

**Purpose:** Convert, transcribe, and add chapters.

### Actions

1. Convert M4A to MP3 (128kbps)
2. Record file size and duration
3. Transcribe with Whisper
4. Generate chapters (10-15)
5. Embed chapters in MP3
6. Log metadata

### Output Files

| File | Description |
|------|-------------|
| YYYY-MM-DD-slug.mp3 | Final audio with chapters |
| _transcript.json | Whisper output |
| _chapters.txt | FFmpeg format |
| _chapters.json | Podcasting 2.0 format |

### Phase Completion

- [ ] M4A converted to MP3
- [ ] File size recorded (bytes)
- [ ] Duration recorded (MM:SS)
- [ ] Transcript generated
- [ ] Chapters created (10-15)
- [ ] Chapters embedded
- [ ] Metadata logged

---

## Phase 11: Publishing

**Purpose:** Update RSS feed with new episode.

### Actions

1. Gather all metadata
2. Create episode item XML
3. Insert into feed.xml
4. Update lastBuildDate
5. Validate feed structure
6. Validate source links

### Metadata Required

| Field | Source |
|-------|--------|
| Title | Episode planning |
| Description | Report summary |
| File size | File system (bytes) |
| Duration | FFmpeg output |
| Keywords | Report content |
| Sources | Report citations |

### Phase Completion

- [ ] Metadata gathered
- [ ] Episode item created
- [ ] feed.xml updated
- [ ] lastBuildDate current
- [ ] XML validates
- [ ] URLs accessible

---

## Phase 12: Deployment

**Purpose:** Push changes and verify deployment.

### Actions

1. Stage all new files
2. Commit with descriptive message
3. Push to main branch
4. Wait for GitHub Pages deployment (2-3 min)
5. Verify feed accessible
6. Test episode playback

### Commit Message Format

```
feat: Add [Episode Title] to podcast feed

- Series: [Series Name] Episode [N]
- Duration: [MM:SS]
- Topics: [key topics]
```

### Phase Completion

- [ ] Files staged
- [ ] Commit created
- [ ] Pushed to main
- [ ] GitHub Pages deployed
- [ ] Feed accessible
- [ ] Episode plays correctly

---

## Workflow Entry Points

### Starting a New Episode

Use slash command:
```
/podcast-episode [topic]
```

### Starting a Series

Use slash command:
```
/podcast-series [topic-area]
```

---

## Phase Dependencies

```
Phase 1 (Setup)
    │
    ▼
Phase 2 (Academic Research)
    │
    ▼
Phase 3 (Question Discovery)
    │
    ▼
Phase 4 (Targeted Research) ─── Parallel execution
    │
    ▼
Phase 5 (Cross-Validation)
    │
    ▼
Phase 6 (Master Briefing)
    │
    ▼
Phase 7 (Synthesis)
    │
    ├───────────────────────┐
    ▼                       ▼
Phase 8 (Cover Art)    Phase 9 (Audio) ─── User task
    │                       │
    └───────────────────────┘
                │
                ▼
        Phase 10 (Audio Processing)
                │
                ▼
        Phase 11 (Publishing)
                │
                ▼
        Phase 12 (Deployment)
```

---

## Resuming Interrupted Workflows

If workflow is interrupted:

1. Check which phase was last completed
2. Review existing files in episode directory
3. Resume from next incomplete phase
4. Verify all previous phase outputs exist

### Phase Output Verification

| Phase | Verify Exists |
|-------|---------------|
| 1 | Episode directory, p1-brief.md |
| 2 | p2-perplexity.md |
| 4 | p2-gemini.md, p2-chatgpt.md |
| 5 | cross-validation.md |
| 6 | p3-briefing.md |
| 7 | report.md |
| 8 | cover.png |
| 10 | .mp3, _transcript.json, _chapters.* |
| 11 | Episode in feed.xml |

---

## Time Estimates

| Scenario | Estimated Time |
|----------|----------------|
| Full episode (research + audio) | 3-4 hours |
| Research only (Phases 1-7) | 1.5-2 hours |
| Audio processing only (Phase 10) | 30-40 min |
| Publishing only (Phases 11-12) | 15-20 min |

Note: Phase 9 (audio creation) time depends on user and NotebookLM processing.
