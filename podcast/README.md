# Personal Podcast Feed

A simple self-hosted podcast feed using GitHub Pages.

## Quick Start

### Adding a New Episode

1. **Create your MP3 file** using your preferred audio tools
2. **Name it**: `YYYY-MM-DD-title-slug.mp3` (e.g., `2025-01-19-intro-to-math.mp3`)
3. **Add to episodes folder**: Drop the file into `podcast/episodes/`
4. **Update feed.xml**:
   - Copy an existing `<item>` block
   - Update: title, description, pubDate, file URL, file size, duration, guid
5. **Check episode count**: If more than 8 episodes exist:
   - Delete oldest MP3 from `episodes/`
   - Remove oldest `<item>` from feed.xml
   - Purge from git history (see below)
6. **Commit and push**

### Purging Old Episodes from Git History

When you delete an episode, remove it from git history to save space:

```bash
# Install BFG Repo-Cleaner (one-time setup)
brew install bfg

# Purge the old file
bfg --delete-files "old-episode.mp3" .git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

### Subscribe to Your Feed

Once GitHub Pages is enabled, subscribe to:
```
https://yudame.github.io/protocols/podcast/feed.xml
```

## Limits

- Maximum 8 episodes at a time
- Each file must be under 100 MB
- Repository should stay under 1 GB total

## File Sizes

For reference, typical podcast bitrates:
- 64 kbps = ~29 MB per hour
- 96 kbps = ~43 MB per hour
- 128 kbps = ~58 MB per hour (recommended)
