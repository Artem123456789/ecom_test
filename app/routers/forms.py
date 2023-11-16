from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/get_form",
)
async def get_form():
    return {"status": "ok"}
