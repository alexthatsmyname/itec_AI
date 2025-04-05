from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.core.llm_client import get_diagnosis_from_llm

router = APIRouter()

class Message(BaseModel):
    text: str
    sender: str

class ConversationInput(BaseModel):
    current_message: str
    conversation_history: List[Message]

@router.post("/assess")
def assess_symptoms(data: ConversationInput):
    # Construim contextul din istoricul conversației
    context = "\n".join([
        f"{'Assistant' if msg.sender == 'bot' else 'User'}: {msg.text}"
        for msg in data.conversation_history
    ])
    
    # Adăugăm mesajul curent
    full_context = f"{context}\nUser: {data.current_message}"
    
    # Obținem diagnosticul cu tot contextul
    diagnosis = get_diagnosis_from_llm(full_context)
    return {"diagnosis": diagnosis}
