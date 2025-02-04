from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'avatar',
        'age',
        'bio',
        'phone',
        'created_at',
        'city',
        'male',
    ]

@admin.register(Emails)
class EmailAdmin(admin.ModelAdmin):
    list_display = [
        'email'
    ]



