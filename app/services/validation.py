from starlette.requests import Request

from app.routers.entities.input.get_form_input_entity import (
    GetFormEmailQueryParam,
    GetFormDateQueryParam,
    GetFormPhoneQueryParam,
    GetFormTextQueryParam,
    GetFormInputEntity,
)


class GetFormQueryParamFactory:
    @staticmethod
    def get_form_query_param(field_name: str, field_value: str):
        possible_classes = [
            GetFormDateQueryParam,
            GetFormPhoneQueryParam,
            GetFormEmailQueryParam,
        ]
        for possible_class in possible_classes:
            try:
                params = possible_class(field_name=field_name, field_value=field_value)
                return params
            except ValueError:
                continue
        else:
            return GetFormTextQueryParam(field_name=field_name, field_value=field_value)


def validate_get_form_query_params(request: Request) -> GetFormInputEntity:
    get_form_input_entity = GetFormInputEntity()
    for i, j in request.query_params.items():
        query_param = GetFormQueryParamFactory.get_form_query_param(i, j)
        if isinstance(query_param, GetFormDateQueryParam):
            get_form_input_entity.date_params.append(query_param)
        elif isinstance(query_param, GetFormPhoneQueryParam):
            get_form_input_entity.phone_params.append(query_param)
        elif isinstance(query_param, GetFormEmailQueryParam):
            get_form_input_entity.email_params.append(query_param)
        else:
            get_form_input_entity.text_params.append(query_param)

    return get_form_input_entity
