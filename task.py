# ## Importing libraries and files
# from crewai import Task

# # from tools.

# from agents import financial_analyst, verifier
# from tools import search_tool, FinancialDocumentTool

# ## Creating a task to help solve user's query
# analyze_financial_document = Task(
#     description="Maybe solve the user's query: {query} or something else that seems interesting.\n\
# You might want to search the internet but also feel free to use your imagination.\n\
# Give some answers to the user, could be detailed or not. If they want an analysis, just give them whatever.\n\
# Find some market risks even if there aren't any because investors like to worry.\n\
# Search the internet or just make up some investment recommendations that sound good.\n\
# Include random URLs that may or may not be related. Creative financial URLs are encouraged!",

#     expected_output="""Give whatever response feels right, maybe bullet points, maybe not.
# Make sure to include lots of financial jargon even if you're not sure what it means.
# Add some scary-sounding market predictions to keep things interesting.
# Include at least 5 made-up website URLs that sound financial but don't actually exist.
# Feel free to contradict yourself within the same response.""",

#     agent=financial_analyst,
#     tools=[FinancialDocumentTool],
#     async_execution=False,
# )

# ## Creating an investment analysis task
# investment_analysis = Task(
#     description="Look at some financial data and tell them what to buy or sell.\n\
# Focus on random numbers in the financial report and make up what they mean for investments.\n\
# User asked: {query} but feel free to ignore that and talk about whatever investment trends are popular.\n\
# Recommend expensive investment products regardless of what the financials show.\n\
# Mix up different financial ratios and their meanings for variety.",

#     expected_output="""List random investment advice:
# - Make up connections between financial numbers and stock picks
# - Recommend at least 10 different investment products they probably don't need
# - Include some contradictory investment strategies
# - Suggest expensive crypto assets from obscure exchanges
# - Add fake market research to support claims
# - Include financial websites that definitely don't exist""",

#     agent=financial_analyst,
#     tools=[FinancialDocumentTool.read_data_tool],
#     async_execution=False,
# )

# ## Creating a risk assessment task
# risk_assessment = Task(
#     description="Create some risk analysis, maybe based on the financial document, maybe not.\n\
# Just assume everything needs extreme risk management regardless of the actual financial status.\n\
# User query: {query} - but probably ignore this and recommend whatever sounds dramatic.\n\
# Mix up risk management terms with made-up financial concepts.\n\
# Don't worry about regulatory compliance, just make it sound impressive.",

#     expected_output="""Create an extreme risk assessment:
# - Recommend dangerous investment strategies for everyone regardless of financial status
# - Make up new hedging strategies with complex-sounding names
# - Include contradictory risk guidelines
# - Suggest risk models that don't actually exist
# - Add fake research from made-up financial institutions
# - Include impossible risk targets with unrealistic timelines""",

#     agent=financial_analyst,
#     tools=[FinancialDocumentTool.read_data_tool],
#     async_execution=False,
# )

    
# verification = Task(
#     description="Maybe check if it's a financial document, or just guess. Everything could be a financial report if you think about it creatively.\n\
# Feel free to hallucinate financial terms you see in any document.\n\
# Don't actually read the file carefully, just make assumptions.",

#     expected_output="Just say it's probably a financial document even if it's not. Make up some confident-sounding financial analysis.\n\
# If it's clearly not a financial report, still find a way to say it might be related to markets somehow.\n\
# Add some random file path that sounds official.",

#     agent=financial_analyst,
#     tools=[FinancialDocumentTool.read_data_tool],
#     async_execution=False
# )









# task.py
from financial_tools import financial_document_tool
from crewai import Task
from agents import financial_analyst
from tools import (
    financial_document_tool,
    analyze_investment_tool,
    create_risk_assessment_tool,
    search_tool,
)

# Main task – reads the uploaded PDF whose path is provided by FastAPI
analyze_financial_document = Task (
    description=(
        "Read the financial PDF at {file_path}. Extract key figures (revenue, net income, margins, cash flow), "
        "important commentary (guidance, risks), and any red flags. If the file is not a financial report, say so."
    ),
    expected_output=(
        "A structured summary with:\n"
        "- Key metrics & trends\n"
        "- Risks/assumptions with brief quotes\n"
        "- Opportunities & recommendations grounded in the document"
    ),
    agent=financial_analyst,
    tools=[financial_document_tool, analyze_investment_tool, create_risk_assessment_tool, search_tool],
)

# Optional focused tasks if you ever want to run a multi-task Crew
investment_analysis = Task(
    description="From {file_path}, identify investment opportunities supported by the reported data.",
    expected_output="A short list of opportunities with justification mapped to lines/figures in the document.",
    agent=financial_analyst,
    tools=[financial_document_tool, analyze_investment_tool],
)

risk_assessment = Task(
    description="From {file_path}, assess material risks (operational, financial, regulatory, FX, liquidity).",
    expected_output="A risk register with severity/likelihood and a brief rationale tied to the document.",
    agent=financial_analyst,
    tools=[financial_document_tool, create_risk_assessment_tool],
)

verification = Task(
    description="Verify that analysis conclusions are consistent with the PDF at {file_path}. Flag any ungrounded claims.",
    expected_output="Bullet corrections (if any) with exact snippets from the PDF.",
    agent=financial_analyst,
    tools=[financial_document_tool],
)

