from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Instance, Nepal


class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class NepalAdmin(LeafletGeoAdmin):
    list_display = ('district', 'region')


admin.site.register(Instance, IncidenceAdmin)
admin.site.register(Nepal, NepalAdmin)
