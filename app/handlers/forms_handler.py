import itertools
from typing import Union

from app.routers.entities.input.get_form_input_entity import GetFormInputEntity
from app.routers.entities.response.get_from_response_entity import GetFormSuccessResponseEntity
from app.services.mongo_db_service import MongoDbService


class FormsHandler:

    def __init__(self, db_name: str, forms_collection_name: str):
        self.__db_name = db_name
        self.__forms_collection_name = forms_collection_name
        self.__mongo_db_service = MongoDbService()

    def __prepare_get_form_query(self, input_entity: GetFormInputEntity):
        query = {}

        for param in input_entity.date_params:
            query[param.field_name] = 'date'
        for param in input_entity.phone_params:
            query[param.field_name] = 'phone'
        for param in input_entity.email_params:
            query[param.field_name] = 'email'
        for param in input_entity.text_params:
            query[param.field_name] = 'text'

        query_list = []
        for i in range(1, len(query) + 1):
            for combination in itertools.combinations(query.items(), i):
                query_list.append(dict(combination))

        full_query = {
            '$or': query_list
        }

        return full_query

    def get_form(self, input_entity: GetFormInputEntity) -> Union[GetFormSuccessResponseEntity, dict]:
        query = self.__prepare_get_form_query(input_entity)

        ecom_db = self.__mongo_db_service.get_db(self.__db_name)
        forms_collection = ecom_db[self.__forms_collection_name]
        result = forms_collection.find(query, {'name': 1})
        for item in result:
            return GetFormSuccessResponseEntity(name=item['name'])

        return query
