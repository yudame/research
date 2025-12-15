#!/bin/bash
# Validate feed.xml after edits
# Only runs validation if feed.xml was the edited file

EDITED_FILE="$CLAUDE_FILE_PATH"

if [[ "$EDITED_FILE" == *"feed.xml"* ]]; then
  # Use dynamic path based on repository root
  REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"

  if [ -z "$REPO_ROOT" ]; then
    # Fallback: assume we're in the repository
    FEED_PATH="$(pwd)/podcast/feed.xml"
  else
    FEED_PATH="$REPO_ROOT/podcast/feed.xml"
  fi

  # Basic XML syntax validation
  if xmllint --noout "$FEED_PATH" 2>&1; then
    echo "✅ Basic XML validation passed"
    echo ""
    echo "⚠️  REMINDER: Run comprehensive validation before committing:"
    echo "   Use the podcast-feed-validator skill to check:"
    echo "   - RSS spec compliance"
    echo "   - File metadata accuracy"
    echo "   - Required elements"
    echo "   - Content quality"
  else
    echo "❌ ERROR: feed.xml has XML syntax errors"
    echo ""
    echo "Fix the XML errors above before proceeding."
    exit 1
  fi
fi
