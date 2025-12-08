# Product Requirements Document: Deep Research Automation Skills

**Version:** 1.0
**Date:** 2025-12-08
**Status:** Draft
**Owner:** Valor Engels

---

## Executive Summary

Build 5 Claude Code skills that automate deep research workflows by controlling browser interactions with authenticated sessions on Claude.ai, ChatGPT, Gemini, Grok, and Perplexity platforms. These skills integrate with the Podcast Episode V2 workflow to enable parallel, verified, multi-source research with cross-validation.

**Business Value:**
- Reduce manual research time from 60+ minutes to ~30 minutes (automated parallel execution)
- Improve research quality through multi-source verification
- Eliminate copy-paste errors and formatting inconsistencies
- Enable reproducible research workflows
- Create audit trail of all research sources

---

## Context & Background

### Current Workflow Pain Points

**Manual Process (Current State):**
1. User manually runs research prompts in 4-5 different tools sequentially or in parallel
2. User copies each result and pastes into `research-results.md` with proper formatting
3. User manually cross-validates facts across sources
4. User creates verification matrix in spreadsheet or markdown
5. User compiles master research briefing organized by topic
6. Total time: 60-90 minutes per episode

**Problems:**
- Error-prone copy/paste between platforms
- Formatting inconsistencies
- Easy to miss contradictions across sources
- No structured verification process
- Difficult to reproduce research
- Browser tab juggling and context switching

### Integration with Podcast Workflow V2

This PRD implements automation for **Phase 2 (Parallel Deep Research)** of the podcast episode workflow defined in `.claude/skills/new-podcast-episode-v2.md`.

**Workflow Integration:**
```
[User initiates episode]
    ↓
[Claude Code creates episode structure]
    ↓
[Claude Code generates differentiated prompts for 5 platforms]
    ↓
→ [AUTOMATED: Deep research skills run in parallel] ← THIS PRD
    ↓
[AUTOMATED: Results saved to research-results.md]
    ↓
[Claude Code creates cross-validation matrix]
    ↓
[Rest of workflow continues...]
```

**Expected Outcome:**
- Single command triggers all research
- Structured output ready for validation
- 30 minutes saved per episode
- Higher consistency and quality

---

## Goals & Non-Goals

### Goals

**Primary:**
1. ✅ Automate deep research execution across 5 platforms simultaneously
2. ✅ Produce standardized, structured output compatible with cross-validation
3. ✅ Maintain complete source attribution and metadata
4. ✅ Enable reproducible research workflows
5. ✅ Integrate seamlessly with podcast episode workflow

**Secondary:**
1. ✅ Capture progress indicators and timing data
2. ✅ Handle errors gracefully with partial results
3. ✅ Support both headless and visible browser modes
4. ✅ Provide debugging artifacts (screenshots, logs)

### Non-Goals

**Explicitly Out of Scope:**
1. ❌ Automating login/authentication (assumes existing authenticated Chrome profile)
2. ❌ Building a web UI for research management
3. ❌ Real-time collaboration features
4. ❌ Research synthesis/analysis (handled by Claude Opus 4.5 separately)
5. ❌ API-based access (this is browser automation for UI-only features)
6. ❌ Mobile/tablet browser automation
7. ❌ Handling CAPTCHA/bot detection (assumes authenticated sessions bypass this)

---

## User Stories & Use Cases

### Primary User Story

**As a** podcast researcher,
**I want** to automatically run the same research query across 5 AI platforms in parallel,
**So that** I can gather diverse sources, cross-validate facts, and complete research in 30 minutes instead of 90 minutes.

**Acceptance Criteria:**
- [ ] Single command triggers all 5 platforms
- [ ] Results appear in standardized format in `research-results.md`
- [ ] Each platform's output includes citations with URLs
- [ ] Completion within 10 minutes (5-platform parallel execution)
- [ ] Success rate >90% across all platforms

### Use Case 1: Standard Episode Research

**Context:** Creating a new podcast episode on "Solomon Islands Telecom Competition"

**Steps:**
1. User runs: `research_orchestrator("Solomon Islands telecom market structure and competition dynamics")`
2. System launches 5 browser contexts in parallel:
   - Perplexity: Academic/official sources
   - Grok: Real-time/regional news
   - ChatGPT: Industry reports
   - Gemini: Strategic analysis
   - Claude: Comprehensive synthesis
3. System monitors progress of all 5 executions
4. System saves structured results to `research-results.md`
5. User reviews results and proceeds to cross-validation

**Expected Duration:** 8-12 minutes (parallel execution)

### Use Case 2: Partial Failure Recovery

**Context:** One platform times out or hits rate limit

**Steps:**
1. User runs orchestrator
2. Perplexity completes successfully (3 min)
3. Grok completes successfully (5 min)
4. ChatGPT completes successfully (4 min)
5. Gemini times out after 10 min (partial results captured)
6. Claude completes successfully (6 min)
7. System saves 4 complete results + 1 partial result
8. User reviews what completed and decides whether to retry Gemini

**Expected Behavior:**
- Partial results saved with `timeout: true` flag
- User notified which platform(s) failed
- Failed platforms can be retried individually
- No loss of successful results

### Use Case 3: Verification & Debugging

**Context:** User suspects one platform hallucinated a statistic

**Steps:**
1. User checks `research-results.md` and sees conflicting statistics
2. User opens `prompts.md` to see exact prompt used for each platform
3. User checks screenshot artifacts to verify what was displayed
4. User re-runs single platform with adjusted prompt if needed
5. User manually verifies suspicious source URLs

**Expected Capability:**
- Full audit trail of prompts used
- Screenshots of final results
- Timing data to identify suspicious fast completions
- Source URLs preserved for manual verification

---

## Functional Requirements

### Core Skills (5 Platform Automations)

Each skill must implement:

#### FR-1: Platform Authentication Verification
- **Requirement:** Detect if user is authenticated before starting research
- **Implementation:** Check for presence of user avatar/menu element
- **Success Criteria:** Return clear error if not authenticated
- **Error Handling:** Provide instructions to manually login in visible browser

#### FR-2: Deep Research Mode Activation
- **Requirement:** Trigger the platform's deep/comprehensive research mode
- **Platform-Specific:**
  - **Claude:** Enable "Research" toggle in chat UI
  - **ChatGPT:** Select "o1-pro" or research preview model (NOT standard GPT-4)
  - **Perplexity:** Select "Pro Search" mode with academic focus
  - **Gemini:** Use Gemini Deep Research (separate feature, requires explicit access)
  - **Grok:** Enable "Search" mode with real-time web access
- **Success Criteria:** Correct mode activated >95% of the time
- **Verification:** Screenshot of UI showing mode indicator

#### FR-3: Query Submission with Differentiated Prompts
- **Requirement:** Each platform receives a customized prompt optimized for its strengths
- **Input:** Base research query from user
- **Transformation:** Apply platform-specific prompt template from V2 workflow
- **Example:**
  ```python
  base_query = "Solomon Islands telecom market structure"

  # Perplexity gets:
  "Research Solomon Islands telecom market structure. Focus on academic studies,
   regulatory documents, and official statistics. Provide full citations..."

  # Grok gets:
  "Research Solomon Islands telecom market structure. Focus on recent news (last
   12 months), regional sources, and X/Twitter discussions from industry experts..."
  ```
- **Success Criteria:** Correct prompt template applied per platform

#### FR-4: Progress Monitoring
- **Requirement:** Track research progress and provide status updates
- **Implementation:**
  - Monitor for platform-specific progress indicators
  - Log timing of each research phase
  - Detect stalled executions (no progress for 60 seconds)
- **Status Updates:**
  - "Research started" (timestamp)
  - "Searching sources" (count if visible)
  - "Generating report" (timestamp)
  - "Complete" or "Timeout" (timestamp)
- **Success Criteria:** Progress logs updated every 10-30 seconds

#### FR-5: Completion Detection
- **Requirement:** Accurately detect when research is complete
- **Platform-Specific Indicators:**
  - **Claude:** "Research complete" message + citations visible
  - **ChatGPT:** Response streaming stopped + "Finished" indicator
  - **Perplexity:** Answer section populated + all citations loaded
  - **Gemini:** Response complete indicator (may be subtle)
  - **Grok:** Answer rendered + sources section visible
- **Fallback:** Content stability (no changes for 3 seconds)
- **Timeout:** Maximum wait time per platform (5-10 minutes)
- **Success Criteria:** Completion detected within 5 seconds of actual completion

#### FR-6: Structured Data Extraction
- **Requirement:** Extract research content in standardized format
- **Output Schema:**
  ```python
  {
    "platform": str,  # "claude", "chatgpt", "perplexity", "grok", "gemini"
    "query": str,  # Actual prompt sent to platform
    "content": str,  # Full research report
    "sections": List[{  # If platform provides structured sections
      "heading": str,
      "content": str,
      "level": int  # h1, h2, h3
    }],
    "sources": List[{
      "number": int,  # Citation number if applicable
      "url": str,
      "title": str,
      "description": Optional[str],
      "type": str,  # "academic", "news", "official", "industry", "social"
      "date": Optional[str],  # Publication date if available
      "author": Optional[str]
    }],
    "metadata": {
      "model": Optional[str],  # Model used if visible
      "start_time": str,  # ISO 8601
      "end_time": str,
      "duration_seconds": float,
      "timeout": bool,
      "partial_results": bool,
      "search_queries": List[str],  # If platform shows searches
      "source_count": int,
      "error": Optional[str]
    },
    "artifacts": {
      "screenshot_path": Optional[str],
      "html_path": Optional[str],  # Raw HTML for debugging
      "markdown_export": Optional[str]  # If platform supports export
    }
  }
  ```
- **Success Criteria:** All fields populated correctly >90% of the time

#### FR-7: Source Quality Classification
- **Requirement:** Classify each source by quality tier
- **Classification Logic:**
  ```python
  def classify_source(url: str, title: str, description: str) -> str:
      # Tier 1: Meta-analyses, systematic reviews, official statistics
      if any(x in title.lower() for x in ["meta-analysis", "systematic review"]):
          return "tier_1_meta_analysis"
      if any(x in url for x in [".gov", "worldbank.org", "imf.org", "who.int"]):
          return "tier_1_official"

      # Tier 2: Peer-reviewed studies, RCTs, government reports
      if any(x in url for x in ["pubmed", "scholar.google", "arxiv", "doi.org"]):
          return "tier_2_academic"
      if ".gov" in url and "report" in title.lower():
          return "tier_2_government_report"

      # Tier 3: News, industry reports, case studies
      if any(x in url for x in ["reuters.com", "bloomberg.com", "ft.com"]):
          return "tier_3_news_premium"
      if any(x in title.lower() for x in ["case study", "white paper"]):
          return "tier_3_industry"

      # Default: general web source
      return "tier_3_web"
  ```
- **Success Criteria:** Sources classified with >85% accuracy (manual validation)

#### FR-8: Error Handling & Recovery
- **Requirement:** Handle all failure modes gracefully
- **Error Scenarios:**
  | Error Type | Detection | Response |
  |------------|-----------|----------|
  | Not authenticated | No user avatar visible | Return error with instructions |
  | Feature unavailable | "Upgrade" or "Pro only" message | Return error noting account limitation |
  | Rate limit | "Limit reached" message | Save error with retry-after timestamp |
  | Timeout | No completion after max wait | Save partial results with timeout flag |
  | Network error | Browser navigation fails | Retry 3x with exponential backoff |
  | Content extraction failure | Selectors not found | Save screenshot, return error |
- **Success Criteria:** All error types handled without crashes

### Orchestrator Skill

#### FR-9: Parallel Execution
- **Requirement:** Run all 5 platform skills simultaneously
- **Implementation:**
  ```python
  def parallel_research(base_query: str, platforms: List[str]) -> dict:
      with ThreadPoolExecutor(max_workers=5) as executor:
          futures = {
              executor.submit(run_platform, platform, base_query): platform
              for platform in platforms
          }

          results = {}
          for future in as_completed(futures):
              platform = futures[future]
              try:
                  results[platform] = future.result(timeout=600)
              except TimeoutError:
                  results[platform] = {"error": "timeout", "partial": True}
              except Exception as e:
                  results[platform] = {"error": str(e)}

      return results
  ```
- **Success Criteria:** All 5 platforms execute in parallel (not sequential)

#### FR-10: Results Aggregation
- **Requirement:** Combine results from all platforms into `research-results.md`
- **Output Format:**
  ```markdown
  # Research Results for [Episode Title]

  Research Date: YYYY-MM-DD HH:MM:SS
  Base Query: [Query]
  Platforms: 5 (Claude, ChatGPT, Perplexity, Grok, Gemini)
  Successful: 4/5 (Gemini timed out)
  Total Duration: 8m 42s

  ---

  ## Research from Perplexity (Academic & Official Sources)

  **Status:** ✅ Complete
  **Duration:** 3m 24s
  **Model:** Pro Search
  **Sources Found:** 47
  **Prompt Used:**
  ```
  [Full prompt here]
  ```

  **Results:**

  [Full content from Perplexity]

  **Sources:**
  1. [Title](URL) - Official/Academic/News - YYYY-MM-DD
  2. [Title](URL) - Tier classification
  ...

  ---

  ## Research from Grok (Real-Time & Regional Sources)

  [Same structure]

  ---

  [Repeat for all platforms]

  ---

  ## Summary Statistics

  | Platform | Status | Duration | Sources | Tier 1 | Tier 2 | Tier 3 |
  |----------|--------|----------|---------|--------|--------|--------|
  | Perplexity | ✅ | 3m 24s | 47 | 12 | 18 | 17 |
  | Grok | ✅ | 5m 18s | 23 | 2 | 8 | 13 |
  | ChatGPT | ✅ | 4m 36s | 31 | 8 | 14 | 9 |
  | Gemini | ⏱️ Timeout | 10m 00s | 15 | 3 | 7 | 5 |
  | Claude | ✅ | 6m 12s | 38 | 11 | 16 | 11 |
  | **Total** | **4/5** | **29m 30s** | **154** | **36** | **63** | **55** |
  ```
