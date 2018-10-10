###### Data Preprocessing - Ecuador 2016: Copernicus data
###### Colin Stief
###### 9/16/17

import os
import xml.etree.ElementTree as ET
import csv

## Set working directory
path = '/Users/colin/Desktop/github/one-concern/Equador2016'
os.chdir(path)

## Import XML file and use ET to create tree
tree = ET.parse('Ecuador2016_copernicus.xml')
root = tree.getroot()

################## Alternative -- use 'request' package to grab xml ##################
#import requests
#
#url = 'https://geonode.wfp.org/geoserver/wfs'
#querystring = {'service':'wfs', 'typeName':'geonode:ecu_poi_damageassessment_copernicus_20160422','request':'GetFeature'}
#
#response = requests.request('GET', url, params=querystring)
#root = ET.fromstring(response.content)
#####################################################################################

## Create and open new csv file to write to
newCSV = open('Ecuador2016_copernicus.csv', 'w')
writer = csv.writer(newCSV)

## Define header
header = ['Lat', 'Long', 'Grading', 'Type', 'Subtype']
writer.writerow(header)

## Define namespaces for XML nodes
namespaces = {'wfs': 'http://www.opengis.net/wfs/2.0', 'geonode': 'https://geonode.org/', 'gml':'http://www.opengis.net/gml/3.2'}
primaryNode = 'geonode:ecu_poi_damageassessment_copernicus_20160422'

## Loop through XML nodes and write a new csv row for each
for node in root.findall('wfs:member', namespaces):
    
    ## Grab geometry string and split it to create separate lat/long values
    geom = node.find(primaryNode, namespaces).find('geonode:the_geom', namespaces).find('gml:Point', namespaces).find('gml:pos', namespaces).text
    lat_and_long = geom.split()
    lat = lat_and_long[0]
    long = lat_and_long[1]
    
    ## Grab other values
    grading = node.find(primaryNode, namespaces).find('geonode:grading', namespaces).text
    typeValue = node.find(primaryNode, namespaces).find('geonode:settl_type', namespaces).text
    subType = node.find(primaryNode, namespaces).find('geonode:subtype', namespaces).text
    
    row = [lat, long, grading, typeValue, subType]
    writer.writerow(row)

## Close and save csv
newCSV.close()



###### Data Preprocessing - Ecuador 2016: UNOSAT data
###### Colin Stief
###### 9/16/17

import os
import xml.etree.ElementTree as ET
import csv

## Set working directory
path = '/Users/colin/Desktop/github/one-concern/Equador2016'
os.chdir(path)

## Import XML file and use ET to create tree
tree = ET.parse('Ecuador2016_unosat.xml')
root = tree.getroot()

################## Alternative -- use 'request' package to grab xml ##################
#import requests
#import xml.etree.ElementTree as ET
#
#url = 'https://geonode.wfp.org/geoserver/wfs'
#querystring = {'service':'wfs', 'typeName':'geonode:ecu_poi_damageassessment_unosat_20160422','request':'GetFeature'}
#
#response = requests.request('GET', url, params=querystring)
#root = ET.fromstring(response.content)
#
#####################################################################################

## Create and open new csv file to write to
newCSV = open('Ecuador2016_unosat.csv', 'w')
writer = csv.writer(newCSV)

## Define header
header = ['Lat', 'Long', 'Damage']
writer.writerow(header)

## Define namespaces for XML nodes
namespaces = {'wfs': 'http://www.opengis.net/wfs/2.0', 'geonode': 'https://geonode.org/', 'gml':'http://www.opengis.net/gml/3.2'}
primaryNode = 'geonode:ecu_poi_damageassessment_unosat_20160422'

## Loop through XML nodes and write a new csv row for each
for node in root.findall('wfs:member', namespaces):
    
    ## Grab geometry string and split it to create separate lat/long values
    geom = node.find(primaryNode, namespaces).find('geonode:the_geom', namespaces).find('gml:Point', namespaces).find('gml:pos', namespaces).text
    lat_and_long = geom.split()
    lat = lat_and_long[0]
    long = lat_and_long[1]
    
    ## Grab other values
    damage = node.find(primaryNode, namespaces).find('geonode:Main_Damag', namespaces).text
    
    row = [lat, long, damage]
    writer.writerow(row)

## Close and save csv
newCSV.close()

