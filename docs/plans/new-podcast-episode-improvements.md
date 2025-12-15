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

## Implementation Priority

### Phase 1: Critical Safety Improvements (Prevent Missing Steps)
**Must implement first:**
1. ✅ Quick Reference checklist at top with Phase 10 warning
2. ✅ Visual markers (🚨) for critical push step in Phase 10
3. ✅ Exit criteria for each phase
4. ✅ Verification commands after critical operations

**Impact:** Prevents the specific failure mode that occurred (missing git push)

### Phase 2: Usability Improvements (Easier to Follow)
**Implement second:**
5. ✅ Visual phase boundaries with ASCII art
6. ✅ File state indicators (before/after each phase)
7. ✅ Phase dependency map at top
8. ✅ Decision trees for common choices (Task tool vs direct)

**Impact:** Makes workflow easier to navigate and understand

### Phase 3: Robustness Improvements (Handle Errors)
**Implement third:**
9. ✅ Common failure modes & solutions for each phase
10. ✅ Templates for repetitive tasks (feed.xml)

**Impact:** Reduces time lost to troubleshooting and errors

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

**2024-12-15:**
- Initial documentation of improvement ideas
- Triggered by missing git push in Episode 6 workflow
- Documented 10 specific improvement categories
- Created implementation priority and testing plan

**Next:**
- Implement Phase 1 improvements (critical safety)
- Test with Episode 7 creation
- Gather feedback and iterate
