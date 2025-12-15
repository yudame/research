# New Podcast Episode Workflow Improvements

**Purpose:** Document improvements to `.claude/skills/new-podcast-episode.md` to make it easier to follow and prevent missing critical steps (like the git push in Phase 10).

**Context:** During Episode 6 creation, the workflow was followed correctly through Phase 9 (commit), but Phase 10 (push to GitHub) was missed, requiring manual intervention. This document outlines improvements to prevent similar issues.

---

## Problem Statement

**What happened:**
- Workflow completed through Phase 9 (git commit)
- Phase 10 (git push) was not executed
- Episode remained local and didn't deploy to GitHub Pages
- User had to manually push and question why it wasn't included

**Root cause:**
- Long, complex workflow file (1200+ lines)
- No clear visual hierarchy of critical vs optional steps
- Missing completion criteria for each phase
- No verification that each phase succeeded
- Easy to lose track of where you are in multi-phase workflow

**Goal:** Make it impossible to miss critical steps while maintaining workflow completeness.

---

## Proposed Improvements

### 1. Add Phase Progress Tracker at Top

**Location:** After title, before Phase 1

**Implementation:**
```markdown
## Quick Reference: Episode Workflow Status

Track your progress through the workflow. Check off each phase as you complete it.

- [ ] **Phase 1: Setup** → Directory created, prompts.md initialized
- [ ] **Phase 2: Research** → All research tools completed, results in research-results.md
- [ ] **Phase 3: Validation** → research-briefing.md populated with cross-validated findings
- [ ] **Phase 4: Synthesis** → report.md created by podcast-synthesis-writer agent
- [ ] **Phase 5: Cover Art** → cover.png generated and branded
- [ ] **Phase 6: NotebookLM** → User completes (audio file ready)
- [ ] **Phase 7: Audio Processing** → mp3 converted, transcribed, chaptered, embedded
- [ ] **Phase 8: Publishing** → feed.xml updated with episode metadata
- [ ] **Phase 9: Git Commit** → Changes committed with descriptive message
- [ ] **Phase 10: PUSH TO GITHUB** → `git push` executed, live in 2-3 min ⚠️ CRITICAL

**⚠️ WORKFLOW IS NOT COMPLETE UNTIL PHASE 10 (PUSH) IS DONE**

**Verification:** After Phase 10, check https://research.yuda.me/podcast/feed.xml refreshes with new episode in 2-3 minutes.
```

**Benefits:**
- Always visible at top of file
- Clear definition of "done" for entire workflow
- Visual reminder that push is required
- Easy to see where you are in the process

---

### 2. Use Clear Visual Phase Boundaries

**Current state:** Simple markdown headers
**Problem:** Phases blend together visually
**Solution:** Use ASCII art separators

**Implementation:**
```markdown
═══════════════════════════════════════════════════════════════
                    PHASE 7: AUDIO PROCESSING
═══════════════════════════════════════════════════════════════

**Trigger:** User provides audio file from NotebookLM
**Output:** Processed mp3 with chapters, transcript, metadata
**Critical Next Step:** → Phase 8 (Publishing)

**CHECKLIST:**
- [ ] Convert m4a to mp3 (if needed)
- [ ] Get file metadata (duration, size in bytes)
- [ ] Transcribe with Whisper base model
- [ ] Analyze transcript and create 10-15 chapters
- [ ] Embed chapters into mp3
- [ ] Log to prompts.md

═══════════════════════════════════════════════════════════════
```

**Benefits:**
- Impossible to miss phase transitions
- Clear trigger/output/next-step for each phase
- Built-in checklist for phase steps
- Easy to scan and find current phase

---

### 3. Add Exit Criteria for Each Phase

**Problem:** Unclear when a phase is truly "complete"
**Solution:** Explicit exit criteria that must ALL be true

**Implementation:**
```markdown
### Phase 8: Publishing Metadata

**ENTRY REQUIREMENTS:**
✓ Audio file processed (Phase 7 complete)
✓ Duration known (MM:SS format)
✓ File size known (exact bytes)
✓ Transcript exists

**WORK TO DO:**
[... existing phase content ...]

**EXIT CRITERIA (all must be true to proceed):**
✓ Episode description written (1-2 sentences + report link + key sources)
✓ Keywords generated (5-10 episode-specific terms)
✓ Key sources validated (3-5 Tier 1/2 sources with working URLs)
✓ feed.xml updated with new <item> entry
✓ lastBuildDate updated in feed.xml channel metadata
✓ All metadata accurate (duration matches file, size matches file, pubDate is RFC 2822)

**⚠️ DO NOT PROCEED TO PHASE 9 UNTIL ALL EXIT CRITERIA MET**

**Verification command:**
```bash
# Check feed.xml was updated
git diff podcast/feed.xml | head -50
```
```

