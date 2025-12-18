# Open NotebookLM: Self-Hosted Podcast Audio Generation

A plan for replacing Google NotebookLM with a quality-maximized, self-controlled system for generating conversational podcast audio from research reports.

## Vision

Create a production pipeline that transforms written research reports into broadcast-quality, two-host conversational podcast audio—exceeding NotebookLM's capabilities through superior voice synthesis, professional audio production, and full creative control.

---

## Current State (NotebookLM)

### What NotebookLM Does

1. Accepts document upload (report.md)
2. Generates conversational script with two AI hosts
3. Synthesizes natural-sounding speech
4. Produces ~30-40 minute audio file
5. Delivers as downloadable M4A

### NotebookLM Strengths

- Natural conversational flow
- Two distinct voice personalities
- Appropriate pacing and emphasis
- Handles complex topics accessibly
- Includes natural speech patterns (pauses, affirmations)

### NotebookLM Limitations

- Closed/proprietary system
- No control over voice selection
- No script editing before synthesis
- No customization of conversation style
- Dependency on Google's continued service
- No professional audio post-production
- Limited prosody control
- No emotional range tuning
- Fixed host personalities

---

## Proposed Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        OPEN NOTEBOOKLM PIPELINE                                  │
├───────────────┬───────────────┬───────────────┬───────────────┬─────────────────┤
│               │               │               │               │                 │
│    SCRIPT     │    VOICE      │   PROSODY     │    AUDIO      │   MASTERING     │
│  GENERATION   │  SYNTHESIS    │  ENHANCEMENT  │  PRODUCTION   │   & DELIVERY    │
│               │               │               │               │                 │
│ ┌───────────┐ │ ┌───────────┐ │ ┌───────────┐ │ ┌───────────┐ │ ┌─────────────┐ │
│ │  Claude   │ │ │ ElevenLabs│ │ │  Emotion  │ │ │  iZotope  │ │ │ Broadcast   │ │
│ │  Opus 4   │ │ │  Turbo v2 │ │ │  Injection│ │ │    RX     │ │ │ Limiter     │ │
│ │           │ │ │           │ │ │           │ │ │           │ │ │             │ │
│ └───────────┘ │ └───────────┘ │ └───────────┘ │ └───────────┘ │ └─────────────┘ │
│       │       │       │       │       │       │       │       │       │         │
│       ▼       │       ▼       │       ▼       │       ▼       │       ▼         │
│  script.json  │  raw_audio/   │  enhanced/    │  produced/    │   final.mp3     │
│               │               │               │               │                 │
└───────────────┴───────────────┴───────────────┴───────────────┴─────────────────┘
```

### Pipeline Components

| Component | Purpose | Quality Impact |
|-----------|---------|----------------|
| Script Generation | Natural dialogue creation | Foundation of engagement |
| Voice Synthesis | Human-quality speech | Core listening experience |
| Prosody Enhancement | Emotional authenticity | Listener connection |
| Audio Production | Professional polish | Broadcast readiness |
| Mastering & Delivery | Final optimization | Platform compatibility |

---

## Component 1: Script Generation

### Purpose

Transform a written research report into a compelling two-person podcast conversation that exceeds typical AI-generated dialogue.

### Model Selection

**Primary:** Claude Opus 4 (claude-opus-4-20250514)
- Highest quality reasoning and creativity
- Superior dialogue naturalness
- Best handling of complex source material

**Validation:** Claude Sonnet for structural review
- Check pacing and timing estimates
- Verify chapter alignment
- Confirm dialogue balance

### Host Personas (Enhanced)

**Host A: "The Synthesizer"**
- Primary narrator with authoritative presence
- Warm baritone characteristics in writing style
- Provides structure, context, and depth
- Uses metaphor and analogy naturally
- Comfortable with complexity, explains accessibly
- Occasional dry humor
- Voice direction: NPR host quality

**Host B: "The Explorer"**
- Intellectually curious co-host
- Represents informed listener perspective
- Asks the questions listeners are thinking
- Provides emotional reactions and enthusiasm
- Challenges assumptions constructively
- Creates moments of discovery
- Voice direction: Science podcast co-host

### Script Format (Enhanced)

```json
{
  "metadata": {
    "title": "Episode Title",
    "duration_target_seconds": 2400,
    "generated_at": "2025-12-18T10:00:00Z",
    "model": "claude-opus-4-20250514",
    "version": "2.0"
  },
  "voice_direction": {
    "host_a": {
      "base_tone": "warm_authoritative",
      "energy_baseline": 0.6,
      "formality": 0.7
    },
    "host_b": {
      "base_tone": "curious_engaged",
      "energy_baseline": 0.7,
      "formality": 0.5
    }
  },
  "segments": [
    {
      "id": 1,
      "chapter": "Introduction",
      "chapter_mood": "intriguing",
      "exchanges": [
        {
          "speaker": "A",
          "text": "Welcome back to Yudame Research...",
          "emotion": "warm_welcoming",
          "intensity": 0.6,
          "style": {
            "pace": "moderate",
            "emphasis_words": ["Yudame", "Research"],
            "pause_after_seconds": 0.5,
            "breath_before": true
          },
          "ssml_hints": {
            "prosody_rate": "medium",
            "prosody_pitch": "medium"
          }
        },
        {
          "speaker": "B",
          "text": "Today we're diving into something that genuinely surprised me when I first read the research...",
          "emotion": "genuine_excitement",
          "intensity": 0.75,
          "style": {
            "pace": "slightly_accelerating",
            "emphasis_words": ["genuinely", "surprised"],
            "lean_forward": true
          }
        }
      ]
    }
  ],
  "production_notes": {
    "ambient_suggestion": "quiet_studio",
    "music_cues": [
      {"time": "intro", "type": "fade_in"},
      {"time": "outro", "type": "fade_out"}
    ]
  }
}
```

### Conversation Architecture

**Opening (0:00-1:30)**
- Cold open with hook (surprising fact, provocative question)
- Brief greeting and topic introduction
- Promise of what listener will learn

**Development (1:30-25:00)**
- 3-4 major topic sections
- Each section: setup → exploration → insight → transition
- Natural tangents that circle back
- "Aha moment" design in each section

**Synthesis (25:00-28:00)**
- Connect themes across sections
- Unexpected connections
- "Bigger picture" framing

**Close (28:00-30:00)**
- Practical takeaways
- Lingering question for reflection
- Warm sign-off

### Dialogue Quality Markers

**Natural Speech Patterns:**
- Incomplete thoughts that get completed
- Self-corrections ("Well, actually...")
- Verbal affirmations ("Right", "Exactly", "Hm, interesting")
- Overlapping sentiment (not audio, but written momentum)
- Questions that build on previous answers

**Engagement Techniques:**
- The Setup/Payoff pattern
- Tension and release through questions
- Callback references to earlier points
- The "But wait, there's more" pivot
- Micro-cliffhangers before transitions

### Script Generation Prompt Framework

```markdown
# Podcast Script Generation - Maximum Quality

