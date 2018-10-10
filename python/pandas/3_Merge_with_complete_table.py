__author__ = 'Colin Stief'

## import packages (numpy and pandas)
import os, numpy as np, pandas as pd, scipy
#import openpyxl

## set path and tables
path = r"\\Ccsvr01\d\GIS\_Web_Services\Regional\NALCC_Restoration_Tool\Tables"
#complete_table = pd.read_csv( os.path.join(path, "complete_table_huc.csv") )
complete_table = pd.read_csv( os.path.join(path, "complete_table_catchment.csv") )
walk_path = os.path.join(path, "to_add")
os.chdir( walk_path )

for root, dirs, files in os.walk( walk_path ):
    for name in files:
        if ( name[name.rfind("."):len(name)] == ".csv" ):
            new_table = pd.read_csv(name)
            #complete_table = complete_table.merge( new_table, how="left", on="HUC12" )
            complete_table = complete_table.merge( new_table, how="left", on="Unique_ID" )

#complete_table.to_csv( "complete_table_huc_updated.csv", index=False )
complete_table.to_csv( "complete_table_catchment_updated.csv", index=False )