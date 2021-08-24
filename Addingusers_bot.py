from telegram import *
from telegram.ext import *

bot=Bot("1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc")
updater = Updater(
    "1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc", use_context=True)
dispatcher = updater.dispatcher

def onstart(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text = ("Let me show you the group list. \nUse /groups command to agree")
        bot.register_next_step_handler(text, ongroups)
    )
    
def ongroups(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=effective_chat.id,
        text = ("Here is the group list"),
        
    )
        
start_value = CommandHandler('start', onstart)

dispatcher.add_handler(start_value)

start_value1 = CommandHandler('groups', ongroups)
dipatcher.add_handler(start_value1)
updater.start_polling()
