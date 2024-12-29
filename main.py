from typing import Union
import os

from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import graph

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/run-graph")
async def run_graph(data: dict):
    result = graph.run("Analyzer", data)
    return {"status": "success", "result": result}