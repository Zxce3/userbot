from userbot import app
from pyrogram import filters


# Usage: info
@app.on_message(filters.command("info", prefixes=".") & filters.me)
async def getInfo(app, msg):
    _ = app

    if msg.reply_to_message:
        await msg.reply(f"```{msg.reply_to_message.from_user}```")
    else:
        await msg.reply(f"```{msg.from_user}```")

print("basic.py has been loaded")
