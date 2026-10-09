from crewai import Task


def create_strategy_task(agent):
    return Task(
        description=(
            "Using the research findings for {company}, develop practical "
            "business strategies and recommendations. Identify growth "
            "opportunities, competitive actions, market opportunities, "
            "and specific actions the company should consider."
        ),
        expected_output=(
            "A structured business strategy report containing key "
            "recommendations, growth opportunities, competitive strategies, "
            "and actionable next steps."
        ),
        agent=agent,
    )
