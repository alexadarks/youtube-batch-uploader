# YouTube Batch Uploader

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)]()

# 🎬 YouTube Batch Uploader

**Stop uploading videos one by one. Upload 100+ videos with metadata, scheduling, and automatic retries.**

Automate your YouTube uploads with a beautiful Excel preview, intelligent scheduling, and zero manual intervention. Perfect for podcasters, content creators, stock footage managers, and anyone with a large video library.

---

## ✨ What It Does

| Feature | Benefit |
|---------|---------|
| 📋 **Preview Spreadsheet** | Auto-generated Excel with thumbnails + editable metadata |
| ⏰ **Smart Scheduling** | Upload videos automatically every N minutes |
| 🔀 **Flexible Ordering** | Sequential or random (looks organic, not "batch-dumped") |
| 🛡️ **Automatic Retry** | Failed uploads retry up to 3 times automatically |
| ✅ **Progress Tracking** | Real-time status in JSON queue |
| 🚀 **No Coding Required** | CLI commands + Claude Scheduled Tasks |

---

## 🎯 Perfect For

- 🎙️ **Podcasters** — Upload 100+ episodes with consistent metadata
- 📸 **Stock Footage Creators** — Batch upload with searchable descriptions
- 🎬 **Reels Creators** — Convert TikTok/Instagram reels → YouTube automatically
- 📺 **Live Streamers** — Auto-upload archived streams with timestamps
- 🎓 **Course Creators** — Publish lecture videos in bulk

---

## 🚀 Quick Start (5 Minutes)

### 1️⃣ Install

```bash
git clone https://github.com/alexadarks/youtube-batch-uploader.git
cd youtube-batch-uploader
pip install -r requirements.txt
```

### 2️⃣ Get Connection ID

1. Go to **[YouTubeStudioMCP.com](https://YouTubeStudioMCP.com)**
2. Sign in → Authorize → Copy Connection ID
3. Save it (you'll need it soon)

### 3️⃣ Configure

```bash
cp config.example.yaml config.yaml
# Edit with your Connection ID, video folder path, preferences
```

### 4️⃣ Generate Preview

```bash
python3 scripts/build_preview_spreadsheet.py \
  "/path/to/videos" \
  "./videos_preview.xlsx"
```

Open Excel → Fill in **Title** for each video → Save

### 5️⃣ Build Queue

```bash
python3 scripts/build_upload_queue.py \
  "./videos_preview.xlsx" \
  "/path/to/videos" \
  "YOUR_CONNECTION_ID" \
  "./upload_queue.json"
```

### 6️⃣ Schedule Uploads

Ask Claude:
> "Set up a scheduled task that uploads videos from my queue every 30 minutes."

✅ **Done!** Videos upload automatically.

---

## 📚 Documentation

**[📖 Start Here: Full Docs Index](INDEX.md)**

| Document | Time | For |
|----------|------|-----|
| [QUICKSTART.md](QUICKSTART.md) | 5 min | Impatient people |
| [SETUP.md](SETUP.md) | 15 min | First-time setup |
| [examples/WORKFLOW.md](examples/WORKFLOW.md) | 25 min | Complete guide with troubleshooting |



---

## 🎯 Why Use This?

| Without This | With This |
|--------------|-----------|
| ⏱️ Upload 100 videos = 5+ hours manual work | ⚡ Same upload = 5 min setup |
| 😴 Click, wait, repeat, click, wait, repeat | 🤖 Set it & forget it |
| 📝 Metadata scattered across notes | 📊 All in one Excel file |
| ❌ Upload fails? Start over manually | ✅ Auto-retry up to 3x |
| 🎲 Upload order = random | 🎯 Control exact order |

**Real example:** 50 Instagram Reels → YouTube

```
0:00   ✅ Videos 1-3 uploaded
0:30   ✅ Videos 4-6 uploaded  
1:00   ✅ Videos 7-9 uploaded
...
~4:30  ✅ All 50 uploaded
5:00   🎉 Done, task stops automatically
```

---

## 🔧 Configuration

Copy and customize:

```bash
cp config.example.yaml config.yaml
```

```yaml
youtube:
  connection_id: "abc123xyz789"  # From YouTubeStudioMCP.com
  channel_name: "My Channel"
  privacy_status: "public"  # public, unlisted, private

upload:
  batch_size: 3              # 3 videos per batch
  interval_minutes: 30       # Every 30 minutes
  order: "shuffle"           # Random = organic, not batch-dumped
  
paths:
  video_directory: "/Users/you/Videos/my-reels"
  preview_spreadsheet: "./videos_preview.xlsx"
  upload_queue: "./upload_queue.json"
```

---

## 📊 Preview Spreadsheet

Your Excel file looks like this:

| # | Preview | Filename | Date | Title | Description |
|---|---------|----------|------|-------|-------------|
| 1 | 🖼️ | video1.mp4 | 2024-01-15 | **YOU FILL THIS** | **YOU FILL THIS** |
| 2 | 🖼️ | video2.mp4 | 2024-01-16 | **YOU FILL THIS** | **YOU FILL THIS** |
| 3 | 🖼️ | video3.mp4 | 2024-01-17 | **YOU FILL THIS** | **YOU FILL THIS** |

- 🖼️ **Preview** = Auto-generated thumbnail
- ✏️ **Title & Description** = You edit these
- Dates auto-extracted from filename

---

## 🚨 Common Issues & Fixes

### No thumbnails?
```bash
rm -rf .preview_thumbs_cache/
python3 scripts/build_preview_spreadsheet.py ...
```

### "Connection ID invalid"?
1. Go to https://YouTubeStudioMCP.com
2. Verify your Connection ID is correct
3. Ask Claude: "List my YouTube channels"

### Videos not uploading?
1. Check internet connection
2. Verify video files are valid
3. Check `upload_queue.json` for errors
4. Make sure Claude MCP is connected

**[Full troubleshooting →](SETUP.md)**

---

## 🎬 Advanced Options

```bash
# Upload slower (better for small channels)
--batch-size 1 --interval 60

# Upload faster (for established channels)
--batch-size 5 --interval 15

# Sequential order (playlist-style)
--order sequential

# Reproducible shuffle (same order every time)
--order shuffle --seed 42
```

---

## 🤝 Contributing

Ideas? Bugs? Want to help?

- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) — Code overview
- **Planned:** Linux/Windows support, web UI, other platforms

---

## 📄 License

**MIT** — Use freely, commercially or personally. See [LICENSE](LICENSE).

---

## 🌍 Languages

- 🇬🇧 English (this file)
- 🇪🇸 [Spanish / Español](README.es.md)

---

## 🚀 Next Steps

1. **[Quick Start (5 min) →](QUICKSTART.md)**
2. **[Full Setup (15 min) →](SETUP.md)**  
3. **[Complete Workflow (25 min) →](examples/WORKFLOW.md)**
4. **[GitHub Repo →](https://github.com/alexadarks/youtube-batch-uploader)**

---

## 💡 Tips for Creators

### Organize your videos
```
video_2024-01-15_tips.mp4       ← Date auto-extracted
content_2024-01-16_recipe.mp4   ← Date auto-extracted
episode_final.mp4               ← No date found
```

### Upload in waves
Divide 200 videos into 4 batches of 50, upload weekly → looks natural

### Adjust pacing
- Small channel? 1 video per hour
- Established channel? 5 videos per 15 min

### Reuse metadata
The Excel file remembers your previous titles → edit and rebuild → same metadata preserved

---

**Made with ❤️ for content creators.**

*Because uploading 100 videos manually is not a personality trait.*


