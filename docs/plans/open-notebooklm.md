# Open NotebookLM: Single-Host Research Podcast Generation

A system for transforming research reports into compelling single-host podcast monologues with a distinctive voice and uncompromising quality standards.

## Vision

Create a pipeline that transforms written research reports into broadcast-quality solo podcast episodes—delivered by a charismatic, intellectually rigorous host voice that becomes synonymous with the Yudame Research brand.

**Key Differentiator:** Single host eliminates the hardest problem (fake dialogue) and allows full focus on what matters: a compelling monologue that honors great ideas.

---

## The Yudame Research Voice

### Brand Identity

**Yudame Research is:**
- **Thoughtful** — Every word earns its place
- **Detailed** — Depth without drowning
- **Skeptical** — Questions before conclusions
- **Patient** — Ideas unfold at their natural pace
- **Valuable** — Listener's time is respected
- **Worthy** — Content deserves attention
- **Fidelity** — Accuracy and clarity above all

### What Makes Great Monologue

- The topic is the host's **genuine obsession**
- Laughing at ironies and absurdities
- **Rare expletives** as excited reaction to breakthrough ideas ("This is *bullshit*" when calling out bad research, "Holy shit" at genuine revelations)
- **Passion to truly get ideas across** — not performing, teaching
- **Honor great sources** — name researchers, link in show notes
- Natural self-correction ("Actually, let me back up...")
- Thinking out loud, not reading

### What Makes Great Education

1. **Start with a question that raises a problem**
2. **Lead to a bigger question and bigger problem**
3. **Tell a story**
4. **Tell another story**
5. **Weave them together with a common moral**
6. **Identify exceptions and contradictions**
7. **Bite-size takeaways or punchy quotes**
8. **Imagine the limit case**
9. **"Paint the picture"** with just the appropriate dose of information
10. **What, So What, Now What**

### The Voice

- **Accent:** Charismatic Austrian or German speaking English
- **Delivery:** Enunciation and projection of a popular university professor
- **Energy:** Intellectually alive, not caffeinated
- **Presence:** Commands attention without demanding it

---

## Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           PODCAST GENERATION PIPELINE                                │
├─────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────┤
│                 │                 │                 │                 │             │
│     SCRIPT      │     CRITIC      │     VOICE       │     AUDIO       │  MASTERING  │
│   GENERATION    │    REFINEMENT   │   SYNTHESIS     │   PRODUCTION    │  & DELIVERY │
│                 │                 │                 │                 │             │
│  ┌───────────┐  │  ┌───────────┐  │  ┌───────────┐  │  ┌───────────┐  │ ┌─────────┐ │
│  │  Claude   │  │  │  Trained  │  │  │ ElevenLabs│  │  │  FFmpeg   │  │ │ Loudness│ │
│  │  Opus 4   │  │  │  Critic   │  │  │  Custom   │  │  │  iZotope  │  │ │ Limiting│ │
│  │           │  │  │  Agent    │  │  │  Voice    │  │  │           │  │ │         │ │
│  └───────────┘  │  └───────────┘  │  └───────────┘  │  └───────────┘  │ └─────────┘ │
│        │        │        │        │        │        │        │        │      │      │
│        ▼        │        ▼        │        ▼        │        ▼        │      ▼      │
│   draft.json    │   final.json    │   raw_audio/    │   produced/     │  final.mp3  │
│                 │                 │                 │                 │             │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┴─────────────┘
```

### Pipeline Components

| Component | Purpose | Quality Gate |
|-----------|---------|--------------|
| Script Generation | Transform report to monologue | Critic approval |
| Critic Refinement | Iterative quality improvement | Style guide alignment |
| Voice Synthesis | Generate spoken audio | Pronunciation accuracy |
| Audio Production | Professional polish | Technical standards |
| Mastering | Final optimization | Broadcast compliance |

---

## Component 1: Script Generation

### Purpose

Transform a dense research report into a compelling 30-40 minute monologue that sounds like a passionate expert sharing their obsession.

### Model Selection

**Primary:** Claude Opus 4
- Highest reasoning for complex source material
- Best at maintaining voice consistency
- Superior narrative construction

### Script Structure (The Arc)

**Opening Hook (0:00-2:00)**
```
Start with THE question. The problem that makes this topic matter.
Not "Today we're going to talk about X."
Instead: "Here's something that doesn't make sense..."
```

**Problem Escalation (2:00-5:00)**
```
The question leads to a bigger question.
"But wait—if that's true, then why..."
Build tension. Make the listener NEED the answer.
```

**Story One (5:00-12:00)**
```
A specific story that illuminates the problem.
Name names. Give dates. Make it real.
"In 1987, a researcher named..."
```

**Story Two (12:00-19:00)**
```
A contrasting or complementary story.
Different angle, same underlying truth.
"Meanwhile, on the other side of the world..."
```

**The Weave (19:00-26:00)**
```
Connect the stories. Reveal the common thread.
"Here's what both of these tell us..."
This is where the "aha" lives.
```

**Exceptions & Contradictions (26:00-30:00)**
```
Intellectual honesty. What doesn't fit?
"Now, I should mention—this isn't the whole story."
"There's a study from 2019 that complicates this..."
```

**The Takeaway (30:00-33:00)**
```
What, So What, Now What.
Bite-sized. Quotable. Actionable.
"If you remember nothing else from this episode..."
```

**Close (33:00-35:00)**
```
Honor sources. Tease future episodes.
"The papers I drew from are linked in the show notes."
Leave them thinking.
```

### Script Format

```json
{
  "metadata": {
    "title": "Episode Title",
    "target_duration_seconds": 2100,
    "word_count_target": 5250,
    "generated_at": "2025-12-18T10:00:00Z"
  },
  "segments": [
    {
      "id": 1,
      "type": "hook",
      "duration_target": 120,
      "content": {
        "text": "Here's something that kept me up last night...",
        "delivery": {
          "energy": 0.7,
          "pace": "measured_then_accelerating",
          "emotion": "genuine_puzzlement"
        },
        "notes": {
          "emphasis_words": ["kept", "night"],
          "pause_after": 1.5,
          "laugh_point": null
        }
      }
    },
    {
      "id": 2,
      "type": "escalation",
      "content": {
        "text": "But here's where it gets strange...",
        "delivery": {
          "energy": 0.8,
          "pace": "building",
          "emotion": "intellectual_excitement"
        },
        "notes": {
          "expletive_candidate": false,
          "irony_moment": true
        }
      }
    }
  ],
  "sources_mentioned": [
    {
      "citation": "Smith et al., 2019",
      "link": "https://...",
      "mention_timestamps": [423, 891]
    }
  ],
  "key_quotes": [
    {
      "quote": "The dose makes the poison",
      "attribution": "Paracelsus",
      "timestamp": 1247
    }
  ]
}
```

### Generation Prompt Framework

```markdown
# Yudame Research Podcast Script Generation

