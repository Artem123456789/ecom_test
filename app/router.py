from fastapi import APIRouter

from app.routers.forms import router as forms_router

router = APIRouter()
router.include_router(forms_router)
