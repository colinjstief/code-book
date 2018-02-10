"""
Script: Reproject raster with .prj file
Author: Colin Stief

"""

import os
import subprocess
import gdal

def main():
    """Main script"""
    
    ## Set working directory
    data_directory = os.path.realpath('../maryland/imagery/Ortho_2012')
    os.chdir(data_directory)

    ## Define raster and projection file
    elev = 'BARE_EARTH_2014.TIF'
    source_prj = '7058.prj'
    
    ## gdalwarp
    subprocess.call([
        'gdalwarp',
        '-s_srs', source_prj,           # Source projection; this uses custom .prj file
        '-t_srs', 'EPSG:102285'         # Target projection
        elev,
        'bare_earth_2014_proj.tif'      # Output raster
    ])


if __name__ == '__main__':
    main()

