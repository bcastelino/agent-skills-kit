# Hugging Face CLI Command Reference

Complete reference for the `hf` CLI tool.

## Authentication

| Command | Description |
|---------|-------------|
| `hf auth login` | Interactive login |
| `hf auth login --token TOKEN` | Login with token |
| `hf auth whoami` | Show current user |
| `hf auth list` | List saved tokens |
| `hf auth switch` | Switch between tokens |
| `hf auth logout` | Remove saved token |

## Download

| Command | Description |
|---------|-------------|
| `hf download REPO_ID` | Download full repo |
| `hf download REPO_ID FILE` | Download specific file |
| `hf download REPO_ID --local-dir DIR` | Download to directory |
| `hf download REPO_ID --include "*.safetensors"` | Filter by pattern |
| `hf download REPO_ID --repo-type dataset` | Download dataset |
| `hf download REPO_ID --revision BRANCH` | Download specific revision |

## Upload

| Command | Description |
|---------|-------------|
| `hf upload REPO_ID . .` | Upload current directory |
| `hf upload REPO_ID SRC DST` | Upload specific file |
| `hf upload REPO_ID --repo-type dataset` | Upload as dataset |
| `hf upload REPO_ID --create-pr` | Upload as pull request |
| `hf upload REPO_ID --commit-message MSG` | Custom commit message |

## Repository Management

| Command | Description |
|---------|-------------|
| `hf repo create NAME` | Create model repo |
| `hf repo create NAME --private` | Create private repo |
| `hf repo create NAME --repo-type dataset` | Create dataset repo |
| `hf repo create NAME --space_sdk gradio` | Create Space |
| `hf repo delete REPO_ID` | Delete repository |
| `hf repo settings REPO_ID --private true` | Change visibility |

## Cache Management

| Command | Description |
|---------|-------------|
| `hf cache ls` | List cached repos |
| `hf cache ls --revisions` | Show revision details |
| `hf cache rm REPO_OR_REV` | Remove from cache |
| `hf cache prune` | Remove detached caches |
| `hf cache verify` | Verify cache integrity |

## Search

| Command | Description |
|---------|-------------|
| `hf models ls` | List models |
| `hf models ls --search QUERY` | Search models |
| `hf models info MODEL_ID` | Model details |
| `hf datasets ls` | List datasets |
| `hf datasets info DATASET_ID` | Dataset details |
| `hf spaces ls` | List spaces |

## Jobs

| Command | Description |
|---------|-------------|
| `hf jobs run SCRIPT` | Run a job |
| `hf jobs run SCRIPT --flavor GPU` | Run with specific hardware |
| `hf jobs ps` | List running jobs |
| `hf jobs logs JOB_ID` | View job logs |
| `hf jobs cancel JOB_ID` | Cancel a job |

## Environment

| Command | Description |
|---------|-------------|
| `hf env` | Show environment info |
