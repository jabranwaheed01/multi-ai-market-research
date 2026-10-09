from crewai import Agent
from app.llm import get_llm


def create_market_trends_agent():
    return Agent(
        role="Market Trends Research Specialist",
        goal=(
            "Research current market trends related to the target company "
            "and identify important industry changes, customer trends, "
            "growth opportunities, and emerging technologies."
        ),
        backstory=(
            "You are an experienced market research analyst specializing "
            "in identifying industry trends, emerging technologies, "
            "customer behavior, and future market opportunities."
        ),
        llm=get_llm(),
        max_iter=1,
        max_retry_limit=0,
        use_system_prompt=False,
        verbose=True,
    )

