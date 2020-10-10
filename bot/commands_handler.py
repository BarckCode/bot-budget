# Internal Modules
from utils import AllMessages
from api import DataController
from validation import filter_need_args, filter_no_need_args
from bot.commands import set_balance, set_income, set_expense, show_current_balance


class AllCommands():
    """
    Class with all the commands that we can use with the bot
    """
    def __init__(self):
        self.messages = AllMessages()
        self.data_controller = DataController()


    # Welcome Message:
    def start(self, update, context):
        self.messages.get_message(update=update, message='./messages/welcome.md')
        self.data_controller.user_data(data=update.message['chat'])


    # Save Current Balance
    def save_current_balance(self, update, context):
        argument = filter_need_args(
            context=context,
            handler_messages=self.messages,
            update=update,
        )

        set_balance(
            argument=argument,
            command_function=self.data_controller.user_data,
            update=update,
            handler_messages=self.messages,
            context=context,
        )


    # Save Income
    def save_income(self, update, context):
        argument = filter_need_args(
            context=context,
            handler_messages=self.messages,
            update=update,
        )

        set_income(
            argument=argument,
            command_function=self.data_controller.insert_income_expenses_data,
            update=update,
            handler_messages=self.messages,
            context=context,
        )


    # Save Expense
    def save_expense(self, update, context):
        argument = filter_need_args(
            context=context,
            handler_messages=self.messages,
            update=update,
        )

        set_expense(
            argument=argument,
            command_function=self.data_controller.insert_income_expenses_data,
            update=update,
            handler_messages=self.messages,
            context=context,
        )


    # Get current balance
    def get_current_balance(self, update, context):
        validation = filter_no_need_args(
            context=context,
            handler_messages=self.messages,
            update=update
        )

        show_current_balance(
            validation=validation,
            command_function=self.data_controller.check_current_balance,
            update=update,
            handler_messages=self.messages,
            context=context,
        )
