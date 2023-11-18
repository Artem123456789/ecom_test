import re
from datetime import datetime

from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
)


class GetFormQueryParamBase(BaseModel):
    field_name: str
    field_value: str


class GetFormEmailQueryParam(GetFormQueryParamBase):
    field_value: EmailStr


class GetFormDateQueryParam(GetFormQueryParamBase):
    @field_validator('field_value')
    @classmethod
    def validate_field_value_date(cls, value):
        available_formats = ['%d.%m.%Y', '%Y-%m-%d']
        for available_format in available_formats:
            try:
                new_val = datetime.strptime(value, available_format)
                return new_val
            except ValueError:
                pass

        raise ValueError(f"Invalid date format. Available date formats: dd.mm.yyyy, yyyy-mm-dd")


class GetFormPhoneQueryParam(GetFormQueryParamBase):
    @field_validator('field_value')
    @classmethod
    def validate_field_valie_phone(cls, value):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if value and not re.search(regex, value, re.I):
            raise ValueError("Phone number invalid")

        return value


class GetFormTextQueryParam(GetFormQueryParamBase):
    ...
