"""User models utilities."""

# Utilities
from django.utils import timezone


def set_picture_filename(instance, filename):
    """Return filename composed by UUID as integer and timestamp."""
    extension = filename.split('.')[-1]
    timestamp = str(int(timezone.now().timestamp()))
    user_id = str(instance.uuid.int)
    return 'users/pictures/{}_{}.{}'.format(user_id, timestamp, extension)
