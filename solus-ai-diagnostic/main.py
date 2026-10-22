from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:8b"


class DiagnosisRequest(BaseModel):
    issue: str


@app.get("/")
def health():
    return {
        "status": "running",
        "model": MODEL_NAME
    }


@app.post("/diagnose")
def diagnose(request: DiagnosisRequest):

    prompt = f"""
You are a technical diagnostic assistant.

Analyze this issue:

{request.issue}

Return:
1. Issue summary
2. Possible causes
3. Information missing
4. Recommended next step
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return {
        "diagnosis": result["response"]
    }