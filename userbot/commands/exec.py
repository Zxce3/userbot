from userbot import app
from userbot.utils.misc import modules_help, prefix
from pyrogram import filters
import asyncio

# exec os command and send output to message
@app.on_message(filters.command(["exec",">"], prefix) & filters.me)
async def execCommand(app, msg):
    if len(msg.command) < 2:
        await msg.edit("Usage: `exec [command]`")
        return
    command = msg.text.split(" ", 1)[1]
    await msg.edit(f"Executing command: `{command}`")
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    output = f"**Output:**\n`{stdout.decode().strip()}`"
    if stderr.decode():
        output += f"\n**Error:**\n`{stderr.decode().strip()}`"
    # bypass 4096 char limit to file txt
    if len(output) > 4096:
        with open("output.txt", "w") as f:
            f.write(output)
        await msg.reply_document("output.txt")
        return
    await msg.edit(output)

# help module
modules_help["exec"] = {
    "exec": "execute command",
}
