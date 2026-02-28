# Recommended Git Aliases

Add these to your `~/.gitconfig` under `[alias]`:

```ini
[alias]
    # Status and log
    s = status -sb
    lg = log --oneline --graph --decorate -20
    lga = log --oneline --graph --decorate --all
    last = log -1 HEAD --stat

    # Branching
    co = checkout
    cb = checkout -b
    br = branch -vv
    brd = branch -d
    brD = branch -D

    # Staging and committing
    aa = add --all
    cm = commit -m
    ca = commit --amend --no-edit
    unstage = reset HEAD --

    # Rebasing
    ri = rebase -i
    rc = rebase --continue
    ra = rebase --abort

    # Cleanup
    cleanup = "!git branch --merged main | grep -v main | xargs -r git branch -d"
    prune-remote = fetch --prune

    # Stashing
    sl = stash list
    sp = stash pop
    ss = stash push -m

    # Diff
    d = diff --stat
    dc = diff --cached
    dt = difftool
```
