from pyrogram import Client, filters
from pyrogram.types import Message

from userbot.utils.db import db
from userbot.utils.scripts import restart
from userbot.utils.misc import modules_help, prefix

# enable and disable welcome message
@Client.on_message(
    filters.command(["welcome", "welcomemsg"], prefix) & filters.me
)
async def welcome(_, message: Message):
    if len(message.command) > 1:
        if message.command[1] == "on":
            db.set("core.main", "welcome", True)
            await message.edit("**Welcome message is enabled!**")
        elif message.command[1] == "off":
            db.set("core.main", "welcome", False)
            await message.edit("**Welcome message is disabled!**")
        else:
            await message.edit("**Usage:**\n`welcome on` - enable welcome message\n`welcome off` - disable welcome message")
    else:
        await message.edit("**Usage:**\n`welcome on` - enable welcome message\n`welcome off` - disable welcome message")

# set welcome message

@Client.on_message(
    filters.command(["setwelcome", "setwelcomemsg"], prefix) & filters.me
)
async def setwelcome(_, message: Message):
    if len(message.command) > 1:
        msg = message.text.split(None, 1)[1]
        db.set("core.main", "welcome_msg", msg)
        await message.edit(f"**Welcome message is set!**\n\n{msg}")
    else:
        await message.edit("**Usage:**\n`setwelcome [message]`")

@Client.on_message(
    filters.new_chat_members &
    filters.group
)

async def welcome_new(client: Client, message: Message):
    if db.get("core.main", "welcome"):
        msg = db.get("core.main", "welcome_msg")
        if msg:
            await message.reply(msg.format(message.from_user.mention))
        else:
            await message.reply(f"**Hai {message.from_user.mention}!**")

modules_help["welcome"] = {
    "welcome on": "Enable welcome message",
    "welcome off": "Disable welcome message",
    "setwelcome [message]": "Set welcome message",
}