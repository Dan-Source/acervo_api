from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
    )
    list_display = [
        'username', 'email', 'is_active', 'is_staff', 'date_joined'
    ]
    search_fields = ['username']


admin.site.register(User, UserAdmin)
