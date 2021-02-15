release: python3 manage.py migrate
release: python3 manage.py collectstatic --no-input
web: gunicorn simpletodo.wsgi