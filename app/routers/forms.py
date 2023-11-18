from fastapi import (
    APIRouter,
    Depends,
)

from app.routers.entities.input.get_form_input_entity import GetFormInputEntity
from app.services.validation import validate_get_form_query_params

router = APIRouter()


@router.post(
    "/get_form",
)
async def get_form(params: GetFormInputEntity = Depends(validate_get_form_query_params)):

    return params
