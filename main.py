# Python Core
import os
# Env Variables
from dotenv import load_dotenv
# Telegram Library
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup
# Internal Modules
from utils.commands import AllCommands

# Load Bot Commands
all_commands = AllCommands()

if __name__ == '__main__':
    """
    Program Entry
    """
    # Load Env Variables
    load_dotenv()
    TOKEN_API_TELEGRAM = os.getenv('TOKEN_API_TELEGRAM')

    # Load Bot
    updater = Updater(token=TOKEN_API_TELEGRAM, use_context=True)
    dispatcher = updater.dispatcher

    # Commands
    start_handler = CommandHandler('start', all_commands.start)
    dispatcher.add_handler(start_handler)

    caps_handler = CommandHandler('print', all_commands.print_console)
    dispatcher.add_handler(caps_handler)

    unknown_handler = MessageHandler(Filters.command, all_commands.unknown)
    dispatcher.add_handler(unknown_handler)

    # Start Bot
    updater.start_polling()