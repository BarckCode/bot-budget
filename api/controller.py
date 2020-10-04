# MongoDB Driver
from pymongo import MongoClient
from bson.objectid import ObjectId
# Internal Modules
from api.model import ModelApi
from api.operations import find_value_and_replace_it


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
        user_document = self.user_exist(user_id=user_id)

        if user_document == None:
            user = {
                "user_id": user_id,
                "username": username,
                "budget": {
                    "initial_budget": initial_budget,
                    "current_balance": initial_budget
                },

                "relationship_id": user_id
            }

            income = {
                "name": "Income",
                "income": [],
                "relationship_income_id": user_id
            }

            expenses = {
                "name": "Expenses",
                "expenses": [],
                "relationship_expense_id": user_id
            }


            self.model_api.insert_one_document_into_db(document=user)
            self.model_api.insert_one_document_into_db(document=income)
            self.model_api.insert_one_document_into_db(document=expenses)
        elif initial_budget != 0:
            # We look for the current value of initial_budget and replace it with the same value: initial_budget - initial_budget = 0
            find_value_and_replace_it(
                document=user_document,
                updater=self.model_api.find_one_and_update_document,
                updated_value=initial_budget[0]
            )
        else:
            print('El usuario existe. A la espera de comandos...')


    def insert_income_expenses_data(self, user_data, field, type_data, value):
        user_id = user_data.id

        self.model_api.update_and_push(
            field_to_search=field,
            value_to_search=user_id,
            field_to_push=type_data,
            value_to_push=value[0]
        )
