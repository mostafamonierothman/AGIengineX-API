# app.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AGIengineX API is LIVE!", "status": "OK"}

@app.get("/next_move")
def next_move():
    return {"next_move": "Here is your next move!"}

@app.get("/opportunity")
def opportunity():
    return {"opportunity": "Here is your opportunity!"}

@app.post("/run_agent")
async def run_agent(request: Request):
    data = await request.json()
    agent_name = data.get("agent_name")
    input_data = data.get("input", {})

    # Simulated agent result
    result = f"Agent '{agent_name}' ran with input {input_data}!"

    return {"result": result}
