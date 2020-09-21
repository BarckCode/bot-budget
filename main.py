# Python Core
import os
# Env Variables
from dotenv import load_dotenv
# Internal Modules
from bot import load_bot


def main():
    # Load Env Variables
    load_dotenv()
    TOKEN_API_TELEGRAM = os.getenv('TOKEN_API_TELEGRAM')


    # Load Telegram Bot
    load_bot(TOKEN_API_TELEGRAM)


if __name__ == '__main__':
    """
    Program Entry
    """
    main()