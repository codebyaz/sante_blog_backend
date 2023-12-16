python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# make migrations
python3 manage.py migrate