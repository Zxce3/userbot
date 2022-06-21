from userbot import app
from pyrogram import filters


# Usage: info
@app.on_message(filters.command("info", prefixes=".") & filters.me)
async def getInfo(app, msg):
    _ = app
    rep = msg.reply_to_message

    if (rep):
        _msg = await app.get_users(rep.from_user.id)
        await msg.reply(f"```{_msg}```")
    else:
        _msg = await app.get_me()
        await msg.reply(f"```{_msg}```")

print("basic.py has been loaded")
