# Project Structure

```
youtube-batch-uploader/
│
├── README.md                    # Main documentation (start here)
├── SETUP.md                     # Detailed setup instructions
├── GITHUB_SETUP.md             # How to publish to GitHub
├── CONTRIBUTING.md             # Contributing guidelines
├── LICENSE                     # MIT License
├── requirements.txt            # Python dependencies
│
├── config.example.yaml         # Configuration template (copy to config.yaml)
├── .gitignore                  # Git ignore rules
│
├── scripts/                    # Python scripts
│   ├── build_preview_spreadsheet.py
│   │   └── Creates Excel with video thumbnails and metadata
│   │
│   ├── build_upload_queue.py
│   │   └── Converts spreadsheet to upload queue JSON
│   │
│   └── scheduled_upload_worker.py
│       └── Processes upload queue batches (for scheduled tasks)
│
├── examples/                   # Example workflows and documentation
│   ├── WORKFLOW.md            # Complete step-by-step guide
│   └── ... (future examples)
│
└── .github/                    # GitHub configuration
    └── workflows/              # GitHub Actions (future CI/CD)
```

## File Descriptions

### Root Documentation

| File | Purpose |
|------|---------|
| **README.md** | Overview, features, quick start |
| **SETUP.md** | Detailed setup guide with troubleshooting |
| **GITHUB_SETUP.md** | How to create GitHub repo and push code |
| **CONTRIBUTING.md** | Guidelines for contributors |
| **LICENSE** | MIT License (permissive, great for open source) |

### Configuration

| File | Purpose |
|------|---------|
| **config.example.yaml** | Template - copy to config.yaml and customize |
| **.gitignore** | Prevents committing: config.yaml, *.xlsx, upload_queue.json, thumbnails |

### Scripts (`scripts/`)

#### build_preview_spreadsheet.py
- **Purpose**: Generate Excel file with video thumbnails
- **Input**: Video folder path
- **Output**: Excel file (.xlsx) with embedded thumbnails
- **Cached**: Thumbnails stored in `.preview_thumbs_cache/` for fast reruns
- **Smart**: Preserves existing Title/Description when rebuilding

#### build_upload_queue.py
- **Purpose**: Convert spreadsheet → upload queue
- **Input**: Excel file, video folder, connection ID
- **Output**: JSON queue file (upload_queue.json)
- **Options**: Privacy level, batch size, shuffle/sequential order
- **Validation**: Warns about missing metadata

#### scheduled_upload_worker.py
- **Purpose**: Process next batch from queue
- **Input**: Queue JSON file
- **Output**: Updated queue with progress
- **Flow**: Read batch → Upload → Update queue → Report
- **Note**: Called by scheduled task, fully self-contained

### Examples (`examples/`)

#### WORKFLOW.md
Complete walkthrough covering:
1. Setup (one-time)
2. Generate preview spreadsheet
3. Fill in metadata
4. Build upload queue
5. Schedule uploads
6. Monitor progress
7. Troubleshooting

Includes timeline examples and handling edge cases.

## Dependencies

File: `requirements.txt`

```
openpyxl>=3.0.0      # Excel file creation/reading
Pillow>=9.0.0        # Image processing (thumbnails)
PyYAML>=6.0          # Configuration file parsing
```

## Generated Files (Not Committed)

These files are created during use but excluded from git:

- `config.yaml` - Your configuration (contains connection ID)
- `*.xlsx` - Spreadsheets you create
- `*.numbers` - If Numbers.app converts xlsx files
- `upload_queue.json` - Upload progress tracking
- `.preview_thumbs_cache/` - Cached thumbnail images
- `*.log` - Log files (if added later)

## Workflow Data Flow

```
Video Files (.mp4)
       ↓
build_preview_spreadsheet.py
       ↓
videos_preview.xlsx (with thumbnails)
       ↓ (user fills in Title/Description)
       ↓
build_upload_queue.py
       ↓
upload_queue.json
       ↓
scheduled_upload_worker.py (via Claude scheduled task)
       ↓
YouTube (videos uploaded)
       ↓
upload_queue.json (updated with status)
```

## Configuration Hierarchy

1. **config.example.yaml** - Template (never modified)
2. **config.yaml** - Your personal config (created by you, not committed)
3. **Command-line args** - Override config values when running scripts

## Future Improvements

Possible additions (not yet implemented):

- [ ] GitHub Actions workflow for testing
- [ ] Support for other video platforms (Vimeo, Rumble)
- [ ] Web UI for metadata entry
- [ ] Support for Linux/Windows (currently macOS only for thumbnails)
- [ ] Direct integration with Claude MCP (no separate scripts)
- [ ] Database for tracking upload history
- [ ] Thumbnail generation with ffmpeg as fallback

## Development

To contribute:

1. Fork the repo
2. Make changes
3. Test thoroughly
4. Follow PEP 8 style
5. Submit PR

See CONTRIBUTING.md for details.

---

**Current Status**: Production-ready for macOS users with YouTube channels
**Last Updated**: July 2024
