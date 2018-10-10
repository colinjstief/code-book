"""
Class: Utility functions for geospatial tasks
Author: Colin Stief

"""


def csv_to_geojson(file, geometry_type):
    """
    Convert a csv file to a geojson object
    """

    features = []

    if geometry_type == "point":
        return "Not implemented yet"
    elif geometry_type == "polyline":

        return "polyline here is re"
    elif geometry_type == "polygon":
        return "Not implemented yet"
    else:
        return "Geometry type not recognized"
