# Detailed Setup Guide

## Getting Your YouTube Connection ID

### Step 1: Visit YouTubeStudioMCP.com

1. Open https://YouTubeStudioMCP.com in your browser
2. You'll see the YouTube Studio MCP interface

### Step 2: Authenticate

1. Click "Sign in with Google"
2. Select the Google account associated with your YouTube channel
3. Review the permissions requested (read/write access to channel data)
4. Click "Authorize" or "Allow"

### Step 3: Get Your Connection ID

After authorization, you'll see:
```
Connected Channels:
- Channel Name: "My Awesome Channel"
  Connection ID: abc123xyz789...
```

**Copy the Connection ID** - you'll need this for the configuration.

> **Note**: Connection IDs don't expire, but can change if you reconnect. Keep it somewhere safe.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-batch-uploader.git
cd youtube-batch-uploader
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `openpyxl` - Excel file manipulation
- `Pillow` - Image processing (for thumbnails)
- `PyYAML` - Configuration file parsing

## Configuration

### 1. Create Configuration File

```bash
cp config.example.yaml config.yaml
```

### 2. Edit config.yaml

Open `config.yaml` and update:

```yaml
youtube:
  # REQUIRED: Paste your connection ID from YouTubeStudioMCP.com
  connection_id: "YOUR_CONNECTION_ID_HERE"
  
  # REQUIRED: Your YouTube channel name (for validation)
  channel_name: "My Channel Name"
  
  # Optional: privacy setting (public, unlisted, private)
  privacy_status: "public"

upload:
  # Recommended: 3 (balanced for stability and speed)
  batch_size: 3
  
  # Recommended: 30 (uploads look organic, not batch-dumped)
  interval_minutes: 30
  
  # Recommended: "shuffle" for natural distribution
  order: "shuffle"

paths:
  # REQUIRED: Full path to your videos folder
  # Use absolute path (not ~)
  video_directory: "/Users/yourname/Videos/my-reels"
  
  # Optional: where to save preview spreadsheet
  preview_spreadsheet: "./videos_preview.xlsx"
  
  # Optional: where to save upload queue
  upload_queue: "./upload_queue.json"
  
  # Optional: thumbnail cache location
  thumbnail_cache: "./.preview_thumbs_cache"
```

### 3. Verify Configuration

```bash
# Check that Python can read your config
python3 -c "import yaml; print(yaml.safe_load(open('config.yaml')))"
```

## Verifying Your Setup

### Check Video Folder

```bash
# List MP4 files to verify
ls -la /path/to/your/videos/*.mp4 | wc -l
```

Should show your video count.

### Test Thumbnail Generation

```bash
# Generate preview spreadsheet (will be slow on first run)
python3 scripts/build_preview_spreadsheet.py \
  "/path/to/your/videos" \
  "./test_preview.xlsx"

# Should create test_preview.xlsx with thumbnails
ls -lh test_preview.xlsx
ls -lh .preview_thumbs_cache/
```

### Test Queue Generation

```bash
# Build a test queue
python3 scripts/build_upload_queue.py \
  "./test_preview.xlsx" \
  "/path/to/your/videos" \
  "YOUR_CONNECTION_ID" \
  "./test_queue.json" \
  --batch-size 2 \
  --privacy unlisted

# Should create test_queue.json
cat test_queue.json | python3 -m json.tool | head -30
```

### Test Claude Connection

In Claude, ask:

> Using the YouTube Studio MCP, list all connected channels and show me the channel titles and connection IDs.

You should see your channel listed with a matching connection ID.

## Next Steps

Once setup is verified:

1. Read `examples/WORKFLOW.md` for the complete workflow
2. Start with a small batch (3-5 videos) as a test
3. Once comfortable, upload your full batch

## Troubleshooting Setup

### "No module named 'openpyxl'"

```bash
pip install -r requirements.txt
# or
pip install openpyxl Pillow PyYAML
```

### "qlmanage: command not found"

Thumbnail generation requires macOS. If on Linux/Windows, you'll need to:
1. Modify the script to use ffmpeg instead
2. Or use manual thumbnails
3. Or run on macOS

### "Video directory not found"

Double-check the path:
```bash
# Verify it exists
ls -la "/path/to/your/videos"

# In config.yaml, use full path:
# ❌ Wrong: ~/Videos/reels
# ✅ Right: /Users/yourname/Videos/reels
```

### "Connection ID invalid"

1. Verify you copied it correctly from YouTubeStudioMCP.com
2. In Claude, confirm the MCP is connected and list channels
3. Try reconnecting at YouTubeStudioMCP.com

### No .mp4 files found

```bash
# Check file extensions
ls "/path/to/your/videos/" | grep -i ".mp4"

# Convert if needed (outside this tool)
```

## Security Notes

- `config.yaml` contains your connection ID - don't commit it to git
- Add to `.gitignore` (already included)
- Never share your connection ID publicly
- Videos are private until you mark them public in settings

## Getting Help

- Check `README.md` for overview
- Read `examples/WORKFLOW.md` for step-by-step
- Review `TROUBLESHOOTING` section in README
