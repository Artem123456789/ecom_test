import json

from pymongo import MongoClient

from app.settings import MONGO_CONNECTION_STRING


class EcomDbFiller:

    def __init__(self, db_name: str, forms_collection_name: str, forms_data_file_name: str):
        self.__db_name = db_name
        self.__forms_collection_name = forms_collection_name
        self.__forms_data_file_name = forms_data_file_name
        self.__client = MongoClient(MONGO_CONNECTION_STRING)

    def __get_forms_data(self) -> list:
        with open(self.__forms_data_file_name, "r") as f:
            data = json.load(f)

        return data

    def __check_db_is_not_exists(self) -> bool:
        db_list = self.__client.list_database_names()
        if self.__db_name in db_list:
            return False

        return True

    def fill_db(self) -> None:
        if self.__check_db_is_not_exists():
            ecom_db = self.__client[self.__db_name]
            forms_collection = ecom_db[self.__forms_collection_name]
            forms_data = self.__get_forms_data()
            forms_collection.insert_many(forms_data)