## Your Role
You are writing a script for a solo podcast host who is genuinely obsessed
with this topic. Not performing enthusiasm—actually passionate. Think of
the best university lecturer you ever had, the one who made you care about
something you didn't know you cared about.

## The Voice
- Austrian/German accent cadence (write for this rhythm)
- Professor energy: authoritative but accessible
- Genuine reactions: laughs at ironies, occasionally swears at bad ideas
- Thinks out loud: "Actually, let me back up..." "Wait, that's not quite right..."

## Source Material
[Research report content]

## Structure Requirements

### The Arc
1. HOOK: Start with the question/problem that makes this matter
2. ESCALATE: Lead to a bigger question
3. STORY 1: Specific narrative that illuminates
4. STORY 2: Contrasting/complementary narrative
5. WEAVE: Connect them—this is where insight lives
6. EXCEPTIONS: What doesn't fit? Intellectual honesty.
7. TAKEAWAY: What, So What, Now What
8. CLOSE: Honor sources, leave them thinking

### Style Requirements
- Write for SPOKEN delivery, not reading
- Short sentences when making points
- Longer sentences when building atmosphere
- Name researchers and studies specifically
- Round numbers for speech ("roughly forty percent" not "39.7%")
- Include natural self-corrections
- Mark potential laugh/expletive moments (sparingly—maybe 2-3 per episode)

### What to Include
- At least 2 specific stories with names, dates, places
- At least 3 "aha moment" candidates
- At least 1 acknowledged limitation or contradiction
- 3-5 quotable takeaways
- All sources cited by name for show notes

### What to Avoid
- "Today we're going to discuss..."
- "Studies show that..." (say WHICH study)
- Fake enthusiasm ("This is SO fascinating!")
- Explaining things the audience already knows
- Hedging everything into meaninglessness
- Monologue without variation (no 3-minute flat sections)

## Output Format
[JSON schema as defined above]

## Word Count
Target: ~150 words per minute of audio
35-minute episode = ~5,250 words
```

---

## Component 2: Critic Refinement Agent

### Purpose

A trained critic agent that reviews generated scripts against quality standards derived from excellent podcasts (Huberman Lab, Founders Podcast).

### Training Data Sources

**Huberman Lab (Andrew Huberman)**
- Deep scientific rigor
- Clear explanation of mechanisms
- Practical takeaways
- "Protocols" structure
- Genuine enthusiasm for biology

**Founders Podcast (David Senra)**
- Obsessive deep reading
- Story-driven education
- Punchy quotes and insights
- Historical narrative mastery
- Honoring sources ("I learned this from...")

### Critic Agent Design

```markdown
# Podcast Script Critic Agent

