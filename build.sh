# install requirements
echo '### installing requirements to allow running django manage ###'
pip install -r requirements.txt

# collect static files
echo '### collecting static files ###'
python3 manage.py collectstatic
python manage.py createsuperuser --username $ADMIN_USER --password $ADMIN_PASSWORD