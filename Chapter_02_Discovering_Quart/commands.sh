#!/bin/bash

sudo apt-get install python3-venv
python3 -m venv my_venv

source my_venv/bin/activate

pip3 install quart

python3 quart_basic.py

curl -v http://localhost:5000/api


python3 quart_details.py
curl -v http://localhost:5000/api
