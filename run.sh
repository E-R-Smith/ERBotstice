#!/usr/bin/env bash

set -a
source .env
set +a
cd ./venv/Scripts/
source ./activate
cd ../../

python test.py