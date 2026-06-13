import os
import threading
from flask import Flask
# Import your bot library here, e.g., telebot

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Start Flask in a background thread
    threading.Thread(target=run_flask, daemon=True).start()
    
    # Start your bot polling
    # Ensure this is a blocking call (it will keep the main script running)
    print("Starting bot polling...")
    # e.g., bot.infinity_polling()
