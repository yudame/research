# Issue 14: Update skills and agents for Claude Code 2.1.x changes

## Plan

### Phase 1: High Priority Fixes

1. **Fix podcast-synthesis-writer agent** (`.claude/agents/podcast-synthesis-writer.md`)
   - Remove `BashOutput` from tools list (unshipped in v2.0.64, replaced by `TaskOutput`)

2. **Hide deprecated chatgpt-deep-research skill** (`.claude/skills/chatgpt-deep-research/SKILL.md`)
   - Add `user-invocable: false` frontmatter

3. **Add frontmatter to unnamed skills**
   - `podcast-quality-scorecard/SKILL.md` — add `name` and `description`
   - `podcast-episode-planner/SKILL.md` — add `name` and `description`

### Phase 2: Medium Priority

4. **Add memory to podcast-synthesis-writer agent**
   - Add `memory: project` to frontmatter (v2.1.33 feature)

5. **Hide internal-only skills** (add `user-invocable: false`)
   - `podcast-episode-planner/SKILL.md`
   - `podcast-quality-scorecard/SKILL.md`
   - `notebooklm-audio/SKILL.md`

### Phase 3: Low Priority (Evaluate later)

- Consider `context: fork` for long-running skills (gpt-researcher, gemini-deep-research)
- Consider `agent` field for synthesis-heavy skills

## Files to Modify

| File | Changes |
|------|---------|
| `.claude/agents/podcast-synthesis-writer.md` | Remove BashOutput, add `memory: project` |
| `.claude/skills/chatgpt-deep-research/SKILL.md` | Add `user-invocable: false` |
| `.claude/skills/podcast-quality-scorecard/SKILL.md` | Add name, description, `user-invocable: false` |
| `.claude/skills/podcast-episode-planner/SKILL.md` | Add name, description, `user-invocable: false` |
| `.claude/skills/notebooklm-audio/SKILL.md` | Add `user-invocable: false` |

## Estimated Time

~15 minutes to execute + validate
