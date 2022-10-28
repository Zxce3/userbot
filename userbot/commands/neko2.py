# get neko from nekos.fun api/v2/img
from userbot import app
from userbot.utils.misc import modules_help, prefix
from pyrogram import filters
import requests

data = [
    'smug',
    'woof',
    'gasm',
    '8ball',
    'goose',
    'cuddle',
    'avatar',
    'slap',
    'v3',
    'pat',
    'gecg',
    'feed',
    'fox_girl',
    'lizard',
    'neko',
    'hug',
    'meow',
    'kiss',
    'wallpaper',
    'tickle',
    'spank',
    'waifu',
    'lewd',
    'ngif'
]

# create query command for neko2
@app.on_message(filters.command("neko2", prefix) & filters.me)
async def neko2(app, msg):
    url = "https://nekos.life/api/v2/img/"
    if len(msg.command) < 2:
        await msg.edit(f"`{prefix}neko2` **category**")
        return
    category = msg.text.split(None, 1)[1]
    r = requests.get(url + category)
    if r.status_code == 404:
        await msg.edit("Category not found")
        return
    data = r.json()
    url = data["url"]
    await msg.edit(f"**Neko for {category}**")
    # fix gif image
    ext = url.split(".")[-1]
    if ext == "gif":
        await app.send_animation(msg.chat.id, animation=url)
    else:
        await app.send_photo(msg.chat.id, photo=url)

# list of categories from data
@app.on_message(filters.command("neko2list", prefix) & filters.me)
async def neko2list(app, msg):
    # parse data to string and make list of categories
    categories = "\n-".join(data)
    # usage of categories
    text = f"usage: `{prefix}neko2` **-category**\n\n**Categories:**\n-{categories}"""
    await msg.edit(text)

# help module
modules_help['neko2'] = {
    'neko2 <category>': 'Get neko from nekos.life api/v2/img',
    'neko2list': 'List of categories'
    }
