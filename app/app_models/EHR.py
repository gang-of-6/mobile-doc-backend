from pydantic import BaseModel, constr
from typing import Optional, List
from datetime import datetime


class Medicine(BaseModel):
    name: str
    generic_name: str
    precautions: Optional[list[str]]


class CorrelatedSymptoms(BaseModel):
    symptom_name: str
    correlated_symptoms: list[str]
    required_doctor_speciality: list[str]


class SymptomEntry(BaseModel):
    symptom_name: str
    duration: Optional[int]
    added_by: constr(regex="doctor|patient")

    class Config:
        schema_extra = {
            "example": {"symptom_name": "fever", "duration": 2, "added_by": "patient"}
        }


class Session(BaseModel):
    session_id: str
    patient_id: str
    doctor_id: Optional[str]  # Need to create a session before selecting doctor.
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    video_call_link: Optional[str]
    Diagonosis: Optional[str]
    advice: Optional[str]
    symptom_list: Optional[List[SymptomEntry]] = []
    suggested_test_list: Optional[list[str]] = []
