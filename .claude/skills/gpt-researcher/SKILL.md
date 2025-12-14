---
name: gpt-researcher
description: Run GPT-Researcher multi-agent deep research framework locally. Alternative to Perplexity/ChatGPT/Claude Deep Research. Researches 100+ sources in parallel, provides comprehensive citations, benchmarks competitively. Use for Phase 1 academic foundation or Phase 3 comprehensive synthesis. Supports multiple LLM providers (OpenAI, Anthropic, xAI, OpenRouter). Takes 6-20 min depending on report type.
---

# GPT-Researcher Skill

Use this skill to run GPT-Researcher's multi-agent deep research framework locally.

## What is GPT-Researcher?

GPT-Researcher is an autonomous multi-agent research framework that:
- Uses **parallel agent execution** for faster research
- **Researches 100+ sources** across the web
- Provides **comprehensive citations** and source validation
- Benchmarks **competitively with ChatGPT Deep Research and Claude Research**
- Supports **multiple LLM providers** (OpenAI, Anthropic, xAI, OpenRouter)

**Carnegie Mellon Benchmark (DeepResearchGym, May 2025):**
GPT-Researcher **outperformed** Perplexity, OpenAI Deep Research, and other tools on:
- Citation quality
- Report quality
- Information coverage

## When to Use This Skill

Use GPT-Researcher for deep research tasks in the podcast episode workflow:

1. **Phase 1: Academic Foundation** (alternative to Perplexity API)
2. **Phase 3: Comprehensive Synthesis** (alternative to ChatGPT/Claude Deep Research)
3. **Any multi-dimensional research** requiring parallel information gathering

## Configuration

API keys are auto-discovered from `.env` files in:
- `/Users/valorengels/src/research/.env` (root)
- `/Users/valorengels/src/research/podcast/tools/.env` (tools)

**Available providers:**
- **OpenAI**: `OPENAI_API_KEY` (GPT-4, GPT-4o, etc.)
- **Anthropic**: `ANTHROPIC_API_KEY` (Claude Opus, Sonnet)
- **OpenRouter**: `OPENROUTER_API_KEY` (unified access to 400+ models including Claude, GPT-4, Grok)
- **xAI**: `XAI_API_KEY` (Grok models)

## Usage

### Basic Usage

```bash
cd /Users/valorengels/src/research/podcast/tools
python gpt_researcher_run.py "Your research prompt here"
```

### Read Prompt from File

```bash
cd /Users/valorengels/src/research/podcast/tools
python gpt_researcher_run.py --file ../episodes/YYYY-MM-DD-slug/prompt.txt
```

### Specify Model Provider

```bash
# Use OpenAI GPT-4o (default)
python gpt_researcher_run.py "prompt" --model openai:gpt-4o

# Use Anthropic Claude Opus 4
python gpt_researcher_run.py "prompt" --model anthropic:claude-opus-4

# Use xAI Grok
python gpt_researcher_run.py "prompt" --model xai:grok-beta

# Use OpenRouter for Claude Opus 4.5
python gpt_researcher_run.py "prompt" --model openrouter/anthropic/claude-opus-4.5
```

### Save to File

```bash
python gpt_researcher_run.py "prompt" --output results.md
```

### Report Types

```bash
# Standard research report (default, 6-10 min)
python gpt_researcher_run.py "prompt" --report-type research_report

# Detailed comprehensive report (10-20 min)
python gpt_researcher_run.py "prompt" --report-type detailed_report

# Quick report (3-5 min, fewer sources)
python gpt_researcher_run.py "prompt" --report-type quick_report
```

## Integration with Podcast Workflow

### Phase 1: Academic Foundation (Alternative to Perplexity)

**Use Case:** Quick academic research with GPT-4 or Claude Opus

```bash
cd podcast/tools
python gpt_researcher_run.py --file ../episodes/YYYY-MM-DD-slug/phase1_prompt.txt \
    --model openai:gpt-4o \
    --report-type quick_report \
    --output ../episodes/YYYY-MM-DD-slug/research-results-gptr.md
```

**Expected time:** 3-5 minutes
**Output:** Quick academic overview with 30-50 sources

### Phase 3: Comprehensive Synthesis (Alternative to ChatGPT/Claude Deep Research)

**Use Case:** Deep multi-dimensional research with comprehensive synthesis

```bash
cd podcast/tools
python gpt_researcher_run.py --file ../episodes/YYYY-MM-DD-slug/phase3_prompt.txt \
    --model anthropic:claude-opus-4 \
    --report-type detailed_report \
    --output ../episodes/YYYY-MM-DD-slug/research-results-gptr-detailed.md
```

**Expected time:** 10-20 minutes
**Output:** Comprehensive report with 100+ sources, multi-agent synthesis

### Using OpenRouter for Multi-Provider Access

