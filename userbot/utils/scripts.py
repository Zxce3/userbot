import asyncio
import os
import sys
from io import BytesIO

from PIL import Image
import importlib
import subprocess

from pyrogram import Client, errors, types
import traceback
from .misc import modules_help, prefix, requirements_list


def text(message: types.Message):
    return message.text if message.text else message.caption


def restart():
    os.execvp(sys.executable, [sys.executable, "main.py"])


def format_exc(e: Exception, hint: str = None):
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        return (
            f"**Telegram API error!**\n"
            f"`[{e.CODE} {e.ID or e.NAME}] - {e.MESSAGE}`"
        )
    if hint:
        hint_text = f"\n\n**Hint: {hint}**"
    else:
        hint_text = ""
    return (
        f"**Error!**\n" f"`{e.__class__.__name__}: {e}`" + hint_text
    )


def with_reply(func):
    async def wrapped(client: Client, message: types.Message):
        if not message.reply_to_message:
            await message.edit("**Reply to message is required**")
        else:
            return await func(client, message)

    return wrapped


async def interact_with(message: types.Message) -> types.Message:
    """
    Check history with bot and return bot's response

    Example:
    .. code-block:: python
        bot_msg = await interact_with(await bot.send_message("@BotFather", "/start"))
    :param message: already sent message to bot
    :return: bot's response
    """

    await asyncio.sleep(1)
    # noinspection PyProtectedMember
    response = await message._client.get_history(message.chat.id, limit=1)
    seconds_waiting = 0

    while response[0].from_user.is_self:
        seconds_waiting += 1
        if seconds_waiting >= 5:
            raise RuntimeError("bot didn't answer in 5 seconds")

        await asyncio.sleep(1)
        # noinspection PyProtectedMember
        response = await message._client.get_history(message.chat.id, limit=1)

    interact_with_to_delete.append(message.message_id)
    interact_with_to_delete.append(response[0].message_id)

    return response[0]


interact_with_to_delete = []


def format_module_help(module_name: str):
    commands = modules_help[module_name]

    help_text = f"**Help for |{module_name}|\n\nUsage:**\n"

    for command, desc in commands.items():
        cmd = command.split(maxsplit=1)
        args = " `" + cmd[1] + "`" if len(cmd) > 1 else ""
        help_text += f"`{prefix}{cmd[0]}`{args} — __{desc}__\n"

    return help_text


def format_small_module_help(module_name: str):
    commands = modules_help[module_name]

    help_text = f"**Help for |{module_name}|\n\nCommands list:\n"
    for command, desc in commands.items():
        cmd = command.split(maxsplit=1)
        args = " `" + cmd[1] + "`" if len(cmd) > 1 else ""
        help_text += f"`{prefix}{cmd[0]}`{args}\n"
    help_text += f"\nGet full usage: `{prefix}help {module_name}`**"

    return help_text


def import_library(library_name: str, package_name: str = None):
    """
    Loads a library, or installs it in ImportError case
    :param library_name: library name (import example...)
    :param package_name: package name in PyPi (pip install example)
    :return: loaded module
    """
    if package_name is None:
        package_name = library_name
    requirements_list.append(package_name)

    try:
        return importlib.import_module(library_name)
    except ImportError:
        completed = subprocess.run(["python3", "-m", "pip", "install", package_name])
        if completed.returncode != 0:
            raise AssertionError(
                f"Failed to install library {package_name} (pip exited with code {completed.returncode})"
            )
        return importlib.import_module(library_name)


def resize_image(input_img, output=None, img_type="PNG"):
    if output is None:
        output = BytesIO()
        output.name = f"sticker.{img_type.lower()}"

    with Image.open(input_img) as img:
        # We used to use thumbnail(size) here, but it returns with a *max* dimension of 512,512
        # rather than making one side exactly 512 so we have to calculate dimensions manually :(
        if img.width == img.height:
            size = (512, 512)
        elif img.width < img.height:
            size = (max(512 * img.width // img.height, 1), 512)
        else:
            size = (512, max(512 * img.height // img.width, 1))

        img.resize(size).save(output, img_type)

    return output
