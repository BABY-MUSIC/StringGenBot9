import threading
import importlib
import asyncio
from flask import Flask
from pyrogram import idle
from StringGen import LOGGER, Anony
from StringGen.modules import ALL_MODULES
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "StringGen Bot is running!"

async def anony_boot():
    try:
        LOGGER.info("Attempting to start the bot...")
        await Anony.start()  # Start the bot
        LOGGER.info(f"Bot started as @{Anony.username}")
    except Exception as ex:
        LOGGER.error(f"Error while starting bot: {ex}")
        quit(1)  # Exit if there's any error while starting the bot

    for all_module in ALL_MODULES:
        try:
            importlib.import_module("StringGen.modules." + all_module)
            LOGGER.info(f"Loaded module: {all_module}")
        except Exception as e:
            LOGGER.error(f"Error loading module {all_module}: {e}")

    LOGGER.info(f"@{Anony.username} Started successfully.")
    await idle()  # Keeps the bot running

def run_flask():
    port = int(os.environ.get('PORT', 8000))  # Default port for Koyeb is 8000
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    
    # Start the Flask thread
    flask_thread.start()

    # Run the bot in the main thread using asyncio
    asyncio.run(anony_boot())

    # Wait for the Flask thread to finish
    flask_thread.join()

    LOGGER.info("Stopping String Gen Bot...")
