__author__ = 'Colin Stief'

## split table
## First written on January 25, 2017

## Import packages (numpy and pandas)
import os, numpy as np, pandas as pd, scipy
#import openpyxl

## Set working directory
#path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\HUC_12_Tables\brand_new_tables"
path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\Catchment_Tables\brand_new_tables"
os.chdir( path )

## Set boundary table
#metrics = pd.read_csv( "complete_table_huc.csv" )
metrics = pd.read_csv( "complete_table_catchment.csv" )

for column in metrics.columns:
    new_table = metrics[["Unique_ID", column]]
    new_table.to_csv(column + ".csv", index=False)

print "Script done."