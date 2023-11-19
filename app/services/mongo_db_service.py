from typing import List

from pymongo import MongoClient

from app.settings import MONGO_CONNECTION_STRING


class MongoDbService:

    def __init__(self):
        self.__client = MongoClient(MONGO_CONNECTION_STRING)

    def get_db_list(self) -> List[str]:
        return self.__client.list_database_names()

    def get_db(self, db_name: str):
        return self.__client[db_name]
