# Telegram Library
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Internal Modules
from bot.commands_handler import AllCommands
from validation import alerts

def load_bot(TOKEN_API_TELEGRAM):

    # Load Bot
    updater = Updater(token=TOKEN_API_TELEGRAM, use_context=True)
    dispatcher = updater.dispatcher

    # Load Bot Commands
    command = AllCommands()

    commands = {
        'start': command.start,
        'set_saldo': command.save_current_balance,
        'set_ingreso': command.save_income,
        'set_gasto': command.save_expense,
        'saldo_actual': command.get_current_balance,
    }

    # Set Commands in Dispatcher
    for command_name, command_function in commands.items():
        dispatcher.add_handler(
            CommandHandler(command_name, command_function)
        )


    # Set The Warning Commands
    alerts(
        dispatcher=dispatcher,
        MessageHandler=MessageHandler,
        Filters=Filters
    )


    # Start Bot
    updater.start_polling()