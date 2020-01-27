import telebot
import requests
from telebot import apihelper
import random
apihelper.proxy = {"https": 'https://78.8.126.198:8080'}
bot = telebot.TeleBot('871294244:AAHWg7AdS4JXa-Y0B-NZKHo5vn4FidkU3G4')

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, {0}'.format(message.from_user.first_name))

bot.polling()