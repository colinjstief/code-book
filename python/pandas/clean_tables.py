__author__ = 'Colin Stief'

# merge dataframes
# First written on January 25, 2017

# Import packages (numpy and pandas)
import os
import numpy as np
import pandas as pd
import scipy
#import openpyxl

# Set working directory
path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\HUC_12_Tables\new_tables"
#path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\Catchment_Tables\new_tables"
os.chdir(path)

for root, dirs, files in os.walk(path):
    for name in files:
        if (name != "complete_table_huc.csv"):
            old_table = pd.read_csv(os.path.join(root, name))
            new_table = old_table[["HUC12", "MEAN"]]
            new_table = new_table.rename(columns={"MEAN": name[:-4]})
            new_table.to_csv(os.path.join("output", name), index=False)
