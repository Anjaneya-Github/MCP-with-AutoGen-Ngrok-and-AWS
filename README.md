# MCP-with-AutoGen-Ngrok-and-AWS
# Notion MCP Agent Interface

## Overview
This project is a full-stack system designed to connect a user-facing web frontend to a Notion workspace using an AI Agent framework. It leverages the **Model Context Protocol (MCP)** to securely bridge the gap between AI-driven task execution and Notion's infrastructure. Users can submit natural language tasks (e.g., "Create a new Notion page about our meeting"), and the backend agent will autonomously execute the request.

## Architecture
The system is composed of several key components working together to process and execute tasks:

* **Front End:** A web-based UI for users to submit tasks and view results.
* **ngrok:** Acts as a secure tunnel, exposing the local development backend to the public internet so the frontend can communicate with it.
* **Flask API:** A Python-based backend server (running locally on port `7001`) that exposes endpoints like `/task` to receive frontend instructions.
* **AI Agent (AutoGen):** The intelligence layer that processes the incoming tasks, determines the necessary steps, and formats the payload.
* **Notion MCP Server:** Provides standardized, bi-directional communication with Notion, allowing the AI agent to read context or perform actions like creating databases and pages.
* **AWS EC2:** Cloud compute infrastructure used to host the agent environment, manage database state, or handle heavy processing.

## How It Works (Data Flow)
1. **User Request:** The user submits a natural language task via the **Front End**.
2. **Tunneling:** The request is sent to an **ngrok public URL**, which routes it to the local **Flask API**.
3. **Task Ingestion:** The Flask app receives the payload at the `localhost:7001/task` endpoint and hands it off to the **AI Agent**.
4. **Agent Processing:** The agent interprets the task and prepares the necessary commands.
5. **Execution:** The agent communicates with the **Notion MCP Server** to execute the requested action (e.g., creating a new page) directly within the authenticated Notion workspace.
