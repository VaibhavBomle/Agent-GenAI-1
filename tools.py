from crewai_tools import YoutubeChannelSearchTool
from youtube_transcript_api import YouTubeTranscriptApi

# Set up the channel name as before
YouTube_Channel_Name = "YouTube_Channel_Name"
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle=YouTube_Channel_Name)

