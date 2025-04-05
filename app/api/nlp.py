from fastapi import APIRouter
from pydantic import BaseModel
from app.core.llm_client import get_diagnosis_from_llm

router = APIRouter()

class SymptomInput(BaseModel):
    symptoms: str

@router.post("/assess")
def assess_symptoms(data: SymptomInput):
    diagnosis = get_diagnosis_from_llm(data.symptoms)
    return {"diagnosis": diagnosis}
