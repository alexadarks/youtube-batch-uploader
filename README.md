# YouTube Batch Uploader

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)]()

Automate batch uploading of video files to YouTube with a preview spreadsheet and intelligent scheduling. Upload hundreds of videos paced over time instead of all at once. Using Claude Code

## Features

- 📋 **Preview Spreadsheet**: Auto-generate Excel sheets with video thumbnails for easy metadata entry
- 📅 **Smart Scheduling**: Upload videos in batches at configurable intervals (e.g., 3 videos every 30 minutes)
- 🎬 **Flexible Ordering**: Sequential or randomized upload order (useful to avoid "batch dump" appearance)
- 🔄 **Automatic Retry**: Built-in retry logic with exponential backoff
- 🎯 **Selective Upload**: Mark videos to skip or re-upload
- 📊 **Progress Tracking**: Real-time queue status and upload metrics

## Prerequisites

- Python 3.8+
- macOS (for Quick Look thumbnail generation)
- YouTube channel with API access
- Claude with YouTube Studio MCP connected

## Quick Start

### 1. Setup MCP Connection

Follow these steps to connect YouTube Studio MCP to your Claude account:

#### Option A: Via YouTubeStudioMCP.com (Recommended)
1. Visit https://YouTubeStudioMCP.com
2. Sign in with your Google account
3. Authorize access to your YouTube channel
4. Copy your connection ID
5. Save it for the configuration step

#### Option B: Via Claude's MCP Settings
1. Open Claude and go to Settings → Connected Accounts
2. Search for "YouTube Studio"
3. Click "Connect" and sign in with your Google account
4. Authorize the requested permissions
5. Note your channel name or connection ID

### 2. Install Dependencies

```bash
git clone https://github.com/yourusername/youtube-batch-uploader.git
cd youtube-batch-uploader
pip install -r requirements.txt
```

### 3. Configure Your Setup

```bash
cp config.example.yaml config.yaml
# Edit config.yaml with your video folder path and channel info
```

### 4. Run the Workflow

```bash
# Step 1: Generate preview spreadsheet
python3 scripts/build_preview_spreadsheet.py \
  "/path/to/videos" \
  "./videos_preview.xlsx"

# Step 2: Fill in titles/descriptions in the spreadsheet, then:
python3 scripts/build_upload_queue.py \
  "./videos_preview.xlsx" \
  "/path/to/videos" \
  "YOUR_CONNECTION_ID" \
  "./upload_queue.json" \
  --privacy public \
  --order shuffle \
  --batch-size 3
```

## Workflow Overview

### Step 1: Generate Preview Spreadsheet
Creates an Excel file with:
- Video filename
- Extracted date (if present in filename)
- Auto-generated thumbnail (via macOS Quick Look)
- Empty Title/Description columns for you to fill

**Script**: `build_preview_spreadsheet.py`

```bash
python3 scripts/build_preview_spreadsheet.py <video_dir> <output_xlsx>
```

Thumbnails are cached in `.preview_thumbs_cache/` so subsequent runs are fast.

### Step 2: Add Metadata
Open the generated Excel file and:
- Fill in **Title** for each video
- Fill in **Description** (optional but recommended)
- Leave rows blank to skip them
- Save the file

### Step 3: Build Upload Queue
Converts the spreadsheet into a queue JSON that the scheduled task will consume.

**Script**: `build_upload_queue.py`

```bash
python3 scripts/build_upload_queue.py <xlsx_path> <video_dir> <connection_id> <out_json> \
  --privacy public \
  --order shuffle \
  --batch-size 3
```

**Options:**
- `--privacy`: `public`, `unlisted`, or `private` (default: `public`)
- `--order`: `sequential` or `shuffle` (default: `shuffle`)
- `--batch-size`: videos per batch (default: `3`)
- `--seed`: optional seed for reproducible shuffle

### Step 4: Schedule Uploads
Set up a recurring task with your Claude scheduled-tasks MCP to process the queue automatically.

## Configuration

### config.yaml

