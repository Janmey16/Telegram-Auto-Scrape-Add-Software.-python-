from telegram import *
from telegram.ext import *

bot = Bot("1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc")
# print(bot.get_me())
updater = Updater(
    "1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc", use_context=True)
dispatcher = updater.dispatcher


def test_function(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="tutorial link : https://www.youtube.com/watch?v=NwBWW8cNCP4&t=59s",
        print("yes")
    )
    
 

start_value = CommandHandler('motion_detection', test_function)
dispatcher.add_handler(start_value)
updater.start_polling()
