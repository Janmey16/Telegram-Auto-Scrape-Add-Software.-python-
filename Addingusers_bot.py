from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import re
import traceback
import time
import random
import telebot


BOT_TOKEN = '1910773191:AAFXjLzXfjbOK1VnGqmaz6ea37noZCsURtc'
bot = telebot.TeleBot(BOT_TOKEN)
# bot.get_api_id()
# bot.get_api_hash()
# constants and establishing connection with client.
# api
# api_id = 7478146
# # hash
# api_hash = 'f481ce610cbe3fd47e9402f9771f18b3'
# phone = '+918976826588'
# client = TelegramClient()

SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100


# async def main():
#     await client.send_message('me', 'Hello !!!!')
# with client:
#     client.loop.run_until_complete(main())
# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     client.sign_in(phone, input('Enter verification code: '))


# test if connection established or not.


chats = []
last_date = None
chunk_size = 200
groups = []


# result = telebot(GetDialogsRequest(
#     offset_date=last_date,
#     offset_id=0,
#     offset_peer=InputPeerEmpty(),
#     limit=chunk_size,
#     hash=0
# ))
# chats.extend(result.chats)


for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue


group_list = ""
i = 0
for g in groups:
    group_list = group_list + (str(i) + '- ' + g.title + '\n')

    i += 1


# scrapes members from all groups because not able to pass the user-input into our grouplist array.
i = 0
unimembers = []
for g in groups:
    all_participants = []
    all_participants = bot.get_participants(
        g.title, aggressive=True)

    members = []
    for j in all_participants:
        user = {}
        user['username'] = j.username
        user['id'] = j.id
        user['access_hash'] = j.access_hash

        # user['name'] = j.name
        members.append(user)
    unimembers.append(members)


source_group = -1
mode = 2


# def add_members(message):
#     bot.send_message(message.chat.id, "adding members")
#     users = unimembers[source_group]
#     n = 0
#     for user in users:
#         n += 1
#         if n % 80 == 0:
#             time.sleep(60)
#         try:
#             print("Adding {}".format(user['id']))
#             if mode == 1:
#                 if user['username'] == "":
#                     continue
#                 user_to_add = client.get_input_entity(user['username'])
#             elif mode == 2:
#                 user_to_add = InputPeerUser(
#                     user['id'], user['access_hash'])
#             else:
#                 sys.exit("Invalid Mode Selected. Please Try Again.")
#             target_group = groups[int(source_group)]
#             target_group_entity = InputPeerChannel(
#                 target_group.id, target_group.access_hash)

#             client(InviteToChannelRequest(target_group_entity, [user_to_add]))
#             print("Waiting for about 60 seconds...")
#             time.sleep(random.randrange(0, 5))
#         except PeerFloodError:
#             print(
#                 "Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
#             print("Waiting {} seconds".format(SLEEP_TIME_2))
#             time.sleep(SLEEP_TIME_2)
#         except UserPrivacyRestrictedError:
#             print("The user's privacy settings do not allow you to do this. Skipping.")
#             print("Waiting for 5 Seconds...")
#             time.sleep(random.randrange(0, 5))
#         except:
#             traceback.print_exc()
#             print("Unexpected Error")
#             continue


def scrape_members(message):
    try:
        source_group = message.text
        destination = bot.send_message(
            message.chat.id, "Enter Destination Group:")
        # print(destination)
        # bot.register_next_step_handler(destination, add_members)
        # print(message.text)
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(
        message.chat.id, 'Showing you the group list...\nUse /groups command to confirm')
    

@bot.message_handler(commands=['groups'])
def before_scrape(message):
    # printing the group list in chat section.
    bot.send_message(message.chat.id, group_list)
    source = bot.send_message(message.chat.id, "Select the source group:")
    # store user input into source_group:
    source_group = source.text
    bot.register_next_step_handler(source, scrape_members)


bot.enable_save_next_step_handlers(delay=10)
bot.load_next_step_handlers()


if __name__ == '__main__':
    bot.polling()
