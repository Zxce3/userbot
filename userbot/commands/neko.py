from userbot import app, commands
from pyrogram import filters
import requests
import logging
from userbot.utils.misc import modules_help, prefix


sfw = "**Kiss** : `Kissing images`\n**Lick** : `Lick`\n**Hug** : `Give someone a hug`\n**Baka** : `B-Baka!!!`\n**cry** : `:,(`\n**Poke** : `Senpai notice meeeee!`\n**Smug** : `What to put here?`\n**Slap** : `Ope`\n**Tickle** : `;)`\n**Pat** : `Pat someone`\n**Laugh** : `HaHaHaHa`\n**Feed** : `I want foooooodddddd`\n**Cuddle** : `well in this context.... An intesnse hug`\n"
"**Cuddle** : `well in this context.... An intesnse hug`\n"
nsfw ="**4K** : `Real 4K images (mostly 4k but all uhd)`\n**Ass** : `Reall Asses`\n**Blowjob/BJ** : `d-do I need to explain > ///< (anime)`\n**Boobs** : `Real breasts`\n**Cum** : `Baby gravy!`\n**Feet** : `👀`\n**hentai** : `random hentai`\n**wallpapers** : `99% sfw`\n**spank** : `NSFW for butts`\n**gasm** : `aheago`\n**lesbian** : `girls rule!`\n**lewd** : `**WARNING** this folder is unsorted I would not use it untill weve filtered out loli/shota content`\n**pussy** : `u-ummm > ///<`\n"
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
        if cmd == "sfw":
            await msg.edit(f"**SFW (Safe for work) list** \n\n{sfw}")
            return
        if cmd == "nsfw":
            await msg.edit(f"**NSFW (NOT safe for work) list** \n\n{nsfw}")
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


modules_help["neko"] = {
    "neko [neko name]": "Get neko",
    "neko sfw": "to see list sfw",
    "neko nsfw": "to see list nsfw"
    }