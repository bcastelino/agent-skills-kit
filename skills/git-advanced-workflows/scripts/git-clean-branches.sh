#!/bin/bash
# Clean up merged and stale Git branches.
# Usage: ./git-clean-branches.sh [--remote] [--stale-days 90]
set -euo pipefail

REMOTE=false
STALE_DAYS=90

while [[ $# -gt 0 ]]; do
    case $1 in
        --remote) REMOTE=true; shift ;;
        --stale-days) STALE_DAYS="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

echo "=== Git Branch Cleanup ==="

# Clean merged local branches
echo "\nMerged local branches (will delete):"
MERGED=$(git branch --merged main | grep -v "main\|develop\|\*" || true)
if [ -n "$MERGED" ]; then
    echo "$MERGED"
    echo "$MERGED" | xargs git branch -d
    echo "Deleted merged branches."
else
    echo "None found."
fi

# Prune remote tracking branches
echo "\nPruning stale remote tracking branches..."
git remote prune origin

# List stale branches
echo "\nBranches with no commits in the last ${STALE_DAYS} days:"
CUTOFF=$(date -d "${STALE_DAYS} days ago" +%Y-%m-%d 2>/dev/null || date -v-${STALE_DAYS}d +%Y-%m-%d)
git for-each-ref --sort=-committerdate refs/heads/ \
    --format='%(committerdate:short) %(refname:short)' | \
    while read date branch; do
        if [[ "$date" < "$CUTOFF" ]]; then
            echo "  $date $branch"
        fi
    done

echo "\n=== Cleanup complete ==="