## Role
You are an award-winning podcast scriptwriter creating dialogue for a
research-focused show that combines the intellectual depth of Radiolab
with the accessibility of Planet Money.

## Hosts
- Host A ("Alex"): The Synthesizer - authoritative, warm, uses great metaphors
- Host B ("Jordan"): The Explorer - curious, energetic, asks great questions

## Source Material
[Report content]

## Requirements

### Structural
- Target: [X] minutes of audio (estimate 150 words/minute of dialogue)
- Create [N] natural chapter breaks
- Open with a hook, not a summary
- Build to insights, don't front-load conclusions

### Dialogue Quality
- Every exchange must feel like it could only exist in THIS conversation
- Include moments of genuine discovery
- Use specific examples over generalities
- Translate jargon instantly and naturally
- Statistics need context and human scale

### Emotional Arc
- Map the emotional journey of the episode
- Include moments of: curiosity, surprise, concern, hope, resolution
- Vary energy levels - not everything is exciting
- Create at least one "mind-blown" moment

### Technical
- Include SSML hints for emphasis and pacing
- Note emotional tone for each utterance
- Mark breath points and natural pauses
- Identify words requiring specific pronunciation

### Forbidden
- Robotic transitional phrases ("Moving on to...")
- Unearned excitement ("This is SO fascinating!")
- Reading statistics without human context
- Monologues over 45 seconds
- Questions with obvious answers
- Summarizing what was just said

## Output Format
[JSON schema as defined above]
```

---

## Component 2: Voice Synthesis

### Purpose

Convert script to speech that is indistinguishable from professional voice actors.

### Provider: ElevenLabs (Primary)

**Why ElevenLabs:**
- Industry-leading naturalness
- Best-in-class emotional range
- Professional Studio Voice options
- Fine-grained control over delivery
- Turbo v2.5 model for quality + speed

### Voice Selection Strategy

**Option A: Professional Voice Actors (Highest Quality)**

Commission custom voice models:
1. Hire two professional voice actors for 30-minute recording sessions
2. Record samples covering full emotional and tonal range
3. Create Professional Voice Clones via ElevenLabs
4. Result: Unique, owned voices with broadcast quality

**Recording Session Requirements:**
- Professional studio environment
- Range of emotions: neutral, excited, concerned, thoughtful, amused
- Various energy levels and pacing
- Technical pronunciation samples
- Conversational flow samples

**Option B: ElevenLabs Studio Voices**

Use pre-built professional voices:
- Extensive library of broadcast-quality voices
- Consistent and reliable
- No setup time
- Good emotional range

**Recommended Voices:**

| Host | Voice Characteristics | ElevenLabs Voice Type |
|------|----------------------|----------------------|
| A | Warm, authoritative, baritone | "Adam" or custom NPR-style |
| B | Energetic, curious, slightly higher | "Josh" or custom science-host |

### Synthesis Configuration

```json
{
  "model_id": "eleven_turbo_v2_5",
  "voice_settings": {
    "host_a": {
      "voice_id": "selected_or_cloned_voice_a",
      "stability": 0.71,
      "similarity_boost": 0.85,
      "style": 0.45,
      "use_speaker_boost": true,
      "output_format": "mp3_44100_192"
    },
    "host_b": {
      "voice_id": "selected_or_cloned_voice_b",
      "stability": 0.65,
      "similarity_boost": 0.82,
      "style": 0.55,
      "use_speaker_boost": true,
      "output_format": "mp3_44100_192"
    }
  },
  "pronunciation_dictionary": {
    "Yudame": "yoo-DAH-may",
    "research-specific-terms": "..."
  }
}
```

### Advanced Synthesis Features

**Emotion Injection:**
ElevenLabs supports emotional styling:
- Map script emotions to synthesis parameters
- Adjust style parameter per utterance
- Use stability variance for natural imperfection

**Pronunciation Control:**
- Custom pronunciation dictionary for technical terms
- SSML tags for emphasis and pacing
- Phonetic overrides for uncommon words

**Quality Settings:**
- Output: 44.1kHz, 192kbps minimum during synthesis
- Enable speaker boost for presence
- Use latest model version always

### Alternative: Parallel Synthesis for A/B Quality

Generate each segment with multiple parameter variations:
1. Synthesize each line 2-3 times with slight variations
2. Use AI or human selection to pick best take
3. Assemble final from best segments

---

## Component 3: Prosody Enhancement

### Purpose

Add micro-level authenticity that distinguishes broadcast audio from synthetic speech.

### Breath Insertion

**Natural Breathing:**
- Insert breath sounds at natural pause points
- Vary breath intensity based on upcoming phrase energy
- Use actual recorded breaths (from voice actor sessions or libraries)

**Breath Placement Rules:**
- Before sentences starting new thoughts
- After long phrases
- Before emphasized words
- At emotional transitions

### Micro-Pause Injection

**Timing Adjustments:**
| Context | Pause Duration |
|---------|----------------|
| Thinking pause ("Well...") | 300-500ms |
| Emphasis pause (before key word) | 150-250ms |
| Emotional beat (after revelation) | 400-700ms |
| Topic transition | 800-1200ms |
| Breath pause | 200-400ms |

### Filler Sound Library

**Optional Authenticity Markers:**
- Subtle "um" or "uh" (sparingly, 1-2 per segment)
- Soft laughs at appropriate moments
- Affirmative sounds ("Mm-hmm", "Hm")
- Intake breath sounds

**Implementation:**
- Build library of filler sounds from voice actors
- Script indicates insertion points
- Blend seamlessly with synthesized speech

### Room Tone Matching

**Acoustic Consistency:**
- Add subtle room ambiance to synthesized audio
- Match reverb characteristics between hosts
- Create sense of shared space

---

## Component 4: Audio Production

### Purpose

Transform raw synthesized segments into broadcast-quality mixed audio.

### Professional Audio Processing Chain

**Stage 1: Individual Segment Processing**

```
Raw Segment
    ↓
