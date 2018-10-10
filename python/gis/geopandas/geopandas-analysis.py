"""
Analyzing geospatial data with GeoPandas
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
    import rasterio
    import rasterio.plot as rioplot
    import rasterstats as rs
    print('Libraries imported')

except ImportError:
    print('Could not import necessary libraries')
    sys.exit()

## Set environments
workingDirectory = 'C:/Users/Duncan/Desktop/OneConcern/tasks/analysis'
outputDirectory = os.path.join(workingDirectory, 'output')
os.chdir(workingDirectory)

## Define data
dataDirectory = 'C:/Users/Duncan/Desktop/OneConcern/data'
dcData = os.path.join(dataDirectory, 'washington')
drains = os.path.join(dcData, 'Storm_Drains.shp')
neighborhoods = os.path.join(dcData, 'Neighborhood_Planning_Areas.shp')
landcover = os.path.join(dcData, 'DC_11001.img')

## Create GeoPandas Dataframe
gpdDrains = gpd.read_file(drains)
gpdNeighborhoods = gpd.read_file(neighborhoods)

## Merge pd
# frames = [df1, df2, df3]
# result = pd.concat(frames)

## Merge gpd
# country_shapes = country_shapes.merge(country_names, on='iso_a3')

## Clip
# country_cores = gpd.overlay(countries, capitals, how='intersection')

## Spatial join ##
neighborhoodJoin = gpd.tools.sjoin(gpdDrains, gpdNeighborhoods, how="inner")
neighborhoodBuildingMean = neighborhoodJoin.dissolve(by='index_right', aggfunc='mean')
neighborhoodBuildingMean.plot(column = 'Buildings', scheme='quantiles', cmap='YlOrRd')

## Open landcover with rasterio
rasterLandcover = rasterio.open(landcover)
rasterLandcover.meta
rioplot.show(rasterLandcover, with_bounds=True)

## Run zonal statistics on neighborhoods
gpdNeighborhoods = gpd.read_file(neighborhoods)
zonalStats = rs.zonal_stats(neighborhoods, landcover, geojson_out=True)


