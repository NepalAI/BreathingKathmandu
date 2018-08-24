from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Instance, Nepal, InstanceConservation, Conservation


class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class NepalAdmin(LeafletGeoAdmin):
    list_display = ('dist_id', 'district', 'zone_name', 'region', 'diss', 'xc', 'yc')


class IncidenceConservationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

class ConservationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'descriptio')

admin.site.register(Instance, IncidenceAdmin)
admin.site.register(InstanceConservation, IncidenceConservationAdmin)
admin.site.register(Nepal, NepalAdmin)
admin.site.register(Conservation, ConservationAdmin)
