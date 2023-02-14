from pydantic import BaseModel
from datetime import date
from typing import Optional


class GeneralInformation(BaseModel):
    blood_group: str
    allergies: Optional[list[str]]
    heart_condition: Optional[bool]
    diabetes: Optional[bool]
    smoking_history: Optional[bool]
    asthema: Optional[bool]


class PhysicalAttribute(BaseModel):
    name: str
    value: float
    date_added: date


class Patient(BaseModel):
    patient_id: str
    name: str
    identification_no: str
    date_of_brth: date
    address: str
    phone_no: str
    email: str
    profession: str
    general_information: GeneralInformation
    physical_attributes: Optional[list[PhysicalAttribute]]
