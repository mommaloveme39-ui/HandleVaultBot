import os
import telebot

# 1. Add your token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

# 2. Your bot's commands go here
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! The bot is working.")

# 3. Keep the bot running
print("Starting bot polling...")
bot.infinity_polling()
