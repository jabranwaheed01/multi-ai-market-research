
from app.crews.research_crew import create_research_crew

jobs = {}


def start_research(job_id: str, company: str):
    jobs[job_id] = {
        "job_id": job_id,
        "company": company,
        "status": "running",
        "report": None,
        "error": None,
    }

    try:
        crew = create_research_crew()

        result = crew.kickoff(
            inputs={"company": company}
        )

        jobs[job_id]["status"] = "completed"
        jobs[job_id]["report"] = str(result)

    except Exception as exc:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(exc)


def get_job(job_id: str):
    return jobs.get(job_id)