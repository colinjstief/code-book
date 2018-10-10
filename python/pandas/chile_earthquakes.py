###### Data Preprocessing - Chile 2010
###### Colin Stief
###### 9/16/17

import os
import pandas as pd

## Set working directory
path = '/Users/colin/Desktop/github/one-concern/Chile2010'
os.chdir(path)

## Import csv
df = pd.read_csv('Chile2010_Buildings.csv')

## Read column names
for column in df.columns:
    print(column)

## Fields to grab
fieldNames = ['010  Lat. [degrees]', '011  Long. [degrees]', '075  Structural  Failures  or Severe  Damage?', '077  Nonstructural   Element  Failures?', '007  Occupancy', '006  Const.  Date  or  Range', '023  Stories  above  Ground', '025  Total  Floor  Area [m^2]', '037  Vertical  Force-Resisting  System', '038  Lateral  Force-Resisting  System', '039  Foundation  Type', '040  Type of  Partitions']
newFieldNames = ['Lat', 'Long', 'StructuralSevereDamage', 'NonstructuralFailure', 'Occupancy', 'ConstructionDate', 'Stories', 'TotalFloorArea_m2', 'VerticalSystem', 'LateralSystem', 'Foundation', 'Partitions']

## Create dataframe with only fields of interest
df = df[fieldNames]

## Rename fields
df.columns = newFieldNames

## Remove rows with empty lat/long values
df = df[df.Lat.notnull()]
df = df[df.Long.notnull()]

## Remove rows with damage unreported
df = df[df.StructuralSevereDamage != "Not Available"]
df = df[df.NonstructuralFailure  != "Not Available"]

## Check for structural/severe damage and non-structural damage to create a new index
## StructuralSevereDamage == True && NonstructuralFailure == True     -> 3
## StructuralSevereDamage == True && NonstructuralFailure == False    -> 2
## StructuralSevereDamage == False && NonstructuralFailure == True    -> 1
## StructuralSevereDamage == False && NonstructuralFailure == False   -> 0
def calculateDamage(row):
    if row['StructuralSevereDamage'] == 'Yes' and row['NonstructuralFailure'] == 'Yes':
        return 3
    elif row['StructuralSevereDamage'] == 'Yes' and row['NonstructuralFailure'] == 'No':
        return 2
    elif row['StructuralSevereDamage'] == 'No' and row['NonstructuralFailure'] == 'Yes':
        return 1 
    else:
        return 0

df['DamageIndex'] = df.apply(calculateDamage, axis=1)

## Save as separate csv
df.to_csv("Chile2010_subset.csv", index=False)