"""
Exploring geospatial data with GeoPandas
"""

## Import libraries
try:
    import os, sys
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from shapely.geometry import Point
    import pandas as pd
    import geopandas as gpd
    from geopandas import GeoSeries, GeoDataFrame
    print('Libraries imported')

except ImportError:
    print('Could not import necessary libraries')
    sys.exit()

## Define data
dataDirectory = 'C:/Users/Duncan/Desktop/OneConcern/data'
#dcData = os.path.join(dataDirectory, 'washington')
#parcels = os.path.join(dcData, 'Parcel_Lots.shp')

## Set environments
workingDirectory = 'C:/Users/Duncan/Desktop/OneConcern/tasks/analysis'
scratchDirectory = os.path.join(workingDirectory, 'scratch')
outputDirectory = os.path.join(workingDirectory, 'export')
os.chdir(workingDirectory)

## Create GeoPandas Dataframe
# gpdDrains = gpd.read_file(drains)

## Explore data
# gpdDrains.head()
# gpdDrains.crs
# gpdDrains.plot()
# gpdDrains.geom_type
# gpdDrains.geometry.area
# gpdDrains.geometry.bounds