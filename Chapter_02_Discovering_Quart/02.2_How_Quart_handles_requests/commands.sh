#!/bin/bash

sudo apt-get install python3-venv
python3 -m venv my_venv

source my_venv/bin/activate

pip3 install quart

python3 quart_basic.py

curl -v http://localhost:5000/api


python3 quart_details.py
curl -v http://localhost:5000/api


python3 variables.py
curl -v http://localhost:5000/person/3


python3 quart_converter.py
curl -v http://localhost:5000/person/1

python3 url_for.py

python3 quart_auth.py
curl http://localhost:5000/ --user alice:password

python3 yamlify.py
