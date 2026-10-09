
# import time, requests, gradio as gr

# API = "http://localhost:8000"
# AGENTS = ["Company Research Agent", "Competitor Research Agent", "Market Trends Agent",
#           "Data Analysis Agent", "Strategic Analysis Agent", "Report Writer Agent", "QA Reviewer Agent"]

# def progress_md(current, status):
#     lines = []
#     idx = AGENTS.index(current) if current in AGENTS else -1
#     for i, a in enumerate(AGENTS):
#         if status == "completed" or i < idx: lines.append(f"✓ {a}")
#         elif i == idx: lines.append(f"→ **{a}**")
#         else: lines.append(f"○ {a}")
#     return "\n\n".join(lines)

# def run(company, industry, objective, depth):
#     r = requests.post(f"{API}/research", json={
#         "company": company, "industry": industry,
#         "research_objective": objective, "depth": depth})
#     rid = r.json()["job_id"]
#     while True:
#         s = requests.get(f"{API}/research/{rid}/status").json()
#         status = s.get("status")
#         if status is None:
#             yield f"API response missing status: {s}", "", None
#             return
#         yield progress_md(s.get("current_agent"), status), "", None

#         if s["status"] in ("completed", "failed"):
#             break
#         time.sleep(3)
#     report = requests.get(f"{API}/research/{rid}/report").json()["content"]
#     path = f"report_{rid}.md"
#     open(path, "w").write(report)
#     yield progress_md(None, s["status"]), report, path

# with gr.Blocks() as demo:
#     gr.Markdown("# AI Market Research System")
#     company = gr.Textbox(label="Company")
#     industry = gr.Textbox(label="Industry")
#     objective = gr.Textbox(label="Research Objective", lines=3)
#     depth = gr.Radio(["Basic", "Detailed"], value="Detailed", label="Research Depth")
#     btn = gr.Button("Start Research")
#     progress = gr.Markdown()
#     report = gr.Markdown()
#     download = gr.File(label="Download Report")
#     btn.click(run, [company, industry, objective, depth], [progress, report, download])

# demo.launch()





import time
from pathlib import Path

import requests
import gradio as gr

API = "http://127.0.0.1:8000"

AGENTS = [
    "Company Research Agent",
    "Competitor Research Agent",
    "Market Trends Agent",
    "Data Analysis Agent",
    "Strategic Analysis Agent",
    "Report Writer Agent",
    "QA Reviewer Agent",
]


def progress_md(current, status):
    lines = []

    try:
        idx = AGENTS.index(current) if current in AGENTS else -1
    except ValueError:
        idx = -1

    for i, agent in enumerate(AGENTS):
        if status == "completed":
            lines.append(f"✅ {agent}")
        elif status == "failed":
            lines.append(f"⚠️ {agent}")
        elif idx >= 0 and i < idx:
            lines.append(f"✅ {agent}")
        elif i == idx:
            lines.append(f"🔄 **{agent}**")
        else:
            lines.append(f"⏳ {agent}")

    return "\n\n".join(lines)


def run(company, industry, objective, depth):
    if not company or not company.strip():
        yield "Please enter a company name.", "", None
        return

    # Start research
    try:
        response = requests.post(
            f"{API}/research",
            json={
                "company": company.strip(),
                "industry": industry,
                "research_objective": objective,
                "depth": depth,
            },
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()

        rid = data.get("job_id")

        if not rid:
            yield f"Could not start research:\n\n{data}", "", None
            return

    except requests.RequestException as exc:
        yield (
            f"Could not connect to FastAPI: {exc}\n\n"
            "Check that the FastAPI server is running on port 8000."
        ), "", None
        return

    # Poll the existing job
    while True:
        try:
            response = requests.get(
                f"{API}/research/{rid}",
                timeout=20,
            )
            response.raise_for_status()
            result = response.json()

        except requests.RequestException as exc:
            yield f"Could not fetch research status: {exc}", "", None
            return

        status = result.get("status", "unknown")
        current_agent = result.get("current_agent")

        progress = (
            f"**Job ID:** `{rid}`\n\n"
            f"**Status:** {status}\n\n"
            f"{progress_md(current_agent, status)}"
        )

        report = result.get("report") or ""

        if status in ("completed", "failed"):
            if not report:
                report = (
                    "Research completed, but no report was returned."
                    if status == "completed"
                    else "Research failed. Check the FastAPI terminal for details."
                )

            report_path = Path(f"report_{rid}.md")
            report_path.write_text(report, encoding="utf-8")

            yield progress, report, str(report_path)
            return

        yield progress, report, None
        time.sleep(3)


with gr.Blocks() as demo:
    gr.Markdown("# AI Market Research System")

    company = gr.Textbox(label="Company")
    industry = gr.Textbox(label="Industry")
    objective = gr.Textbox(
        label="Research Objective",
        lines=3,
    )

    depth = gr.Radio(
        ["Basic", "Detailed"],
        value="Detailed",
        label="Research Depth",
    )

    btn = gr.Button("Start Research")
    progress = gr.Markdown()
    report = gr.Markdown()
    download = gr.File(label="Download Report")

    btn.click(
        run,
        inputs=[company, industry, objective, depth],
        outputs=[progress, report, download],
    )

demo.launch()