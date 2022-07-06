from userbot import app, commands
from pyrogram import filters
import json
from userbot.utils.misc import modules_help, prefix


# Usage: info
@app.on_message(filters.command("info", prefixes=".") & filters.me)
async def getInfo(app, msg):
    _ = app

    if msg.reply_to_message:
        await msg.reply(f"```{msg.reply_to_message.from_user}```")
    else:
        await msg.reply(f"```{msg.from_user}```")

# Usage: modules
@app.on_message(filters.command("commands", prefixes=".") & filters.me)
async def getCommands(app, msg):
    _ = app

    res = json.dumps(commands, sort_keys=True, indent=4)
    await msg.reply(f"```{res}```")


modules_help["info"] = {"info": "get json info"}
