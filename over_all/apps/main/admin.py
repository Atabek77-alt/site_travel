from django.contrib import admin
from .models import *

@admin.register(Appeal)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'message',
        'created_at']
    list_filter =['created_at']
    search_fields = ['name',
                     'email']

