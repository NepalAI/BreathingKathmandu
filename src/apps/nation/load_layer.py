import os
from django.contrib.gis.utils import LayerMapping
from .models import Nepal, Conservation


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


# Auto-generated `LayerMapping` dictionary for Conservation model
conservation_mapping = {
    'fid_protec': 'FID_Protec',
    'name': 'Name',
    'type': 'Type',
    'area': 'Area',
    'descriptio': 'Descriptio',
    'sources': 'Sources',
    'issues': 'Issues',
    'remarks': 'Remarks',
    'quality': 'Quality',
    'qltyremark': 'QltyRemark',
    'date_time': 'Date_Time',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

conservation_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Conservation/conservation area.shp'))

def run_conservation(verbose=True):
    lm = LayerMapping(Conservation, conservation_shp, conservation_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True)