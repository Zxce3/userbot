from pyrogram import Client, filters
from pyrogram.types import Message

from userbot.utils.db import db
from userbot.utils.scripts import restart
from userbot.utils.misc import modules_help, prefix


@Client.on_message(
    filters.command(["sp", "setprefix"], prefix) & filters.me
)
async def setprefix(_, message: Message):
    if len(message.command) > 1:
        pref = message.command[1]
        db.set("core.main", "prefix", pref)
        await message.edit(f"**Prefix [ `{pref}` ] is set!**")
        restart()
    else:
        await message.edit("**The prefix must not be empty!**")


modules_help["prefix"] = {
    "setprefix [prefix]": "Set custom prefix",
    "sp [prefix]": "Set custom prefix",
}
