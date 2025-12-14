---
name: perplexity-deep-research
description: Automate Perplexity Deep Research API calls using sonar-deep-research model. Use for Phase 1 academic research in podcast episodes. Handles API key verification, Python script creation, execution (30-120s), and result formatting with citations. Returns research ready to paste into research-results.md.
---

# Perplexity Deep Research API Automation

This skill automates the submission of research prompts to Perplexity's Deep Research API (`sonar-deep-research` model).

## Overview

Perplexity Deep Research is an API-based research tool that:
1. Conducts comprehensive web research
2. Synthesizes findings from multiple authoritative sources
3. Returns structured research reports with citations
4. Focuses on academic studies, peer-reviewed papers, and official sources

**Time:** Research typically takes 30-120 seconds to complete (much faster than Gemini's 3-5 minutes).

**Output:** JSON response containing the research report with inline citations.

## Prerequisites

- Perplexity API key stored in `.env` file
- Python 3.x with `requests` library installed
- API key from: https://www.perplexity.ai/settings/api

## API Key Setup

**Location:** API key should be stored in `.env` file in the repository root.

```bash
# In /Users/valorengels/src/research/.env
PERPLEXITY_API_KEY=pplx-your-api-key-here
```

**Getting an API key:**
1. Go to https://www.perplexity.ai/settings/api
2. Sign in to your Perplexity account
3. Generate a new API key
4. Copy the key and add to `.env` file

**Verify .env file exists:**
```bash
ls -la /Users/valorengels/src/research/.env
```

If it doesn't exist, create it:
```bash
echo "PERPLEXITY_API_KEY=your-key-here" >> /Users/valorengels/src/research/.env
```

## API Model Information

**Model:** `sonar-deep-research`

**Capabilities:**
- Conducts multi-step research process
- Searches across academic databases, official sources, peer-reviewed journals
- Synthesizes findings with proper citations
- Returns structured markdown-formatted reports
- Includes source URLs for verification

**Reasoning Effort Parameter:**
- Controls computational effort for research depth
- Options: `low`, `medium`, `high`
- **Recommended:** `high` for podcast research (most comprehensive)
- Higher effort = better quality + longer processing time
- Default is `medium` if not specified

**Documentation:**
- Model: https://docs.perplexity.ai/getting-started/models/models/sonar-deep-research
- Reasoning Effort: https://docs.perplexity.ai/getting-started/models/models/sonar-deep-research#reasoning-effort

## Complete Automation Workflow

### Step 1: Read API Key from Environment

```bash
# Check if .env file exists
cat /Users/valorengels/src/research/.env | grep PERPLEXITY_API_KEY
```

**If key not found:**
- Inform user: "PERPLEXITY_API_KEY not found in .env file"
- Provide setup instructions
- Cannot proceed without API key

### Step 2: Create Python Script for API Call

Create a temporary Python script to make the API request:

```python
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/Users/valorengels/src/research/.env')

# Get API key
api_key = os.getenv('PERPLEXITY_API_KEY')

if not api_key:
    print("ERROR: PERPLEXITY_API_KEY not found in .env file")
    exit(1)

# API endpoint
url = "https://api.perplexity.ai/chat/completions"

# Prepare payload with research prompt
payload = {
    "model": "sonar-deep-research",
    "messages": [
        {
            "role": "user",
            "content": """RESEARCH_PROMPT_HERE"""
        }
    ],
    "reasoning_effort": "high"  # Options: low, medium, high
}

# Headers with authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Make API request
print("Submitting research request to Perplexity API...")
response = requests.post(url, json=payload, headers=headers)

# Check response status
if response.status_code == 200:
    result = response.json()
    print("\n=== PERPLEXITY DEEP RESEARCH RESULT ===\n")
    print(result['choices'][0]['message']['content'])
    print("\n=== END OF RESULT ===\n")
else:
    print(f"ERROR: API request failed with status {response.status_code}")
    print(response.text)
    exit(1)
```

### Step 3: Write Script to Temporary File

```bash
# Create temp script
cat > /tmp/perplexity_research.py << 'EOF'
[Insert Python script from Step 2]
EOF
```

**Replace placeholder:** Substitute `RESEARCH_PROMPT_HERE` with the actual research prompt from prompts.md.

### Step 4: Install Required Python Package

Check if `requests` and `python-dotenv` are installed:

```bash
python3 -c "import requests, dotenv" 2>/dev/null || pip3 install requests python-dotenv
```

### Step 5: Execute the API Request

```bash
cd /Users/valorengels/src/research
python3 /tmp/perplexity_research.py
```

**Expected output:**
```
Submitting research request to Perplexity API...

=== PERPLEXITY DEEP RESEARCH RESULT ===

[Full research report with citations]

=== END OF RESULT ===
```

### Step 6: Parse and Save the Response

The API returns JSON with this structure:
```json
{
  "id": "request-id",
  "model": "sonar-deep-research",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "# Research Report Title\n\nFull research content with citations..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 456,
    "total_tokens": 579
  }
}
```

**Extract the content:**
```python
content = result['choices'][0]['message']['content']
```

### Step 7: Inform User

```
Inform user:
- "Perplexity Deep Research completed successfully"
- "Research report is [X] tokens / [Y] words"
- "Output contains comprehensive research with inline citations"
- "Copy the research output between the markers and paste into research-results.md"
```

## Alternative: Direct Bash Execution with curl

For simpler execution without Python script:

```bash
# Read API key from .env
source /Users/valorengels/src/research/.env

# Make API call with curl
curl -X POST "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: "application/json" \
  -d '{
    "model": "sonar-deep-research",
    "messages": [
      {
        "role": "user",
        "content": "RESEARCH_PROMPT_HERE"
      }
    ],
    "reasoning_effort": "high"
  }' | python3 -m json.tool
```

**Note:** This requires proper escaping of the research prompt content, especially quotes and newlines.

## Error Handling

### API Key Errors

**Error:** `401 Unauthorized`
```
- API key is invalid or expired
- Check .env file has correct key
- Verify key at https://www.perplexity.ai/settings/api
- Regenerate key if needed
```

**Error:** `PERPLEXITY_API_KEY not found`
```
- .env file doesn't exist or doesn't contain key
- Run setup instructions from Prerequisites section
- Verify file permissions: chmod 600 .env
```

### API Request Errors

**Error:** `429 Too Many Requests`
```
- Rate limit exceeded
- Wait 60 seconds and retry
- Check API usage limits in Perplexity dashboard
```

**Error:** `500 Internal Server Error`
```
- Perplexity API is experiencing issues
- Retry after 30 seconds
- Check Perplexity status page
- Fallback: Manual research or use different tool
```

**Error:** `Request timeout`
```
- Research is taking longer than expected
- Deep research can take 1-2 minutes for complex topics
- Increase timeout if needed
- Consider simplifying the prompt
```

### Python Errors

**Error:** `ModuleNotFoundError: No module named 'requests'`
```bash
pip3 install requests python-dotenv
```

**Error:** `ModuleNotFoundError: No module named 'dotenv'`
```bash
pip3 install python-dotenv
```

## Prompt Format Guidelines

For best results with Perplexity Deep Research:

**Structure:**
```
Research [TOPIC].
Focus on [SPECIFIC FOCUS AREA].
Provide [OUTPUT REQUIREMENTS].
```

**Example - Academic Focus:**
```
Research Solomon Islands telecommunications market structure and competitive dynamics.
Focus on peer-reviewed studies, meta-analyses, systematic reviews, and official government/regulatory sources.
Provide comprehensive findings with full citations, sample sizes, methodological details, and source URLs.
```

**Important:**
- Keep prompts under 2000 characters for optimal performance
- Use single newlines (not double) to prevent formatting issues
- Be specific about desired source types
- Request citations explicitly
- Specify output format needs (e.g., "with full citations", "with source URLs")

## Output Format

Perplexity Deep Research returns:

**Content structure:**
- Markdown-formatted research report
- Section headings (# ## ###)
- Inline citations with superscript numbers [1]
- Source list at the end with URLs
- Organized by topic/subtopic

**Citation format:**
```
Finding statement with citation[1].
Another finding with multiple sources[2][3].

## Sources
[1] Source Title - URL
[2] Source Title - URL
[3] Source Title - URL
```

## Integration with Podcast Workflow

When called from the podcast episode workflow:

**Input needed:**
- Research prompt (3-line format from prompts.md)
- Episode context (optional, for logging)

**Expected output:**
- Success: Research report with citations saved to variable
- Failure: Clear error message + fallback instructions

**After successful API call:**
```
1. Extract content from JSON response
2. Format output with clear markers
3. Inform user to copy and paste into research-results.md
4. Provide token/word count summary
5. Confirm all citations are included
```

**Fallback instructions if API fails:**
```
Manual alternative:
1. Go to https://www.perplexity.ai/
2. Enable "Pro Search" mode
3. Paste the prompt from prompts.md
4. Wait for results (30-120 seconds)
5. Copy the full research output
6. Paste into research-results.md under Perplexity section
```

## Comparison: API vs Web Interface

**API Advantages:**
- Fully automated (no browser required)
- Faster execution (30-120 seconds)
- Scriptable and repeatable
- No UI interaction needed
- Works in headless environments

**API Limitations:**
- Requires paid API access
- Limited to text output (no UI features)
- Cannot view research plan before execution
- Less control over research depth

**Web Interface Advantages:**
- Free tier available
- Can review and edit queries
- Access to UI features (share, export)
- Can see research progress

**Recommendation:** Use API for automation in workflows, use Web UI for exploratory research or when API key is unavailable.

## API Cost Considerations

**Pricing:** Check current pricing at https://www.perplexity.ai/settings/api

**Typical costs (as of 2025):**
- Deep Research requests are more expensive than regular queries
- Cost varies by input/output tokens
- Monitor usage in Perplexity dashboard

**Cost optimization:**
- Keep prompts concise but specific
- Avoid redundant requests
- Cache results for reuse
- Set up usage alerts in Perplexity dashboard

## Best Practices

1. **Always verify .env file exists** before attempting API calls
2. **Test API key** with a simple request before running full research
3. **Log API responses** for debugging and verification
4. **Handle rate limits gracefully** with retry logic
5. **Escape special characters** in prompts (quotes, newlines)
6. **Set reasonable timeouts** (120-180 seconds for deep research)
7. **Parse JSON carefully** - check for 'choices' array existence
8. **Preserve citations** - don't strip formatting when processing output
9. **Monitor API usage** to avoid surprise costs

## Complete Example Workflow

```bash
# 1. Verify API key exists
if [ -f .env ]; then
    source .env
    if [ -z "$PERPLEXITY_API_KEY" ]; then
        echo "ERROR: PERPLEXITY_API_KEY not found in .env"
        exit 1
    fi
else
    echo "ERROR: .env file not found"
    exit 1
fi

# 2. Create research script
cat > /tmp/perplexity_research.py << 'EOF'
import requests
import os
from dotenv import load_dotenv

load_dotenv('/Users/valorengels/src/research/.env')

url = "https://api.perplexity.ai/chat/completions"
payload = {
    "model": "sonar-deep-research",
    "messages": [{"role": "user", "content": "PROMPT_HERE"}],
    "reasoning_effort": "high"
}
headers = {
    "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, timeout=180)
result = response.json()

if response.status_code == 200:
    print(result['choices'][0]['message']['content'])
else:
    print(f"ERROR: {response.status_code} - {result}")
EOF

# 3. Replace PROMPT_HERE with actual prompt (properly escaped)
# 4. Run the script
python3 /tmp/perplexity_research.py

# 5. Clean up
rm /tmp/perplexity_research.py
```

## Notes

- API is significantly faster than Gemini Deep Research API (30-120s vs 3-10 minutes)
- Requires paid API access (no free tier for sonar-deep-research model)
- Returns markdown-formatted text ideal for direct pasting into research-results.md
- Citations are inline with superscript numbers [1][2][3]
- Full source list provided at end with URLs
- Can handle complex, multi-faceted research queries
- Focuses on academic and authoritative sources
- No browser automation required - pure API call
- Perfect for automated workflows and CI/CD pipelines
