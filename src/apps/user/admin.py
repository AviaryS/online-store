from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone", "sex", "is_active", "is_staff")
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'phone',
                'sex',
                'password',
                'is_active',
                'is_staff',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'phone',
                'password1',
                'password2'
            )
        }),
    )


admin.site.unregister(Group)