from crewai import Crew, Process

from app.agents.strategy_agent import create_strategy_agent
from app.tasks.strategy_task import create_strategy_task


def create_strategy_crew():
    strategy_agent = create_strategy_agent()

    strategy_task = create_strategy_task(strategy_agent)

    crew = Crew(
        agents=[strategy_agent],
        tasks=[strategy_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew