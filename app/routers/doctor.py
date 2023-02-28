from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

import json
from ..util import get_db

router = APIRouter()


@router.get(
    "/doctor/{doctor_id}",
    tags=["Doctor"],
    summary="Returns profile of a doctor for a valid doctor_id",
)
async def get_doctor(doctor_id: str):
    print(f"get_doctor endpoint called for doctor_id={doctor_id}")
    db = get_db()

    db_result = db.doctor.find_one(
        filter={"doctor_id": doctor_id}, projection={"_id": False}
    )

    if db_result == None:
        print(f"doctor id='{doctor_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"doctor id='{doctor_id}' not found"
        )

    return {"success": True, "doctor": db_result}
