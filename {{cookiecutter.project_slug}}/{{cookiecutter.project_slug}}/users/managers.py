"""Users managers."""

# Django
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    User manager.

    Handle new users creation and super users creation.
    """

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """Creare and save user with the given email, first_name, last_name and password."""
        if not email:
            raise ValueError('Email is required.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """Create and save user with admin privileges."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)
