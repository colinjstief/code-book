"""
Script: Change symbology of layers in a group
Author: Colin Stief

"""
import arcpy

PRJ = arcpy.mp.ArcGISProject("CURRENT")
for map in PRJ.listMaps():
    if map.name == "Layers":
        for lyr in map.listLayers():
            if lyr.isGroupLayer and lyr.name == "Protected":
                for sublyr in lyr.listLayers():
                    print(sublyr.name)
                    sym = sublyr.symbology
                    sym.renderer.symbol.color = {'RGB': [230, 0, 169, 100]}
                    sym.renderer.symbol.outlineColor = {'RGB': [0, 0, 0, 100]}
                    sym.renderer.symbol.size = 0.75
                    sublyr.symbology = sym
