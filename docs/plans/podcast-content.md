# Yudame Research Podcast: Episode Planning Framework

**Version:** 3.1
**Last Updated:** 2026-02-05
**Purpose:** Comprehensive reference and operational instructions for structuring 35-minute educational podcast episodes.

---

## Status Update (2026-02-05)

### Implementation Summary

This document was originally created for a **single-host TTS workflow** (Gemini TTS API). The podcast system has since evolved to use **NotebookLM's two-host AI format**. Many planning concepts remain valuable, but the TTS-specific generation pipeline is now obsolete.

### What's Been Implemented

#### Wave 1 (Research & Synthesis) - COMPLETE AND VALIDATED

The following improvements are now enforced in the workflow (validated on Stablecoin Ep. 8, Feb 4 2026):

| Task | Description | Status |
|------|-------------|--------|
| **B1.1** | Depth Distribution Analysis | ✅ Required in p3-briefing.md, blocking exit criteria |
| **B1.2** | Counterpoint Discovery | ✅ Required for dialogue opportunities |
| **B1.3** | Practical Implementation Audit | ✅ Ensures actionable content with specifics |
| **B2.1** | Takeaway Clarity | ✅ Explicit takeaways required in synthesis |
| **B2.2** | Story Bank | ✅ Stories collected with memorability ratings |

**Validation Results:** Pre-refactoring 28/50 (56%) -> Post-Wave 1 44/50 (88%), +16 points improvement.

**Artifacts:**
- Enhanced template: `docs/templates/p3-briefing-enhanced.md`
- Workflow enforcement: `.claude/skills/new-podcast-episode.md` (Phase 6 exit criteria)
- Synthesis agent: `.claude/agents/podcast-synthesis-writer.md` (input validation)

#### Wave 2 (Episode Planning) - TEMPLATE CREATED, READY FOR IMPLEMENTATION

The enhanced content plan template exists at `docs/templates/content_plan-enhanced.md` with:

| Task | Description | Status |
|------|-------------|--------|
| **A1.1** | Episode Structure Map | ✅ Template created - maps philosophical, practical, storytelling, analytical modes |
| **A1.2** | Mode-Switching Framework | ✅ Template created - defines 5 modes with language markers |
| **A1.3** | Signposting Language | ✅ Template created - transition phrases for NotebookLM |
| **A1.4** | Depth Budget | ✅ Template created - time allocation with runtime constraint guidance |
| **A2.1** | Problem -> Solution Architecture | ✅ Template created - separates problem exploration from solution |
| **A2.2** | Build Toward Resolution | ✅ Template created - works backward from main takeaway |
| **A2.3** | Counterpoint Moments Design | ✅ Template created - assigns speaker positions for debates |
| **E1.1** | Update content_plan.md template | ✅ Template created at `docs/templates/content_plan-enhanced.md` |
| **E1.2** | Create podcast-episode-planner skill | ✅ Created at `.claude/skills/podcast-episode-planner/SKILL.md` |

**Artifacts:**
- Enhanced template: `docs/templates/content_plan-enhanced.md`
- Planner skill: `.claude/skills/podcast-episode-planner/SKILL.md`

### What's Superseded or Obsolete

| Original Section | Status | Replacement/Notes |
|------------------|--------|-------------------|
| Section 1.4: Output Pipeline (TTS phases) | Obsolete | NotebookLM handles audio generation directly |
| Section 6: Episode Plan Output Format | Superseded | `docs/templates/content_plan-enhanced.md` has enhanced structure |
| Appendix B: Script Generation with TTS Directives | Obsolete | No longer generate script.md; NotebookLM creates audio directly |
| Appendix C: File Structure (script.md reference) | Obsolete | script.md no longer generated |
| Section 7.1: Word count criteria for script.md | Obsolete | NotebookLM controls duration |

### What Remains Valuable and Current

| Section | Status | Notes |
|---------|--------|-------|
| Section 1.1-1.3: Core Mission, Persona, Episode Anatomy | ✅ Current | Foundational principles still apply |
| Section 2: Section Structure (Blended Approach) | ✅ Current | WHY/WHAT/HOW ratios still apply |
| Section 3: State Tracking Requirements | ✅ Current | Concepts established, callbacks |
| Section 4: The Toolkit | ✅ Current | Opening hooks, clarity devices, takeaways |
| Section 5: Episode Planning Process (conceptual) | ✅ Current | Enhanced by Wave 2 template |
| Section 7.2-7.6: Quality Criteria (non-TTS) | ✅ Current | Adapted into quality scorecard |
| Section 8: Quick Reference | ✅ Current | Useful reference tables |
| Appendix A: Episode Type Examples | ✅ Current | Illustrative examples |

