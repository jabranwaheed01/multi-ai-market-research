from crewai import Crew, Process

from app.agents.market_trends_agent import create_market_trends_agent
from app.tasks.market_trends_task import create_market_trends_task


def create_market_trends_crew():
    market_agent = create_market_trends_agent()

    market_task = create_market_trends_task(market_agent)

    crew = Crew(
        agents=[market_agent],
        tasks=[market_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew

