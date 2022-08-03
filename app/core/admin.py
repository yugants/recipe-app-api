"""
Django admin customization
"""
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _    # To create data at user_page in admin

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages here."""
    ordering = ['id']
    list_display= ['email', 'name']
    """We need to overwrite fields of
    default User model like username, last_name
    etc. otherwise it will show error in admin panel.
    Below we are overwriting these fields:"""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    '''Below lines are added to display fields in
    the user creation page.'''
    add_fieldsets = (
        (None, {
            'classes': ('wide',), # Its CSS optional
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

admin.site.register(models.User, UserAdmin)
