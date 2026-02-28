# Saving Results — Hugging Face Jobs

> **⚠️ EPHEMERAL ENVIRONMENT** — The Jobs environment is temporary. All files are
> deleted when the job ends. If results aren't persisted, **ALL WORK IS LOST**.

## Persistence Options

### 1. Push to Hugging Face Hub (Recommended)

```python
import os
from huggingface_hub import HfApi

api = HfApi(token=os.environ.get("HF_TOKEN"))

# Push models
model.push_to_hub("username/model-name", token=os.environ["HF_TOKEN"])

# Push datasets
dataset.push_to_hub("username/dataset-name", token=os.environ["HF_TOKEN"])

# Push arbitrary artifacts
api.upload_file(
    path_or_fileobj="results.json",
    path_in_repo="results.json",
    repo_id="username/results",
    token=os.environ["HF_TOKEN"]
)
```

### 2. External Storage (S3, GCS, etc.)

```python
import boto3
s3 = boto3.client('s3')
s3.upload_file('results.json', 'my-bucket', 'results.json')
```

### 3. Send Results via API

```python
import requests
requests.post("https://your-api.com/results", json=results)
```

## Required Configuration for Hub Push

**In job submission:**
```python
{
    "secrets": {"HF_TOKEN": "$HF_TOKEN"}  # Enables authentication
}
```

**In script:**
```python
import os
from huggingface_hub import HfApi
api = HfApi(token=os.environ.get("HF_TOKEN"))
api.upload_file(...)
```

## Pre-submission Checklist

- [ ] Results persistence method chosen
- [ ] `secrets={"HF_TOKEN": "$HF_TOKEN"}` included if using Hub
- [ ] Script handles missing token gracefully
- [ ] Test persistence path works
