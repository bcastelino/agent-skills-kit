# Token Usage Guide — Hugging Face Jobs

## Understanding Tokens

**What are HF Tokens?**
- Authentication credentials for Hugging Face Hub
- Required for authenticated operations (push, private repos, API access)
- Stored securely on your machine after `hf auth login`

**Token Types:**
- **Read Token** — download models/datasets, read private repos
- **Write Token** — push models/datasets, create/modify repos
- **Organization Token** — act on behalf of an organization

## When Tokens Are Required

**Always Required:**
- Pushing models/datasets to Hub
- Accessing private repositories
- Creating or modifying repositories
- Using Hub APIs programmatically

**Not Required:**
- Downloading public models/datasets
- Running jobs that don't interact with Hub
- Reading public repository information

## How to Provide Tokens to Jobs

### Method 1: Automatic Token (Recommended)

```python
hf_jobs("uv", {
    "script": "your_script.py",
    "secrets": {"HF_TOKEN": "$HF_TOKEN"}  # ✅ Automatic replacement
})
```

`$HF_TOKEN` is a placeholder replaced with your actual token from `hf auth login`.
Token is encrypted server-side when passed as a secret.

**Benefits:** no token exposure in code, uses current login session, automatically updated on re-login.

### Method 2: Explicit Token (Not Recommended)

```python
hf_jobs("uv", {
    "script": "your_script.py",
    "secrets": {"HF_TOKEN": "hf_abc123..."}  # ⚠️ Hardcoded
})
```

Use only when automatic token doesn't work or when testing with a specific token.

### Method 3: Environment Variable (Less Secure)

```python
hf_jobs("uv", {
    "script": "your_script.py",
    "env": {"HF_TOKEN": "hf_abc123..."}  # ⚠️ Visible in job logs
})
```

**Always prefer `secrets` over `env`** — secrets are encrypted server-side, env values appear in logs.

## Using Tokens in Scripts

```python
import os
from huggingface_hub import HfApi

# Token available as env var when passed via secrets
token = os.environ.get("HF_TOKEN")

# Explicit usage
api = HfApi(token=token)

# Or let huggingface_hub auto-detect HF_TOKEN
api = HfApi()
```

## Token Verification

```python
# Check if logged in
from huggingface_hub import whoami
user_info = whoami()

# Verify token in job
import os
assert "HF_TOKEN" in os.environ, "HF_TOKEN not found!"
token = os.environ["HF_TOKEN"]
print(f"Token starts with: {token[:7]}...")  # Should start with "hf_"
```

## Common Token Issues

| Error | Cause | Fix |
|-------|-------|-----|
| 401 Unauthorized | Token missing or invalid | Add `secrets={"HF_TOKEN": "$HF_TOKEN"}` |
| 403 Forbidden | Insufficient permissions | Ensure write permissions for push operations |
| Token not found | secrets not passed | Use `secrets=` (not `env=`) |
| Repo access denied | No access to private repo | Use token from account with access |

## Security Best Practices

1. **Never commit tokens** — use `$HF_TOKEN` placeholder
2. **Use secrets, not env** — secrets are encrypted server-side
3. **Rotate tokens regularly** — generate new tokens periodically
4. **Use minimal permissions** — create tokens with only needed permissions
5. **Don't share tokens** — each user should use their own
6. **Monitor token usage** — check activity in Hub settings

## Complete Example

```python
hf_jobs("uv", {
    "script": """
# /// script
# dependencies = ["huggingface-hub", "datasets"]
# ///
import os
from huggingface_hub import HfApi
from datasets import Dataset

assert "HF_TOKEN" in os.environ, "HF_TOKEN required!"
api = HfApi(token=os.environ["HF_TOKEN"])

data = {"text": ["Hello", "World"]}
dataset = Dataset.from_dict(data)
dataset.push_to_hub("username/my-dataset", token=os.environ["HF_TOKEN"])
print("✅ Dataset pushed successfully!")
""",
    "flavor": "cpu-basic",
    "timeout": "30m",
    "secrets": {"HF_TOKEN": "$HF_TOKEN"}
})
```
