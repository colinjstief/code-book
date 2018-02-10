"""
Script: python subprocess snippets for GDAL commands
Author: Colin Stief

"""

import subprocess
import Config


## ogr2ogr
subprocess.call([
    'ogrinfo',
    '-al',                              # list all features of all layers (used instead of having to give layer names as arguments)
    '-so',                              # summary Only: suppress listing of features, show only the summary information like projection, schema, feature count and extents.
    '/user/dir/file'                    # dataset path
])

## shp2pgsql
PG_SQL = subprocess.check_output([
    'shp2pgsql',
    '-I',                               # create spatial index
    '-s', '4326',                       # spatial reference, WGS 84
    '/user/dir/file',                   # shapefile path
    'awesome_data.table'                # schema.table
])

## ogr2ogr

def get_connection_parameters():
    """Return the PostgreSQL database parameters"""

    return """
        host='localhost'
        dbname='GeospatialData'
        user='duncanrager'
        password='%s'
    """ % Config.PGSQL_PASSWORD

connection_parameters = 'PG:' + get_connection_parameters()

subprocess.call([
    'ogr2ogr',
    '-f', 'PostgreSQL', 
    connection_parameters,              # file type; connection; schema.table
    '-lco', 'SCHEMA=washingtondc',      # layer option; schema for import
    '-nln', 'streets',                  # name of new layer
    '-t_srs', 'EPSG:4326',              # output spatial reference
    '/user/dir/street.shp',             # shapefile path
])

## raster2pgsql (bash command)
# raster2pgsql -R /Users/duncanrager/Desktop/GeospatialData/washingtondc/elevation/BARE_EARTH_2014/bare_earth_2014.tif washingtondc.bareearth2014 > raster.sql
# psql -U duncanrager -d GeospatialData -f raster.sql