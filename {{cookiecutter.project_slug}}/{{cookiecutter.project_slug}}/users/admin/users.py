"""Users admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from {{cookiecutter.project_slug}}.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """User admin class."""

    ordering = ('-created',)
    search_fields = ('email',)
    filter_horizontal = ()
    list_display = (
        'email',
        'is_active',
        'is_admin',
        'is_staff',
        'first_name',
        'last_name',
        'created'
    )
    list_filter = (
        'is_active',
        'is_admin',
        'is_staff',
        'created'
    )
    fieldsets = (
        (None, {
            'fields': (('email', 'password'),)
        }),
        (None, {
            'fields': (('first_name', 'last_name', 'picture'),)
        }),
        ('Roles', {
            'fields': (('is_admin', 'is_staff',),)
        }),
        (None, {
            'fields': (('is_active',),)
        })
    )

    readonly_fields = ('is_admin', 'is_staff', 'created', 'modified')

    def has_delete_permission(self, request, obj=None):
        """Disable delete option."""
        return False

    def has_add_permission(self, request, obj=None):
        """Disable add option."""
        return False
