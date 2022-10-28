from userbot import app
from userbot.utils.misc import modules_help, prefix
from pyrogram import filters
import requests

@app.on_message(filters.command("git", prefix) & filters.me)
async def git_user_info(app, msg):
    url = "https://api.github.com/users/"
    if len(msg.command) < 2:
        await msg.edit(f"`{prefix}git` **username**")
        return
    username = msg.text.split(None, 1)[1]
    r = requests.get(url + username)
    if r.status_code == 404:
        await msg.edit("User not found")
        return
    data = r.json()
    avatar_url = r.json()["avatar_url"] + "?v=" + str(r.json()["id"])
    name = data["name"]
    bio = data["bio"]
    company = data["company"]
    blog = data["blog"]
    location = data["location"]
    twitter = data["twitter_username"]
    public_repos = data["public_repos"]
    public_gists = data["public_gists"]
    followers = data["followers"]
    following = data["following"]
    created_at = data["created_at"]
    updated_at = data["updated_at"]
    html_url = data["html_url"]
    text = f"**User info for {username}**\n\n"""
    output = f"""
**Name:** `{name}`
**Bio:** `{bio}`
**Company:** `{company}`
**Blog:** `{blog}`
**Location:** `{location}`
**Twitter:** `{twitter}`
**Public Repos:** `{public_repos}`
**Public Gists:** `{public_gists}`
**Followers:** `{followers}`
**Following:** `{following}`
**Created At:** `{created_at}`
**Updated At:** `{updated_at}`
**Profile:** {html_url}
"""
    await msg.edit(text)
# send image with caption to message
    await app.send_photo(msg.chat.id, photo=avatar_url, caption=output)

# help module
modules_help['git'] = {
    'git <username>': 'Get info about github user'
    }
