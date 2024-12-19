import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5552688846:AAGad_D7Tk6CtA-ADQCp-B1KPk2AMzt2dNs")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "2481005"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "acd50fc7a43525751be61c5a9c9bf6a9")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1381004184"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ilmaneha:ClwVXUTl3eGy2Ev3@cluster0.y3krv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