De-noise (if needed)
    ↓
De-ess (reduce sibilance)
    ↓
EQ (voice clarity)
    ↓
Compression (dynamic control)
    ↓
Processed Segment
```

**Stage 2: Assembly and Mixing**

```
All Processed Segments
    ↓
Sequencing with timing
    ↓
Crossfade transitions
    ↓
Stereo positioning
    ↓
Room ambiance layer
    ↓
Music bed (if applicable)
    ↓
Mixed Audio
```

### EQ Settings (Voice Optimization)

**Host A (Deeper voice):**
```
High-pass: 80 Hz (remove rumble)
Low-shelf: +1 dB at 200 Hz (warmth)
Parametric: -2 dB at 400 Hz, Q=1.5 (reduce mud)
Parametric: +2 dB at 3 kHz, Q=2 (presence)
High-shelf: +1 dB at 10 kHz (air)
Low-pass: 16 kHz
```

**Host B (Higher energy voice):**
```
High-pass: 100 Hz
Parametric: -1 dB at 300 Hz, Q=1.5
Parametric: +2.5 dB at 4 kHz, Q=2 (clarity)
High-shelf: +1.5 dB at 12 kHz (brightness)
De-esser: 5-7 kHz range
Low-pass: 16 kHz
```

### Compression Settings

**Voice Compression:**
```
Threshold: -18 dB
Ratio: 3:1
Attack: 10 ms
Release: 100 ms
Knee: Soft
Makeup gain: As needed
```

**Purpose:** Even out dynamics without killing life

### Stereo Field Design

**Spatial Positioning:**
- Host A: Slight left (10-15% pan)
- Host B: Slight right (10-15% pan)
- Ambiance: Stereo wide
- Music: True stereo

**Creates:** Sense of two people in conversation, not alternating monologues

### Transition Design

**Speaker Transitions:**
- 50-100ms micro-overlap for natural conversation feel
- Or 200-300ms gap for considered responses
- Crossfade: 30-50ms for seamlessness

**Chapter Transitions:**
- 1-2 second pause
- Optional subtle music swell
- Room tone fill (not silence)

### Music and Sound Design

**Intro/Outro Music:**
- Custom composed or licensed broadcast-quality
- 10-15 seconds intro, fade under dialogue
- Outro: dialogue fade into music, 10-15 second tail

**Transition Sounds (Optional):**
- Subtle, branded audio signatures
- Between major sections only
- Never interrupt flow

**Ambient Bed:**
- Extremely subtle studio ambiance
- Creates presence without distraction
- -30 to -40 dB relative to voice

---

## Component 5: Mastering & Delivery

### Purpose

Final optimization for podcast distribution standards and maximum listening quality.

### Mastering Chain

```
Mixed Audio
    ↓
Multi-band compression (gentle)
    ↓
