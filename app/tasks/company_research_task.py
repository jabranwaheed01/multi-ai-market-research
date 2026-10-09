from crewai import Task


def create_company_research_task(agent):
    return Task(
        description=(
            "Research the target company: {company}. "
            "Identify its main products or services, target customers, "
            "market position, strengths, weaknesses, and major business "
            "opportunities. Present the findings in a clear and structured format."     
            ),
        expected_output=(
            "A structured company research report containing company overview, "
            "products or services, target customers, market position, "
            "strengths, weaknesses, and business opportunities."
        ),
        agent=agent,
    )

