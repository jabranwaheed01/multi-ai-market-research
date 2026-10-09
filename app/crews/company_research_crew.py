from crewai import Crew, Process

from app.agents.company_research_agent import create_company_research_agent
from app.agents.competitor_research_agent import create_competitor_research_agent
from app.agents.market_trends_agent import create_market_trends_agent
from app.agents.data_analyst_agent import create_data_analyst_agent
from app.agents.strategy_agent import create_strategy_agent
from app.agents.report_writer_agent import create_report_writer_agent
from app.agents.qa_agent import create_qa_agent

from app.tasks.company_research_task import create_company_research_task
from app.tasks.competitor_research_task import create_competitor_research_task
from app.tasks.market_trends_task import create_market_trends_task
from app.tasks.data_analysis_task import create_data_analysis_task
from app.tasks.strategy_task import create_strategy_task
from app.tasks.report_writing_task import create_report_writing_task
from app.tasks.qa_task import create_qa_task
from app.tasks.report_revision_task import create_report_revision_task


def create_research_crew():
    company_agent = create_company_research_agent()
    competitor_agent = create_competitor_research_agent()
    market_agent = create_market_trends_agent()
    data_agent = create_data_analyst_agent()
    strategy_agent = create_strategy_agent()
    report_agent = create_report_writer_agent()
    qa_agent = create_qa_agent()

    company_task = create_company_research_task(company_agent)

    competitor_task = create_competitor_research_task(
        competitor_agent
    )
    competitor_task.context = [company_task]

    market_task = create_market_trends_task(
        market_agent
    )
    market_task.context = [
        competitor_task,
    ]

    data_task = create_data_analysis_task(
        data_agent
    )
    data_task.context = [
        market_task,
        competitor_task,
    ]

    strategy_task = create_strategy_task(
        strategy_agent
    )
    strategy_task.context = [
        data_task,
    ]

    report_task = create_report_writing_task(
        report_agent
    )
    report_task.context = [
        strategy_task,
    ]

    qa_task = create_qa_task(
        qa_agent
    )
    qa_task.context = [
        report_task,
    ]

    revision_task = create_report_revision_task(
        report_agent,
        report_task,
        qa_task,
    )

    crew = Crew(
        agents=[
            company_agent,
            competitor_agent,
            market_agent,
            data_agent,
            strategy_agent,
            report_agent,
            qa_agent,
        ],
        tasks=[
            company_task,
            competitor_task,
            market_task,
            data_task,
            strategy_task,
            report_task,
            qa_task,
            revision_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    return crew