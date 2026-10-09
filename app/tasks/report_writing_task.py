from crewai import Task


def create_report_writing_task(agent):
    return Task(
        description=(
            "Create a professional business intelligence report for {company} "
            "using the available company research, competitor analysis, "
            "market trends, data analysis, and strategy findings. "
            "Organize the information clearly and present useful conclusions "
            "and recommendations."
        ),
        expected_output=(
            "A professional business intelligence report containing an "
            "executive summary, company overview, competitor analysis, "
            "market trends, key insights, strategic recommendations, "
            "and conclusion."
        ),
        agent=agent,
    )