```yaml
youtube:
  # Your YouTube connection ID from YouTubeStudioMCP.com
  connection_id: "YOUR_CONNECTION_ID"
  # Channel title to validate before uploading
  channel_name: "My Channel"
  # Privacy: public, unlisted, private
  privacy_status: "public"

upload:
  # Batch size (videos per run)
  batch_size: 3
  # Interval in minutes between batches
  interval_minutes: 30
  # Order: sequential or shuffle
  order: "shuffle"
  # Random seed (optional, for reproducible shuffle)
  seed: null

paths:
  # Folder containing .mp4 files
  video_directory: "/path/to/videos"
  # Where to save preview spreadsheet
  preview_spreadsheet: "./videos_preview.xlsx"
  # Where to save upload queue
  upload_queue: "./upload_queue.json"
  # Cache for thumbnails
  thumbnail_cache: "./.preview_thumbs_cache"
```

## Column Details

### Preview Spreadsheet Columns

| Column | Purpose | Editable |
|--------|---------|----------|
| # | Row number | No |
| Preview | Thumbnail image | No |
| Filename | Video filename | No |
| Date | Extracted from filename (YYYY-MM-DD) | No |
| Title | Video title (required) | **Yes** |
| Description | Video description (optional) | **Yes** |

## Pitfalls & Solutions

### ⚠️ File Format Confusion (.xlsx vs .numbers)

**Problem**: On macOS, opening an Excel file with Numbers.app can auto-convert it to `.numbers` format, breaking the scripts.

**Solution**: 
- Don't edit the file manually if possible
- If converted to `.numbers`, manually convert back to `.xlsx` (Right-click → Export as Excel)
- Or use CLI: `python3 scripts/build_preview_spreadsheet.py` to rebuild from scratch

### ⚠️ Deleting Rows from Spreadsheet

**Problem**: Deleting rows manually or via `openpyxl.delete_rows()` can desync images from filenames.

**Solution**:
- Always rebuild the spreadsheet using the script
- Mark videos as "Title/Description: [SKIP]" then filter them out when building the queue
- Or simply remove the .mp4 files from disk and rebuild

### ⚠️ Empty Titles/Descriptions

**Problem**: Videos uploading with missing metadata.

**Solution**: The script warns about empty titles. Either:
- Fill them in before building the queue
- Use the filename as a fallback (scripts can auto-fill)

### ⚠️ Upload Failures

**Problem**: Video upload fails, need to retry.

**Solution**: 
- Queue has built-in retry logic (up to 3 attempts per video)
- Failed videos show in `upload_queue.json` with `error` field
- Scheduled task automatically retries until attempts = 3

### ⚠️ Large Video Files

**Problem**: Timeout or bandwidth issues uploading huge files.

**Solution**:
- Reduce batch size (e.g., 1-2 videos per batch)
- Increase interval between batches
- Upload videos sequentially at different times of day

## Using with Claude Scheduled Tasks

Once you have `upload_queue.json`, create a scheduled task with Claude to automatically process batches:

```bash
# Example cron (every 30 minutes)
*/30 * * * *

# Task runs:
python3 scripts/scheduled_upload_worker.py <path-to-upload-queue.json> <connection-id>
```

The worker script:
1. Reads the queue file
2. Uploads next batch of videos
3. Updates queue with results
4. Disables itself when complete

## Troubleshooting

### No thumbnails generated
- Ensure you're on macOS (uses `qlmanage`)
- Check that video files are valid: `file video.mp4`
- Clear cache and retry: `rm -rf .preview_thumbs_cache/`

### "Connection ID not found"
- Verify connection ID from YouTubeStudioMCP.com
- Test connection: Ask Claude to list your YouTube channels via the MCP

### Videos not uploading
- Check internet connection
- Verify video file sizes (YouTube has limits)
- Review `upload_queue.json` for error messages
- Ensure channel still has upload quota

### Spreadsheet not updating
- Clear local cache: `rm upload_queue.json`
- Rebuild spreadsheet with `--thumb-cache` flag pointing to a fresh directory
- Check file permissions: `ls -la videos_preview.xlsx`

## Requirements

See `requirements.txt`:

```
openpyxl>=3.0.0
Pillow>=9.0.0
```

## License

MIT

## Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch
3. Test your changes
4. Submit a PR

## Support

- 📖 See `examples/` for step-by-step workflows
- 🐛 Open an issue for bugs
- 💡 Discussions for feature requests
