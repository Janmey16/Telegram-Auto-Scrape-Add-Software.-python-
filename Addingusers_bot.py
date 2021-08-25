from telegram import *
from telegram.ext import *
from telethon import *
import telebot

bot = Bot("1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc")
# print(bot.get_me())
updater = Updater(
    "1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc", use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello Janmey!
    )
    
 

start_value = CommandHandler('start', start)
dispatcher.add_handler(start_value)
updater.start_polling()


