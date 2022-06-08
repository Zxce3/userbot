#!/bin/env python3


import os
import sys
import asyncio
import pyrogram


API_ID   = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
DATA_DIR = os.getenv("DATA_DIR")

def die(msg):
    print(f"{msg} must be provided!", file=sys.stderr)
    sys.exit(1)

def setup():
    if (API_ID == None):
        die("API_ID")

    if (API_HASH == None):
        die("API_HASH")

    if (DATA_DIR == None):
        die("DATA_DIR")

    return pyrogram.Client(name="userbot",
                           api_id=API_ID,
                           api_hash=API_HASH,
                           app_version="userbot 0.0.1",
                           device_model="Linux",
                           workdir=DATA_DIR)


if __name__ == "__main__":
    client = setup()

    client.run()
