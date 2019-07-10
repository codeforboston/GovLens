#!/bin/sh

    python /usr/src/app/manage.py migrate  # apply database migrations
    python /usr/src/app/manage.py collectstatic --clear --noinput # clearstatic files
    python /usr/src/app/manage.py collectstatic --noinput  # collect static files

    gunicorn --reload config.wsgi:application -b 0.0.0.0:8000
