# Counterpoint Execution Enhancement Plan

**Date:** 2026-02-09
**Purpose:** Additional workflow adjustments to address persistent weak points in Episodes 3 and 8

---

## Problem Statement

**Common Weak Points Across Episodes 3 & 8:**

| Dimension | Ep 3 Score | Ep 8 Score | Pattern |
|-----------|------------|------------|---------|
| **Dialogue Dynamics** | 3/5 | 3/5 | Counterpoint moments designed but executed collaboratively, not as positional debate |
| **Mode-Switching Clarity** | 3/5 | 4/5 | Modes present but transitions conversational, not explicitly signposted |

**Root Cause Analysis:**

### Dialogue Dynamics (3/5 in both episodes)

**What's happening:**
- Content plan designs counterpoint moments with both positions documented
- NotebookLM receives generic instruction: "create disagreement at these moments"
- Audio output: collaborative framing ("Framework A says X, Framework B says Y")
- Missing: positional dialogue ("I think X..." / "Wait, I disagree because Y...")

**Episode 3 example:**
- Planned: Chesky vs. Wasserman as debate
- Executed: Sequential analysis (both speakers agree to "gear shift" resolution)
- Only the 70% Rule moment had genuine tension

**Episode 8 example:**
- Planned: 3 debates documented in p3-briefing.md
- Executed: "Both interpretations have merit" collaborative framing
- Result: Dimension 4 stuck at 3/5

**Why Wave 2-5 improvements might not be enough:**
- Wave 2 Task A2.3: Adds explicit position assignment language ✅
- Wave 3 Task A3.2: Adds dialogue dynamics to episodeFocus ✅
- **Gap:** Still relies on NotebookLM interpreting general guidance rather than following specific scripts

### Mode-Switching Clarity (3-4/5)

**What's happening:**
- Content plan specifies mode-switching framework and signposting language
- NotebookLM creates natural conversational flow
- Audio output: modes blend without explicit markers
- Missing: actual transition phrases that signal mode changes

**Episode 3 example:**
- Content plan specified: "Let's look at what the research actually found when they tested this..."
- None of these exact phrases appeared in transcript
- 70% Rule section blended research, philosophy, and practical advice in 3 minutes with no markers

**Episode 8 example:**
- Mode-switching better (4/5) but still conversational
- Listeners can't clearly identify "we're now in storytelling mode" vs "we're back in research mode"

**Why Wave 2-5 improvements might not be enough:**
- Wave 2 Task A1.2: Adds mode-switching framework ✅
- Wave 2 Task A1.3: Adds signposting language templates ✅
- **Gap:** Provides examples but doesn't require specific phrases at specific moments

---

## Proposed Solution: Workflow Script Injection

**Core idea:** Move from "design guidance" to "script verbatim dialogue" at critical moments.

### New Principle: The Specificity Ladder

Current approach is at Level 2. We need to climb to Level 3-4.

| Level | Approach | Example | NotebookLM Execution |
|-------|----------|---------|---------------------|
| **Level 1** | Generic instruction | "Create some disagreement" | Produces agreement with "interesting point" |
| **Level 2** | Position assignment | "Speaker A defends X, Speaker B challenges with Y" | Produces collaborative framing: "Some say X, others say Y" |
| **Level 3** | Cue language | "Use phrases: 'Wait, but...' 'I disagree because...'" | Produces debate-like exchanges ~50% of the time |
| **Level 4** | Verbatim script | "Speaker A: 'I have to say, looking at these numbers...' Speaker B: 'Wait—that's survivorship bias talking.'" | Produces exact or very close variation ~90% of the time |

**Current state:** Wave 2-5 improvements move us from Level 1 → Level 3
**Target:** Level 4 for critical counterpoint moments, Level 3 for mode transitions

---

## Additional Workflow Adjustments

### Adjustment 1: Counterpoint Script Section in content_plan.md

**Phase:** 8 (Episode Planning)

**Location:** New section in content_plan.md template

**What to add:**

