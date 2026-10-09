from crewai import Agent
from app.llm import get_llm


def create_competitor_research_agent():
    return Agent(
        role="Competitor Research Specialist",
        goal=(
            "Research the main competitors of the target company and "
            "analyze their products, market position, strengths, weaknesses, "
            "and competitive advantages."
        ),
        backstory=(
            "You are an experienced competitive intelligence researcher. "
            "You specialize in identifying major competitors and comparing "
            "businesses to help companies understand their competitive landscape."
        ),
        llm=get_llm(),
        max_iter=1,
        max_retry_limit=0,
        use_system_prompt=False,
        verbose=True,
    )