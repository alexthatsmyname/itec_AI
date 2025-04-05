from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.api import nlp

load_dotenv()

app = FastAPI(title="Smart Healthcare Assistant")

# Adăugăm CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL-ul frontend-ului
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nlp.router, prefix="/nlp", tags=["NLP"])

@app.get("/")
def read_root():
    return {"message": "Welcome to our app!"}