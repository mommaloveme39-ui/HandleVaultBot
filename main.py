import os
import threading
from flask import Flask
# ... your other bot imports ...

# 1. Create a dummy Flask app for Render's port check
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    # Render automatically provides a PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # 2. Start the Flask server in a background thread
    threading.Thread(target=run_flask, daemon=True).start()
    
    # 3. Start your Telegram bot polling below as usual
    print("Starting bot polling...")
    # your_bot.run() or your_bot.infinity_polling()
