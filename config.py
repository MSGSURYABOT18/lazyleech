import os

class Config(object):
    DB_URL = os.environ.get("DB_URL", "xxxxxxxxxxxx")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "xxxxxxxxx")
    EVERYONE_CHATS = os.environ.get("EVERYONE_CHATS", "-100xxxx")
    API_ID = int(os.environ.get("API_ID", xx))
    API_HASH = os.environ.get("API_HASH", "xxxx")
    LICHER_CHAT = os.environ.get("LICHER_CHAT", "xxxxxxx")
    ADMIN_CHATS = os.environ.get('ADMIN_CHATS', "xxxxx")
