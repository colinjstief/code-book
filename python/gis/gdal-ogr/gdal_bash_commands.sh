

## Get gdal version
gdalinfo --version

## Generate overviews
gdaladdo bare_earth_2014_proj.tif 2 4 8 16

## Copy and create tiles
gdal_translate -of GTiff -a_srs EPSG:9001 -co "COMPRESS=NONE" -co "TILED=YES" input.tif output.tif
gdal_translate -of GTiff -a_srs mywkt.prj -co "COMPRESS=LZW" -co "TILED=YES" input.tif output.tif