## Your Training
You have internalized the quality standards of:
- Huberman Lab: Scientific depth, mechanism clarity, practical protocols
- Founders Podcast: Obsessive research, story-driven insight, punchy wisdom

## Your Task
Review the submitted podcast script and provide:
1. PASS/FAIL overall assessment
2. Specific issues with line-level citations
3. Suggested revisions

## Evaluation Criteria

### Structure (25%)
- Does it start with a compelling question/problem?
- Does tension build appropriately?
- Are stories specific (names, dates, places)?
- Does the weave deliver genuine insight?
- Is intellectual honesty present (limitations acknowledged)?

### Voice Authenticity (25%)
- Does it sound like genuine passion, not performance?
- Are there natural moments (self-correction, thinking aloud)?
- Would the Yudame voice say this? (thoughtful, detailed, skeptical, patient)
- Are rare expletives/laughs earned, not forced?

### Educational Value (25%)
- Is the "What, So What, Now What" clear?
- Are takeaways bite-sized and quotable?
- Would a listener remember the key points?
- Is appropriate information density achieved?

### Source Honoring (25%)
- Are researchers named specifically?
- Are studies cited, not vaguely referenced?
- Is the intellectual lineage clear?
- Would sources be proud to be featured?

## Output Format
{
  "verdict": "PASS" | "REVISE",
  "score": 0-100,
  "issues": [
    {
      "segment_id": 3,
      "severity": "major" | "minor",
      "issue": "Description of problem",
      "suggestion": "How to fix"
    }
  ],
  "strengths": ["What works well"],
  "revision_priority": ["Most important fixes first"]
}
```

### Refinement Loop

```
Script Draft
    │
    ▼
Critic Review ──────┐
    │               │
    │ PASS?         │ REVISE
    │               │
    ▼               ▼
Final Script    Revision with
                specific fixes
                    │
                    └──► Back to Critic
                         (max 3 iterations)
```

### Collecting Training Examples

**From Huberman Lab:**
- Transcribe 10-20 episodes covering different topics
- Annotate: hooks, mechanism explanations, protocol sections
- Extract: sentence patterns, transition phrases, emphasis patterns

**From Founders Podcast:**
- Transcribe 10-20 episodes (especially the best-rated)
- Annotate: story openings, quote integrations, insight moments
- Extract: David's signature phrases, pacing patterns, source acknowledgments

**Training the Critic:**
- Few-shot examples in prompt
- Reference transcripts for style comparison
- Explicit rubric with examples of good/bad

---

## Component 3: Voice Synthesis

### The Yudame Voice

**Target Characteristics:**
- Austrian or German native speaking fluent English
- University professor presence—commands attention naturally
- Clear enunciation without being stiff
- Intellectual warmth
- Capable of energy range: thoughtful quiet to genuine excitement

### Voice Acquisition Strategy

**Option A: Professional Voice Actor**

Commission a voice actor session:
1. Find Austrian/German actor with professor-like delivery
2. 60-90 minute recording session covering:
   - Full emotional range (curious, excited, skeptical, amused, passionate)
   - Technical terminology samples
   - Various energy levels
   - Natural reactions (laughs, sighs, "hmm")
3. Create ElevenLabs Professional Voice Clone
4. Result: Unique, owned brand voice

**Casting Requirements:**
- Native German/Austrian speaker
- Excellent English with charming accent (not heavy)
- Academic or intellectual background preferred
- Comfortable with scientific/technical vocabulary
- Natural charisma in delivery

**Option B: ElevenLabs Voice Library**

Evaluate existing voices for:
- European accent options
- Intellectual/authoritative tone
- Emotional range capability
- Pronunciation clarity

**Candidates to evaluate:**
- Search for German/Austrian accent voices
- Test with sample scripts
- Evaluate across emotional range

### Synthesis Configuration

```json
{
  "model_id": "eleven_turbo_v2_5",
  "voice_settings": {
    "voice_id": "yudame_professor_voice",
    "stability": 0.70,
    "similarity_boost": 0.80,
    "style": 0.40,
    "use_speaker_boost": true,
    "output_format": "mp3_44100_192"
  },
  "pronunciation_dictionary": {
    "Yudame": "YOO-dah-may",
    "research_terms": {
      "meta-analysis": "MEH-ta ah-NAL-ih-sis",
      "epidemiology": "eh-pih-dee-mee-OL-oh-gee"
    }
  }
}
```

### Emotional Delivery Mapping

| Script Emotion | ElevenLabs Parameters |
|----------------|----------------------|
| Thoughtful baseline | stability: 0.75, style: 0.35 |
| Building excitement | stability: 0.65, style: 0.55 |
| Genuine revelation | stability: 0.60, style: 0.65 |
| Skeptical/critical | stability: 0.80, style: 0.30 |
| Amused/ironic | stability: 0.55, style: 0.50 |
| Passionate emphasis | stability: 0.50, style: 0.70 |

### Handling Special Moments

**Rare Expletives:**
- Generate separately with slightly lower stability
- Review for natural delivery
- Blend seamlessly

**Laughs/Reactions:**
- Use ElevenLabs' non-verbal sound capabilities
- Or record separately and blend
- Keep subtle and genuine

**Technical Terms:**
- Custom pronunciation dictionary
- Generate and verify
- Regenerate mispronunciations

---

## Component 4: Audio Production

### Single-Voice Processing Chain

**Stage 1: Raw Processing**
```
Synthesized Audio
    ↓
De-noise (if needed)
    ↓
De-ess (reduce sibilance)
    ↓
EQ (voice optimization)
    ↓
Compression (dynamic control)
    ↓
Processed Audio
```

### EQ Profile (Germanic Voice)

```
High-pass: 80 Hz (remove rumble)
Low-shelf: +1.5 dB at 180 Hz (chest resonance - common in Germanic voices)
Parametric: -2 dB at 350 Hz, Q=1.5 (reduce potential muddiness)
Parametric: +2 dB at 2.5 kHz, Q=2.5 (clarity for accented speech)
Parametric: +1 dB at 5 kHz, Q=2 (presence)
High-shelf: +0.5 dB at 12 kHz (air)
Low-pass: 16 kHz
```

### Compression Settings

```
Threshold: -20 dB
Ratio: 2.5:1
Attack: 15 ms (preserve transients for enunciation)
Release: 120 ms
Knee: Soft
Makeup gain: As needed
```

### Pause and Breath Engineering

**Natural Pauses:**
| Context | Duration |
|---------|----------|
| End of thought | 400-600ms |
| Before emphasis | 200-300ms |
| After revelation | 600-900ms |
| Section transition | 1000-1500ms |
| "Let me think..." moment | 500-800ms |

**Breath Sounds:**
- Insert subtle breaths before new thoughts
- Vary intensity with upcoming energy
- No breath in middle of phrases

### Music and Sound

**Intro (10-15 seconds):**
- Sophisticated, European sensibility
- Not corporate, not overly dramatic
- Fades under first words

**Outro (10-15 seconds):**
- Same theme
- Voice fades, music rises
- Clean ending

**No transition sounds between sections**
- Let the words do the work
- Silence and pacing create structure

---

## Component 5: Mastering & Delivery

### Mastering Chain

```
Processed Audio
    ↓
Subtle room ambiance (optional)
    ↓
Multi-band compression (gentle)
    ↓
Loudness normalization (-16 LUFS)
    ↓
True peak limiting (-1.5 dB)
    ↓
Format conversion
    ↓
Metadata + chapters
    ↓
Final Delivery
```

### Output Specifications

| Property | Value |
|----------|-------|
| Format | MP3 |
| Bitrate | 128 kbps (distribution), 320 kbps (archive) |
| Sample Rate | 44.1 kHz |
| Channels | Mono (single voice, saves bandwidth) |
| Loudness | -16 LUFS |
| True Peak | -1.5 dB max |

---

## Quality Assurance

### Automated Checks

- [ ] Duration within 5% of target
- [ ] Loudness: -17 to -15 LUFS
- [ ] No true peaks above -1.5 dB
- [ ] No audio dropouts
- [ ] Transcription matches script >98%
- [ ] All pronunciation dictionary terms correct

### Critic Agent Final Review

After synthesis, critic agent reviews:
- Does audio delivery match script intent?
- Are emphasis moments landing?
- Is pacing appropriate throughout?
- Any uncanny valley moments?

### Human QA Checklist

- [ ] Would I listen to this voluntarily?
- [ ] Does it sound like a person, not AI?
- [ ] Are the stories engaging?
- [ ] Do I remember the key points?
- [ ] Is the voice distinctive and appealing?
- [ ] Does it honor the Yudame brand values?

---

## Feasibility Assessment

### Why Single Host Is Easier

| Challenge | Two Hosts | Single Host |
|-----------|-----------|-------------|
| Natural dialogue | Very Hard | N/A |
| Turn-taking timing | Hard | N/A |
| Voice consistency | Hard (×2) | Medium (×1) |
| Emotional authenticity | Hard | Medium |
| Information density | Constrained by dialogue | Full control |

### Remaining Challenges

| Challenge | Difficulty | Mitigation |
|-----------|------------|------------|
| Monologue engagement | Medium | Strong structure (arc), story-driven |
| Voice acquisition | Medium | Professional actor or extensive search |
| Critic calibration | Medium | Training data from Huberman/Founders |
| Maintaining energy | Medium | Varied pacing, emotion mapping |

### Success Probability

With the simplifications made:
- **Script generation:** High confidence (monologue is tractable)
- **Critic refinement:** High confidence (clear rubric, training data)
- **Voice synthesis:** High confidence (single voice, good TTS)
- **Overall:** **High feasibility** for quality exceeding NotebookLM

---

## File Structure

```
podcast/tools/audio_generation/
├── orchestrator.py                 # Main pipeline
├── script/
│   ├── generator.py                # Opus script generation
│   ├── prompts/
│   │   └── generation_prompt.md    # Master prompt
│   └── schema.json                 # Script format
├── critic/
│   ├── agent.py                    # Critic refinement agent
│   ├── rubric.md                   # Evaluation criteria
│   └── training/
│       ├── huberman_examples/      # Annotated transcripts
│       └── founders_examples/      # Annotated transcripts
├── synthesis/
│   ├── elevenlabs_client.py        # TTS wrapper
│   ├── pronunciation.json          # Custom dictionary
│   └── emotion_mapping.json        # Delivery parameters
├── production/
│   ├── processor.py                # EQ, compression
│   ├── pauses.py                   # Pause engineering
│   └── presets/
│       └── yudame_voice_chain.json
├── mastering/
│   ├── loudness.py                 # LUFS normalization
│   ├── limiter.py                  # Peak limiting
│   └── metadata.py                 # ID3 embedding
├── qa/
│   ├── automated_checks.py
│   ├── critic_final_review.py
│   └── reports/
└── voice/
    ├── config.json                 # Voice settings
    └── samples/                    # Reference recordings
```

---

## Building the Judge with Limited Human Feedback

### The Core Problem

You can provide detailed feedback on 10-20 episodes, not 100s. How do we build a reliable critic from this?

### Strategy: Constitutional + Comparative + Active Learning

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    JUDGE TRAINING STRATEGY                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  LAYER 1: Constitutional Rubric (Zero human examples needed)            │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Explicit rules derived from style guide                          │   │
│  │ Checkable criteria that don't need subjective judgment           │   │
│  │ "Does it start with a question?" "Are researchers named?"        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                              │                                          │
│                              ▼                                          │
│  LAYER 2: NotebookLM Comparison (Unlimited "free" signal)               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Generate both versions from same report                          │   │
│  │ Structural diff: what did each include/exclude?                  │   │
│  │ Pacing comparison: word count per section                        │   │
│  │ "Would a human prefer ours or theirs?"                           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                              │                                          │
│                              ▼                                          │
│  LAYER 3: Few-Shot Human Examples (10-20 detailed reviews)              │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Your detailed feedback becomes few-shot examples                 │   │
│  │ Critic sees: script → your comments → final verdict              │   │
│  │ Learns YOUR taste, not generic "good podcast"                    │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                              │                                          │
│                              ▼                                          │
│  LAYER 4: Active Sampling (Maximize value of limited feedback)          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Identify uncertain cases (critic score 40-60)                    │   │
│  │ Surface those for human review                                   │   │
│  │ Continuously calibrate with minimal effort                       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Layer 1: Constitutional Rubric (Automated)

These checks need NO human examples—they're derived directly from the style guide:

**Structural Checks (Binary Pass/Fail):**
```
□ Opens with a question or problem (not "Today we'll discuss...")
□ Contains at least 2 specific stories (named people, dates, places)
□ Acknowledges at least 1 limitation or contradiction
□ Ends with clear takeaways
□ All statistics include context (not naked numbers)
□ Researchers are named, not "studies show"
□ Word count within 10% of target
□ No section exceeds 4 minutes without energy shift
```

**Voice Checks (Pattern Matching):**
```
□ Contains self-correction language ("Actually...", "Let me back up...")
□ Contains thinking-aloud markers ("Here's what's interesting...")
□ No forbidden phrases ("Today we're going to discuss", "This is SO fascinating")
□ Expletives, if present, are ≤3 and at high-intensity moments
□ Technical terms are immediately explained
```

**These catch 60-70% of issues without any human training.**

### Layer 2: NotebookLM Comparison (Free Signal)

Use NotebookLM as an unlimited comparison baseline:

**Process:**
```
Same Report.md
      │
      ├──────────────────┬──────────────────┐
      ▼                  ▼                  │
   Our Script      NotebookLM Audio         │
      │                  │                  │
      │                  ▼                  │
      │           Transcribe                │
      │                  │                  │
      ▼                  ▼                  │
   Compare Scripts ◄─────┘                  │
      │                                     │
      ▼                                     │
   Structural Analysis                      │
      │                                     │
      ▼                                     │
   Learning Signal                          │
