#! bin/bash

sudo apt install python3-pip python3.8-venv
cd casa
python3 -m venv .env && source .env/bin/activate && pip install -r requirements.txt
