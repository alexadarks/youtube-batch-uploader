# Complete YouTube Batch Upload Workflow

This guide walks through a complete batch upload from start to finish.

## Scenario

You have 50 video files in a folder that you want to upload to YouTube. You want:
- Custom title and description for each
- To upload 3 videos every 30 minutes (so ~5 hours total)
- Videos in random order (to avoid "batch dump" appearance)
- To be able to check progress at any time

## Step 1: Setup (One-Time)

### 1a. Get Your YouTube Connection ID

1. Go to https://YouTubeStudioMCP.com
2. Click "Sign in with Google"
3. Select your YouTube account
4. Grant access when prompted
5. You'll see your **Connection ID** - copy it

> **Alternative**: In Claude, ask it to list your YouTube channels using the MCP. It will show your channel info including connection details.

### 1b. Install & Configure

```bash
git clone https://github.com/yourusername/youtube-batch-uploader.git
cd youtube-batch-uploader
pip install -r requirements.txt

# Copy and edit configuration
cp config.example.yaml config.yaml

# Edit config.yaml:
# - Set connection_id to what you copied from YouTubeStudioMCP.com
# - Set video_directory to your videos folder
# - Verify other settings
```

Example config:

```yaml
youtube:
  connection_id: "abc123xyz789"
  channel_name: "My Awesome Channel"
  privacy_status: "public"

upload:
  batch_size: 3
  interval_minutes: 30
  order: "shuffle"

paths:
  video_directory: "/Users/alex/Videos/MyReels"
  preview_spreadsheet: "./videos_preview.xlsx"
  upload_queue: "./upload_queue.json"
```

## Step 2: Generate Preview Spreadsheet

This creates an Excel file with thumbnails so you can add titles/descriptions.

```bash
python3 scripts/build_preview_spreadsheet.py \
  "/Users/alex/Videos/MyReels" \
  "./videos_preview.xlsx"
```

**Output:**
- `videos_preview.xlsx` with all videos, thumbnails, and empty Title/Description columns
- `.preview_thumbs_cache/` folder with cached thumbnails

**Expected output:**
```json
{
  "output": "./videos_preview.xlsx",
  "video_count": 50,
  "preserved_captions": 0,
  "dropped_from_previous_sheet": []
}
```

> **First run takes longer** (generates all thumbnails). Subsequent runs are fast since thumbnails are cached.

## Step 3: Fill in Metadata

