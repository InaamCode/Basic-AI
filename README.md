# Basic AI Agent

## AI-Augmented Workflow Project

This project is a beginner-level implementation of a Basic AI Agent developed
for the "AI-Augmented Workflow" course.

The project demonstrates how Python can be used to communicate with a Large
Language Model through an API and generate responses to user requests.

---

## Project Objective

The main objective of this project is to understand the basic architecture
and development workflow of an AI Agent.

The agent accepts a user's question or instruction, sends it to an AI model,
and displays the generated response.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenAI API | Communication with the AI model |
| Visual Studio Code | Development environment |
| Git | Version control |
| GitHub | Project repository |
| Ollama | Optional local LLM alternative |

---

## Basic Architecture

```text
+-------------+
|    User     |
+-------------+
       |
       v
+-------------+
| Python      |
| AI Agent    |
+-------------+
       |
       v
+-------------+
| OpenAI API  |
+-------------+
       |
       v
+-------------+
| LLM Model   |
+-------------+
       |
       v
+-------------+
| AI Response |
+-------------+
       |
       v
+-------------+
|    User     |
+-------------+