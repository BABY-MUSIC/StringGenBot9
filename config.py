from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "16457832"))
API_HASH = getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")

BOT_TOKEN = getenv("BOT_TOKEN", "7561329328:AAGLoPkySLMXkxjlqSxj3H0lycU68Q7Hvgg")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", "7400383704"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")
