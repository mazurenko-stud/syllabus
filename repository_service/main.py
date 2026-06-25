import os

import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

STUDENT_N = int(os.getenv("STUDENT_N", "11"))
DOCUMENT_SERVICE_URL = os.getenv("DOCUMENT_SERVICE_URL", "http://document-service-11:8000")

app = FastAPI(title=f"Repository Service N{STUDENT_N}")
REPOSITORY_RECORDS = []

class PublishRequest(BaseModel):
    document_id: int
    visibility: str = "public"

@app.get("/health")
def health_check():
    return {"student_id": STUDENT_N, "service": "repository-service", "status": "ok"}

@app.post("/repository/publish")
def publish_document(request: PublishRequest):
    try:
        response = requests.get(f"{DOCUMENT_SERVICE_URL}/documents/{request.document_id}", timeout=5)
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Document Service is unavailable")
    if response.status_code == 404:
        raise HTTPException(status_code=400, detail="Document does not exist")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Unexpected response from Document Service")
    document = response.json()["document"]
    record = {
        "record_id": len(REPOSITORY_RECORDS) + 1,
        "student_id": STUDENT_N,
        "document_id": document["id"],
        "document_title": document["title"],
        "document_type": document["type"],
        "visibility": request.visibility,
        "repository_url": f"https://www.syllabus.uno/repository/{document['id']}",
        "status": "published",
    }
    REPOSITORY_RECORDS.append(record)
    return {"student_id": STUDENT_N, "source_service": "repository-service", "linked_service": "document-service", "record": record}

@app.get("/repository/records")
def get_repository_records():
    return {"student_id": STUDENT_N, "count": len(REPOSITORY_RECORDS), "records": REPOSITORY_RECORDS}
