import os
from dotenv import load_dotenv
from instabot import Bot


# Arrancamos el paquete para leer variables de entorno
load_dotenv()


# Cargamos los datos de Login de Instagram
INSTA_USER = os.getenv('INSTA_USER')
INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')


# Inicializamos la instancia del Bot
bot = Bot(
    follow_delay = 60 # Segundos que tarda en seguir a cada persona
)


# Hacemos Login
bot.login(username=INSTA_USER, password=INSTA_PASSWORD)


# Seleccionamos un usuario objetivo.
bot.follow('andresvidoza')
