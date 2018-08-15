from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Instance


class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

admin.site.register(Instance, IncidenceAdmin)
