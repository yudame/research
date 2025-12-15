---
name: perplexity-deep-research
description: Automate Perplexity Deep Research API calls using sonar-deep-research model. Use for Phase 1 academic research in podcast episodes. Handles API key verification, script execution (30-120s), and result formatting with citations. Returns research ready to paste into research-results.md.
---

# Perplexity Deep Research API Automation

This skill automates research using Perplexity's Deep Research API - simple, fast API calls with no browser automation.

## Overview

The Perplexity Deep Research API provides programmatic access to comprehensive research:
1. Conducts multi-step research process
2. Searches across academic databases, official sources, peer-reviewed journals
3. Synthesizes findings with proper citations
4. Returns structured markdown-formatted reports

**Time:** Research typically takes 30-120 seconds (fastest of all deep research tools).

**Output:** Comprehensive research report with inline citations and source links.

**Focus Areas:**
- Academic studies and peer-reviewed papers
- Meta-analyses and systematic reviews
- Official government/regulatory sources
- Authoritative industry reports

## Prerequisites

- Perplexity API key in `.env` file
- Python 3.x with `requests` and `python-dotenv` installed
- API key from: https://www.perplexity.ai/settings/api

## API Key Setup

**Check if API key exists:**

```bash
grep PERPLEXITY_API_KEY .env
```

If not found, add to `.env` file:

```bash
# In .env file
PERPLEXITY_API_KEY=pplx-your-api-key-here
```

**Getting an API key:**
1. Go to https://www.perplexity.ai/settings/api
2. Sign in to your Perplexity account
3. Generate a new API key
4. Copy the key and add to `.env` file

## Complete Automation Workflow

### Step 1: Verify API Key

Use Bash to check if the API key is configured:

```bash
grep PERPLEXITY_API_KEY .env
```

If not found, inform user to set up API key at https://www.perplexity.ai/settings/api

### Step 2: Prepare Research Prompt

The research prompt should be saved in the episode's `prompts.md` file under the Perplexity Deep Research section.

**Prompt format (3 lines, single newlines):**
```
Research [TOPIC].
Focus on peer-reviewed studies, meta-analyses, systematic reviews, and official government/regulatory sources.
Provide comprehensive findings with full citations, sample sizes, methodological details, and source URLs.
```

### Step 3: Run Research via Python Script

Execute the Python script using Bash:

```bash
cd /Users/valorengels/src/research/podcast/tools
python perplexity_deep_research.py --file ../episodes/[episode-dir]/prompts.md --output ../episodes/[episode-dir]/perplexity-results.md
```

Or with inline prompt:

```bash
python perplexity_deep_research.py "Research prompt here"
```

**Available options:**
- `--file FILEPATH` - Read prompt from file
- `--output FILEPATH` - Write results to file
- `--reasoning-effort LEVEL` - Effort level: low, medium, high (default: high)
- `--quiet` - Minimal output (just the result)

### Step 4: Monitor Progress

The script will:
1. Validate API key
2. Submit research request to Perplexity API
3. Wait for completion (30-120 seconds)
4. Display results with word count and token usage

**Expected output:**
```
==============================================================
PERPLEXITY DEEP RESEARCH API
==============================================================

Prompt: Research Solomon Islands telecommunications...

Configuration:
  Model: sonar-deep-research
  Reasoning Effort: high

Submitting research request...
Expected time: 30-120 seconds
--------------------------------------------------------------

API Usage:
  Input tokens: 234
  Output tokens: 5678
  Total tokens: 5912

==============================================================
RESEARCH COMPLETE
Length: ~4500 words
==============================================================
```

### Step 5: Extract and Save Results

If `--output` was specified, results are automatically saved to the file.

Otherwise, the script prints results to stdout and you should:
1. Copy the research output
2. Paste into the episode's `research-results.md` under the Perplexity section

**Recommended workflow:**
```bash
# Run with output file
python perplexity_deep_research.py \
  --file ../episodes/episode-dir/prompts.md \
  --output ../episodes/episode-dir/perplexity-results.md

# Append to research-results.md
cat ../episodes/episode-dir/perplexity-results.md >> ../episodes/episode-dir/research-results.md
```

## API Details

**Base URL:** `https://api.perplexity.ai/chat/completions`

**Model:** `sonar-deep-research`

**Request Format:**
```json
{
  "model": "sonar-deep-research",
  "messages": [
    {
      "role": "user",
      "content": "Research prompt here"
    }
  ],
  "reasoning_effort": "high"
}
```

**Response Format:**
```json
{
  "id": "request-id",
  "model": "sonar-deep-research",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Research report content with citations..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 234,
    "completion_tokens": 5678,
    "total_tokens": 5912
  }
}
```

## Error Handling

### API Key Errors

**Error:** `ERROR: PERPLEXITY_API_KEY not found`

**Solution:**
1. Check `.env` file exists in repository root
2. Verify API key is set: `grep PERPLEXITY_API_KEY .env`
3. Get API key from https://www.perplexity.ai/settings/api
4. Add to `.env`: `PERPLEXITY_API_KEY=pplx-your-key-here`

### API Request Failures

**Error:** `ERROR: Authentication failed (401 Unauthorized)`

**Solution:**
- API key is invalid or expired
- Verify key at https://www.perplexity.ai/settings/api
- Regenerate key if needed

