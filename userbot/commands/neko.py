from userbot import app
from pyrogram import filters
import requests


# Usage: neko [-h|ARG]
@app.on_message(filters.command("neko", prefixes=".") & filters.me)
async def getNeko(app, msg):
    url_api = "http://api.nekos.fun:8080/api/"
    url_help = "https://www.nekos.fun/apidoc.html"
    cmd = msg.command

    if len(cmd) == 1:
        cmd = cmd[0]
    else:
        cmd = cmd[1]
        if cmd == "-h":
            await msg.reply(url_help)
            return

    try:
        res = requests.get(url_api + cmd)
        if res.status_code == 404:
            await msg.reply(f"Unknown tag! See: {url_help}")
            return

        img = res.json()["image"]
        ext = img.split(".")[-1]

        rep = msg.from_user.id
        if msg.reply_to_message_id:
            rep = msg.reply_to_message_id

        if ext == "gif":
            await app.send_animation(msg.chat.id, animation=img,
                                     reply_to_message_id=rep)
        else:
            await app.send_photo(msg.chat.id, photo=img,
                                 reply_to_message_id=rep)
    # Dumb exception handler :v
    except Exception as e:
        print(e)

print("neko.py has been loaded")
