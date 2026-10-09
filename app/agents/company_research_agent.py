# from crewai import Agent


# def create_company_research_agent():
#     return Agent(
#         role="Company Research Specialist",
#         goal=(
#             "Research the target company and provide accurate information "
#             "about its products, services, target customers, market position, "
#             "and business opportunities."
#         ),
#         backstory=(
#             "You are an experienced business researcher specializing in "
#             "company analysis and market research. You focus on finding "
#             "relevant and reliable information that can support business decisions."
#         ),
#         max_iter=1,
#         verbose=True,
#     )




from crewai import Agent

from app.llm import get_llm


def create_company_research_agent():
    return Agent(
        role="Company Research Specialist",
        goal=(
            "Research the target company and provide accurate information "
            "about its products, services, target customers, market position, "
            "and business opportunities."
        ),
        backstory=(
            "You are an experienced business researcher specializing in "
            "company analysis and market research."
        ),
        llm=get_llm(),
        max_iter=1,
        max_retry_limit=0,
        use_system_prompt=False,
        verbose=True,
    )