#!/usr/ env python
# -*- coding: utf-8 -*-
import telebot
from subFile import check_or_add,check_old
from telebot import types


bot=telebot.TeleBot('1117323096:AAFjgXAykVD7T4qMPFsWo35mBQZV2YfIgzo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Hi there")
    bot.send_message(message.chat.id, text=str(message.from_user.id))
    check_or_add(message.from_user.id)


@bot.message_handler(content_types=["text"])
def replay(message):
    a=check_old(message.from_user.id)
    if not a :
        bot.send_message(message.chat.id,text=" انت تستخدم اخر اصدار من البوت ")
    else:
        bot.send_message(message.chat.id,text="انت تستخدم اصدار قديم من البوت الرجاء اضغط على \n/start\nلتحديث البوت ...وشكراً")
     


print("bot is running")
bot.polling(True)