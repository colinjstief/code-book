## Import packages (numpy and pandas)
import os, numpy as np, pandas as pd, scipy

path = r"\\CCSVR01\d\GIS\Regional_Conservation_Opportunity_Areas\Analysis\Restoration_Tool\Tables\Catchment_Tables\new_tables"
os.chdir( path )

for root, dirs, files in os.walk( path ):
    for name in files:
        if ( name[name.rfind("."):len(name)] == ".xlsx" ):
            old_xlsx = pd.read_excel( os.path.join(root, name) )
            new_csv = old_xlsx[ ["Unique_ID", "MEAN"] ]
            new_csv = new_csv.rename(columns={"MEAN": name[:-5]})
            new_csv.to_csv(name[:-5] + ".csv" , index=False)
            print "Finished with " + name[:-5]
            

print "Script done"