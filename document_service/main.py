import os

from fastapi import FastAPI, HTTPException

STUDENT_N = int(os.getenv("STUDENT_N", "11"))
app = FastAPI(title=f"Document Service N{STUDENT_N}")

DOCUMENTS = {
    STUDENT_N * 100 + 1: {"id": STUDENT_N * 100 + 1, "title": "Syllabus of Medical Informatics", "type": "syllabus", "year": 2026, "status": "approved"},
    STUDENT_N * 100 + 2: {"id": STUDENT_N * 100 + 2, "title": "Working Program of Web Design in Medicine", "type": "work_program", "year": 2026, "status": "draft"},
}

@app.get("/health")
def health_check():
    return {"student_id": STUDENT_N, "service": "document-service", "status": "ok"}

@app.get("/documents")
def get_documents():
    return {"student_id": STUDENT_N, "count": len(DOCUMENTS), "documents": list(DOCUMENTS.values())}

@app.get("/documents/{document_id}")
def get_document(document_id: int):
    if document_id not in DOCUMENTS:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"student_id": STUDENT_N, "document": DOCUMENTS[document_id]}
