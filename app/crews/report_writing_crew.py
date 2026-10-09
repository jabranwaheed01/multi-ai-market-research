from crewai import Crew, Process

from app.agents.report_writer_agent import create_report_writer_agent
from app.tasks.report_writing_task import create_report_writing_task


def create_report_writing_crew():
    report_agent = create_report_writer_agent()

    report_task = create_report_writing_task(report_agent)

    crew = Crew(
        agents=[report_agent],
        tasks=[report_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew