# Quick Start (5 Minutes)

Already familiar with the concept? Fast path to uploading.

## 1. Prerequisites

- [ ] YouTube channel
- [ ] Connection ID from https://YouTubeStudioMCP.com
- [ ] Python 3.8+
- [ ] Folder with .mp4 files

## 2. Install

```bash
git clone https://github.com/yourusername/youtube-batch-uploader.git
cd youtube-batch-uploader
pip install -r requirements.txt
```

## 3. Configure

```bash
cp config.example.yaml config.yaml
# Edit config.yaml with your paths and connection ID
```

## 4. Generate Preview

```bash
python3 scripts/build_preview_spreadsheet.py \
  "/path/to/videos" \
  "./videos_preview.xlsx"
```

Open `videos_preview.xlsx` and fill in **Title** for each video.

## 5. Build Queue

```bash
python3 scripts/build_upload_queue.py \
  "./videos_preview.xlsx" \
  "/path/to/videos" \
  "YOUR_CONNECTION_ID" \
  "./upload_queue.json" \
  --privacy public \
  --order shuffle \
  --batch-size 3
```

## 6. Schedule Uploads

Ask Claude:

> Set up a scheduled YouTube upload task that processes the queue at `./upload_queue.json` every 30 minutes with connection ID `YOUR_CONNECTION_ID`. Upload 3 videos per batch.

Claude will create the scheduled task and run the first batch immediately.

## Done!

Videos will upload automatically. Monitor progress:

```bash
python3 -c "
import json
q = json.load(open('upload_queue.json'))
uploaded = sum(1 for i in q['items'] if i['uploaded'])
total = len(q['items'])
print(f'Progress: {uploaded}/{total} uploaded')
"
```

---

## Common Options

| Option | Example | Effect |
|--------|---------|--------|
| `--batch-size` | `--batch-size 2` | Upload 2 per batch instead of 3 |
| `--privacy` | `--privacy unlisted` | Upload as unlisted (not public) |
| `--order` | `--order sequential` | Upload in spreadsheet order (not random) |
| `--seed` | `--seed 42` | Reproducible random order |

## Common Issues

| Problem | Solution |
|---------|----------|
| No thumbnails | Verify you're on macOS; check `.preview_thumbs_cache/` |
| "Connection ID invalid" | Verify at https://YouTubeStudioMCP.com |
| Videos not uploading | Check internet; verify config.yaml; ask Claude to test MCP |
| Excel won't open | Delete `.numbers` file if it exists; rebuild with script |

---

**Need more detail?** See [README.md](README.md) or [examples/WORKFLOW.md](examples/WORKFLOW.md)
