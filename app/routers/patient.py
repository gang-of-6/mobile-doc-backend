from fastapi import APIRouter, HTTPException
from ..app_models.patient import Patient
import json
from .fake_db import patient_list

router = APIRouter()


@router.get(
    "/patient/{patient_id}",
    tags=["Patient"],
    summary="Returns details of a patient given a valid patient ID",
)
async def get_patient(patient_id: str):
    print(f"get_patient endpoint called for patient_id='{patient_id}'")
    db_reult = get_patient_from_fake_db(patient_id=patient_id)

    if db_reult == None:
        print(f"Patient id='{patient_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"Patient id='{patient_id}' not found"
        )

    # try:
    validated_result = Patient.parse_raw(json.dumps(db_reult, default=str))
    # except:
    #     print(
    #         f"Validation error while parsing Patient data for patient_id='{patient_id}'"
    #     )
    #     validated_result = None
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
    db_reult = get_patient_from_fake_db(patient_id=patient_id)

    if db_reult == None:
        print(f"Patient id='{patient_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"Patient id='{patient_id}' not found"
        )

    db_result = update_patient_from_fake_db(patient_id, patient_details)

    if db_result:
        return {"status": "OK", "message": "patient details is updated"}
    else:
        return {"status": False, "message": "patient details could not be updated"}


def get_patient_from_fake_db(patient_id: str):
    for x in patient_list:
        if x["patient_id"] == patient_id:
            return x
    return None


def update_patient_from_fake_db(patient_id: str, patient_details: Patient):
    idx = 0
    for x in patient_list:
        if x["patient_id"] == patient_id:
            break
        idx += 1
    patient_list[idx] = patient_details.dict()
    print("Updated result: ", patient_list[idx])
    return True