Stereo enhancement (subtle)
    ↓
Loudness normalization (-16 LUFS)
    ↓
True peak limiting (-1.5 dB)
    ↓
Format conversion
    ↓
Metadata embedding
    ↓
Final Delivery
```

### Loudness Standards

**Target:** -16 LUFS (podcast standard)

**Parameters:**
- Integrated loudness: -16 LUFS
- True peak: -1.5 dB maximum
- Loudness range: 8-12 LU

### Output Formats

**Primary Delivery:**
- MP3 320kbps for archival
- MP3 128kbps for distribution
- Both at 44.1 kHz stereo

**Quality Archive:**
- FLAC or WAV at 48kHz/24-bit
- Preserve for future remastering

### Metadata Embedding

**ID3 Tags:**
- Title, Artist, Album, Year
- Episode number
- Genre: Podcast
- Cover art (high resolution)
- Chapter markers (if supported)

---

## Advanced Quality Enhancements

### Multi-Take Selection

**Process:**
1. Generate each script line 3 times with parameter variations
2. Score each take for:
   - Naturalness
   - Emotional accuracy
   - Pronunciation clarity
   - Pacing appropriateness
3. Select best take per line
4. Assemble optimal version

**Automation:**
- Use Claude to evaluate take quality from spectrograms + transcriptions
- Or human review for critical segments

### Adaptive Pacing

**Dynamic Timing:**
- Analyze content complexity per segment
- Slow pacing for complex ideas
- Faster pacing for familiar concepts
- Automatic adjustment of pause lengths

### Emotional Continuity

**Cross-Segment Consistency:**
- Track emotional state across segment boundaries
- Ensure smooth emotional transitions
- No jarring tone shifts

### Pronunciation Verification

**Quality Control:**
- Transcribe all synthesized audio
- Compare against script
- Flag and regenerate mispronunciations
- Special attention to proper nouns, technical terms

---

## Quality Assurance Framework

### Automated QA Checks

**Technical:**
- [ ] Loudness within -17 to -15 LUFS
- [ ] No true peaks above -1.5 dB
- [ ] No audio dropouts or glitches
- [ ] Correct total duration (±5% of target)
- [ ] All chapters present

**Content:**
- [ ] Transcription matches script (>98%)
- [ ] No mispronounced key terms
- [ ] Voice consistency throughout
- [ ] Appropriate pacing (WPM in range)

### Human QA Checklist

**Listening Review:**
- [ ] Natural conversation flow
- [ ] Engaging opening hook
- [ ] Clear explanation of complex topics
- [ ] Appropriate emotional moments
- [ ] Satisfying conclusion
- [ ] No uncanny valley moments
- [ ] Would listen to full episode voluntarily

**A/B Comparison:**
- [ ] Compare against NotebookLM baseline
- [ ] Compare against professional podcasts
- [ ] Note areas for improvement

### Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Naturalness score | >4.5/5 | Listener panel |
| Engagement (completion rate) | >80% | Analytics |
| Transcription accuracy | >99% | Automated |
| Technical compliance | 100% | Automated |
| MOS (Mean Opinion Score) | >4.0 | Standard testing |

---

## Technical Architecture

### System Requirements

**Compute:**
- High-memory instance for audio processing
- GPU optional (speeds up some processing)
- Fast storage for audio files

**Software Stack:**
- Python 3.12+
- FFmpeg 8.0+ with full codec support
- iZotope RX (or equivalent) for pro audio processing
- ElevenLabs API access
- Claude API access (Opus tier)

### File Structure

```
podcast/tools/audio_generation/
├── orchestrator.py              # Main pipeline controller
├── script/
│   ├── generator.py             # Claude script generation
│   ├── validator.py             # Script quality checks
│   └── templates/
│       └── generation_prompt.md
├── synthesis/
│   ├── elevenlabs_client.py     # TTS API wrapper
│   ├── multi_take.py            # Multiple take generation
│   ├── take_selector.py         # Best take selection
│   └── pronunciation.json       # Custom dictionary
├── prosody/
│   ├── breath_inserter.py       # Natural breathing
│   ├── pause_adjuster.py        # Micro-timing
│   └── assets/
│       ├── breaths/             # Breath samples
│       └── fillers/             # Filler sounds
├── production/
│   ├── mixer.py                 # Audio assembly
│   ├── processor.py             # EQ, compression
│   ├── spatial.py               # Stereo positioning
│   └── presets/
│       ├── host_a_chain.json
│       └── host_b_chain.json
├── mastering/
│   ├── loudness.py              # LUFS normalization
│   ├── limiter.py               # True peak limiting
│   └── metadata.py              # ID3 embedding
├── qa/
│   ├── automated_checks.py      # Technical QA
│   ├── transcription_verify.py  # Accuracy check
│   └── reports/                 # QA reports
└── voices/
    ├── host_a/
    │   ├── config.json
    │   └── samples/             # Reference audio
    └── host_b/
        ├── config.json
        └── samples/
