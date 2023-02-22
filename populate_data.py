from fastapi.encoders import jsonable_encoder
import pymongo

from pydantic import BaseModel
from typing import Optional


client = pymongo.MongoClient(
    "mongodb+srv://user:1234@cluster0.ds5ggbq.mongodb.net/?retryWrites=true&w=majority"
)

db = client.get_database("main_db")


class Medicine(BaseModel):
    name: str
    generic_name: str
    precautions: Optional[list[str]]


med_list = [
    {
        "name": "Rolac",
        "generic_name": "ketorolac-tromethamine",
        "precautions": ["kidney_problem"],
    },
    {
        "name": "Brufen",
        "generic_name": "Ibuprofen",
    },
    {
        "name": "Flagyl",
        "generic_name": "Metronidazole",
        "precautions": ["liver_problem"],
    },
    {
        "name": "Ciprofloxacin",
        "generic_name": "Ciprofloxacin",
    },
    {
        "name": "Augmentin",
        "generic_name": "Amoxicillin and Clavulanic acid",
    },
    {
        "name": "Vitamin C",
        "generic_name": "Ascorbic acid",
        "precautions": ["kidney_problem"],
    },
    {
        "name": "Amlodipine",
        "generic_name": "Amlodipine",
    },
    {
        "name": "Erythromycin",
        "generic_name": "Erythromycin",
    },
    {
        "name": "Spirulina",
        "generic_name": "Spirulina",
    },
    {
        "name": "Prothiaden",
        "generic_name": "Dosulepin",
    },
    {
        "name": "Atenolol",
        "generic_name": "Atenolol",
    },
    {
        "name": "Levocetirizine",
        "generic_name": "Levocetirizine",
    },
    {
        "name": "Loratadine",
        "generic_name": "Loratadine",
    },
    {
        "name": "Napa",
        "generic_name": "Paracetamol",
        "precautions": ["liver_problem"],
    },
    {
        "name": "Amoxicillin",
        "generic_name": "Amoxicillin",
    },
    {
        "name": "Rantac",
        "generic_name": "Ranitidine",
        "precautions": ["kidney_problem"],
    },
]


for med in med_list:
    med = Medicine.parse_obj(med)
    med = jsonable_encoder(med)
    db_result = db.medicine.insert_one(med)
    print(db_result.inserted_id)
