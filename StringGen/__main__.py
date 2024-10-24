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
        await Anony.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("StringGen.modules." + all_module)

    LOGGER.info(f"@{Anony.username} Started.")
    await idle()

def run_flask():
    port = int(os.environ.get('PORT', 8000))  # Default port is 8000 for Koyeb
    app.run(host="0.0.0.0", port=port)

def run_bot():
    asyncio.run(anony_boot())  # This will ensure the bot runs with the event loop

if __name__ == "__main__":
    # Create two threads: one for Flask and one for the bot
    flask_thread = threading.Thread(target=run_flask)
    bot_thread = threading.Thread(target=run_bot)

    # Start both threads
    flask_thread.start()
    bot_thread.start()

    # Wait for both threads to finish
    flask_thread.join()
    bot_thread.join()

    LOGGER.info("Stopping String Gen Bot...")
