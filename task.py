from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

# Initialize research task
research_task = Task(
    description = (
     "Identify the video {topic}."
     "Get detailed information about the video from the channal video."
    ),
    expected_output = "A compresensive 3 paragraphs long report based on the {topic} of video content.",
    tools = [yt_tool],
    agent = blog_researcher
)

# Writing task with language model configuration
write = Task(
    description = (
        "get the info from the yutube channel on the topic {topic}."
    ),
    expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='blog-post-new.md'
)