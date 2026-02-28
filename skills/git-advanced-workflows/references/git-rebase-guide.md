# Git Rebase Guide

Comprehensive guide to interactive and non-interactive rebasing.

## When to Rebase

- **Before merging**: Clean up feature branch history
- **Keeping up to date**: Rebase feature branch onto updated main
- **Squashing commits**: Combine related commits before PR

## When NOT to Rebase

- **Shared branches**: Never rebase commits that others have pulled
- **Main/develop branches**: Only merge into these
- **After push**: Unless you're the only one on the branch

## Interactive Rebase Commands

| Command | Effect |
|---------|--------|
| `pick` | Keep commit as-is |
| `reword` | Change commit message only |
| `edit` | Pause to amend commit |
| `squash` | Combine with previous, edit message |
| `fixup` | Combine with previous, discard message |
| `drop` | Remove commit entirely |
| `exec` | Run a shell command |

## Common Workflows

### Clean Up Before PR
```bash
git rebase -i main
# Squash fixup commits, reword unclear messages
```

### Split a Commit
```bash
git rebase -i HEAD~3
# Mark commit as 'edit'
git reset HEAD~1
git add -p  # Stage pieces
git commit -m "Part 1"
git add .
git commit -m "Part 2"
git rebase --continue
```

### Reorder Commits
```bash
git rebase -i HEAD~5
# Move lines up/down in the editor
```

## Handling Conflicts

1. Fix conflicts in affected files
2. `git add <resolved-files>`
3. `git rebase --continue`
4. To abort: `git rebase --abort`
