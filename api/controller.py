# MongoDB Driver
from pymongo import MongoClient
from bson.objectid import ObjectId
# Internal Modules
from api.model import ModelApi


class DataController():
    """
    Class that receives all data and manages it
    """
    def __init__(self):
        self.model_api = ModelApi()


    def users_collections(self, users):
        # Collections
        return users


    def user_exist(self, user_id):

        validation = self.model_api.find_one_value_in_db(
            field="user_id",
            value=user_id,
        )

        return validation


    def user_data(self, data, initial_budget=0):
        user_id = data.id
        username = data.username

        # Check user exists:
        user_data = self.user_exist(user_id=user_id)

        if user_data == None:

            user = {
                "user_id": user_id,
                "username": username,
                "budget": {
                    "initial_budget": initial_budget,
                    "current_balance": initial_budget
                },

                "relationship_id": user_id
            }

            self.model_api.insert_one_document_into_db(document=user)
        elif initial_budget != 0:

            self.model_api.find_one_and_update_document(
                field_to_search='_id',
                value_to_search=user_data['_id'],
                field_to_replace='budget.initial_budget',
                value_to_replace=float(initial_budget[0])
            )
        else:
            print('El usuario existe. A la espera de comandos...')
