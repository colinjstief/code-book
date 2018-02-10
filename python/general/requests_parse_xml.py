"""
Request package snippets
"""

import csv
import xml.etree.ElementTree as ET
import requests

ENDPOINT = 'https://geonode.wfp.org/geoserver/wfs'
QUERY = {
    'service':'wfs',
    'typeName':'geonode:ecu_poi_damageassessment_copernicus_20160422',
    'request':'GetFeature'
}

RESPONSE = requests.request(
    'GET',
    ENDPOINT,
    params=QUERY
)

ROOT = ET.fromstring(RESPONSE.content)

NEWCSV = open('Ecuador2016_copernicus.csv', 'w')
WRITER = csv.writer(NEWCSV)

## Define header
HEADER = ['Lat', 'Long', 'Grading', 'Type', 'Subtype']
WRITER.writerow(HEADER)

## Define namespaces for XML nodes
NAMESPACES = {
    'wfs': 'http://www.opengis.net/wfs/2.0',
    'geonode': 'https://geonode.org/',
    'gml':'http://www.opengis.net/gml/3.2'
}
PRIMARY_NODE = 'geonode:ecu_poi_damageassessment_copernicus_20160422'

## Loop through XML nodes and write a new csv row for each
for node in ROOT.findall('wfs:member', NAMESPACES):

    ## Grab geometry string and split it to create separate lat/long values
    geom = node.find(PRIMARY_NODE, NAMESPACES).find(
        'geonode:the_geom', NAMESPACES
    ).find('gml:Point', NAMESPACES).find('gml:pos', NAMESPACES).text

    LAT_LONG = geom.split()
    LAT = LAT_LONG[0]
    LONG = LAT_LONG[1]

    ## Grab other values
    GRADING = node.find(PRIMARY_NODE, NAMESPACES).find('geonode:grading', NAMESPACES).text
    TYPE_VALUE = node.find(PRIMARY_NODE, NAMESPACES).find('geonode:settl_type', NAMESPACES).text
    SUB_TYPE = node.find(PRIMARY_NODE, NAMESPACES).find('geonode:subtype', NAMESPACES).text

    ROW = [LAT, LONG, GRADING, TYPE_VALUE, SUB_TYPE]
    WRITER.writerow(ROW)

## Close and save csv
NEWCSV.close()
