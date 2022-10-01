import os
import sys
import platform
from pyrogram import Client, enums

BOT_NAME    = "Userbot"
APP_VERSION = f"{BOT_NAME} 0.0.1"
DEV_MODEL   = "Linux"

script_path = os.path.dirname(os.path.realpath(__file__))
if script_path != os.getcwd():
    os.chdir(script_path)

def die(msg):
    print(f"{msg} must be provided!", file=sys.stderr)
    sys.exit(1)

API_ID = os.getenv("API_ID")
if API_ID is None:
    die("API_ID")

API_HASH = os.getenv("API_HASH")
if API_HASH is None:
    die("API_HASH")

DATA_DIR = os.getenv("DATA_DIR")
if DATA_DIR is None:
    die("DATA_DIR")

SESSION_STRING = os.getenv("SESSION_STRING")
if SESSION_STRING is None:
    die("SESSION_STRING")

DB_NAME = os.getenv("DB_NAME")
if DB_NAME is None:
    die("DB_NAME")

DB_URL = os.getenv("DB_URL")
if DB_URL is None:
    pass

DB_TYPE = os.getenv("DB_TYPE")
if DB_TYPE is None:
    die("DB_TYPE")

app = Client(name=BOT_NAME,
             api_id=API_ID,
             api_hash=API_HASH,
             app_version=APP_VERSION,
             device_model=DEV_MODEL,
             workdir=script_path,
             sleep_threshold=30,
             system_version=platform.version() + " + " + platform.machine(),
             session_string=SESSION_STRING,
             parse_mode=enums.ParseMode.MARKDOWN
             )
