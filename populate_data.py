from fastapi.encoders import jsonable_encoder
import pymongo

from pydantic import BaseModel
from typing import Optional


client = pymongo.MongoClient(
    "mongodb+srv://user:1234@cluster0.ds5ggbq.mongodb.net/?retryWrites=true&w=majority"
)

db = client.get_database("main_db")


class CorrelatedSymptoms(BaseModel):
    symptom_name: str
    correlated_symptoms: list[str]
    required_doctor_speciality: list[str]


correlated_symptoms_list = [
    {
        "symptom_name": "cough",
        "correlated_symptoms": [
            "fever",
            "sore throat",
            "fatigue",
            "shortness of breath",
            "chest pain",
        ],
        "required_doctor_speciality": [
            "Pulmonologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "fever",
        "correlated_symptoms": [
            "cough",
            "headache",
            "nausea",
            "chills",
            "fatigue",
            "muscle aches",
        ],
        "required_doctor_speciality": [
            "Medicine",
        ],
    },
    {
        "symptom_name": "headache",
        "correlated_symptoms": [
            "fever",
            "fatigue",
            "dizziness",
            "nausea",
            "neck pain",
            "photophobia",
        ],
        "required_doctor_speciality": [
            "Neurologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "sore throat",
        "correlated_symptoms": [
            "cough",
            "fever",
            "swollen lymph nodes",
            "headache",
            "fatigue",
            "body aches",
        ],
        "required_doctor_speciality": [
            "ENT",
            "Medicine",
        ],
    },
    {
        "symptom_name": "fatigue",
        "correlated_symptoms": [
            "headache",
            "nausea",
            "muscle weakness",
            "joint pain",
            "fever",
            "chills",
            "dizziness",
        ],
        "required_doctor_speciality": [
            "Medicine",
        ],
    },
    {
        "symptom_name": "nausea",
        "correlated_symptoms": [
            "vomiting",
            "abdominal pain",
            "headache",
            "fatigue",
            "diarrhea",
            "dizziness",
            "heartburn",
        ],
        "required_doctor_speciality": [
            "Gastroenterologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "vomiting",
        "correlated_symptoms": [
            "nausea",
            "abdominal pain",
            "diarrhea",
            "headache",
            "fatigue",
            "dehydration",
            "fever",
            "chills",
        ],
        "required_doctor_speciality": [
            "Gastroenterologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "abdominal pain",
        "correlated_symptoms": [
            "vomiting",
            "diarrhea",
            "nausea",
            "fever",
            "chills",
            "bloating",
            "constipation",
            "back pain",
        ],
        "required_doctor_speciality": [
            "Gastroenterologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "diarrhea",
        "correlated_symptoms": [
            "abdominal pain",
            "nausea",
            "vomiting",
            "fever",
            "dehydration",
            "fatigue",
            "chills",
            "headache",
            "muscle cramps",
        ],
        "required_doctor_speciality": [
            "Gastroenterologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "shortness of breath",
        "correlated_symptoms": [
            "chest pain",
            "wheezing",
            "cough",
            "fatigue",
            "dizziness",
            "headache",
            "anxiety",
            "rapid heartbeat",
        ],
        "required_doctor_speciality": [
            "Pulmonologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "chest pain",
        "correlated_symptoms": [
            "shortness of breath",
            "arm pain",
            "back pain",
            "neck pain",
            "jaw pain",
            "nausea",
            "sweating",
            "anxiety",
            "heart palpitations",
        ],
        "required_doctor_speciality": [
            "Cardiologist",
            "Medicine",
        ],
    },
    {
        "symptom_name": "back pain",
        "correlated_symptoms": [
            "abdominal pain",
            "leg pain",
            "neck pain",
            "shoulder pain",
            "hip pain",
            "chest pain",
            "headache",
            "fatigue",
            "muscle weakness",
            "numbness",
        ],
        "required_doctor_speciality": [
            "Orthopedist",
        ],
    },
    {
        "symptom_name": "neck pain",
        "correlated_symptoms": [
            "headache",
            "shoulder pain",
            "back pain",
            "arm pain",
            "tingling",
            "numbness",
            "dizziness",
            "fatigue",
            "nausea",
            "jaw pain",
        ],
        "required_doctor_speciality": [
            "Orthopedist",
        ],
    },
    {
        "symptom_name": "shoulder pain",
        "correlated_symptoms": [
            "neck pain",
            "back pain",
            "arm pain",
            "headache",
            "chest pain",
            "numbness",
            "tingling",
            "stiffness",
            "fatigue",
            "dizziness",
        ],
        "required_doctor_speciality": [
            "Orthopedist",
        ],
    },
    {
        "symptom_name": "arm pain",
        "correlated_symptoms": [
            "shoulder pain",
            "neck pain",
            "back pain",
            "chest pain",
            "numbness",
            "tingling",
            "weakness",
            "swelling",
            "fatigue",
            "dizziness",
        ],
        "required_doctor_speciality": [
            "Orthopedist",
        ],
    },
    {
        "symptom_name": "leg pain",
        "correlated_symptoms": [
            "back pain",
            "hip pain",
            "knee pain",
            "foot pain",
            "swelling",
            "numbness",
            "tingling",
            "weakness",
            "fatigue",
            "cramps",
        ],
        "required_doctor_speciality": [
            "Orthopedist",
        ],
    },
    {
        "symptom_name": "hip pain",
        "correlated_symptoms": [
            "back pain",
            "leg pain",
            "knee pain",
            "groin pain",
            "numbness",
            "tingling",
            "stiffness",
            "fatigue",
            "swelling",
            "limping",
        ],
        "required_doctor_speciality": [
            "Orthopedist",
        ],
    },
    {
        "symptom_name": "knee pain",
        "correlated_symptoms": [
            "leg pain",
            "hip pain",
            "foot pain",
            "swelling",
            "stiffness",
            "numbness",
            "tingling",
            "weakness",
            "cracking",
            "limping",
        ],
        "required_doctor_speciality": [
            "Orthopedist",
        ],
    },
]


for x in correlated_symptoms_list:
    x = CorrelatedSymptoms.parse_obj(x)
    x = jsonable_encoder(x)
    db_result = db.symptoms.insert_one(x)
    print(db_result.inserted_id)
    # print(x)
