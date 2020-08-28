import os
from dotenv import load_dotenv


def _get_environment_variables():
    """
        Get data from environment variables
    """

    # Initialize the funtion to read the environment variables.
    load_dotenv()


    # Load the Instagram login data from the environment variables.
    user_login = os.getenv('INSTA_USER')
    user_password = os.getenv('INSTA_PASSWORD')


    instagram_data = (
        user_login,
        user_password,
    )

    return instagram_data