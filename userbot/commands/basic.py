from userbot import app, commands
from pyrogram import filters
import json
from userbot.utils.misc import modules_help, prefix

# get group id and send it to message
@app.on_message(filters.command("id", prefix) & filters.me)
async def getGroupId(app, msg):
    if msg.chat.type == "private":
        await msg.edit("This is private chat")
        return
    await msg.edit(f"Chat id: `{msg.chat.id}`")
    if msg.reply_to_message:
        await msg.edit(f"Chat id: `{msg.chat.id}`\nUser id: `{msg.reply_to_message.from_user.id}`")
    if msg.reply_to_message and msg.reply_to_message.forward_from:
        await msg.edit(f"Chat id: `{msg.chat.id}`\nUser rep id: `{msg.reply_to_message.forward_from.id}`")
    if msg.reply_to_message and msg.reply_to_message.forward_from_chat:
        await msg.edit(f"Chat id: `{msg.chat.id}`\nUser forward from id: `{msg.reply_to_message.forward_from_chat.id}`")
    if msg.reply_to_message and msg.reply_to_message.forward_sender_name:
        await msg.edit(f"Chat id: `{msg.chat.id}`\nUser forward name id: `{msg.reply_to_message.forward_sender_name}`")
    if msg.reply_to_message and msg.reply_to_message.forward_from_message_id:
        await msg.edit(f"Chat id: `{msg.chat.id}`\nUser forward message id: `{msg.reply_to_message.forward_from_message_id}`")

# help module
modules_help["info"] = {
    "id": "get chat id",
}