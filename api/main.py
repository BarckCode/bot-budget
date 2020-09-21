# MongoDB Driver
from pymongo import MongoClient
# Internal Modules
from api.model import ModelApi

def load_db(CONECTION_TO_DATABASE):
    client = MongoClient(CONECTION_TO_DATABASE)
    db = client.budget_control

    # DB Users Collection
    users = db.users

    print(users)
    print("*" * 10)

    model_api = ModelApi()
    model_api.users_collections(users=users)



