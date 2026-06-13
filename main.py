import os
import telebot

# Paste your actual fresh token here
BOT_TOKEN = "8773341112:AAGMk5KBa7oPfdxReBpWlpZkjSZp_QY3Nvs"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me any username/handle to check if it has been picked or not.")

@bot.message_handler(func=lambda message: True)
def check_username(message):
    username = message.text.strip().replace('@', '')
    bot.reply_to(message, f"Checking if @{username} is available...")
    
    # Simple checker test logic
    import requests
    try:
        res = requests.get(f"https://t.me/{username}")
        if "If you have Telegram, you can contact" in res.text and "right away" in res.text:
            bot.send_message(message.chat.id, f"✅ @{username} appears to be AVAILABLE!")
        else:
            bot.send_message(message.chat.id, f"❌ @{username} is already TAKEN.")
    except Exception:
        bot.send_message(message.chat.id, "Error checking username. Try again.")

print("Starting Username Checker Bot...")
bot.infinity_polling()
