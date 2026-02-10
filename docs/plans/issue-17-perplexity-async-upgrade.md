# Issue 17: Upgrade perplexity-deep-research to Async API

## Summary

Upgrade from synchronous Perplexity API (blocking 30-120s+) to the new Async API (June 2025). Fire-and-forget research with polling for results.

## Current State

- **Script**: `podcast/tools/perplexity_deep_research.py`
- **Skill**: `.claude/skills/perplexity-deep-research/SKILL.md`
- **API**: Synchronous `POST /chat/completions` with 10-minute timeout and retry logic
- **Pain points**: Blocking calls, timeout management, retry dance, no cost visibility

## New API Capabilities

### Async API (High Priority)
```
POST /async/chat/completions → { job_id: "abc123" }
GET /async/jobs/{job_id} → { status: "pending|complete", result: ... }
```
- Results stored 7 days
- No blocking, no timeouts
- Fire off research, poll when ready

### Rich Response Metadata (High Priority)
```json
{
  "citations": [{ "url": "...", "title": "..." }],
  "search_results": [{ "title": "...", "snippet": "...", "date": "..." }],
  "cost": {
    "input_tokens": 234,
    "output_tokens": 5678,
    "citation_tokens": 1200,
    "reasoning_tokens": 3400,
    "search_queries": 15
  }
}
```

### Granular Pricing (Medium Priority)
| Component | Cost |
|-----------|------|
| Input tokens | $2/M |
| Output tokens | $8/M |
| Citation tokens | $2/M |
| Reasoning tokens | $3/M |
| Search queries | $5/1K |

Typical deep research: $0.50-$1.00

### Streaming (Low Priority)
Stream results as they generate (optional enhancement).

## Implementation Plan

### Phase 1: Core Async Implementation

**File: `podcast/tools/perplexity_deep_research.py`**

1. Add async submission function:
```python
def submit_async_research(prompt: str, reasoning_effort: str = "high") -> str:
    """Submit research job, return job_id."""
    url = "https://api.perplexity.ai/async/chat/completions"
    payload = {
        "model": "sonar-deep-research",
        "messages": [{"role": "user", "content": prompt}],
        "reasoning_effort": reasoning_effort
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["job_id"]
```

2. Add polling function:
```python
def poll_async_result(job_id: str, timeout: int = 600, poll_interval: int = 10) -> dict:
    """Poll for job completion, return full result with metadata."""
    url = f"https://api.perplexity.ai/async/jobs/{job_id}"
    start = time.time()
    while time.time() - start < timeout:
        response = requests.get(url, headers=headers)
        data = response.json()
        if data["status"] == "complete":
            return data
        time.sleep(poll_interval)
    raise TimeoutError(f"Job {job_id} not complete after {timeout}s")
```

3. Add CLI flags:
```
--async              Use async API (default: True for new behavior)
--sync               Force synchronous API (legacy)
--job-id ID          Poll existing job instead of submitting new
--no-wait            Submit and return job_id immediately (don't poll)
```

4. Remove retry/timeout complexity (async handles this server-side)

### Phase 2: Rich Metadata & Cost Tracking

1. Parse and display new response fields:
```python
def format_metadata(result: dict) -> str:
    """Format citations, search results, and cost breakdown."""
    citations = result.get("citations", [])
    cost = result.get("cost", {})

    output = []
    output.append(f"Citations: {len(citations)}")
    output.append(f"Cost breakdown:")
    output.append(f"  Input: ${cost.get('input_tokens', 0) * 2 / 1_000_000:.4f}")
    output.append(f"  Output: ${cost.get('output_tokens', 0) * 8 / 1_000_000:.4f}")
    # etc.
    return "\n".join(output)
```

2. Save structured citations to separate file:
```
research/p2-perplexity.md          # Research content
research/p2-perplexity_meta.json   # Structured citations, costs, search results
```

3. Add `--show-cost` flag to display cost breakdown

### Phase 3: Skill Documentation Update

**File: `.claude/skills/perplexity-deep-research/SKILL.md`**

1. Update workflow to use async:
```bash
# Submit research (returns immediately)
python perplexity_deep_research.py --no-wait "Research prompt"
# Output: Job submitted: abc123

# Later, poll for results
python perplexity_deep_research.py --job-id abc123 --output results.md
```

2. Document new response metadata format
3. Update cost section with granular pricing
4. Remove timeout/retry troubleshooting (no longer needed)
5. Add job management section (list pending jobs, check status)

### Phase 4: Workflow Integration

1. Update podcast episode workflow to leverage async:
   - Phase 3 can fire off all research tools in parallel
   - Each returns job_id immediately
   - Poll all jobs at end of research phase

2. Add job tracking file:
```yaml
# podcast/episodes/YYYY-MM-DD-slug/research/jobs.yaml
perplexity:
  job_id: abc123
  submitted: 2025-06-15T10:30:00
  status: pending
gemini:
  job_id: def456
  submitted: 2025-06-15T10:30:05
  status: complete
```

## Files to Modify

| File | Changes |
|------|---------|
| `podcast/tools/perplexity_deep_research.py` | Add async submit/poll, metadata parsing, cost tracking |
| `.claude/skills/perplexity-deep-research/SKILL.md` | Update workflow, document async API, new metadata |
| `.claude/skills/new-podcast-episode.md` | Update Phase 3 to use async fire-and-forget pattern |

## Testing Plan

1. Test async submission returns valid job_id
2. Test polling with short/long research queries
3. Test job_id retrieval for existing jobs
4. Test metadata parsing (citations, costs, search_results)
5. Test --no-wait + later --job-id workflow
6. Test integration with podcast episode workflow

## Rollout

1. Implement async alongside existing sync (--sync flag for fallback)
2. Default to async for new calls
3. After validation, deprecate sync path
4. Update skill to async-first documentation

## Estimated Time

- Phase 1 (Core Async): 2-3 hours
- Phase 2 (Metadata): 1-2 hours
- Phase 3 (Docs): 1 hour
- Phase 4 (Workflow): 1-2 hours
- **Total: 5-8 hours**

## Dependencies

- Perplexity API key with async access
- Verify async endpoint URL (may need API docs check)
