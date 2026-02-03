# Workflow Refactoring Map: Quality Improvements Integration

**Created:** 2026-01-30
**Purpose:** Map 37 improvement tasks to specific workflow sections for systematic integration

---

## Overview

This document maps the 37 improvement tasks from `docs/plans/podcast_episode_improvements.md` to specific sections of `.claude/skills/new-podcast-episode.md` for refactoring.

**Target:** Integrate Waves 1-5 (31 tasks) into standard workflow. Wave 6 (6 tasks) remains as experimental variations.

---

## Wave 1: Research & Synthesis (Phases 5-7)

### Phase 5: Cross-Validation (Lines 1027-1086)

**B1.2 (Task 2) - Counterpoint Discovery**
- **Location:** After "Critical Facts Verification" section (line ~1036)
- **Add:** New "Counterpoint Discovery" section in cross-validation matrix
- **Purpose:** Identify where sources disagree for later use in dialogue design
- **Template addition:**
  ```markdown
  ## Counterpoint Discovery

  | Topic | Source A Position | Source B Position | Opportunity |
  |-------|------------------|------------------|-------------|
  | [Topic] | [Position] | [Conflicting position] | Dialogue moment |
  ```

### Phase 6: Master Briefing (Lines 1087-1153)

**Current structure:** research/p3-briefing.md template (lines 276-375)

**B1.1 (Task 1) - Depth Distribution Analysis**
- **Location:** After "VERIFIED KEY FINDINGS" section, before "RESEARCH GAPS"
- **Add:** New "DEPTH DISTRIBUTION ANALYSIS" section
- **Purpose:** Flag subtopics with insufficient evidence/sources
- **Template addition:**
  ```markdown
  ## DEPTH DISTRIBUTION ANALYSIS

  | Subtopic | Sources Found | Depth Rating | Action Needed |
  |----------|---------------|--------------|---------------|
  | [Topic 1] | 12 sources | ⭐⭐⭐⭐⭐ Deep | None |
  | [Topic 2] | 3 sources | ⭐⭐☆☆☆ Shallow | Request additional research |
  ```

**B1.3 (Task 3) - Practical Implementation Audit**
- **Location:** After "VERIFIED KEY FINDINGS" section, before "RESEARCH GAPS"
- **Add:** New "PRACTICAL IMPLEMENTATION AUDIT" section
- **Purpose:** For each finding, identify "How would someone actually do this?"
- **Template addition:**
  ```markdown
  ## PRACTICAL IMPLEMENTATION AUDIT

  For each major finding, document:
  - **Finding:** [What the research shows]
  - **Implementation:** [Specific tactics, steps, frameworks]
  - **Specificity check:** Does this include timeframes, thresholds, concrete criteria?
  ```

**B2.2 (Task 5) - Story Bank**
- **Location:** After "PRACTITIONER PERSPECTIVES" section
- **Add:** New "STORY BANK" section
- **Purpose:** Collect examples, case studies, narratives for storytelling mode
- **Template addition:**
  ```markdown
  ## STORY BANK

  Examples and case studies collected during research:

  ### Story 1: [Title]
  - **Source:** [Citation]
  - **Summary:** [What happened]
  - **Illustrates:** [Which concept/finding]
  - **Emotional resonance:** [High/Medium/Low]
  - **Memorability:** [High/Medium/Low]
  ```

### Phase 7: Synthesis (Lines 1154-1228)

**B2.1 (Task 4) - Takeaway Clarity Check**
- **Location:** In podcast-synthesis-writer agent invocation instructions
- **Modify:** Add to quality requirements for report.md
- **Change:**
  ```markdown
  The podcast-synthesis-writer agent will:
  1. Read research/p3-briefing.md and individual research/p2-*.md files
  2. Transform organized research into engaging narrative report
  3. Apply evidence standards and podcast storytelling principles
  4. Create report.md with proper citations and source hierarchy
  5. **Ensure takeaway clarity:**
     - Each major section ends with "What does this mean for listeners?"
     - 1-3 core takeaways for entire episode identified
     - Core takeaways made explicit in synthesis
  ```

**Updated p3-briefing.md template location:** Lines 276-375

---

## Wave 2: Episode Planning (Phase 8)

### Phase 8: Episode Planning (Lines 1232-1300)

**Current:** Invokes podcast-episode-planner skill to create content_plan.md

**A1.1 (Task 6) - Episode Structure Map**
- **Location:** content_plan.md template (new section)
- **Add:** "Episode Structure Map" section
- **Purpose:** Map when to be philosophical, practical, storytelling, analytical

**A1.2 (Task 7) - Mode-Switching Framework**
- **Location:** content_plan.md template (new section)
- **Add:** "Mode-Switching Framework" section
- **Purpose:** Define clear transitions between modes

**A1.3 (Task 8) - Signposting Language**
- **Location:** content_plan.md template (new section)
- **Add:** "Signposting Language" section
- **Purpose:** Template phrases for transitions

