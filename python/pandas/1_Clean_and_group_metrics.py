__author__ = 'Colin Stief'

## Merge CSV files
## First written on June 26, 2016

## Import packages (numpy and pandas)
import os, numpy as np, pandas as pd, scipy
#import openpyxl

## Set working directory
#path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\HUC_12_Tables\to_calculate"
path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\Catchment_Tables\to_calculate"
os.chdir( path )

## Set boundary table
#boundary = pd.read_csv( "complete_table_huc.csv" )
boundary = pd.read_csv( "complete_table_catchment.csv" )

## Roll through working directory to add multiple data tables to a single table and then join it with the boundary table
for root, dirs, files in os.walk( path ):
    for name in files:
        if ( name != "complete_table_catchment.csv" ):

            ## Construct full path to data table
            data_table = pd.read_csv( os.path.join(root, name) )

            ## For Zonal Statistic data tables
            if 'MEAN' in data_table.columns:

                ## Grab the only 2 important columns from data table
                #data_table = data_table[ ["HUC12","MEAN"] ]
                data_table = data_table[ ["Value","MEAN"] ]

                ## Rename statistic column
                data_table = data_table.rename(columns={"MEAN": name[:-4]})
                data_table = data_table.rename(columns={"Value": "Unique_ID"})

                ## Join with boundary table
                #boundary = boundary.merge(data_table, how="left", on='HUC12')
                boundary = boundary.merge(data_table, how="left", on='Unique_ID')

            ## For Tabulate Area data tables
            else:

                ## Grab only area columns
                area_metrics = data_table.drop( "OBJECTID", axis=1 )

                ## Rename the columns
                for column in area_metrics.columns:
                    if column != "UNIQUE_ID":
                        area_metrics = area_metrics.rename( columns={column: name[:-4]} )
                    else:
                        area_metrics = area_metrics.rename(columns={"UNIQUE_ID": "Unique_ID"})

                ## Join with boundary table
                #boundary = boundary.merge(area_metrics, how="left", on='HUC12')
                boundary = boundary.merge(area_metrics, how="left", on='Unique_ID')

            print("Finished with " + name)
        
#boundary.to_csv("complete_table_huc_updated.csv", index=False)
boundary.to_csv("complete_table_catchment_updated.csv", index=False)