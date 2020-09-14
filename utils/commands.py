class AllCommands():
    """
    Class with all the commands that we can use with the bot
    """
    def __init__(self):
        pass


    # Welcome Message:
    def start(self, update, context):
        update.message.reply_text(
            'Hola! Soy BotBugetControl.\n'
            'Un bot. Creado para ayudarte a manejar mejor tu presupuesto\n\n'
            'Puedes controlarme utilizando estos comandos:',
        )


    # Save Current Balance
    def save_current_balance(self, update, context):
        if len(context.args) == 0:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"El comando necesita que le envíes un valor.\nPor ejemplo:\n/set_saldo 1000"
            )
        else:
            current_balance = ' '.join(context.args)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Tu saldo actual es de: {current_balance}"
            )


    # Save Income
    def save_income(self, update, context):
        income = ' '.join(context.args)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Has introducido este ingreso: {income}",
        )


    # Save Expense
    def save_expense(self, update, context):
        expense = ' '.join(context.args)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Has introducido este gasto: {expense}"
        )


    def get_current_balance(self, update, context):
        current_balance = ' '.join(context.args)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Tu saldo actual es de: {current_balance}"
        )


    # Default message
    def unknown(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Lo siento. Aún no entiendo ese comando"
        )