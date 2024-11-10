from youtube_transcript_api import YouTubeTranscriptApi
import re

# fetch transcript by passing video ID
def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

# fetch video id by passing youtube video url
def get_video_id(youtube_video_url):
    video_id_match = re.search(r"v=([a-zA-Z0-9_-]{11})", youtube_video_url)
    if video_id_match:
        youtube_video_id = video_id_match.group(1)
        print("Video ID:", youtube_video_id)
        return youtube_video_id
    else:
        print("Invalid YouTube URL")
    