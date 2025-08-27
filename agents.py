# agents.py
from financial_tools import financial_document_tool
from crewai import Agent, LLM
from tools import (
    financial_document_tool,
    analyze_investment_tool,
    create_risk_assessment_tool,
    search_tool,
)

# Configure the LLM used by your agents
# (Adjust model/temperature per your setup; works with litellm/OpenAI routing)
llm = LLM(model="gpt-3.5-turbo", temperature=0.3)

financial_analyst = Agent(
    role="Financial Analyst",
    goal=(
        "Read the uploaded financial document, extract key numbers and sections, "
        "identify risks/opportunities, and produce clear, actionable insights."
    ),
    backstory=(
        "A meticulous analyst experienced in financial statements, ratios, and risk assessment. "
        "Focuses on grounded, verifiable outputs with brief, helpful summaries."
    ),
    tools=[
        financial_document_tool,
        analyze_investment_tool,
        create_risk_assessment_tool,
        search_tool,
    ],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# Optional second agent if you reference `verifier` in task.py
verifier = Agent(
    role="Compliance Verifier",
    goal=(
        "Verify that conclusions are supported by the provided document text. "
        "Flag hallucinations and request clarifications when data is missing."
    ),
    backstory="A careful reviewer ensuring outputs are consistent with the source document.",
    tools=[financial_document_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)
