from crewai import Crew, Process
from agents import blog_writer, blog_researcher
from task import research, write
from fetch_transcript_video_id import fetch_transcript,get_video_id


# Initialize Crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research, write],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)


# Define the topic to search for
topic = "VIDEO_NAME OR TOPIC"

youtube_video_link =  "YOUTUBE_VIDEO_LINK"
youtube_VIDEO_ID =  get_video_id(youtube_video_link)

# Fetch the transcript if the video ID is available
if youtube_VIDEO_ID:
    transcript = fetch_transcript(youtube_VIDEO_ID)
    print("transcript =>",transcript)
    if transcript != "Transcript not available for this video.":
        print("Transcript fetched successfully.")
        # Start the task execution with the transcript as input
        result = crew.kickoff(inputs={'topic': topic, 'transcript': transcript})
        print(result)
    else:
        print("Could not fetch transcript.")
else:
    print("Video ID not found.")

