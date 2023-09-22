#!/bin/ash

echo "Apply database migrations"
python manage.py migrate
python createsuperuser

exec "$@"
