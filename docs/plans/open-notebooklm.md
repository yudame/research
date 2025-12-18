# Open NotebookLM: Self-Hosted Podcast Audio Generation

A plan for replacing Google NotebookLM with an open, self-hosted system for generating conversational podcast audio from research reports.

## Vision

Create a fully open-source pipeline that transforms written research reports into engaging, two-host conversational podcast audio—replicating and extending NotebookLM's "Audio Overview" functionality without dependency on Google's proprietary system.

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
- Rate limits and availability constraints

---

## Proposed Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     OPEN NOTEBOOKLM PIPELINE                        │
├─────────────────┬─────────────────┬─────────────────┬───────────────┤
│                 │                 │                 │               │
│     SCRIPT      │     VOICE       │     AUDIO       │    OUTPUT     │
│   GENERATION    │   SYNTHESIS     │   PRODUCTION    │   DELIVERY    │
│                 │                 │                 │               │
│  ┌───────────┐  │  ┌───────────┐  │  ┌───────────┐  │ ┌───────────┐ │
│  │  Claude   │  │  │  TTS API  │  │  │  FFmpeg   │  │ │  Final    │ │
│  │  Script   │  │  │  (Multi)  │  │  │  Mixing   │  │ │  MP3      │ │
│  │  Writer   │  │  │           │  │  │           │  │ │           │ │
│  └───────────┘  │  └───────────┘  │  └───────────┘  │ └───────────┘ │
│        │        │        │        │        │        │       │       │
│        ▼        │        ▼        │        ▼        │       ▼       │
│   script.json   │   segments/*.mp3│   mixed.mp3     │   final.mp3   │
│                 │                 │                 │               │
└─────────────────┴─────────────────┴─────────────────┴───────────────┘
```

### Pipeline Phases

| Phase | Input | Output | Duration |
|-------|-------|--------|----------|
| 1. Script Generation | report.md | script.json | 2-5 min |
| 2. Voice Synthesis | script.json | segments/*.mp3 | 10-30 min |
| 3. Audio Production | segments/*.mp3 | mixed.mp3 | 2-5 min |
| 4. Output Delivery | mixed.mp3 | final.mp3 | 1 min |

---

## Component 1: Script Generation

### Purpose

Transform a written research report into a natural two-person podcast conversation script.

### Approach

Use Claude to generate a structured conversation script with:
- Two distinct host personas
- Natural dialogue flow
- Topic segmentation matching chapters
- Speech patterns (pauses, emphasis, reactions)
- Appropriate pacing for audio consumption

### Host Personas

**Host A: "The Explainer"**
- Primary narrator
- Presents main concepts
- Provides structure and transitions
- Warmer, more accessible tone

**Host B: "The Curious One"**
- Asks clarifying questions
- Expresses reactions ("That's fascinating...")
- Challenges assumptions
- Represents the listener's perspective

### Script Format

```json
{
  "metadata": {
    "title": "Episode Title",
    "duration_target": 2400,
    "generated_at": "2025-12-18T10:00:00Z"
  },
  "segments": [
    {
      "id": 1,
      "chapter": "Introduction",
      "exchanges": [
        {
          "speaker": "A",
          "text": "Welcome back to Yudame Research...",
          "style": {
            "pace": "moderate",
            "emphasis": ["Yudame", "Research"],
            "pause_after": 0.5
          }
        },
        {
          "speaker": "B",
          "text": "Today we're diving into something really interesting...",
          "style": {
            "pace": "slightly_fast",
            "tone": "enthusiastic"
          }
        }
      ]
    }
  ]
}
```

### Script Generation Prompt Structure

```markdown
# Podcast Script Generation

## Input
- Research report content
- Target duration (minutes)
- Episode metadata

## Output Requirements
- Conversational dialogue between two hosts
- Natural speech patterns
- Chapter-aligned segments
- Style annotations for synthesis

## Conversation Guidelines
- Open with hook, not summary
- Use questions to drive exploration
- Include moments of discovery
- Acknowledge complexity without jargon
- End segments with transitions
- Include natural affirmations ("Right", "Exactly", "Interesting")

## Forbidden
- Reading statistics without context
- Long monologues (max 30 seconds per turn)
- Academic language without translation
- Unnatural transitions
```

### Estimated Output

- 30-40 minute episode = ~6,000-8,000 words of dialogue
- ~100-150 speaker exchanges
- 10-15 chapter segments

---

## Component 2: Voice Synthesis

### Purpose

Convert script text into natural-sounding speech audio for each host.

### TTS Provider Options

| Provider | Quality | Cost | Latency | Self-Hosted |
|----------|---------|------|---------|-------------|
| ElevenLabs | Excellent | $$$ | Fast | No |
| OpenAI TTS | Very Good | $$ | Fast | No |
| Azure Neural | Very Good | $$ | Fast | No |
| Google Cloud | Very Good | $$ | Fast | No |
| Coqui XTTS | Good | Free | Slow | Yes |
| Bark | Good | Free | Slow | Yes |
| StyleTTS2 | Very Good | Free | Moderate | Yes |
| VALL-E X | Excellent | Free | Slow | Yes |

### Recommended Approach: Hybrid

**Primary:** ElevenLabs or OpenAI TTS (quality + speed)
**Fallback:** Coqui XTTS or StyleTTS2 (self-hosted, free)

### Voice Selection

**Host A Voice Requirements:**
- Warm, authoritative
- Clear enunciation
- Moderate pace
- Slight lower register

**Host B Voice Requirements:**
- Energetic, curious
- Expressive range
- Slightly faster pace
- Slight higher register

### Synthesis Parameters

```json
{
  "host_a": {
    "voice_id": "selected_voice_a",
    "stability": 0.75,
    "similarity_boost": 0.80,
    "style": 0.35,
    "speaking_rate": 1.0
  },
  "host_b": {
    "voice_id": "selected_voice_b",
    "stability": 0.65,
    "similarity_boost": 0.85,
    "style": 0.50,
    "speaking_rate": 1.05
  }
}
```

### Synthesis Workflow

1. Parse script.json into individual utterances
2. Group by speaker to minimize voice switching overhead
3. Synthesize each utterance with appropriate voice
4. Save as numbered segment files
5. Generate timing metadata for mixing

### Output Structure

```
segments/
├── 001_A_intro.mp3
├── 002_B_response.mp3
├── 003_A_explanation.mp3
├── ...
└── segments.json  # Timing and ordering metadata
```

### Cost Estimation

| Provider | Cost per 1M chars | 30-min episode | Monthly (4 eps) |
|----------|-------------------|----------------|-----------------|
| ElevenLabs | $11-24 | $0.80-1.70 | $3.20-6.80 |
| OpenAI TTS | $15 | $1.05 | $4.20 |
| Azure | $16 | $1.12 | $4.48 |
| Self-hosted | $0 | $0 | $0 |

---

## Component 3: Audio Production

### Purpose

Combine synthesized segments into polished podcast audio.

### Production Steps

1. **Concatenation** - Join segments in order
2. **Crossfade** - Smooth transitions between speakers
3. **Normalization** - Consistent volume levels
4. **Compression** - Dynamic range control
5. **EQ** - Frequency balance for voice clarity
6. **Silence Trimming** - Remove excessive pauses
7. **Music/SFX** - Optional intro/outro, transitions

### FFmpeg Processing Pipeline

**Step 1: Normalize each segment**
```
ffmpeg -i segment.mp3 -af loudnorm=I=-16:TP=-1.5:LRA=11 normalized.mp3
```

**Step 2: Concatenate with crossfade**
```
ffmpeg -i "concat:seg1.mp3|seg2.mp3" -af acrossfade=d=0.3 output.mp3
```

**Step 3: Apply podcast mastering**
```
ffmpeg -i input.mp3 -af "
  highpass=f=80,
  lowpass=f=12000,
  compand=attacks=0.1:decays=0.3:points=-80/-80|-45/-45|-27/-25|0/-10,
  loudnorm=I=-16:TP=-1.5:LRA=11
" mastered.mp3
```

### Timing Adjustments

| Transition Type | Pause Duration |
|-----------------|----------------|
| Same speaker, same thought | 0.2s |
| Same speaker, new thought | 0.5s |
| Speaker change, response | 0.3s |
| Speaker change, new topic | 0.8s |
| Chapter transition | 1.5s |

### Optional Enhancements

**Intro/Outro Music:**
- 5-10 second branded intro
- Fade under first dialogue
- Outro with fade from final dialogue

**Transition Sounds:**
- Subtle swoosh between chapters
- Optional background ambiance (very subtle)

**Sound Design:**
- Room tone/presence for naturalness
- Subtle stereo positioning (Host A slightly left, B slightly right)

---

## Component 4: Output Delivery

### Purpose

Finalize audio and prepare for podcast workflow integration.

### Output Specifications

| Property | Value |
|----------|-------|
| Format | MP3 |
| Bitrate | 128 kbps |
| Sample Rate | 44.1 kHz |
| Channels | Stereo |
| Loudness | -16 LUFS |

### Integration Points

Generated audio integrates with existing workflow:

1. Output saved to episode directory
2. Filename follows convention: `YYYY-MM-DD-slug.mp3`
3. Triggers existing audio processing pipeline:
   - Transcription (Whisper)
   - Chapter generation
   - Chapter embedding
4. Continues to publishing phase

### Metadata Embedding

Before delivery, embed:
- Title
- Artist
- Album (podcast name)
- Year
- Genre (Podcast)
- Cover art (from cover.png)

---

## Self-Hosted TTS Deep Dive

### Option A: Coqui XTTS v2

**Strengths:**
- Excellent voice cloning
- Multi-language support
- Active open-source community
- Runs on consumer GPU

**Requirements:**
- 8GB+ VRAM GPU
- Python 3.10+
- ~4GB model download

**Performance:**
- ~0.5x real-time on RTX 3080
- 30-min episode = ~60 min generation

**Voice Cloning:**
- Provide 6-30 seconds of reference audio
- Creates custom voice matching reference

### Option B: StyleTTS2

**Strengths:**
- State-of-the-art naturalness
- Fast inference
- Good prosody control

**Requirements:**
- 6GB+ VRAM GPU
- Python 3.9+

**Performance:**
- ~1-2x real-time on RTX 3080
- 30-min episode = 15-30 min generation

### Option C: Bark (Suno)

**Strengths:**
- Includes non-speech sounds (laughs, sighs)
- Very natural prosody
- No voice cloning needed (built-in voices)

**Requirements:**
- 12GB+ VRAM GPU
- Python 3.8+

**Limitations:**
- Slower generation
- Less consistent long-form

### Option D: VALL-E X / VoiceCraft

**Strengths:**
- State-of-the-art quality
- Excellent voice cloning
- Natural conversation

**Requirements:**
- 16GB+ VRAM GPU
- Complex setup

**Status:**
- Research models, less production-ready

### Recommendation

**For quality priority:** ElevenLabs API (cost: ~$5-10/month for 4 episodes)

**For self-hosted priority:** Coqui XTTS v2 with cloned voices
- Clone two distinct voices from royalty-free samples
- Invest in one-time GPU compute for generation
- Zero ongoing costs

---

## Script Generation Deep Dive

### Conversation Dynamics

**Natural Dialogue Patterns:**

```
A: [States concept]
B: [Asks clarifying question or reacts]
A: [Elaborates with example]
B: [Connects to broader context]
A: [Summarizes and transitions]
```

**Engagement Techniques:**

1. **The Hook** - Open with intriguing question or surprising fact
2. **The Callback** - Reference earlier points
3. **The Analogy** - Complex concepts via familiar comparisons
4. **The Pivot** - "But here's where it gets interesting..."
5. **The Cliffhanger** - Tease upcoming sections

### Handling Source Material

**From Report to Conversation:**

| Report Element | Conversation Approach |
|----------------|----------------------|
| Statistics | Contextualize, round numbers |
| Citations | "Researchers at Stanford found..." |
| Technical terms | Define naturally in dialogue |
| Lists | Break into conversational points |
| Contradictions | Frame as "debate" or "tension" |
| Conclusions | Build toward, don't state upfront |

### Pacing Structure

**30-Minute Episode:**

| Section | Duration | Purpose |
|---------|----------|---------|
| Cold open | 0:30 | Hook with intriguing element |
| Intro | 1:00 | Topic overview |
| Context | 3:00 | Background and framing |
| Core 1 | 6:00 | First major section |
| Core 2 | 6:00 | Second major section |
| Core 3 | 6:00 | Third major section |
| Synthesis | 4:00 | Connecting themes |
| Takeaways | 2:30 | Practical implications |
| Outro | 1:00 | Close and preview |

---

## Quality Assurance

### Script QA Checklist

- [ ] Natural dialogue flow (not robotic)
- [ ] Both hosts have substantive contributions
- [ ] No monologues over 30 seconds
- [ ] Technical terms explained
- [ ] Statistics contextualized
- [ ] Transitions between topics
- [ ] Chapter alignment
- [ ] Target duration within 10%

### Audio QA Checklist

- [ ] Voice consistency throughout
- [ ] No audio artifacts or glitches
- [ ] Appropriate pacing (not rushed)
- [ ] Clean transitions between speakers
- [ ] Volume normalized (-16 LUFS)
- [ ] No excessive silence
- [ ] Total duration matches target

### Comparison Testing

Periodically compare with NotebookLM output:
- Naturalness of conversation
- Listener engagement
- Information retention
- Production quality

---

## Implementation Phases

### Phase 1: Script Generation (Week 1-2)

- Define host personas
- Create script generation prompt
- Build script JSON schema
- Develop Claude integration
- Test with sample reports
- Iterate on conversation quality

### Phase 2: Voice Synthesis (Week 2-4)

- Evaluate TTS providers
- Select primary and fallback options
- Clone/select voices for hosts
- Build synthesis pipeline
- Handle long-form generation
- Implement segment management

### Phase 3: Audio Production (Week 4-5)

- Build FFmpeg processing pipeline
- Implement crossfade logic
- Add normalization and mastering
- Create timing adjustment system
- Add optional music/transitions
- Test end-to-end quality

### Phase 4: Integration (Week 5-6)

- Connect to existing podcast workflow
- Replace NotebookLM step
- Update episode workflow docs
- Create operator documentation
- Performance optimization
- Error handling and recovery

---

## Cost Analysis

### Cloud TTS Approach

| Component | Monthly Cost (4 eps) |
|-----------|---------------------|
| ElevenLabs TTS | $5-10 |
| Claude API (scripts) | $2-5 |
| **Total** | **$7-15/month** |

### Self-Hosted Approach

| Component | One-Time Cost | Monthly |
|-----------|---------------|---------|
| GPU compute (cloud) | - | $20-50 |
| OR GPU hardware | $500-1500 | $0 |
| Claude API (scripts) | - | $2-5 |
| **Total (cloud GPU)** | - | **$22-55** |
| **Total (own GPU)** | $500-1500 | **$2-5** |

### Break-Even Analysis

Own GPU vs cloud TTS:
- Cloud TTS: ~$10/month
- Own GPU: ~$800 one-time
- Break-even: ~80 months (6.5 years)

Recommendation: **Start with cloud TTS, migrate to self-hosted if volume increases**

---

## Technical Requirements

### Minimum System (Cloud TTS)

- Python 3.12+
- FFmpeg 8.0+
- Claude API access
- TTS provider API key
- 4GB RAM

### Self-Hosted TTS

- Python 3.10+
- FFmpeg 8.0+
- NVIDIA GPU 8GB+ VRAM
- CUDA 11.8+
- 32GB RAM
- 50GB disk (models)

---

## File Structure

```
podcast/tools/
├── generate_podcast_audio.py      # Main orchestrator
├── script_generator.py            # Report → script.json
├── voice_synthesizer.py           # script.json → segments/
├── audio_producer.py              # segments/ → final.mp3
├── voices/                        # Voice configurations
│   ├── host_a.json
│   └── host_b.json
└── templates/
    └── script_prompt.md           # Script generation prompt
```

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| TTS quality insufficient | High | Test multiple providers, hybrid approach |
| Script lacks natural flow | High | Iterate prompts, human review option |
| Long generation times | Medium | Parallel processing, caching |
| Voice consistency issues | Medium | Strict synthesis parameters |
| API cost overruns | Low | Usage monitoring, fallback to self-hosted |
| Provider API changes | Medium | Abstract provider interface |

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Generation time | <45 min total | Automated timing |
| Audio quality | Match NotebookLM | Listener survey |
| Naturalness | >4/5 rating | Listener survey |
| Cost per episode | <$5 | Usage tracking |
| Reliability | 99% success | Error monitoring |

---

## Future Enhancements

### Version 2.0

- Interactive editing of generated scripts
- Multiple voice options per host
- Style transfer (formal, casual, technical)
- Multi-language support
- Real-time preview during script editing

### Version 3.0

- Custom voice cloning from user samples
- Dynamic pacing based on content complexity
- Automated music selection
- A/B testing of conversation styles
- Listener feedback integration

---

## References

### TTS Technologies

- ElevenLabs: https://elevenlabs.io/
- OpenAI TTS: https://platform.openai.com/docs/guides/text-to-speech
- Coqui TTS: https://github.com/coqui-ai/TTS
- Bark: https://github.com/suno-ai/bark
- StyleTTS2: https://github.com/yl4579/StyleTTS2

### Audio Processing

- FFmpeg: https://ffmpeg.org/
- Podcast audio standards: https://podcasters.apple.com/support/893

### Podcast Conversation Design

- NPR podcast guidelines (internal reference)
- Radiolab production techniques
- Conversational AI research papers
