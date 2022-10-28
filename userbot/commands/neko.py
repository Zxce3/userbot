from userbot import app, commands
from pyrogram import filters
import requests
import logging
from userbot.utils.misc import modules_help, prefix


dsfw = [
"**Kiss** : `Kissing images`",
"**Lick** : `Lick`",
"**Hug** : `Give someone a hug`",
"**Baka** : `B-Baka!!!`",
"**cry** : `:,(`",
"**Poke** : `Senpai notice meeeee!`",
"**Smug** : `What to put here?`",
"**Slap** : `Ope`",
"**Tickle** : `;)`",
"**Pat** : `Pat someone`",
"**Laugh** : `HaHaHaHa`",
"**Feed** : `I want foooooodddddd`",
"**Cuddle** : `well in this context.... An intesnse hug`"
]

dnsfw = [
"**4K** : `Real 4K images (mostly 4k but all uhd)`",
"**Ass** : `Reall Asses`",
"**Blowjob/BJ** : `d-do I need to explain > ///< (anime)`",
"**Boobs** : `Real breasts`",
"**Cum** : `Baby gravy!`",
"**Feet** : `👀`",
"**hentai** : `random hentai`",
"**wallpapers** : `99% sfw`",
"**spank** : `NSFW for butts`",
"**gasm** : `aheago`",
"**lesbian** : `girls rule!`",
"**lewd** : `⚠️WARNING this folder is unsorted I would not use it untill weve filtered out loli/shota content`",
"**pussy** : `u-ummm > ///<`"
]

# Usage: neko [-h|ARG]
@app.on_message(filters.command("neko", prefix) & filters.me)
async def getNeko(app, msg):
    url_api = "http://api.nekos.fun:8080/api/"
    url_help = "https://www.nekos.fun/apidoc.html"
    cmd = msg.command
    if len(cmd) == 1:
        cmd = cmd[0]
    else:
        cmd = cmd[1]
        if cmd == "-h":
            await msg.edit(f"See: `{prefix}help neko`")
            return
    try:
        res = requests.get(url_api + cmd)
        if res.status_code != 200:
            await msg.edit(f"Unknown tag! See: `{prefix}help neko`")
            return

        img = res.json()["image"]
        ext = img.split(".")[-1]

        rep = msg.from_user.id
        if msg.reply_to_message_id:
            rep = msg.reply_to_message_id

        if ext == "gif":
            await app.send_animation(msg.chat.id, animation=img,
                                     reply_to_message_id=rep)
        else:
            await app.send_photo(msg.chat.id, photo=img,
                                 reply_to_message_id=rep)
    # Dumb exception handler :v
    except Exception as e:
        # print(e)
        logging.warning(e)

# list of categories from data dsfw and dnsfw for nekolist
@app.on_message(filters.command("nekolist", prefix) & filters.me)
async def getNekoList(app, msg):
    sfw = "\n- ".join(dsfw)
    nsfw = "\n- ".join(dnsfw)
    await msg.edit(f"**SFW (Safe for work) list** \n\n- {sfw}\n\n**NSFW (NOT safe for work) list** \n\n- {nsfw}")
# Help module
modules_help['neko'] = {
    'neko <category>': 'Get neko from nekos.life api/v2/img',
    'nekolist': 'List of categories'
    }
