from userbot import app
from userbot.utils.misc import modules_help, prefix
from pyrogram import filters
import requests

@app.on_message(filters.command("stack", prefix) & filters.me)
async def stack(app, msg):
    await msg.edit("Processing...")
    if len(msg.command) < 2:
        await msg.edit(f"`{prefix}stack` **query**")
        return
    query = msg.text.split(None, 1)[1]
    url = "https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&q=" + query + "&accepted=True&site=stackoverflow"
    r = requests.get(url)
    if r.status_code == 404:
        await msg.edit("Query not found")
        return
    data = r.json()
    text = f"**Search results for {query}**\n\n"""
    for i in data["items"]:
        title = i["title"]
        link = i["link"]
        output = f"""
**Title:** `{title}`
**Link:** {link}
"""
        text += output
    # bypass long message error
    if len(text) > 4096:
        text = text[:4096]
    await msg.edit(text)

# help module
modules_help['stack'] = {
    'stack <query>': 'Search query on stackoverflow'
    }
