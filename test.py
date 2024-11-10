import re

# Example YouTube URL
youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Regular expression to match video ID from YouTube URL
video_id_match = re.search(r"v=([a-zA-Z0-9_-]{11})", youtube_url)
if video_id_match:
    youtube_VIDEO_ID = video_id_match.group(1)
    print("Video ID:", youtube_VIDEO_ID)
else:
    print("Invalid YouTube URL")