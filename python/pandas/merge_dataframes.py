__author__ = 'Colin Stief'

## merge dataframes
## First written on January 25, 2017

## Import packages (numpy and pandas)
import os, numpy as np, pandas as pd, scipy
#import openpyxl

## Set working directory
path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\HUC_12_Tables\new_tables"
#path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\Catchment_Tables\new_tables"
os.chdir( path )

## Set boundary table
boundary = pd.read_csv( "complete_table_huc.csv" )
#boundary = pd.read_csv( "complete_table_catchment.csv" )

tables_to_merge = [boundary]

for root, dirs, files in os.walk( path ):
    for name in files:
        if ( name != "complete_table_huc.csv" ):
            table = pd.read_csv( os.path.join(root, name) )
            tables_to_merge.append( table )

result = tables_to_merge[0]
for table in tables_to_merge[1:]:
    result = result.merge(table, how="left", on='HUC12')

result.to_csv("complete_table_huc_updated.csv", index=False)

print "Script done."