from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from ..app_models.EHR import Session
import uuid
import json
from ..util import get_db

router = APIRouter()


@router.get(
    "/session/new/{patient_id}",
    tags=["Session"],
    summary="Creates a new session between doctor and patient",
)
async def create_session(patient_id: str):
    print(f"create_session endpoint called for patient_id='{patient_id}'")
    db = get_db()

    db_reult = db.patient.find_one({"patient_id": patient_id})

    if db_reult == None:
        print(f"Patient id='{patient_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"Patient id='{patient_id}' not found"
        )

    session_id = uuid.uuid4().hex
    created_session = Session(session_id=session_id, patient_id=patient_id)
    created_session = jsonable_encoder(created_session)

    insert_result = db.session.insert_one(created_session)

    if insert_result.acknowledged:
        return {
            "success": True,
            "created_session_id": session_id,
            "message": f"Created a new session for patient_id='{patient_id}'",
        }
    else:
        return {
            "success": False,
            "message": "Could not create a session. Database error",
        }
