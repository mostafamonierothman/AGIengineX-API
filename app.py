# app.py
from fastapi import FastAPI, Request

# Mock agents — replace with real ones later
def get_next_move():
    return "Move: Execute strategic task."

def get_opportunity():
    return "Opportunity: Explore new market."

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AGIengineX is LIVE!", "status": "OK"}

@app.get("/next_move")
def next_move_endpoint():
    result = get_next_move()
    return {"next_move": result}

@app.get("/opportunity")
def opportunity_endpoint():
    result = get_opportunity()
    return {"opportunity": result}

@app.post("/run_agent")
async def run_agent(request: Request):
    data = await request.json()
    agent_name = data.get("agent_name")
    input_data = data.get("input", None)

    # Dispatch to correct agent
    if agent_name == "next_move_agent":
        return {"result": get_next_move()}
    elif agent_name == "opportunity_agent":
        return {"result": get_opportunity()}
    else:
        return {"error": f"Unknown agent: {agent_name}"}
