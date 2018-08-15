from django.contrib import admin
from .models import Instance


class IncidenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

admin.site.register(Instance, IncidenceAdmin)
