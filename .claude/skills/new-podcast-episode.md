# New Podcast Episode Workflow

You are helping create a new podcast episode following a structured research and production workflow.

## Episode Directory Structure

Each episode follows this organization:
```
podcast/episodes/YYYY-MM-DD-topic-slug/
├── research/
│   ├── sources.md          # Organized list of source links
│   ├── raw-notes.md        # NotebookLM/research tool outputs
│   ├── documents/          # PDFs, articles, downloads
│   └── assets/             # Images, charts, data files
├── report.md               # Final research report/show notes
├── script.md               # Episode script/outline (optional)
└── YYYY-MM-DD-topic-slug.mp3  # Final audio file
```

## Workflow Phases

### 1. Setup Phase
- Ask for the episode topic and date
- Create the episode directory structure
- Initialize sources.md with a template structure

### 2. Research Phase (User-led with your support)
- User will conduct research using deep research tools and NotebookLM
- Help organize source files into `/documents/` and `/assets/`
- Maintain sources.md with all links and references
- Organize raw notes into raw-notes.md

### 3. Report Phase (Collaborative)
- Review all research materials
- Compile findings into report.md
- Structure the final report with clear sections
- Create show notes if needed

### 4. Production Phase
- Help organize any final materials
- Once audio file is ready, place it in the episode directory
- Update the main feed.xml with episode metadata
- Commit and publish

## Your Role

Throughout this process:
- Keep files organized in the correct directories
- Maintain clean, structured markdown for sources and reports
- Track source links and ensure proper attribution
- Help synthesize research into clear, publishable reports
- Never create the audio file (user handles this)

## Getting Started

Ask the user:
1. What's the topic for this episode?
2. What date should we use (YYYY-MM-DD format)?
3. Are they ready to create the directory structure now?

Then guide them through each phase as they progress.
