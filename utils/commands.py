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


    # Command Example
    def print_console(self, update, context):
        text_caps = ' '.join(context.args)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Has introducido: {text_caps}"
        )


    # Default message
    def unknown(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Lo siento. Aún no entiendo ese comando"
        )