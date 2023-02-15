from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from ..app_models.patient import Patient
import json
from ..util import get_db

router = APIRouter()


@router.get(
    "/patient/{patient_id}",
    tags=["Patient"],
    summary="Returns details of a patient given a valid patient ID",
)
async def get_patient(patient_id: str):
    print(f"get_patient endpoint called for patient_id='{patient_id}'")
    db = get_db()

    db_reult = db.patient.find_one({"patient_id": patient_id})

    if db_reult == None:
        print(f"Patient id='{patient_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"Patient id='{patient_id}' not found"
        )

    try:
        validated_result = Patient.parse_raw(json.dumps(db_reult, default=str))
    except:
        print(
            f"Validation error while parsing Patient data for patient_id='{patient_id}'"
        )
        validated_result = None
    return {
        "status": "OK",
        "patient": validated_result,
    }


@router.put(
    "/patient/{patient_id}",
    tags=["Patient"],
    summary="Update details of a patient given a valid patient ID",
)
async def get_patient(patient_id: str, patient_details: Patient):
    print(f"update_patient endpoint called for patient_id='{patient_id}'")
    db = get_db()
    db_reult = db.patient.find_one({"patient_id": patient_id})

    if db_reult == None:
        print(f"Patient id='{patient_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"Patient id='{patient_id}' not found"
        )

    update_result = db.patient.replace_one(
        {"patient_id": patient_id}, jsonable_encoder(patient_details)
    )

    if update_result.modified_count == 1:
        return {"status": "OK", "message": "patient details is updated"}
    else:
        return {"status": False, "message": "patient details could not be updated"}
