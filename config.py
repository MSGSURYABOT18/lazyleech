import os

class Config(object):
    DB_URL = os.environ.get("DB_URL", "xxxxxxxxxxxx")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1880548732:AAEzASDcPx0D9UibII8ZGpvjyZITpgaPj10")
    EVERYONE_CHATS = os.environ.get("EVERYONE_CHATS", "-1001462883083")
    API_ID = int(os.environ.get("API_ID", 1428490))
    API_HASH = os.environ.get("API_HASH", "5c9503dce40dd0a522712aede1093b6f")
    LICHER_CHAT = os.environ.get("LICHER_CHAT", "-1001462883083")
    ADMIN_CHATS = os.environ.get('ADMIN_CHATS', "-1001462883083")
