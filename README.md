# 📊 Financial Document Analyzer (FastAPI + CrewAI)

This project is a **Financial Document Analyzer** built with **FastAPI** and **CrewAI**.  
It allows users to upload financial PDF reports, processes them using custom tools, and generates **structured insights, risk assessments, and investment recommendations** with the help of AI agents.

---

## 🚀 Features
- Upload **financial PDF documents** via REST API
- Extract text from PDFs with **LangChain’s PyPDFLoader**
- AI-powered analysis using **CrewAI agents + tasks**
- Provides:
  - ✅ Key metrics & trends  
  - ✅ Investment opportunities  
  - ✅ Risk assessments  
  - ✅ Verification of findings  
- Interactive **Swagger UI** docs at `/docs`

---

## 🛠 Tech Stack
- **Python 3.10+**
- [FastAPI](https://fastapi.tiangolo.com/) – REST API
- [CrewAI](https://github.com/joaomdmoura/crewAI) – Multi-agent framework
- [CrewAI Tools](https://pypi.org/project/crewai-tools/) – extra integrations
- [LangChain Community](https://python.langchain.com/docs/) – PDF parsing
- [Pydantic v2](https://docs.pydantic.dev/) – data validation
- [Uvicorn](https://www.uvicorn.org/) – ASGI server

---

## 📂 Project Structure
financial-document-analyzer/
├── agents.py # AI agent definitions
├── tools.py # Custom tools (PDF reader, risk, investment, search)
├── task.py # Task definitions
├── main.py # FastAPI entrypoint (API)
├── data/ # Sample PDFs (ignored in git)
├── uploads/ # Uploaded PDFs (ignored in git)
├── .env # API keys (ignored in git)
├── requirements.txt # Python dependencies
└── README.md # Documentation

yaml
Copy code

---

## ▶️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/financial-document-analyzer.git
cd financial-document-analyzer
2. Create a virtual environment
bash
Copy code
python -m venv venv
# Activate it:
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root:

ini
Copy code
OPENAI_API_KEY=sk-xxxxxx
SERPER_API_KEY=xxxxxx
⚠️ Never commit .env — it is ignored by .gitignore.

5. Run the API
bash
Copy code
uvicorn main:app --reload
Server will start at:
👉 http://127.0.0.1:8000

Swagger UI docs:
👉 http://127.0.0.1:8000/docs

📌 Example Usage
Go to Swagger UI

Expand POST /analyze

Upload a financial PDF (e.g. Tesla Q2 report)

Add an optional query (e.g. "Summarize risks and opportunities")

Execute → get a JSON response with:

Extracted summary

Risks

Opportunities

Recommendations

🛠 Corrections & Fixes Made
During development, several fixes were required:

Wrong tool import

❌ from crewai import tool

✅ Fixed with from crewai.tools import tool

Virtual environment pushed by mistake

venv/ was committed (huge files rejected by GitHub).

Fixed by adding venv/ to .gitignore and removing it from Git history.

Secrets committed accidentally

.env with API keys was pushed.

GitHub Push Protection blocked it.

Fixed by removing .env from history, rotating keys, and ignoring .env.

Tools were plain functions, not Tool objects

Error: 'function' object has no attribute 'get'

Fixed by properly decorating tools with @tool from crewai.tools.

File uploads failed

Error: "Form data requires 'python-multipart' to be installed"

Fixed with:

bash
Copy code
pip install python-multipart
⚠️ Notes
Always run in a virtual environment (venv/)

Always use .gitignore to exclude:

venv/

.env

uploads/

data/*.pdf

Always rotate API keys if they were exposed

Use requirements.txt so others can recreate the environment

📜 License
MIT License – free to use and modify.
