# -*- coding: utf-8 -*-

"""Development environment settings."""

from .base import * #  NOQA


DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env('DJANGO_SECRET_KEY')

INSTALLED_APPS += (
    'django_extensions',
)

ALLOWED_HOSTS = [
    '{{ cookiecutter.project_slug }}.dev',
    'localhost',
    '127.0.0.1',
]