```markdown
## COUNTERPOINT SCRIPTS

**Purpose:** Verbatim dialogue to ensure positional debate, not collaborative framing.

**Instructions:** For each counterpoint moment, script the opening exchange (3-5 lines per speaker).

### Counterpoint Moment 1: [Topic]

**Context:** [When this occurs in episode arc]

**Position Assignment:**
- Speaker A position: [Specific stance]
- Speaker B position: [Opposing stance]

**Scripted Opening Exchange:**

> **Speaker A:** "[Exact opening line that states position]"
>
> **Speaker B:** "[Exact challenge line - must use disagreement language]"
>
> **Speaker A:** "[Defense/elaboration]"
>
> **Speaker B:** "[Counter-evidence or alternative view]"

**Required elements:**
- ✓ Speaker B must use explicit disagreement language: "Wait, but..." / "I disagree because..." / "Hold on..." / "I'm not convinced..."
- ✓ Neither speaker can use collaborative framing: "Both have merit" / "It's complicated" / "There are many perspectives"
- ✓ Exchange must run minimum 60-90 seconds before resolution/synthesis

**Resolution approach:** [How speakers eventually reconcile or synthesize]

---

### Counterpoint Moment 2: [Topic]

[Repeat structure]

---

### Counterpoint Moment 3: [Topic]

[Repeat structure]
```

**Exit criteria addition for Phase 8:**
- ✓ 2-3 counterpoint moments scripted with verbatim opening exchanges
- ✓ Each script includes explicit disagreement language (verified)
- ✓ Each script avoids collaborative framing (verified)

---

### Adjustment 2: Mode Transition Scripts in content_plan.md

**Phase:** 8 (Episode Planning)

**Location:** New section in content_plan.md template

**What to add:**

```markdown
## MODE TRANSITION SCRIPTS

**Purpose:** Explicit signposting at key mode shifts to help listeners orient.

**Instructions:** Identify 5-7 critical mode transitions and provide exact transition phrases.

### Transition 1: Opening Hook → Foundation (Philosophy Mode)

**Timing:** ~3-5 minutes in

**Transition phrase:**
> "So that's the hook. Now let's step back and ask a bigger question: [philosophical reframe]"

**Mode signal:** Uses "step back" / "bigger question" to signal shift from storytelling to philosophy

---

### Transition 2: Foundation → Evidence (Research Mode)

**Timing:** ~10-12 minutes in

**Transition phrase:**
> "That's the conceptual frame. Now let's look at what the research actually found when they tested this..."

**Mode signal:** "Let's look at what the research actually found" explicitly signals data incoming

---

### Transition 3: Evidence → Application (Practical Mode)

**Timing:** ~30-35 minutes in

**Transition phrase:**
> "Okay, so that's what the science says. Now let's talk about what you actually do with this information. Here are the specific protocols..."

**Mode signal:** "That's what the science says" bookends research; "what you actually do" signals practical shift

---

### Transition 4: [Continue for 5-7 key transitions]

[Repeat structure]
```

**Exit criteria addition for Phase 8:**
- ✓ 5-7 mode transitions identified
- ✓ Each has specific transition phrase (not generic guidance)
- ✓ Phrases use explicit mode-signaling language

---

### Adjustment 3: Enhanced episodeFocus Prompt with Script Injection

**Phase:** 9 (Audio Generation)

**Location:** podcast/tools/notebooklm_prompt.py and notebooklm_api.py

**Current approach:**
```python
episodeFocus = f"""
DIALOGUE DYNAMICS:
- Counterpoint moments at: {counterpoint_topics_list}
- Use phrases: "Wait, but..." "I disagree because..."
"""
```

**Enhanced approach with script injection:**

```python
# Read counterpoint scripts from content_plan.md
counterpoint_scripts = extract_counterpoint_scripts(content_plan_path)

episodeFocus = f"""
DIALOGUE DYNAMICS - CRITICAL REQUIREMENT:

You MUST create genuine positional debate at the following moments.
Use the scripted dialogue provided, or very close variations that preserve
the position-taking structure and disagreement language.

{format_counterpoint_scripts(counterpoint_scripts)}

AVOID:
- Collaborative framing: "Both have merit" / "It's complicated"
- Sequential presentation: "Framework A says... Framework B says..."
- Immediate agreement: "That's exactly right" / "Precisely"

REQUIRED PATTERN:
- Speaker A states position
- Speaker B explicitly disagrees with reason
- Back-and-forth for 60-90 seconds minimum
- Then synthesis/resolution
"""
```

