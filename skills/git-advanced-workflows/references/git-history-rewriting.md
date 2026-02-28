# Git History Rewriting Guide

Advanced techniques for modifying Git history safely.

## Amending Recent Commits

```bash
# Change last commit message
git commit --amend -m "New message"

# Add forgotten file to last commit
git add forgotten-file.py
git commit --amend --no-edit

# Change author of last commit
git commit --amend --author="Name <email@example.com>"
```

## Rewriting Older Commits

### Interactive Rebase
```bash
# Edit the last 5 commits
git rebase -i HEAD~5
```

### git-filter-repo (Recommended over filter-branch)
```bash
# Remove sensitive file from all history
git filter-repo --path secrets.env --invert-paths

# Change email across all commits
git filter-repo --mailmap mailmap.txt

# Rename a directory
git filter-repo --path-rename old-dir/:new-dir/
```

## Recovery with Reflog

```bash
# View recent HEAD movements
git reflog

# Recover deleted branch
git checkout -b recovered-branch HEAD@{5}

# Undo a bad rebase
git reset --hard HEAD@{3}
```

## Safety Rules

1. **Never rewrite shared history** (pushed commits others depend on)
2. **Always backup** before major rewrites: `git branch backup-before-rewrite`
3. **Use force-push with lease**: `git push --force-with-lease` (safer than `--force`)
4. **Communicate** with team before any history rewrite on shared branches
