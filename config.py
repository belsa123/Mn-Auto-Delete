from dotenv import load_dotenv
load_dotenv()

import os

class BOT:
    TOKEN = os.environ.get("TOKEN", "7589055357:AAHarvk9rGaJoHUVta4NYMOjfWf7rVQpA0E")

class API:
    HASH = os.environ.get("API_HASH", "adfd92666a3cce231cf750514a57920d")
    ID = int(os.environ.get("API_ID", 16767636))

class OWNER:
    ID = int(os.environ.get("OWNER", 808533633))

class WEB:
    PORT = int(os.environ.get("PORT", 8000))

class CHATS:
    IDS = list(map(int, os.environ.get("CHATS", "-1002242134235 -1002284460452").split())) if os.environ.get("CHATS") else []
    DELETE_DELAY = int(os.environ.get("DELETE_DELAY", "5")) 
