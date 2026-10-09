from crewai import Agent
from app.llm import get_llm


def create_data_analyst_agent():
    return Agent(
        role="Data Analysis Specialist",
        goal=(
            "Analyze the research findings and identify important patterns, "
            "comparisons, business insights, and meaningful conclusions "
            "that can support decision-making."
        ),
        backstory=(
            "You are an experienced business data analyst who specializes "
            "in interpreting research data, comparing findings, identifying "
            "patterns, and turning information into useful business insights."
        ),
        llm=get_llm(),
        max_iter=1,
        max_retry_limit=0,
        use_system_prompt=False,
        verbose=True,
    )