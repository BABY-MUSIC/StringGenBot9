import asyncio
import importlib
import os
import threading
from flask import Flask
from pyrogram import idle
from StringGen import LOGGER, Anony
from StringGen.modules import ALL_MODULES

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

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

if __name__ == "__main__":
    # Start the Flask app in a separate thread
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8000)))).start()
    
    # Start the Telegram bot
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping String Gen Bot...")
