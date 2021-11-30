#! bin/bash

#git clone https://github.com/marcomasulli/flasklet.git
sudo apt install python3-pip python3.8-venv
cd flasklet
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
