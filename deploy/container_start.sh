#!/bin/sh

    cd /usr/src/app/
    python manage.py migrate  # apply database migrations
    python manage.py collectstatic --clear --noinput # clearstatic files
    python manage.py collectstatic --noinput  # collect static files

    gunicorn --reload config.wsgi:application -b 0.0.0.0:8000
