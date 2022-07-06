import os
import sys
from . import app
from pyrogram import idle, errors
from userbot.utils.db import db
from userbot.utils.scripts import restart
from pathlib import Path
from importlib import import_module
import logging
import platform
import sqlite3
import subprocess

logging.basicConfig(format='[%(levelname)s] at %(asctime)s:\n» %(message)s',
                    datefmt='%I:%M:%S %p', 
                    level=logging.INFO)
if __name__ == "__main__":
    script_path = os.path.dirname(os.path.realpath(__file__))
    if script_path != os.getcwd():
        os.chdir(script_path)
    # _ = userbot.commands
    # app.run()
    try:
        app.start()
    except sqlite3.OperationalError as e:
            logging.warning(
                f"Session file is locked.{e}"
            )
            die()
    except (errors.NotAcceptable, errors.Unauthorized) as e:
        logging.error(
            f"{e.__class__.__name__}: {e}\n"
            f"Get help"
        )
        die()

    success_handlers = 0
    failed_handlers = 0
    success_modules = 0
    failed_modules = 0

    for path in sorted((Path("commands")).rglob("*.py")):
        module_path = "userbot." + ".".join(path.parent.parts + (path.stem,))

        try:
            module = import_module(module_path)
            for name, obj in vars(module).items():
                # defaulting to [] if obj isn't a function-handler
                for handler, group in getattr(obj, "handlers", []):
                    try:
                        app.add_handler(handler, group)
                        success_handlers += 1
                    except Exception as e:
                        failed_handlers += 1
                        logging.warning(
                            f"Can't add {module_path}.{name}.{handler.__name__}: {e.__class__.__name__}: {e}"
                        )
        except Exception as e:
            logging.warning(
                f"Can't import module {module_path}: {e.__class__.__name__}: {e}"
            )
            failed_modules += 1
        else:
            success_modules += 1

    logging.info(
        f"Imported {success_handlers} handlers from {success_modules} modules."
    )
    if failed_modules:
        logging.warning(f"Failed to import {failed_modules} modules")
    if failed_handlers:
        logging.warning(f"Failed to add {failed_handlers} to handlers")

    if len(sys.argv) == 4:
        restart_type = sys.argv[3]
        if restart_type == "1":
            text = "**Update process completed!**"
        else:
            text = "**Restart completed!**"
        try:
            app.send_message(
                chat_id=sys.argv[1], text=text, reply_to_message_id=int(sys.argv[2])
            )
        except errors.RPCError:
            app.send_message(chat_id=sys.argv[1], text=text)

    logging.info("app started!")

    idle()