# MongoDB Driver
from bson.objectid import ObjectId
from pymongo import MongoClient
# Python Core
import ssl
import os
# Env Variables
from dotenv import load_dotenv

class ModelApi():
    """
    Class that consults and accesses the database.
    """
    def __init__(self):
        # Load Env Variables
        load_dotenv()
        CONECTION_TO_DATABASE = os.getenv('CONECTION_TO_DATABASE')

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