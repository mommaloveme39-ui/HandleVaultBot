import os
import telebot

# Paste your BRAND NEW token here
8773341112:AAEj1r5HOfbqUJrwaKk9kmFTjvL2aMeJUiw
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! The bot is working.")

print("Starting bot polling...")
bot.infinity_polling()
