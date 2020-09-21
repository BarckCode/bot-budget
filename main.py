# Python Core
import os
# Env Variables
from dotenv import load_dotenv
# Internal Modules
from bot import load_bot
from api import load_db

def main():
    # Load Env Variables
    load_dotenv()
    CONECTION_TO_DATABASE = os.getenv('CONECTION_TO_DATABASE')
    TOKEN_API_TELEGRAM = os.getenv('TOKEN_API_TELEGRAM')

    # Load MongoDB
    load_db(CONECTION_TO_DATABASE)

    # Load Telegram Bot
    load_bot(TOKEN_API_TELEGRAM)

if __name__ == '__main__':
    """
    Program Entry
    """
    main()