from fastapi import FastAPI
from pydantic import BaseModel
from brain import process_command

app = FastAPI(title="JARVIS Core")

class Command(BaseModel):
    text: str

@app.get("/")
def status():
    return {
        "name": "JARVIS",
        "status": "online",
        "version": "0.1"
    }

@app.post("/command")
def command(data: Command):
    return process_command(data.text)
