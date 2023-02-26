from pydantic import BaseModel, constr
from typing import Optional, List
from datetime import datetime
from fastapi.encoders import jsonable_encoder


class TestDataEntry(BaseModel):
    data_element: str
    data_value: float
    data_unit: str


class TestFileEntry(BaseModel):
    file_name: str
    file_url: str


class TestResult(BaseModel):
    test_result_id: str
    patient_id: str
    test_name: str
    date: datetime
    numeric_results: Optional[list[TestDataEntry]]
    test_files: Optional[list[TestFileEntry]]


test_results = [
    {
        "test_result_id": "12345",
        "patient_id": "0001",
        "test_name": "Complete Blood Count (CBC)",
        "date": "2023-02-26T12:00:00",
        "numeric_results": [
            {"data_element": "Hemoglobin", "data_value": 13.5, "data_unit": "g/dL"},
            {"data_element": "Hematocrit", "data_value": 40, "data_unit": "%"},
            {
                "data_element": "White blood cell count (WBC)",
                "data_value": 7500,
                "data_unit": "/mm3",
            },
            {
                "data_element": "Red blood cell count (RBC)",
                "data_value": 4.5,
                "data_unit": "million/mm3",
            },
            {
                "data_element": "Platelet count",
                "data_value": 150000,
                "data_unit": "/mm3",
            },
        ],
    },
    {
        "test_result_id": "54321",
        "patient_id": "0001",
        "test_name": "Liver Function Test (LFT)",
        "date": "2022-11-10T08:30:00",
        "numeric_results": [
            {"data_element": "Albumin", "data_value": 3.9, "data_unit": "g/dL"},
            {
                "data_element": "Total bilirubin",
                "data_value": 1.2,
                "data_unit": "mg/dL",
            },
            {
                "data_element": "Aspartate aminotransferase (AST)",
                "data_value": 40,
                "data_unit": "U/L",
            },
            {
                "data_element": "Alanine aminotransferase (ALT)",
                "data_value": 30,
                "data_unit": "U/L",
            },
        ],
        "test_files": [
            {
                "file_name": "LFT_Report.pdf",
                "file_url": "https://example.com/files/LFT_Report.pdf",
            },
            {
                "file_name": "LFT_Images.zip",
                "file_url": "https://example.com/files/LFT_Images.zip",
            },
        ],
    },
    {
        "test_result_id": "54321",
        "patient_id": "0001",
        "test_name": "X-Ray of Chest",
        "date": "2022-12-10T08:30:00",
        "test_files": [
            {
                "file_name": "X-Ray of Chest",
                "file_url": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Normal_posteroanterior_%28PA%29_chest_radiograph_%28X-ray%29.jpg",
            },
        ],
    },
    {
        "test_result_id": "98765",
        "patient_id": "0002",
        "test_name": "Thyroid Function Test (TFT)",
        "date": "2022-06-15T10:15:00",
        "numeric_results": [
            {
                "data_element": "Free thyroxine (FT4)",
                "data_value": 1.4,
                "data_unit": "ng/dL",
            },
            {
                "data_element": "Triiodothyronine (T3)",
                "data_value": 150,
                "data_unit": "ng/dL",
            },
            {
                "data_element": "Thyroid-stimulating hormone (TSH)",
                "data_value": 2.5,
                "data_unit": "uIU/mL",
            },
        ],
    },
]


import pymongo

atlas_password = "1234"
atlas_username = "user"

client = pymongo.MongoClient(
    f"mongodb+srv://{atlas_username}:{atlas_password}@cluster0.ds5ggbq.mongodb.net/?retryWrites=true&w=majority"
)

db = client.get_database("main_db")

for tr in test_results:
    tr = TestResult.parse_obj(tr)
    tr = jsonable_encoder(tr)
    db_result = db.test_result.insert_one(tr)
    print(db_result.inserted_id)
    print(tr)
