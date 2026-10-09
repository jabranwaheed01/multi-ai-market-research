from crewai import Task


def create_data_analysis_task(agent):
    return Task(
        description=(
            "Analyze the research findings for {company}. "
            "Compare the available information, identify important patterns, "
            "business insights, strengths, weaknesses, and meaningful "
            "conclusions that can support decision-making."
        ),
        expected_output=(
            "A structured data analysis report containing key findings, "
            "comparisons, patterns, business insights, and conclusions."
        ),
        agent=agent,
    )
