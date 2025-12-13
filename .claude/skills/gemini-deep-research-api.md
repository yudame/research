# Gemini Deep Research API Automation

This skill automates research using Google's Gemini Deep Research API (Interactions API) - no browser automation required.

## Overview

The Gemini Deep Research API provides programmatic access to Google's multi-step research agent:
1. Autonomously plans research strategy
2. Executes web searches across multiple sources
3. Synthesizes findings into a comprehensive report with citations
4. Runs asynchronously with status polling

**Time:** Research typically takes 3-10 minutes depending on complexity (max 60 minutes).

**Output:** Comprehensive research report with inline citations and source links.

## Prerequisites

- Google AI API key stored in `.env` file
- Python 3.x with `requests` library installed
- API key from: https://aistudio.google.com/apikey

## API Key Setup

**Location:** API key should be stored in `.env` file in the repository root.

```bash
# In .env file
GOOGLE_AI_API_KEY=your-api-key-here
```

**Getting an API key:**
1. Go to https://aistudio.google.com/apikey
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add to `.env` file

## API Details

**Base URL:** `https://generativelanguage.googleapis.com/v1beta/interactions`

**Agent Model:** `deep-research-pro-preview-12-2025`

**Key Parameters:**
| Parameter | Value | Description |
|-----------|-------|-------------|
| `input` | string | Research prompt/query |
| `agent` | `deep-research-pro-preview-12-2025` | Deep research agent |
| `background` | `true` | Required for async execution |
| `store` | `true` | Required when background=true |

**Default Capabilities (enabled automatically):**
- `google_search` - Web search across Google
- `url_context` - Fetches and analyzes webpage content

## Complete Automation Workflow

### Step 1: Verify API Key

```bash
# Check if .env file has the API key
grep GOOGLE_AI_API_KEY .env
```

If not found, inform user to set up API key at https://aistudio.google.com/apikey

### Step 2: Submit Research Request

Create and run the research submission script:

```python
import requests
import os
import json
import time
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv('GOOGLE_AI_API_KEY')

if not api_key:
    print("ERROR: GOOGLE_AI_API_KEY not found in .env file")
    exit(1)

# API endpoint
base_url = "https://generativelanguage.googleapis.com/v1beta/interactions"

# Research prompt
research_prompt = """RESEARCH_PROMPT_HERE"""

# Create interaction (start research)
print("Submitting research request to Gemini Deep Research API...")
response = requests.post(
    base_url,
    headers={
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    },
    json={
        "input": research_prompt,
        "agent": "deep-research-pro-preview-12-2025",
        "background": True,
        "store": True
    }
)

if response.status_code != 200:
    print(f"ERROR: Failed to submit research request: {response.status_code}")
    print(response.text)
    exit(1)

result = response.json()
interaction_id = result.get("id")
print(f"Research started. Interaction ID: {interaction_id}")
print(f"Status: {result.get('status')}")
```

### Step 3: Poll for Completion

The research runs asynchronously. Poll until status is `completed`:

```python
# Poll for completion
max_attempts = 30  # Maximum 30 attempts (60 minutes with 2-min intervals)
poll_interval = 120  # 2 minutes between checks

for attempt in range(max_attempts):
    print(f"\nChecking status (attempt {attempt + 1}/{max_attempts})...")

    status_response = requests.get(
        f"{base_url}/{interaction_id}",
        headers={"x-goog-api-key": api_key}
    )

    if status_response.status_code != 200:
        print(f"ERROR: Failed to get status: {status_response.status_code}")
        continue

    status_result = status_response.json()
    status = status_result.get("status")

    print(f"Status: {status}")

    if status == "completed":
        print("\n=== GEMINI DEEP RESEARCH RESULT ===\n")
        outputs = status_result.get("outputs", [])
        for output in outputs:
            if output.get("type") == "text":
                print(output.get("text", ""))
        print("\n=== END OF RESULT ===\n")
        break
    elif status == "failed":
        error = status_result.get("error", "Unknown error")
        print(f"ERROR: Research failed: {error}")
        exit(1)
    else:
        # Still in progress
        print(f"Research in progress. Waiting {poll_interval} seconds...")
        time.sleep(poll_interval)
else:
    print("ERROR: Research timed out after 60 minutes")
    exit(1)
```

### Step 4: Complete Python Script

Here's the full script to save as a file:

```python
#!/usr/bin/env python3
"""
Gemini Deep Research API - Automated Research Script
Usage: python gemini_research.py "Your research prompt here"
"""

import requests
import os
import sys
import time
from dotenv import load_dotenv

def run_gemini_research(prompt: str, poll_interval: int = 120, max_attempts: int = 30):
    """
    Submit a research request to Gemini Deep Research API and wait for completion.

    Args:
        prompt: Research prompt/query
        poll_interval: Seconds between status checks (default 120 = 2 min)
        max_attempts: Maximum polling attempts (default 30 = 60 min max)

    Returns:
        Research report text or None if failed
    """
    # Load API key
    load_dotenv()
    api_key = os.getenv('GOOGLE_AI_API_KEY')

    if not api_key:
        print("ERROR: GOOGLE_AI_API_KEY not found in .env file")
        print("Get your API key at: https://aistudio.google.com/apikey")
        return None

    base_url = "https://generativelanguage.googleapis.com/v1beta/interactions"
    headers = {
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    }

    # Submit research request
    print("Submitting research request to Gemini Deep Research API...")
    print(f"Prompt: {prompt[:100]}..." if len(prompt) > 100 else f"Prompt: {prompt}")

    try:
        response = requests.post(
            base_url,
            headers=headers,
            json={
                "input": prompt,
                "agent": "deep-research-pro-preview-12-2025",
                "background": True,
                "store": True
            },
            timeout=30
        )
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Failed to submit request: {e}")
        return None

    if response.status_code != 200:
        print(f"ERROR: API returned status {response.status_code}")
        print(response.text)
        return None

    result = response.json()
    interaction_id = result.get("id")

    if not interaction_id:
        print("ERROR: No interaction ID returned")
        print(result)
        return None

    print(f"Research started successfully!")
    print(f"Interaction ID: {interaction_id}")
    print(f"Estimated time: 3-10 minutes (max 60 minutes)")
    print(f"Polling every {poll_interval} seconds...")

    # Poll for completion
    for attempt in range(max_attempts):
        print(f"\n[{time.strftime('%H:%M:%S')}] Checking status (attempt {attempt + 1}/{max_attempts})...")

        try:
            status_response = requests.get(
                f"{base_url}/{interaction_id}",
                headers={"x-goog-api-key": api_key},
                timeout=30
            )
        except requests.exceptions.RequestException as e:
            print(f"WARNING: Status check failed: {e}")
            time.sleep(poll_interval)
            continue

        if status_response.status_code != 200:
            print(f"WARNING: Status check returned {status_response.status_code}")
            time.sleep(poll_interval)
            continue

        status_result = status_response.json()
        status = status_result.get("status")

        print(f"Status: {status}")

        if status == "completed":
            # Extract research output
            outputs = status_result.get("outputs", [])
            research_text = ""
            for output in outputs:
                if output.get("type") == "text":
                    research_text += output.get("text", "")

            if research_text:
                print("\n" + "=" * 50)
                print("GEMINI DEEP RESEARCH COMPLETE")
                print("=" * 50 + "\n")
                return research_text
            else:
                print("WARNING: Research completed but no text output found")
                print(status_result)
                return None

        elif status == "failed":
            error = status_result.get("error", "Unknown error")
            print(f"ERROR: Research failed: {error}")
            return None

        else:
            # in_progress - wait and retry
            if attempt < max_attempts - 1:
                print(f"Research in progress. Waiting {poll_interval} seconds...")
                time.sleep(poll_interval)

    print("ERROR: Research timed out")
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gemini_research.py 'Your research prompt'")
        print("   or: python gemini_research.py --file prompt.txt")
        sys.exit(1)

    if sys.argv[1] == "--file" and len(sys.argv) > 2:
        with open(sys.argv[2], 'r') as f:
            prompt = f.read().strip()
    else:
        prompt = " ".join(sys.argv[1:])

    result = run_gemini_research(prompt)

    if result:
        print(result)
        print("\n" + "=" * 50)
        print("Copy the above output to research-results.md")
        print("=" * 50)
    else:
        print("\nResearch failed. See error messages above.")
        sys.exit(1)
```

### Step 5: Run the Research

```bash
# Save the script
cat > /tmp/gemini_research.py << 'SCRIPT'
# [Insert full script from Step 4]
SCRIPT

# Run with prompt
python3 /tmp/gemini_research.py "Research prompt here"

# Or with prompt from file
python3 /tmp/gemini_research.py --file prompts.md
```

## Streaming Support (Optional)

For real-time progress updates, use streaming mode:

```python
# Enable streaming in the request
response = requests.post(
    base_url,
    headers={
        "x-goog-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    },
    json={
        "input": prompt,
        "agent": "deep-research-pro-preview-12-2025",
        "stream": True
    },
    stream=True
)

# Process server-sent events
for line in response.iter_lines():
    if line:
        line = line.decode('utf-8')
        if line.startswith('data: '):
            event_data = json.loads(line[6:])
            event_type = event_data.get('type')

            if event_type == 'content.delta':
                # Real-time text output
                delta = event_data.get('delta', {})
                if delta.get('type') == 'text':
                    print(delta.get('text', ''), end='', flush=True)
                elif delta.get('type') == 'thought_summary':
                    print(f"\n[Thinking: {delta.get('text', '')}]", flush=True)

            elif event_type == 'interaction.complete':
                print("\n\nResearch complete!")
                break
```

