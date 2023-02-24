from pydantic import BaseModel


class Doctor(BaseModel):
    doctor_id: str
    name: str
    designation: str
    degrees: str  # list of degrees seperated by comma
    speciality: str
