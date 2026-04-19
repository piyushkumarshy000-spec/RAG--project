from fastapi import APIRouter
from app.services.rag_pipeline import run_rag

from app.core.guardrails import validate_query
from app.db.logger import log_query

router = APIRouter()

@router.get("/ask")
def ask(question: str):
    query = validate_query(question)
    
    answer = run_rag(query)
    
    log_query(query, answer)

    result = run_rag(query)

    return {
        "question": query,
        "answer": result["answer"],
        "sources": result["sources"]
        }
from fastapi import UploadFile, File, HTTPException
import shutil
from app.services.ingest_service import process_file

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):

    # ✅ Restrict file types
    if not file.filename.lower().endswith((".pdf", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF and TXT files allowed")

    file_path = f"data/{file.filename}"

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        chunks_added = process_file(file_path, file.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "message": "File uploaded successfully",
        "chunks_added": chunks_added
    }