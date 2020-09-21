# Internal Modules
from api.model import ModelApi

class DataController():
    """
    Class that receives all data and manages it
    """
    def __init__(self):
        self.model_api = ModelApi()


    def user_exist(self, _id):

        validation = self.model_api.query_the_database_once("43596404267294110")
        print(validation)


    def user_data(self, data, initial_budget=""):
        _id = data.id
        username = data.username

        # self.user_exist(_id=_id) --> Hay que probar cómo realizar la busqueda a la BBDD para validar la información antes de añadirla.

        user = {
            "_id": _id,
            "username": username,
            "budget": {
                "initial_budget": initial_budget,
                "current_balance": "",
            },

            "relationship_id": _id,
        }