**Benefits:**
- Clear definition of "done" for each phase
- Prevents moving forward with incomplete work
- Built-in verification commands
- Catches errors early (before they compound)

---

### 4. Highlight Critical Steps with Visual Markers

**Problem:** All steps look equally important
**Solution:** Use emoji and visual markers for critical/commonly-missed steps

**Implementation:**
```markdown
### 10. Git Workflow

**Commit and push the episode:**

1. Check status and review changes:
   ```bash
   git status
   git diff feed.xml
   ```

2. Add all episode files and updated feed:
   ```bash
   git add podcast/feed.xml podcast/episodes/YYYY-MM-DD-slug/
   ```

3. Commit with descriptive message using heredoc:
   ```bash
   git commit -m "$(cat <<'EOF'
   feat: Add episode on [topic]
   ...
   EOF
   )"
   ```

   **VERIFY COMMIT SUCCEEDED:**
   ```bash
   git log -1 --oneline  # Should show your commit message
   git status            # Should show "nothing to commit, working tree clean"
   ```

4. 🚨 **CRITICAL: Push to GitHub** 🚨
   ```bash
   git push
   ```

   **⚠️ COMMON MISTAKE:** Stopping after commit without pushing

   **WHY THIS MATTERS:** Without push, episode stays local and NEVER goes live on GitHub Pages

   **VERIFY PUSH SUCCEEDED:**
   ```bash
   git log -1 --oneline                    # Note the commit hash
   git ls-remote origin main | grep main   # Hash should match
   ```

   **Expected output:** `[commit-hash] refs/heads/main`

   **If hashes don't match:** Your push didn't work. Run `git push` again.

5. ✅ **FINAL VERIFICATION: Episode is Live**

   Wait 2-3 minutes, then check:
   ```bash
   curl -s https://research.yuda.me/podcast/feed.xml | grep "episode-6-smartphone-frontier"
   ```

   **Expected:** Should return the episode title and enclosure URL

   **If not found:** Check GitHub Actions for deployment errors

**UPDATE TODOS:**
```
Mark "Update feed.xml and commit" as completed.
Mark "Push to GitHub" as completed.
ALL EPISODE WORKFLOW TASKS COMPLETE! ✅
```
```

**Benefits:**
- Impossible to miss critical push step
- Clear explanation of why it matters
- Verification commands prove it worked
- Final check that episode is actually live

---

### 5. Add Decision Trees for Complex Choices

**Problem:** Unclear when to use Task tool vs direct tools
**Solution:** Visual decision tree

**Implementation:**
```markdown
### When to Use Task Tool vs Direct Tools

**Decision Tree:**

```
┌─────────────────────────────────────────┐
│ What kind of work needs to be done?     │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴────────────┐
       │                    │
   RESEARCH            FILE OPERATIONS
       │                    │
       │                    ├─ Read specific file path?
       │                    │  → Use Read tool directly
       │                    │
       │                    ├─ Edit specific file?
       │                    │  → Use Edit tool directly
       │                    │
       │                    ├─ Search for pattern in files?
       │                    │  → Use Grep tool directly
       │                    │
       │                    └─ Run terminal command?
       │                       → Use Bash tool directly
       │
       ├─ Multi-round exploration?
       │  (e.g., "Where are errors handled?")
       │  → Use Task tool (Explore agent)
       │
       ├─ Question requires synthesis?
       │  (e.g., "How do these systems interact?")
       │  → Analyze directly with current context
       │
       ├─ Open-ended search across codebase?
       │  (e.g., "Find all authentication code")
       │  → Use Task tool (general-purpose agent)
       │
       └─ Specialized skill needed?
          (e.g., podcast-synthesis-writer)
          → Use Task tool with specific subagent
```

**Examples:**

✅ **USE DIRECT TOOLS:**
- "Read podcast/feed.xml" → Read tool
- "Edit line 42 in config.py" → Edit tool
- "Search for 'TODO' in all files" → Grep tool
- "Run git status" → Bash tool

✅ **USE TASK TOOL:**
- "Where is user authentication handled?" → Task (Explore)
- "Generate podcast report from research" → Task (podcast-synthesis-writer)
- "Find all database migration code" → Task (Explore)
- "Synthesize research into briefing" → Task (podcast-synthesis-writer)
```

**Benefits:**
- Clear decision criteria
- Prevents over-using Task tool for simple operations
- Prevents under-using Task tool for complex exploration
- Concrete examples for common scenarios

---

### 6. Add File State Indicators

**Problem:** Unclear what files should exist at each phase
**Solution:** File state checklist before/after each phase

