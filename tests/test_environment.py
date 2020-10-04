# Python Core
import os

def test_environment_variables():
    token_api_telegram = type(os.environ['TOKEN_API_TELEGRAM'])
    conection_to_database = type(os.environ['CONECTION_TO_DATABASE'])

    test_string = type("test")

    assert token_api_telegram == test_string and conection_to_database == test_string

