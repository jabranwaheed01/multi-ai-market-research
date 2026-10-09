from crewai import Crew, Process

from app.agents.data_analyst_agent import create_data_analyst_agent
from app.tasks.data_analysis_task import create_data_analysis_task


def create_data_analysis_crew():
    data_agent = create_data_analyst_agent()

    data_task = create_data_analysis_task(data_agent)

    crew = Crew(
        agents=[data_agent],
        tasks=[data_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew