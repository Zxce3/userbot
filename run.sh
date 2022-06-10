#!/bin/sh

set -e

. ./.env
. ./venv/bin/activate

mkdir -pv "$DATA_DIR"

python -m userbot
