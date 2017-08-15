"""Users models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Managers
from {{cookiecutter.project_slug}}.users.managers import UserManager

# Utils
{% if cookiecutter.use_uuids == 'y' -%}
import uuid
{%- endif %}
from {{cookiecutter.project_slug}}.users.models.utils import set_picture_filename


class User(AbstractBaseUser):
    """User model."""

    {% if cookiecutter.use_uuids == 'y' -%}
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    {%- endif %}
    email = models.EmailField(
        'email',
        unique=True,
        error_messages={'unique': 'This email address is already in use.'}
    )

    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    picture = models.ImageField('picture', upload_to=set_picture_filename, null=True, blank=True)

    is_admin = models.BooleanField(
        'admin status',
        default=False,
        help_text='Designates whether the user can log into the admin site.'
    )
    is_active = models.BooleanField(
        'admin status',
        default=False,
        help_text='Designates whether the user should be treated as active. Unselect this instead of deleting accounts.'
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into the admin site.'
    )

    # Metadata
    created = models.DateTimeField(
        'creation date',
        auto_now_add=True,
        help_text='Identifies the exact datetime when the user was first created'
    )
    modified = models.DateTimeField(
        'last modification date',
        auto_now_add=True,
        help_text='Identifies the exact datetime when the user data was last modified'
    )

    # Manager
    objects = UserManager()

    # User configuration
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        """Check single permission."""
        return True

    def has_module_perms(self, app_label):
        """Check module permissions."""
        return True

    def get_short_name(self):
        """Return first_name."""
        return self.first_name

    def get_full_name(self):
        """Return first_name + last_name."""
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        """Return user's email."""
        return self.email
