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
    liver_problem: Optional[bool]
    kidney_problem: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "blood_group": "AB+",
                "allergies": ["Peanuts", "Shellfish"],
                "heart_condition": False,
                "diabetes": True,
                "smoking_history": None,
                "asthema": None,
            }
        }


class PhysicalAttribute(BaseModel):
    name: str
    value: float
    date_added: date

    class Config:
        schema_extra = {
            "example": {"name": "Height", "value": 170.5, "date_added": "2022-01-01"}
        }


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

    class Config:
        schema_extra = {
            "example": {
                "patient_id": "1234",
                "name": "Dhrubo Kamal",
                "identification_no": "5678",
                "date_of_brth": "1980-01-01",
                "address": "123 Main St.",
                "phone_no": "555-1234",
                "email": "jane@example.com",
                "profession": "Engineer",
                "general_information": GeneralInformation.Config.schema_extra[
                    "example"
                ],
                "physical_attributes": [
                    PhysicalAttribute.Config.schema_extra["example"]
                ],
            }
        }


class PatientInput(BaseModel):
    name: str
    identification_no: str
    date_of_brth: date
    address: str
    phone_no: str
    email: str
    profession: str
    general_information: GeneralInformation
    physical_attributes: Optional[list[PhysicalAttribute]]

    class Config:
        schema_extra = {
            "example": {
                "name": "Dhrubo Kamal",
                "identification_no": "5678",
                "date_of_brth": "1980-01-01",
                "address": "123 Main St.",
                "phone_no": "555-1234",
                "email": "jane@example.com",
                "profession": "Engineer",
                "general_information": GeneralInformation.Config.schema_extra[
                    "example"
                ],
                "physical_attributes": [
                    PhysicalAttribute.Config.schema_extra["example"]
                ],
            }
        }
