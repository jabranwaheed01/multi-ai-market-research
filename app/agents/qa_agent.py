from crewai import Agent
from app.llm import get_llm


def create_qa_agent():
    return Agent(
        role="Quality Assurance Specialist",
        goal=(
            "Review the business intelligence report for accuracy, "
            "completeness, clarity, consistency, and overall quality. "
            "Identify missing information, weak conclusions, and errors "
            "that should be corrected before the report is finalized."
        ),
        backstory=(
            "You are an experienced quality assurance specialist who "
            "reviews business research reports. You focus on accuracy, "
            "consistency, completeness, and actionable recommendations."
        ),
        llm=get_llm(),
        max_iter=1,
        max_retry_limit=0,
        use_system_prompt=False,
        verbose=True,
    )