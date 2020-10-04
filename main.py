# Python Core
import os
# Internal Modules
from bot import load_bot


def main():
    # Load Env Variables
    TOKEN_API_TELEGRAM = os.environ['TOKEN_API_TELEGRAM']


    # Load Telegram Bot
    load_bot(TOKEN_API_TELEGRAM)


if __name__ == '__main__':
    """
    Program Entry
    """
    main()
