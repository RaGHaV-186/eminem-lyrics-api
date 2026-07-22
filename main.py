from fastapi import FastAPI 
from model import load_model, generate_text
from pydantic import BaseModel,Field

model, stoi, itos = load_model("eminem_gpt.pt")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status":"Alive"}

class GenerateRequest(BaseModel):
    prompt : str
    max_tokens : int = Field(default = 100, ge = 1, le=500)

@app.post("/generate")
def generate(request: GenerateRequest):
    output = generate_text(model, stoi, itos, request.prompt, request.max_tokens)
    return {"prompt": request.prompt, "output": output}