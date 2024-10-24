import asyncio
import importlib
import threading
from flask import Flask
from pyrogram import idle

from StringGen import LOGGER, Anony
from StringGen.modules import ALL_MODULES

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

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

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(anony_boot())

def run_flask():
    app.run(host='0.0.0.0', port=8000)  # Port 8000 par run karein

if __name__ == "__main__":
    # Bot aur Flask ko alag threads par run karna
    bot_thread = threading.Thread(target=run_bot)
    flask_thread = threading.Thread(target=run_flask)

    bot_thread.start()
    flask_thread.start()

    bot_thread.join()  # Bot thread complete hone ka intezaar karein
    flask_thread.join()  # Flask thread complete hone ka intezaar karein
