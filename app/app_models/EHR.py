from pydantic import BaseModel
from typing import Optional


class Medicine(BaseModel):
    name: str
    generic_name: str
    precautions: Optional[list[str]]


class CorrelatedSymptoms(BaseModel):
    symptom_name: str
    correlated_symptoms: list[str]
