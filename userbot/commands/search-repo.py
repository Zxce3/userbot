from userbot import app
from userbot.utils.misc import modules_help, prefix
from pyrogram import filters
import requests

@app.on_message(filters.command("repo", prefix) & filters.me)
async def search_repo(app, msg):
    url = "https://api.github.com/search/repositories?q="
    if len(msg.command) < 2:
        await msg.edit(f"`{prefix}search-repo` **query**")
        return
    query = msg.text.split(None, 1)[1]
    r = requests.get(url + query)
    if r.status_code == 404:
        await msg.edit("Repo not found")
        return
    data = r.json()
    text = f"**Search results for {query}**\n\n"""
    for i in data["items"]:
        name = i["name"]
        full_name = i["full_name"]
        description = i["description"]
        html_url = i["html_url"]
        output = f"""
**Name:** `{name}`
**Full Name:** `{full_name}`
**Description:** `{description}`
**Profile:** {html_url}
"""
        text += output
    if len(text) > 4096:
        text = text[:4096]
    await msg.edit(text, disable_web_page_preview=True)

# help module
modules_help['repo'] = {
    'repo <query>': 'Search repo on github'
    }


