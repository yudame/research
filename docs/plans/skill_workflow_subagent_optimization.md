---
status: Approved
type: chore
appetite: Medium
owner: Tom
created: 2026-02-11
tracking:
---

# Podcast Skill Workflow: Sub-Agent Optimization

## Problem

The 12-phase podcast episode workflow (`new-podcast-episode.md`) runs inside a single orchestrator context that progressively accumulates massive amounts of content, eventually overwhelming the context window and degrading quality.

**Current behavior:**

The orchestrator context accumulates:

| Content | Size | When Loaded |
|---------|------|-------------|
| `new-podcast-episode.md` (skill definition) | 77 KB | Phase 1 (start) |
| `CLAUDE.md` (project instructions) | 11 KB | Phase 1 (start) |
| `p2-perplexity.md` | ~67 KB | Phase 3 (question discovery reads it) |
| `p2-claude.md` | ~33 KB | Phase 5 (cross-validation reads all) |
| `p2-gemini.md` | ~27 KB | Phase 5 (cross-validation reads all) |
| `p2-chatgpt.md` | ~24 KB | Phase 5 (cross-validation reads all) |
| `p2-grok.md` | ~16 KB | Phase 5 (cross-validation reads all) |
| `p3-briefing.md` (created by orchestrator) | ~69 KB | Phase 6 (writes it, stays in context) |
| `report.md` (verification read) | ~38 KB | Phase 7 (reads to verify) |
| `content_plan.md` (verification read) | ~50 KB | Phase 8 (reads to verify) |
| Synthesis agent definition | 14 KB | Phase 7 (loaded via Task) |
| Episode planner skill | 14 KB | Phase 8 (loaded via Skill) |
| **Total accumulated** | **~440 KB** | |

At ~4 chars/token, that's **~110K tokens** of content alone, not counting tool call overhead, task tracking, user messages, and the system prompt. The context fills up, earlier phases get compressed or evicted, and the orchestrator loses track of state.

**The critical bottlenecks are:**

1. **Phase 3 (Question Discovery):** Orchestrator reads entire `p2-perplexity.md` (~67KB) to analyze gaps and create targeted prompts
2. **Phase 5 (Cross-Validation):** Orchestrator reads ALL 5 p2-*.md files (~167KB) to build verification matrix
3. **Phase 6 (Master Briefing):** Orchestrator reads all p2-*.md files AGAIN to create p3-briefing.md (~69KB), which then also stays in context
4. **Phase 7 (Synthesis):** The synthesis-writer agent reads p3-briefing.md + all p2-*.md files (~238KB) into its own context
5. **Phase 8 (Episode Planning):** Runs in the main context, reading report.md + p3-briefing.md (~107KB)

**Desired outcome:**

