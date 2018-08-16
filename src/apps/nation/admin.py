from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Instance, Nepal


class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class NepalAdmin(LeafletGeoAdmin):
    list_display = ('dist_id', 'district', 'zone_name', 'region', 'diss', 'xc', 'yc')


admin.site.register(Instance, IncidenceAdmin)
admin.site.register(Nepal, NepalAdmin)
