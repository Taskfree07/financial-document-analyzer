# tools.py
import os
from dotenv import load_dotenv
from crewai.tools import tool           # ✅ correct place for the decorator
from crewai_tools import SerperDevTool  # ✅ built-in tool
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

# Built-in search tool (requires SERPER_API_KEY in your .env)
search_tool = SerperDevTool()

@tool("financial_document_tool")
def financial_document_tool(path: str = "data/sample.pdf") -> str:
    """Reads and extracts text from a financial PDF file."""
    # NOTE: requires `pip install langchain-community pypdf`
    docs = PyPDFLoader(path).load()
    parts = []
    for d in docs:
        content = d.page_content.replace("\r", "")
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")
        parts.append(content)
    return "\n".join(parts)

@tool("investment_analysis_tool")
def analyze_investment_tool(financial_document_data: str) -> str:
    """Analyzes investment opportunities in financial document data."""
    # TODO: implement real logic
    return "Investment analysis functionality to be implemented"

@tool("risk_assessment_tool")
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """Performs risk assessment on financial document data."""
    # TODO: implement real logic
    return "Risk assessment functionality to be implemented"
