# Git Workflow Checklist

## Before Starting a Feature
- [ ] Pull latest changes from main
- [ ] Create feature branch with descriptive name
- [ ] Verify you're on the correct branch

## During Development
- [ ] Commit frequently with clear messages
- [ ] Keep commits focused (one logical change per commit)
- [ ] Run tests before committing
- [ ] Rebase onto main periodically for long-lived branches

## Before Opening PR
- [ ] Rebase onto latest main
- [ ] Squash fixup/WIP commits
- [ ] Ensure all tests pass
- [ ] Review your own diff
- [ ] Write clear PR description

## After PR Approval
- [ ] Squash merge or rebase merge (per team convention)
- [ ] Delete feature branch after merge
- [ ] Verify deployment (if applicable)

## Emergency Procedures
- [ ] Revert a bad merge: `git revert -m 1 <merge-commit>`
- [ ] Recover lost commits: `git reflog`
- [ ] Undo last commit: `git reset --soft HEAD~1`
