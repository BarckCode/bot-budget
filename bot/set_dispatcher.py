from telegram.ext import CommandHandler, MessageHandler, Filters

class SetDispatcher():
    """
    Class that saves the command in the dispatcher
    """
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher


    def set_command(self, name_command, command):
        self.dispatcher.add_handler(
            CommandHandler(name_command, command)
        )


    def set_command_message_handler(self, command):
        self.dispatcher.add_handler(
            MessageHandler(Filters.command, command)
        )
