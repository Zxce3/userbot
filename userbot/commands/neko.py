from userbot import app
from pyrogram import filters
import json
import requests


# Usage: neko [-h|ARG]
@app.on_message(filters.command("neko", prefixes=".") & filters.me)
async def getNeko(app, msg):
    url_api = "http://api.nekos.fun:8080/api/"
    cmd = msg.command

    if (len(cmd) == 1):
        cmd = cmd[0]
    else:
        cmd = cmd[1]
        if (cmd == "-h"):
            await msg.reply("https://www.nekos.fun/apidoc.html")
            return

    try:
        res = requests.get(url_api + cmd).text
        img = json.loads(res)["image"]
        rep = msg.reply_to_message

        if (rep):
            await msg.reply(img)
        else:
            await msg.edit_text(img)
    except:
        pass

print("neko.py has been loaded")
