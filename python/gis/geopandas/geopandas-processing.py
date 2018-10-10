"""
Processing geospatial data with GeoPandas
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
    from random import randint
    print('Libraries imported')

except ImportError:
    print('Could not import necessary libraries')
    sys.exit()

## Set environments
workingDirectory = 'C:/Users/Duncan/Desktop/OneConcern/tasks/processing'
outputDirectory = os.path.join(workingDirectory, 'output')
os.chdir(workingDirectory)

## Define data
dataDirectory = 'C:/Users/Duncan/Desktop/OneConcern/data'
dcData = os.path.join(dataDirectory, 'washington')
drains = os.path.join(dcData, 'Storm_Drains.shp')
drainsCSV = os.path.join(dcData, '_bucket/Storm_Drains.csv')
contoursJSON = os.path.join(dcData, '_bucket/contours.json')

###### CSV TO SHAPEFILE #######
pdDrains = pd.read_csv(drainsCSV)
pdDrains['geometry'] = pdDrains.apply(lambda row: Point(row.X, row.Y), axis=1)
gpdDrains = gpd.GeoDataFrame(pdDrains)
gpdDrains.crs = {'init' :'epsg:4326'}

outputDrainsShapefile = os.path.join(outputDirectory, 'drains.shp')
gpdDrains.to_file(outputDrainsShapefile, 'ESRI Shapefile')

###### GEOJSON TO SHAPEFILE #######
pdContours = gpd.read_file(contoursJSON)
outputContoursShapefile = os.path.join(outputDirectory, 'contours.shp')
pdContours.to_file(outputContoursShapefile, 'ESRI Shapefile')

###### CHANGE PROJECTION #######
gpdDrains = gpd.read_file(drains)
gpdDrains = pdDrains.to_crs(epsg=6703)

###### ADD/EDIT FIELD #######
gpdDrains['RandomNumber'] = gpdDrains.apply(lambda val: randint(0, 9), axis=1)  ## Inline labdma

def classifyNumber(row):
    if row.RandomNumber < 5:
        return 'low'
    else:
        return 'high'

gpdDrains['DamageClass'] = gpdDrains.apply(classifyNumber, axis=1) ## With function


###### DELETE FIELD #######
gpdDrains = gpdDrains[gpdDrains.DamageClass != 'low']

