from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from ..app_models.EHR import Session, SymptomEntry
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


@router.post(
    "/session/symptoms/{session_id}",
    tags=["Session"],
    summary="Add a new symptom to existing session",
)
async def add_symptoms(session_id: str, symptom_entry: SymptomEntry):
    print(f"add_symptoms endpoint called for session_id='{session_id}'")
    db = get_db()

    db_reult = db.session.find_one({"session_id": session_id})

    if db_reult == None:
        print(f"session id='{session_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"session id='{session_id}' not found"
        )

    symptom_entry_json = jsonable_encoder(symptom_entry)

    db_update = db.session.update_one(
        {"session_id": session_id}, {"$push": {"symptom_list": symptom_entry_json}}
    )

    # correlated-symptom list
    correlated_symptoms = db.symptoms.find_one(
        filter={"symptom_name": symptom_entry.symptom_name},
        projection={"correlated_symptoms": 1, "_id": 0},
    )["correlated_symptoms"]

    print(correlated_symptoms)

    if db_update.modified_count == 1:
        return {
            "success": True,
            "message": f"Successfully added symptoms to 'session_id'={session_id} ",
            "symptom_added": symptom_entry,
            "correlated_symptoms": correlated_symptoms,
        }
    else:
        return {
            "success": False,
            "message": f"Could not add symptoms to 'session_id'={session_id}. Potential DB issue",
        }


@router.get(
    "/session/suggested_doctors/{session_id}",
    tags=["Session"],
    summary="Suggests a list of doctors based on provided symptoms",
)
async def get_suggested_doctors(session_id: str):
    print(f"get_suggested_doctors endpoint called for session_id='{session_id}'")
    db = get_db()

    db_reult = db.session.find_one({"session_id": session_id})

    if db_reult == None:
        print(f"session id='{session_id}' not found")
        raise HTTPException(
            status_code=404, detail=f"session id='{session_id}' not found"
        )

    symptom_dict_list = db_reult["symptom_list"]
    symptom_list = [x["symptom_name"] for x in symptom_dict_list]
    symptom_list = set(symptom_list)

    required_doctor_specialities = set()

    for symptom_name in symptom_list:
        doc_speciality_list = db.symptoms.find_one(
            filter={"symptom_name": symptom_name},
            projection={"_id": 0, "required_doctor_speciality": 1},
        )["required_doctor_speciality"]

        required_doctor_specialities = required_doctor_specialities.union(
            set(doc_speciality_list)
        )

    required_doctor_specialities = list(required_doctor_specialities)

    db_result = db.doctor.find(
        {"speciality": {"$in": required_doctor_specialities}}, projection={"_id": 0}
    )

    suggested_doctors = [x for x in db_result]

    return {
        "success": True,
        "required_doctor_specialities": required_doctor_specialities,
        "suggested_doctors": suggested_doctors,
    }
