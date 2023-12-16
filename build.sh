#!/bin/bash

echo '### installing requirements to allow running django manage ###'
pip install -r requirements.txt

echo '### collecting static files ###'
python3 manage.py collectstatic

echo '### create superuser ###'
python3 manage.py createsuperuser --noinput