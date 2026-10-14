from crewai import Task


def create_company_research_task(agent):
    return Task(
        description=(
            "Research the target company: {company}. "
            "Identify its main products or services, target customers, "
            "market position, strengths, weaknesses, and major business "
            "opportunities. Include recent developments when reliable "
            "information is available. Distinguish verified facts from "
            "estimates, and do not invent statistics or sources. "
            "Organize findings under clear headings and explain how each "
            "finding may affect the company's business performance."
        ),
        expected_output=(
            "A structured company research report containing a company "
            "overview, products or services, target customers, market "
            "position, strengths, weaknesses, and business opportunities. "
            "Include relevant evidence and source references when available, "
            "and clearly identify information that could not be verified."
        ),
        agent=agent,
    )