- **Success Criteria:** Markdown file generated with all sections properly formatted

#### FR-11: Cross-Validation Preparation
- **Requirement:** Create initial cross-validation matrix from results
- **Output:** `cross-validation-matrix.md` with claims to verify
- **Logic:**
  ```python
  def extract_verifiable_claims(results: dict) -> List[dict]:
      """
      Extract claims that appear in multiple sources for verification
      """
      claims = []

      # Look for statistical claims (numbers, percentages, dates)
      for platform, data in results.items():
          content = data['content']

          # Regex patterns for common claim types
          stats = re.findall(r'\d+%|\$\d+[KMB]?|\d+\s+(?:million|billion)', content)
          dates = re.findall(r'\d{4}', content)

          for stat in stats:
              claims.append({
                  'claim': stat,
                  'platform': platform,
                  'context': extract_context(content, stat, window=50)
              })

      # Group similar claims across platforms
      grouped = group_similar_claims(claims)

      return grouped
  ```
- **Success Criteria:** Matrix identifies all numerical claims for verification

---

## Platform-Specific Requirements

### Skill 1: Claude Research (`claude_deep_research`)

**Platform Context:**
- URL: `https://claude.ai/chat`
- Feature: "Research" toggle in chat interface
- Model: Claude Sonnet 4.5 or Opus 4.5 (depending on account)
- Key Strength: Comprehensive synthesis across multiple sources

**Specific Requirements:**

**FR-Claude-1: Research Toggle Activation**
- Selector: `button[aria-label*="Research"]` or text-based fallback
- Verify toggle is active (blue background)
- If toggle missing, check account tier

**FR-Claude-2: Search Query Visibility**
- Claude shows individual search queries in expandable cards
- Extract list of search queries performed
- Store in `metadata.search_queries`

**FR-Claude-3: Citation Extraction**
- Citations appear as numbered links `[1]`, `[2]`, etc.
- Extract URL from link `href`
- Extract source title from link text or tooltip
- Map citation numbers to content references

**FR-Claude-4: Progress Indicators**
- Monitor for "Searching..." status
- Track how many searches completed (if visible)
- Detect "Research complete" message

**Edge Cases:**
- Long research (10+ minutes): Keep connection alive, no timeout
- API rate limit during research: Capture partial results
- Project creation: Research may save to Projects automatically

---

### Skill 2: ChatGPT Deep Research (`chatgpt_deep_research`)

**Platform Context:**
- URL: `https://chatgpt.com/`
- Feature: Requires **o1-pro** or research preview access (NOT standard GPT-4)
- Model: o1-pro or o3-pro (when available)
- Key Strength: Step-by-step reasoning and comprehensive reports

**CRITICAL CLARIFICATION:**
ChatGPT "Deep Research" is NOT a separate UI toggle. It requires:
1. Access to o1-pro or research preview models
2. Phrasing the query to trigger research behavior
3. OR using specific model selection if available

**Specific Requirements:**

**FR-ChatGPT-1: Model Selection**
- Open model selector dropdown
- Select "o1-pro" or "Research Preview" if available
- If not available, return error: "Deep Research requires o1-pro access"
- **Do NOT attempt research with GPT-4** (different feature set)

**FR-ChatGPT-2: Research Triggering**
- Deep research may activate automatically for complex queries
- OR prefix query with: "Conduct comprehensive research on:"
- Verify research mode active by checking for step-by-step output

**FR-ChatGPT-3: Step Tracking**
- ChatGPT shows research steps:
  - "Searching the web for..."
  - "Reading and analyzing sources..."
  - "Synthesizing information..."
  - "Generating report..."
- Extract and log each step with timestamp

**FR-ChatGPT-4: Section Extraction**
- ChatGPT structures reports with markdown headers
- Extract sections: `## Introduction`, `## Key Findings`, etc.
- Parse as structured sections in output

**FR-ChatGPT-5: Citation Format**
- Sources typically appear in footnotes or "Sources" section
- Extract source title, URL, and brief description
- Match sources to inline citations if numbered

**Edge Cases:**
- Research may take 10-20 minutes for complex queries
- Model may refuse certain research queries (policy limitations)
- Output may be paginated (click "Continue" button)

---

### Skill 3: Perplexity Pro Search (`perplexity_deep_research`)

**Platform Context:**
- URL: `https://www.perplexity.ai/`
- Feature: "Pro Search" mode (requires Pro subscription)
- Models: Claude Sonnet 4.5, GPT-4, or Gemini (user configurable)
- Key Strength: Academic source prioritization and inline citations

**Specific Requirements:**

**FR-Perplexity-1: Pro Search Activation**
- Toggle "Pro Search" mode (slider or toggle button)
- Verify Pro Search is active (visual indicator)
- If Pro not available, can still run basic search but note limitation

**FR-Perplexity-2: Model Selection**
- Settings gear icon → "Answer Engine" → Select model
- Options: Claude Sonnet 4.5, GPT-4 Turbo, Gemini Pro
- Default to Claude Sonnet 4.5 for consistency
- Log which model was used

**FR-Perplexity-3: Focus Mode**
- Enable "Academic" focus if available
- OR "All" for comprehensive search
- Note: Focus affects source prioritization

**FR-Perplexity-4: Search Query Extraction**
- Perplexity shows its generated search queries at top of results
- Extract queries from query cards: `[data-testid="query-card"]`
- Store as `metadata.search_queries`

**FR-Perplexity-5: Inline Citation Parsing**
- Citations appear as superscript numbers: [1], [2], etc.
- Citation details in expandable "Sources" section
- Map citation numbers to:
  - URL
  - Title
  - Snippet/description
  - Favicon/domain

**FR-Perplexity-6: Related Questions**
- Perplexity suggests follow-up questions
- Extract and store in `metadata.related_questions`
- Useful for research expansion

**Edge Cases:**
- Free tier: Limited to 5 searches per 4 hours
- Pro tier: Still has rate limits (~50-100 searches/day)
- Image generation: May trigger for some queries, ignore

**Note:** Perplexity also has an API, but UI automation allows access to Pro-specific features and real-time model selection that API may not fully support.

---

### Skill 4: Grok Search (`grok_deep_search`)

**Platform Context:**
- URL: `https://grok.x.ai/` OR `https://x.com/` with Grok integration
- Feature: Real-time web search with X/Twitter integration
- Model: Grok 3 or Grok 4 (latest available)
- Key Strength: Real-time information and X/Twitter context

