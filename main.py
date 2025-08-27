from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio
import traceback

from financial_tools import financial_document_tool
from crewai import Crew
from agents import financial_analyst
from task import analyze_financial_document

# from .task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")

from crewai import Crew
from agents import financial_analyst
from task import analyze_financial_document

def run_crew(query: str, file_path: str):
    crew = Crew(
        agents=[financial_analyst],  # ✅ agent object, not function
        tasks=[analyze_financial_document],  # ✅ Task object
        verbose=True,
    )
    return crew.kickoff(inputs={"query": query, "file_path": file_path})

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_financial_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """Analyze financial document and provide comprehensive investment recommendations"""
    
    file_id = str(uuid.uuid4())
    base_dir = f"D:\\Internship\\financial-document-analyzer-debug (1)\\financial-document-analyzer-debug\\data"
    file_path = f"D:\\Internship\\financial-document-analyzer-debug (1)\\financial-document-analyzer-debug\\data/financial_document_{file_id}.pdf"
    # file_path = "D:\\Internship\\financial-document-analyzer-debug (1)\\financial-document-analyzer-debug\\data/financial_document_04024cd0-61f7-43e2-81ad-588439cd075e.pdf"
    print(file_path)
    
    try:
        # Ensure data directory exists
        os.makedirs(base_dir, mode=0o777, exist_ok=True)
        
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        file_path=f"D:\\Internship\\financial-document-analyzer-debug (1)\\financial-document-analyzer-debug\\data\\TSLA-Q2-2025-Update.pdf"
        # Validate query
        if query=="" or query is None:
            query = "Analyze this financial document for investment insights"
            
        # Process the financial document with all analysts
        response = run_crew(query=query.strip(), file_path=file_path)
        
        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }
        
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass  # Ignore cleanup errors

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)