from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

# Initialize Blog Researcher Agent
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Identify the video {topic} from the provided YouTube channel and retrieve the transcript if available.',
    verbose=True,
    memory=True,
    backstory="Expert in finding transcripts for AI, Data Science, ML, and GEN AI topics.",
    tools=[yt_tool],
    allow_delegation=True
)

# Initialize Blog Writer Agent
blog_writer = Agent(
    role='Blog Writer',
    goal='Generate engaging blog content based on the video transcript and topic {topic}.',
    verbose=True,
    memory=True,
    backstory="Crafts compelling narratives that simplify complex topics and engage readers.",
    tools=[], # No need to pass yt_tool
    allow_delegation=False
)
