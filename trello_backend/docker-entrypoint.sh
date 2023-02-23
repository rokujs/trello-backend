#!/bin/sh

# apply database migrations
echo "---apply database migrations---"
/root/env/bin/python manage.py migrate

# runserver
echo "---run server---"
/root/env/bin/gunicorn trello.wsgi --workers=2 --bind 0.0.0.0:8000 --reload
