from time import perf_counter, sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from userbot.utils.misc import modules_help, prefix


@Client.on_message(filters.command(["ping", "p"], prefix) & filters.me)
async def ping(_, message: Message):
    await message.edit("⚡️")
    sleep(3)
    start = perf_counter()
    await message.edit("Wait..")
    end = perf_counter()
    await message.edit(f"**🏓 PONG !\n⏱ {round(end - start, 3)}s**")


modules_help["ping"] = {
    "ping": "Check ping to Telegram servers",
}
