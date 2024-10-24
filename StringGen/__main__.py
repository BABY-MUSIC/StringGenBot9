import asyncio
import importlib

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pyrogram import idle

from StringGen import LOGGER, Anony
from StringGen.modules import ALL_MODULES

app = FastAPI()

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

@app.on_event("startup")
async def startup_event():
    await anony_boot()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": f"String Gen Bot started by @{Anony.username}"})

if __name__ == "__main__":
    # Start the FastAPI server on port 8000
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    LOGGER.info("Stopping String Gen Bot...")
