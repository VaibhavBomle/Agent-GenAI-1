from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Initialize research task with direct call to `fetch_transcript`
research = Task(
    description="Search for the video with {topic} and retrieve the transcript if available.",
    expected_output="A comprehensive 3-paragraph report based on the video transcript and content.",
    tools=[yt_tool],
    agent=blog_researcher
)

# Modify `write` task to use the transcript directly, assuming it has been retrieved
write = Task(
    description="Use the fetched video transcript to create a blog post on the topic {topic}.",
    expected_output="Summarize and narrate the information into blog content based on the transcript.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='blog-post.md'
)
