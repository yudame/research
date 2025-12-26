# Podcast Audio Generation

Generate podcast audio from script.md using Gemini TTS API.

## When to Use This Skill

Use this skill when:
- User has a completed `script.md` in an episode directory
- User wants to generate audio from a TTS-ready script
- User explicitly requests audio generation

## Prerequisites

Before using this skill, verify:

1. **script.md exists** in the episode directory
   - Contains ~5,200 words (for ~35 min episode)
   - Includes TTS directives (`[VOICE: ...]`, `[PAUSE: ...]`, etc.)
   - Structured with Opening, Sections 1-3, and Closing

2. **Environment configured**
   - `GOOGLE_API_KEY` set in `/Users/valorengels/.env` (auto-loaded via ~/.zshenv)
   - Python 3.12+ available
   - ffmpeg installed (`brew install ffmpeg`)

3. **Dependencies installed**
   ```bash
   cd ~/src/research/podcast/tools
   pip install google-genai pydub
   ```

## Usage

### Via Command Line

```bash
cd ~/src/research/podcast/tools
python generate_audio_tts.py ../episodes/YYYY-MM-DD-slug/
```

### What Happens

1. **Load script.md** (~5,200 words, ~7k tokens)
2. **Generate audio** - Single Gemini TTS API call
3. **Convert to MP3** - 128kbps, tagged with metadata
4. **Create transcript** - Strip directives from script.md

## Output Files

After successful generation:

```
episode-directory/
├── script.md                     # Input (unchanged)
├── <episode-slug>.mp3            # Final audio (~30MB for 35 min)
└── <episode-slug>_transcript.txt # Plain text (directives stripped)
```

## TTS Directive Syntax

The script.md should contain embedded directives that guide vocal delivery:

```markdown
[VOICE: warm, authoritative]
[PACE: measured]

Welcome to Yudame Research.

[PAUSE: 0.8s]

Today, we're examining something that challenges everything you thought
you knew about cardiovascular health.

[VOICE: curious, leaning in]
Here's where it gets interesting...

[EMPHASIS: strong]
The effect size was 0.8—that's substantial.
```

### Directive Categories

| Directive | Options |
|-----------|---------|
| `[VOICE: ...]` | warm, authoritative, curious, skeptical, emphatic, reflective, matter-of-fact, precise |
| `[PACE: ...]` | measured, slightly faster, slower, building energy, deliberate |
| `[PAUSE: ...]` | 0.3s, 0.5s, 0.8s, 1.2s, 2.0s |
| `[EMPHASIS: ...]` | strong, subtle |

## Voice Identity

The audio uses the Yudame Research voice identity:

- **Model**: `gemini-2.5-flash-preview-tts`
- **Voice**: Alnilam
- **Output**: PCM 16-bit @ 24kHz → MP3 128kbps
- **Style**: Charismatic academic, public intellectual
- **Characteristics**:
  - Warm authority with intellectual curiosity
  - Precision—every word intentional
  - Accessibility—complex ideas made clear

See `docs/design/VOICE-IDENTITY.md` for complete voice specifications.

## Workflow Integration

This skill is Phase 9 in the podcast episode workflow:

```
Phase 7: Synthesis → report.md created
Phase 8a: Episode Planning → content_plan.md
Phase 8b: Script Generation → script.md (with TTS directives)
Phase 9: Audio Generation (this skill) → mp3 + transcript.txt
Phase 10: Audio Processing → chapters, metadata
Phase 11: Publishing → feed.xml update
```

**Note**: After audio generation, you still need to:
1. Generate chapters from transcript
2. Embed chapters into mp3
3. Create publishing metadata
4. Update feed.xml

## Troubleshooting

### "GOOGLE_API_KEY not set"
```bash
# API keys are stored in /Users/valorengels/.env (auto-loaded via ~/.zshenv)
grep GOOGLE_API_KEY /Users/valorengels/.env

# Add if missing:
echo 'GOOGLE_API_KEY=your_api_key_here' >> /Users/valorengels/.env
```

### "Missing script.md"
Ensure the episode has completed script generation (Phase 8b).

The script should have:
- ~5,200 words
- TTS directives distributed throughout
- Three-section structure

### Audio too short or cut off
The TTS API has a 32k token context limit. A 5,200-word script is ~7k tokens, so it should fit comfortably. If issues occur:
- Verify word count: `wc -w script.md`
- Check for malformed directives
- Try regenerating with `--verbose` flag

### Audio quality issues
- Ensure directives are distributed (not clustered at top)
- Use varied VOICE and PACE directives for emotional range
- Include PAUSE directives for natural breathing

## Cost Estimation

| Component | Cost | Notes |
|-----------|------|-------|
| Script Generation | ~$0.05 | Claude (Phase 8b) |
| TTS Generation | ~$0.10 | Gemini TTS API |
| **Total per Episode** | ~$0.15 | Much cheaper than Live API |

**Comparison**:
- NotebookLM: Free but no control
- Live API: ~$0.50 but unpredictable duration
- TTS API: ~$0.15 with full duration control

## Technical Details

### API Configuration

```python
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents=script_text,
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name='Alnilam'
                )
            )
        )
    )
)

# Extract PCM audio (16-bit, 24kHz)
audio_data = response.candidates[0].content.parts[0].inline_data.data
```

### Available Voices

| Voice | Notes |
|-------|-------|
| **Alnilam** | Primary - matches voice identity |
| Kore | Female alternative |
| Charon | Male alternative |
| Puck | Lighter tone |
| Aoede | Female |
| Achernar | Female |

Full list: Zephyr, Puck, Charon, Kore, Fenrir, Leda, Orus, Aoede, Callirrhoe, Autonoe, Enceladus, Iapetus, Umbriel, Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia, Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird, Zubenelgenubi, Vindemiatrix, Sadachbia, Sadaltager, Sulafat

---

*Skill Version: 2.0*
*Last Updated: 2025-12-24*
*Approach: Text-first TTS (replaces Live API)*
