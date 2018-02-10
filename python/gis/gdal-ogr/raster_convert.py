"""
Script: Get raster info
Author: Colin Stief

"""

## Import libraries
try:
    # Core
    import os
    import sys
    import subprocess

    # User
    import GeoUtils

except ImportError:
    print('Could not import necessary libraries')
    sys.exit()


def main():
    """Main script"""

    ## Get list of shapefiles from data directory
    data_directory = os.path.realpath('../maryland/imagery/Ortho_2012')
    # data_dict = GeoUtils.horde_files(data_directory, ['jp2'])
    data_dict = GeoUtils.horde_files(data_directory, ['tif'])

    ## Loop through list and add to PostGIS
    for name, fullpath in data_dict.items():

        print('Processing ' + fullpath)

        # subprocess.call([
        #     'gdalwarp',
        #     '-s_srs', 'EPSG:2261',        # Source projection; this uses custom .prj file
        #     '-t_srs', 'EPSG:4326',        # Target projection
        #     fullpath,
        #     os.path.join(data_directory, name + '_rprj.tif')      # Output raster
        # ])

        subprocess.call([
            'gdaladdo',
            '-r', 'nearest',
            fullpath,
            '2 4 8 16'
        ])

        # subprocess.call([
        #     'gdal_translate',
        #     '-of', 'GTiff',
        #     '-co', 'TILED=YES',
        #     '-co', 'COMPRESS=NONE',
        #     '-co', 'PHOTOMETRIC=RGB',
        #     fullpath,
        #     os.path.join(data_directory, name + '.tif')
        # ])




## Prevent run on import
if __name__ == '__main__':
    main()
