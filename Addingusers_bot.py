from telegram import *
from telegram.ext import *

bot = Bot("1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc")
# print(bot.get_me())
updater = Updater(
    "1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc", use_context=True)
dispatcher = updater.dispatcher


def onstart(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Running the start function now!",
    )
    
 

start_value = CommandHandler('start', onstart)
dispatcher.add_handler(start_value)
updater.start_polling()