1. Open `videos_preview.xlsx` with Excel or Google Sheets
2. For each row:
   - Fill in **Title** (required)
   - Fill in **Description** (recommended)
   - Leave blank to skip (don't delete the row!)

> **Pro tip**: Spreadsheet will auto-save. Don't worry if Numbers.app tries to convert it - just close and use CLI to rebuild if needed.

Example:

| # | Filename | Date | Title | Description |
|---|----------|------|-------|-------------|
| 1 | video1.mp4 | 2024-01-15 | Morning Workout Tips | Quick 5-minute routine to start your day |
| 2 | video2.mp4 | 2024-01-16 | Healthy Smoothie | Easy recipe with 3 ingredients |
| 3 | video3.mp4 | 2024-01-17 | [SKIP] | (leave blank to skip upload) |

**Save the file when done.**

## Step 4: Build Upload Queue

Convert the spreadsheet to an upload queue that the scheduler will process.

```bash
python3 scripts/build_upload_queue.py \
  "./videos_preview.xlsx" \
  "/Users/alex/Videos/MyReels" \
  "abc123xyz789" \
  "./upload_queue.json" \
  --privacy public \
  --order shuffle \
  --batch-size 3
```

**Options explained:**
- `--privacy public` - make videos public (alternatives: `unlisted`, `private`)
- `--order shuffle` - randomize order (alternatives: `sequential`)
- `--batch-size 3` - upload 3 videos per batch
- `--seed 42` - (optional) use specific seed for reproducible shuffle

**Expected output:**
```json
{
  "output": "./upload_queue.json",
  "queued": 49,
  "missing_files_skipped": [],
  "empty_title_or_desc": []
}
```

> **If you see "empty_title_or_desc" warnings**, go back to the spreadsheet and fill them in, then rebuild the queue.

## Step 5: Start Scheduled Uploads

Now set up Claude to automatically upload batches at regular intervals.

### Option A: Using Claude Scheduled Tasks (Recommended)

In Claude, create a new scheduled task. Ask Claude to:

> Set up a scheduled task that:
> 1. Runs every 30 minutes
> 2. Processes the YouTube upload queue at `/path/to/upload_queue.json`
> 3. Uses connection ID `abc123xyz789`
> 4. Uploads 3 videos per run
> 5. Reports progress in JSON format
> 6. Automatically disables when complete

Claude will:
- Create the scheduled task
- Run the first batch immediately (so you see proof of concept)
- Continue automatically every 30 minutes

### Option B: Manual Per-Batch Upload

If you prefer manual control, you can also process each batch yourself:

```bash
python3 scripts/scheduled_upload_worker.py "./upload_queue.json" "abc123xyz789"
```

This uploads the next 3 videos and saves progress. Run it manually whenever you want the next batch.

## Step 6: Monitor Progress

### Check Queue Status

```bash
# View current queue state (human-readable)
python3 -c "import json; q = json.load(open('./upload_queue.json')); print(f\"Uploaded: {sum(1 for i in q['items'] if i['uploaded'])}/{len(q['items'])}\")"
```

### Follow Along

The scheduled task will:
- Upload the next batch every 30 minutes
- Show which videos were uploaded
- Report any errors
- Automatically stop when all videos are done

**Timeline example** (for 50 videos, 3 per batch, 30 min interval):
- **0:00** - First 3 videos uploaded
- **0:30** - Next 3 videos uploaded
- **1:00** - Next 3 videos uploaded
- ...
- **~4:30** - Last batch uploaded
- Task automatically disables

## Step 7: Handle Issues

### Some Videos Failed to Upload

The queue has automatic retry logic. Failed videos are retried up to 3 times automatically.

If a video fails 3 times:
1. Check the error in `upload_queue.json`
2. Fix the issue (e.g., too large, bad format)
3. Either:
   - Update the queue file manually and re-run
   - Rebuild the queue from the spreadsheet

### You Want to Stop

1. Disable the scheduled task via Claude
2. No files are deleted; you can resume later by re-running the task

### You Want to Resume Later

All progress is saved in `upload_queue.json`. You can:
1. Stop the current task
2. Come back days later
3. Re-enable the task
4. It picks up where it left off

### You Want to Add More Videos

1. Add new .mp4 files to the video folder
2. Run Step 2 again (rebuild preview spreadsheet)
3. New videos appear in the spreadsheet with prior captions preserved
4. Fill in metadata for new videos
5. Build a new queue file with a different name (e.g., `upload_queue_batch2.json`)
6. Set up a new scheduled task for the new queue

## Troubleshooting

### Spreadsheet won't open / .numbers format error

Numbers.app sometimes auto-converts .xlsx. If this happens:

```bash
# Rebuild from scratch (preserves your captions)
python3 scripts/build_preview_spreadsheet.py \
  "/Users/alex/Videos/MyReels" \
  "./videos_preview.xlsx"
```

### No thumbnails in spreadsheet

1. Verify you're on macOS (uses Quick Look)
2. Check files are valid: `file *.mp4`
3. Clear cache: `rm -rf .preview_thumbs_cache/`
4. Rebuild: `python3 scripts/build_preview_spreadsheet.py ...`

### Videos aren't uploading

1. Verify connection ID is correct
2. Check internet connection
3. In Claude, verify the MCP is connected: "List my YouTube channels"
4. Check video file sizes (YouTube has limits)
5. Review `upload_queue.json` for error messages

### Want to skip/delete a video

**Option 1** (recommended): Leave Title/Description blank, then rebuild queue

**Option 2**: Delete the actual .mp4 file, then rebuild preview spreadsheet

> **Don't manually edit the Excel file** - use the scripts to rebuild for safety

## Next Steps

- Monitor uploads for a few batches to ensure quality
- Adjust settings if needed (slower pace, different privacy levels, etc.)
- Add more videos anytime by repeating the workflow for a new batch

---

**Questions?** See the main README.md for more details and advanced options.
