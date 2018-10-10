__author__ = 'Colin Stief'

## import packages (numpy and pandas)
import os, numpy as np, pandas as pd, scipy, openpyxl

## set path and table
path = r"\\Ccsvr01\d\GIS\NALCC\NALCC_Restoration_Tool_Workspace\Tables\HUC_12_Tables\Originals\To_calculate"
os.chdir( path )
table_to_rank = pd.read_csv( "endangered_species.csv" )

for column in table_to_rank.columns:
    if column != "HUC12" and column != "NAME" and column != "HUC8" and column != "STATES":
        rank_name = column + "_rank"
        table_to_rank[rank_name] = table_to_rank[column].rank(method="max", pct=True)
        print("Finished ranking " + column)

table_to_rank.to_csv("endangered_species_rank.csv", index=False)