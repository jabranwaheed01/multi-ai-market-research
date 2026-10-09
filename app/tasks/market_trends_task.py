from crewai import Task


def create_market_trends_task(agent):
    return Task(
        description=(
            "Research the current market trends related to {company}. "
            "Identify major industry changes, customer behavior trends, "
            "emerging technologies, market growth opportunities, and "
            "important future developments."
        ),
        expected_output=(
            "A structured market trends report covering current industry "
            "trends, customer trends, emerging technologies, growth "
            "opportunities, and future market developments."
        ),
        agent=agent,
    )