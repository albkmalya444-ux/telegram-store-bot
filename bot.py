import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("TOKEN")
ADMIN_ID = 6640201644  #

bot = telebot.TeleBot(8227205835:AAGDshagYcqrC7QH6FzneYRcxt2RTSwCIPU)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("شراء حساب انستغرام - 10$", callback_data="buy"))
    bot.send_message(message.chat.id, "اهلاً بك 👋 اختر منتج:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "buy":
        text = """💳 طرق الدفع:

Binance Pay:
1185027764

او

USDT TRC20:
0xb4c9217a41cd3b3e1be541ce92d4a5bd0a4b8494

بعد الدفع اضغط تم الدفع"""
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("تم الدفع", callback_data="paid"))
        bot.send_message(call.message.chat.id, text, reply_markup=markup)

    elif call.data == "paid":
        bot.send_message(ADMIN_ID, f"طلب جديد من ID: {call.from_user.id}")
        bot.send_message(call.message.chat.id, "تم استلام طلبك ⏳ جاري التحقق")

bot.infinity_polling()
