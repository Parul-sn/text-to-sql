from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline import run

app = FastAPI(title="Text-to-SQL")


class Query(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query")
def query(q: Query):
    return run(q.question)