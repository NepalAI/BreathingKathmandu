import os
from django.contrib.gis.utils import LayerMapping
from .models import Nepal


# Auto-generated `LayerMapping` dictionary for Nepal model
nepal_mapping = {
    'dist_id': 'DIST_ID',
    'district': 'DISTRICT',
    'zone_name': 'ZONE_NAME',
    'region': 'REGION',
    'diss': 'DISS',
    'xc': 'Xc',
    'yc': 'Yc',
    'geom': 'MULTIPOLYGON',
}

nepal_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Nepal/NP_75DWGS84.shp'))

def run(verbose=True):
    lm = LayerMapping(Nepal, nepal_shp, nepal_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True)