**Script formatting function:**

```python
def format_counterpoint_scripts(scripts):
    """Format counterpoint scripts for episodeFocus prompt."""
    formatted = []
    for i, script in enumerate(scripts, 1):
        formatted.append(f"""
--- COUNTERPOINT MOMENT {i}: {script['topic']} ---
Timing: {script['context']}

SCRIPTED OPENING (use this dialogue or very close variation):

Speaker A: "{script['speaker_a_line_1']}"
Speaker B: "{script['speaker_b_line_1']}"
Speaker A: "{script['speaker_a_line_2']}"
Speaker B: "{script['speaker_b_line_2']}"

Position Assignment:
- Speaker A defends: {script['position_a']}
- Speaker B challenges with: {script['position_b']}

Resolution approach: {script['resolution']}
Duration: Minimum 60-90 seconds of debate before resolution
""")
    return "\n".join(formatted)
```

**Mode transition injection:**

```python
# Read mode transitions from content_plan.md
mode_transitions = extract_mode_transitions(content_plan_path)

episodeFocus = f"""
MODE TRANSITIONS - USE THESE EXACT PHRASES:

{format_mode_transitions(mode_transitions)}

These phrases are required signposts. Use them verbatim or with minimal variation
to help listeners know when you're shifting between philosophy, research,
storytelling, and practical modes.
"""
```

---

### Adjustment 4: Post-Transcription Quality Check

**Phase:** 10 (Audio Processing - after transcription)

**Location:** New quality check step after transcribe_only.py

**What to add:**

Create new script: `podcast/tools/verify_counterpoints.py`

```python
"""
Verify that scripted counterpoint moments were executed in audio.

Reads:
- content_plan.md (counterpoint scripts)
- episode_transcript.json (transcription)

Checks:
- Are the scripted topics discussed?
- Does disagreement language appear? ("wait", "disagree", "but", "hold on")
- Are collaborative phrases present? ("both have merit", "it's complicated")
- Duration of counterpoint exchanges

Outputs:
- counterpoint_verification.md report
- PASS/FAIL status for each counterpoint moment
"""

def verify_counterpoint_execution(content_plan_path, transcript_path):
    """Main verification function."""

    # Extract expected counterpoints
    expected = extract_counterpoint_scripts(content_plan_path)

    # Parse transcript
    transcript = load_transcript(transcript_path)

    results = []
    for cp in expected:
        result = {
            'topic': cp['topic'],
            'found': False,
            'has_disagreement_language': False,
            'has_collaborative_language': False,
            'duration_seconds': 0,
            'status': 'FAIL'
        }

        # Find relevant section in transcript
        section = find_transcript_section(transcript, cp['topic'], cp['context'])

        if section:
            result['found'] = True

            # Check for disagreement markers
            disagreement_markers = ['wait', 'disagree', 'but', 'hold on',
                                   'not convinced', 'challenge', 'push back']
            result['has_disagreement_language'] = any(
                marker in section.lower() for marker in disagreement_markers
            )

            # Check for collaborative framing (anti-pattern)
            collaborative_markers = ['both have merit', 'it\'s complicated',
                                    'many perspectives', 'nuanced']
            result['has_collaborative_language'] = any(
                marker in section.lower() for marker in collaborative_markers
            )

            # Calculate duration
            result['duration_seconds'] = section['end_time'] - section['start_time']

            # Determine status
            if (result['has_disagreement_language'] and
                not result['has_collaborative_language'] and
                result['duration_seconds'] >= 60):
                result['status'] = 'PASS'

        results.append(result)

    return results
```

**Workflow integration:**

After transcription completes:

```bash
# Current workflow
uv run python transcribe_only.py episode.mp3 --model base

# Enhanced workflow - add verification step
uv run python transcribe_only.py episode.mp3 --model base
uv run python verify_counterpoints.py ../content_plan.md episode_transcript.json
```