### Future Work (Not Yet Implemented)

**Wave 3 (Audio Generation Enhancement):**
- [ ] A3.1 - Enhanced episodeFocus prompt with structural guidance
- [ ] A3.2 - Dialogue Dynamics section for NotebookLM (counterpoint execution)
- [ ] A3.3 - Episode Arc Template integration
- [ ] E1.3 - Update notebooklm_prompt.py script

**Wave 4 (Publishing & Productization):**
- [ ] C1.1-C1.3 - Description enhancements, CTA framework, source presentations (HIGH PRIORITY - quick wins)
- [ ] C2.1-C2.3 - Feed.xml metadata improvements (LOW PRIORITY)
- [ ] C3.1-C3.2 - Companion resources, landing pages (MEDIUM PRIORITY)

**Wave 5 (Quality Gates):**
- [ ] E3.1 - Phase 8 exit criteria with counterpoint execution checks
- [ ] E3.2 - Phase 11 exit criteria for packaging

See `docs/plans/podcast_episode_improvements.md` for the complete task list, status, and lessons learned.

---

## 1. Framework Overview

### 1.1 Core Mission

Transform rigorous academic research into accessible, engaging audio content that respects the listener's intelligence while never losing them in complexity. Each episode answers a single core question from a specific perspective, providing listeners with both deep understanding and actionable protocols.

### 1.2 Persona: The Authoritative Educator

**Model:** Andrew Huberman's presentation style

**Characteristics:**
- Stays within the bounds of available evidence
- Does not speculate beyond the data
- Acknowledges uncertainty and limitations openly
- Explains technical concepts without dumbing them down
- Uses everyday analogies to anchor abstract concepts
- Provides specific, actionable protocols with practical parameters
- Treats listeners as capable of understanding sophisticated material

**Listener Context:**
- Intelligent professionals who value depth over shortcuts
- Not concerned with fine-grain budgeting (cost comparisons are not relevant)
- Prefer practical, intuitive measures over precise imperial units

**Voice Principles:**
- Warm but authoritative
- Curious and intellectually engaged
- Direct without being dismissive
- Confident in claims that have support; measured in claims that don't

### 1.3 Episode Anatomy

**Total Duration:** ~35 minutes (acceptable range: 30-40 minutes)

**Structure:** Three sections of approximately 12 minutes each

| Section | Name | Duration Target | Primary Focus |
|---------|------|-----------------|---------------|
| 1 | Foundation | ~12 min | WHY: Mechanism, context, significance |
| 2 | Evidence | ~12 min | WHAT: Studies, perspectives, data synthesis |
| 3 | Application | ~11 min | HOW: Protocols, takeaways, action items |

### 1.4 Output Pipeline

> **Note:** This section updated for NotebookLM workflow. TTS pipeline is obsolete.

**Current Pipeline (NotebookLM Two-Host):**

```
Phase 1-6: Research & Synthesis
report.md + sources.md + p3-briefing.md -> content_plan.md (guidance)

Phase 7-9: Audio Generation
content_plan.md + report.md -> NotebookLM -> audio.mp3

Phase 10-11: Post-Processing & Publishing
audio.mp3 -> transcription -> chapters -> feed.xml
```

**Required Files:**
| File | Purpose | Target Size |
|------|---------|-------------|
| `report.md` | Synthesized research | 15-25KB |
| `sources.md` | Validated citations | 5-10KB |
| `content_plan.md` | Episode structure guide | 8-12KB |
| `p3-briefing.md` | Master research briefing (Wave 1 enhanced) | 10-15KB |

---

## 2. Section Structure: The Blended Approach

Sections are not rigid silos. Each section has a primary focus with secondary and tertiary touches that create continuity and prevent jarring transitions.

### 2.1 Section 1: Foundation

**Blend Ratio:** 70% WHY / 20% WHAT / 10% HOW

**Purpose:** Establish the underlying mechanism, build foundational understanding, and create the mental scaffolding for everything that follows.

**Content Focus:**
- Why this topic matters (relevance, stakes)
- The underlying mechanism or principle
- How researchers approached this question (methodology context)
- Key terminology introduced and defined
- Preview of key concepts that will be explored
- Light foreshadowing of practical applications

