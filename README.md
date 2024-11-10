# Agent-GenAI-1
---

This project uses the CrewAI framework to automate the generation of blog content from YouTube videos. It leverages two main agents — a `blog_researcher` and a `blog_writer` — to extract transcripts from YouTube videos, summarize the content, and create comprehensive blog posts on AI, data science, machine learning, and general AI topics. The tools and tasks are orchestrated sequentially within a `Crew` instance, allowing for effective data extraction, summarization, and content creation.

## Table of Contents

- [Project Overview](#project-overview)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Configuration](#configuration)

## Project Overview

This project extracts and generates blog posts from YouTube videos by automating the following tasks:
1. **Research** - Extracts detailed information from YouTube videos based on the given topic.
2. **Writing** - Summarizes the extracted data and formats it into a blog post.

The system is built to handle various AI and data science topics by pulling video transcripts and creating blog-friendly summaries, making it an ideal tool for content creators, bloggers, or tech enthusiasts.

## Components

- **Agents**: Defined in `agents.py`, these are the specialized entities performing distinct tasks.
  - `blog_researcher`: Extracts video transcripts and content based on the topic.
  - `blog_writer`: Transforms the extracted information into readable, engaging blog content.

- **Tasks**: Configured in `task.py`, these tasks define the work done by each agent.
  - `research`: Gathers comprehensive video information related to a specific topic.
  - `write`: Summarizes the information and structures it into blog content.

- **Crew**: Assembled in `crew.py`, this defines the process by which tasks are executed and agents interact.

## Installation

1. **Install Dependencies**:
    Ensure you have Python 3.x installed and install dependencies:
    ```bash
    pip install crewai crewai_tools python-dotenv
    ```

2. **API Keys and Environment Variables**:
    - Create a `.env` file in the root directory.
    - Add your OpenAI API Key:
      ```plaintext
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

### Running the Script

To run the project, define a topic in the `crew.kickoff` function call. Replace `{topic}` with a specific topic for content extraction and generation:

```python
crew.kickoff(inputs={'topic': 'Your Desired Topic Here'})
```


Run:
```
   python crew.py
```

Example topics might include:
- `"What Is LangChain?`

This will execute both research and writing tasks, generating a blog post based on the YouTube video content.

### Output

The final blog post will be saved in a markdown file (`new-blog-post.md`) in the current directory.

## File Descriptions

- **tools.py**: Contains the configuration for the `YoutubeChannelSearchTool`, specifying the YouTube channel from which to pull video content.
- **task.py**: Defines `research` and `write` tasks, specifying the agents and tools used for content extraction and creation.
- **agents.py**: Configures the `blog_researcher` and `blog_writer` agents with goals, backstory, and API settings.
- **crew.py**: Manages the `Crew` instance and processes for sequentially executing the defined tasks.
- **.env**: Stores sensitive API keys (ensure this file is added to `.gitignore` to avoid accidental exposure).

## Configuration

- **Sequential Process**: The tasks run in a sequential process by default.
- **Agent Memory**: Agents have `memory=True`, meaning they can retain context across tasks for a more coherent output.
- **API Integration**: The project uses the OpenAI API (GPT-4 model) to generate human-like blog content based on video transcripts.

---

