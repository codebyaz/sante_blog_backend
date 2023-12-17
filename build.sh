#!/bin/bash

echo '### creating venv ###'
python3 -m venv env

echo '### activating venv ###'
source env/bin/activate

echo '### ensuring pip is up-to-date ###'
python3 -m pip install --upgrade pip

echo '### installing requirements to allow running django manage ###'
pip install -r requirements.txt

echo '### collecting static files ###'
python3 manage.py collectstatic

echo '### running migrations ###'
python3 manage.py migrate

echo '### create superuser ###'
python3 manage.py createsuperuser --noinput --skip-checks

if [ $? -ne 0 ]; then
  echo "user already exists"
fi
