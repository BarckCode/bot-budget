from bot.helpers.send_messages_helper import AllMessages
from api import DataController

class AllCommands():
    """
    Class with all the commands that we can use with the bot
    """
    def __init__(self):
        self.messages = AllMessages()
        self.data_controller = DataController()


    # Welcome Message:
    def start(self, update, context):
        self.messages.welcome_message(update=update)
        self.data_controller.user_data(data=update.message['chat'])


    # Save Current Balance
    def save_current_balance(self, update, context):
        if len(context.args) == 0:
            message = f'El comando necesita que le envíes un valor.\nPor ejemplo:\n/set_saldo 1000'
        else:
            message = 'Has configurado tu saldo actual en'
            self.data_controller.user_data(data=update.message['chat'], initial_budget=context.args)

        self.messages.standard_message(
            update=update,
            context=context,
            message=message,
        )


    # Save Income
    def save_income(self, update, context):
        if len(context.args) == 0:
            message = f'El comando necesita que le envíes un valor.\nPor ejemplo:\n/set_ingreso 100'
        else:
            message = 'Has añadido este ingreso'
            self.data_controller.insert_income_expenses_data(user_data=update.message['chat'], field="relationship_income_id", type_data="income", value=context.args)

        self.messages.standard_message(
            update=update,
            context=context,
            message=message,
        )


    # Save Expense
    def save_expense(self, update, context):
        if len(context.args) == 0:
            message = f'El comando necesita que le envíes un valor.\nPor ejemplo:\n/set_gasto 200'
        else:
            message = 'Has añadido este gasto'
            self.data_controller.insert_income_expenses_data(user_data=update.message['chat'], field="relationship_expense_id", type_data="expenses", value=context.args)

        self.messages.standard_message(
            update=update,
            context=context,
            message=message,
        )


    # Show current balance
    def get_current_balance(self, update, context):
        if len(context.args) > 0:
            message = f'El comando no necesita valores.\nPara conocer tu saldo actual ejecuta:\n/saldo_actual'
        else:
            message = 'Tu saldo actual es: 900'

        self.messages.standard_message(
            update=update,
            context=context,
            message=message,
            args=False
        )


    # Default message
    def unknown(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Lo siento. Aún no entiendo ese comando"
        )
