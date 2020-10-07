
class AllMessages():
    """
    Class with all messages sent by the bot
    """
    def __init__(self):
        pass


    # Welcome Message:
    def get_message(self, update, message):
        welcome_marckdown = open(message).read()
        update.message.reply_markdown(welcome_marckdown)


    # Standard Command Output
    def standard_message(self, update, context, message, args=True):
        user_input = ' '.join(context.args)

        if args == True:
            if len(context.args) == 0:
                text_message = f'{message}'
            else:
                text_message = f'{message}: {user_input}'
        else:
            text_message = f'{message}'

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'{text_message}'
        )