# Git Conflict Resolution Guide

Strategies and tools for resolving merge conflicts efficiently.

## Understanding Conflict Markers

```
<<<<<<< HEAD (current branch)
Your changes
=======
Their changes
>>>>>>> feature-branch (incoming)
```

## Resolution Strategies

### Accept One Side
```bash
# Accept current (ours)
git checkout --ours <file>

# Accept incoming (theirs)
git checkout --theirs <file>
```

### Manual Merge
1. Open conflicted file
2. Find conflict markers (`<<<<<<<`)
3. Edit to desired result
4. Remove conflict markers
5. Save and `git add <file>`

### Using Merge Tools
```bash
# VS Code
git config merge.tool vscode
git mergetool

# Beyond Compare
git config merge.tool bc
git mergetool
```

## Prevention Strategies

- Pull/rebase frequently to stay current
- Communicate with team about shared files
- Use smaller, focused commits
- Avoid reformatting unrelated code
- Use `.gitattributes` for merge strategies

## Complex Scenarios

### Conflict During Rebase
```bash
# Fix conflict, then continue
git add <file>
git rebase --continue

# Skip problematic commit
git rebase --skip

# Give up and restore
git rebase --abort
```

### Conflict in Binary Files
- Binary files cannot be merged automatically
- Choose one version: `git checkout --ours/--theirs <file>`
- Or manually replace the file
