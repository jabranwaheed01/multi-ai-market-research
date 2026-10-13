# AI-Powered Market Research Workflow

## Research Process

1. Receive the target company name through the API.
2. Create a background research job.
3. Collect company information.
4. Research competitors and market trends.
5. Analyze the collected information.
6. Develop strategic recommendations.
7. Generate a research report.
8. Review the report through quality assurance.
9. Return the job status and report through the API.

## API Endpoints

- `POST /research` — Start a research job.
- `GET /research/{job_id}` — Check job status and retrieve the report.
