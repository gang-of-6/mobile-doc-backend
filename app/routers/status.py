from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    tags=["General"],
)
async def root():
    return {
        "status": "OK",
        "message": "Welcome to Mobile Docs Backend. Go to /docs for documentation",
    }
