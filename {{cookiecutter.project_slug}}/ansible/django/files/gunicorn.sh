#!/bin/sh

python3 /app/manage.py collectstatic --noinput
python3 /app/manage.py migrate

/usr/local/bin/gunicorn config.wsgi -w 4 -b 127.0.0.1:5000 --chdir=/app
