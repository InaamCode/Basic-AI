# ADR 1: Selection of Tech Stack for Basic AI Agent

## Status

Proposed

## Date

16 August 2026

## Context

We need to develop a basic AI Agent as part of the college project for the
"AI-Augmented Workflow" course.

The purpose of the project is to understand how an AI Agent can receive a
user request, communicate with a Large Language Model (LLM), process the
response, and provide useful output to the user.

As this is a beginner-level project, the technology stack should be simple,
easy to understand, easy to test, and compatible with AI-assisted coding.

The project should also be flexible enough to add more features in the future,
such as conversation memory, tools, external APIs, and a user interface.

## Decision

We have selected the following technology stack:

### 1. Python

Python will be used as the primary programming language.

Python is beginner-friendly and widely used for Artificial Intelligence,
Machine Learning, automation, and API-based applications.

### 2. OpenAI API

The OpenAI API will be used to communicate with a Large Language Model.

The Python application will send a user prompt to the API and receive an
AI-generated response.

An open-source alternative such as Ollama can be considered in the future
if a local LLM implementation is required.

### 3. Visual Studio Code

Visual Studio Code will be used as the main development environment.

It provides useful features such as syntax highlighting, debugging,
extensions, terminal integration, and AI-assisted coding support.

### 4. Git and GitHub

Git will be used for version control.

GitHub will be used to store the project repository and maintain the
development history.

### 5. Python Virtual Environment

A Python virtual environment will be used to isolate the dependencies of
this project from other Python projects.

## Architecture

The basic architecture of the AI Agent is:

User
  |
  v
Python AI Agent
  |
  v
OpenAI API
  |
  v
Large Language Model
  |
  v
AI Response
  |
  v
User

## Consequences

### Advantages

1. Python is easy for beginners to learn and understand.

2. Python has a large ecosystem for Artificial Intelligence and Machine
   Learning.

3. The OpenAI API provides access to an LLM without requiring us to train
   a language model from scratch.

4. AI coding assistants can help generate, explain, debug, and improve
   Python code.

5. The project can be developed incrementally.

6. Git and GitHub provide version control and make it easier to track
   project changes.

7. Ollama can be considered later for experimenting with local,
   open-source language models.

### Disadvantages

1. The OpenAI API requires an API key.

2. API usage may involve costs depending on the service and account.

3. An internet connection is required when using a hosted API.

4. API keys must be protected and must never be uploaded to GitHub.

5. AI-generated code can contain errors and must be reviewed and tested
   by the developer.

6. Local LLM solutions such as Ollama may require more computer resources
   depending on the selected model.

## AI-Assisted Coding Compatibility

This technology stack is highly compatible with AI-assisted development.

AI tools can assist with:

- Generating Python code
- Explaining programming concepts
- Creating API integration code
- Debugging errors
- Improving code structure
- Creating documentation
- Writing test cases
- Suggesting project improvements
- Explaining error messages

However, AI-generated code will not be accepted blindly.

The developer will review, understand, test, and modify AI-generated code
before including it in the project.

## Alternatives Considered

### Ollama + Open-Source LLM

Ollama can be considered as an alternative for running compatible
open-source language models locally.

Advantages:

- Local model execution
- Useful for learning about local LLMs
- Reduced dependency on external API requests

Disadvantages:

- Requires suitable hardware
- Larger models may require significant RAM or GPU resources
- Model setup can be more complex for beginners

### JavaScript / Node.js

JavaScript with Node.js could also be used for developing the AI Agent.

However, Python was selected because it is beginner-friendly and widely
used in Artificial Intelligence and Machine Learning.

## Final Decision

Python with the OpenAI API has been selected as the primary technology
stack for the Basic AI Agent.

Ollama will be considered as an alternative if a local and open-source
LLM implementation is required in the future.

The project will use Visual Studio Code for development and Git/GitHub
for version control.