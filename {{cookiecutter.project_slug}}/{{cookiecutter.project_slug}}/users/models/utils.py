"""User models utilities."""

# Utilities
from django.utils import timezone


def set_picture_filename(instance, filename):
    {% if cookiecutter.use_uuids == 'y' -%}
    """Return filename composed by UUID as integer and timestamp."""
    {% else %}
    """Return filename compose by formated ID and timestamp."""
    {%- endif %}
    extension = filename.split('.')[-1]
    timestamp = str(int(timezone.now().timestamp()))
    {% if cookiecutter.use_uuids == 'y' -%}
    user_id = str(instance.uuid.int)
    {% else %}
    user_id = str(instance.pk).zfill(15)
    {%- endif %}
    return 'users/pictures/{}_{}.{}'.format(user_id, timestamp, extension)