**Implementation:**
```markdown
### Phase 4: Synthesis

**BEFORE STARTING THIS PHASE - Verify File State:**

Run verification:
```bash
ls -lh podcast/episodes/YYYY-MM-DD-slug/ | grep -E "research-briefing|research-results|sources"
```

**Required files (must exist):**
- ✓ research-briefing.md (should be 15-30KB with validated findings)
- ✓ research-results.md (should be 50-200KB with raw research)
- ✓ sources.md (should list 30+ sources in 3 tiers)
- ✓ prompts.md (should have all research prompts logged)

**If any missing:** Go back and complete earlier phases

**WORK:** [... phase content ...]

**AFTER COMPLETING THIS PHASE - Verify File State:**

Run verification:
```bash
ls -lh podcast/episodes/YYYY-MM-DD-slug/report.md
wc -w podcast/episodes/YYYY-MM-DD-slug/report.md
```

**New files created:**
- ✓ report.md exists
- ✓ report.md is 15-25KB (~5,000-8,000 words)
- ✓ report.md has narrative structure (not bullet points)
- ✓ All claims have source citations

**Validation:**
```bash
grep -c "http" podcast/episodes/YYYY-MM-DD-slug/report.md
# Should return 20+ (indicating sufficient citations)
```
```

**Benefits:**
- Prevents starting a phase with missing prerequisites
- Catches file creation failures immediately
- Provides size/content sanity checks
- Easy to verify before proceeding

---

### 7. Create Phase Dependency Map

**Problem:** Unclear which phases can run in parallel vs must be sequential
**Solution:** Visual dependency diagram at top

**Implementation:**
```markdown
## Workflow Phase Dependencies

**Understanding the flow:**
- Phases in the same column can potentially run in parallel
- Arrows (↓) show required sequential dependencies
- 🔴 indicates user action required
- 🚨 indicates critical step that's commonly missed

```
┌──────────────────┐
│  Phase 1: Setup  │
│  (Directory)     │
└────────┬─────────┘
         ↓
┌────────────────────────────────┐
│  Phase 2: Research             │
│  (Perplexity → Analysis →      │
│   Grok/GPT/Gemini/Claude)      │
│  ⚠️ Can parallelize within      │
└────────┬───────────────────────┘
         ↓
┌────────────────────────────────┐
│  Phase 3: Validation           │
│  (Cross-validate all sources)  │
│  ⚠️ Requires ALL research done  │
└────────┬───────────────────────┘
         ↓
┌────────────────────────────────┐
│  Phase 4: Synthesis            │
│  (podcast-synthesis-writer)    │
│  ⚠️ Requires research-briefing  │
└────────┬───────────────────────┘
         ↓
         ├──────────────────┬─────────────────┐
         ↓                  ↓                 ↓
┌─────────────────┐  ┌──────────────┐  ┌─────────────┐
│ Phase 5:        │  │ Phase 6:     │  │ (Optional)  │
│ Cover Art       │  │ NotebookLM   │  │ Validate    │
│ (AI + branding) │  │ 🔴 USER      │  │ report.md   │
└────────┬────────┘  └──────┬───────┘  └─────────────┘
         │                  │
         └──────────┬───────┘
                    ↓
         ┌──────────────────────┐
         │  Phase 7: Audio      │
         │  Processing          │
         │  (Convert, Whisper,  │
         │   chapters, embed)   │
         └──────────┬───────────┘
                    ↓
         ┌──────────────────────┐
         │  Phase 8: Publishing │
         │  (Description,       │
         │   keywords, feed)    │
         └──────────┬───────────┘
                    ↓
         ┌──────────────────────┐
         │  Phase 9: Commit     │
         │  (git add + commit)  │
         └──────────┬───────────┘
                    ↓
         ┌──────────────────────┐
         │  Phase 10: PUSH      │
         │  🚨 CRITICAL         │
         │  (git push)          │
         └──────────┬───────────┘
                    ↓
         ┌──────────────────────┐
         │  ✅ LIVE ON GITHUB   │
         │  (2-3 min deploy)    │
         └──────────────────────┘
```

**Key insights:**
- Phases 5 & 6 can run in parallel (cover art while waiting for NotebookLM)
- Phase 7 is BLOCKED until user provides audio
- Phases 8-10 must be strictly sequential
- Phase 10 is CRITICAL - workflow not done without it
```

**Benefits:**
- Visual understanding of workflow structure
- Clear which phases block others
- Identifies parallelization opportunities
- Highlights critical path to completion

---

### 8. Add Common Failure Modes & Solutions

**Problem:** When things go wrong, unclear how to fix
**Solution:** Troubleshooting section for each phase

