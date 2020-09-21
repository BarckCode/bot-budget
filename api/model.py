# MongoDB Driver
from bson.objectid import ObjectId

class ModelApi():
    """
    Class that consults and accesses the database.
    """
    def __init__(self):
        pass


    def users_collections(self, users):
        # Collections
        self.users = users



    def query_the_database_once(self, value):
        self.users.findOne({'_id': ObjectId(value)})