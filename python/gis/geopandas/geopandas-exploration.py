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

## Set environments
workingDirectory = 'C:/Users/Duncan/Desktop/OneConcern/tasks/exploration'
outputDirectory = os.path.join(workingDirectory, 'output')
os.chdir(workingDirectory)

## Define data
dataDirectory = 'C:/Users/Duncan/Desktop/OneConcern/data'
dcData = os.path.join(dataDirectory, 'washington')
parcels = os.path.join(dcData, 'Parcel_Lots.shp')
drains = os.path.join(dcData, 'Storm_Drains.shp')
neighborhoods = os.path.join(dcData, 'Neighborhood_Planning_Areas.shp')

## Create GeoPandas Dataframe
gpdDrains = gpd.read_file(drains)
gpdNeighborhoods = gpd.read_file(neighborhoods)

###### DESCRIBE DATA #######
gpdNeighborhoods.head()
gpdNeighborhoods.crs
gpdNeighborhoods.geom_type
gpdNeighborhoods.geometry.area
gpdNeighborhoods.geometry.bounds

###### LIST FIELDS #######
for field in gpdNeighborhoods.columns:
    print(field)

###### COUNT FEATURES #######
len(gpdNeighborhoods)


###### FREQUENCY DISTRIBUTION #######
gpdDrains['YEAR_MARKE'].value_counts().plot(kind='bar')


###### BASIC MAP #######
gpdNeighborhoods.plot()

###### MULTIPLE LAYERS #####
base = gpdNeighborhoods.plot(color='white', edgecolor='black')
gpdDrains.plot(ax=base, marker='o', color='red', markersize=5)