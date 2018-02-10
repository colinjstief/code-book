"""
Script: Batch import shapefiles with ogr2ogr
Author: Colin Stief

"""

## Import libraries
try:
    # Core
    import os
    import sys
    import subprocess

    # User
    import Config
    import GeoUtils

    # Third
    # import ogr

except ImportError:
    print('Could not import necessary libraries')
    sys.exit()


def main():
    """Main script"""

    ## Get list of shapefiles from data directory
    data_directory = os.path.realpath('../washingtondc/development')
    shapefile_dict = GeoUtils.horde_files(data_directory, ['shp'])

    ## Get driver
    # driver = ogr.GetDriverByName('ESRI Shapefile')

    ## Loop through list and add to PostGIS
    for name, path in shapefile_dict.items():

        print('Processing ' + name)
        if name != 'buildingfootprints':
            process_shapefile_ogr2ogr(name, path)

def process_shapefile_ogr2ogr(name, path):
    """Import shapefile to PostGIS table using ogr2ogr GDAL command"""

    # dataset = driver.Open(path)
    # layer = dataset.GetLayer(0)
    # layer_name = layer.GetName()

    connection_parameters = 'PG:' + get_connection_parameters()

    # if layer_name== 'Neighborhood_Clusters':
    #     sql = """
    #         SELECT ST_UNION(geometry), TYPE from %s GROUP BY TYPE;
    #     """ % layer_name
    # else:
    #     sql = "SELECT * FROM %s" % layer_name

    subprocess.call([
        'ogr2ogr',
        '-f', 'PostgreSQL', 
        connection_parameters,              # file type; connection; schema.table
        '-lco', 'SCHEMA=washingtondc',      # layer option; schema for import
        '-lco', 'GEOMETRY_NAME=geom',       # layer option; name of geom
        '-nln', name,                       # name of new layer
        # '-nlt', 'PROMOTE_TO_MULTI',         # handle multipolygons
        '-t_srs', 'EPSG:4326',              # output spatial reference
        path,                               # shapefile path
        '-dialect', 'sqlite'                # sql dialect to use geographic functions
        # '-sql', sql                         # sql statements
    ])

def get_connection_parameters():
    """Return the PostgreSQL database parameters"""

    return """
        host='localhost'
        dbname='GeospatialData'
        user='duncanrager'
        password='%s'
    """ % Config.PGSQL_PASSWORD


## Prevent run on import
if __name__ == '__main__':
    main()
