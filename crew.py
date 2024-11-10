from crewai import Crew,Process
from agents import blog_writer,blog_researcher
from task import research,write
print("Everything is working ")

crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research,write],
    process=Process.sequential, # Optional Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the task execution process
result = crew.kickoff(input = {'topic' : 'Realtime Multimodal RAG Usecase Part 3 | MultiVectorRetriver with Langchain | RAG Application'})
print(result)