**Note:** Section 1 builds understanding of concepts and research approaches. Conclusions and takeaways belong in Sections 2-3. Introduce the "what" and "how" of the research before revealing "what we found."

**Micro-Structure:**

| Timing | Element | Function |
|--------|---------|----------|
| 0:00-1:30 | Episode hook | Capture attention, establish relevance |
| 1:30-2:30 | Roadmap | Preview the three sections briefly |
| 2:30-8:00 | Core mechanism | The foundational "why" with 2-3 key concepts |
| 8:00-10:00 | Key terminology | Define essential terms for later use |
| 10:00-11:30 | Synthesis | Connect concepts, reinforce importance |
| 11:30-12:00 | Bridge | Transition to Section 2 with forward momentum |

### 2.2 Section 2: Evidence

**Blend Ratio:** 70% WHAT / 20% WHY / 10% HOW

**Purpose:** Present the evidence base - studies, data, perspectives - while maintaining connection to the foundational "why" and hinting at practical implications.

**Content Focus:**
- Key studies and their findings
- Multiple perspectives on contested points
- Where evidence agrees and disagrees
- Why particular findings matter (callbacks to mechanism)
- Emerging implications for practical application

**Micro-Structure:**

| Timing | Element | Function |
|--------|---------|----------|
| 0:00-1:00 | Section hook | Re-engage, establish section focus |
| 1:00-5:00 | Evidence block A | First major study/perspective cluster |
| 5:00-8:00 | Evidence block B | Second major study/perspective cluster |
| 8:00-10:00 | Synthesis | Where evidence agrees, where it conflicts, why |
| 10:00-11:30 | Implications | What this means (bridge toward application) |
| 11:30-12:00 | Bridge | Transition to Section 3 |

### 2.3 Section 3: Application

**Blend Ratio:** 70% WHAT (synthesized takeaways) / 20% WHY / 10% HOW (implicit in protocols)

**Purpose:** Deliver actionable protocols and synthesized takeaways. The "how" is embedded in specific, concrete recommendations.

**Content Focus:**
- Actionable protocols with specific parameters
- Prioritized recommendations
- Brief callbacks to the "why" for reinforcement
- Clear, memorable takeaways
- Episode summary using What -> So What -> Now What pattern (implicit, not stated)

**Micro-Structure:**

| Timing | Element | Function |
|--------|---------|----------|
| 0:00-1:00 | Section hook | "Now let's translate this into action" |
| 1:00-7:00 | Protocols | 2-4 actionable recommendations with specifics |
| 7:00-9:00 | Caveats/context | Who this applies to, limitations, customization |
| 9:00-10:30 | Synthesis | Tie back to mechanism, reinforce key points |
| 10:30-12:00 | Episode close | Summary, callback to opening, final thought |

---

## 3. State Tracking Requirements

Later sections must know what was fully covered in earlier sections to:
- Avoid accidental repetition
- Enable intentional callbacks for emphasis
- Build on established concepts without re-explaining

### 3.1 Concepts Fully Established

**After Section 1, track:**
- Terms defined (can use freely without re-definition)
- Mechanisms explained (can reference without re-explaining)
- Key statistics or claims introduced (can callback to these)

**After Section 2, add:**
- Studies summarized (can reference by shorthand)
- Synthesis conclusions reached (can build on these)
- Open questions identified (can address in Section 3 if relevant)

### 3.2 Intentional Repetition Guidelines

Repeat intentionally when:
- A concept is central to understanding (spaced repetition principle)
- Connecting new material to foundational concepts (callbacks)
- Summarizing at section transitions
- Reinforcing key takeaways in conclusion

**Callback Format:** "As we discussed earlier, [brief concept] - this is why [new point]."

---

## 4. The Toolkit

Select appropriate tools based on episode context. Not all tools are used in every episode.

### 4.1 Opening Hooks

**Select based on:** Available source material, topic nature, emotional weight

