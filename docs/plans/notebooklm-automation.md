# NotebookLM Automation Plan

---

## Status Update (2026-02-05)

### ✅ SUPERSEDED - Enterprise API Implemented Instead

This plan proposed browser automation as a cost-effective alternative to the Enterprise API. **We subsequently gained access to the Enterprise API and implemented that approach instead.**

### What Was Implemented

| Original Plan | Actual Implementation |
|---------------|----------------------|
| Playwright browser automation | Discovery Engine API (Enterprise) |
| `notebooklm_browser.py` script | `podcast/tools/notebooklm_api.py` |
| Persistent browser sessions | OAuth2 via `gcloud auth` |
| Manual fallback workflow | Manual workflow preserved as backup |

### Current Implementation

**Primary:** NotebookLM Enterprise API
- `.claude/skills/notebooklm-enterprise-api/SKILL.md` - Skill documentation
- `podcast/tools/notebooklm_api.py` - API automation script
- Uses Discovery Engine API with OAuth2 authentication
- Automatically creates notebook, uploads 5 sources, generates audio
- Includes `test_api_access()` for graceful fallback

**Fallback:** Manual NotebookLM workflow
- `.claude/skills/notebooklm-audio/SKILL.md` - Manual workflow documentation
- `podcast/tools/notebooklm_prompt.py` - Generates copy-paste prompt
- Used when Enterprise API is unavailable

**Wave 3 Enhancements (Feb 2026):**
- `extract_content_plan_sections()` - Parses enhanced content_plan.md
- `generate_episode_focus()` - Injects structural guidance, counterpoints, arc templates
- Counterpoint moments with ASSIGNED POSITIONS for dialogue dynamics

### What's Obsolete

| Item | Reason |
|------|--------|
| Playwright automation approach | Enterprise API provides cleaner automation |
| `notebooklm_browser.py` script | Never implemented; API used instead |
| Browser session management | Not needed with API OAuth |
| Selector maintenance concerns | N/A with API |

### What Remains Valuable

| Item | Value |
|------|-------|
| Cost analysis | Still valid for evaluating API vs alternatives |
| Fallback concept | Manual workflow serves as fallback |
| Free tier consideration | Could revisit if API access lost |

### Recommendation

**Archive this plan.** The Enterprise API approach is working well:
- Wave 1 validation: +16 points improvement (28→44/50)
- Wave 3 enhanced episodeFocus with structural guidance
- Graceful fallback to manual workflow when needed

### Related Documents

- `.claude/skills/notebooklm-enterprise-api/SKILL.md` - Current implementation
- `.claude/skills/notebooklm-audio/SKILL.md` - Manual fallback
- `podcast/tools/notebooklm_api.py` - API script
- `podcast/tools/notebooklm_prompt.py` - Manual prompt generator
- `docs/plans/podcast_episode_improvements.md` - Wave 3 details

---

## Original Plan (Archived for Reference)

> **Note:** The following represents the original browser automation proposal. It was not implemented—the Enterprise API approach was used instead. Preserved for historical reference.

## Problem

NotebookLM produces the best podcast audio quality (two-host conversation style), but:

- **Enterprise API**: Requires minimum 15 licenses = $135/month
- **Free/Plus tiers**: No API, manual web interface only
- **TTS alternatives**: Script-based TTS doesn't match NotebookLM's conversation quality

## Proposed Solution: Hybrid Approach

**NotebookLM Plus ($20/month) + Playwright Browser Automation**

### Why This Works

1. NotebookLM Plus provides:
   - Higher usage limits than free tier
   - Priority generation queue
   - Same audio quality as Enterprise

2. Playwright automation provides:
   - Fully automated workflow (no manual intervention)
   - Persistent browser session (login once)
   - Programmatic file upload and download

### Implementation Plan

#### 1. Install Dependencies

```bash
pip install playwright
playwright install chromium
```

#### 2. Create `notebooklm_browser.py`

Script should:
- Use persistent browser context (saves cookies/session)
- Navigate to notebooklm.google.com
- Create new notebook with episode title
- Upload 5 source files:
  - `research/p1-brief.md`
  - `report.md`
  - `research/p3-briefing.md`
  - `sources.md`
  - `content_plan.md`
- Open Audio Overview panel
- Enter customization prompt (from SKILL.md template)
- Select "Deep Dive" format, "Long" length
- Click generate
- Poll/wait for completion (up to 15 minutes)
- Download generated audio
- Clean up notebook (optional)

#### 3. Handle Authentication

First run requires manual Google login. Subsequent runs reuse saved session.

```python
# Persistent browser profile location
BROWSER_DATA_DIR = "~/.notebooklm-automation"
```

#### 4. Usage

```bash
python notebooklm_browser.py ../episodes/cardiovascular-health/ep1-lifestyle/ \
  --series "Cardiovascular Health" \
  --title "Lifestyle Factors"
```

### Challenges & Mitigations

| Challenge | Mitigation |
|-----------|------------|
| Google login expires | Re-login prompt, long session cookies |
| UI changes break selectors | Use robust selectors, version pin |
| Generation timeout | Configurable timeout, retry logic |
| Rate limiting | Respect limits, add delays |
| CAPTCHA/verification | Fall back to manual, alert user |

### Cost Comparison

| Approach | Monthly Cost | Automation |
|----------|-------------|------------|
| Enterprise API | $135 | Full API |
| Plus + Browser | $20 | Playwright |
| Free + Browser | $0 | Playwright (with limits) |

### Alternative: Free Tier

Could start with free tier + automation. Upgrade to Plus only if hitting limits.

Free tier limits (as of Dec 2024):
- 3 audio overviews per day
- 50 sources per notebook
- Standard generation queue

### Next Steps

1. [x] ~~Subscribe to NotebookLM Plus~~ → Used Enterprise API instead
2. [x] ~~Build Playwright automation script~~ → Built API script instead
3. [x] Test with one episode ✅
4. [x] Integrate into podcast workflow ✅
5. [x] Document failure modes and recovery ✅

### Files to Create

- ~~`podcast/tools/notebooklm_browser.py`~~ → `podcast/tools/notebooklm_api.py` (API version)
- ~~`podcast/tools/notebooklm_browser_config.py`~~ → Not needed with API

### Reference

- NotebookLM: https://notebooklm.google.com/
- NotebookLM Plus: https://notebooklm.google.com/plans
- ~~Playwright Python: https://playwright.dev/python/~~ → Not used
- Current manual workflow: `.claude/skills/notebooklm-audio/SKILL.md`
- **Current API workflow: `.claude/skills/notebooklm-enterprise-api/SKILL.md`**
