from crewai import Crew, Process

from app.agents.competitor_research_agent import create_competitor_research_agent
from app.tasks.competitor_research_task import create_competitor_research_task


def create_competitor_research_crew():
    competitor_agent = create_competitor_research_agent()

    competitor_task = create_competitor_research_task(competitor_agent)

    crew = Crew(
        agents=[competitor_agent],
        tasks=[competitor_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew