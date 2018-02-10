## Install GIS packages
conda list
conda create -n gis
source activate gis
conda install -c conda-forge gdal
pip install fiona
conda install -c conda-forge pyproj rtree shapely psycopg2
pip install rasterio
pip install geopandas

## Create SQL script for transforming shapefile to PostgreSQL
shp2pgsql -g the_geom buildings.shp tbl_buildings > buildings.sql