from crewai import Task


def create_competitor_research_task(agent):
    return Task(
        description=(
            "Research the main competitors of {company}. "
            "Identify direct and indirect competitors, their products or "
            "services, target customers, market position, strengths, "
            "weaknesses, pricing or business models when reliable information "
            "is available, and competitive advantages. Compare competitors "
            "with the target company and identify market gaps and potential "
            "competitive threats. Use reliable evidence where available. "
            "Do not invent facts, figures, or sources, and clearly state "
            "when information cannot be verified."
        ),
        expected_output=(
            "A structured competitor research report containing direct and "
            "indirect competitors, products or services, target customers, "
            "market position, strengths, weaknesses, business models where "
            "available, competitive advantages, comparison with the target "
            "company, market gaps, and competitive threats. Include source "
            "references when available and distinguish verified facts from "
            "estimates."
        ),
        agent=agent,
    )
