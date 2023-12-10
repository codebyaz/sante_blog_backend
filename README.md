## Load initial data

#### workspace_directory/sante_blog_backend

    python manage.py shell < fixtures_generator.py
    python manage.py loaddata fixtures

case refreshing the database is necessary ``python manage.py flush``
