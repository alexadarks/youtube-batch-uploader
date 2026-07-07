#!/usr/bin/env python3
"""
Scheduled batch upload worker for YouTube.

This script is meant to be run by a scheduled task (e.g., via cron or Claude's
scheduled-tasks MCP). It processes one batch from the upload queue and updates
the queue file with progress.

Usage:
  python3 scheduled_upload_worker.py <queue_json_path> [<connection_id>]

The script is FULLY SELF-CONTAINED -- it does not ask for user input and
only reports progress via stdout JSON.

Queue JSON format:
{
  "connectionId": "...",
  "privacyStatus": "public|unlisted|private",
  "batchSize": 3,
  "items": [
    {
      "filename": "video.mp4",
      "path": "/full/path/to/video.mp4",
      "title": "Video Title",
      "description": "Video description",
      "fileSizeBytes": 123456789,
      "uploaded": false,
      "attempts": 0,
      "videoId": null,
      "error": null
    },
    ...
  ]
}

This worker is designed to be called by Claude's scheduled-tasks MCP with this prompt:

---
You are running a batch YouTube upload step. Fully self-contained -- do not ask the
user anything, just execute and report a short summary at the end.

QUEUE FILE: /absolute/path/to/upload_queue.json

Steps:
1. Call python3 scripts/scheduled_upload_worker.py with the queue file path
2. Capture and report the JSON output
3. Check the "completed" and "failed" counts
4. If queue is fully processed (remaining == 0), note that uploads are complete

Report findings as JSON with keys: uploaded, skipped, failed, remaining, errors.
---

Note: Actual file upload is handled via curl, as the YouTube Studio MCP only
provides upload session creation, not the actual PUT request.
"""
import sys
import os
import json
import subprocess
from pathlib import Path


def load_queue(queue_path):
    """Load and validate the upload queue."""
    try:
        with open(queue_path, 'r') as f:
            queue = json.load(f)
        return queue
    except FileNotFoundError:
        print(json.dumps({"error": f"Queue file not found: {queue_path}"}))
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"Invalid queue JSON: {e}"}))
        sys.exit(1)


def save_queue(queue, queue_path):
    """Save queue back to file."""
    with open(queue_path, 'w') as f:
        json.dump(queue, f, ensure_ascii=False, indent=1)


def get_next_batch(queue):
    """Get next batch of items to upload (up to batchSize, not yet uploaded, attempts < 3)."""
    batch = []
    batch_size = queue.get("batchSize", 3)

    for item in queue["items"]:
        if len(batch) >= batch_size:
            break
        if not item["uploaded"] and item.get("attempts", 0) < 3:
            batch.append(item)

    return batch


def upload_video_via_youtube_mcp(item, connection_id, privacy_status):
    """
    Upload a video using YouTube Studio MCP.

    This function should be called from within a Claude session that has
    the YouTube Studio MCP connected. It will use the MCP tools to:
    1. Create an upload session
    2. Get the upload URL
    3. curl the file bytes to the upload URL

    Returns: (success: bool, video_id: str or None, error: str or None)

    NOTE: This is a placeholder. In practice, this would be called from
    Claude's scheduled-tasks runner which has MCP access.
    """
    # This is a stub - actual implementation requires Claude MCP context
    # The real flow happens inside Claude's scheduled task prompt
    return (False, None, "Upload requires Claude MCP context (run from scheduled task)")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scheduled_upload_worker.py <queue_json_path> [<connection_id>]")
        sys.exit(1)

    queue_path = sys.argv[1]
    queue = load_queue(queue_path)

    # Summary stats
    result = {
        "queue_file": queue_path,
        "batch_size": queue.get("batchSize", 3),
        "privacy_status": queue.get("privacyStatus", "public"),
    }

    # Count current state
    total_items = len(queue["items"])
    uploaded = sum(1 for item in queue["items"] if item["uploaded"])
    failed = sum(1 for item in queue["items"] if not item["uploaded"] and item.get("attempts", 0) >= 3)
    remaining = total_items - uploaded - failed

    result.update({
        "total_items": total_items,
        "uploaded": uploaded,
        "failed": failed,
        "remaining": remaining,
    })

    # Get next batch
    batch = get_next_batch(queue)

    if not batch:
        if remaining == 0:
            result["status"] = "complete"
            result["message"] = f"All uploads done: {uploaded} uploaded, {failed} failed"
        else:
            result["status"] = "waiting"
            result["message"] = f"No videos ready for upload. {uploaded} done, {failed} failed."
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # Process batch
    result["status"] = "processing"
    result["batch_items"] = len(batch)
    uploaded_this_run = []
    errors_this_run = []

    for item in batch:
        # Increment attempts
        item["attempts"] = item.get("attempts", 0) + 1

        # TODO: Call YouTube MCP to upload
        # For now, just mark structure
        # In real use: parse upload response, get videoId, mark uploaded=true
        error_msg = "Upload requires Claude MCP context (must run from scheduled task)"
        item["error"] = error_msg
        errors_this_run.append({
            "filename": item["filename"],
            "attempt": item["attempts"],
            "error": error_msg,
        })

    # Save updated queue
    save_queue(queue, queue_path)

    result["uploaded_this_run"] = uploaded_this_run
    result["errors"] = errors_this_run

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
