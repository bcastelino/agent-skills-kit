# GitHub Workflow Automation — Full Examples

> This file contains complete YAML workflow definitions and code excerpts
> referenced from the main SKILL.md.  Keep them here so the skill file
> stays concise while users can copy-paste ready-made workflows.

---

## 1. PR Review Action

```yaml
# .github/workflows/ai-review.yml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize]

permissions:
  pull-requests: write
  contents: read

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Get changed files
        id: changed
        run: |
          files=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
          echo "files<<EOF" >> $GITHUB_OUTPUT
          echo "$files" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Get diff
        id: diff
        run: |
          diff=$(git diff origin/${{ github.base_ref }}...HEAD)
          echo "diff<<EOF" >> $GITHUB_OUTPUT
          echo "$diff" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: AI Review
        uses: actions/github-script@v7
        with:
          script: |
            const { Anthropic } = require('@anthropic-ai/sdk');
            const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

            const response = await client.messages.create({
              model: "claude-3-sonnet-20240229",
              max_tokens: 4096,
              messages: [{
                role: "user",
                content: `Review this PR diff and provide feedback:
                
                Changed files: ${{ steps.changed.outputs.files }}
                
                Diff:
                ${{ steps.diff.outputs.diff }}
                
                Provide:
                1. Summary of changes
                2. Potential issues or bugs
                3. Suggestions for improvement
                4. Security concerns if any
                
                Format as GitHub markdown.`
              }]
            });

            await github.rest.pulls.createReview({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number,
              body: response.content[0].text,
              event: 'COMMENT'
            });
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Review Comment Structure

````markdown
## 📋 Summary
Brief description of what this PR does.

## ✅ What looks good
- Well-structured code
- Good test coverage

## ⚠️ Potential Issues
1. **Line 42**: Possible null pointer — suggest optional chaining.
2. **Line 78**: Missing error handling.

## 💡 Suggestions
- Extract validation into a separate function.
- Add JSDoc comments for public methods.

## 🔒 Security Notes
- No sensitive data exposure detected.
````

### Focused Review (filter by file type)

```yaml
- name: Filter code files
  run: |
    files=$(git diff --name-only origin/${{ github.base_ref }}...HEAD | \
            grep -E '\.(ts|tsx|js|jsx|py|go)$' || true)
    echo "code_files=$files" >> $GITHUB_OUTPUT
```

---

## 2. Issue Triage

### Auto-label Issues

```yaml
# .github/workflows/issue-triage.yml
name: Issue Triage

on:
  issues:
    types: [opened]

jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:
      issues: write

    steps:
      - name: Analyze issue
        uses: actions/github-script@v7
        with:
          script: |
            const issue = context.payload.issue;
            const analysis = await analyzeIssue(issue.title, issue.body);

            const labels = [];
            if (analysis.type === 'bug') {
              labels.push('bug');
              if (analysis.severity === 'high') labels.push('priority: high');
            } else if (analysis.type === 'feature') {
              labels.push('enhancement');
            } else if (analysis.type === 'question') {
              labels.push('question');
            }
            if (analysis.area) labels.push(`area: ${analysis.area}`);

            await github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: issue.number,
              labels: labels
            });

            if (analysis.type === 'bug' && !analysis.hasReproSteps) {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                body: `Thanks for reporting! Please provide:
- Steps to reproduce
- Expected vs actual behavior
- Environment details`
              });
            }
```

### Triage Prompt

```typescript
const TRIAGE_PROMPT = `
Analyze this GitHub issue:
Title: {title}  Body: {body}
Return JSON:
{
  "type": "bug"|"feature"|"question"|"docs"|"other",
  "severity": "low"|"medium"|"high"|"critical",
  "area": "frontend"|"backend"|"api"|"docs"|"ci"|"other",
  "summary": "one-line summary",
  "hasReproSteps": boolean,
  "suggestedLabels": ["label1"],
  "suggestedAssignees": ["username"]
}`;
```

### Stale Issue Management

```yaml
# .github/workflows/stale.yml
name: Manage Stale Issues

on:
  schedule:
    - cron: "0 0 * * *"

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          stale-issue-message: |
            This issue has been automatically marked as stale because it has not had
            recent activity. It will be closed in 14 days if no further activity occurs.
          stale-pr-message: |
            This PR has been automatically marked as stale and will be closed in 14 days.
          days-before-stale: 60
          days-before-close: 14
          stale-issue-label: "stale"
          stale-pr-label: "stale"
          exempt-issue-labels: "pinned,security,in-progress"
          exempt-pr-labels: "pinned,security"
