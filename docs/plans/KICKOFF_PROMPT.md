# Prompt to Start Wave 1 Implementation

Use this prompt when you're ready to produce your next podcast episode and want to implement the first wave of quality improvements.

---

## Copy-Paste Prompt

```
I'm ready to produce a new podcast episode and want to implement Wave 1 improvements from the quality plan.

**Episode topic:** [DESCRIBE TOPIC]

**What to do:**

Read the improvement plan at `docs/plans/podcast_episode_improvements.md` and implement **Wave 1: Research & Synthesis** (5 tasks) during episode production:

**Wave 1 Tasks (Phases 2-7):**

1. **B1.1** - Depth Distribution Analysis in Phase 6 (Master Briefing)
   - After organizing research by subtopic, assess relative depth
   - Flag subtopics with insufficient evidence/sources
   - Create table showing theme coverage percentages

2. **B1.2** - Counterpoint Discovery in Phase 5 (Cross-Validation)
   - Explicitly identify where sources disagree
   - Note alternative frameworks or approaches
   - Document for use in dialogue design

3. **B1.3** - Practical Implementation Audit in Phase 6 (Master Briefing)
   - For each major finding, identify: "How would someone actually do this?"
   - Extract specific tactics, steps, frameworks
   - Ensure practical advice is proportional to conceptual coverage

4. **B2.1** - Takeaway Clarity Check in Phase 7 (Synthesis)
   - Each major section in report.md should end with "What does this mean for listeners?"
   - Identify 1-3 core takeaways for entire episode
   - Make these explicit in synthesis

5. **B2.2** - Story Bank in Phase 6 (Master Briefing)
   - Collect examples, case studies, narratives during research
   - Tag by: illustrative power, emotional resonance, memorability
   - Ensure storytelling mode has rich material

**Integration approach:**

- Apply these tasks DURING the normal episode workflow, not as separate work
- When you reach Phase 6 (Master Briefing creation), add the depth distribution analysis, practical audit, and story bank sections
- When you reach Phase 7 (Synthesis), add the takeaway clarity check
- Document what you did in each task (brief notes)

**After episode is complete:**

1. Run quality scorecard (use `.claude/skills/podcast-quality-scorecard/SKILL.md`)
2. Compare scores to baseline (Delegation episode: 33/50)
3. Focus on Dimensions 2, 5, 6, 7 (the ones Wave 1 targets):
   - Dimension 2: Depth Distribution (baseline: 2/5)
   - Dimension 5: Practical Actionability (baseline: 5/5 - maintain)
   - Dimension 6: Takeaway Clarity (baseline: 4/5 - improve to 5/5)
   - Dimension 7: Storytelling Quality (baseline: 4/5 - improve to 5/5)

4. Document learnings: What worked? What needs refinement? Ready for Wave 2?

**Expected outcome:** Episode scores 4+ on Dimensions 2, 5, 6, 7 with measurable improvements in depth distribution and storytelling.
```

---

## Alternative: Gradual Implementation

If you want to ease into it, implement **one task per episode** instead of all 5 at once:

**Episode 1:** Implement B1.1 only (Depth Distribution Analysis)
**Episode 2:** Implement B1.1 + B1.2 (add Counterpoint Discovery)
**Episode 3:** Implement B1.1 + B1.2 + B1.3 (add Practical Audit)
**Episode 4:** Implement all 5 Wave 1 tasks
**Episode 5:** Refine Wave 1, prepare for Wave 2

This slower approach lets you learn and refine each improvement before adding the next.

---

## Success Criteria for Wave 1 Completion

**Complete Wave 1 when:**
- 3 consecutive episodes score 4+ on Dimensions 2, 5, 6, 7
- Improvements are repeatable (not one-off flukes)
- Workflow changes feel natural, not forced
- Documentation exists for how to apply each task

**Then:** Move to Wave 2 (Episode Planning improvements)
