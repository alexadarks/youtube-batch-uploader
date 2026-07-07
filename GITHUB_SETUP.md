# Pushing to GitHub

Follow these steps to publish your `youtube-batch-uploader` project to GitHub.

## Prerequisites

- GitHub account (create one at https://github.com if you don't have it)
- Git installed (`brew install git` on macOS)
- Terminal access

## Step 1: Initialize Local Git Repository

```bash
cd /path/to/youtube-batch-uploader
git init
git add .
git commit -m "Initial commit: youtube-batch-uploader"
```

## Step 2: Create GitHub Repository

### Option A: Via Web (Recommended)

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `youtube-batch-uploader`
   - **Description**: "Automate batch uploading of videos to YouTube with scheduling and metadata management"
   - **Public** (to share with others)
   - **Add a README**: ❌ (you already have one)
   - **Add .gitignore**: ❌ (you already have one)
   - **Choose a license**: ❌ (you already have one)
3. Click "Create repository"
4. Copy the repository URL (should be `https://github.com/yourusername/youtube-batch-uploader.git`)

### Option B: Via GitHub CLI

```bash
brew install gh  # if you don't have it
gh auth login    # sign in with your account
gh repo create youtube-batch-uploader --public --source=. --remote=origin --push
```

## Step 3: Connect and Push to GitHub

```bash
# Add remote (replace with your actual URL)
git remote add origin https://github.com/yourusername/youtube-batch-uploader.git

# Verify it's connected
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Verify on GitHub

1. Go to https://github.com/yourusername/youtube-batch-uploader
2. You should see:
   - All your files and folders
   - README.md displayed on the homepage
   - License information
   - File list

## Step 5: Add GitHub Metadata (Optional)

In your repository settings at GitHub:

1. Go to **Settings** → **General**
2. Add:
   - **About** description
   - **Topics**: `youtube`, `automation`, `video-upload`, `batch-upload`, `scheduler`
3. Go to **Settings** → **Pages** (to enable GitHub Pages if desired)

## Step 6: Sharing

Your project is now public and shareable:

```
Link: https://github.com/yourusername/youtube-batch-uploader
Clone: git clone https://github.com/yourusername/youtube-batch-uploader.git
```

## Updating Your Repository

Whenever you make changes locally:

```bash
# Make your changes
# ... edit files ...

# Commit
git add .
git commit -m "Description of changes"

# Push
git push origin main
```

## Adding a Release (Optional)

To create a release for v1.0:

```bash
# Tag your version
git tag -a v1.0 -m "First release"

# Push tags
git push origin v1.0
```

Or via GitHub web interface:
1. Go to your repo
2. Click "Releases" 
3. Click "Create a new release"
4. Fill in version, title, and description

## Next Steps

- Add GitHub Issues for bugs/features
- Add GitHub Discussions for questions
- Consider adding GitHub Actions for CI/testing
- Monitor issues and PRs from other users

## .gitignore Reminder

Your `.gitignore` already excludes:
- `config.yaml` (your connection ID)
- `*.xlsx`, `*.numbers` (spreadsheets)
- `upload_queue.json` (queue state)
- `.preview_thumbs_cache/` (thumbnails)

This is good - don't commit these files!

---

Once published, other people can use your project by:

```bash
git clone https://github.com/yourusername/youtube-batch-uploader.git
cd youtube-batch-uploader
pip install -r requirements.txt
cp config.example.yaml config.yaml
# ... follow SETUP.md ...
```
