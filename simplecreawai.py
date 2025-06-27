import os
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

# Read your API key from the environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# print("\n--- gemini_api_key:", GOOGLE_API_KEY)


# Use Gemini 1.5 Pro or other Gemini models
# Note the format: 'gemini/model-name'
gemini_llm = LLM(
    model='gemini/gemini-2.5-flash-preview-05-20',  # Or 'gemini/gemini-1.5-flash', etc.
    api_key=GOOGLE_API_KEY,
    temperature=0.7,  # Adjust temperature for creativity (0.0 to 1.0)
    # Add other parameters as needed, e.g., max_tokens, top_p, etc.
)

# Now, you can use this gemini_llm when defining your agents:
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory="""You work at a leading tech think tank. Your expertise lies in identifying emerging trends.You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    llm=gemini_llm,  # Assign the Gemini LLM here
    allow_delegation=False,
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on tech advancements',
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles. You transform complex concepts into compelling narratives.""",
    verbose=True,
    allow_delegation=True,
    llm=gemini_llm,  # Assign the Gemini LLM here
)

# Define tasks and crew as usual
task1 = Task(
    description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024. Identify key trends, breakthrough technologies, and potential industry impacts. Your final answer MUST be a full analysis report""",
    agent=researcher
    ,expected_output="A comprehensive analysis report on the latest advancements in AI in 2024, including key trends, breakthrough technologies, and potential industry impacts."
)

task2 = Task(
    description="""Using the insights provided, develop an engaging blog post that highlights the most significant AI advancements.""",
    agent=writer
    ,expected_output="An engaging blog post highlighting the most significant AI advancements based on the provided analysis."
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    process=Process.sequential, # or Process.hierarchical
    verbose=True
)

result = crew.kickoff()
print("########################")
print(result)
