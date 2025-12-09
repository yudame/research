# ChatGPT Deep Research Automation

This skill automates the submission of research prompts to ChatGPT's Deep Research feature using Chrome DevTools.

## Overview

ChatGPT Deep Research is a tool that performs comprehensive web research by:
1. Analyzing your prompt and potentially asking clarifying questions
2. Conducting multi-source web research across industry, technical, and business sources
3. Synthesizing findings into a comprehensive report with citations

**Time:** Research typically takes 5-10 minutes to complete.

**Output:** Comprehensive research report with inline citations and source links.

**Key feature:** ChatGPT may ask clarifying questions before starting research, making it more interactive than other tools.

## Prerequisites

- Chrome must be running with remote debugging enabled
- User must be logged into ChatGPT (https://chatgpt.com/)
- ChatGPT Plus or Team subscription required (Deep Research is a paid feature)
- Model must support Deep Research (o1, o1-mini, or Research-enabled models)

## Key Characteristics

**ChatGPT's unique approach:**
- May ask clarifying questions before starting research (interactive mode)
- Allows user to continue chatting while research runs in background
- Focuses on industry reports, technical documentation, case studies, and business analysis
- More conversational and interactive than Gemini or Claude

**Research specialization:**
- Industry analyst reports and market research
- Technical documentation and specifications
- Business case studies and financial analysis
- Company reports and corporate information
- Commercial and trade data

## Complete Automation Workflow

### Step 1: List and Select ChatGPT Page

Check if ChatGPT is already open, or navigate to it:

```
1. Use list_pages to see available Chrome pages
2. If ChatGPT is open (https://chatgpt.com/*), select that page
3. If not open, use navigate_page or new_page to open https://chatgpt.com/
```

**Expected page URL patterns:**
- Home/Research mode: `https://chatgpt.com/`
- Existing chat: `https://chatgpt.com/c/[chat-id]`

### Step 2: Take Snapshot to Identify Current State

```
Take snapshot to identify:
- Model selector button (shows current model)
- Research mode status
- Main textarea for prompts
- UI layout and available elements
```

**Key elements to look for:**
- Model selector button (e.g., "Model selector, current model is 5.1")
- "Research, click to remove" button (if Research mode already enabled)
- Main textarea with "Get a detailed report" or "What are you researching?"
- "Add files and more" button

### Step 3: Ensure Research Mode is Active

**Check for Research mode indicator:**

```
1. Look for "Research, click to remove" button
2. If present, Research mode is already enabled - proceed to Step 4
3. If not present, need to enable Research mode:
   a. Look for model selector button
   b. May need to click and select a research-capable model
   c. Look for Research toggle or option
```

**Note:** Research mode may be automatically enabled when navigating to https://chatgpt.com/ for a new conversation.

**Models that support Deep Research:**
- o1
- o1-mini
- Research-enabled GPT models (check model selector)

### Step 4: Fill and Submit the Research Prompt

```
1. Find the main textarea element
2. Use fill() to enter the research prompt
3. Look for "Send prompt" button
4. Click "Send prompt" to submit
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
Focus on industry analyst reports, market research, technical documentation, case studies, and financial/business analysis.
Provide comprehensive findings with citations, data sources, and comparative analysis where relevant.
```

### Step 5: Handle Potential Clarifying Questions

**CRITICAL:** ChatGPT may ask clarifying questions before starting research.

```
1. After submitting, wait 3-5 seconds
2. Take snapshot to check response
3. Look for clarifying questions in ChatGPT's response
4. If questions are asked:
   a. Inform user: "ChatGPT is asking clarifying questions. Please review and respond."
   b. Provide fallback: User must manually answer questions to proceed
   c. This is a manual step - automation cannot answer domain-specific questions
5. If no questions, proceed to Step 6
```

**Why manual intervention needed:**
- Questions are research-specific and require domain knowledge
- Automated responses might misdirect the research
- User should have control over research scope

**Alternative approach for automation:**
- Use very detailed prompts upfront to minimize likelihood of questions
- Include specifics: time period, geographic scope, data types, etc.

### Step 6: Wait for Research to Start

```
1. Look for "Starting research" button or text
2. This indicates research has begun
3. May also see "Stop streaming" button
```

**Research start indicators:**
- "Starting research" text or button visible
- Message like "I'll gather the most recent data available..."
- "Stop streaming" button appears
- Status changes in the UI

### Step 7: Inform User Research is Running

```
Inform user:
- "ChatGPT Deep Research is now running"
- "Research topic: [topic]"
- "Estimated time: 5-10 minutes"
- "ChatGPT allows you to continue chatting while research runs in background"
- "I'll poll for completion every 2 minutes"
```

### Step 8: Poll for Research Completion

**Polling strategy:** Check every 2 minutes for completion.

```
1. Wait 5 minutes before first check (research typically takes 5-10 min)
2. Take snapshot and look for completion indicators:
   - Research report is displayed
   - "Copy" button appears near the research output
   - No "Stop streaming" button visible
   - Research status shows complete
3. If not complete, wait 2 more minutes and check again
4. Maximum polling: 6 attempts (5 min initial + 10 min polling = 15 min total)
5. If not complete after 15 minutes, inform user to check manually
```

**Completion indicators:**
- Full research report visible in the conversation
- "Copy" button available
- No "Stop streaming" or "Starting research" buttons
- Report contains sections, citations, and conclusions

### Step 9: Locate and Copy Research Output

```
1. Take snapshot to identify the research report article
2. Look for the most recent "ChatGPT said:" article with substantial content
3. Find "Copy" button associated with that article
4. Click "Copy" to copy research output to clipboard
5. Look for copy confirmation or success indicator
```

**What gets copied:**
- Complete research report with findings
- Inline citations and source references
- Section headings and structure
- Analysis and conclusions
- Source list (may be inline or at end)

### Step 10: Inform User Output is Ready

```
Inform user:
- "ChatGPT Deep Research complete! ✓"
- "Duration: [actual time taken]"
- "Research output copied to clipboard"
- ""
- "Next steps:"
- "Paste the research output into research-results.md under 'Research from ChatGPT Deep Research (Industry & Technical)'"
- "Let me know when pasted so I can continue with cross-validation"
```

## Error Handling

### If ChatGPT page not found:
```
- Navigate to https://chatgpt.com/
- Wait for page load
- Verify user is logged in
```

### If Research mode not available:
```
- User may not have ChatGPT Plus/Team subscription
- Model may not support Deep Research
- Inform user: "Deep Research requires ChatGPT Plus/Team and a research-capable model"
- Provide fallback: Manual submission or skip ChatGPT research
```

### If clarifying questions are asked:
```
- This is expected behavior
- Inform user of the questions
- User must manually respond to continue
- Cannot automate this step - requires human judgment
```

### If research times out after 15 minutes:
```
- Take final snapshot to check status
- If research is still running: "Research is taking longer than expected. Please check chatgpt.com and copy output when complete."
- If research failed: "Research may have encountered an error. Please check chatgpt.com manually."
- Provide manual fallback instructions
```

### If Copy button not found:
```
- Research may not be complete
- UI may have changed
- Fallback: Inform user to manually select and copy text from the research output
```

## UI Element Patterns

Based on ChatGPT interface:

**Model selector:**
- Button showing current model (e.g., "Model selector, current model is 5.1")
- Expandable menu to switch models
- Research-capable models are clearly labeled

**Research mode indicator:**
- Button labeled "Research, click to remove" when enabled
- Can be toggled off by clicking
- May auto-enable when navigating to research page

**Textarea:**
- Main input area for prompts
- Placeholder varies: "Get a detailed report", "What are you researching?", "Ask anything"
- Dynamically changes based on context

**Send button:**
- Text: "Send prompt"
- Only enabled when text is entered
- Submits the research query

**Research status:**
- "Starting research" button/text during initialization
- "Stop streaming" button while research is running
- Research report appears in conversation when complete

**Copy button:**
- Simple button labeled "Copy"
- Appears in each message article
- Multiple copy buttons in conversation - select the one next to research output

## Common Issues and Solutions

### Issue: Research mode doesn't enable
**Solution:** Check subscription status and model selection. Ensure using research-capable model.

### Issue: ChatGPT asks too many clarifying questions
**Solution:** Make initial prompt more detailed and specific. Include: time period, geographic scope, specific focus areas, data types needed.

### Issue: Can't find the research output
**Solution:** Scroll through conversation to find the substantial research report (not the clarifying questions phase).

### Issue: Research seems stuck
**Solution:** Wait full 15 minutes. ChatGPT research can take longer for complex topics. Check for "Stop streaming" button.

### Issue: Copy button copies wrong content
**Solution:** Identify the correct article containing the research report. There may be multiple "Copy" buttons - use the one adjacent to the full research output.

## Best Practices

1. **Detailed prompts:** Include specifics upfront to minimize clarifying questions
2. **Time expectations:** Set realistic wait times (5-10 minutes typical, up to 15 minutes)
3. **Single newlines only:** Use single newlines in prompts to prevent accidental partial submissions
4. **Parallel execution:** Can launch ChatGPT research alongside other tools
5. **Error reporting:** If automation fails, provide clear fallback instructions for manual submission
6. **Model selection:** Verify research-capable model is selected before starting
7. **Manual intervention ready:** Be prepared for user to answer clarifying questions

## Integration with Podcast Workflow

When called from the podcast episode workflow:

**Input needed:**
- Research prompt (3-line format, single newlines)
- Episode context (optional, for better error messages)

**Expected output:**
- Success: Research output copied to clipboard
- Partial success: Research submitted but requires user to answer clarifying questions
- Failure: Clear error message + fallback manual instructions

**Timing considerations:**
- ChatGPT research takes 5-10 minutes (faster than Claude, similar to Gemini)
- Launch in parallel with other tools
- May require manual intervention if clarifying questions are asked

**Fallback instructions if automation fails:**
```
Manual steps:
1. Go to https://chatgpt.com/
2. Ensure a research-capable model is selected (o1, o1-mini, or Research)
3. Verify Research mode is enabled (look for "Research, click to remove" button)
4. Paste the ChatGPT research prompt from prompts.md
5. Click "Send prompt"
6. If ChatGPT asks clarifying questions, answer them with specific details
7. Wait 5-10 minutes for research to complete
8. Click "Copy" button next to the research output
9. Paste into research-results.md under "Research from ChatGPT Deep Research"
```

## Example Complete Automation Sequence

```markdown
1. list_pages → Find ChatGPT at index 3
2. select_page(3) → Switch to ChatGPT (if needed)
3. take_snapshot → See current state
4. Check for "Research, click to remove" button
5. If not present, enable Research mode via model selector or toggle
6. take_snapshot → Verify Research mode enabled
7. fill(textarea_uid, research_prompt) → Enter research prompt
8. click(send_button_uid) → Submit prompt
9. sleep(3) → Wait for initial response
10. take_snapshot → Check for clarifying questions
11. If questions present: Inform user, manual intervention required
12. If no questions: Wait for "Starting research" indicator
13. Inform user: Research running, estimated 5-10 minutes
14. sleep(300) → Wait 5 minutes initial
15. take_snapshot → Check for completion
16. If not complete: Loop sleep(120) + snapshot (max 5 times)
17. When complete: Locate research output article
18. click(copy_button_uid) → Copy research output
19. Inform user: Output ready to paste into research-results.md
```

## Notes

- ChatGPT's clarifying questions phase makes it more interactive but less fully automatable than Gemini or Claude
- Research quality is excellent for industry, technical, and business analysis
- Faster completion time (5-10 min) compared to Claude (10-20 min)
- Background research mode allows user to continue using ChatGPT while research runs
- Output format may vary but always includes citations and structured sections
- Best used for: industry reports, technical docs, case studies, business/financial analysis
- Cost: Uses ChatGPT Plus/Team credits - one deep research session costs more than regular chat
