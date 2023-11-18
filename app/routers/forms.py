from typing import (
    Tuple,
    List,
)

from fastapi import (
    APIRouter,
    Depends,
)

from app.routers.entities.input.get_form_input_entity import (
    GetFormEmailQueryParam,
    GetFormDateQueryParam,
    GetFormPhoneQueryParam,
    GetFormTextQueryParam,
)
from app.services.validation import validate_get_form_query_params

router = APIRouter()


@router.post(
    "/get_form",
)
async def get_form(params: Tuple[
    List[GetFormEmailQueryParam],
    List[GetFormDateQueryParam],
    List[GetFormPhoneQueryParam],
    List[GetFormTextQueryParam],
] = Depends(validate_get_form_query_params)):

    return params