```

**What to Compare:**

| Dimension | Our Script | NotebookLM | Learning |
|-----------|------------|------------|----------|
| Opening approach | Question? Hook? | How do they start? | Adopt better patterns |
| Information selection | What we included | What they included | Are we missing key points? |
| Story density | Count stories | Count stories | Calibrate expectations |
| Pacing | Words per section | Words per section | Match successful rhythms |
| Transitions | How we move between topics | How they transition | Steal good transitions |

**Automated Preference Signal:**

Without human labeling, we can still learn:
```python
# Pseudo-signal: Which script better matches Huberman/Founders patterns?
huberman_similarity_ours = compare_to_reference(our_script, huberman_corpus)
huberman_similarity_notebooklm = compare_to_reference(notebooklm_script, huberman_corpus)

# If NotebookLM is closer to our target style, we need to adjust
if huberman_similarity_notebooklm > huberman_similarity_ours:
    flag_for_review(our_script, "NotebookLM closer to target style")
```

### Layer 3: Few-Shot Human Examples (10-20 Reviews)

Your feedback on 10-20 episodes becomes the critic's training data.

**Feedback Collection Format:**

For each reviewed episode, capture:
```json
{
  "episode_id": "ep_001",
  "report_source": "report.md hash",
  "script_version": "draft_v2",

  "overall_verdict": "REVISE",
  "overall_score": 65,

  "section_feedback": [
    {
      "section": "hook",
      "verdict": "GOOD",
      "comment": "Strong opening question, immediately engaging"
    },
    {
      "section": "story_1",
      "verdict": "WEAK",
      "comment": "Too abstract—need specific names and dates",
      "example_fix": "Instead of 'researchers found', say 'In 2019, Maria Santos at Stanford...'"
    }
  ],

  "line_level_feedback": [
    {
      "line": 47,
      "issue": "Fake enthusiasm",
      "original": "This is really fascinating when you think about it",
      "suggested": "Cut entirely—let the content speak"
    }
  ],

  "what_worked": [
    "The transition from story 1 to story 2 felt natural",
    "Good use of 'What does this mean for you?' framing"
  ],

  "what_to_change": [
    "Need more specific numbers in the takeaway section",
    "The exception section felt rushed—expand by 30 seconds"
  ]
}
```

**How 10-20 Examples Become Powerful:**

The critic prompt includes:
```markdown
## Your Calibration Examples

Here are 15 scripts I've reviewed with detailed feedback.
Use these to understand MY standards:

### Example 1: Score 45 (REVISE)
[Script excerpt]
My feedback: "The hook was weak because..."
After revision: [Improved version]

### Example 2: Score 82 (PASS)
[Script excerpt]
My feedback: "This worked because..."

### Example 3: Score 58 (REVISE)
...

