import os
from dotenv import load_dotenv

# Utils:
from .follow import follow_user


def instagram_main():
    """
        Instagram Options
    """

    # Inicializamos la función para leer las variables de entorno.
    load_dotenv()


    # Cargamos los datos de Login de Instagram.
    INSTA_USER = os.getenv('INSTA_USER')
    INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')


    # Ejecutamos:
    follow_user(INSTA_USER, INSTA_PASSWORD)