```

---

## 3. CI/CD Integration

### Smart Test Selection

```yaml
# .github/workflows/smart-tests.yml
name: Smart Test Selection

on:
  pull_request:

jobs:
  analyze:
    runs-on: ubuntu-latest
    outputs:
      test_suites: ${{ steps.analyze.outputs.suites }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Analyze changes
        id: analyze
        run: |
          changed=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
          suites="[]"
          if echo "$changed" | grep -q "^src/api/"; then
            suites=$(echo $suites | jq '. + ["api"]')
          fi
          if echo "$changed" | grep -q "^src/frontend/"; then
            suites=$(echo $suites | jq '. + ["frontend"]')
          fi
          if echo "$changed" | grep -q "^src/database/"; then
            suites=$(echo $suites | jq '. + ["database", "api"]')
          fi
          if [ "$suites" = "[]" ]; then suites='["all"]'; fi
          echo "suites=$suites" >> $GITHUB_OUTPUT

  test:
    needs: analyze
    runs-on: ubuntu-latest
    strategy:
      matrix:
        suite: ${{ fromJson(needs.analyze.outputs.test_suites) }}
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: |
          if [ "${{ matrix.suite }}" = "all" ]; then
            npm test
          else
            npm test -- --suite ${{ matrix.suite }}
          fi
```

### Deploy with AI Risk Assessment

```yaml
# .github/workflows/deploy.yml
name: Deploy with AI Validation

on:
  push:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Get deployment changes
        id: changes
        run: |
          last_deploy=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
          if [ -n "$last_deploy" ]; then
            changes=$(git log --oneline $last_deploy..HEAD)
          else
            changes=$(git log --oneline -10)
          fi
          echo "changes<<EOF" >> $GITHUB_OUTPUT
          echo "$changes" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: AI Risk Assessment
        id: assess
        uses: actions/github-script@v7
        with:
          script: |
            const prompt = `Analyze these changes for deployment risk:
            ${process.env.CHANGES}
            Return JSON: { "riskLevel", "concerns", "recommendations", "requiresManualApproval" }`;
            const analysis = await callAI(prompt);
            if (analysis.riskLevel === 'high') {
              core.setFailed('High-risk deployment detected. Manual review required.');
            }
            return analysis;
        env:
          CHANGES: ${{ steps.changes.outputs.changes }}

  deploy:
    needs: validate
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy
        run: echo "Deploying to production..."
```

### Rollback Automation

```yaml
# .github/workflows/rollback.yml
name: Automated Rollback

on:
  workflow_dispatch:
    inputs:
      reason:
        description: "Reason for rollback"
        required: true

jobs:
  rollback:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Find last stable version
        id: stable
        run: |
          stable=$(git tag -l 'v*' --sort=-version:refname | head -1)
          echo "version=$stable" >> $GITHUB_OUTPUT
      - name: Rollback
        run: |
          git checkout ${{ steps.stable.outputs.version }}
          npm run deploy
      - name: Notify team
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "🔄 Rolled back to ${{ steps.stable.outputs.version }}",
              "blocks": [{
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "*Rollback*\n• Version: `${{ steps.stable.outputs.version }}`\n• Reason: ${{ inputs.reason }}\n• By: ${{ github.actor }}"
                }
              }]
            }
```

---

## 4. Git Operations

### Auto-Rebase

```yaml
# .github/workflows/auto-rebase.yml
name: Auto Rebase

on:
  issue_comment:
    types: [created]

jobs:
  rebase:
    if: github.event.issue.pull_request && contains(github.event.comment.body, '/rebase')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}
      - name: Setup Git
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
      - name: Rebase PR
        run: |
          gh pr checkout ${{ github.event.issue.number }}
          git fetch origin main
          git rebase origin/main
          git push --force-with-lease
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Comment result
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: '✅ Successfully rebased onto main!'
            })