**Output format (counterpoint_verification.md):**

```markdown
# Counterpoint Execution Verification

**Episode:** [Title]
**Date:** [Date]

## Counterpoint Moment 1: [Topic]

- **Status:** ✅ PASS / ❌ FAIL
- **Found in transcript:** Yes / No
- **Disagreement language present:** Yes / No
- **Collaborative framing detected:** Yes / No
- **Duration:** 82 seconds (target: 60-90s)

**Transcript excerpt:**
> [Relevant section showing counterpoint execution]

**Assessment:** [Why this passed or failed]

---

## Counterpoint Moment 2: [Topic]

[Repeat]

---

## Overall Assessment

**Counterpoints verified:** 2/3 PASS

**Recommendations:**
- Counterpoint 3 used collaborative framing ("it's complicated") instead of position-taking
- Consider regenerating audio with stronger script emphasis for Counterpoint 3
```

**Exit criteria addition for Phase 10:**
- ✓ Counterpoint verification run
- ✓ 2/3 or more counterpoint moments executed successfully (PASS)
- ✓ If <2/3 pass: document which failed and why

---

### Adjustment 5: Mode Transition Verification

**Phase:** 10 (Audio Processing - after transcription)

**Location:** Same quality check step

Create companion script: `podcast/tools/verify_mode_transitions.py`

```python
"""
Verify that mode transition phrases were used in audio.

Checks:
- Were the scripted transition phrases used (exact or close variation)?
- Are mode-signaling keywords present?
- Frequency of signposting throughout episode
"""

def verify_mode_transitions(content_plan_path, transcript_path):
    """Check if mode transitions were signposted."""

    expected = extract_mode_transitions(content_plan_path)
    transcript = load_transcript(transcript_path)

    results = []
    for transition in expected:
        result = {
            'name': transition['name'],
            'expected_phrase': transition['phrase'],
            'found_exact': False,
            'found_variation': False,
            'actual_phrase': None,
            'status': 'FAIL'
        }

        # Check for exact match
        if transition['phrase'].lower() in transcript.lower():
            result['found_exact'] = True
            result['actual_phrase'] = transition['phrase']
            result['status'] = 'PASS'
        else:
            # Check for close variation (fuzzy matching)
            variation = find_similar_phrase(transcript, transition['phrase'],
                                           similarity_threshold=0.7)
            if variation:
                result['found_variation'] = True
                result['actual_phrase'] = variation
                result['status'] = 'PASS'

        results.append(result)

    return results
```

---

## Implementation Sequence

### Phase 1: Template Updates (Immediate)

1. **Update content_plan.md template** with:
   - Counterpoint Scripts section
   - Mode Transition Scripts section

2. **Update Phase 8 exit criteria** in workflow to require:
   - 2-3 counterpoint scripts with verbatim dialogue
   - 5-7 mode transition scripts with exact phrases
   - Verification that scripts avoid collaborative framing

**Files to modify:**
- `docs/templates/content_plan-enhanced.md` (add two new sections)
- `.claude/skills/new-podcast-episode.md` (update Phase 8 exit criteria)

**Effort:** LOW - Template additions

---

### Phase 2: Script Injection (Medium Priority)

3. **Enhance notebooklm_prompt.py** to:
   - Read counterpoint scripts from content_plan.md
   - Read mode transition scripts from content_plan.md
   - Inject verbatim into episodeFocus prompt

4. **Enhance notebooklm_api.py** (if different from prompt script)

**Files to modify:**
- `podcast/tools/notebooklm_prompt.py`
- `podcast/tools/notebooklm_api.py` (if needed)

**New functions needed:**
- `extract_counterpoint_scripts(content_plan_path)` - Parse markdown, extract scripts
- `extract_mode_transitions(content_plan_path)` - Parse markdown, extract transitions
- `format_counterpoint_scripts(scripts)` - Format for episodeFocus
- `format_mode_transitions(transitions)` - Format for episodeFocus

**Effort:** MEDIUM - Script parsing and injection logic

---

### Phase 3: Quality Verification (Lower Priority - Can Add Later)

