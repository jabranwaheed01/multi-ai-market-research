# AI-Powered Multi-Agent Market Research System

An AI-powered market research system built with **CrewAI, Python, and FastAPI**. The system uses specialized AI agents to research companies, analyze competitors, identify market trends, generate business insights, and prepare structured research reports.

## Overview

Traditional market research requires collecting information from multiple sources and analyzing it manually. This project automates major parts of that workflow using a team of AI agents, with each agent responsible for a specific research or analysis task.

The system accepts a company name, runs the research workflow in the background, and provides an API to check the job status and retrieve the generated report.

## Features

- Multi-agent research and analysis using CrewAI
- Company and competitor research
- Market trends and industry analysis
- Data-driven business insights
- Strategic recommendations
- Automated business report generation
- Quality assurance and report review workflow
- REST API built with FastAPI
- Background research execution and job-status tracking
- Interactive API documentation with Swagger UI

## AI Agents

The system is designed around seven specialized agents:

1. **Company Research Specialist** — researches company products, customers, strengths, weaknesses, and opportunities.
2. **Competitor Research Specialist** — analyzes competitors and their competitive advantages.
3. **Market Trends Research Specialist** — identifies industry changes, customer behavior, emerging technologies, and growth opportunities.
4. **Data Analysis Specialist** — analyzes findings and identifies patterns and business insights.
5. **Business Strategy Specialist** — develops strategic recommendations and potential growth initiatives.
6. **Business Report Writer** — combines research findings into a structured business report.
7. **QA Reviewer** — reviews report quality and identifies areas that need improvement.

## Technology Stack

- **Language:** Python
- **Multi-Agent Framework:** CrewAI
- **LLM Integration:** LiteLLM and Groq
- **Backend API:** FastAPI
- **ASGI Server:** Uvicorn
- **Data Validation:** Pydantic
- **API Documentation:** Swagger UI / OpenAPI

## Project Structure

```text
Multi-AI-Agents/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── tasks/
│   │   ├── crews/
│   │   ├── schemas/
│   │   └── services/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── .gitignore
└── README.md
```

*Note: Adjust this structure to match the actual files and folders in your repository.*

## Getting Started

### Prerequisites

- Python 3.12
- pip
- A Groq API key

### 1. Clone the repository

```bash
git clone https://github.com/jabranwaheed01/multi-ai-market-research.git
cd multi-ai-market-research
```

### 2. Create a virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure you run this command from the directory containing `requirements.txt`.

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a reference, and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Use the exact environment variable names expected by your application. Never commit your real API key or `.env` file to GitHub.

### 5. Start the API server

From the directory containing `main.py`, run:

```bash
python -m uvicorn main:app --reload --port 8000
```

### 6. Open the API documentation

Visit:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running |
| POST | `/research` | Starts a research job |
| GET | `/research/{job_id}` | Checks job status and retrieves available results |

### Example: Start Research

**Request**

```http
POST /research
Content-Type: application/json
```

```json
{
  "company": "Tesla"
}
```

**Example response**

```json
{
  "job_id": "your-job-id",
  "status": "started"
}
```

The returned `job_id` can be used to check the research job.

### Example: Check Research Status

```http
GET /research/your-job-id
```

The response may include the job status, generated report, or an error message, depending on the job's progress.

## Example Use Case

For example, submitting `Tesla` initiates a workflow that researches the company, analyzes competitors, evaluates market trends, identifies business insights, develops strategic recommendations, and prepares a business intelligence report.

## Future Improvements

- Improve rate-limit handling and retry mechanisms
- Add structured research output using Pydantic models
- Implement a QA feedback loop with a maximum of two revisions
- Add hierarchical agent delegation
- Improve source verification and factual accuracy
- Add persistent storage for research jobs and reports
- Develop an interactive Gradio user interface
- Add Docker-based deployment and automated tests

## Current Limitations

- Research quality depends on the selected LLM and available sources.
- LLM provider rate limits may interrupt longer research workflows.
- Research results should be verified before being used for business decisions.

## License

Add a license appropriate for your project before distributing or reusing the code.
