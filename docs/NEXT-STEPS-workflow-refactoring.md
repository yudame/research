# Next Steps: Workflow Refactoring Implementation

**Date:** 2026-01-30
**Status:** Workflow refactored, automation scripts need updates, ready for testing

---

## What's Complete ✅

1. **Workflow file refactored** - `.claude/skills/new-podcast-episode.md` updated with all Waves 1-5 improvements
2. **Three enhanced templates created:**
   - `docs/templates/p3-briefing-enhanced.md` (Wave 1 - Research & Synthesis)
   - `docs/templates/content_plan-enhanced.md` (Wave 2 - Episode Planning)
   - `docs/templates/metadata-enhanced.md` (Wave 4 - Publishing)
3. **Comprehensive documentation:**
   - `docs/workflow-refactoring-map.md` - Task-to-section mapping
   - `docs/workflow-refactoring-summary.md` - Complete change log with impact analysis

**Quality Improvements Integrated:**
- Wave 1 (5 tasks) - Research & Synthesis foundation
- Wave 2 (9 tasks) - Episode Planning architecture
- Wave 3 (4 tasks) - Audio Generation enhancements
- Wave 4 (11 tasks) - Publishing & Productization
- Wave 5 (2 tasks) - Quality Gates (exit criteria)

**Total:** 31 of 37 tasks integrated (Wave 6 format experiments remain as optional variations)

---

## What Needs Work ⚠️

### Critical (Blocking Test Episode)

**3 automation scripts need updates to support enhanced workflow:**

1. **podcast/tools/notebooklm_api.py**
   - **What needs updating:** Read `content_plan.md` and inject enhanced episodeFocus prompt
   - **Required enhancements:**
     - Extract Episode Structure Map summary
     - Extract Depth Budget summary
     - Extract Counterpoint Moments list
     - Inject Dialogue Dynamics section
     - Inject Episode Arc Template
   - **Reference:** See enhanced episodeFocus template in workflow Phase 9, lines ~1425-1475
   - **Test:** Generate audio for test episode, verify prompt includes all Wave 3 elements

2. **podcast/tools/notebooklm_prompt.py**
   - **What needs updating:** Same as notebooklm_api.py (manual fallback version)
   - **Reference:** Same enhanced template
   - **Test:** Generate prompt manually, verify completeness

3. **podcast/tools/update_feed.py**
   - **What needs updating:** Generate enhanced feed.xml with Wave 4 improvements
   - **Required enhancements:**
     - Read enhanced `logs/metadata.md` template
     - Generate rich `<content:encoded>` HTML from "What You'll Learn", Timestamps, Resources sections
     - Add `<podcast:transcript>` tag pointing to transcript.txt
     - Add `<itunes:episodeType>` tag (full/trailer/bonus)
     - Add `<itunes:episode>` number if series
   - **Reference:** See metadata-enhanced.md template, Wave 4 tasks C2.1-C2.3
   - **Test:** Update feed for test episode, validate with podcast-feed-validator

### Optional (Can test manually first)

**1 new script to create:**

4. **podcast/tools/generate_companion_resources.py**
   - **What it does:** Auto-generate one-page summary, action checklist, framework diagrams
   - **Input files:** report.md, content_plan.md, logs/metadata.md
   - **Output files:**
     - `YYYY-MM-DD-slug-cheatsheet.pdf` (one-pager)
     - `YYYY-MM-DD-slug-checklist.pdf` (action items)
     - `YYYY-MM-DD-slug-framework.png` (visual diagram if applicable)
   - **Reference:** Wave 4, tasks C3.1 and E2.3
   - **Test:** Generate resources for test episode, validate usefulness (Dimension 10)

**Decision:** Can manually create companion resources for first test episode, then automate if workflow is validated.

---

## Recommended Approach

### Option A: Full Automation First (Recommended if comfortable with script updates)

**Timeline:** ~2-4 hours of script work, then produce test episode

1. **Update 3 critical scripts** (notebooklm_api.py, notebooklm_prompt.py, update_feed.py)
2. **Test each script individually** with sample inputs
3. **Produce one full test episode** using refactored workflow + updated scripts
4. **Run quality scorecard** on test episode
5. **Compare to baseline** (33/50) and projection (46/50)
6. **Refine based on results**

**Pros:**
- Tests complete automation pipeline
- Faster per-episode execution once scripts work
- Validates that automation maintains quality

**Cons:**
- Upfront script development time
- If scripts have bugs, harder to isolate workflow vs. script issues

---

### Option B: Manual Test First (Recommended if want to validate workflow quickly)

**Timeline:** ~1-2 hours, produce test episode immediately

1. **Produce one full test episode MANUALLY** using refactored workflow
   - Use enhanced templates directly
   - Create companion resources manually
   - Hand-edit feed.xml with Wave 4 enhancements
2. **Run quality scorecard** on test episode
3. **Validate that workflow improvements work** (score ≥40/50?)
4. **THEN update automation scripts** if workflow is validated

**Pros:**
- Fastest path to validating workflow changes
- Isolates workflow quality from script bugs
- Can refine templates based on manual use before automating

