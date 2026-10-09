from crewai import Task


def create_qa_task(agent):
    return Task(
        description=(
            "Review the business intelligence report for {company}. "
            "Check the report for accuracy, completeness, clarity, "
            "consistency, weak conclusions, missing information, and "
            "unsupported recommendations. Identify the issues that "
            "must be corrected before the report is finalized."
        ),
        expected_output=(
            "A structured quality assurance review containing identified "
            "issues, missing information, accuracy concerns, and specific "
            "corrections or improvements required before finalization."
        ),
        agent=agent,
    )