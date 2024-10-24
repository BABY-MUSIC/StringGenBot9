import asyncio
import importlib
import logging
import threading
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pyrogram import idle
from StringGen import Anony, ALL_MODULES

# Set up logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

app = FastAPI()

async def anony_boot():
    try:
        LOGGER.info("Starting the bot...")
        await Anony.start()
        LOGGER.info("Bot started successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to start the bot: {ex}")
        quit(1)

    # Import all modules
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("StringGen.modules." + all_module)
            LOGGER.info(f"Module {all_module} loaded successfully.")
        except Exception as ex:
            LOGGER.error(f"Error loading module {all_module}: {ex}")

    LOGGER.info(f"@{Anony.username} started.")
    await idle()  # Keep the bot running

def start_bot():
    try:
        asyncio.run(anony_boot())
    except Exception as ex:
        LOGGER.error(f"Error running bot: {ex}")

@app.on_event("startup")
async def startup_event():
    # Start the bot in a separate thread
    threading.Thread(target=start_bot).start()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": f"String Gen Bot started by @{Anony.username}"})

if __name__ == "__main__":
    # Start the FastAPI server on port 8000
    import uvicorn
    LOGGER.info("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