**Implementation:**
```markdown
### Phase 10: Git Workflow - Common Issues

**❌ Problem:** `git commit` fails with "nothing to commit, working tree clean"

**Diagnosis:**
```bash
git status  # Check what's staged
```

**Solution:**
1. Verify files were added: `git status` should show files in "Changes to be committed"
2. If files are untracked: Run `git add podcast/episodes/YYYY-MM-DD-slug/`
3. If files are modified but not staged: Run `git add -u`
4. Then retry: `git commit -m "..."`

---

**❌ Problem:** `git push` fails with "Updates were rejected"

**Error message:**
```
! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'origin'
```

**Diagnosis:**
```bash
git log origin/main..main  # Show commits you have that remote doesn't
git log main..origin/main  # Show commits remote has that you don't
```

**Solution:**
```bash
git pull --rebase origin main  # Rebase your commit on top of remote
git push                       # Should now succeed
```

---

**❌ Problem:** `feed.xml` validation fails - duration mismatch

**Error:** "Duration in feed.xml (36:50) doesn't match file (36:49)"

**Solution:**
1. Get exact duration: `ffmpeg -i file.mp3 2>&1 | grep Duration`
2. Copy exact value (e.g., "36:49.88" → use "36:49")
3. Update feed.xml `<itunes:duration>36:49</itunes:duration>`
4. Verify: `git diff feed.xml`
5. Recommit: `git add feed.xml && git commit --amend --no-edit`
6. Force push: `git push --force-with-lease`

---

**❌ Problem:** GitHub Pages not deploying after push

**Diagnosis:**
1. Check GitHub Actions: https://github.com/[user]/[repo]/actions
2. Look for failed workflows
3. Check Pages settings: Settings → Pages → Source should be "main" branch

**Solution:**
- If Actions shows failure: Click on failed action to see error log
- Common fix: Re-run the workflow from Actions tab
- If Pages is disabled: Re-enable in Settings → Pages
- Wait full 5 minutes (sometimes takes longer than 2-3 min)

**Verification:**
```bash
# After 5 minutes, check if feed updated
curl -s https://research.yuda.me/podcast/feed.xml | grep "YYYY-MM-DD-slug"
```
```

**Benefits:**
- Immediate solutions when things break
- Reduces context switching to search for solutions
- Builds confidence in recovery procedures
- Prevents workflow abandonment due to errors

---

### 9. Add Verification Commands Throughout

**Problem:** Unclear if each step actually worked
**Solution:** Verification command after every critical operation

