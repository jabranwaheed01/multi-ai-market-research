from pydantic import BaseModel, field_validator


class ResearchRequest(BaseModel):
    company: str

    @field_validator("company")
    @classmethod
    def validate_company(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Company name cannot be empty")
        return value


class ResearchResponse(BaseModel):
    job_id: str
    status: str