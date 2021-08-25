from telegram import *
from telegram.ext import *
from telethon import *
import telebot

BOT_TOKEN = '1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    sent = bot.send_message(
        message.chat.id, 'Showing you the group list...\nUse /groups command to confirm')
    
if __name__ == '__main__':
    bot.polling()