**Implementation Example:**
```markdown
2. Convert m4a to mp3:
   ```bash
   ffmpeg -i "audio.m4a" -codec:a libmp3lame -b:a 128k "episode.mp3" -y
   ```

   **VERIFY CONVERSION SUCCEEDED:**
   ```bash
   ls -lh episode.mp3               # Should exist and be ~30-40MB
   ffmpeg -i episode.mp3 2>&1 | grep Duration  # Should show duration
   ```

   **Expected output:**
   ```
   -rw-r--r--  1 user  staff   35.4M Dec 15 08:00 episode.mp3
   Duration: 00:36:49.88, start: 0.025057, bitrate: 128 kb/s
   ```

3. Transcribe with Whisper:
   ```bash
   python transcribe_only.py episode.mp3 --model base
   ```

   **VERIFY TRANSCRIPTION SUCCEEDED:**
   ```bash
   ls -lh episode_transcript.json   # Should exist and be ~300-500KB
   head -20 episode_transcript.json # Should show JSON with "text" and "segments"
   ```

   **Expected output:**
   ```
   -rw-r--r--  1 user  staff   421K Dec 15 08:05 episode_transcript.json
   {
     "text": " Welcome to the Deep Dive...",
     "segments": [
   ```
```

**Benefits:**
- Immediate feedback that step worked
- Catches errors before they cascade
- Provides expected output for comparison
- Builds confidence in process

---

### 10. Create Reusable Templates

**Problem:** Repetitive manual work prone to errors (feed.xml entries)
**Solution:** Template files with placeholders

**Implementation:**

Create `.claude/templates/feed-item-template.xml`:
```xml
<!-- Episode {{EPISODE_NUM}}: {{SERIES_NAME}} - Episode {{SERIES_EP}} -->
<item>
  <title>{{SERIES_NAME}}: Ep. {{SERIES_EP}}, {{EPISODE_TITLE}}</title>
  <itunes:image href="https://research.yuda.me/podcast/episodes/{{SLUG}}/cover.png"/>
  <description>{{DESCRIPTION}}

Full research report: https://research.yuda.me/podcast/episodes/{{SLUG}}/report.md</description>
  <content:encoded><![CDATA[<p>{{DESCRIPTION}}</p><p><strong>Full research report:</strong> <a href="https://research.yuda.me/podcast/episodes/{{SLUG}}/report.md">report.md</a></p><p><strong>Key Sources:</strong></p><ul>{{KEY_SOURCES_HTML}}</ul>]]></content:encoded>
  <author>valor@yuda.me (Valor Engels)</author>
  <pubDate>{{PUBDATE}}</pubDate>
  <enclosure url="https://research.yuda.me/podcast/episodes/{{SLUG}}/{{SLUG}}.mp3"
             length="{{FILE_SIZE}}"
             type="audio/mpeg"/>
  <guid>https://research.yuda.me/podcast/episodes/{{SLUG}}/{{SLUG}}.mp3</guid>
  <itunes:author>Valor Engels</itunes:author>
  <itunes:duration>{{DURATION}}</itunes:duration>
  <itunes:explicit>no</itunes:explicit>
  <itunes:episodeType>full</itunes:episodeType>
  <itunes:season>{{SEASON}}</itunes:season>
  <itunes:episode>{{EPISODE_NUM}}</itunes:episode>
  <itunes:keywords>{{KEYWORDS}}</itunes:keywords>
  <research:series>{{SERIES_NAME}}</research:series>
  <podcast:chapters url="https://research.yuda.me/podcast/episodes/{{SLUG}}/{{SLUG}}_chapters.json" type="application/json+chapters"/>
</item>
```

Update Phase 8 instructions:
```markdown
### Phase 8: Publishing Metadata

Instead of manually constructing feed.xml entry:

1. Use the template:
   ```bash
   cp .claude/templates/feed-item-template.xml /tmp/episode-item.xml
   ```

2. Fill in placeholders (using sed or manual editing):
   - {{EPISODE_NUM}} = 19
   - {{SERIES_NAME}} = Solomon Islands Telecom Series
   - {{SERIES_EP}} = 6
   - {{EPISODE_TITLE}} = The Smartphone Frontier
   - {{SLUG}} = solomon-islands-telecom-series/episode-6-smartphone-frontier
   - {{DESCRIPTION}} = [your 1-2 sentence description]
   - {{PUBDATE}} = Sun, 15 Dec 2025 08:00:00 GMT
   - {{FILE_SIZE}} = 35359483
   - {{DURATION}} = 36:49
   - {{SEASON}} = 1
   - {{KEYWORDS}} = [your keywords]
   - {{KEY_SOURCES_HTML}} = <li>...</li> items

3. Insert into feed.xml after line 29 (after channel metadata, before other episodes)

4. Update channel lastBuildDate
```

**Benefits:**
- Reduces manual typing errors
- Ensures consistent XML structure
- Faster episode publishing
- Less cognitive load remembering all required tags

---

## Implementation Status

### ✅ COMPLETED - Phase 1: Critical Safety Improvements
**Implemented 2025-12-15:**
1. ✅ Quick Reference checklist at top (12 phases with completion criteria)
2. ✅ Visual markers (🚨, ⚠️) for critical steps throughout
3. ✅ Exit criteria for all major phases (1, 7-12)
4. ✅ Verification commands after all critical operations

**Files modified:**
- `.claude/skills/new-podcast-episode.md` - Added Phase Progress Tracker (lines 3-20)
- All major phases updated with entry/exit criteria and verification

**Impact:** Prevents missing ANY critical step (not just git push)

---

### ✅ COMPLETED - Phase 2: Foundational Structure
**Implemented 2025-12-15:**
5. ✅ Visual phase boundaries with ASCII art (all phases 1, 7-12)
6. ✅ File state indicators (Setup phase + Audio Processing)
7. ✅ File organization structure (research/, logs/, tmp/)
8. ✅ Phase-prefixed file naming (p1, p2, p3)

**Files modified:**
- `.claude/skills/new-podcast-episode.md` - Complete restructure
- `.claude/skills/podcast-series.md` - Updated directory examples
- `docs/plans/implementation-summary.md` - Created

**Impact:** Clean, organized episode directories; easy navigation; parallel-safe research

---

### 🔄 PARTIALLY COMPLETED - Phase 3: Error Handling
**Implemented 2025-12-15:**
9. ✅ Common failure modes for critical phases (Phase 10 Audio, Phase 11 Publishing, Phase 12 Git)
10. ⏭️ Templates - SKIPPED (test-first approach, add if Episode 7 shows value)

**Files modified:**
- `.claude/skills/new-podcast-episode.md` - Troubleshooting tables in Phases 10-12

**Impact:** Faster error recovery, reduced troubleshooting time

---

### ⏭️ NOT IMPLEMENTED (By Design)
**The following were not implemented:**
- #5 Decision Trees (Task tool vs direct) - Not critical, added only if user feedback shows confusion
- #7 Phase Dependency Map - Quick Reference tracker achieves same goal
- #10 Reusable Templates - Test with Episode 7 first before creating templates

**Rationale:** Focus on foundational improvements. Add these incrementally based on real-world usage.

---

## Testing Plan

**How to validate improvements work:**

1. **Dry run with new user:**
   - Give workflow file to someone unfamiliar with it
   - Ask them to walk through creating an episode
   - Note where they get confused or stuck
   - Revise based on feedback

2. **Checklist validation:**
   - For next 3 episodes, strictly follow quick reference checklist
   - Verify all exit criteria can be objectively verified
   - Adjust any ambiguous criteria

3. **Error injection testing:**
   - Intentionally break each phase (wrong file path, missing dependency, etc.)
   - Verify troubleshooting section helps recover
   - Add solutions for any new failure modes discovered

4. **Verification command testing:**
   - Run every verification command in a real workflow
   - Confirm expected output matches actual output
   - Update any outdated command syntax

---

### 11. Episode Directory File Organization

**Problem:** Episode directories end up cluttered with 18+ files mixing final outputs, research materials, process logs, and temporary files

**Current state (Episode 1 analysis):**
```
ep1-foundations/
├── [18 files in root directory, 122MB total]
├── 81MB .m4a file (should be gitignored but was committed)
├── Research files mixed with final outputs
├── HTML files with unclear origin
└── Temporary files (chapters.txt) not cleaned up
```

**Solution:** Organize files into purpose-based subdirectories

**Implementation:**

Create subdirectory structure during Phase 1 setup:
```bash
# Phase 1: Setup
mkdir -p podcast/episodes/YYYY-MM-DD-slug/{research,logs,tmp}
```

**File organization rules:**

| File Type | Location | Committed | Purpose |
|-----------|----------|-----------|---------|
| **FINAL/PUBLISHED** (root) | | | |
| `*.mp3` | Root | ✅ Yes | Final audio - linked in feed.xml |
| `*_chapters.json` | Root | ✅ Yes | Podcasting 2.0 metadata - linked in feed.xml |
| `cover.png` | Root | ✅ Yes | Episode artwork - linked in feed.xml |
| `report.md` | Root | ✅ Yes | Narrative report - linked in description |
| `report.html` | Root | ✅ Yes | HTML report - linked from series index.html |
| `transcript.html` | Root | ✅ Yes | HTML transcript - linked from series index.html |
| `sources.md` | Root | ✅ Yes | Source documentation - reference material |
| **RESEARCH FILES** (research/) - **Phase-prefixed for chronological sorting** | | | |
| `p1-brief.md` | research/ | ✅ Yes | Research brief (topic/question) - Phase 1 |
| `p2-perplexity.md` | research/ | ✅ Yes | Perplexity research output - Phase 2 |
| `p2-grok.md` | research/ | ✅ Yes | Grok research output - Phase 2 |
| `p2-chatgpt.md` | research/ | ✅ Yes | ChatGPT research output - Phase 2 |
| `p2-gemini.md` | research/ | ✅ Yes | Gemini research output - Phase 2 |
| `p2-claude.md` | research/ | ✅ Yes | Claude research output - Phase 2 (optional) |
| `p2-manual.md` | research/ | ✅ Yes | Manual research, user sources - Phase 2 |
| `p3-briefing.md` | research/ | ✅ Yes | Cross-validated synthesis for Opus - Phase 3 |
| `p3-validation.md` | research/ | ⚠️ Optional | Cross-validation matrix - Phase 3 |
| `documents/*.pdf` | research/documents/ | ✅ Yes | Source PDFs, papers |
| **PROCESS LOGS** (logs/) | | | |
| `prompts.md` | logs/ | ✅ Yes | All prompts used in workflow |
| `metadata.md` | logs/ | ✅ Yes | Publishing metadata scratch |
| **TEMPORARY FILES** (tmp/) | | | |
| `*_transcript.json` | tmp/ | ⚠️ Optional | Full Whisper output (449KB) |
| `*_chapters.txt` | tmp/ | ❌ No | FFmpeg temp file - delete after embed |
| **NEVER COMMIT** | | | |
| `*.m4a` | - | ❌ No | Source audio - already in .gitignore |

**Naming rationale:**
- **Phase prefixes (p1, p2, p3):** Ensures files sort chronologically in directory listing
- **No "research-" prefix:** Redundant when files are in `/research` directory
- **p1-brief.md:** "Brief" (not "prompt") - prompt is reserved for tool prompts
- **Individual tool files:** Each research tool saves to separate file (no race conditions)
- **Eliminate research-results.md:** Redundant - go directly from individual files to p3-briefing.md

**Phase-specific file placement:**

```markdown
### Phase 1: Setup
**Create directory structure and initial brief:**
```bash
mkdir -p research/documents logs tmp
# User provides or we create: research/p1-brief.md
```

### Phase 2: Research
**Save each tool output to individual file:**
```bash
# Perplexity → research/p2-perplexity.md
# Grok → research/p2-grok.md
# ChatGPT → research/p2-chatgpt.md
# Gemini → research/p2-gemini.md
# Manual sources → research/p2-manual.md
# PDFs/papers → research/documents/
```

**Benefits:**
- ✅ No race conditions (each tool writes to own file)
- ✅ Can run tools in parallel safely
- ✅ Easy to retry individual tool without re-running all
- ✅ Files sort chronologically: p2-chatgpt, p2-gemini, p2-grok, p2-perplexity

### Phase 3: Validation & Synthesis
**Read all p2-*.md files and create synthesis:**
```bash
# Read: research/p2-*.md (all Phase 2 outputs)
# Create: research/p3-briefing.md (cross-validated synthesis for Opus)
# Optional: research/p3-validation.md (validation matrix)
```

### Phase 7: Audio Processing
**Handle temporary files:**
```bash
# After creating chapters.txt and embedding into mp3:
rm YYYY-MM-DD-slug_chapters.txt  # Delete temp file

# Optionally move large transcript to tmp/:
mv YYYY-MM-DD-slug_transcript.json tmp/
```

### Phase 8: Publishing
**Create HTML files in root (for series index):**
```bash
# These ARE needed - linked from series index.html
# report.html → root (created from report.md)
# transcript.html → root (created from transcript.json)
```
```

**Benefits:**
- Root directory: 7 files (down from 18) - only final outputs
- Clear separation of concerns
- 37MB total (down from 122MB after removing .m4a)
- Easy to find files by purpose
- Git-friendly structure

**Verification after cleanup:**
```bash
# Expected root structure
ls -lh podcast/episodes/YYYY-MM-DD-slug/
# Should show: mp3, chapters.json, cover.png, report.md, report.html, transcript.html, sources.md
# Plus: research/, logs/, tmp/ subdirectories

# Verify .m4a not committed
git ls-files | grep ".m4a"
# Should return nothing
```

**HTML file creation (MISSING FROM WORKFLOW):**

Currently `report.html` and `transcript.html` are expected (linked from series `index.html`) but not documented in workflow.

Add to Phase 8 or create new phase:
```markdown
### Phase 8.5: Create HTML Outputs (for Series Only)

**If episode is part of a series:**

1. Generate report.html from report.md:
   ```bash
   # Use markdown converter (e.g., pandoc, or custom script)
   pandoc report.md -o report.html --standalone --css=../../style.css
   ```

2. Generate transcript.html from transcript.json:
   ```bash
   # Parse JSON and create readable HTML
   python tools/transcript-to-html.py tmp/YYYY-MM-DD-slug_transcript.json report.html
   ```

3. Verify HTML files:
   ```bash
   ls -lh report.html transcript.html
   # Should exist and be small (2-5KB)
   ```

**If standalone episode:**
Skip this phase - HTML files only needed for series index pages
```

**Critical .m4a handling:**

Add reminder to Phase 7 (Audio Processing):
```markdown
### Phase 7: Audio Processing

**⚠️ IMPORTANT: Source audio files**

The .m4a file you provide is already .gitignored (see .gitignore line 23).

**DO NOT:**
- Use `git add -f` to force-add .m4a files
- Manually add .m4a to git staging

**VERIFY .m4a not staged:**
```bash
git status | grep ".m4a"
# Should return nothing
```

**If .m4a was accidentally committed:**
```bash
# Remove from git but keep local file
git rm --cached YYYY-MM-DD-slug.m4a
git commit -m "Remove .m4a source file (should be gitignored)"
```
```

---

## Future Enhancements

**Nice-to-have improvements for consideration:**

1. **Interactive checklist script:**
   ```bash
   ./podcast-workflow.sh
   # Walks through each phase, checks exit criteria, blocks progression
   ```

2. **Automated validation:**
   ```bash
   ./validate-episode.sh YYYY-MM-DD-slug
   # Checks all files exist, metadata is correct, feed.xml is valid
   ```

3. **Pre-commit hooks:**
   - Automatically validate feed.xml structure before allowing commit
   - Check file sizes match what's in feed.xml
   - Verify duration format is correct

4. **Workflow state file:**
   - Track which phases are complete in `.workflow-state.json`
   - Allow resuming if interrupted
   - Prevent skipping required phases

5. **AI-assisted metadata generation:**
   - Automatically extract keywords from report.md
   - Generate description from first paragraph of report
   - Suggest pubDate based on current time

---

## Measurements of Success

**How we'll know improvements are working:**

1. **Zero missed critical steps** in next 10 episodes
   - Specifically: git push executed every time
   - All episodes deploy to GitHub Pages on first try

2. **Reduced time per episode:**
   - Baseline: ~X hours (measure current)
   - Target: 20% reduction through better workflow clarity

3. **Fewer errors requiring troubleshooting:**
   - Track number of times user needs to fix errors
   - Target: <2 errors per episode workflow

4. **User confidence:**
   - Can complete workflow without asking "did I miss anything?"
   - Can recover from errors without external help

---

## Change Log

**2024-12-15 (Initial):**
- Initial documentation of improvement ideas
- Triggered by missing git push in Episode 6 workflow
- Documented 10 specific improvement categories
- Created implementation priority and testing plan

**2024-12-15 (Update 1 - File Organization):**
- Added improvement #11: Episode Directory File Organization
- Analyzed Episode 1 file structure (18 files, 122MB)
- Discovered HTML files (report.html, transcript.html) are intentional for series index pages
- Identified missing workflow documentation for HTML generation
- Confirmed .m4a already in .gitignore (line 23) but still being committed
- Proposed research/, logs/, tmp/ subdirectory structure
- Created comprehensive file organization table with placement rules
- Identified Phase 8.5 gap: HTML creation not documented
- Added .m4a verification steps to prevent accidental commits

**Key findings:**
- Root directory should have only 7 final files (vs current 18)
- 81MB .m4a file should never be committed (already gitignored)
- HTML files ARE needed for series but workflow doesn't create them
- chapters.txt is temporary and should be deleted after embed
- transcript.json (449KB) could be moved to tmp/ or gitignored

**2024-12-15 (Update 2 - File Naming Convention):**
- Refined research file naming to use phase prefixes: p1, p2, p3
- Removed redundant "research-" prefix (files are in /research directory)
- Chose "p1-brief.md" over "p1-prompt.md" (reserve "prompt" for tool prompts)
- Individual tool outputs: p2-perplexity.md, p2-grok.md, p2-chatgpt.md, p2-gemini.md, p2-manual.md
- Synthesis output: p3-briefing.md (cross-validated synthesis for Opus)
- Eliminated research-results.md as redundant (go directly from individual files to briefing)
- Files now sort chronologically when listing directory (ls research/)

**Naming rationale:**
- Phase prefixes ensure chronological sorting
- "Brief" describes research topic/question without implying tool-specific prompt
- Individual tool files prevent race conditions and enable parallel execution
- Clear workflow progression: p1 (brief) → p2 (research) → p3 (synthesis)

**Files requiring updates:**

**1. `.claude/skills/podcast-series.md`**

Current structure shown (lines 20-37):
```
podcast/episodes/
├── series-name/
│   ├── ep1-topic-slug/
│   │   ├── prompts.md
│   │   ├── research-results.md
│   │   ├── sources.md
│   │   ├── report.md
│   │   ├── publish.md
│   │   ├── documents/
│   │   ├── cover.png
│   │   ├── YYYY-MM-DD-series-name-episode-1-topic.mp3
│   │   ├── YYYY-MM-DD-series-name-episode-1-topic_transcript.json
│   │   ├── YYYY-MM-DD-series-name-episode-1-topic_chapters.txt
│   │   └── YYYY-MM-DD-series-name-episode-1-topic_chapters.json
```

**Should be updated to:**
```
podcast/episodes/
├── series-name/
│   ├── ep1-topic-slug/
│   │   ├── research/                    # Research files organized by phase
│   │   │   ├── p1-brief.md
│   │   │   ├── p2-perplexity.md
│   │   │   ├── p2-grok.md
│   │   │   ├── p2-chatgpt.md
│   │   │   ├── p2-gemini.md
│   │   │   ├── p2-manual.md
│   │   │   ├── p3-briefing.md
│   │   │   └── documents/
│   │   ├── logs/                        # Process logs
│   │   │   ├── prompts.md
│   │   │   └── metadata.md
│   │   ├── tmp/                         # Temporary files (optional)
│   │   │   └── *_transcript.json
│   │   ├── cover.png
│   │   ├── report.md
│   │   ├── report.html                  # For series index page
│   │   ├── transcript.html              # For series index page
│   │   ├── sources.md
│   │   ├── YYYY-MM-DD-series-ep1-topic.mp3
│   │   └── YYYY-MM-DD-series-ep1-topic_chapters.json
```

**2. `.claude/skills/new-podcast-episode.md`**
- Update Phase 1 to create research/, logs/, tmp/ subdirectories
- Update Phase 2 to save outputs to research/p2-[tool].md
- Update Phase 3 to create research/p3-briefing.md from p2-*.md files
- Update Phase 7 to delete chapters.txt after embedding
- Update Phase 10 to use new file structure in git add

**3. Episode creation templates**
- Update any template files or examples to use new naming convention

**Next:**
- Update `.claude/skills/podcast-series.md` with new directory structure
- Update `.claude/skills/new-podcast-episode.md` with phase-prefixed naming
- Implement Phase 1 improvements (critical safety)
- Create tools for HTML generation (report.md → report.html, transcript.json → transcript.html)
- Test file organization structure with Episode 7
- Gather feedback and iterate