**Error:** `ERROR: Rate limit exceeded (429 Too Many Requests)`

**Solution:**
- Wait 60 seconds and retry
- Check usage at https://www.perplexity.ai/settings/api
- Upgrade plan if needed

**Error:** `ERROR: Request timed out after 180 seconds`

**Solution:**
- Research query too complex
- Simplify the prompt or break into smaller tasks
- Use `--reasoning-effort medium` instead of `high`

**Error:** `ERROR: Perplexity API server error (500)`

**Solution:**
- Service experiencing issues
- Wait 30 seconds and retry
- Check Perplexity status page
- Use alternative tool if persistent

### Python Errors

**Error:** `ModuleNotFoundError: No module named 'requests'`

```bash
pip3 install requests python-dotenv
```

## Integration with Podcast Workflow

When called from the podcast episode workflow:

**Input needed:**
- Research prompt from `prompts.md` (Perplexity section)
- Episode directory path

**Expected output:**
- Success: Full research report with citations saved to file
- Failure: Error message with troubleshooting steps

**Workflow integration example:**

```bash
# Phase 1: Research Execution - Perplexity Deep Research
EPISODE_DIR="podcast/episodes/2024-12-14-topic-slug"

# Run Perplexity research
cd podcast/tools
python perplexity_deep_research.py \
  --file "../${EPISODE_DIR}/prompts.md" \
  --output "../${EPISODE_DIR}/research-results-perplexity.md" \
  --reasoning-effort high

# Check if successful
if [ $? -eq 0 ]; then
  echo "Perplexity research complete"
  # Append to main research results
  cat "../${EPISODE_DIR}/research-results-perplexity.md" >> "../${EPISODE_DIR}/research-results.md"
else
  echo "Perplexity research failed - check error messages"
fi
```

## Why API-Based Automation

This skill uses the official Perplexity Deep Research API for maximum reliability:

- **Fast:** 30-120 seconds (fastest deep research option)
- **Stable:** No UI changes breaking automation
- **Simple:** Just API key configuration needed
- **Scriptable:** Fully automated, no browser required
- **Portable:** Works in any environment with Python and internet
- **Official:** Direct API access to Perplexity's research agent
- **Maintainable:** API contracts are stable and documented

## Best Practices

1. **Always verify API key** before running research
2. **Use high reasoning effort** for podcast research (default)
3. **Save output to file** using `--output` flag
4. **Handle errors gracefully** - check exit code before continuing
5. **Monitor API usage** to control costs
6. **Use specific prompts** - vague prompts waste API calls
7. **Request citations explicitly** in prompts
8. **Test with simple prompts** before complex research

## Example Commands

**Basic research:**
```bash
python perplexity_deep_research.py "Research quantum computing applications"
```

**From file with output:**
```bash
python perplexity_deep_research.py \
  --file research-prompt.txt \
  --output results.md
```

**Medium effort (faster, less comprehensive):**
```bash
python perplexity_deep_research.py \
  --reasoning-effort medium \
  "Research climate change policy in Pacific nations"
```

**Quiet mode (just results):**
```bash
python perplexity_deep_research.py \
  --quiet \
  --file prompt.txt \
  --output results.md
```

## Script Location

**Path:** `/Users/valorengels/src/research/podcast/tools/perplexity_deep_research.py`

**Usage:**
```
python perplexity_deep_research.py [OPTIONS] [PROMPT]

Options:
  --file, -f PATH           Read prompt from file
  --output, -o PATH         Write output to file
  --reasoning-effort LEVEL  Effort: low, medium, high (default: high)
  --quiet, -q               Minimal output

Examples:
  python perplexity_deep_research.py "Your prompt here"
  python perplexity_deep_research.py --file prompt.txt
  python perplexity_deep_research.py --file prompt.txt --output results.md
```

## Comparison to Other Tools

| Feature | Perplexity | Gemini | GPT-Researcher |
|---------|-----------|--------|----------------|
| Speed | 30-120s | 3-10 min | 6-20 min |
| Cost | $$$ | $$ | $ (varies) |
| Academic Focus | ✓✓✓ | ✓ | ✓✓ |
| Policy/Regulatory | ✓ | ✓✓✓ | ✓✓ |
| Citations | Inline | Inline | Comprehensive |
| API-Based | ✓ | ✓ | ✓ |

**Recommendation:** Use Perplexity for Phase 1 academic research when speed and scholarly sources are priorities.

## API Cost Considerations

**Pricing:** Check current pricing at https://www.perplexity.ai/settings/api

**Typical costs:**
- Deep Research requests use significant tokens (5000-15000 output tokens)
- Cost varies by input/output tokens
- Monitor usage in Perplexity dashboard

**Cost optimization:**
- Keep prompts concise but specific
- Use `--reasoning-effort medium` for less critical research
- Avoid redundant requests
- Cache results for reuse

## Notes

- Fastest deep research option (30-120s vs 3-20 min for alternatives)
- Requires paid API access
- Returns markdown-formatted text ideal for direct pasting
- Citations are inline with superscript numbers [1][2][3]
- Full source list provided at end with URLs
- Focuses on academic and authoritative sources
- No browser automation required - pure API call
- Perfect for automated workflows and CI/CD pipelines
