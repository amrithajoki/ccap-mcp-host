from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def health():
    return {"status": "CCAP MCP Host running"}

@app.post("/query")
def query(req: PromptRequest):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are CCAP, a CRM assistant for Salesforce and HubSpot."},
            {"role": "user", "content": req.prompt}
        ]
    )
    return {"response": response.choices[0].message.content}