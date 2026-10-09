from crewai import Task


def create_competitor_research_task(agent):
    return Task(
        description=(
            "Research the main competitors of {company}. "
            "Identify their products or services, target customers, "
            "market position, strengths, weaknesses, and competitive advantages. "
            "Compare the competitors with the target company."
        ),
        expected_output=(
            "A structured competitor research report containing major "
            "competitors, their products or services, target customers, "
            "market position, strengths, weaknesses, competitive advantages, "
            "and comparison with the target company."
        ),
        agent=agent,
    )