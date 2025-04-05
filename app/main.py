from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.api import nlp

load_dotenv()

app = FastAPI(title="Smart Healthcare Assistant")

app.include_router(nlp.router, prefix="/nlp", tags=["NLP"])
@app.get("/")
def read_root():
    return {"message": "Welcome to our app!"}