**Use Case:** Single API key for all providers

```bash
# Claude Opus 4.5 via OpenRouter
python gpt_researcher_run.py "prompt" --model openrouter/anthropic/claude-opus-4.5

# GPT-4o via OpenRouter
python gpt_researcher_run.py "prompt" --model openrouter/openai/gpt-4o

# Grok via OpenRouter
python gpt_researcher_run.py "prompt" --model openrouter/x-ai/grok-4
```

**Advantage:** Only need `OPENROUTER_API_KEY` instead of multiple API keys

## Output Format

The script outputs markdown-formatted research with:
- **Header:** Date, model, prompt
- **Research report:** Comprehensive findings with structure
- **Citations:** Inline citations with source URLs
- **Sources:** List of sources researched

Example output structure:
```markdown
# GPT-Researcher Results

**Date:** 2025-12-14 14:30

**Model:** anthropic:claude-opus-4

**Prompt:** Research early childhood educator burnout interventions

---

## Executive Summary
[Comprehensive overview]

## Key Findings
[Detailed findings with citations]

## Methodology Considerations
[Study quality notes]

## Sources
[List of 100+ sources with URLs]
```

## Implementation Steps (from Claude Code)

When invoking this skill from Claude Code:

1. **Create the research prompt** based on episode topic
2. **Write prompt to temporary file** (or pass directly)
3. **Invoke the script** with appropriate model and report type
4. **Wait for completion** (6-20 minutes depending on report type)
5. **Read the output** and format for `research-results.md`

Example:
```python
# In Claude Code tool call
cd podcast/tools
python gpt_researcher_run.py \
    "Research [TOPIC] with comprehensive methodology..." \
    --model anthropic:claude-opus-4 \
    --report-type detailed_report \
    --output /tmp/gptr_results.md
```

## Troubleshooting

### Error: "No API keys found"
- Check `.env` files exist in root or `podcast/tools/`
- Ensure at least one API key is set: `OPENAI_API_KEY`, `OPENROUTER_API_KEY`, etc.
- Verify `.env` format: `KEY=value` (no spaces around `=`)

### Error: "gpt-researcher not installed"
- Run: `cd podcast/tools && source .venv/bin/activate && pip install gpt-researcher`

### Research times out or fails
- Try `--report-type quick_report` for faster results
- Check API key has sufficient credits
- Use `--quiet` flag and check for specific error messages

### Model not found
- For OpenRouter models, use format: `openrouter/provider/model`
- Check model names at https://openrouter.ai/models
- For native providers, use format: `provider:model`

## Comparison: GPT-Researcher vs. Dedicated Tools

| Feature | GPT-Researcher | ChatGPT Deep Research | Claude Research |
|---------|----------------|----------------------|-----------------|
| **Multi-agent architecture** | ✅ | ✅ | ✅ |
| **Citation quality** | ⭐️ Best (CMU benchmark) | ⭐️ High | ⭐️ High |
| **Report quality** | ⭐️ Best (CMU benchmark) | ⭐️ High | ⭐️ High |
| **Sources analyzed** | 100+ | 25-50 | 260-427 |
| **Processing time** | 6-20 min | 10-20 min | 6-10 min |
| **Cost** | $0.27-2/search | $200/mo | $125/mo |
| **Local control** | ✅ | ❌ | ❌ |
| **Multi-provider** | ✅ | ❌ | ❌ |
| **Benchmark performance** | ⭐️ CMU winner | ⭐️ 26.6% HLE | ⭐️ 90.2% vs single-agent |

**Conclusion:** GPT-Researcher is the only open source tool that benchmarks competitively with commercial deep research features, especially when using top-tier models (GPT-4o, Claude Opus 4).

## Advanced Configuration

### Environment Variables

GPT-Researcher uses these environment variables (set in `.env`):

```bash
# Required: At least one API key
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
OPENROUTER_API_KEY=sk-or-...
XAI_API_KEY=...

# Optional: Model selection (override with --model flag)
FAST_LLM=openai:gpt-4o          # Quick tasks
SMART_LLM=anthropic:claude-opus-4  # Deep analysis
STRATEGIC_LLM=anthropic:claude-opus-4  # Planning

# Optional: Search provider
SEARCH_PROVIDER=tavily  # Default
```

### Custom Configurations

The wrapper script automatically configures:
- Model selection via `--model` flag
- Report type via `--report-type` flag
- Output formatting for podcast workflow

No manual configuration needed!

## Notes

- **Processing time:** Budget 10-20 minutes for detailed reports
- **Parallel execution:** Can run multiple research sessions if needed
- **API costs:** Typically $0.27-2 per research session (varies by model and sources)
- **Quality:** Competitive with ChatGPT Deep Research on benchmarks
- **Local execution:** Runs on your machine, full control over configuration