| Hook Type | Description | Best For | Example Pattern |
|-----------|-------------|----------|-----------------|
| **Provocative Question** | Opens with a question that challenges assumptions | Topics where common beliefs are wrong | "What if everything you believe about X is fundamentally wrong?" |
| **Surprising Statistic** | Specific number that triggers novelty response | Data-rich topics with counterintuitive findings | "X has Y times more Z than A - and that changes everything about how we should think about B." |
| **Bold Claim** | Confident statement of what listener will gain | Protocol-heavy episodes | "By the end of this episode, you'll understand exactly how to X, with specific protocols you can implement today." |
| **In Medias Res Story** | Drops listener into the middle of action | Episodes with strong case studies | "The year is X. Researcher Y is staring at data that shouldn't exist. What they discovered would overturn decades of..." |
| **Counterintuitive Claim** | Statement that contradicts common wisdom | Myth-busting episodes | "The experts have been wrong about this for decades - and the data finally shows us why." |
| **Stakes Establishment** | Why this matters urgently | Health, business risk, time-sensitive topics | "This single factor predicts X better than any other - and most people are getting it completely wrong." |

**Usage Rules:**
- Choose ONE hook type per episode
- Get core idea out within first 60 seconds
- Avoid lengthy introductions or credential-listing before establishing relevance

### 4.2 Series Position Modifiers

**Select based on:** Episode's position within its series

| Position | Modifier | Function |
|----------|----------|----------|
| **Series Opener** | Series Frame Opening | Establish the overarching question the series answers, preview perspectives |
| **Series Opener** | "Why This Series" Block | Explain why this topic warrants deep, multi-episode exploration |
| **Mid-Series** | Perspective Anchor | Briefly state: "This series asks [core question]. This episode answers it through the lens of [perspective]." |
| **Series Closer** | Synthesis Frame | Acknowledge insights from previous episodes, position this as culminating perspective |
| **Series Closer** | Series Wrap | Summarize the full arc, highlight how perspectives complemented each other |
| **Standalone** | No series modifiers | Episode is self-contained |

**Series Frame Opening Template:**
> "This is the [first/second/third] episode in our series on [topic]. Throughout this series, we're answering one question: [core question]. Each episode approaches this from a different angle. Today, we're looking at it through the lens of [specific perspective]."

**Series Wrap Template:**
> "This concludes our series on [topic]. We've explored this through [list perspectives covered]. Each perspective revealed something essential: [1-2 sentence synthesis]. Together, they give you a complete framework for [core question]."

### 4.3 Contradiction Handling

**Select based on:** Whether evidence on a topic is contested or in consensus

| Scenario | Tool | Approach |
|----------|------|----------|
| **Clear consensus** | Standard presentation | Present findings directly |
| **Minor disagreement** | Brief acknowledgment | "Some studies suggest X, though the weight of evidence supports Y." |
| **Substantive conflict** | Study Comparison Structure | Describe each study briefly, focus on agreement, explain divergence, synthesize |
| **Irreconcilable conflict** | Insufficient Confidence Dismissal | Note disagreement, explain why no confident recommendation can be made, move on |

**Study Comparison Structure Template:**
> "Study A, from [institution/year], found [finding]. Study B, from [institution/year], found [different/opposing finding]. Where they agree: [common ground]. Where they diverge: [specific disagreement]. The likely explanation for this discrepancy is [methodological difference / population difference / measurement difference]. For our purposes, this means [synthesis or actionable implication]."

**Insufficient Confidence Dismissal Template:**
> "The evidence on [specific sub-topic] is genuinely mixed - studies have produced conflicting results, and we can't include it in our protocols with confidence. What we *can* say is [whatever is established], so let's focus there."

### 4.4 Clarity Devices

**Select based on:** Concept abstraction level, need for memorability

| Device | Description | When to Use | Usage Limit |
|--------|-------------|-------------|-------------|
| **Everyday Analogy** | Compares abstract concept to familiar experience | Dense/abstract mechanisms | Unlimited, use liberally |
| **"Imagine..." Scenario** | Invites listener to visualize | Complex processes, temporal sequences | 2-3 per episode |
| **Metaphor** | Sustained comparison that frames understanding | Core concepts that recur throughout | 1-2 per episode, commit to using throughout |
| **Mnemonic/Acronym** | Memory device for multi-part protocols | Critical protocols with 3+ steps | MAX 1 per episode, use rarely |
| **Rhyme/Rhythm** | Memorable phrasing for key principles | Foundational rules that should stick | MAX 1 per episode, use very rarely |

**Everyday Analogy Examples:**
- HRV: "Think of it like the responsiveness of your car's suspension - you want it to absorb bumps smoothly, not be rigid."
- VO2 max: "It's essentially your body's horsepower - how much energy you can produce when you need it most."
- Polarized training: "It's like practicing piano: most of your time is slow, deliberate practice, but occasionally you perform at full intensity."

