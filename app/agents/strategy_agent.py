from crewai import Agent
from app.llm import get_llm


def create_strategy_agent():
    return Agent(
        role="Business Strategy Specialist",
        goal=(
            "Use the research and analysis findings to develop practical "
            "business strategies, recommendations, growth opportunities, "
            "and actions that can improve the company's competitive position."
        ),
        backstory=(
            "You are an experienced business strategist who specializes in "
            "turning market research and analytical insights into practical "
            "business strategies and recommendations."
        ),
        llm=get_llm(),
        max_iter=1,
        max_retry_limit=0,
        use_system_prompt=False,
        verbose=True,
    )
