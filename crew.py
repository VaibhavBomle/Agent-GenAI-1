from crewai import Crew,Process
from agents import blog_writer,blog_researcher
from task import research,write
print("Everything is working ")

# Initialize Crew
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research,write],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the task execution process
youtube_VIDEO_NAME =  "You tube video name"
result = crew.kickoff(inputs = {'topic' : youtube_VIDEO_NAME})
print(result)
