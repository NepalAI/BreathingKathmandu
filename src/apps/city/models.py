from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gis_models


class Instance(models.Model):
    name = models.CharField(max_length=50)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()
