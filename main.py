# Python Core
import os
# Env Variables
from dotenv import load_dotenv
# Telegram Library
from telegram.ext import Updater
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup
# Internal Modules
from utils.commands import AllCommands
from utils.set_dispatcher import SetDispatcher


def main():
    # Load Env Variables
    load_dotenv()
    TOKEN_API_TELEGRAM = os.getenv('TOKEN_API_TELEGRAM')

    # Load Bot
    updater = Updater(token=TOKEN_API_TELEGRAM, use_context=True)
    dispatcher = updater.dispatcher

    # Load Bot Commands
    all_commands = AllCommands()

    # Set Commands in Dispatcher
    set_command_in_dispatcher = SetDispatcher(dispatcher=dispatcher)

    set_command_in_dispatcher.set_command(
        name_command='start',
        command=all_commands.start,
    )

    set_command_in_dispatcher.set_command(
        name_command='set_saldo',
        command=all_commands.save_current_balance,
    )

    set_command_in_dispatcher.set_command(
        name_command='set_ingreso',
        command=all_commands.save_income,
    )

    set_command_in_dispatcher.set_command(
        name_command='set_gasto',
        command=all_commands.save_expense,
    )

    set_command_in_dispatcher.set_command(
        name_command='saldo_actual',
        command=all_commands.get_current_balance,
    )

    set_command_in_dispatcher.set_command_message_handler(
        command=all_commands.unknown,
    )

    # Start Bot
    updater.start_polling()



if __name__ == '__main__':
    """
    Program Entry
    """
    main()