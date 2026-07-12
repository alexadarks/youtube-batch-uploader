# 🎙️ For Podcasters: Complete Guide

Upload your entire podcast catalog to YouTube with consistent metadata and perfect pacing.

---

## Why YouTube for Podcasts?

- 📈 Expand audience (50% of YouTube viewers also listen to podcasts)
- 🎥 Add video: background visuals, waveforms, slides
- 🔍 Better discoverability (search + recommendations)
- 💰 Monetization opportunities
- 📊 Track views & engagement metrics

---

## Scenario: Upload 100 Podcast Episodes

You have 100 MP3s converted to MP4s (with artwork/visuals). You want them on YouTube with:
- Consistent branding
- Episode numbers in title
- Timestamps in description
- Organized upload (5 episodes per week for 20 weeks)

---

## Step 1: Organize Your Files

```bash
# Name files with episode number for easy sorting
# This makes ordering predictable

episode_001_intro.mp4
episode_002_first_guest.mp4
episode_003_deep_dive.mp4
...
episode_100_anniversary_special.mp4
```

**Why this matters:** Excel preview will show them in order, making metadata entry fast.

---

## Step 2: Generate Preview

```bash
python3 scripts/build_preview_spreadsheet.py \
  "/path/to/podcast/episodes" \
  "./podcast_preview.xlsx"
```

Open the Excel file. You'll see:

| # | Preview | Filename | Date | Title | Description |
|---|---------|----------|------|-------|-------------|
| 1 | 🎙️ | episode_001_intro.mp4 | - | **FILL IN** | **FILL IN** |
| 2 | 🎙️ | episode_002_first_guest.mp4 | - | **FILL IN** | **FILL IN** |

---

## Step 3: Fill Metadata (Template)

For each episode, use this template:

### Title (50-70 chars)
```
Episode 42 - Guest Name | Podcast Title
```

### Description
```
📻 Podcast Name - Episode 42

Guest: [Guest Name]
Topic: [Main topic]

⏱️ Timestamps:
0:00 - Intro
2:30 - Guest intro
5:00 - Main topic
15:00 - Audience questions
20:00 - Closing

🔗 Links:
Spotify: [link]
Apple Podcasts: [link]
Website: [link]

#Podcast #[Topic] #[GuestName]
```

**Pro tip:** Once you've formatted a few, copy/paste and just change the episode number and guest name.

---

## Step 4: Build Queue for Sequential Upload

```bash
python3 scripts/build_upload_queue.py \
  "./podcast_preview.xlsx" \
  "/path/to/podcast/episodes" \
  "YOUR_CONNECTION_ID" \
  "./podcast_queue.json" \
  --privacy public \
  --order sequential \
  --batch-size 1
```

**Why these settings:**
- `--order sequential` - Upload in episode order (listener experience)
- `--batch-size 1` - One episode per batch (controlled rollout)
- `--privacy public` - Discoverable for new listeners

---

## Step 5: Schedule Uploads

Ask Claude:

> "Set up a scheduled task that uploads podcast episodes every 7 days (once per week). Use the queue at `./podcast_queue.json` with connection ID `YOUR_ID`. Upload 1 episode per batch. Notify me when complete."

This uploads:
```
Week 1  - Episodes 1-2 (2 uploaded)
Week 2  - Episodes 3-4 (4 total)
Week 3  - Episodes 5-6 (6 total)
...
Week 50 - Episodes 99-100 (100 total)
```

**Timeline:** 100 episodes spread over 50 weeks = professional, organic upload pattern.

---

## Optimization Tips

### 1. Add Chapter Markers

Include timestamps in description for YouTube chapters:

```
0:00 Intro
2:30 Announcement
5:45 Topic deep dive
15:20 Q&A
22:15 Outro
```

YouTube auto-creates clickable chapters from these timestamps.

### 2. Create Playlists

After some episodes upload, ask Claude:

> "Create a YouTube playlist called 'Podcast Name - All Episodes' and add the uploaded videos."

This helps viewers binge-watch your podcast.

### 3. Consistent Thumbnail

For podcasts, use the same visual template:
- Your podcast logo
- Episode number
- Guest name (if applicable)

This creates brand recognition in search results.

### 4. Series Tags

Use series tags for better recommendation:

```
Description footer:
📺 Subscribe for new episodes every [day]
👉 Podcast Series: [Your Podcast Name]
🔔 Ring the bell for notifications
```

---

## Real Example: 50 Episodes

```
Setup time: 30 minutes
Metadata entry: 2-3 hours (templates save time)
Configuration: 5 minutes
Total manual time: ~3 hours

Without this tool:
50 episodes × 5 min per upload = 4+ hours JUST clicking
Plus metadata entry × 2 = 8-10 hours total

With this tool:
Setup = 3 hours (one-time)
Future batches = 15 minutes each
Uploads = Automatic (no babysitting)
```

---

## Handling New Episodes

### Adding to Existing Channel

```bash
# 1. Add new episode MP4 to folder
# 2. Rebuild preview (old metadata preserved!)
python3 scripts/build_preview_spreadsheet.py ...

# 3. Fill metadata for new episodes only
# 4. Build new queue
python3 scripts/build_upload_queue.py \
  "./podcast_preview.xlsx" \
  "/path/to/episodes" \
  "YOUR_CONNECTION_ID" \
  "./podcast_queue_new.json" \
  --order sequential

# 5. Create new scheduled task for new episodes
```

The Excel file **remembers** your previous titles, so you only edit new entries.

---

## Podcast-Specific Settings

### For Established Podcasts (100k+ subscribers)
```bash
--batch-size 3 --interval 15 minutes
# 3 episodes per 15 min = feels natural, not batch-dumped
```

### For New Podcasts (<10k subscribers)
```bash
--batch-size 1 --interval 1 day
# Controlled rollout, allows time between uploads
# Gives algorithm time to process each video
```

### For Growing Podcasts (10k-100k)
```bash
--batch-size 2 --interval 2 hours
# Balanced: visible activity, not overwhelming
```

---

## Troubleshooting

### "Some episodes didn't upload"
- Check `podcast_queue.json` for error field
- Verify video file is valid: `ffprobe episode_X.mp4`
- Check YouTube upload quota (limits per day)
- Automatic retry happens up to 3 times

### "Episode order is wrong"
- Use `--order sequential` (you did this ✓)
- Verify filenames sort correctly: `ls episodes/ | sort`
- If wrong, rename files and rebuild queue

### "Metadata looks different on YouTube"
- YouTube truncates long titles (60 chars limit)
- Some HTML chars not allowed (< > &)
- Hashtags work best at end of description

---

## Next Steps

1. ✅ Organize podcast files
2. ✅ Generate preview spreadsheet
3. ✅ Fill metadata (use templates to save time)
4. ✅ Build upload queue (sequential, 1 per batch)
5. ✅ Schedule with Claude
6. ✅ Monitor first 2-3 uploads to verify
7. ✅ Let it run automatically

---

## Creator Resources

- [YouTube Audio Library](https://www.youtube.com/audiolibrary) - Background music
- [Epidemic Sound](https://www.epidemicsound.com) - Royalty-free music
- [Adobe Podcast](https://podcast.adobe.com) - Audio enhancement
- [Descript](https://www.descript.com) - Transcription + editing

---

**🎙️ Your podcast deserves to be on YouTube. This tool makes it effortless.**

Good luck with your uploads! 🚀
