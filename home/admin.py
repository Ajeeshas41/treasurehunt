from django.contrib import admin
from home.models import Configuration

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    fields = ('config','value')
    empty_value_display = '-empty-'
