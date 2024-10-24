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

if __name__ == "__main__":
    # Run Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    
    # Start the Flask thread
    flask_thread.start()
    
    # Run the bot in the main thread using asyncio
    asyncio.run(anony_boot())

    # Wait for the Flask thread to finish
    flask_thread.join()

    LOGGER.info("Stopping String Gen Bot...")
