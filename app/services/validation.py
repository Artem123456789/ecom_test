from typing import (
    List,
    Tuple,
)

from starlette.requests import Request

from app.routers.entities.input.get_form_input_entity import (
    GetFormEmailQueryParam,
    GetFormDateQueryParam,
    GetFormPhoneQueryParam,
    GetFormTextQueryParam,
)


def validate_get_form_query_params(request: Request) -> Tuple[
    List[GetFormEmailQueryParam],
    List[GetFormDateQueryParam],
    List[GetFormPhoneQueryParam],
    List[GetFormTextQueryParam],
]:
    email_params: List[GetFormEmailQueryParam] = []
    date_params: List[GetFormDateQueryParam] = []
    phone_params: List[GetFormPhoneQueryParam] = []
    text_params: List[GetFormTextQueryParam] = []
    possible_classes = [
        GetFormEmailQueryParam,
        GetFormDateQueryParam,
        GetFormPhoneQueryParam,
    ]
    for i, j in request.query_params.items():
        for possible_class in possible_classes:
            try:
                params = possible_class(field_name=i, field_value=j)
                if isinstance(params, GetFormEmailQueryParam):
                    email_params.append(params)
                    break
                elif isinstance(params, GetFormDateQueryParam):
                    date_params.append(params)
                    break
                elif isinstance(params, GetFormPhoneQueryParam):
                    phone_params.append(params)
                    break
            except ValueError:
                continue
        else:
            text_params.append(GetFormTextQueryParam(field_name=i, field_value=j))

    return email_params, date_params, phone_params, text_params