**Cons:**
- Manual episode production is slower
- Risk of manual errors (which automation would prevent)

---

## Recommended: Option B (Manual Test First)

**Rationale:** The workflow is the core change. Scripts are implementation details. Validate that the enhanced templates and quality gates actually improve episode quality BEFORE investing time in automation.

**Steps:**

### 1. Choose Test Topic

**Criteria:**
- Similar to baseline episode (30-40 min, evidence-based, multiple themes)
- Rich enough to test all improvements (needs counterpoint opportunities, storytelling, actionable frameworks)
- Not part of existing series (to avoid comparison bias)

**Example topics:**
- "The Science of Habit Formation: What Actually Works"
- "Decision-Making Under Uncertainty: Frameworks from Research"
- "The Attention Economy: How Social Media Changed Learning"

### 2. Run /podcast-episode Workflow

Follow `.claude/skills/new-podcast-episode.md` EXACTLY as refactored:

**Phase 1: Setup**
- Use `setup_episode.py` as usual

**Phases 2-4: Research**
- Run Perplexity (Phase 2)
- Question discovery (Phase 3)
- Targeted followup research (Phase 4)

**Phase 5: Cross-Validation**
- ⭐ **NEW:** Create Counterpoint Discovery table
- Document where sources disagree, alternative frameworks

**Phase 6: Master Briefing**
- ⭐ **Use enhanced template:** `docs/templates/p3-briefing-enhanced.md`
- Complete Depth Distribution Analysis table
- Complete Practical Implementation Audit
- Create Story Bank (3-5 stories)
- Document Counterpoint Discovery

**Phase 7: Synthesis**
- Invoke podcast-synthesis-writer agent as usual
- Agent will follow enhanced requirements (Takeaway Clarity, Story Bank leverage)

**Phase 8: Episode Planning**
- ⭐ **Use enhanced template:** `docs/templates/content_plan-enhanced.md`
- Complete Episode Structure Map table
- Complete Mode-Switching Framework (5 modes with time allocations)
- Create Signposting Language section
- Complete Depth Budget table (time per theme)
- Define Problem → Solution Architecture
- Complete Build Toward Resolution section
- ⭐ **Design Counterpoint Moments** (2-3 minimum from p3-briefing discoveries)
- Complete Episode Arc Template
- ⭐ **Check exit criteria** (20+ checks) - DO NOT proceed until all pass

**Phase 9: Audio Generation**
- ⭐ **MANUAL:** Create enhanced episodeFocus prompt by hand
- Read content_plan.md sections
- Manually construct episodeFocus with:
  - Structural Guidance (Structure Map, Mode-Switching, Signposting, Depth Budget)
  - Dialogue Dynamics (counterpoint moments with specific prompts)
  - Episode Arc (Opening → Middle → Closing)
- Use NotebookLM manually or API with hand-crafted prompt

**Phase 10: Audio Processing**
- Transcription and chapters as usual

**Phase 11: Publishing**
- ⭐ **Use enhanced template:** `docs/templates/metadata-enhanced.md`
- Complete "What You'll Learn" section (3-5 bullets)
- Complete Key Timestamps section (5-7 major sections)
- Complete Resources & Tools section (grouped, actionable descriptions)
- Complete Call-to-Action section (primary + voiced)
- ⭐ **Manually create companion resources:**
  - One-page summary (use report.md + content_plan.md frameworks)
  - Action checklist (extract from Practical Implementation Audit)
  - Framework diagram if applicable (e.g., Mode-Switching visual)
- ⭐ **Manually update feed.xml with Wave 4 enhancements:**
  - Rich `<content:encoded>` HTML (use metadata template "Show Notes" section)
  - Add `<podcast:transcript>` tag
  - Add `<itunes:episodeType>` and episode number
- ⭐ **Check exit criteria** (30+ checks) - DO NOT proceed until all pass

**Phase 12: Commit & Push**
- As usual

### 3. Run Quality Scorecard

```bash
# After episode is published, run scorecard
Use Task tool with subagent_type='general-purpose':

"Run the podcast-quality-scorecard skill on the test episode.

Episode path: podcast/episodes/YYYY-MM-DD-test-topic/
Episode title: [Test Topic Title]

Generate comprehensive quality scorecard and save to logs/quality_scorecard.md"
```

### 4. Analyze Results

**Compare to baseline:**
- Baseline (Delegation): 33/50 (66%)
- Test episode: ___ /50 (___%)

**By dimension:**
| Dimension | Baseline | Test | Change | Target |
|-----------|----------|------|--------|--------|
| 1. Structural Clarity | 4/5 | ? | ? | 5/5 |
| 2. Depth Distribution | 2/5 | ? | ? | 4/5 |
| 3. Mode-Switching Clarity | 3/5 | ? | ? | 4/5 |
| 4. Dialogue Dynamics | 2/5 | ? | ? | 4/5 |
| 5. Practical Actionability | 5/5 | ? | ? | 5/5 |
| 6. Takeaway Clarity | 4/5 | ? | ? | 5/5 |
| 7. Storytelling Quality | 4/5 | ? | ? | 5/5 |
| 8. Episode Arc & Resolution | 4/5 | ? | ? | 5/5 |
| 9. Packaging & Discoverability | 3/5 | ? | ? | 4/5 |
| 10. Companion Resource Value | 2/5 | ? | ? | 4/5 |