**Mnemonic Decision Criteria:**
Before creating a mnemonic, ask:
1. Is this a multi-step protocol the listener will need to recall?
2. Is the sequence/combination critical to getting it right?
3. Will they use this repeatedly?

If yes to all three, consider a mnemonic. Otherwise, skip it.

**Acronym Rule:** Always spell out acronyms on first use:
- "polyunsaturated fatty acids, or PUFA" - then use "PUFA" freely
- "high-intensity interval training, or HIIT" - then use "HIIT"

### 4.5 Takeaway Structures

**Select based on:** Content type, listener action requirements

| Structure | Description | Best For |
|-----------|-------------|----------|
| **Numbered Protocol** | Step 1, Step 2, Step 3... | Sequential actions where order matters |
| **Prioritized Single Action** | "If you do nothing else, do X" | When one intervention dominates |
| **Tiered Recommendations** | Beginner / Intermediate / Advanced | When optimal action depends on baseline |
| **Conditional Protocol** | "If X, then Y; if A, then B" | When context determines best action |
| **Minimum Effective Dose** | The least you can do for meaningful benefit | When listener bandwidth is limited |

**Specificity Requirement:** All protocols must include specific parameters:
- Timing: "90-120 minutes after waking" not "in the morning"
- Duration: "5 continuous minutes" not "a few minutes"
- Frequency: "3 times per week" not "regularly"
- Dosage: "2-4 grams" not "some"

**Practical Measures:** Use metric units (grams, ml) or intuitive descriptions:
- "A handful of almonds" or "30 grams" - not "1 oz"
- "A thumb-sized piece of cheese" - not "1.5 oz"
- "A palm-sized portion of protein" - not "4 oz"

### 4.6 Narrative Devices

**Select based on:** Available source material

| Device | Description | When to Use |
|--------|-------------|-------------|
| **Case Study as Story** | Transform a research case into narrative | When source material includes compelling individual cases |
| **Research Journey** | Frame the scientific discovery process as a story | When the history of discovery is interesting |
| **Data Woven into Story** | Embed statistics within an ongoing narrative | When data alone is dry but important |
| **Problem-Solution Arc** | Present problem, failed attempts, eventual solution | When topic evolved through trial and error |

**Case Study as Story Template:**
> "Consider the case of [subject/context]. [Initial situation]. Then, [inciting incident or intervention]. What happened next surprised even the researchers: [outcome]. This case illustrates [principle]."

**Cold Data Rule:** If data cannot be woven into an existing narrative or converted to an actionable guideline, leave it out. Isolated statistics without context compete with core content.

### 4.7 Attention Maintenance

**These are structural defaults, not optional tools:**

| Technique | Frequency | Implementation |
|-----------|-----------|----------------|
| **Content type rotation** | Every 5-7 minutes | Cycle through: explanation -> example -> insight -> story -> implication |
| **Pattern interrupts** | Every 7-10 minutes | Vocal shift, topic pivot, direct address, or meta-commentary |
| **Open loops** | 1-2 per section max | Introduce a question answered later; always close before episode ends |
| **Signposting** | At every major transition | Explicit markers: "Key point here...", "This brings us to...", "The crucial finding is..." |

### 4.8 Solo Host Energy Techniques

> **Note:** These techniques apply to single-host format. For NotebookLM two-host format, see Counterpoint Moments Design in `docs/templates/content_plan-enhanced.md`.

| Technique | Description | Example |
|-----------|-------------|---------|
| **Rhetorical self-interrogation** | Ask yourself questions the listener is thinking | "Okay, let's pause on that statistic. What does that actually mean?" |
| **Number translation** | Give the number, then make it tangible | "R equals 0.64... that means nearly 40% of the difference is explained by this one factor" |
| **Committed metaphors** | Introduce a metaphor and use it throughout | Introduce "hippocampal desk" in Section 1, reference it in Sections 2-3 |
| **Escalating stakes** | Layer importance as you go | "This is important... Here's where it gets stunning... This is the finding that changes everything" |
| **Real-terms translation** | Convert abstract to concrete | "Let's put that in real terms for our listener..." |

**Solo Signposting Phrases:**
- "Okay, let's pause on that"
- "Give me the hard numbers here"
- "Let's put that in real terms"
- "Here's where it gets interesting"
- "This is the finding that should make you sit up"
- "And this is the critical follow-up"