## Follow-up Questions

To ask follow-up questions on the same research:

```python
# Use previous_interaction_id to continue conversation
followup_response = requests.post(
    base_url,
    headers=headers,
    json={
        "input": "What are the top 5 sources you used?",
        "agent": "deep-research-pro-preview-12-2025",
        "previous_interaction_id": interaction_id,
        "background": True,
        "store": True
    }
)
```

## Error Handling

### API Key Errors

**Error:** `401 Unauthorized`
```
- API key is invalid or expired
- Verify key at https://aistudio.google.com/apikey
- Regenerate key if needed
```

### Rate Limits

**Error:** `429 Too Many Requests`
```
- Rate limit exceeded
- Wait 60 seconds and retry
- Consider using exponential backoff
```

### Research Failures

**Error:** `status: "failed"`
```
- Research could not complete
- Check error message in response
- May be due to: prompt issues, source access problems, timeout
- Retry with simplified prompt or try different tool
```

### Timeout

**Error:** Research takes > 60 minutes
```
- Research may be too complex
- Simplify the prompt
- Break into smaller research tasks
- Fallback to browser-based Gemini or other tools
```

## Integration with Podcast Workflow

When called from the V2 podcast workflow:

**Input needed:**
- Research prompt (3-line format from prompts.md)
- Episode directory path (for logging)

**Expected output:**
- Success: Full research report with citations
- Failure: Error message + fallback to browser automation

**Workflow integration:**

```python
# In podcast workflow
from gemini_research import run_gemini_research

prompt = """Research [TOPIC].
Focus on regulatory frameworks, legislation, government policy documents, strategic plans, and comparative policy analysis.
Provide findings with official source citations, effective dates, and policy context."""

result = run_gemini_research(prompt)

if result:
    # Save to research-results.md
    with open(f"{episode_dir}/research-results.md", "a") as f:
        f.write("\n\n## Research from Gemini Deep Research (API)\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"**Focus:** Strategic & Policy Sources\n\n")
        f.write(result)
else:
    # Fallback to browser automation
    print("API failed, falling back to browser-based Gemini research")
    # Use gemini-deep-research.md skill
```

**Fallback instructions if API fails:**
```
Manual steps (browser-based):
1. Go to https://gemini.google.com/
2. Ensure "Fast" mode is selected (not "Thinking")
3. Click "Tools" button → "Deep Research"
4. Paste the prompt from prompts.md
5. Review the research plan
6. Click "Start research"
7. Wait 3-5 minutes for completion
8. Click Export → Copy
9. Paste into research-results.md
```

## Comparison: API vs Browser Automation

| Aspect | API | Browser (Chrome DevTools) |
|--------|-----|---------------------------|
| **Reliability** | High (direct API) | Medium (UI changes break it) |
| **Speed** | Same research time | Same + UI overhead |
| **Setup** | API key only | Chrome + debug mode |
| **Automation** | Fully scriptable | Requires browser running |
| **Headless** | Yes | No (needs Chrome) |
| **Cost** | API usage | Free (Gemini Advanced sub) |
| **Maintenance** | Low | High (UI changes) |

**Recommendation:** Use API as primary method, browser automation as fallback.

## API Cost Considerations

**Pricing:** Check current pricing at https://ai.google.dev/pricing

**Cost factors:**
- Deep Research uses more compute than standard queries
- Longer research = higher cost
- Background execution may have different pricing

**Cost optimization:**
- Keep prompts focused
- Set reasonable poll intervals
- Don't run redundant research
- Monitor usage in Google AI Studio

## Best Practices

1. **Always verify API key** before running research
2. **Use background mode** for research (required for long tasks)
3. **Set reasonable poll intervals** (2 minutes is good balance)
4. **Handle timeouts gracefully** with fallback to browser
5. **Log all interactions** for debugging
6. **Preserve citations** - don't strip markdown formatting
7. **Use streaming** for real-time progress visibility
8. **Test with simple prompts** before complex research
9. **Monitor API usage** to control costs

## Notes

- This API is in **preview** (as of December 2025) - schema may change
- Model name includes date suffix: `deep-research-pro-preview-12-2025`
- `background: true` and `store: true` are required together
- Web search (google_search, url_context) enabled by default
- Maximum research duration: 60 minutes
- Follow-up questions supported via `previous_interaction_id`
- Streaming provides real-time thinking summaries and content deltas
- Citations are included inline in the output
- Perfect for automated workflows - no browser required
