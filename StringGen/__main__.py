import importlib
import threading
from flask import Flask
from pyrogram import Client, idle
from StringGen import LOGGER, Anony
from StringGen.modules import ALL_MODULES
import os

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "StringGen Bot is running!"

def run_flask():
    port = int(os.environ.get('PORT', 8000))  # Default port for Koyeb is 8000
    app.run(host="0.0.0.0", port=port)

def anony_boot():
    try:
        LOGGER.info("Attempting to start the bot...")
        Anony.start()  # Start the bot synchronously
        LOGGER.info(f"Bot started as @{Anony.username}")
    except Exception as ex:
        LOGGER.error(f"Error while starting bot: {ex}")
        quit(1)  # Exit if there's any error while starting the bot

    # Load all the modules
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("StringGen.modules." + all_module)
            LOGGER.info(f"Loaded module: {all_module}")
        except Exception as e:
            LOGGER.error(f"Error loading module {all_module}: {e}")

    LOGGER.info(f"@{Anony.username} Started successfully.")
    idle()  # Keeps the bot running

if __name__ == "__main__":
    try:
        # Start the Flask server in a separate thread
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.start()

        # Start the bot
        anony_boot()

    except KeyboardInterrupt:
        LOGGER.info("Stopping String Gen Bot...")
        Anony.stop()
        LOGGER.info("Bot and server stopped.")
