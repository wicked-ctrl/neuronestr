from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from app.database import create_db_and_tables

# ── lifespan callback replaces the old @app.on_event("startup") ──────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield        # ← FastAPI will run any shutdown logic *after* this line

app = FastAPI(
    title="NeuroNestr API",
    version="0.1.0",
    lifespan=lifespan,
)

class PingResponse(BaseModel):
    message: str

@app.get("/ping", response_model=PingResponse)
async def ping():
    return {"message": "pong 🏓"}
