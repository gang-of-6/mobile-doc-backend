from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from ..app_models.EHR import Medicine
import json
from ..util import get_db

router = APIRouter()


@router.get(
    "/medicine/all",
    tags=["Medicine"],
    summary="Returns a list of prescribable medicine",
)
async def get_medicines():
    print(f"get_medicines endpoint called")
    db = get_db()

    db_result = db.medicine.find(filter={}, projection={"_id": False})
    med_list = [x for x in db_result]

    return {"success": True, "all_medicines": med_list}
