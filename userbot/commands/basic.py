from userbot import app
from pyrogram import filters
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
# get user id and send it to message
@app.on_message(filters.command("uid", prefix) & filters.me)
async def getUserId(app, msg):
    if msg.reply_to_message:
        await msg.edit(f"User id: `{msg.reply_to_message.from_user.id}`")
    else:
        await msg.edit("Reply to message")
# get all id and send it to message
@app.on_message(filters.command("allid", prefix) & filters.me)
async def getAllId(app, msg):
    if msg.chat.type == "private":
        await msg.edit("This is private chat")
        return
    if msg.reply_to_message:
        await msg.edit(f"Chat id: `{msg.chat.id}`\nUser id: `{msg.reply_to_message.from_user.id}`\nUser rep id: `{msg.reply_to_message.forward_from.id}`\nUser forward from id: `{msg.reply_to_message.forward_from_chat.id}`\nUser forward name id: `{msg.reply_to_message.forward_sender_name}`\nUser forward message id: `{msg.reply_to_message.forward_from_message_id}`")
    else:
        await msg.edit(f"Chat id: `{msg.chat.id}`")

# get user info and send it to message
@app.on_message(filters.command("info", prefix) & filters.me)
async def getUserInfo(app, msg):
    if msg.reply_to_message:
        await msg.edit(f"**User info**\n\n**First name:** `{msg.reply_to_message.from_user.first_name}`\n**Last name:** `{msg.reply_to_message.from_user.last_name}`\n**Username:** `{msg.reply_to_message.from_user.username}`\n**User id:** `{msg.reply_to_message.from_user.id}`")
    else:
        await msg.edit("Reply to message")
# help module
modules_help["id"] = {
    "id": "get group id",
    "uid": "get user id",
    "allid": "get all id",
}