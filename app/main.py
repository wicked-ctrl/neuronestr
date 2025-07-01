from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NeuroNestr API", version="0.1.0")


class PingResponse(BaseModel):
    message: str


@app.get("/ping", response_model=PingResponse)
async def ping():
    return {"message": "pong 🏓"}
