#!/bin/env python3


import os
import sys
import asyncio
from pyrogram import Client


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


app = Client(name="userbot",
             api_id=API_ID,
             api_hash=API_HASH,
             app_version="userbot 0.0.1",
             device_model="Linux",
             workdir=DATA_DIR)


if __name__ == "__main__":
    app.run()
