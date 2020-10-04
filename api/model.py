# MongoDB Driver
from bson.objectid import ObjectId
from pymongo import MongoClient
# Python Core
import ssl
import os

class ModelApi():
    """
    Class that consults and accesses the database.
    """
    def __init__(self):
        # Load Env Variables
        CONECTION_TO_DATABASE = os.environ['CONECTION_TO_DATABASE']

        # Conect to MongoDB
        client = MongoClient(
            CONECTION_TO_DATABASE,
            ssl=True,
            ssl_cert_reqs=ssl.CERT_NONE
        )

        # Get DB
        db = client.budget_control

        # Get Users Collection
        self.users = db.users


    def find_one_value_in_db(self, field, value):

        search = self.users.find_one({field: value})

        return search


    def insert_one_document_into_db(self, document):
        self.users.insert_one(document)


    def update_and_push(self, field_to_search, value_to_search, field_to_push, value_to_push):
        self.users.update(
            {field_to_search: value_to_search},
            {'$push': {field_to_push: value_to_push}}
        )


    def find_one_and_update_document(self, field_to_search, value_to_search, field_to_replace, value_to_replace):
        self.users.find_one_and_update(
            {field_to_search: value_to_search},
            {'$inc': {field_to_replace: value_to_replace}}
        )