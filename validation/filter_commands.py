# Internal Modules
from utils import AllMessages

def alerts(dispatcher, MessageHandler, Filters):
    messages = AllMessages()

    # Filter all messages sent to the chat bot
    def filter_all(update, context):
        messages.get_message(update=update, message='./messages/info/filter_all_messages.md')

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='👆🏾'
        )


    dispatcher.add_handler(
        MessageHandler(Filters.all, filter_all)
    )

