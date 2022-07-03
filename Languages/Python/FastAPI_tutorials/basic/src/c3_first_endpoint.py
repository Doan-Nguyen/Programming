import re
from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"Olleh": "world"}