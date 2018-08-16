from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gis_models


class Instance(models.Model):
    name = models.CharField(max_length=50)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()


from django.contrib.gis.db import models


class Nepal(models.Model):
    dist_id = models.IntegerField()
    district = models.CharField(max_length=18)
    zone_name = models.CharField(max_length=16)
    region = models.CharField(max_length=16)
    diss = models.IntegerField()
    xc = models.FloatField()
    yc = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.district
