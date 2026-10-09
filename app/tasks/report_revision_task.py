from crewai import Task


def validate_revised_report(result):
    if not result or len(str(result).strip()) < 500:
        return (
            False,
            "The revised report is too short or incomplete. "
            "Provide a complete professional business intelligence report."
        )

    return True, result


def create_report_revision_task(agent, report_task, qa_task):
    return Task(
        description=(
            "Revise the business intelligence report for {company}. "
            "Use the original report and the QA review as context. "
            "Fix all identified accuracy, completeness, clarity, "
            "consistency, and recommendation issues. "
            "Return a corrected and professional final report."
        ),
        expected_output=(
            "A corrected final business intelligence report that addresses "
            "the issues identified by the QA review."
        ),
        agent=agent,
        context=[report_task, qa_task],
        guardrail=validate_revised_report,
        guardrail_max_retries=2,
    )