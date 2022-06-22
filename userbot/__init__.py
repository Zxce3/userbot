import os
import sys
from pyrogram.client import Client


BOT_NAME    = "userbot"
APP_VERSION = f"{BOT_NAME} 0.0.1"
DEV_MODEL   = "Linux"


def die(msg):
    print(f"{msg} must be provided!", file=sys.stderr)
    sys.exit(1)

API_ID = os.getenv("API_ID")
if (API_ID == None):
    die("API_ID")

API_HASH = os.getenv("API_HASH")
if (API_HASH == None):
    die("API_HASH")

DATA_DIR = os.getenv("DATA_DIR")
if (DATA_DIR == None):
    die("DATA_DIR")


app = Client(name=BOT_NAME,
             api_id=API_ID,
             api_hash=API_HASH,
             app_version=APP_VERSION,
             device_model=DEV_MODEL,
             workdir=DATA_DIR)

commands = {}
