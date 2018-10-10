__author__ = 'Colin Stief'

## import packages (numpy and pandas)
import os, numpy as np, pandas as pd, scipy, openpyxl

## set path and tables
path = r"\\Ccsvr01\d\GIS\_Web_Services\Regional\NALCC_Restoration_Tool\Tables\to_add"
os.chdir( path )

#table = pd.read_csv( "complete_table_huc_updated.csv" )
table = pd.read_csv( "complete_table_catchment_updated.csv" )
table.fillna(0, inplace=True)
#table.to_csv( "complete_table_huc_updated_no_zeroes.csv", index=False )
table.to_csv( "complete_table_catchment_updated_no_zeroes.csv", index=False )