**A1.4 (Task 9) - Depth Budget**
- **Location:** content_plan.md template (new section)
- **Add:** "Depth Budget" table
- **Purpose:** Allocate time percentage to each major theme

**A2.1 (Task 10) - Problem → Solution Architecture**
- **Location:** content_plan.md template (new section)
- **Add:** "Problem → Solution Architecture" framework
- **Purpose:** Separate problem exploration from solution delivery

**A2.2 (Task 11) - Build Toward Resolution**
- **Location:** content_plan.md template (new section)
- **Add:** "Build Toward Resolution" structure
- **Purpose:** Work backward from main takeaway

**A2.3 (Task 12) - Counterpoint Moments**
- **Location:** content_plan.md template (new section)
- **Add:** "Counterpoint Moments" design
- **Purpose:** Identify 2-3 moments where speakers should diverge

**E1.1 (Task 13) - Update content_plan.md template**
- **Location:** New file template (see Template Updates section below)
- **Consolidates:** Tasks 6-12

**E1.2 (Task 14) - podcast-episode-planner skill requirements**
- **Location:** Workflow instructions for Phase 8
- **Update:** Enhanced skill requirements

**Updated Phase 8 exit criteria (E3.1, Task 30):**
```markdown
EXIT CRITERIA (all must be true to proceed):
✓ content_plan.md created with three-section structure
✓ Episode Structure Map defined (modes and transitions)
✓ Mode-Switching Framework applied
✓ Signposting language included
✓ Depth Budget confirms even coverage across themes
✓ Counterpoint moments designed (2-3 minimum)
✓ Problem → Solution architecture clear
✓ Episode builds toward clear resolution/takeaway
```

---

## Wave 3: Audio Generation (Phase 9)

### Phase 9: Audio Generation (Lines 1305-1407)

**A3.1 (Task 15) - Enhanced episodeFocus prompt template**
- **Location:** notebooklm_api.py and notebooklm_prompt.py scripts
- **Modify:** episodeFocus prompt to include structural guidance
- **Purpose:** NotebookLM follows intended structure with mode-switching

**A3.2 (Task 16) - Dialogue Dynamics section**
- **Location:** episodeFocus prompt template
- **Add:** Instructions for counterpoint moments
- **Purpose:** Request specific moments of push-back or divergence

**A3.3 (Task 17) - Episode Arc Template**
- **Location:** episodeFocus prompt template
- **Add:** Opening → Middle → Closing structure guidance
- **Purpose:** Consistent arc execution

**E1.3 (Task 18) - Update notebooklm_prompt.py**
- **Location:** podcast/tools/notebooklm_prompt.py
- **Modify:** Script to read content_plan.md and inject improvements
- **Purpose:** Automation maintains quality

**Enhanced episodeFocus prompt template (Tasks 15-17):**
```python
episodeFocus = f"""
You are creating a Yudame Research podcast episode: {episode_title}

**STRUCTURAL GUIDANCE** (from content_plan.md):
- **Episode Structure Map:** {structure_map_summary}
- **Mode-Switching:** Use clear transitions when moving between philosophy, research, storytelling, practical, and landing modes
- **Signposting Language:** Preview structure at opening, use progress markers throughout
- **Depth Budget:** Allocate time proportionally: {depth_budget_summary}

**DIALOGUE DYNAMICS:**
- **Counterpoint Moments:** At these specific points, speakers should diverge or push back:
  {counterpoint_moments_list}
- Request 2-3 "wait, but what about..." or "I see it differently because..." moments
- Avoid pure agreement pattern - encourage supportive challenge

**EPISODE ARC:**
- **Opening (3-5 min):** Hook + Problem Definition + Structure Preview
- **Middle (20-30 min):** Exploration with clear mode-switching and signposting
- **Closing (3-5 min):** Synthesis + Key Takeaway + Clear Next Step + Callback to opening

Follow the episode content plan and research materials to create an engaging, well-structured conversation.
"""
```

---

## Wave 4: Publishing & Productization (Phase 11)

### Phase 11: Publishing (Lines 1540-1714)

**E2.1 (Task 19) - Update logs/metadata.md template**
- **Location:** New template (see Template Updates section below)
- **Add:** "What You'll Learn", "Key Timestamps", "Resources & Tools", "Call-to-Action" sections

**C1.1 (Task 20) - Expand description template**
- **Location:** logs/metadata.md template
- **Integrated with Task 19**

**C1.2 (Task 21) - Call-to-Action Framework**
- **Location:** logs/metadata.md template + episodeFocus prompt
- **Add:** CTA section in metadata + voiced CTA in audio

**C1.3 (Task 22) - Enhance source links presentation**
- **Location:** logs/metadata.md template
- **Add:** Grouped sources with 1-sentence actionable descriptions

**C2.1 (Task 23) - iTunes episode metadata**
- **Location:** update_feed.py script modifications
- **Add:** `<itunes:episode>`, `<itunes:episodeType>` tags