**IMPORTANT CLARIFICATION:**
As of December 2024, Grok does NOT have a separate "DeepSearch" feature. It has:
1. Standard conversational mode
2. Search-enhanced mode (searches web in real-time)
3. X/Twitter integration (can search posts and trends)

**Specific Requirements:**

**FR-Grok-1: Search Mode Verification**
- Grok searches web by default for recent/factual queries
- Verify search is triggered by checking for "Searching..." indicator
- If no search triggered, query may be answered from model knowledge only

**FR-Grok-2: X/Twitter Integration**
- Grok can search X posts when relevant
- Look for "Searched X for..." indicator
- Extract posts referenced:
  - Post URL
  - Author handle
  - Post content snippet
  - Engagement metrics (if visible)

**FR-Grok-3: Real-Time Data Indicators**
- Grok emphasizes recency
- Extract timestamps from sources ("Published 2 hours ago")
- Flag sources as "real-time" if < 24 hours old

**FR-Grok-4: Source Extraction**
- Web sources appear as inline citations or in sources section
- Extract:
  - URL
  - Title
  - Publication date (if available)
  - Domain/publisher

**FR-Grok-5: Think Mode (if available)**
- Some accounts may have access to "Think" mode for deeper reasoning
- If available, use for research queries
- Extract reasoning trace if visible

**Edge Cases:**
- Premium access required (Grok may be gated behind X Premium subscription)
- Rate limits: Unknown, likely generous for Premium users
- Content moderation: Some queries may be filtered
- X integration: May be limited by X API rate limits

**Fallback Strategy:**
If Grok unavailable or limited:
- Use Perplexity or Claude as alternative for real-time sources
- Note in output that Grok was unavailable

---

### Skill 5: Gemini Deep Research (`gemini_deep_research`)

**Platform Context:**
- URL: `https://gemini.google.com/`
- Feature: **Gemini Deep Research** (separate feature, may require Google One AI Premium)
- Model: Gemini 2.0 or Gemini Ultra
- Key Strength: Google Workspace integration (Gmail, Docs, Calendar context)

**CRITICAL CLARIFICATION:**
Gemini Deep Research is a **distinct feature** that:
1. Requires Google One AI Premium subscription
2. Is accessed as a separate experience from standard Gemini chat
3. Creates a multi-step research plan before executing
4. May take 5-10 minutes to complete

**Access verification needed:**
- Feature may be at `https://gemini.google.com/deep-research` (verify)
- OR accessed via button/toggle in standard Gemini interface
- If unavailable, can fallback to standard Gemini Advanced search

**Specific Requirements:**

**FR-Gemini-1: Deep Research Mode Verification**
- Check if Deep Research feature is accessible
- URL pattern or UI toggle
- If not available:
  - Log warning
  - Fallback to Gemini Advanced with search enabled
  - Note limitation in output

**FR-Gemini-2: Research Plan Extraction**
- Gemini Deep Research creates a research plan first
- Plan shows steps it will take
- Extract plan steps:
  - Search queries to perform
  - Topics to investigate
  - Sources to analyze
- Store as `metadata.research_plan`

