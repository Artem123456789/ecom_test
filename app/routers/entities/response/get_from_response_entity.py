from pydantic import BaseModel


class GetFormSuccessResponseEntity(BaseModel):
    name: str
