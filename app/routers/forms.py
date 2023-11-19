from fastapi import (
    APIRouter,
    Depends,
)

from app.handlers.forms_handler import FormsHandler
from app.routers.entities.input.get_form_input_entity import GetFormInputEntity
from app.services.validation import validate_get_form_query_params

router = APIRouter()


@router.post(
    "/get_form",
)
def get_form(params: GetFormInputEntity = Depends(validate_get_form_query_params)):
    result = FormsHandler('ecom_db', 'forms').get_form(params)

    return result
