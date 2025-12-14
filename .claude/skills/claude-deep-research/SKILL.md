---
name: claude-deep-research
description: Automate Claude.ai Deep Research using Chrome DevTools. Use for Phase 3 complex multi-dimensional research requiring synthesis across academic, industry, policy, and recent sources. Handles browser automation, 10-20 min wait with polling, and extraction of both main output and sources list. Returns comprehensive research ready to paste into research-results.md.
---

# Claude Deep Research Automation

This skill automates the submission of research prompts to Claude.ai's Deep Research feature using Chrome DevTools, including polling for completion and collecting both main output and sources.

## Overview

Claude Deep Research (via claude.ai) is a tool that performs comprehensive web research by:
1. Assessing the research scope and determining if clarifying questions are needed
2. Initializing research tools and conducting deep web research
3. Accessing 500+ sources across the web
4. Synthesizing findings into a comprehensive report with extensive citations

**Time:** Research typically takes 10-20 minutes to complete.

**Output:**
1. Main research report with inline citations (first copy)
2. Top sources list with detailed source quality assessment (second copy after followup prompt)

## Prerequisites

- Chrome must be running with remote debugging enabled
- User must be logged into Claude.ai (https://claude.ai/)
- Claude Pro or Team subscription required (Deep Research is a paid feature)

## Key Features

**Research capabilities:**
- Accesses 500+ sources
- Multi-dimensional analysis across academic, industry, policy, and recent sources
- Extensive citations with source URLs
- Distinguishes correlation from causation
- Notes methodological limitations
- Includes contradictory findings and uncertainties

**Two-part output:**
1. **Main research report:** Comprehensive findings with citations
2. **Top sources list:** Tiered by quality (meta-analyses, RCTs, official sources)

## Complete Automation Workflow

### Step 1: List and Select Claude Page

Check if Claude.ai is already open, or navigate to it:

```
1. Use list_pages to see available Chrome pages
2. If Claude is open (https://claude.ai/*), select that page
3. If not open, use navigate_page or new_page to open https://claude.ai/new
```

**Expected page URL patterns:**
- New chat: `https://claude.ai/new`
- Existing chat: `https://claude.ai/chat/[chat-id]`

### Step 2: Take Snapshot to Identify Current State

```
Take snapshot to identify:
- Tools menu button location
- Main textarea for prompts
- Current mode indicators (Extended thinking, Research mode, model selection)
```

**Key elements to look for:**
- "Open tools menu" button (expandable)
- Main textarea: "Write your prompt to Claude"
- Mode buttons: "Extended thinking", "Research mode", model selector (e.g., "Opus 4.5")

### Step 3: Enable Research Mode

```
1. Click the "Open tools menu" button to expand tools menu
2. Take snapshot to see tools menu options
3. Look for "Research" button with a switch toggle
4. Click "Research" to enable Research mode
5. Verify switch is checked and "Research mode" button appears in the bottom bar
6. Click away from menu (e.g., click on textarea) to close it
```

**Tools menu contents:**
- Use style
- Extended thinking (may already be enabled)
- **Research** ← Enable this
- Web search
- Drive search
- Connected integrations (Gmail, Calendar, Notion, etc.)

**Why this matters:** Research mode must be enabled before submitting the prompt for deep research capabilities.

### Step 4: Fill and Submit the Research Prompt

```
1. Find the main textarea element ("Write your prompt to Claude")
2. Use fill() to enter the research prompt
3. Find the "Send message" button
4. Click "Send message" to submit
```

**Prompt format:** Should be 3 lines with single newlines (no double newlines):
```
Research [TOPIC].
Focus on [SPECIFIC FOCUS AREA].
Provide [OUTPUT REQUIREMENTS].
```

**Example:**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.
Conduct comprehensive research across academic, industry, policy, and recent sources to provide multi-dimensional analysis.
Prioritize authoritative sources, distinguish correlation from causation, note methodological limitations, and cite extensively.
```

### Step 5: Inform User and Begin Wait Period

```
Inform user:
- "Claude Deep Research submitted successfully"
- "Research topic: [topic]"
- "Estimated time: 10-20 minutes (accessing 500+ sources)"
- "Waiting 20 minutes before first check..."
- "You can continue with other research tools in parallel"
```

### Step 6: Wait Initial Period (20 Minutes)

**CRITICAL:** Don't poll immediately. Research takes at least 10-20 minutes.

```
1. Wait 20 minutes (1200 seconds) before first check
2. This allows research to complete without unnecessary polling
```

**Why 20 minutes:**
- Research typically completes in 10-20 minutes
- Waiting the expected duration avoids premature checks
- More efficient than frequent polling

### Step 7: Check for Completion (First Check)

```
1. Take snapshot of the page
2. Look for "Research complete" text or similar completion indicator
3. Check for presence of "Copy" button (indicates output is ready)
4. Look for research status button showing completion (e.g., "Research complete • 503 sources • 12m 1s")
```

**Completion indicators:**
- Status button shows "Research complete • [N] sources • [time]"
- "Copy" button is visible
- "Preview contents" button may be visible
- Full research output is displayed

### Step 8: Poll Every 2 Minutes if Not Complete

```
If research not complete after 20 minutes:
1. Wait 2 minutes (120 seconds)
2. Take snapshot and check for completion again
3. Repeat up to 5 times (total 10 additional minutes)
4. Max total wait: 30 minutes (20 min initial + 10 min polling)
```

**Polling strategy:**
- Check every 2 minutes (not too aggressive)
- Maximum 5 additional checks
- If not complete after 30 minutes, report timeout

### Step 9: Copy Main Research Output

```
Once research is complete:
1. Take snapshot to locate "Copy" button
2. Click the "Copy" button to copy main research output to clipboard
3. Look for "Copied" confirmation or similar indicator
```

**What gets copied:**
- Complete research report with full narrative
- All inline citations and source URLs
- Section headings and structure
- Research findings organized by topic
- Methodological notes and limitations
- Contradictory findings where applicable

### Step 10: Inform User of Main Output Copy

```
Inform user:
- "Claude Deep Research complete! ✓"
- "Duration: [actual time taken]"
- "Sources accessed: [number if visible]"
- "Main research output copied to clipboard"
- "Now requesting top sources list..."
```

### Step 11: Submit Followup Prompt for Sources

```
1. Find the main textarea element (same as before)
2. Use fill() to enter: "list the top sources"
3. Click "Send message" to submit
```

**Why this followup:**
- Gets a curated list of top sources organized by tier
- Includes source quality assessment (meta-analyses, RCTs, studies)
- Provides methodological details and citation information
- Essential for cross-validation phase

### Step 12: Wait for Sources Response (1 Minute)

```
1. Wait 60 seconds for Claude to generate sources list
2. Sources list generation is much faster than full research
```

### Step 13: Take Snapshot and Locate Copy Button

```
1. Take snapshot after 1 minute wait
2. Look for "Copy" button for the sources response
3. Verify sources list has been generated
```

### Step 14: Copy Sources List

```
1. Click the "Copy" button for the sources response
2. Look for "Copied" confirmation
```

**What gets copied:**
- Tiered source list (Tier 1: Meta-analyses, Tier 2: RCTs, Tier 3: Case studies)
- Full citations with authors, titles, journals
- Source URLs
- Key contributions of each source
- Methodological quality notes
- Sample sizes where applicable

### Step 15: Inform User Both Outputs Ready

```
Inform user:
- "Top sources list copied to clipboard ✓"
- "You now have both outputs ready:"
- "  1. Main research report (first copy)"
- "  2. Top sources list (second copy)"
- ""
- "Next steps:"
- "1. Paste main research output into research-results.md under 'Research from Claude Deep Research > Main Research Output'"
- "2. Paste top sources list into research-results.md under 'Research from Claude Deep Research > Top Sources'"
- "3. Let me know when both are pasted so I can begin cross-validation"
```

## Error Handling

### If Claude page not found:
```
- Navigate to https://claude.ai/new
- Wait for page load
- Verify user is logged in
```

### If Research mode button not visible:
```
- User may not have Claude Pro/Team subscription
- Inform user: "Deep Research requires Claude Pro or Team subscription"
- Provide fallback: Manual submission or skip Claude research
```

### If research times out after 30 minutes:
```
- Take final snapshot to check status
- If research is still running: "Research is taking longer than expected. You can manually check claude.ai and copy outputs when complete."
- If research failed: "Research may have encountered an error. Please check claude.ai manually."
- Provide manual fallback instructions
```

### If Copy button not found:
```
- Research output may not be complete
- Check for error messages in the UI
- Fallback: Inform user to manually select and copy text from the research output
```

### If followup sources prompt fails:
```
- May have hit rate limits
- Inform user: "Could not submit sources followup. You can manually type 'list the top sources' and copy the result."
- Main research output is already captured, so this is not critical
```

## UI Element Patterns

Based on Claude.ai interface:

**Tools menu button:**
- Button labeled "Open tools menu"
- Expandable/collapsible
- When expanded, shows list of tools with toggles

**Research mode toggle:**
- Appears in Tools menu
- Button labeled "Research"
- Has a switch that can be checked/unchecked
- When enabled, "Research mode" button appears in bottom bar

**Textarea:**
- Multiline textbox
- Placeholder: "Write your prompt to Claude"
- Usually focused by default on new chat

**Send message button:**
- Text: "Send message"
- Disabled when textarea is empty
- Enabled when text is entered

**Research status:**
- During research: "Initializing research tools..." or similar
- When complete: Button showing "Research complete • [N] sources • [duration]"

**Copy button:**
- Simple button labeled "Copy"
- Appears after research output is complete
- Multiple copy buttons possible (one for each message)
- Need to identify correct one based on position in conversation

## Common Issues and Solutions

### Issue: Research mode doesn't enable
**Solution:** Check subscription status. Deep Research requires paid plan.

### Issue: Research starts but gets stuck
**Solution:** Wait full 30 minutes. Research accessing 500+ sources takes time.

### Issue: Can't find the correct Copy button
**Solution:** Take snapshot and look for Copy button near the research output message. May be multiple Copy buttons in conversation - select the one adjacent to the research report.

### Issue: Sources followup doesn't work
**Solution:** Not critical - main research is already captured. User can manually request sources.

### Issue: Automation works but clipboard is empty
**Solution:** Copy button may not have worked. Retry clicking Copy, or inform user to manually select and copy text.

## Best Practices

1. **Wait the full duration:** Don't poll too early - 20 minutes is the minimum expected time
2. **Take snapshots frequently:** UI state changes during research - snapshot after each action
3. **Single newlines only:** Use single newlines in prompts to prevent accidental partial submissions
4. **Parallel execution:** Launch Claude research first (longest duration), then move to other tools
5. **Error reporting:** If automation fails at any step, provide clear fallback instructions for manual submission
6. **Both outputs are important:** Don't skip the sources followup - it's essential for cross-validation
7. **Check clipboard after each copy:** Verify copy operations succeeded before moving on

## Integration with Podcast Workflow

When called from the podcast episode workflow:

**Input needed:**
- Research prompt (3-line format, single newlines)
- Episode context (optional, for better error messages)

**Expected output:**
- Success: Two clipboard copies ready (main research + sources)
- Failure: Clear error message + fallback manual instructions

**Timing considerations:**
- Claude research takes longest (10-20 minutes)
- Launch Claude automation first
- Run other tools (Perplexity, Grok, ChatGPT, Gemini) in parallel
- Claude will complete last, giving time for other research to finish

**Fallback instructions if automation fails:**
```
Manual steps:
1. Go to https://claude.ai/new
2. Click "Open tools menu" button
3. Click "Research" to enable Research mode
4. Close tools menu
5. Paste the Claude research prompt from prompts.md
6. Click "Send message"
7. Wait 10-20 minutes for research to complete (500+ sources)
8. Click "Copy" button to copy main research output
9. Paste into research-results.md under "Main Research Output"
10. Type "list the top sources" and submit
11. Wait ~1 minute for response
12. Click "Copy" button to copy sources list
13. Paste into research-results.md under "Top Sources"
```

## Example Complete Automation Sequence

```markdown
1. list_pages → Find Claude at index 0
2. select_page(0) → Switch to Claude (if needed)
3. take_snapshot → See current state
4. click(tools_menu_uid) → Open Tools menu
5. take_snapshot → See tools options
6. click(research_toggle_uid) → Enable Research mode
7. click(textarea_uid) → Close menu by focusing elsewhere
8. take_snapshot → Verify Research mode enabled
9. fill(textarea_uid, research_prompt) → Enter research prompt
10. click(send_button_uid) → Submit prompt
11. Inform user: Research submitted, waiting 20 minutes
12. sleep(1200) → Wait 20 minutes
13. take_snapshot → Check for completion
14. If not complete, loop: sleep(120) + snapshot (max 5 times)
15. click(copy_button_uid) → Copy main research output
16. Inform user: Main output copied, requesting sources
17. fill(textarea_uid, "list the top sources") → Followup prompt
18. click(send_button_uid) → Submit followup
19. sleep(60) → Wait 1 minute
20. take_snapshot → Find Copy button for sources
21. click(copy_button_uid) → Copy sources list
22. Inform user: Both outputs ready, paste into research-results.md
```

## Notes

- Claude Deep Research accesses significantly more sources (500+) than other tools
- Research quality is very high with extensive citations and methodological rigor
- Two-part output structure ensures both comprehensive findings and source quality assessment
- Longest research duration of all tools, but most thorough
- Sources list is critical for the cross-validation phase
- Research mode must remain enabled throughout the session for subsequent research queries
- Claude may show "thinking" process before starting research - this is normal
- Output includes contradictory findings and areas of uncertainty, making it excellent for cross-validation
- Cost: Uses Claude Pro/Team credits - one deep research session typically costs equivalent to several regular conversations
