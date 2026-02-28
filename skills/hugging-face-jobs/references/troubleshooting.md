# Troubleshooting — Hugging Face Jobs

## Common Failure Modes

### Out of Memory (OOM)

**Symptoms:** Job crashes with `RuntimeError: CUDA out of memory` or process killed by OOM-killer.

**Fixes:**
1. Reduce batch size or data chunk size
2. Process data in smaller batches / streaming mode
3. Upgrade hardware: `cpu` → `t4` → `a10g` → `a100`
4. Enable gradient checkpointing for training workloads
5. Use lower precision (`fp16` / `bf16`)

### Job Timeout

**Symptoms:** Job stops at exactly the timeout duration; logs show no error.

**Fixes:**
1. Check logs for actual runtime so far
2. Increase timeout with 20-30% buffer: `"timeout": "3h"`
3. Optimize code for faster execution
4. Process data in chunks and save checkpoints

### Hub Push Failures

**Symptoms:** `401 Unauthorized`, `403 Forbidden`, or `HfHubHTTPError`.

**Fixes:**
1. Add `secrets={"HF_TOKEN": "$HF_TOKEN"}` to job config
2. Verify token in script: `assert "HF_TOKEN" in os.environ`
3. Check token permissions (write required for push)
4. Verify target repo exists or your token can create it

### Missing Dependencies

**Symptoms:** `ModuleNotFoundError` at runtime.

**Fix:** Add to PEP 723 header:
```python
# /// script
# dependencies = ["package1", "package2>=1.0.0"]
# ///
```

Or pass extra deps:
```python
hf_jobs("uv", {
    "script": "...",
    "dependencies": ["transformers", "torch>=2.0"]
})
```

### Authentication Errors

**Symptoms:** `401 Unauthorized` when calling Hub APIs.

**Fixes:**
1. Check `hf_whoami()` works locally
2. Verify `secrets={"HF_TOKEN": "$HF_TOKEN"}` in job config
3. Re-login: `hf auth login`
4. Check token has required permissions at https://huggingface.co/settings/tokens

### Script Path Errors (MCP tool)

**Symptoms:** `FileNotFoundError` when using `hf_jobs()` MCP tool with a local path.

**Cause:** The remote container doesn't have your local file system.

**Fixes:**
```python
# ❌ Will fail
hf_jobs("uv", {"script": "./scripts/foo.py"})

# ✅ Read file contents and pass inline
from pathlib import Path
script = Path("hf-jobs/scripts/foo.py").read_text()
hf_jobs("uv", {"script": script})

# ✅ Use a URL
hf_jobs("uv", {"script": "https://huggingface.co/.../raw/main/foo.py"})
```

> Note: the `hf jobs uv run` CLI *does* support local paths (it uploads the script).

## Quick Diagnosis Checklist

| Problem | First thing to check |
|---------|---------------------|
| Job times out | Increase timeout, check logs for actual progress |
| Results not saved | Verify persistence method + HF_TOKEN in secrets |
| OOM | Reduce batch size, upgrade hardware |
| Import errors | Add packages to PEP 723 `dependencies` |
| Auth errors | Check `hf_whoami()`, verify secrets parameter |
| Script not found | Pass inline code or URL to `hf_jobs()` MCP tool |
