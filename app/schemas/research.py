from pydantic import BaseModel


class ResearchRequest(BaseModel):
    company: str


class ResearchResponse(BaseModel):
    job_id: str
    status: str