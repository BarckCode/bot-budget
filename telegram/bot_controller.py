# Prueba del Bot:
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN_API_TELEGRAM = os.getenv('TOKEN_API_TELEGRAM')

updater = Updater(token=TOKEN_API_TELEGRAM, use_context=True)
dispatcher = updater.dispatcher


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Mensaje de Bienvenida del Bot:
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola soy un bot creado por @barckcode!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Repite todo lo que escribas (Que no sea un comando)
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


# Te transforma en mayúsculas todo lo que escribas (Que no sea un comando)
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


# Mensaje que se envía cuando escriben un comando que no conoce el Bot.
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento. Aún no entiendo ese comando")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()