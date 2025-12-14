# Gemini Deep Research Automation

This skill automates the submission of research prompts to Gemini's Deep Research feature using Chrome DevTools.

## Overview

Gemini Deep Research is a tool that performs comprehensive web research by:
1. Analyzing your prompt
2. Creating a multi-step research plan (8-10 research steps)
3. Searching multiple sources across the web
4. Synthesizing findings into a comprehensive report with citations

**Time:** Research typically takes 3-5 minutes to complete.

**Output:** Comprehensive research report with inline citations and source links.

## Prerequisites

- Chrome must be running with remote debugging enabled.
- User must be logged into Google Gemini (https://gemini.google.com/)
- Gemini Advanced subscription required (Deep Research is a paid feature)

## Key Constraints

**CRITICAL:** Deep Research mode is incompatible with "Thinking" mode.
- You MUST be in "Fast" mode to use Deep Research
- If "Thinking" mode is active, switch to "Fast" first

## Complete Automation Workflow

### Step 1: List and Select Gemini Page

Check if Gemini is already open, or navigate to it:

```
1. Use list_pages to see available Chrome pages
2. If Gemini is open (https://gemini.google.com/app*), select that page
3. If not open, use navigate_page or new_page to open https://gemini.google.com/
```

**Expected page URL patterns:**
- New chat: `https://gemini.google.com/app?...`
- Existing chat: `https://gemini.google.com/app/[chat-id]?...`

### Step 2: Take Snapshot to Identify Current State

```
Take snapshot to identify:
- Current mode (Fast vs Thinking)
- Location of UI elements (textarea, Tools button, mode selector)
```

**Key elements to look for:**
- Mode selector button (shows "Fast" or "Thinking")
- "Tools" button
- Main textarea with "Enter a prompt here"

### Step 3: Ensure Fast Mode is Active

```
1. Look for the mode selector button (shows current mode)
2. If it shows "Thinking", click to expand menu
3. Select "Fast" from the menu
4. Verify mode switched to "Fast"
```

**Why this matters:** Deep Research is only available in Fast mode, not Thinking mode.

### Step 4: Enable Deep Research

```
1. Click the "Tools" button to open tools menu
2. Look for "Deep Research" button in the menu
3. Click "Deep Research" to enable it
4. Verify Deep Research is active (button changes to "Deselect Deep Research")
```

**Other tools in menu (ignore these):**
- Create images
- Canvas
- Guided Learning

### Step 5: Fill and Submit the Research Prompt

```
1. Find the main textarea element (usually "Enter a prompt here")
2. Use fill() to enter the research prompt
3. Prompt is auto-submitted when filled (no separate submit button needed initially)
```

**Prompt format:** Should be 3 lines with single newlines (no double newlines):
```
Research [TOPIC].
Focus on [SPECIFIC FOCUS AREA].
Provide [OUTPUT REQUIREMENTS].
```

### Step 6: Wait for Research Plan Generation

**CRITICAL STEP:** Gemini generates a research plan before starting research.

```
1. Use wait_for() to wait for "Start research" text to appear
2. Set timeout to 10000ms (10 seconds)
3. Gemini will show:
   - Research plan title
   - 8-10 numbered research steps
   - "Start research" button
   - "Edit the research plan" button (optional)
```

**What Gemini shows:**
- "Here's the plan I've put together. Let me know if you need any changes before I start researching."
- Research plan with detailed steps
- Estimated time: "Ready in a few mins"

### Step 7: Confirm and Start Research

```
1. Find the "Start research" button in the snapshot
2. Click it to begin the actual research process
3. Look for "Stop response" button to confirm research is running
```

**After clicking:** Research begins immediately and runs for 3-5 minutes.

### Step 8: Inform User

```
Inform user:
- "Gemini Deep Research is now running"
- "Research topic: [topic]"
- "Estimated time: 3-5 minutes"
- "You can continue with other research tools in parallel"
- "When complete, copy the full research output from Gemini and paste into research-results.md"
```

## Error Handling

### If Gemini page not found:
```
- Navigate to https://gemini.google.com/
- Wait for page load
- Verify user is logged in
```

### If Deep Research button not visible:
```
- User may not have Gemini Advanced subscription
- Inform user: "Deep Research requires Gemini Advanced subscription"
- Provide fallback: Manual submission or skip Gemini research
```

### If mode is stuck in Thinking:
```
- Click mode selector
- Look for "Fast" menu item
- Click "Fast"
- Retry Tools → Deep Research
```

### If "Start research" doesn't appear:
```
- Gemini may still be generating the plan
- Wait additional 5 seconds
- Check for error messages in the UI
- Fallback: Inform user to manually click "Start research"
```

## Example Complete Automation Sequence

```markdown
1. list_pages → Find Gemini at index 1
2. select_page(1) → Switch to Gemini
3. take_snapshot → See current state
4. click(mode_selector_uid) → Open mode menu
5. click(fast_option_uid) → Switch to Fast mode
6. take_snapshot → Verify Fast mode active
7. click(tools_button_uid) → Open Tools menu
8. click(deep_research_uid) → Enable Deep Research
9. take_snapshot → Verify Deep Research active
10. fill(textarea_uid, prompt) → Enter research prompt
11. wait_for("Start research", 10000) → Wait for plan
12. take_snapshot → Find "Start research" button
13. click(start_research_uid) → Begin research
14. take_snapshot → Verify "Stop response" visible
15. Inform user research is running
```

## UI Element Patterns

Based on successful automation, here are the typical UID patterns:

**Mode selector (Fast/Thinking):**
- Button with expandable menu
- Text shows current mode
- Menu has two options: "Fast" and "Thinking with 3 Pro"

**Tools button:**
- Simple button labeled "Tools"
- Opens menu with 4 options

**Deep Research button:**
- Appears in Tools menu
- Changes to "Deselect Deep Research" when active

**Textarea:**
- Multiline textbox
- Placeholder: "Enter a prompt here"
- Usually focused by default

**Start research button:**
- Appears after research plan generation
- Text: "Start research"
- Alternative option: "Edit the research plan"

## Common Issues and Solutions

### Issue: Prompt submits but nothing happens
**Solution:** Deep Research may not be enabled. Check for "Deselect Deep Research" button.

### Issue: "Start research" button doesn't appear
**Solution:** Research plan may still be generating. Wait longer or check for errors.

### Issue: Can't find Deep Research in Tools menu
**Solution:** User needs Gemini Advanced subscription. This is a paid feature.

### Issue: Automation works but research fails
**Solution:** Gemini may have hit rate limits or the prompt may be too complex. Try again or simplify prompt.

## Best Practices

1. **Always verify mode:** Check Fast mode is active before enabling Deep Research
2. **Use wait_for():** Don't assume immediate responses - research plan takes 3-5 seconds to generate
3. **Take snapshots frequently:** UI state changes rapidly - snapshot after each action
4. **Single newlines only:** Use single newlines in prompts to prevent accidental partial submissions
5. **Parallel execution:** Launch Gemini research in one tab, then move to other tools in separate tabs
6. **Error reporting:** If automation fails at any step, provide clear fallback instructions for manual submission

## Integration with Podcast Workflow

When called from the podcast episode workflow:

**Input needed:**
- Research prompt (3-line format, single newlines)
- Episode context (optional, for better error messages)

**Expected output:**
- Success: "Gemini Deep Research running, estimated 3-5 minutes"
- Failure: Clear error message + fallback manual instructions

**Fallback instructions if automation fails:**
```
Manual steps:
1. Go to https://gemini.google.com/
2. Ensure "Fast" mode is selected (not "Thinking")
3. Click "Tools" button
4. Click "Deep Research"
5. Paste the prompt from prompts.md
6. Review the research plan
7. Click "Start research"
8. Wait 3-5 minutes for completion
9. Copy the full output to research-results.md
```

## Collecting the Completed Research Report

Once Deep Research completes (3-5 minutes), you need to copy the full report.

### Step 9: Navigate to Completed Research and Copy Report

**Finding the report:**
```
1. Research completion is indicated by "I've completed your research" message
2. Look for "Export menu" button on the right side panel
3. The export menu may already be open/expanded
```

**Copying the report:**
```
1. If Export menu is not open, click the "Export menu" button
2. Take snapshot to find menu options
3. Look for three options in the menu:
   - "Share report" (may be disabled)
   - "Export to Docs"
   - "Copy"
4. Click "Copy" to copy entire report to clipboard
5. Look for "Copied to clipboard" confirmation message
```

**What gets copied:**
- Complete research report with full narrative
- All inline citations and source links
- Section headings and structure
- Research findings organized by topic
- Full source list at the end

**After copying:**
```
Inform user:
- "Gemini Deep Research report copied to clipboard"
- "The complete report with citations is ready to paste into research-results.md"
- "Report includes: [brief summary of sections]"
- "You can now paste it into the Gemini Deep Research section of research-results.md"
```

### Alternative: Export to Google Docs

If user prefers, they can click "Export to Docs" instead of "Copy":
- Creates a new Google Doc with the full report
- Preserves formatting and links
- Useful for sharing or further editing
- Note: This is manual user action, not automated

## Complete Workflow Summary

**Full automation sequence (Steps 1-9):**
1. Select/navigate to Gemini page
2. Take snapshot to identify UI state
3. Switch to Fast mode (if needed)
4. Open Tools menu
5. Enable Deep Research
6. Fill research prompt
7. Wait for research plan (10 seconds)
8. Click "Start research"
9. **Wait 3-5 minutes for completion**
10. Navigate to completed research page (if needed)
11. Open Export menu
12. Click "Copy" to copy report to clipboard
13. Confirm copy success
14. Inform user report is ready to paste

## Notes

- Deep Research is more comprehensive than regular Gemini chat
- Research plans are customizable (user can click "Edit the research plan" before starting)
- Sources are cited inline with clickable links
- Output includes "Research Websites", "Analyze Results", "Create Report" sections
- Estimated completion time is shown but may vary (typically 3-5 minutes)
- Research can be stopped mid-process with "Stop response" button
- **Export menu is the key to collecting the final report** - look for it on the right side panel
- Copied report is plain text with markdown formatting, perfect for pasting into research-results.md
