# Hugging Face CLI Workflow Examples

## Download and Use a Model

```bash
# Download model to local directory
hf download meta-llama/Llama-3.2-1B-Instruct --local-dir ./model

# Get cache path (for scripts)
MODEL_PATH=$(hf download meta-llama/Llama-3.2-1B-Instruct --quiet)

# Download specific files only
hf download bert-base-uncased --include "*.bin" "*.json" --local-dir ./bert
```

## Publish a Model

```bash
# Create repo and upload
hf repo create my-username/my-model --private
hf upload my-username/my-model ./output . --commit-message "Initial release"

# Upload specific files
hf upload my-username/my-model model.safetensors model.safetensors
hf upload my-username/my-model config.json config.json
```

## Work with Datasets

```bash
# Download a dataset
hf download --repo-type dataset squad --local-dir ./squad

# Upload a dataset
hf repo create my-username/my-dataset --repo-type dataset
hf upload my-username/my-dataset --repo-type dataset ./data .
```

## Create and Deploy a Space

```bash
# Create Gradio space
hf repo create my-username/my-app --space_sdk gradio

# Upload Space files
hf upload my-username/my-app ./app .
```

## Cache Management

```bash
# Check what's cached
hf cache ls

# Free up space
hf cache prune           # Remove detached revisions
hf cache rm MODEL_ID     # Remove specific model

# Verify cache integrity
hf cache verify
```

## Batch Operations

```bash
# Download multiple models
for model in bert-base gpt2 t5-small; do
    hf download $model --local-dir ./models/$model
done

# Upload with PR for review
hf upload org/shared-model ./updates . --create-pr --commit-message "Update weights"
```
