#!/bin/bash

echo '### creating venv ###'
python3 -m venv env

echo '### activate venv ###'
source env/bin/activate

echo '### installing requirements to allow running django manage ###'
pip install -r requirements.txt

echo '### collecting static files ###'
python3 manage.py collectstatic

echo '### running migrations ###'
python3 manage.py migrate

echo '### create superuser ###'
python3 manage.py createsuperuser --noinput