#!/bin/sh

set -e

. ./.env
. ./venv/bin/activate

./src/main.py