The orchestrator never loads raw research content into its own context. Instead, it delegates token-heavy work to purpose-built Opus sub-agents and receives only compact summaries back. Research digests provide a searchable index, and individual research files can be queried via parallel Opus sub-agents when specific questions arise. Quality is the priority — cost optimization experiments can follow once the workflow is validated (see GitHub issue #18).

## Appetite

**Size:** Medium

**Team:** Solo dev

**Interactions:**
- PM check-ins: 1 (scope alignment on which phases to sub-agent)
- Review rounds: 1 (validate the new workflow works end-to-end on next episode)

## Prerequisites

No prerequisites — this is a refactoring of existing skill/agent definitions. All tools and infrastructure already exist.

## Solution

### Design Principle: Orchestrator as Dispatcher

The orchestrator's job changes from "read everything, do everything" to "dispatch work, receive summaries, make decisions." It should never read a raw research file (p2-*.md) directly. Instead:

- **For quick lookups:** Check the research digests (~3-5KB each, always available in orchestrator)
- **For targeted questions about a research file:** Spin up an Opus sub-agent that reads that one file and answers the specific question
- **For synthesis/analysis across files:** Spin up a dedicated Opus sub-agent that reads the files and returns a compact result
- **For verification checks:** Spin up an Opus sub-agent that reads the output and confirms criteria are met

### Key Elements

- **Research Digest Agent (Opus):** After each research file is collected, produces a structured ~3-5KB digest (table of contents, key findings, notable sources, unique angles). Makes research content searchable without loading raw files. Runs once per p2-*.md file.
- **Research File Q&A Agent (Opus):** Reads a single p2-*.md file and answers a specific question. Fast, parallelizable. Can run 5 in parallel to answer the same question across all research files.
- **Question Discovery Agent (Opus):** Replaces Phase 3 in-context work. Reads p2-perplexity.md, produces structured gap analysis + targeted prompts for Phase 4 tools.
- **Cross-Validation Agent (Opus):** Replaces Phase 5 in-context work. Reads all p2-*.md files, produces verification matrix + coverage map as compact output. Cross-validation requires comparing subtle contradictions across sources — Opus ensures nothing is missed.
- **Master Briefing Agent (Opus):** Replaces Phase 6 in-context work. Reads all p2-*.md files, writes p3-briefing.md directly to disk. Returns only a summary to the orchestrator. Empirically validated: Opus handles all 12 Wave 1 sections reliably in a single pass (tested on ep5 and ep6 with 100% section completeness).
- **Briefing Validator (Opus):** Checks that p3-briefing.md meets Wave 1 exit criteria without loading the full file into orchestrator context. Safety net only — master briefing agent has 100% success rate on existing episodes.
- **Episode Planner Agent (Opus):** Replaces Phase 8 in-context work. Reads report.md + p3-briefing.md, writes content_plan.md. Returns only a summary. Episode planning is architecturally complex creative work (counterpoint design, mode-switching, depth budgets) — Opus ensures structural quality.
- **Plan Validator (Opus):** Checks that content_plan.md meets Wave 2 exit criteria.
- **Metadata Agent (Opus):** Replaces Phase 11 metadata creation. Reads report.md + transcript, writes logs/metadata.md.

### Flow

**Phase 1-2: Setup & Perplexity** (unchanged — lightweight, no sub-agent needed)

**Orchestrator** → setup_episode.py → directory created → Perplexity API skill → p2-perplexity.md saved

**Phase 2.5: Research Digest** (NEW: after each research file is collected)

Each time a p2-*.md file is saved, **Orchestrator** spawns a **Research Digest Agent** (Opus) that reads the file and produces a structured digest (~3-5KB) saved alongside as `p2-*-digest.md`. Contains: table of contents, key findings summary, notable sources, unique angles not found elsewhere, and searchable topic index. These digests serve as the orchestrator's "index" into the research — it reads digests, not raw files.

**Phase 3: Question Discovery** (NEW: delegated)

**Orchestrator** → spawns **Question Discovery Agent** (Opus, reads p2-perplexity.md) → returns structured gap analysis (~2-3KB) + 4 targeted prompts → **Orchestrator** displays manual prompts, launches automated research

**Phase 4: Targeted Research** (unchanged — already uses external tools/skills, digests generated per file)

**Phase 5: Cross-Validation** (NEW: delegated)

**Orchestrator** → spawns **Cross-Validation Agent** (Opus, reads all p2-*.md) → returns verification matrix + coverage map (~3-5KB) → **Orchestrator** reviews compact summary, decides if more research needed

**Phase 6: Master Briefing** (NEW: delegated)

**Orchestrator** → spawns **Master Briefing Agent** (Opus, reads all p2-*.md + cross-validation summary from Phase 5, writes p3-briefing.md to disk) → returns summary of findings (~2-3KB) → **Orchestrator** spawns **Briefing Validator** (Opus, reads p3-briefing.md, checks Wave 1 criteria) → returns pass/fail with details. On failure (rare — 0% failure rate on ep5/ep6), re-run the master briefing agent with the specific missing sections noted.

**Phase 7: Synthesis** (KEPT: synthesis-writer reads all research for maximum quality)

**Orchestrator** → spawns **podcast-synthesis-writer** (Opus) → agent reads p3-briefing.md + ALL p2-*.md files (repetition across sources reinforces important findings — this is intentional) → writes report.md → **Orchestrator** spawns **Opus verifier** to check report.md size/structure instead of reading it

**Phase 8: Episode Planning** (NEW: delegated)

**Orchestrator** → spawns **Episode Planner Agent** (Opus, reads `.claude/skills/podcast-episode-planner/SKILL.md` + `docs/templates/content_plan-enhanced.md` for full Wave 2 methodology, then reads report.md + p3-briefing.md + sources.md, writes content_plan.md) → returns summary → **Orchestrator** spawns **Plan Validator** (Opus, checks Wave 2 criteria) → returns pass/fail

**Phase 9-10: Audio** (unchanged — external tools)

**Phase 11: Publishing** (NEW: partially delegated)

**Orchestrator** → spawns **Metadata Agent** (Opus, reads report.md + transcript + p3-briefing.md, writes logs/metadata.md) → returns metadata summary → **Orchestrator** runs companion resource scripts + update_feed.py + validator

**Phase 12: Commit** (unchanged — lightweight git operations)

### Technical Approach

**1. New agent definitions in `.claude/agents/`:**

Create focused agent definitions for each sub-agent type:

- `research-digest.md` — Opus agent. Reads a single p2-*.md file, produces structured digest (~3-5KB) with TOC, key findings, notable sources, unique angles, searchable topic index.
- `research-qa.md` — Opus agent. Reads a single p2-*.md file and answers a specific question.
- `question-discovery.md` — Opus agent. Reads p2-perplexity.md, outputs structured gap analysis.
- `cross-validator.md` — Opus agent. Reads all p2-*.md, outputs verification matrix.
- `master-briefing-writer.md` — Opus agent. Reads all research + cross-validation summary, writes p3-briefing.md.
- `briefing-validator.md` — Opus agent. Reads p3-briefing.md, checks Wave 1 criteria.
- `episode-planner.md` — Opus agent. Reads SKILL.md methodology + report.md + sources, writes content_plan.md.
- `plan-validator.md` — Opus agent. Reads content_plan.md, checks Wave 2 criteria.
- `metadata-writer.md` — Opus agent. Reads episode files, writes logs/metadata.md.

**Model policy:** All sub-agents use Opus. Quality is the priority for the initial implementation — every sub-agent gets the same model as the orchestrator to ensure no quality regression from the refactor. Cost optimization (selectively downgrading specific agents to Sonnet) is tracked as a separate experiment (see GitHub issue #18).

**2. Update `new-podcast-episode.md`:**

Replace inline instructions for Phases 3, 5, 6, 8, 11 with sub-agent dispatch instructions. The orchestrator:
- Spawns sub-agents via Task tool with appropriate `subagent_type` and `model`
- Receives compact summaries (target: <3KB per sub-agent response)
- Makes go/no-go decisions based on summaries
- Never reads p2-*.md, p3-briefing.md, report.md, or content_plan.md directly

**3. Parallel Q&A pattern (Opus):**

When the orchestrator needs to know something specific about research files (e.g., "Does any research file mention X?"), it can:
- **First:** Check the research digests (~3-5KB each, can be loaded into orchestrator)
- **If deeper answer needed:** Spawn N parallel Opus agents, one per research file:

```
Task(model=opus, prompt="Read {file} and answer: {question}")
```

This keeps the orchestrator lean while ensuring quality answers. The digest layer means most questions can be answered without even spawning Q&A agents.

**4. Summary contracts:**

Each sub-agent returns a structured summary the orchestrator can parse:

```markdown
## Summary
- Key findings: [3-5 bullet points]
- Gaps identified: [list]
- Contradictions: [list]
- Recommendation: [proceed / needs more research]

## Files Written
- research/p3-briefing.md (68KB, 15 sections)

## Exit Criteria Check
- [x] Depth Distribution Analysis present
- [x] Story Bank (4 stories)
- [ ] Counterpoint Discovery (MISSING - only 1 found)
```

### Estimated Token Savings

| Phase | Current (orchestrator context) | Proposed (orchestrator context) | Savings |
|-------|-------------------------------|--------------------------------|---------|
| Phase 3 | +67KB (reads perplexity) | +3KB (receives summary) | -64KB |
| Phase 5 | +167KB (reads all p2-*) | +5KB (receives matrix) | -162KB |
| Phase 6 | +167KB (reads all p2-* again) | +3KB (receives summary) | -164KB |
| Phase 7 | +38KB (reads report to verify) | +1KB (receives pass/fail) | -37KB |
| Phase 8 | +107KB (reads report + briefing) | +2KB (receives summary) | -105KB |
| Phase 11 | +50KB (reads report + transcript) | +2KB (receives summary) | -48KB |
| **Total orchestrator** | **~596KB accumulated** | **~16KB accumulated** | **-580KB (~97%)** |

The work still gets done — it just happens in isolated sub-agent contexts that don't pollute the orchestrator.

## Rabbit Holes

- **Don't create a generic "research agent framework"** — Each sub-agent is a focused, single-purpose prompt. Don't abstract this into a configurable system.
- **Don't try to make sub-agents resume-able** — These are fire-and-forget. If one fails, re-run it. Don't build state management.
- **Don't limit the synthesis-writer's access to research files** — It benefits from reading ALL p2-*.md files. When multiple research sources mention the same finding, the repetition reinforces what's important. The synthesis-writer already runs in its own isolated context, so its token usage doesn't affect the orchestrator.
- **Don't break up the master briefing agent into per-section agents** — Empirical testing on ep5 and ep6 shows the Opus agent handles all 12 Wave 1 sections reliably in a single pass with 100% completeness. Breaking it up would add complexity to solve a problem that doesn't exist.
- **Don't refactor the skill file format** — The 77KB skill file is large but loads once. The real problem is the accumulated research content, not the instructions.
- **Don't optimize model costs in this plan** — Use Opus for everything first. Get the architecture right, validate end-to-end, then experiment with selectively downgrading specific agents to Sonnet. Premature cost optimization risks introducing quality regressions that are hard to attribute. See GitHub issue #18 for the cost optimization experiments.

## Risks

### Risk 1: Sub-agent quality degradation
**Impact:** Sub-agents in isolated contexts might miss nuances that the orchestrator would catch when holding all context.
**Mitigation:** All sub-agents use Opus — same model as the orchestrator, eliminating model-capability as a variable. Each sub-agent gets a fresh, uncluttered context dedicated to its task, which may actually improve quality over the current approach where the orchestrator's context is polluted with 400KB+ of accumulated content. Include specific quality criteria in each agent prompt. Validate outputs against Wave 1/2 exit criteria.

### Risk 2: Orchestrator loses "big picture" awareness
**Impact:** Without reading research files, the orchestrator can't make judgment calls about research quality or coverage.
**Mitigation:** Sub-agents return structured summaries with explicit recommendations (proceed/stop). The orchestrator still makes decisions — it just reads summaries instead of raw files. Research digests provide a searchable index, and for edge cases, the Opus Q&A pattern lets it ask targeted follow-up questions.

### Risk 3: Increased latency from sequential sub-agent calls
**Impact:** Each sub-agent spawn adds latency (model warmup, file reads, response generation).
**Mitigation:** Parallelize where possible (e.g., 5 digest agents in parallel after research collection, or 5 Q&A agents in parallel for cross-file questions). Most sub-agents replace work that was already sequential. The cross-validation agent might take slightly longer than inline reads, but it saves the orchestrator from context overflow.

## No-Gos (Out of Scope)

- Not changing the 12-phase workflow structure itself
- Not limiting the synthesis-writer's access to research files (it deliberately reads everything)
- Not modifying the research tool skills (perplexity, gpt-researcher, gemini)
- Not building new Python tooling — this is purely skill/agent definition changes
- Not changing the audio generation, processing, or publishing phases (9-12) beyond metadata
- Not reducing the skill file size (77KB) — that loads once and is fine

## Update System

No update system changes required — this only modifies files in `.claude/agents/` and `.claude/skills/` which are part of the repo.

## Agent Integration

No agent integration required — this is a restructuring of the podcast workflow's internal agent architecture. No MCP servers or bridge changes needed.

## Documentation

### Feature Documentation
- [ ] Update `.claude/skills/new-podcast-episode.md` with sub-agent dispatch instructions
- [ ] Create new agent definitions in `.claude/agents/`
- [ ] Update `CLAUDE.md` workflow documentation section if needed

### Inline Documentation
- [ ] Each new agent definition includes clear input/output contracts
- [ ] Summary contract format documented in orchestrator instructions

## Success Criteria

- [ ] Orchestrator never reads a p2-*.md file directly during the workflow
- [ ] Orchestrator never reads p3-briefing.md, report.md, or content_plan.md directly (uses validators)
- [ ] Research digests generated for each p2-*.md file (~3-5KB each, saved as p2-*-digest.md)
- [ ] Phase 3 (question discovery) runs as a dedicated sub-agent returning <5KB
- [ ] Phase 5 (cross-validation) runs as a dedicated sub-agent returning <5KB
- [ ] Phase 6 (master briefing) runs as a dedicated sub-agent writing to disk + returning <5KB
- [ ] Phase 8 (episode planning) runs as a dedicated sub-agent writing to disk + returning <5KB
- [ ] Wave 1 and Wave 2 exit criteria validated by Opus validator agents, not orchestrator reads
- [ ] All sub-agents use Opus (no Sonnet or Haiku in the research pipeline)
- [ ] Synthesis-writer retains full access to all p2-*.md files (no input reduction)
- [ ] End-to-end workflow completes successfully on a real episode
- [ ] Orchestrator context stays under ~30KB of accumulated content throughout all 12 phases

## Team Orchestration

### Team Members

- **Builder (agent-definitions)**
  - Name: agent-author
  - Role: Create all new agent definitions in .claude/agents/
  - Agent Type: agent-architect
  - Resume: true

- **Builder (workflow-update)**
  - Name: workflow-updater
  - Role: Rewrite new-podcast-episode.md phases 3, 5, 6, 8, 11 to use sub-agent dispatch
  - Agent Type: builder
  - Resume: true

- **Validator (workflow)**
  - Name: workflow-validator
  - Role: Verify the updated workflow is internally consistent and all sub-agents are properly referenced
  - Agent Type: validator
  - Resume: true

## Step by Step Tasks

### 1. Create research digest agent definition
- **Task ID**: build-research-digest-agent
- **Depends On**: none
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/research-digest.md` — Opus agent for per-file digests
- Input: single p2-*.md file path
- Output: structured digest (~3-5KB) saved as `p2-*-digest.md` with: table of contents, key findings (5-10 bullets), notable sources with quality ratings, unique angles not likely in other sources, searchable topic index
- Digest serves as "index card" — orchestrator reads digests instead of raw files

### 2. Create research Q&A agent definition
- **Task ID**: build-research-qa-agent
- **Depends On**: none
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/research-qa.md` — Opus agent for single-file Q&A
- Include input contract (file path + question) and output contract (direct answer, <500 tokens)

### 3. Create question discovery agent definition
- **Task ID**: build-question-discovery-agent
- **Depends On**: none
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/question-discovery.md` — Opus agent for Phase 3
- Input: p2-perplexity.md path + episode topic
- Output: structured gap analysis + 4 targeted prompts (<3KB)

### 4. Create cross-validation agent definition
- **Task ID**: build-cross-validation-agent
- **Depends On**: none
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/cross-validator.md` — Opus agent for Phase 5
- Input: episode directory path
- Output: verification matrix + coverage map (<5KB)

### 5. Create master briefing writer agent definition
- **Task ID**: build-briefing-writer-agent
- **Depends On**: build-cross-validation-agent
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/master-briefing-writer.md` — Opus agent for Phase 6
- Input: episode directory path + enhanced template reference + cross-validation summary (verification matrix + coverage map from Phase 5)
- Output: writes p3-briefing.md to disk, returns summary (<3KB)
- Must enforce Wave 1 template requirements
- The cross-validation summary gives the agent a head start on contradictions, coverage gaps, and areas needing emphasis — avoiding redundant re-discovery from raw files

### 6. Create briefing/plan validator agent definitions
- **Task ID**: build-validator-agents
- **Depends On**: none
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/briefing-validator.md` — Opus agent for Wave 1 exit criteria
- Create `.claude/agents/plan-validator.md` — Opus agent for Wave 2 exit criteria
- Input: file path
- Output: structured pass/fail checklist (<1KB)

### 7. Create episode planner agent definition
- **Task ID**: build-episode-planner-agent
- **Depends On**: none
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/episode-planner.md` — Opus agent for Phase 8
- **CRITICAL: Agent must read full Wave 2 methodology at runtime** — instruct agent to read `.claude/skills/podcast-episode-planner/SKILL.md` (14KB) and `docs/templates/content_plan-enhanced.md` before planning. The methodology contains toolkit selection, mode-switching framework, counterpoint design, depth budgets, and signposting language that are essential for content_plan quality. Do NOT attempt to summarize the methodology in the agent definition — the agent must read the full source files.
- Input: episode directory path (agent reads SKILL.md + template + report.md + p3-briefing.md + sources.md)
- Output: writes content_plan.md, returns summary (<3KB)

### 8. Create metadata writer agent definition
- **Task ID**: build-metadata-agent
- **Depends On**: none
- **Assigned To**: agent-author
- **Agent Type**: agent-architect
- **Parallel**: true
- Create `.claude/agents/metadata-writer.md` — Opus agent for Phase 11
- Input: episode directory path + metadata template reference
- Output: writes logs/metadata.md, returns summary (<2KB)

### 9. Rewrite new-podcast-episode.md
- **Task ID**: build-workflow-update
- **Depends On**: build-research-digest-agent, build-research-qa-agent, build-question-discovery-agent, build-cross-validation-agent, build-briefing-writer-agent, build-validator-agents, build-episode-planner-agent, build-metadata-agent
- **Assigned To**: workflow-updater
- **Agent Type**: builder
- **Parallel**: false
- Rewrite Phases 3, 5, 6, 7 (verification only), 8, 11 to use sub-agent dispatch
- Replace all "Read p2-*.md" instructions with sub-agent spawning
- Add summary contract expectations for orchestrator
- Preserve all exit criteria (delegate checking to validators)
- Keep Phases 1, 2, 4, 9, 10, 12 unchanged

### 10. Validate workflow consistency
- **Task ID**: validate-workflow
- **Depends On**: build-workflow-update
- **Assigned To**: workflow-validator
- **Agent Type**: validator
- **Parallel**: false
- Verify all sub-agent references in new-podcast-episode.md match actual agent definitions
- Verify exit criteria are still enforced (via validators, not inline reads)
- Verify no phase instructs the orchestrator to read a raw research file
- Verify summary contracts are consistent across agents
- Run validation checks

## Validation Commands

- `grep -c "Read.*p2-" .claude/skills/new-podcast-episode.md` — should be 0 (orchestrator never reads p2-* files)
- `ls .claude/agents/research-digest.md .claude/agents/research-qa.md .claude/agents/question-discovery.md .claude/agents/cross-validator.md .claude/agents/master-briefing-writer.md .claude/agents/briefing-validator.md .claude/agents/plan-validator.md .claude/agents/episode-planner.md .claude/agents/metadata-writer.md` — all exist
- `grep -c "subagent_type\|Task tool\|model.*opus" .claude/skills/new-podcast-episode.md` — should show multiple sub-agent dispatch points

---

## Resolved Design Decisions

These were open questions during planning, now resolved:

1. **Synthesis-writer keeps full research access.** It reads p3-briefing.md + ALL p2-*.md files. When multiple research sources mention the same finding, the repetition reinforces what matters. This runs in an isolated sub-agent context, so token usage doesn't affect the orchestrator. Don't limit its potential.

2. **All sub-agents use Opus.** Quality is the priority for the initial implementation. Every sub-agent gets the same model as the orchestrator — this ensures the refactor cannot introduce quality regressions from model capability differences. Cost optimization (selectively downgrading specific agents to Sonnet where quality is comparable) is tracked separately in GitHub issue #18.

3. **Research digests are a standard step, not ad-hoc.** After each p2-*.md file is collected, an Opus digest agent produces a ~3-5KB structured summary saved as `p2-*-digest.md`. This serves as a table of contents / index card for each research file, making the content searchable without loading raw files. The orchestrator reads digests (predictable, compact) rather than spawning ad-hoc Q&A agents (unpredictable, expensive).

4. **Validator failure = simple retry of the same agent.** If the briefing validator reports a missing section, re-run the master briefing writer with the failure details. This is a safety net, not a frequent event — empirical testing on ep5 and ep6 shows 100% Wave 1 section completeness from the master briefing agent. Breaking the briefing into per-section sub-agents would solve a problem that doesn't exist and add unnecessary complexity. The agents are smart enough; if they ever fail, it's better to retry than to fragment the work.
