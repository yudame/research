# NotebookLM Automation Plan

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

1. [ ] Subscribe to NotebookLM Plus (or test with free tier first)
2. [ ] Build Playwright automation script
3. [ ] Test with one episode
4. [ ] Integrate into podcast workflow
5. [ ] Document failure modes and recovery

### Files to Create

- `podcast/tools/notebooklm_browser.py` - Main automation script
- `podcast/tools/notebooklm_browser_config.py` - Selectors and constants (easy to update if UI changes)

### Reference

- NotebookLM: https://notebooklm.google.com/
- NotebookLM Plus: https://notebooklm.google.com/plans
- Playwright Python: https://playwright.dev/python/
- Current manual workflow: `.claude/skills/notebooklm-audio/SKILL.md`
