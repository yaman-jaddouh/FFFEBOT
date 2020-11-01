#!/usr/ env python
# -*- coding: utf-8 -*-
import telebot
from telebot.types import KeyboardButton , ReplyKeyboardMarkup
from subFile import check_old,check_or_add,historyW

bot=telebot.TeleBot('1117323096:AAFjgXAykVD7T4qMPFsWo35mBQZV2YfIgzo')

@bot.message_handler(commands=['start'])
def start(message):
    
    key = ReplyKeyboardMarkup(one_time_keyboard = True , resize_keyboard = True)
    b1 = KeyboardButton("المحاضرات 📝")
    b2 = KeyboardButton("حول البوت⁉️")
    b3=KeyboardButton("دورات 🖌🗒")
    b4=KeyboardButton("مراجع وكتب عامة  📚")
    key.add(b1,b3)
    key.add(b4)
    key.add(b2)
    bot.send_message(message.chat.id,text=" أهلا وسهلا بك 💚 ",reply_markup=key)
    historyW(message.from_user.id,[])
    check_or_add(message.from_user.id)








@bot.message_handler(content_types=["text"])
def replay(message):
    a=check_old(message.from_user.id)
    if not a :
        if message.text =='حول البوت⁉️' :
            bot.send_message(message.chat.id,text="FEEEBot v 1.0.0\nبوت مساعد لكل طلاب الكهرباء في جامعة حلب\nيحتوي على محاضرات ودورات\nفي حالة وجود اي اقتراحات [أرجو إعلامنا بها](t.me/Yaman_jaddouh)\n\nby [Yaman jaddouh](t.me/Yaman_jaddouh)",parse_mode="Markdown")
            return
    else:
        bot.send_message(message.chat.id,text="انت تستخدم اصدار قديم من البوت الرجاء اضغط على \n/start\nلتحديث البوت ...وشكراً")
     


print("bot is running")
bot.polling(True)