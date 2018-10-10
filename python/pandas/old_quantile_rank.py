
# Create an output JSON object that holds the min/max values
output_min_max = {}
output_min_max["min"] = model_table["percentile_rank"].min()
output_min_max["max"] = model_table["percentile_rank"].max()

# Create an output csv file
output_spreadsheet = os.path.join( output_path_for_files, "Result_spreadsheet.csv" )
model_table.to_csv( output_spreadsheet, index=False )

# Create an output feature layer to show on the web map
# (a) Convert the csv to a geodatabase table
join_table = arcpy.TableToTable_conversion( output_spreadsheet, output_path, "join_table")
# (b) Join the geodatabase table with the complete planning unit feature layer, keeping only the common fields
arcpy.AddJoin_management( geography_layer_var, join_field, join_table, join_field, "KEEP_COMMON" )
# (c) Copy the layer to make the join permanent
output_layer_copy = arcpy.CopyFeatures_management( geography_layer_var, os.path.join( output_path, "Result_layer_copied" ) )
# (d) Make the layer a feature layer
output_layer = arcpy.MakeFeatureLayer_management( output_layer_copy, "in_memory\\Result_layer" )

## Part 2 - Report Generator
template = r"\\Ccsvr01\d\GIS\_Web_Services\Regional\NALCC_Restoration_Tool\NALCC_Restoration_Tool_Report_Template.mxd"
mxd = arcpy.mapping.MapDocument(template)
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
mxd.activeView = df.name

results_symbology = r"\\Ccsvr01\d\GIS\_Web_Services\Regional\NALCC_Restoration_Tool\Results_Symbology.lyr"
arcpy.ApplySymbologyFromLayer_management( "in_memory\\Result_layer", results_symbology)
report_results_layer = arcpy.mapping.Layer( "in_memory\\Result_layer" )
arcpy.mapping.AddLayer(df, report_results_layer)
df.extent = report_results_layer.getExtent()

for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
    if elm.name == 'model_box':
        model_summary = fields_weights["summary"].replace("?line?", r"\n")
        elm.text = model_summary

arcpy.RefreshActiveView()

output_report = os.path.join(output_path_for_files, "Results_report.pdf")
arcpy.mapping.ExportToPDF(mxd, output_report)

# Set outputs
arcpy.SetParameter(5, output_layer)
arcpy.SetParameter(6, output_spreadsheet)
arcpy.SetParameter(7, output_report)
arcpy.SetParameterAsText(8, json.dumps(output_min_max))