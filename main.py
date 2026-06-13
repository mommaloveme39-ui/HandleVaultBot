import os
import telebot

# 1. Add your token
8773341112:AAGu5MuAFZhwtKJNeyOQ1L6Wl72q1gT52mw
# 2. Your bot's commands go here
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! The bot is working.")

# 3. Keep the bot running
print("Starting bot polling...")
bot.infinity_polling()