**FR-Gemini-3: Workspace Integration**
- If enabled, Gemini can access:
  - Gmail (search user's emails)
  - Google Docs (search user's documents)
  - Google Calendar (search events)
  - Google Drive (search files)
- Extract which workspace sources were accessed
- **Privacy note:** Workspace integration requires explicit user permission

**FR-Gemini-4: Progress Tracking**
- Deep Research shows progress:
  - "Creating research plan..." (Step 1)
  - "Searching the web..." (Step 2)
  - "Analyzing sources..." (Step 3)
  - "Writing report..." (Step 4)
- Track progress through steps

**FR-Gemini-5: Export to Google Doc**
- Deep Research can export to Google Doc
- If available, trigger export
- Return Google Doc URL
- Download as markdown via Google Docs API if accessible

**FR-Gemini-6: Source Extraction**
- Web sources appear with:
  - Title
  - URL
  - Snippet
  - Domain
- Workspace sources (if any) show:
  - Document title
  - Document type (Gmail, Docs, etc.)
  - Relevant excerpt
  - Date

**Edge Cases:**
- Feature availability: May not be available in all regions
- Subscription required: Google One AI Premium ($20/month)
- Workspace permissions: User must grant access
- Long execution time: 10-15 minutes not uncommon

**Fallback Strategy:**
If Deep Research unavailable:
1. Use standard Gemini Advanced (still has search)
2. Enable "Search the web" toggle
3. Note in output that Deep Research feature was unavailable
4. Results will be less comprehensive but still useful

**Note for Implementation:**
- High priority to verify exact access method for Deep Research
- May need to test with actual Premium account
- Document exact UI flow once verified

---

## Non-Functional Requirements

### NFR-1: Performance
- **Parallel Execution:** All 5 platforms must run simultaneously, not sequentially
- **Total Time:** <15 minutes for all platforms to complete (excluding timeouts)
- **Individual Timeout:** 10 minutes per platform maximum
- **Memory Usage:** <2GB RAM total across all browser contexts
- **CPU Usage:** <80% during peak execution

### NFR-2: Reliability
- **Success Rate:** >90% successful completion across all platforms
- **Error Recovery:** All errors must be caught and logged (no crashes)
- **Partial Results:** Save all partial results on timeout/error
- **Retry Logic:** 3 retry attempts for network errors with exponential backoff

### NFR-3: Security & Privacy
- **No Credential Storage:** Never store passwords or API keys
- **Browser Profile Isolation:** Use existing authenticated Chrome profile (read-only access)
- **Data Handling:**
  - All research results saved locally only
  - No cloud storage without explicit user consent
  - No telemetry or analytics sent to third parties
- **Workspace Access:** Gemini workspace integration requires explicit opt-in
- **Screenshot Privacy:** Screenshots may contain sensitive info, stored locally only

### NFR-4: Maintainability
- **Selector Strategy:**
  1. Use `data-testid` attributes (most stable)
  2. Fallback to ARIA labels
  3. Last resort: text content matching
  4. Document all selectors in code comments
- **Logging:**
  - Log every major step (debug level)
  - Log errors with full context (error level)
  - Log timing for performance analysis (info level)
- **Screenshots:**
  - Capture screenshot on every error
  - Capture final result screenshot (optional, configurable)
  - Store in `artifacts/` directory

### NFR-5: Usability
- **Progress Visibility:**
  - Real-time progress updates every 10 seconds
  - Clear indication of which platforms completed
  - ETA for remaining platforms (if possible)
- **Error Messages:**
  - User-friendly error descriptions
  - Actionable suggestions for resolution
  - Link to troubleshooting docs
- **Headless vs Visible:**
  - Support both headless and visible browser modes
  - Default to headless for production
  - Visible mode for debugging

### NFR-6: Testability
- **Unit Tests:** Each platform skill has isolated unit tests
- **Integration Tests:** Orchestrator tested with all 5 platforms
- **Mock Mode:** Support mock mode for testing without actual browser automation
- **Test Coverage:** >80% code coverage

---

## Technical Architecture

### Technology Stack

**Core Dependencies:**
```
playwright >= 1.40.0
playwright-stealth >= 1.0.0  # If needed for bot detection
pydantic >= 2.0.0  # For data validation
python >= 3.11
```

**Browser Strategy:**
- Use Playwright (faster, more reliable than Selenium)
- Connect to existing Chrome profile for authentication
- Launch persistent context with user data directory
- Disable automation flags to avoid detection

### Directory Structure

```
/Users/valorengels/src/research/.claude/skills/
├── deep-research-orchestrator/
│   ├── skill.py              # Main orchestrator
│   ├── config.py             # Configuration
│   ├── SKILL.md              # Skill documentation
│   └── tests/
│       ├── test_orchestrator.py
│       └── test_integration.py
├── claude-research/
│   ├── skill.py              # Claude automation
│   ├── selectors.py          # UI selectors
│   ├── SKILL.md
│   └── tests/
│       └── test_claude.py
├── chatgpt-research/
│   ├── skill.py
│   ├── selectors.py
│   ├── SKILL.md
│   └── tests/
├── perplexity-research/
│   ├── skill.py
│   ├── selectors.py
│   ├── SKILL.md
│   └── tests/
├── grok-research/
│   ├── skill.py
│   ├── selectors.py
│   ├── SKILL.md
│   └── tests/
├── gemini-research/
│   ├── skill.py
│   ├── selectors.py
│   ├── SKILL.md
│   └── tests/
└── _shared/
    ├── browser_utils.py      # Shared browser management
    ├── data_models.py        # Pydantic models
    ├── prompts.py            # Prompt templates
    └── validation.py         # Cross-validation logic
```

### Data Models

```python
# _shared/data_models.py

from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Literal
from datetime import datetime

class Source(BaseModel):
    """Individual source citation"""
    number: Optional[int] = None
    url: HttpUrl
    title: str
    description: Optional[str] = None
    type: Literal["academic", "news", "official", "industry", "social", "web"]
    tier: Literal["tier_1_meta_analysis", "tier_1_official",
                  "tier_2_academic", "tier_2_government_report",
                  "tier_3_news_premium", "tier_3_industry", "tier_3_web"]
    date: Optional[datetime] = None
    author: Optional[str] = None

class Section(BaseModel):
    """Content section with heading"""
    heading: str
    content: str
    level: int = Field(ge=1, le=6)  # h1-h6

class ResearchMetadata(BaseModel):
    """Metadata about research execution"""
    model: Optional[str] = None
    start_time: datetime
    end_time: datetime
    duration_seconds: float
    timeout: bool = False
    partial_results: bool = False
    search_queries: List[str] = []
    source_count: int
    error: Optional[str] = None

class Artifacts(BaseModel):
    """Debugging artifacts"""
    screenshot_path: Optional[str] = None
    html_path: Optional[str] = None
    markdown_export: Optional[str] = None

class PlatformResult(BaseModel):
    """Result from a single platform"""
    platform: Literal["claude", "chatgpt", "perplexity", "grok", "gemini"]
    query: str
    content: str
    sections: List[Section] = []
    sources: List[Source]
    metadata: ResearchMetadata
    artifacts: Artifacts

class OrchestratorResult(BaseModel):
    """Result from orchestrator running all platforms"""
    base_query: str
    platforms_queried: List[str]
    platforms_successful: List[str]
    platforms_failed: List[str]
    results: dict[str, PlatformResult]  # keyed by platform name
    total_duration_seconds: float
    total_sources: int
    sources_by_tier: dict[str, int]  # tier -> count
    cross_validation_matrix: Optional[str] = None  # Path to matrix file
```

### Browser Utilities

```python
# _shared/browser_utils.py

from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from playwright_stealth import stealth_sync
import os
from typing import Optional, Callable
import time

class ResearchBrowser:
    """Shared browser management for all research skills"""

    def __init__(
        self,
        user_data_dir: Optional[str] = None,
        headless: bool = False,
        slow_mo: int = 0  # ms delay between actions (debugging)
    ):
        self.user_data_dir = user_data_dir or os.path.expanduser(
            "~/.config/google-chrome/Default"
        )
        self.headless = headless
        self.slow_mo = slow_mo
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None

    def __enter__(self) -> Page:
        """Launch browser and return new page"""
        self.playwright = sync_playwright().start()

        # Launch persistent context (uses existing Chrome profile)
        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,
            headless=self.headless,
            slow_mo=self.slow_mo,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',  # May be needed in some environments
            ],
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
        )

        page = self.context.new_page()

        # Apply stealth mode to avoid bot detection
        stealth_sync(page)

        return page

    def __exit__(self, *args):
        """Cleanup browser resources"""
        if self.context:
            self.context.close()
        if self.playwright:
            self.playwright.stop()

def wait_for_completion(
    page: Page,
    timeout: int = 300,
    completion_selectors: Optional[List[str]] = None,
    stability_window: int = 3
) -> bool:
    """
    Wait for research to complete using multiple detection methods

    Args:
        page: Playwright page object
        timeout: Maximum seconds to wait
        completion_selectors: List of CSS selectors indicating completion
        stability_window: Seconds of content stability to consider complete

    Returns:
        True if completed, False if timeout
    """
    start_time = time.time()
    last_content = ""
    stable_count = 0

    while time.time() - start_time < timeout:
        # Method 1: Check for explicit completion indicators
        if completion_selectors:
            for selector in completion_selectors:
                if page.query_selector(selector):
                    return True

        # Method 2: Content stability (no changes for N seconds)
        current_content = page.content()
        if current_content == last_content:
            stable_count += 1
            if stable_count >= (stability_window * 2):  # 0.5s checks
                return True
        else:
            stable_count = 0

        last_content = current_content
        time.sleep(0.5)

    return False  # Timeout

def safe_screenshot(page: Page, path: str) -> Optional[str]:
    """
    Capture screenshot with error handling
    """
    try:
        page.screenshot(path=path, full_page=True)
        return path
    except Exception as e:
        print(f"Screenshot failed: {e}")
        return None

def extract_text_content(page: Page, selector: str, default: str = "") -> str:
    """
    Safely extract text content from selector
    """
    try:
        element = page.query_selector(selector)
        return element.text_content().strip() if element else default
    except Exception:
        return default
```

---

## Implementation Plan

### Phase 1: Foundation (Week 1)
**Goal:** Basic infrastructure and 1 working skill

**Tasks:**
- [ ] Set up project structure
- [ ] Implement shared browser utilities
- [ ] Define Pydantic data models
- [ ] Implement Perplexity skill (simplest, has API for validation)
- [ ] Create unit tests for browser utilities
- [ ] Test on sample research query
- [ ] Document setup process

**Deliverables:**
- Working Perplexity automation
- Shared utilities tested
- Basic documentation

**Success Criteria:**
- Perplexity skill runs successfully >90% of time
- Results match manual Perplexity usage
- Documentation allows new developer to run skill

---

### Phase 2: Core Platform Skills (Week 2)
**Goal:** Implement Claude and ChatGPT skills

**Tasks:**
- [ ] Implement Claude Research skill
- [ ] Implement ChatGPT Deep Research skill
- [ ] Verify model selection (o1-pro for ChatGPT)
- [ ] Test prompt differentiation
- [ ] Create integration tests
- [ ] Refine error handling across all 3 skills
- [ ] Test parallel execution of 3 skills

**Deliverables:**
- 3 working skills (Perplexity, Claude, ChatGPT)
- Integration tests passing
- Error handling refined

**Success Criteria:**
- All 3 skills complete successfully in parallel
- Results properly structured and saved
- Errors handled gracefully

---

### Phase 3: Remaining Platforms (Week 3)
**Goal:** Implement Grok and Gemini skills

**Tasks:**
- [ ] Research Gemini Deep Research access (verify feature availability)
- [ ] Implement Gemini skill (or fallback to Gemini Advanced)
- [ ] Research Grok access and features
- [ ] Implement Grok skill
- [ ] Test all 5 skills in parallel
- [ ] Optimize performance and timing
- [ ] Create comprehensive test suite

**Deliverables:**
- All 5 skills working
- Performance optimized
- Full test coverage

**Success Criteria:**
- 5 skills complete in <15 minutes total
- >90% success rate across all platforms
- Test coverage >80%

---

### Phase 4: Orchestrator & Integration (Week 4)
**Goal:** Build orchestrator and integrate with podcast workflow

**Tasks:**
- [ ] Implement orchestrator skill
- [ ] Add parallel execution with proper error handling
- [ ] Implement cross-validation matrix creation
- [ ] Generate research-results.md output
- [ ] Integrate with podcast-episode-v2 workflow
- [ ] Create end-to-end test with real episode
- [ ] Write comprehensive documentation
- [ ] Create troubleshooting guide

**Deliverables:**
- Working orchestrator
- Integration with podcast workflow
- Complete documentation

**Success Criteria:**
- Orchestrator successfully runs all 5 platforms
- Results integrate into podcast workflow
- Documentation complete and tested

---

### Phase 5: Polish & Production (Week 5)
**Goal:** Production-ready release

**Tasks:**
- [ ] Performance optimization
- [ ] Add progress indicators and status updates
- [ ] Implement headless mode
- [ ] Add screenshot artifacts for debugging
- [ ] Create monitoring/logging dashboard
- [ ] User acceptance testing
- [ ] Bug fixes and refinements
- [ ] Final documentation review

**Deliverables:**
- Production-ready skills
- Monitoring and debugging tools
- Complete user guide

**Success Criteria:**
- All acceptance tests pass
- User can run workflow end-to-end
- Documentation covers all use cases

---

## Testing Strategy

### Unit Tests

**Browser Utilities:**
- Test browser launch with/without user data dir
- Test completion detection with various scenarios
- Test screenshot capture
- Test text extraction

**Platform Skills:**
- Test authentication verification
- Test selector stability (mock page HTML)
- Test data extraction from mock HTML
- Test error handling for each error type

### Integration Tests

**Single Platform:**
- Full workflow: launch → research → extract → save
- Test with real research query
- Verify output format matches schema
- Test timeout handling (short timeout on long query)

**Orchestrator:**
- Run all 5 platforms in parallel
- Test with one platform failing (mock failure)
- Test with partial timeouts
- Verify aggregated output

### End-to-End Tests

**Full Podcast Workflow:**
1. Create new episode structure
2. Run orchestrator with real query
3. Verify research-results.md created
4. Run cross-validation
5. Complete episode workflow

**Test Queries:**
- Simple factual: "Population of Solomon Islands"
- Complex research: "Solomon Islands telecom market structure and regulatory framework"
- Recent events: "Major AI developments December 2024"
- Academic: "Meta-analyses of early childhood educator burnout"

### Manual Testing

**Platform-Specific:**
- Test each platform with various query types
- Verify citations extracted correctly
- Check source classification accuracy
- Test export features (if available)

**Failure Scenarios:**
- Network disconnection during research
- Rate limit reached
- Account not authenticated
- Feature not available (downgrade subscription)

---

## Monitoring & Observability

### Metrics to Track

**Performance:**
- Duration per platform (avg, p50, p95, p99)
- Total orchestrator duration
- Success rate per platform
- Error rate per platform
- Timeout rate per platform

**Quality:**
- Number of sources found per platform
- Source tier distribution (Tier 1 vs Tier 2 vs Tier 3)
- Citation extraction accuracy (manual validation)
- Duplicate sources across platforms

**Usage:**
- Number of research queries per day
- Most common query types
- Platform preference (if user can select)

### Logging

**Structured Logs:**
```json
{
  "timestamp": "2024-12-08T10:30:45Z",
  "level": "INFO",
  "skill": "claude-research",
  "event": "research_started",
  "query": "Solomon Islands telecom...",
  "metadata": {
    "episode": "episode-2-breaking-duopoly",
    "session_id": "abc123"
  }
}
```

**Log Levels:**
- DEBUG: Every selector query, page navigation
- INFO: Major steps (research started, completed)
- WARNING: Retries, fallbacks, degraded functionality
- ERROR: Failures, timeouts, exceptions

### Debugging Artifacts

**On Error:**
- Screenshot of page at error point
- Full HTML dump
- Network logs (if available)
- Console errors (if available)

**On Success:**
- Screenshot of final results (optional)
- Timing breakdown
- Search queries used

**Storage:**
```
artifacts/
├── YYYY-MM-DD-HH-MM-SS/
│   ├── claude_screenshot.png
│   ├── claude_html.html
│   ├── chatgpt_screenshot.png
│   └── ...
```

---

## Security & Privacy Considerations

### Authentication
- **No credential storage:** Never store passwords, API keys, or session tokens
- **Browser profile reuse:** Leverage existing authenticated Chrome profile
- **Read-only access:** Skills only read from browser profile, never modify
- **Session isolation:** Each skill runs in isolated browser context

### Data Privacy
- **Local storage only:** All research results stored on user's machine
- **No cloud sync:** No automatic uploads to cloud services
- **Screenshot privacy:** Screenshots may contain sensitive info, never shared
- **Workspace data:** Gemini workspace integration requires explicit user opt-in

### Content Handling
- **No content filtering:** Research tools don't filter or modify research content
- **Citation preservation:** All sources attributed to original platforms
- **No data aggregation:** Results not combined with other users' data

### Compliance
- **Terms of Service:** Skills operate within each platform's ToS (automated access for personal use)
- **Rate limiting:** Respect each platform's rate limits
- **Robot detection:** Use stealth techniques to avoid triggering bot detection (for legitimate use)

**Note:** Users are responsible for ensuring their use of these automation tools complies with each platform's Terms of Service. These skills are intended for personal research use only.

---

## Success Metrics

### Launch Criteria (MVP)

**Must Have:**
- [ ] All 5 platform skills implemented and working
- [ ] Orchestrator runs all skills in parallel successfully
- [ ] Success rate >90% across all platforms
- [ ] Results saved in correct format to research-results.md
- [ ] Integration with podcast workflow V2 tested
- [ ] Documentation complete (setup, usage, troubleshooting)
- [ ] Error handling for all common failure modes

**Should Have:**
- [ ] Cross-validation matrix auto-generated
- [ ] Progress indicators show real-time status
- [ ] Screenshots captured on errors for debugging
- [ ] Unit test coverage >80%
- [ ] Headless mode working

**Nice to Have:**
- [ ] Performance dashboard showing metrics
- [ ] Automatic retry on transient failures
- [ ] Source quality classification >90% accuracy
- [ ] Export to additional formats (JSON, CSV)

### Post-Launch Metrics (3 months)

**Usage:**
- [ ] 50+ research queries completed
- [ ] Used for 10+ podcast episodes
- [ ] User satisfaction >4/5

**Quality:**
- [ ] Success rate maintained >90%
- [ ] Average completion time <12 minutes
- [ ] Source count per query >100 across all platforms
- [ ] False positive rate in cross-validation <5%

**Reliability:**
- [ ] Uptime >95% (excluding platform outages)
- [ ] Mean time to resolution for bugs <48 hours
- [ ] Zero data loss incidents

---

## Dependencies & Assumptions

### External Dependencies

**Platforms:**
- Claude.ai availability and Research feature
- ChatGPT availability and o1-pro access
- Perplexity Pro subscription
- Grok access (X Premium subscription)
- Gemini Deep Research availability (Google One AI Premium)

**Technical:**
- Playwright browser automation library
- Chrome/Chromium browser installed
- Python 3.11+
- Stable internet connection (10+ Mbps recommended)

### Assumptions

**User Environment:**
- User has active subscriptions to all required platforms
- User is already authenticated in Chrome (cookies/sessions valid)
- User's Chrome profile path is accessible
- No strict firewall/proxy blocking platform access

**Platform Stability:**
- Platform UIs remain relatively stable (selectors don't change drastically)
- Deep research features continue to exist
- APIs/features don't get paywalled or removed
- Rate limits don't become prohibitively restrictive

**Risks if Assumptions Invalid:**
- UI changes break selectors → Requires selector updates (maintenance)
- Features removed → Skill becomes obsolete, remove or adapt
- Authentication expires → User must re-authenticate manually
- Rate limits hit → Graceful degradation, warn user

---

## Open Questions & Risks

### Open Questions

1. **Gemini Deep Research Access:**
   - Is Deep Research a separate URL or integrated into standard Gemini?
   - Does it require Google One AI Premium or is it in Google Workspace plans?
   - What's the exact activation flow?
   - **Resolution:** Test with actual Premium account, document exact flow

2. **Grok Feature Verification:**
   - Is there actually a "DeepSearch" mode or is it just standard search?
   - What's the difference between free and Premium Grok features?
   - How reliable is X/Twitter integration?
   - **Resolution:** Test with X Premium account, verify available features

3. **ChatGPT Model Selection:**
   - Is o1-pro sufficient or do we need o3-pro (when available)?
   - Can we programmatically select model or does it auto-select?
   - Are there query-specific model restrictions?
   - **Resolution:** Test with Pro account, document model selection flow

4. **Rate Limiting:**
   - What are exact rate limits for each platform?
   - Do limits reset daily, hourly, or rolling window?
   - Can we detect approaching limits before hitting them?
   - **Resolution:** Monitor usage, document observed limits, add buffer

5. **Platform TOS Compliance:**
   - Do any platforms explicitly prohibit automation?
   - Is "automation for personal use" acceptable?
   - Should we add user consent/warning?
   - **Resolution:** Review each platform's TOS, add disclaimer if needed

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Platform UI changes break selectors | High | Medium | Use multiple selector strategies, add monitoring for failures |
| Features become paywalled or removed | Medium | High | Build fallbacks, document alternatives |
| Rate limits more restrictive than expected | Medium | Medium | Implement retry logic, add delays between requests |
| Bot detection blocks automation | Low | High | Use stealth techniques, user-agent spoofing, authenticated sessions |
| Authentication expires mid-research | Medium | Low | Detect auth failures early, prompt user to re-authenticate |
| One platform takes 20+ minutes | Low | Medium | Implement per-platform timeouts, save partial results |
| Legal/TOS issues with automation | Low | High | Add user consent, document personal use only |

---

## Appendix

### A. Platform Comparison Matrix

| Feature | Claude | ChatGPT | Perplexity | Grok | Gemini |
|---------|--------|---------|------------|------|--------|
| **Research Mode** | Toggle | Model select | Toggle | Auto | Separate feature |
| **Subscription Required** | Pro | Plus (o1-pro) | Pro | X Premium | One AI Premium |
| **Typical Duration** | 4-8 min | 5-15 min | 2-5 min | 3-6 min | 8-15 min |
| **Source Types** | Web, academic | Web, mixed | Academic-focused | Web, X posts | Web, workspace |
| **Citation Format** | Numbered inline | Footnotes | Numbered inline | Inline links | Citations section |
| **Export Options** | None | Copy | PDF | None | Google Docs |
| **Search Visibility** | Yes | Step-by-step | Yes | Limited | Research plan |
| **Unique Strength** | Synthesis quality | Reasoning depth | Academic sources | Real-time/X data | Workspace context |

### B. Example Prompts by Platform

**Base Query:** "Solomon Islands telecom market structure and competitive dynamics"

**Perplexity (Academic/Official):**
```
Research the Solomon Islands telecommunications market structure and competitive dynamics.

Focus on:
- Peer-reviewed studies on telecom competition in small island nations
- Official regulatory documents from Solomon Islands government
- Market structure analysis from World Bank, ITU, or regional development banks
- Statistical data on market shares, pricing, infrastructure

Prioritize:
- Meta-analyses and systematic reviews
- Government reports and official statistics
- Academic papers with sample sizes and methodology clearly stated
- Primary sources over secondary sources

For each finding:
- Provide full citation with publication year
- Note sample size and methodology if study-based
- Distinguish correlation from causation
- Include effect sizes where available

Output: Comprehensive report with extensive citations organized by source quality tier.
```

**Grok (Real-Time/Regional):**
```
Research the Solomon Islands telecommunications market structure and competitive dynamics.

Focus on:
- Recent news and developments (last 12 months)
- Regional Pacific telecom industry analysis
- X/Twitter discussions from telecom industry experts
- Local Solomon Islands news sources and commentary
- Practitioner perspectives from telecom operators

Prioritize:
- Breaking news and recent announcements
- Regional sources (Pacific-focused publications)
- Expert commentary on X from telecom professionals
- Local perspectives from Solomon Islands media
- Industry conference presentations or reports

For each source:
- Provide URL and publication date
- Note credibility level (official, news, expert opinion)
- Highlight if this updates or contradicts older information
- Extract key quotes from experts

Output: Current state of the market with emphasis on latest developments and ground-level perspectives.
```

**ChatGPT (Industry/Technical):**
```
Research the Solomon Islands telecommunications market structure and competitive dynamics.

Focus on:
- Industry reports from McKinsey, BCG, Deloitte, etc.
- Technical infrastructure assessments
- Case studies of similar small island nation telecom markets
- Financial analysis and market sizing
- Technical specifications and standards in use

Prioritize:
- Industry analyst reports with market data
- Infrastructure assessments (tower counts, spectrum allocation, etc.)
- Comparative case studies (Fiji, Vanuatu, PNG telecom markets)
- Financial metrics (ARPU, market cap, revenue)
- Technical details practitioners need

For each source:
- Cite report title, organization, and year
- Extract key data points and metrics
- Build comparison tables across similar markets
- Note methodologies used for estimates

Output: Industry-focused analysis with hard data, technical specs, and comparative benchmarks.
```

**Gemini (Strategic/Policy):**
```
Research the Solomon Islands telecommunications market structure and competitive dynamics.

Focus on:
- Regulatory frameworks and telecommunications legislation
- Government policy documents and strategic plans
- Market structure analysis (monopoly, duopoly, competition)
- Comparative regulatory approaches across Pacific nations
- Policy positions from government and industry stakeholders

Prioritize:
- Official legislation and regulatory documents
- Government strategic plans and policy papers
- Regulatory authority reports (Solomon Islands and regional)
- Comparative regulatory analysis
- Stakeholder position papers

For each finding:
- Cite regulation/policy name, effective date, and source
- Extract key provisions relevant to market competition
- Compare regulatory approaches across jurisdictions
- Note any pending legislation or policy changes

If workspace integration available:
- Search for any relevant emails or documents in my Google Workspace
- Check calendar for telecom-related events or meetings

Output: Regulatory and strategic landscape with policy framework documentation.
```

**Claude (Comprehensive Synthesis):**
```
Research the Solomon Islands telecommunications market structure and competitive dynamics.

Conduct comprehensive research across multiple domains:
- Academic studies and peer-reviewed research
- Official government and regulatory sources
- Industry analysis and market reports
- Recent news and developments
- Regional context and comparative markets

Research methodology:
- Prioritize meta-analyses and systematic reviews for established findings
- Distinguish correlation from causation
- Report effect sizes and practical significance
- Note study populations and generalizability
- Identify preliminary vs. well-replicated findings
- Include contradictory findings and areas of uncertainty
- Cite specific studies, researchers, and sources

Analysis framework:
- Market structure (players, market shares, concentration)
- Regulatory environment (laws, policies, oversight)
- Infrastructure (coverage, technology, capacity)
- Competitive dynamics (pricing, service quality, innovation)
- Strategic considerations (barriers to entry, competitive advantages)

Output: Comprehensive research synthesis with extensive citations, clear evidence hierarchy, and multi-dimensional analysis suitable for strategic decision-making.
```

### C. Selector Documentation Template

Each platform skill should document selectors in this format:

```python
# claude-research/selectors.py

"""
UI Selectors for Claude Research Automation

Last Updated: 2024-12-08
Last Verified: 2024-12-08
Platform Version: Claude.ai (Dec 2024)

Note: Selectors may change with UI updates. Update this file and
increment version when selectors are modified.
"""

SELECTORS = {
    # Authentication verification
    "user_avatar": [
        'button[aria-label*="Account"]',
        '[data-testid="user-menu"]',
        'img[alt*="avatar"]'  # Fallback
    ],

    # Research toggle
    "research_toggle": [
        'button[aria-label*="Research"]',
        'button:has-text("Research")',  # Text-based fallback
    ],

    # Research active indicator
    "research_active": [
        'button[aria-label*="Research"][aria-pressed="true"]',
        'button[aria-label*="Research"].active',
    ],

    # Chat input
    "chat_input": [
        'textarea[placeholder*="Talk"]',
        'div[contenteditable="true"]',
    ],

    # Research in progress
    "research_in_progress": [
        '[data-testid="research-status"]',
        'div:has-text("Searching")',
    ],

    # Research complete
    "research_complete": [
        '[data-testid="research-complete"]',
        'div:has-text("Research complete")',
    ],

    # Search query cards
    "search_queries": [
        '[data-testid="search-query"]',
        '.search-query-card',
    ],

    # Citations
    "citations": [
        'a[href^="http"][data-citation]',
        'sup > a[href^="http"]',  # Superscript links
    ],

    # Response container
    "response": [
        '[data-testid="conversation-turn"]',
        '.message.assistant',
    ],
}

def get_selector(key: str) -> list[str]:
    """
    Get selector list for a key

    Returns list of selectors to try in order (most stable first)
    """
    return SELECTORS.get(key, [])
```

### D. Troubleshooting Guide

**Problem:** "Not authenticated" error

**Solutions:**
1. Open Chrome manually and verify you're logged in to the platform
2. Check that skills are using the correct Chrome profile path
3. Clear cookies and re-authenticate
4. Check if platform requires 2FA that expired

---

**Problem:** Research timeout after 10 minutes

**Solutions:**
1. Check if platform is experiencing outages (status page)
2. Try simpler query to verify platform is working
3. Check network connection (slow connection may cause timeouts)
4. Review partial results to see where it got stuck
5. Try running that platform alone (not in parallel) to see if resource contention

---

**Problem:** Selectors not found / "Element not found" errors

**Solutions:**
1. Run in visible (non-headless) mode to see what's happening
2. Check if platform UI has changed recently
3. Update selectors in `selectors.py` for that platform
4. Capture screenshot to see page state
5. Check if you're on the wrong URL (redirected?)

---

**Problem:** Rate limit errors

**Solutions:**
1. Wait for rate limit to reset (check platform's limit policy)
2. Reduce frequency of research queries
3. Spread queries across more time (add delays)
4. Check if you're running multiple instances simultaneously
5. Upgrade subscription tier if limits too restrictive

---

**Problem:** Partial/incomplete results

**Solutions:**
1. Check if timeout was hit (increase timeout if needed)
2. Verify completion detection logic is working
3. Check for errors in middle of execution (review logs)
4. Try query manually to see if platform completes it
5. Save and review partial results - may still be useful

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-08 | Valor Engels | Initial PRD based on engineering brief and V2 workflow context |

---

## Approval & Sign-off

**Product Owner:** Valor Engels
**Status:** Draft - Pending Review
**Next Review:** After Phase 1 completion

---

**End of Document**
