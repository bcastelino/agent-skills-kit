---
name: example-skill
description: Example skill for downloading videos from common platforms for offline viewing, editing, or archival.
license: MIT
metadata: {version: "1.0.0", tags: [video, download, media]}
---

# Example Skill: Video Downloader

## When to Use
- Save a video for offline viewing
- Archive a webinar or conference talk
- Download your own content for editing
- Extract audio from a video

## What This Skill Does
1. Clarifies the target platform and URL
2. Collects preferred quality and format
3. Provides a safe, permission-aware workflow
4. Produces a local file with a clear name

## Required Inputs
- Video URL
- Preferred quality (example: 720p, 1080p)
- Preferred format (example: mp4, webm, mp3)
- Output folder (optional)

## How to Use

### Single Video
"Download this video in 1080p MP4: https://example.com/video"

### Audio Only
"Download the audio as MP3 from https://example.com/video"

### Batch
"Download these videos in 720p: [url1], [url2], [url3]"

## Output Format
- A short summary of what will be downloaded
- The chosen quality and format
- The expected filename and save location

## Safety and Compliance
- Only download content you own or have permission to use
- Follow platform terms of service and local laws
- Do not redistribute copyrighted media without rights

## Tips
- Use lower quality for smaller files
- Prefer audio-only for podcasts
- Keep downloads organized by folder

## Common Use Cases
- Offline study
- Content backup
- Editing or remixing your own content
