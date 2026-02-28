# Git Advanced Workflows Implementation Playbook

Detailed guides and examples for advanced Git operations.

## Interactive Rebase Guide

### Common Operations
```bash
# Rebase last 5 commits interactively
git rebase -i HEAD~5

# Rebase onto main
git rebase -i main

# Commands in interactive rebase:
# pick   = keep commit as-is
# reword = change commit message
# edit   = stop to amend commit
# squash = combine with previous commit
# fixup  = like squash but discard message
# drop   = remove commit
```

### Squash Workflow
```bash
git checkout feature-branch
git rebase -i main
# Mark all but first as 'squash'
git checkout main
git merge feature-branch
```

## Conflict Resolution Strategies

### Standard Resolution
```bash
git rebase main
# On conflict:
git add <resolved-files>
git rebase --continue
# To abort if needed
git rebase --abort
```

### Using Merge Tools
```bash
git config merge.tool vscode
git config mergetool.vscode.cmd "code --wait --merge $REMOTE $LOCAL $BASE $MERGED"
git mergetool
```

## History Rewriting

### Amending Commits
```bash
git commit --amend -m "New message"
git add <files>
git commit --amend --no-edit
git commit --amend --author="Name <email>"
```

### Filter-Branch Alternatives
```bash
git filter-repo --path secrets.env --invert-paths
git filter-repo --mailmap mailmap.txt
```

## Branch Cleanup

### Automated Cleanup Script
```bash
#!/bin/bash
# Clean merged branches
git branch --merged main | grep -v "main\|develop" | xargs -r git branch -d

# Clean remote tracking branches
git remote prune origin

# List stale branches (no commits in 3 months)
git for-each-ref --sort=-committerdate refs/heads/ \
  --format="%(committerdate:short) %(refname:short)"
```

## Bisect Workflow

```bash
git bisect start
git bisect bad HEAD
git bisect good v1.0.0
# Git checks out middle commit; test and mark
git bisect good  # or git bisect bad
# Automate with test script
git bisect run ./test-script.sh
# When done
git bisect reset
```
