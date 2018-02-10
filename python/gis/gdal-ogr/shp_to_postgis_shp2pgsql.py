"""
Script: Batch import shapefiles with shp2pgsql
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
    import psycopg2
    import GeoUtils

except ImportError:
    print('Could not import necessary libraries')
    sys.exit()


def main():
    """Main script"""

    ## Get list of shapefiles from data directory
    data_directory = os.path.realpath('../washingtondc/boundaries')
    shapefile_dict = GeoUtils.horde_files(data_directory, ['shp'])

    ## Loop through list and add to PostGIS
    for name, path in shapefile_dict.items():

        print('Processing ' + name)

        ## shp2pgsql
        process_shapefile_shp2pgsql(name, path)


def process_shapefile_shp2pgsql(name, path):
    """Import shapefile to PostGIS table using shp2pgsql GDAL command"""

    ## Get sql statement from shp2pgsql gdal command
    pg_sql = get_pgsql(name, path)

    ## Get database parameters
    connection_parameters = get_connection_parameters()

    ## Connect to database
    with psycopg2.connect(connection_parameters) as connection:
        ## Grab cursor
        with connection.cursor() as cursor:
            ## Execute SQL
            cursor.execute(pg_sql)

def get_pgsql(name, path):
    """Return the SQL statement from shp2pgsql"""

    pg_sql = subprocess.check_output([
        'shp2pgsql',
        '-I',                           # create spatial index
        '-s', '4326',                   # WGS 84
        path,                           # shapefile path
        'washingtondc.' + name          # schema.table
    ])

    return pg_sql

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