```

### API Dependencies

| Service | Purpose | Tier Needed |
|---------|---------|-------------|
| ElevenLabs | Voice synthesis | Creator+ (for quality) |
| Anthropic | Script generation | Standard (Opus access) |

---

## Feasibility Assessment

### Proven Components

| Component | Feasibility | Evidence |
|-----------|-------------|----------|
| Script generation | High | Claude produces excellent dialogue |
| Voice synthesis | High | ElevenLabs Studio voices are broadcast-ready |
| Audio production | High | Standard audio engineering, well-understood |
| Pipeline automation | High | All components have APIs |

### Technical Challenges

| Challenge | Difficulty | Mitigation |
|-----------|------------|------------|
| Emotional consistency across segments | Medium | Careful parameter tuning, multi-take selection |
| Natural conversation timing | Medium | Extensive pause/breath engineering |
| Pronunciation of novel terms | Low | Custom pronunciation dictionary |
| Long-form coherence | Medium | Segment-aware synthesis, state tracking |

### Quality Delta vs NotebookLM

**Expected Improvements:**
- Voice quality: Significantly better (professional vs consumer TTS)
- Emotional range: Better (explicit emotion control)
- Production quality: Much better (professional mastering)
- Customization: Complete control vs none

**Potential Parity Areas:**
- Conversational naturalness (both strong)
- Pacing (both can be tuned)

**Risk Areas:**
- Integration complexity (more components)
- Edge case handling (less battle-tested)

---

## Success Criteria

### Minimum Viable Quality

Audio that listeners cannot distinguish from human-hosted podcasts in blind testing.

### Target Quality

Audio that exceeds typical human-hosted podcasts in:
- Consistency of delivery
- Technical audio quality
- Pacing optimization
- Information density

### Stretch Quality

Audio recognized as "unusually good" by podcast industry professionals.

---

## Future Quality Enhancements

### Voice Improvements

- Custom fine-tuned voice models trained on hundreds of hours
- Real-time voice adjustment during synthesis
- Dialect and accent options
- Age and energy variation for different content types

### Production Improvements

- AI-driven mixing decisions
- Automatic music scoring based on content mood
- Spatial audio (Dolby Atmos) for immersive listening
- Adaptive loudness for different playback environments

### Content Improvements

- Multiple episode styles (interview, narrative, debate)
- Guest voice synthesis
- Multi-language versions from single script
- Interactive/branching podcast formats

---

## References

### Voice Synthesis

- ElevenLabs Documentation: https://elevenlabs.io/docs
- Voice cloning best practices: ElevenLabs professional tier resources
- SSML specification: W3C Speech Synthesis Markup Language

### Audio Production

- Podcast audio standards: Apple Podcasts requirements
- Loudness standards: ITU-R BS.1770-4
- Professional mastering: iZotope RX documentation

### Conversation Design

- Radiolab production methodology
- This American Life storytelling structure
- NPR training materials on conversational audio
