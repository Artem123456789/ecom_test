from fastapi import APIRouter

from app.routers.forms import router as home_router

router = APIRouter()
router.include_router(home_router)