```

### Smart Cherry-Pick

```typescript
async function smartCherryPick(commitHash: string, targetBranch: string) {
  const commitInfo = await exec(`git show ${commitHash} --stat`);
  const targetDiff = await exec(`git diff ${targetBranch}...HEAD -- ${affectedFiles}`);

  const analysis = await ai.analyze(`
    Cherry-pick ${commitHash} to ${targetBranch}:
    ${commitInfo}
    Target state: ${targetDiff}
    Will there be conflicts? Suggest resolution strategy.
  `);

  if (analysis.willConflict) {
    await exec(`git checkout -b cherry-pick-${commitHash.slice(0, 7)} ${targetBranch}`);
    const result = await exec(`git cherry-pick ${commitHash}`, { allowFail: true });
    if (result.failed) {
      const conflicts = await getConflicts();
      for (const conflict of conflicts) {
        const resolution = await ai.resolveConflict(conflict);
        await applyResolution(conflict.file, resolution);
      }
    }
  } else {
    await exec(`git checkout ${targetBranch}`);
    await exec(`git cherry-pick ${commitHash}`);
  }
}
```

### Branch Cleanup

```yaml
# .github/workflows/branch-cleanup.yml
name: Branch Cleanup

on:
  schedule:
    - cron: '0 0 * * 0'
  workflow_dispatch:

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Find stale branches
        id: stale
        run: |
          stale=$(git for-each-ref --sort=-committerdate refs/remotes/origin \
            --format='%(refname:short) %(committerdate:relative)' | \
            grep -E '[3-9][0-9]+ days|[0-9]+ months|[0-9]+ years' | \
            grep -v 'origin/main\|origin/develop' | \
            cut -d' ' -f1 | sed 's|origin/||')
          echo "branches<<EOF" >> $GITHUB_OUTPUT
          echo "$stale" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT
      - name: Create cleanup issue
        if: steps.stale.outputs.branches != ''
        uses: actions/github-script@v7
        with:
          script: |
            const branches = `${{ steps.stale.outputs.branches }}`.split('\n').filter(Boolean);
            await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Stale Branch Cleanup',
              body: `## 🧹 Stale Branches (>30 days)\n${branches.map(b => '- \`' + b + '\`').join('\n')}`,
              labels: ['housekeeping']
            });
```

---

## 5. On-Demand Assistance — @mention Bot

```yaml
# .github/workflows/mention-bot.yml
name: AI Mention Bot

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]

jobs:
  respond:
    if: contains(github.event.comment.body, '@ai-helper')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Extract question
        id: question
        run: |
          question=$(echo "${{ github.event.comment.body }}" | sed 's/.*@ai-helper//')
          echo "question=$question" >> $GITHUB_OUTPUT
      - name: Get context
        id: context
        run: |
          if [ "${{ github.event.issue.pull_request }}" != "" ]; then
            gh pr diff ${{ github.event.issue.number }} > context.txt
          else
            gh issue view ${{ github.event.issue.number }} --json body -q .body > context.txt
          fi
          echo "context=$(cat context.txt)" >> $GITHUB_OUTPUT
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: AI Response
        uses: actions/github-script@v7
        with:
          script: |
            const response = await ai.chat(`
              Context: ${process.env.CONTEXT}
              Question: ${process.env.QUESTION}
              Provide a helpful, specific answer with code examples if relevant.
            `);
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: response
            });
        env:
          CONTEXT: ${{ steps.context.outputs.context }}
          QUESTION: ${{ steps.question.outputs.question }}
```

---

## 6. Repository Configuration

### CODEOWNERS

```
# .github/CODEOWNERS
* @org/core-team
/src/frontend/ @org/frontend-team
*.tsx @org/frontend-team
/src/api/ @org/backend-team
/src/database/ @org/backend-team
/.github/ @org/devops-team
/terraform/ @org/devops-team
Dockerfile @org/devops-team
/docs/ @org/docs-team
/src/auth/ @org/security-team
/src/crypto/ @org/security-team
```

### Branch Protection

```yaml
- name: Configure branch protection
  uses: actions/github-script@v7
  with:
    script: |
      await github.rest.repos.updateBranchProtection({
        owner: context.repo.owner,
        repo: context.repo.repo,
        branch: 'main',
        required_status_checks: {
          strict: true,
          contexts: ['test', 'lint', 'ai-review']
        },
        enforce_admins: true,
        required_pull_request_reviews: {
          required_approving_review_count: 1,
          require_code_owner_reviews: true,
          dismiss_stale_reviews: true
        },
        restrictions: null,
        required_linear_history: true,
        allow_force_pushes: false,
        allow_deletions: false
      });
```
