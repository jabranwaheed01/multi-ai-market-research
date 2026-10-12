from crewai import LLM

def get_llm():
    return LLM(
        model="ollama/llama3.2:1b ",
        base_url="http://localhost:11434",
        temperature=0.2,
        max_tokens=500,
    )



# import os
# from dotenv import load_dotenv
# from crewai import LLM

# load_dotenv()


# def get_llm():
#     return LLM(
#         model="groq/openai/gpt-oss-20b",
#         api_key=os.getenv("GROQ_API_KEY"),
#         temperature=0.2,
#         max_tokens=500,
#     )






# import os
# from dotenv import load_dotenv
# from crewai import LLM

# load_dotenv()


# def get_llm():
#     api_key = os.getenv("GEMINI_API_KEY")

#     if not api_key:
#         raise ValueError("GEMINI_API_KEY is missing from .env")

#     return LLM(
#         model="gemini/gemini-2.5-flash",
#         api_key=api_key,
#         temperature=0.2,
#     )

