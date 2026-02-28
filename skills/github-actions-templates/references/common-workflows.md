# Common GitHub Actions Workflow Patterns

## Caching Dependencies

### Python (pip)
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: ${{ runner.os }}-pip-
```

### Node.js (npm)
```yaml
- uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: npm
```

### Rust (cargo)
```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.cargo/registry
      ~/.cargo/git
      target/
    key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.lock') }}
```

## Conditional Execution

```yaml
# Only on main branch pushes
if: github.ref == 'refs/heads/main' && github.event_name == 'push'

# Only for PRs targeting main
if: github.event_name == 'pull_request' && github.base_ref == 'main'

# Skip for docs-only changes
if: "!contains(github.event.head_commit.message, '[skip ci]')"
```

## Secrets Management

```yaml
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
  API_KEY: ${{ secrets.API_KEY }}
```

## Artifact Sharing Between Jobs

```yaml
# Upload in build job
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/

# Download in deploy job
- uses: actions/download-artifact@v4
  with:
    name: build-output
    path: dist/
```

## Notification Patterns

### Slack on Failure
```yaml
- uses: 8398a7/action-slack@v3
  if: failure()
  with:
    status: failure
    fields: repo,message,author
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```
