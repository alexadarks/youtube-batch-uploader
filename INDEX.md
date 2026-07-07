# YouTube Batch Uploader - Complete Documentation Index

Welcome! This is a complete, production-ready project for batch uploading videos to YouTube.

## Start Here

**First time?** Read in this order:

1. **[README.md](README.md)** - Overview and features (5 min)
2. **[SETUP.md](SETUP.md)** - Installation and configuration (10 min)
3. **[examples/WORKFLOW.md](examples/WORKFLOW.md)** - Complete step-by-step guide (20 min)

## All Documentation

### For Users

| Document | Time | Purpose |
|----------|------|---------|
| [README.md](README.md) | 5 min | Overview, features, quick start |
| [SETUP.md](SETUP.md) | 10 min | Detailed setup and verification |
| [examples/WORKFLOW.md](examples/WORKFLOW.md) | 20 min | Complete workflow walkthrough |
| [config.example.yaml](config.example.yaml) | 5 min | Configuration reference |

### For Developers

| Document | Purpose |
|----------|---------|
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Code organization and file descriptions |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute changes |
| [GITHUB_SETUP.md](GITHUB_SETUP.md) | How to publish to GitHub |

### Reference

| Document | Purpose |
|----------|---------|
| [LICENSE](LICENSE) | MIT License terms |
| [requirements.txt](requirements.txt) | Python dependencies |
| [.gitignore](.gitignore) | Files to exclude from git |

## Quick Links

- 📁 **Scripts** → [scripts/](scripts/)
  - `build_preview_spreadsheet.py` - Generate thumbnail preview
  - `build_upload_queue.py` - Create upload queue
  - `scheduled_upload_worker.py` - Process batches

- 📚 **Examples** → [examples/](examples/)
  - `WORKFLOW.md` - Step-by-step guide

- ⚙️ **Configuration** → [config.example.yaml](config.example.yaml)
  - Copy to `config.yaml` and customize

## Common Tasks

### I want to...

**Upload videos to YouTube**
→ Follow [WORKFLOW.md](examples/WORKFLOW.md)

**Set up YouTube connection**
→ See [SETUP.md](SETUP.md) "Getting Your YouTube Connection ID"

**Understand what this does**
→ Read [README.md](README.md) and [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

**Fix an issue**
→ Check troubleshooting in [README.md](README.md) and [SETUP.md](SETUP.md)

**Contribute improvements**
→ See [CONTRIBUTING.md](CONTRIBUTING.md)

**Publish to GitHub**
→ Follow [GITHUB_SETUP.md](GITHUB_SETUP.md)

## Key Features

✅ **Batch Upload** - Upload dozens/hundreds of videos automatically
✅ **Metadata Management** - Excel preview with thumbnails
✅ **Smart Scheduling** - Uploads paced over time (not "batch dump")
✅ **Automatic Retry** - Failed videos retry up to 3 times
✅ **Progress Tracking** - Real-time status via JSON queue
✅ **Flexible Options** - Privacy levels, batch sizes, orderings

## System Requirements

- **Python**: 3.8+
- **OS**: macOS (for Quick Look thumbnails)
- **YouTube**: Channel with API access
- **Claude**: With YouTube Studio MCP connected

## Getting Help

1. Check the **Troubleshooting** section in [README.md](README.md)
2. Review **Common Issues** in [SETUP.md](SETUP.md)
3. Open an issue on GitHub with details

## Next Steps

1. Copy this folder somewhere safe
2. Follow [SETUP.md](SETUP.md) to install dependencies
3. Get your connection ID from https://YouTubeStudioMCP.com
4. Create `config.yaml` from `config.example.yaml`
5. Follow [WORKFLOW.md](examples/WORKFLOW.md) to upload!

---

**Version**: 1.0
**License**: MIT
**Platform**: macOS
**Python**: 3.8+
