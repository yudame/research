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

**Time:** Research typically takes 30-120 seconds, but can take up to 10 minutes for complex queries. The script now has a 10-minute timeout with automatic retries.

**Output:** Comprehensive research report with inline citations and source links. Results are automatically saved to timestamped files to prevent data loss.

**Focus Areas:**
- Academic studies and peer-reviewed papers
- Meta-analyses and systematic reviews
- Official government/regulatory sources
- Authoritative industry reports

## Prerequisites

- Perplexity API key in repository `.env` or `/Users/valorengels/.env`
- Python 3.x with `requests` and `python-dotenv` installed
- API key from: https://www.perplexity.ai/settings/api

## API Key Setup

**Check if API key exists (checks repository .env first, then home directory):**

```bash
grep PERPLEXITY_API_KEY .env 2>/dev/null || grep PERPLEXITY_API_KEY /Users/valorengels/.env 2>/dev/null || echo "PERPLEXITY_API_KEY not found"
```

If not found, add to repository `.env` file (preferred) or global `.env` file:

```bash
# Preferred: Store in repository .env file
echo 'PERPLEXITY_API_KEY=pplx-your-api-key-here' >> .env

# Alternative: Store in global .env file (auto-loaded via ~/.zshenv)
echo 'PERPLEXITY_API_KEY=pplx-your-api-key-here' >> /Users/valorengels/.env
```

**Getting an API key:**
1. Go to https://www.perplexity.ai/settings/api
2. Sign in to your Perplexity account
3. Generate a new API key
4. Copy the key and add to `.env` file

## Complete Automation Workflow

### Step 1: Verify API Key

Use Bash to check if the API key is configured (checks repository .env first, then home directory):

```bash
grep PERPLEXITY_API_KEY .env 2>/dev/null || grep PERPLEXITY_API_KEY /Users/valorengels/.env 2>/dev/null || echo "PERPLEXITY_API_KEY not found"
```

If not found in either location, inform user to set up API key at https://www.perplexity.ai/settings/api

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
- `--timeout SECONDS` - Request timeout in seconds (default: 600 = 10 minutes)
- `--max-retries N` - Maximum retry attempts on failure (default: 3)
- `--quiet` - Minimal output (just the result)
- `--auto-save` - Automatically save output and logs with timestamp (enabled by default)
- `--no-auto-save` - Disable automatic file saving
- `--log-dir DIR` - Directory for output and log files

### Step 4: Monitor Progress

The script will:
1. Validate API key
2. Submit research request to Perplexity API
3. Wait for completion (30-120 seconds typical, up to 10 minutes maximum)
4. Automatically retry up to 3 times on timeout or failure
5. Auto-save results to timestamped files (prevents data loss)
6. Display results with word count and token usage

**Resilience features:**
- **10-minute timeout** (increased from 3 minutes) - handles longer research queries
- **Automatic retries** (3 attempts with exponential backoff) - handles transient failures
- **Auto-save by default** - results saved to `perplexity_output_TIMESTAMP.md` and `perplexity_log_TIMESTAMP.txt`
- **Separate log files** - progress and errors logged even if research fails
- **Configurable timeout** - use `--timeout` to adjust for very complex queries

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

**Auto-save is enabled by default** to prevent data loss. Results are saved automatically in two scenarios:

**1. With `--output` specified:**
```bash
python perplexity_deep_research.py \
  --file ../episodes/episode-dir/prompts.md \
  --output ../episodes/episode-dir/research/p2-perplexity.md
```

Files created:
- `research/p2-perplexity.md` - Research output
- `research/p2-perplexity_log.txt` - Progress log

**2. Without `--output` (auto-save with timestamp):**
```bash
python perplexity_deep_research.py "Research prompt here"
```

Files created in current directory:
- `perplexity_output_YYYYMMDD_HHMMSS.md` - Research output
- `perplexity_log_YYYYMMDD_HHMMSS.txt` - Progress log with errors/warnings

**Why auto-save by default?**
- **Prevents data loss** if terminal crashes or connection drops
- **Captures partial results** even if script times out
- **Logs all errors** for troubleshooting
- **Timestamped files** make it easy to find latest results

**Recommended workflow:**
```bash
# Run with explicit output file for episode structure
python perplexity_deep_research.py \
  --file ../episodes/episode-dir/logs/prompts.md \
  --output ../episodes/episode-dir/research/p2-perplexity.md

# If auto-saved to timestamped file, move it to episode directory
mv perplexity_output_*.md ../episodes/episode-dir/research/p2-perplexity.md
```

**Disable auto-save** (not recommended):
```bash
python perplexity_deep_research.py --no-auto-save "Research prompt"
# Results only printed to stdout, no files created
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
1. Check if `.env` file exists in repository root or home directory
2. Verify API key is set: `grep PERPLEXITY_API_KEY .env 2>/dev/null || grep PERPLEXITY_API_KEY /Users/valorengels/.env 2>/dev/null`
3. Get API key from https://www.perplexity.ai/settings/api
4. Add to repository `.env` (preferred): `echo 'PERPLEXITY_API_KEY=pplx-your-key-here' >> .env`

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

**Error:** `ERROR: Request timed out after 600 seconds (attempt X/3)`

**What this means:**
- The script automatically retried the request up to 3 times
- Each attempt waited longer with exponential backoff
- The query is taking longer than the 10-minute timeout

**Solution:**
- **Check auto-saved files** - Results may have been captured in `perplexity_output_TIMESTAMP.md`
- **Increase timeout** - Use `--timeout 900` (15 minutes) or `--timeout 1200` (20 minutes)
- **Reduce complexity** - Use `--reasoning-effort medium` instead of `high`
- **Simplify prompt** - Break into smaller research questions
- **Check logs** - Review `perplexity_log_TIMESTAMP.txt` for details

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
3. **Specify output file** using `--output` for organized file structure (auto-save is fallback)
4. **Let auto-save protect you** - don't disable unless you have a reason
5. **Check log files** if research fails - may contain partial results or error details
6. **Increase timeout for complex queries** - use `--timeout 900` or higher if needed
7. **Monitor API usage** to control costs
8. **Use specific prompts** - vague prompts waste API calls and may timeout
9. **Request citations explicitly** in prompts
10. **Trust the retries** - script will automatically retry up to 3 times on failure

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
  --timeout, -t SECONDS     Request timeout (default: 600 = 10 min)
  --max-retries N           Max retry attempts (default: 3)
  --auto-save               Enable auto-save (default: on)
  --no-auto-save            Disable auto-save (not recommended)
  --log-dir DIR             Directory for output/log files
  --quiet, -q               Minimal output

Examples:
  python perplexity_deep_research.py "Your prompt here"
  python perplexity_deep_research.py --file prompt.txt
  python perplexity_deep_research.py --file prompt.txt --output results.md
  python perplexity_deep_research.py --timeout 900 "Complex research query"
  python perplexity_deep_research.py --max-retries 5 --file prompt.txt
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
