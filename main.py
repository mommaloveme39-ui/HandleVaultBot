import os
import telebot
import requests

# 1. Your active token
BOT_TOKEN = "8773341112:AAGu5MuAFZhwtKJNeyOQ1L6Wl72q1gT52mw"
bot = telebot.TeleBot(BOT_TOKEN)

# 2. Welcome message when someone presses /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to HandleVaultBot! Send me a username/handle to check its availability.")

# 3. Handle checking the username
@bot.message_handler(func=lambda message: True)
def check_username(message):
    username = message.text.strip()
    
    # Clean the input if they included '@'
    if username.startswith('@'):
        username = username[1:]
        
    bot.reply_to(message, f"Checking availability for: @{username}...")
    
    # TODO: Add your specific API or scraping logic here to see if the handle is taken
    # For now, a simple placeholder response:
    bot.send_message(message.chat.id, f"Analysis complete for @{username}.")

# 4. Keep it running
print("Starting Username Checker Bot polling...")
bot.infinity_polling()
