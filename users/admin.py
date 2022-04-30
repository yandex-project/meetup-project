from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import User


class UserAdmin(DjUserAdmin):
    fieldsets = (
        ('Конфиденциальная информация', {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'avatar', 'description')}),
        ('Разрешения', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)
    list_display = ['first_name', 'last_name', 'email']
    list_display_links = ('first_name', 'last_name', 'email')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
