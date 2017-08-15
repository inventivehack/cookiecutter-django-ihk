"""Users app configuration file."""

# Django
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """App configuration."""

    name = '{{cookiecutter.project_slug}}.users'
    verbose_name = 'Users'