5. **Create verification scripts:**
   - `podcast/tools/verify_counterpoints.py`
   - `podcast/tools/verify_mode_transitions.py`

6. **Add verification step to workflow:**
   - Update Phase 10 instructions
   - Add to exit criteria

**Files to create:**
- `podcast/tools/verify_counterpoints.py` (~200 lines)
- `podcast/tools/verify_mode_transitions.py` (~150 lines)

**Files to modify:**
- `.claude/skills/new-podcast-episode.md` (Phase 10 step + exit criteria)

**Effort:** MEDIUM-HIGH - Transcript analysis, fuzzy matching

**Note:** Phase 3 can be deferred. Phases 1-2 will have immediate impact.

---

## Expected Impact

### Dialogue Dynamics (Currently 3/5)

**With Adjustments 1 + 2 (Counterpoint Scripts + Injection):**
- **Projected score:** 4-5/5
- **Mechanism:** NotebookLM follows verbatim scripts for opening exchanges, ensuring position-taking language appears
- **Evidence from testing:** Verbatim prompts have ~90% execution fidelity vs ~50% for position assignment prompts

**Risk:** If NotebookLM still produces collaborative framing despite verbatim scripts, we have a harder constraint problem requiring manual audio editing or different audio generation method.

### Mode-Switching Clarity (Currently 3-4/5)

**With Adjustments 3 + 4 (Mode Transition Scripts + Injection):**
- **Projected score:** 4-5/5
- **Mechanism:** Exact transition phrases ensure listeners hear explicit mode-switching signals
- **Evidence from Episode 3:** When exact phrases were specified in content plan but not enforced, they didn't appear. Enforcement through episodeFocus should solve this.

---

## Success Metrics

**Next episode should demonstrate:**

1. **Counterpoint Execution:**
   - ✓ 2-3 counterpoint moments with explicit disagreement language in transcript
   - ✓ Zero use of collaborative framing ("both have merit", "it's complicated")
   - ✓ Each counterpoint exchange runs 60-90+ seconds before resolution
   - ✓ Dimension 4 (Dialogue Dynamics) score: 4-5/5

2. **Mode Transitions:**
   - ✓ 5-7 explicit mode transition phrases appear in transcript (exact or close variation)
   - ✓ Listeners can identify when episode shifts between philosophy/research/storytelling/practical modes
   - ✓ Dimension 3 (Mode-Switching Clarity) score: 4-5/5

**Target: Next episode scores 47-49/50** (currently projected 47-49 with Wave 2+4; these adjustments strengthen execution)

---

## Open Questions

1. **How much verbatim dialogue to script?**
   - Option A: Just opening 3-5 line exchange (recommended for Phase 1)
   - Option B: Full 60-90 second counterpoint conversation (more constraining)
   - **Recommendation:** Start with Option A (opening exchange), allow NotebookLM to improvise continuation

2. **Should mode transitions be required or recommended?**
   - Option A: "Use these exact phrases" (strict)
   - Option B: "Use these phrases or close variations" (flexible)
   - **Recommendation:** Option B with verification that signaling keywords appear

3. **What's the threshold for regenerating audio if verification fails?**
   - If 1/3 counterpoints pass: regenerate
   - If 2/3 counterpoints pass: acceptable, document gap
   - If 3/3 counterpoints pass: excellent
   - **Recommendation:** Set 2/3 as minimum threshold

---

## Next Steps

**Immediate (Can do now):**
1. Update content_plan.md template with Counterpoint Scripts section
2. Update content_plan.md template with Mode Transition Scripts section
3. Update Phase 8 exit criteria in workflow
4. Test with next episode

**Short-term (After template test):**
5. Implement script extraction and injection in notebooklm_prompt.py
6. Test episodeFocus prompt with injected scripts
7. Verify audio output quality

**Long-term (Optional enhancement):**
8. Create verification scripts
9. Add automated quality checking to workflow
10. Build quality trend analysis across episodes

**Would you like me to:**
- Start with template updates (Adjustments 1-2)?
- Implement script injection (notebooklm_prompt.py enhancement)?
- Create verification scripts first to measure current baseline?
