#!/bin/sh

set -e

. ./.env
. ./venv/bin/activate

# mkdir -pv "$DATA_DIR"

reload python3 -m userbot
