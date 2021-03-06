#!/bin/bash

python3 globals.py
curl http://localhost:5000/api

python3 signals.py

python3 middleware.py

python3 email_render.py

python3 prod_settings.py

python3 blueprints.py

python3 error_handler.py
curl http://localhost:5000/api
python3 catch_all_errors.py
