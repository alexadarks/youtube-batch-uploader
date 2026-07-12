# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Linux/Windows support (ffmpeg for thumbnail generation)
- Web UI for metadata entry
- Support for other platforms (Vimeo, Rumble)
- Direct Claude MCP integration (no separate scripts)
- Database for upload history & analytics
- Video duration calculation
- Bulk metadata editing features

---

## [1.1.0] - 2024-07-11

### Added
- Spanish translation (README.es.md)
- Creator-focused documentation
- Real-world examples and use cases
- Tips & Tricks section for content creators
- Improved troubleshooting guide
- Language selector in README
- Advanced options documentation

### Changed
- Redesigned README with visual hierarchy
- Enhanced quick start section (now 5 minutes)
- Better emoji usage for visual scanning
- Improved configuration examples
- Clearer feature descriptions

### Fixed
- Documentation clarity in setup steps
- Better error message handling in scripts
- Improved file permission handling

---

## [1.0.0] - 2024-07-11

### Added
- Initial public release
- `build_preview_spreadsheet.py` - Generate Excel preview with thumbnails
- `build_upload_queue.py` - Create upload queue from spreadsheet
- `scheduled_upload_worker.py` - Process batch uploads
- Complete documentation (README, SETUP, WORKFLOW, examples)
- MIT License
- Configuration template
- GitHub setup instructions
- Project structure documentation

### Features
- 📋 Auto-generated Excel preview with thumbnails
- ⏰ Smart scheduling (configurable batch size & interval)
- 🔀 Flexible ordering (sequential or shuffle)
- 🛡️ Automatic retry logic (up to 3 attempts)
- 📊 Real-time progress tracking
- 🎯 Selective upload with metadata management
- 🚀 No coding required (CLI + Claude)

### Documentation
- README.md (English)
- SETUP.md (Installation & Configuration)
- QUICKSTART.md (5-minute fast path)
- examples/WORKFLOW.md (Complete guide)
- PROJECT_STRUCTURE.md (Code overview)
- INDEX.md (Documentation index)
- CONTRIBUTING.md (Contribution guidelines)

---

## Legend

- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Now removed features
- **Fixed** - Any bug fixes
- **Security** - In case of vulnerabilities

---

## Version Roadmap

### v1.2 (Next)
- [ ] Screenshot gallery in README
- [ ] More creator-specific examples
- [ ] Video duration calculation
- [ ] Playlist management

### v2.0 (Future)
- [ ] Web UI
- [ ] Multi-platform support
- [ ] Database backend
- [ ] Analytics dashboard

---

**Latest version:** 1.1.0  
**Released:** July 11, 2024  
**Maintained by:** [alexadarks](https://github.com/alexadarks)
