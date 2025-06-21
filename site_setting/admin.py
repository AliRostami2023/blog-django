from django.contrib import admin
from .models import Setting, Adver



@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    pass


@admin.register(Adver)
class AdverAdmin(admin.ModelAdmin):
    pass