**Success criteria:**
- **Success:** Test episode ≥40/50 (80%), critical dimensions (2, 4, 10) ≥4/5
- **Partial:** Test episode 37-39/50, critical dimensions ≥3/5
- **Needs work:** <37/50 or critical dimensions <3/5

### 5. Decision Point

**If Successful (≥40/50):**
→ Workflow validated! Proceed to update automation scripts.
→ Update scripts: notebooklm_api.py, notebooklm_prompt.py, update_feed.py
→ Create generate_companion_resources.py
→ Produce 2 more test episodes with automation to confirm repeatability
→ Mark workflow as production-ready

**If Partial (37-39/50):**
→ Identify which dimensions didn't improve as expected
→ Review corresponding workflow sections and templates
→ Make targeted refinements
→ Produce 1 more manual test episode
→ Re-evaluate

**If Needs Work (<37/50):**
→ Conduct root cause analysis
→ Were templates too complex? Too ambiguous?
→ Were exit criteria actually enforced?
→ Were some improvements counterproductive?
→ Refine workflow and/or simplify improvements
→ Retest

---

## Quick Start Commands

### To produce manual test episode:

```bash
# 1. Choose topic and create episode directory
cd ~/src/research/podcast/tools
uv run python setup_episode.py --slug "test-topic" --title "Test Episode Title"

# 2. Follow refactored workflow in .claude/skills/new-podcast-episode.md
# Use enhanced templates:
# - docs/templates/p3-briefing-enhanced.md
# - docs/templates/content_plan-enhanced.md
# - docs/templates/metadata-enhanced.md

# 3. After publishing, run scorecard
# Use Claude to invoke: podcast-quality-scorecard skill on episode path

# 4. Analyze results and decide next steps
```

---

## Timeline Estimate

**Manual Test Episode (Option B):**
- Episode production: 4-6 hours (same as baseline, maybe +1 hour for new templates)
- Quality scorecard: 30 minutes
- Analysis: 30 minutes
- **Total:** 5-7 hours to validate workflow

**Script Updates (if workflow validated):**
- notebooklm_api.py + notebooklm_prompt.py: 1-2 hours
- update_feed.py: 1-2 hours
- generate_companion_resources.py: 2-3 hours (new script)
- Testing each script: 1-2 hours
- **Total:** 5-9 hours to automate

**Full Validation (manual test + automation + 2 more test episodes):**
- Manual test: 5-7 hours
- Script updates: 5-9 hours
- 2 automated test episodes: 6-8 hours (3-4 hours each)
- **Total:** 16-24 hours

**ROI:** If workflow improvements are validated, every future episode benefits. Even 20 hours of upfront investment pays off after 5-10 episodes.

---

## Questions to Answer During Testing

1. **Are enhanced templates usable?**
   - Too complex? Too ambiguous?
   - Missing anything important?
   - Should any sections be optional vs. required?

2. **Do exit criteria catch real issues?**
   - Did they prevent proceeding with low-quality work?
   - Were any checks redundant or busywork?
   - Should any be warnings vs. hard blockers?

3. **Is the workflow sustainable?**
   - Does it feel overwhelming or natural?
   - Is the time investment worth the quality gain?
   - Would you use this workflow for every episode?

4. **Which improvements had the biggest impact?**
   - Rank improvements by ROI (impact per effort)
   - Could some be simplified without losing value?
   - Are there diminishing returns?

---

## Contact & Support

If you encounter issues or have questions during testing:

1. **Review documentation:**
   - `docs/workflow-refactoring-summary.md` - Complete change log
   - `docs/workflow-refactoring-map.md` - Task-to-section mapping
   - Enhanced templates in `docs/templates/`

2. **Check workflow file:**
   - `.claude/skills/new-podcast-episode.md` - Authoritative source

3. **Run quality scorecard:**
   - `.claude/skills/podcast-quality-scorecard/SKILL.md` - Diagnostic tool

4. **Iterate:**
   - This is v1 of refactored workflow
   - Expect to refine based on real usage
   - Document learnings in scorecard notes

---

## Success Indicators

**You'll know the refactoring was successful when:**

✅ Test episode scores ≥40/50 (vs. baseline 33/50)
✅ Critical dimensions (Depth Distribution, Dialogue Dynamics, Companion Resources) score ≥4/5
✅ Workflow feels natural (not bolt-on or overwhelming)
✅ Templates are usable (clear, not ambiguous)
✅ Exit criteria catch real issues (not just busywork)
✅ Quality improvement is repeatable (2-3 test episodes score consistently high)

**Then you can confidently:**
- Use refactored workflow for all future episodes
- Update automation scripts to maintain quality
- Track scorecard trends over time
- Consider Wave 6 format experiments

---

**Current Status:** Ready for manual test episode. Choose a topic and begin!
