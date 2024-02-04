# EdAgent
## Introduction
Example script to automatically write a screenplay from a newsgroup post using agents with [Crew.ai] (https://github.com/Chigoziee/EdAgent) .
EdAgent uses CrewAI to orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

## Overview
An agent workflow capable of generating questions and answers on a specific topic using crewAI.

## Agents Used
### Researcher: 
This agent develops ideas for teaching someone new to the subject.
### Writer: 
This agent uses the Researcher’s ideas to write a piece of text to explain the topic.
### Examiner: 
This agent craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers. In other words: it test whether a student has fully understood the text.
