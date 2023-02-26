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


class Prescription(BaseModel):
    Diagonosis: str
    advice: str
    suggested_test_list: list[str]
    suggested_medicine_list: list[str]

    class Config:
        schema_extra = {
            "example": {
                "Diagonosis": "Seasonal Viral Fever",
                "advice": "Take rest for 2 days.",
                "suggested_test_list": ["CBC test", "Chest X-ray"],
                "suggested_medicine_list": ["Napa", "Seclo"],
            }
        }


class TestDataEntry(BaseModel):
    data_element: str
    data_value: float
    data_unit: str


class TestFileEntry(BaseModel):
    file_name: str
    file_url: str


class TestResult(BaseModel):
    test_result_id: str
    test_name: str
    date: datetime
    numeric_results: Optional[list[TestDataEntry]]
    test_files: Optional[list[TestFileEntry]]
