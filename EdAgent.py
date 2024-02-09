import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

file = open("google_api_key.txt", "r")
api_key = file.read()
file.close()

#Using google gemini-pro as llm
llm = ChatGoogleGenerativeAI(model ='gemini-pro',verbose=True, temperature=0.6, google_api_key=api_key)
search_tool = DuckDuckGoSearchRun()

# Defining the research agent to generate ideas for teaching a topic
researcher = Agent(
  role='educational researcher',
  goal='Uncover ideas for teaching tech beginners',
  backstory="""you are a researcher whose focus is on discovering the best
  learning approach and ideas for teaching software engineering to various types
  of students""",
  verbose=False,
  allow_delegation=False,
  llm = llm,  #using google gemini pro API
  tools=[
        search_tool
      ]
)

# Defining the writer agent to generate tutorial on topic
writer = Agent(
  role='Tech instructor',
  goal='Generate tech tutorial on various topics for beginners',
  backstory="""You are a renowned tech instructor with over 12 years experience
  teaching tech. you are known for using practical examples""",
  verbose=False,
  allow_delegation=False,
  llm = llm,  #using google gemini pro API
  tools=[search_tool]
)

# Defining the agent that examines student understanding of subject topic
examiner = Agent(
  role='Tech examiner',
  goal='generate test questions and then their answers',
  backstory="""You are a professor of computer science, and have been teaching
  freshers for over 25 years. You have are very good at evaluating student's
  understanding of various topics""",
  verbose=False,
  allow_delegation=False,
  llm = llm,  #using google gemini pro API
  tools=[]
)
topic = input('Topic: ')
# Creating tasks for your agents
task1 = Task(
  description=f"""Develop ideas for teaching {topic}""",
  agent=researcher
)
task2 = Task(
  description=f"""Generate an engaing tutorial on {topic}. explain various sub-topics in paragraphs,
  It must contain practical examples for tech beginners, and additional online resources.""",
  agent=writer
)
task3 = Task(
  description="""from the tutorial, generate 3 test
  questions and answers to evaluate understanding of the topic.""",
  agent=examiner
)
# Instantiating my crew with a sequential process
crew = Crew(
  agents=[researcher, writer, examiner],
  tasks=[task1, task2, task3],
  verbose=1, # You can set it to 1 or 2 to different logging levels
  process=Process.sequential
)

# Getting crew to work!
result = crew.kickoff()