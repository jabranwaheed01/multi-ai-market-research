import uuid

from fastapi import BackgroundTasks, FastAPI, HTTPException

from app.schemas.research import ResearchRequest, ResearchResponse
from app.schemas.job import JobStatus
from app.services.research_service import start_research, get_job


app = FastAPI(
    title="AI-Powered Market Research API",
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {
        "status": "API is running"
    }


@app.post("/research", response_model=ResearchResponse)
def create_research(
    request: ResearchRequest,
    background_tasks: BackgroundTasks,
):
    job_id = str(uuid.uuid4())

    background_tasks.add_task(
        start_research,
        job_id,
        request.company,
    )

    return ResearchResponse(
        job_id=job_id,
        status="started",
    )


@app.get("/research/{job_id}", response_model=JobStatus)
def research_status(job_id: str):
    job = get_job(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Research job not found",
        )

    return job