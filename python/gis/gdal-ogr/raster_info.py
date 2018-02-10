"""
Script: Get raster info
Author: Colin Stief

"""

## Import libraries
try:
    # Core
    import os
    import sys

    # User
    import GeoUtils

    # Third
    import gdal
    import osr

except ImportError:
    print('Could not import necessary libraries')
    sys.exit()


def main():
    """Main script"""

    ## Get list of shapefiles from data directory
    data_directory = os.path.realpath('../washingtondc/elevation')
    data_dict = GeoUtils.horde_files(data_directory, ['tif'])

    ## Loop through list and add to PostGIS
    for name, path in data_dict.items():

        print('Processing ' + name)

        gtif = gdal.Open(path)
        print(gtif.GetMetadata())

        ## Projection info
        get_raster_projection(gtif)

        ## Info on all raster bands
        get_raster_band_info(gtif)

def get_raster_projection(raster):
    """Get projection info"""

    prj = raster.GetProjection()
    print(prj)

    srs = osr.SpatialReference(wkt=prj)
    if srs.IsProjected:
        print('Projected...')
        print(srs.GetAttrValue('projcs'))
    print(srs.GetAttrValue('geogcs'))

def get_raster_band_info(raster):
    """Loop through bands of raster and print the statistics"""
    for band in range(raster.RasterCount):
        band += 1
        print("[ GETTING BAND ]: ", band)

        srcband = raster.GetRasterBand(band)
        if srcband is None:
            continue

        stats = srcband.GetStatistics(True, True)
        if stats is None:
            continue

        print("[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
            stats[0], stats[1], stats[2], stats[3]))

        print("[ NO DATA VALUE ] = ", srcband.GetNoDataValue())
        print("[ MIN ] = ", srcband.GetMinimum())
        print("[ MAX ] = ", srcband.GetMaximum())
        print("[ SCALE ] = ", srcband.GetScale())
        print("[ UNIT TYPE ] = ", srcband.GetUnitType())


## Prevent run on import
if __name__ == '__main__':
    main()