**Open Loop Rules:**
- Use only when multiple lines of reasoning genuinely require it
- Always close loops before episode ends
- Target curiosity around key learning points
- Avoid manufactured cliffhangers - these feel manipulative in educational content

### 4.9 Summary Patterns

**"What -> So What -> Now What" (Implicit)**

Use this three-part pattern for any concise summary (intro preview, section transitions, episode conclusion) WITHOUT stating the words "what, so what, now what" explicitly.

| Component | Function | Example |
|-----------|----------|---------|
| **What** | State the finding/concept | "Exercise intensity matters more than duration for cardiovascular adaptation." |
| **So What** | Why it matters | "This means you can achieve better results in less time - if you structure it correctly." |
| **Now What** | What to do | "Aim for 2-3 high-intensity sessions per week, keeping 80% of your training easy." |

**Conclusion Callback Requirement:** The episode conclusion must reference or resolve the opening hook, creating a complete arc.

### 4.10 Sparkline Structure (Business Strategy Episodes Only)

For episodes involving strategic analysis or future projection, use Nancy Duarte's "What Is vs. What Could Be" oscillation.

**Structure:**
1. Present current state (what is)
2. Present aspirational state (what could be)
3. Return to current state with new problem/opportunity
4. Return to aspirational state with solution
5. Repeat until convergence
6. End on "new bliss" - the achievable future state

**Use Only For:** Business strategy, market analysis, speculative forward-looking episodes

**Do Not Use For:** Health/science episodes, evidence synthesis, protocol-focused content

---

## 5. Episode Planning Process

> **Note:** This section provides conceptual guidance. For the full enhanced template with Wave 2 improvements (A1.1-A1.4, A2.1-A2.3, E1.1-E1.2), see `docs/templates/content_plan-enhanced.md`.

### 5.1 Required Inputs

Before structuring an episode, gather:

1. **Episode topic** (specific perspective/angle)
2. **Core question** the episode answers
3. **Series context** (if applicable):
   - Series title and core question
   - Episode position (opener, middle, closer, standalone)
   - Perspectives covered in other episodes (for cross-reference avoidance)
4. **Source material summary:**
   - Key studies with findings
   - Case studies available
   - Contradictions/contested points
   - Available data/statistics
5. **Content type indicators:**
   - Is evidence contested or consensus?
   - Are case studies/stories available?
   - Is this protocol-heavy or concept-heavy?

### 5.2 Planning Steps

**Step 1: Episode Classification**

Determine episode type based on inputs:
- Series position: opener / middle / closer / standalone
- Evidence status: consensus / minor conflict / major conflict
- Content density: concept-heavy / protocol-heavy / balanced
- Narrative availability: case studies present / data-only / research journey available

**Step 2: Toolkit Selection**

Based on classification, select:
- Opening hook type (1)
- Series position modifiers (if applicable)
- Contradiction handling approach (if applicable)
- Clarity devices needed (as many as useful)
- Takeaway structure (1 primary, may combine)
- Narrative devices (if source material supports)
- Memorability device (0-1, only if criteria met)

**Step 3: Section Planning**

For each section, determine:
- Primary concepts to cover (limit to 2-3 major points per section)
- Key terms to define (Section 1 primarily)
- Studies to reference (Section 2 primarily)
- Protocols to present (Section 3 primarily)
- Callbacks to earlier material (Sections 2-3)
- Transition approach to next section

**Step 4: State Tracking Setup**

Create tracking lists:
- Terms defined (after Section 1)
- Concepts established (after each section)
- Claims made (for callback opportunities)
- Open loops (must all close by end)

**Step 5: Output Generation**

Produce structured content for each section with:
- Section objectives
- Key points in sequence
- Suggested tools/devices
- Transition language
- Callback opportunities marked
- Time allocation guidance

---

## 6. Episode Plan Output Format

> **Superseded by Wave 2 Improvements:** The full enhanced template is now at `docs/templates/content_plan-enhanced.md`. That template includes:
> - Episode Structure Map (A1.1)
> - Mode-Switching Framework (A1.2)
> - Signposting Language (A1.3)
> - Depth Budget (A1.4)
> - Problem -> Solution Architecture (A2.1)
> - Build Toward Resolution (A2.2)
> - Counterpoint Moments Design (A2.3)
> - Quality Checklist (E3.1)

For reference, the basic structure is:

```markdown
# Episode Plan: [Episode Title]

## Episode Metadata
- Series: [Series name or "Standalone"]
- Position: [Opener / Middle / Closer / Standalone]
- Core Question: [The question this episode answers]
- Episode Type: [Evidence status] + [Content density]

## Toolkit Selections
- Hook Type: [Selected hook]
- Takeaway Structure: [Selected structure]
- Contradiction Handling: [Approach if applicable]

## NotebookLM Guidance
[Opening instructions, key terms, studies to emphasize, narrative arc]

## Section Plans
[Foundation, Evidence, Application with specifics]

## Quality Checklist
[Pre-generation verification]
```

**Use `docs/templates/content_plan-enhanced.md` for the complete enhanced template with Wave 2 improvements.**

---

## 7. Quality Criteria

> **Note:** These criteria have been expanded into a 10-dimension quality scorecard. See `.claude/skills/podcast-quality-scorecard/SKILL.md` for the full framework. The scorecard is now applied to every episode.

### 7.1 Structure

- [ ] Three sections with blended focus (WHY/WHAT/HOW ratios respected)
- [ ] Each section has beginning, middle, end micro-structure
- [ ] Total content maps to ~35 minutes (30-40 acceptable)
- [ ] No section exceeds 14 minutes or falls below 10 minutes

### 7.2 Clarity

- [ ] Maximum 3-4 major concepts per section
- [ ] All key terms defined before use
- [ ] Abstract concepts anchored with everyday analogies
- [ ] Complex mechanisms broken into digestible steps

### 7.3 State Tracking

- [ ] No accidental repetition (same explanation twice without purpose)
- [ ] Intentional callbacks clearly marked
- [ ] Later sections reference earlier concepts by shorthand
- [ ] All open loops closed by episode end

### 7.4 Tooling

- [ ] Hook type matches available material and topic nature
- [ ] Series modifiers included only when position applies
- [ ] Contradiction handling matches evidence status
- [ ] Memorability devices used sparingly (max 1) with justification
- [ ] Takeaway structure matches content type

### 7.5 Specificity

- [ ] Protocols include specific parameters (timing, duration, frequency, dosage)
- [ ] Statistics are precise, not rounded vaguely
- [ ] Studies referenced with enough context to be credible
- [ ] Recommendations are actionable, not abstract

### 7.6 Narrative Coherence

- [ ] Opening hook connects to closing callback
- [ ] Section transitions feel natural, not abrupt
- [ ] Episode answers its stated core question
- [ ] "What -> So What -> Now What" pattern implicit in summaries

---

## 8. Quick Reference

### 8.1 Section Blend Ratios

| Section | WHY | WHAT | HOW |
|---------|-----|------|-----|
| 1: Foundation | 70% | 20% | 10% |
| 2: Evidence | 20% | 70% | 10% |
| 3: Application | 20% | 70% | (implicit) |

### 8.2 Toolkit Selection Matrix

| If Episode Has... | Consider Using... |
|-------------------|-------------------|
| Strong case study in source material | Case Study as Story, In Medias Res hook |
| Counterintuitive findings | Counterintuitive Claim hook, pattern interrupt at reveal |
| Contested evidence | Study Comparison Structure or Insufficient Confidence Dismissal |
| Multi-step protocol | Numbered Protocol takeaway, consider mnemonic (if criteria met) |
| Abstract mechanism | Multiple everyday analogies, "Imagine..." scenarios |
| Series opener position | Series Frame Opening, "Why This Series" block |
| Series closer position | Synthesis Frame, Series Wrap |
| Business/strategy topic | Sparkline structure (What Is vs. What Could Be) |

### 8.3 Specificity Examples

| Vague (Avoid) | Specific (Use) |
|---------------|----------------|
| "in the morning" | "90-120 minutes after waking" |
| "regularly" | "3 times per week" |
| "some studies show" | "A 2023 meta-analysis of 47 trials found" |
| "significant improvement" | "17% reduction in all-cause mortality" |
| "take some magnesium" | "300-400mg magnesium glycinate" |
| "do high intensity work" | "4x4 minute intervals at 90-95% max heart rate" |

### 8.4 Callback Language Templates

- "As we covered in Section 1, [concept] - this is exactly why [new point]."
- "Remember the mechanism we discussed? [Brief reference]. This study shows it in action."
- "This brings us back to [opening hook reference]. Now you understand why."
- "The [term defined earlier] we discussed is what's driving this effect."

---

## Appendix A: Episode Type Examples