**C2.2 (Task 24) - Enhanced HTML show notes**
- **Location:** update_feed.py script modifications
- **Add:** Structured `<content:encoded>` HTML

**C2.3 (Task 25) - Transcript tag**
- **Location:** update_feed.py script modifications
- **Add:** `<podcast:transcript>` tag support

**E2.2 (Task 26) - Update update_feed.py**
- **Location:** podcast/tools/update_feed.py
- **Consolidates:** Tasks 23-25

**C3.1 (Task 27) - Companion resource templates**
- **Location:** New Phase 11 step (after metadata creation)
- **Add:** One-page summary, action checklist, framework diagram templates

**C3.2 (Task 28) - Episode Landing Page**
- **Location:** New Phase 11 step (after companion resources)
- **Add:** HTML page generation for each episode

**E2.3 (Task 29) - Post-processing script**
- **Location:** New podcast/tools script
- **Consolidates:** Tasks 27-28
- **Purpose:** Generate companion resources automatically

**Updated Phase 11 exit criteria (E3.2, Task 31):**
```markdown
EXIT CRITERIA (all must be true to proceed):
✓ cover.png exists and branded (~1MB)
✓ logs/metadata.md created with all fields:
  - "What You'll Learn" section (3-5 bullets)
  - Key timestamps (5-7 major sections)
  - Resources & Tools with actionable descriptions
  - Call-to-Action defined
✓ Episode description written (1-2 sentences + report link + "What You'll Learn")
✓ Keywords generated (5-10 episode-specific terms)
✓ Key sources validated (3-5 Tier 1/2 sources, grouped by type, actionable descriptions)
✓ Companion resources created:
  - One-page summary/cheat sheet
  - Action checklist
  - Framework diagram (if applicable)
✓ feed.xml updated with new `<item>` entry
✓ Enhanced `<content:encoded>` HTML show notes
✓ `<podcast:transcript>` tag added
✓ iTunes episode metadata included
✓ `<lastBuildDate>` updated
✓ Feed validator reports VALID
```

---

## Wave 5: Quality Gates (Exit Criteria)

**E3.1 (Task 30) - Phase 8 exit criteria**
- **Location:** Phase 8 exit criteria section
- **Documented in:** Wave 2 section above

**E3.2 (Task 31) - Phase 11 exit criteria**
- **Location:** Phase 11 exit criteria section
- **Documented in:** Wave 4 section above

---

## Wave 6: Format Experiments (Separate Branch)

**Note:** Wave 6 tasks (D1.1-D1.4, D2.1-D2.2) are NOT integrated into the standard workflow. They represent experimental format variations that:
- Can be tested after Wave 2 complete (requires planning foundation)
- Each produces a full episode measured against standard workflow
- Successful experiments can be optionally integrated later
- Standard workflow remains the default

**Approach:** Document Wave 6 experiments in a separate `docs/podcast-format-experiments.md` guide rather than modifying the core workflow.

---

## Modification Summary by Workflow Section

| Workflow Section | Lines | Changes | Wave |
|-----------------|-------|---------|------|
| Phase 5: Cross-Validation | 1027-1086 | Add Counterpoint Discovery section | 1 |
| Phase 6: Master Briefing | 1087-1153 | Add 3 sections: Depth Analysis, Practical Audit, Story Bank | 1 |
| Phase 7: Synthesis | 1154-1228 | Add Takeaway Clarity requirements | 1 |
| Phase 8: Episode Planning | 1232-1300 | Major expansion: 7 new content_plan sections + enhanced exit criteria | 2, 5 |
| Phase 9: Audio Generation | 1305-1407 | Enhanced episodeFocus prompt template | 3 |
| Phase 11: Publishing | 1540-1714 | Enhanced metadata template + companion resources + exit criteria | 4, 5 |

**Total sections modified:** 6 of 12 phases
**New template sections:** 13
**Updated exit criteria:** 2 phases
**New scripts/tools:** 1 (post-processing for companion resources)

---

## Dependencies & Order of Implementation

1. **Wave 1 first** - Improves research/synthesis quality → affects all downstream phases
2. **Wave 2 depends on Wave 1** - Needs quality research inputs to plan well
3. **Wave 3 depends on Wave 2** - Needs quality planning to generate quality audio
4. **Wave 4 independent** - Can implement in parallel with Waves 1-3
5. **Wave 5 after Waves 2 & 4** - Quality gates enforce standards from earlier waves

**Recommended rollout:** Implement in wave order (1→2→3→4→5), testing with full episode after each wave.

---

## Next Steps

1. Create updated templates (see next document)
2. Modify workflow file (`.claude/skills/new-podcast-episode.md`)
3. Update automation scripts (notebooklm_prompt.py, update_feed.py)
4. Create new post-processing script for companion resources
5. Test with one full episode
6. Apply quality scorecard to measure improvement
