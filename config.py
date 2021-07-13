import os

class Config(object):
    DB_URL = os.environ.get("DB_URL", "xxxxxxxxxxxx")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", " 1797025883:AAEKRpNY4B88s9PyG-W8kwVSt1QZgAFwOJM")
    EVERYONE_CHATS = os.environ.get("EVERYONE_CHATS", "-1001552567958")
    API_ID = int(os.environ.get("API_ID", 4834535))
    API_HASH = os.environ.get("API_HASH", "93e3ec1796b0a6a6f1f9158415752bab")
    LICHER_CHAT = os.environ.get("LICHER_CHAT", "-1001552567958")
    ADMIN_CHATS = os.environ.get('ADMIN_CHATS', "-1001552567958")
