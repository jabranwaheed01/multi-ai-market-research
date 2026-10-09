from crewai import Agent
from app.llm import get_llm


def create_report_writer_agent():
    return Agent(
        role="Business Report Writer",
        goal=(
            "Combine the research, competitor analysis, market trends, "
            "data analysis, and strategy findings into a clear, professional, "
            "and well-structured business intelligence report."
        ),
        backstory=(
            "You are an experienced business report writer who specializes "
            "in turning complex research and analytical findings into clear, "
            "professional, and decision-ready reports."
        ),
        llm=get_llm(),
        max_iter=1,
        max_retry_limit=0,
        use_system_prompt=False,
        verbose=True,
    )
