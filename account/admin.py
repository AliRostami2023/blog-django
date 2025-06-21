from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
    search_fields = ['full_name', 'email']


admin.site.unregister(Group)
