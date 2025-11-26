#!/bin/bash
# Validate feed.xml after edits
# Only runs validation if feed.xml was the edited file

EDITED_FILE="$CLAUDE_FILE_PATH"

if [[ "$EDITED_FILE" == *"feed.xml"* ]]; then
  FEED_PATH="/Users/tomcounsell/src/research/podcast/feed.xml"

  if xmllint --noout "$FEED_PATH" 2>&1; then
    echo "feed.xml validation passed"
  else
    echo "ERROR: feed.xml has XML errors"
    exit 1
  fi
fi
