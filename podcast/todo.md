# Podcast Setup TODO

## Initial Setup

- [ ] Enable GitHub Pages for this repository
  - Go to repository Settings → Pages
  - Set Source to "Deploy from a branch"
  - Select branch: `main` and folder: `/ (root)`
  - Save and wait for deployment

- [x] Update feed.xml with your information
  - [x] Replace `YOUR_USERNAME` with GitHub organization (yudame)
  - [x] Update podcast title (Yudame Research Podcast)
  - [x] Update author name (Tom Counsell)
  - [x] Update email address
  - [x] Update description/summary

- [ ] Install BFG Repo-Cleaner (for purging old episodes)
  ```bash
  brew install bfg
  ```

- [ ] Create your first episode
  - [ ] Generate MP3 file
  - [ ] Name it using convention: `YYYY-MM-DD-title.mp3`
  - [ ] Copy to `podcast/episodes/`
  - [ ] Get file size: `ls -lh podcast/episodes/YOUR_FILE.mp3`
  - [ ] Get duration from your audio editor
  - [ ] Add episode entry to feed.xml (uncomment and fill in the example)
  - [ ] Commit and push

- [ ] Test the feed
  - [ ] Wait for GitHub Pages to deploy (check Actions tab)
  - [ ] Visit `https://yudame.github.io/research/podcast/feed.xml` in browser
  - [ ] Subscribe in your podcast app
  - [ ] Verify episode appears and plays correctly

## Optional Enhancements

- [ ] Create automation script (Python/Bash) to:
  - [ ] Accept MP3 file and metadata as input
  - [ ] Automatically update feed.xml
  - [ ] Handle git history purging
  - [ ] Push changes

- [ ] Add podcast artwork
  - [ ] Create 1400x1400 or 3000x3000 PNG/JPG
  - [ ] Upload to repo
  - [ ] Add `<itunes:image href="URL"/>` to feed.xml

- [ ] Set up Git LFS for episodes (if needed for files >100MB)
  - Note: This adds complexity, consider keeping episodes under 100MB instead

## Maintenance Checklist

When adding episode #9 (and beyond):
- [ ] Identify oldest episode to delete
- [ ] Remove MP3 from `episodes/` directory
- [ ] Remove corresponding `<item>` from feed.xml
- [ ] Purge from git history using BFG
- [ ] Add new episode MP3
- [ ] Add new `<item>` to feed.xml
- [ ] Commit and push with force
