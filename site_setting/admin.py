from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Setting, Adver



@admin.register(Setting)
class SettingAdmin(ModelAdmin):
    pass


@admin.register(Adver)
class AdverAdmin(ModelAdmin):
    pass