When you evaluate new scripts, ask yourself:
"Would the human who wrote this feedback approve?"
```

**Why Few-Shot Works Here:**

- Your feedback is *specific* and *actionable*
- You're not rating "good/bad" but explaining *why*
- The model learns your taste, not generic standards
- 15 detailed examples > 100 simple thumbs up/down

### Layer 4: Active Sampling (Maximize Limited Feedback)

Don't review random episodes—review the *uncertain* ones.

**Uncertainty Detection:**
```
Critic Score Distribution:

  ┌─────────────────────────────────┐
  │ 0-30:  Clear FAIL (don't review)│
  │ 30-45: Probably FAIL            │ ◄── Review some of these
  │ 45-55: UNCERTAIN                │ ◄── Review ALL of these
  │ 55-70: Probably PASS            │ ◄── Review some of these
  │ 70-100: Clear PASS (don't review)│
  └─────────────────────────────────┘
```

**Active Learning Loop:**
```
Generate 10 scripts
       │
       ▼
Critic scores all 10
       │
       ▼
Sort by uncertainty (closest to 50)
       │
       ▼
Human reviews top 3 uncertain
       │
       ▼
Add to few-shot examples
       │
       ▼
Critic recalibrates
       │
       ▼
Repeat
```

**Result:** Your ~20 reviews are spent on the *most informative* cases, not wasted on obvious passes/fails.

### Calibration Dashboard

Track critic accuracy over time:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CRITIC CALIBRATION                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Agreement with Human Reviews (last 20):                        │
│  ████████████████████░░░░  80% (16/20)                         │
│                                                                 │
│  False Positives (Critic PASS, Human REVISE): 2                 │
│  False Negatives (Critic REVISE, Human PASS): 2                 │
│                                                                 │
│  Score Correlation: 0.78                                        │
│                                                                 │
│  Drift Alert: None                                              │
│                                                                 │
│  Categories Needing Calibration:                                │
│  - "Voice authenticity" (3 disagreements)                       │
│  - "Story specificity" (1 disagreement)                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Implementation Roadmap

### Phase 0: Foundation (Before Any Code)

**0.1 Voice Acquisition**
- [ ] Research ElevenLabs voice library for German/Austrian accents
- [ ] Evaluate 5-10 candidate voices with test scripts
- [ ] If none suitable: Find voice actor (Fiverr, Voices.com, direct outreach)
- [ ] Commission 60-90 minute recording session
- [ ] Create ElevenLabs Professional Voice Clone
- [ ] Test clone across emotional range
- [ ] Build pronunciation dictionary for common research terms
- **Deliverable:** Working voice that passes "would I listen to this?" test

**0.2 Reference Corpus Collection**
- [ ] Select 10 best Huberman Lab episodes (varied topics)
- [ ] Select 10 best Founders Podcast episodes
- [ ] Transcribe all 20 episodes (Whisper or paid service)
- [ ] Annotate transcripts:
  - Mark hooks, transitions, stories, takeaways
  - Note pacing patterns
  - Extract signature phrases
  - Identify emotional beats
- **Deliverable:** Annotated corpus of 20 excellent episodes

**0.3 Style Guide Finalization**
- [ ] Expand Yudame voice document with examples
- [ ] Create "good example / bad example" pairs for each principle
- [ ] Define all forbidden phrases
- [ ] Document the arc structure with timestamps
- **Deliverable:** Comprehensive style guide (this document, expanded)

---

### Phase 1: Script Generation Pipeline

**1.1 Basic Generator**
- [ ] Create script generation prompt (from style guide)
- [ ] Define JSON schema for script output
- [ ] Build generator that takes report.md → script.json
- [ ] Test on 5 existing reports
- **Deliverable:** Generator that produces valid script JSON

**1.2 Constitutional Checker**
- [ ] Implement all binary structural checks
- [ ] Implement pattern-matching voice checks
- [ ] Create check report format
- [ ] Test on generated scripts
- **Deliverable:** Automated checker that catches obvious issues

**1.3 NotebookLM Comparison Pipeline**
- [ ] Build workflow: report → NotebookLM → transcribe → compare
- [ ] Implement structural diff (sections, word counts)
- [ ] Implement content comparison (what's included/excluded)
- [ ] Create comparison report format
- **Deliverable:** Side-by-side analysis of our scripts vs NotebookLM

**1.4 First Human Feedback Round**
- [ ] Generate scripts for 5 reports
- [ ] You provide detailed feedback (using feedback format)
- [ ] Identify patterns in feedback
- [ ] Adjust generation prompt based on patterns
- [ ] Regenerate and compare
- **Deliverable:** 5 annotated examples, improved generator

---

### Phase 2: Critic Agent Development

**2.1 Few-Shot Critic (v1)**
- [ ] Build critic prompt with rubric
- [ ] Include 5 human-reviewed examples as few-shot
- [ ] Test on held-out scripts
- [ ] Compare critic verdicts to your verdicts
- **Deliverable:** Critic that agrees with you >60% of time

**2.2 Expand Few-Shot Examples**
- [ ] Generate 10 more scripts
- [ ] Critic scores all 10
- [ ] You review the 5 most uncertain (scores 40-60)
- [ ] Add to few-shot examples (now 10 total)
- [ ] Retrain critic
- **Deliverable:** Critic with 10 examples, >70% agreement

**2.3 Refinement Loop Integration**
- [ ] Build generate → critique → revise → critique loop
- [ ] Set max iterations (3)
- [ ] Implement revision prompting (critic feedback → specific edits)
- [ ] Test full loop on 5 reports
- **Deliverable:** End-to-end script refinement pipeline

**2.4 Second Human Feedback Round**
- [ ] Run full pipeline on 10 new reports
- [ ] You review 5 uncertain final scripts
- [ ] Add to examples (now 15 total)
- [ ] Calibrate and measure agreement
- **Deliverable:** Critic with 15 examples, >75% agreement

---

### Phase 3: Voice Synthesis Pipeline

**3.1 Basic Synthesis**
- [ ] ElevenLabs API integration
- [ ] Parse script.json → synthesis calls
- [ ] Handle segment-by-segment synthesis
- [ ] Basic concatenation
- **Deliverable:** Raw audio from script

**3.2 Emotion Mapping**
- [ ] Map script emotions to ElevenLabs parameters
- [ ] Test across emotional range
- [ ] Tune stability/style per emotion type
- **Deliverable:** Emotionally varied synthesis

**3.3 Pronunciation Handling**
- [ ] Build pronunciation dictionary system
- [ ] Add verification step (transcribe and check)
- [ ] Implement regeneration for mispronunciations
- **Deliverable:** Accurate pronunciation of technical terms

**3.4 Special Moments**
- [ ] Handle expletives (if present)
- [ ] Handle laugh/reaction cues
- [ ] Test and tune
- **Deliverable:** Natural handling of special moments

---

### Phase 4: Audio Production Pipeline

**4.1 Basic Processing**
- [ ] Implement EQ chain for Germanic voice
- [ ] Implement compression
- [ ] Implement de-esser
- [ ] Test on synthesized audio
- **Deliverable:** Processed audio that sounds good

**4.2 Pause Engineering**
- [ ] Implement pause insertion based on script markers
- [ ] Add breath sounds at appropriate points
- [ ] Tune timing by context type
- **Deliverable:** Naturally paced audio

**4.3 Music Integration**
- [ ] Source/create intro music
- [ ] Implement intro fade
- [ ] Implement outro fade
- **Deliverable:** Complete episode with music

**4.4 Mastering**
- [ ] Implement loudness normalization (-16 LUFS)
- [ ] Implement true peak limiting
- [ ] Implement metadata embedding
- **Deliverable:** Broadcast-ready final audio

---

### Phase 5: Integration & Calibration

**5.1 End-to-End Pipeline**
- [ ] Connect all components
- [ ] Single command: report.md → final.mp3
- [ ] Error handling and logging
- **Deliverable:** Working pipeline

**5.2 Quality Calibration**
- [ ] Run on 10 reports
- [ ] You listen to all 10 final episodes
- [ ] Rate each, provide feedback
- [ ] Identify weak points in pipeline
- [ ] Iterate on weakest components
- **Deliverable:** Pipeline producing consistently good episodes

**5.3 A/B Testing vs NotebookLM**
- [ ] Generate both versions for 5 reports
- [ ] Blind listen test (you, or small group)
- [ ] Analyze preferences
- [ ] Target: preference for our version >60% of time
- **Deliverable:** Evidence we're competitive with NotebookLM

**5.4 Integration with Podcast Workflow**
- [ ] Connect to existing episode workflow
- [ ] Replace NotebookLM step
- [ ] Update documentation
- **Deliverable:** Fully integrated system

---

### Phase 6: Continuous Improvement

**6.1 Feedback Loop**
- [ ] After each published episode, rate it
- [ ] Periodically add to few-shot examples
- [ ] Track critic calibration over time
- [ ] Adjust rubric as taste evolves

**6.2 Voice Evolution**
- [ ] If needed, re-record voice samples
- [ ] Expand pronunciation dictionary
- [ ] Tune emotional parameters based on listening

**6.3 Style Evolution**
- [ ] Update style guide based on learnings
- [ ] Add new "good example / bad example" pairs
- [ ] Evolve the arc structure if needed

---

## Effort Estimation

| Phase | Human Effort | Calendar Time |
|-------|--------------|---------------|
| Phase 0: Foundation | 15-20 hours | 2-3 weeks |
| Phase 1: Script Generation | 5-8 hours | 1-2 weeks |
| Phase 2: Critic Development | 10-15 hours | 2-3 weeks |
| Phase 3: Voice Synthesis | 3-5 hours | 1 week |
| Phase 4: Audio Production | 3-5 hours | 1 week |
| Phase 5: Integration | 8-12 hours | 2 weeks |
| **Total** | **45-65 hours** | **10-12 weeks** |

Human effort is primarily:
- Voice selection/recording session
- Providing feedback on scripts
- Listening to outputs
- Calibration reviews

Most technical implementation can be done by Claude.

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Can't find good German/Austrian voice | Expand to other European accents; consider American with gravitas |
| Critic doesn't calibrate well | More human examples; simpler rubric; human-in-loop for first N episodes |
| Scripts feel robotic | More few-shot examples; emphasize story over information; human edit pass |
| NotebookLM is just better | Hybrid: use NotebookLM for first draft, our voice for synthesis |
| Pipeline too slow | Parallelize synthesis; cache intermediate steps; accept longer generation time |

---

## References

### Style Inspiration

- **Huberman Lab Podcast** — Scientific depth, mechanism clarity
- **Founders Podcast (David Senra)** — Obsessive reading, story-driven wisdom
- **Lex Fridman** — Thoughtful pacing, genuine curiosity
- **Tim Ferriss** — Question-driven structure

### Voice Inspiration

- Austrian/German TED speakers
- Popular European university lecturers
- Documentary narrators with European accents

### Technical

- ElevenLabs: https://elevenlabs.io/docs
- Loudness standards: ITU-R BS.1770-4
- Podcast specifications: Apple Podcasts requirements

### Machine Learning Approaches

- Constitutional AI (Anthropic) — Rule-based self-evaluation
- Few-shot learning — Learning from limited examples
- Active learning — Strategic selection of examples for labeling
- RLHF concepts — Learning from human preferences
