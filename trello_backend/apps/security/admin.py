from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.security.models import User

# Register your models here.


@admin.register(User)
class UserA(UserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_created', 'bio')
