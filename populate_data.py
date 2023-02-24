from fastapi.encoders import jsonable_encoder
import pymongo

from pydantic import BaseModel
from typing import Optional


client = pymongo.MongoClient(
    "mongodb+srv://user:1234@cluster0.ds5ggbq.mongodb.net/?retryWrites=true&w=majority"
)

db = client.get_database("main_db")


class Doctor(BaseModel):
    doctor_id: str
    name: str
    designation: str
    degrees: str  # list of degrees seperated by comma
    speciality: str


doctor_list = [
    {
        "doctor_id": "BD014",
        "name": "Dr. Tanjil Ahmed",
        "designation": "Assistant Professor",
        "degrees": "MBBS, MD",
        "speciality": "Pulmonologist",
    },
    {
        "doctor_id": "BD015",
        "name": "Dr. Ayesha Khan",
        "designation": "Consultant",
        "degrees": "MBBS, FCPS",
        "speciality": "Medicine",
    },
]


for x in doctor_list:
    x = Doctor.parse_obj(x)
    x = jsonable_encoder(x)
    db_result = db.doctor.insert_one(x)
    print(db_result.inserted_id)
    print(x)
