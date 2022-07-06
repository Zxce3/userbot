from pyrogram import Client, filters
from pyrogram.types import Message
from userbot.utils.misc import modules_help, prefix
from userbot.utils.scripts import format_module_help

@Client.on_message(filters.command(["help", "h"], prefix) & filters.me)
async def help_cmd(_, message: Message):
    if len(message.command) == 1:
        msg_edited = False
        text = (
            "**Help for Userbot**\n"
            f"For more help on how to use a command, type `{prefix}help [module]`\n\n"
            "Available Modules:\n"
        )

        for module_name, module_commands in modules_help.items():
            text += "• {}: {}\n".format(
                module_name.title(),
                " ".join(
                    [
                        f"`{prefix + cmd_name.split()[0]}`"
                        for cmd_name in module_commands.keys()
                    ]
                ),
            )
            if len(text) >= 2048:
                text += "*"
                if msg_edited:
                    await message.reply(text, disable_web_page_preview=True)
                else:
                    await message.edit(text, disable_web_page_preview=True)
                    msg_edited = True
                text = "*"

        text += f"\nThe number of modules in the userbot: {len(modules_help) / 1}"

        if msg_edited:
            await message.reply(text, disable_web_page_preview=True)
        else:
            await message.edit(text, disable_web_page_preview=True)
    elif message.command[1].lower() in modules_help:
        await message.edit(format_module_help(message.command[1].lower()))
    else:
        # TODO: refactor this cringe
        command_name = message.command[1].lower()
        for name, commands in modules_help.items():
            for command in commands.keys():
                if command.split()[0] == command_name:
                    cmd = command.split(maxsplit=1)
                    cmd_desc = commands[command]
                    return await message.edit(
                        f"*Help for command `{prefix}{command_name}`\n"
                        f"Module: {name} (`{prefix}help {name}`)*\n\n"
                        f"`{prefix}{cmd[0]}`"
                        f"{' `' + cmd[1] + '`' if len(cmd) > 1 else ''}"
                        f" — __{cmd_desc}__"
                    )
        await message.edit(f"*Module {command_name} not found*")


modules_help["help"] = {"help [module/command name]": "Get common/module/command help"}