### Example A: Consensus Science, Protocol-Heavy

**Topic:** VO2 Max optimization
**Episode Type:** Consensus + Protocol-heavy
**Selected Tools:**
- Hook: Bold Claim ("By the end of this episode, you'll have the complete protocol...")
- Takeaway: Tiered Recommendations (beginner/intermediate/advanced)
- Clarity: Multiple everyday analogies for physiological concepts
- No contradiction handling needed
- No memorability device (protocols are simple enough)

### Example B: Contested Evidence, Concept-Heavy

**Topic:** Saturated fat and cardiovascular health
**Episode Type:** Major Conflict + Concept-heavy
**Selected Tools:**
- Hook: Counterintuitive Claim ("The experts have been arguing about this for decades...")
- Contradiction Handling: Study Comparison Structure (multiple uses)
- Takeaway: Conditional Protocol ("If your context is X, then Y...")
- Clarity: Everyday analogies for lipid metabolism
- Final synthesis: Insufficient Confidence Dismissal for truly unresolved questions

### Example C: Series Opener, Balanced

**Topic:** Cardiovascular Health - Lifestyle Foundations (Episode 1 of series)
**Episode Type:** Series Opener + Consensus + Balanced
**Selected Tools:**
- Hook: Stakes Establishment ("This single metric predicts longevity better than any other...")
- Series Modifier: Series Frame Opening + "Why This Series" block
- Takeaway: Prioritized Single Action ("If you do nothing else...")
- Narrative: Research Journey (how VO2 max became recognized as key predictor)

### Example D: Business Strategy, Speculative

**Topic:** Solomon Islands Telecom - Market Entry Strategy
**Episode Type:** Standalone + Speculative + Balanced
**Selected Tools:**
- Hook: Provocative Question ("What would it take to launch a telecom in one of the world's most challenging markets?")
- Sparkline Structure: What Is (current duopoly) vs. What Could Be (new entrant opportunity)
- Takeaway: Conditional Protocol (different strategies for different entry approaches)
- Narrative: Case Study as Story (comparable market entries in similar contexts)

---

## Appendix B: TTS Script Generation (OBSOLETE)

> **Status:** This section described the Gemini TTS-based script generation workflow. The podcast system now uses NotebookLM's two-host AI format, which handles audio generation internally.
>
> For historical reference, the TTS pipeline involved:
> - Generating `script.md` with ~5,200 words and TTS directives
> - Splitting at `[TRANSITION: new section]` markers
> - Processing through Gemini TTS API in 3 sections
> - Stitching and exporting MP3
>
> **Current Workflow:** Upload `content_plan.md` and research materials to NotebookLM, which generates the audio directly.

---

## Appendix C: File Structure

Current episode directory structure:

```
podcast/episodes/[series]/[episode-slug]/
├── research/
│   ├── p1-brief.md           # Phase 1 research query
│   ├── p2-*.md               # Phase 2 research results
│   └── p3-briefing.md        # Phase 3 synthesis (enhanced with Wave 1)
├── report.md                 # Narrative synthesis (~18KB)
├── sources.md                # Validated links (~8KB)
├── content_plan.md           # Episode structure (~10KB)
├── YYYY-MM-DD-slug.mp3       # Final audio (~30MB)
├── YYYY-MM-DD-slug_transcript.json  # Whisper output
├── YYYY-MM-DD-slug_chapters.txt     # FFmpeg metadata
├── YYYY-MM-DD-slug_chapters.json    # Podcasting 2.0
└── logs/
    ├── metadata.md           # Episode metadata
    └── quality_scorecard.md  # Quality assessment
```

**Note:** `script.md` is no longer generated. Audio is produced directly by NotebookLM.

---

## Related Documents

- **Enhanced Content Plan Template:** `docs/templates/content_plan-enhanced.md`
- **Enhanced Research Briefing Template:** `docs/templates/p3-briefing-enhanced.md`
- **Episode Planner Skill:** `.claude/skills/podcast-episode-planner/SKILL.md`
- **Quality Scorecard:** `.claude/skills/podcast-quality-scorecard/SKILL.md`
- **Improvement Plan:** `docs/plans/podcast_episode_improvements.md`
- **Main Workflow:** `.claude/skills/new-podcast-episode.md`

---

*Version 3.1 - Updated for NotebookLM workflow, Wave 1-2 improvements documented*
*Status: Active (with noted obsolete sections)*
