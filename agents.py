from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview" 

# Initialize Blog Researcher Agent
blog_research = Agent(
    role= 'Blog Researher from Youtube Videos',
    goal = 'get the relevant video transcription for the topic {topic} from the provided Yt channel'
    verboe= True,
    MEMORY = True,
    backstory = (
        "Expert in understanding video in AI Data Science , Machine Learning And GEN AI and providing suggestion"
    ),
    tools = [yt_tool],
    allow_delegation = True
)


# Initialize Blog writer Agent
blog_writer  = Agent(
    role = 'Blog Writer',
    goal = 'Narrate compeling tech stories about the video {topic} from YT video',
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    )
)