/*
createdb -U postgres DatabaseName
psql -d DatabaseName -U postgres
*/

-- Add an extension
CREATE EXTENSION postgis;

-- Create a table
CREATE TABLE Landmarks 
( id integer NOT NULL,   
name character(30),   
type character(15),    
the_geom geometry,  
CONSTRAINT pk_landmarks_id PRIMARY KEY (id) );

-- Insert with no SRS
INSERT INTO Landmarks (name, type, the_geom) 
VALUES ('Abrams', 'Residence', ST_GeomFromText('POINT(-122.151951 37.426754)'));

-- SRS (Spatial Reference System) --> the projetion and transformation
-- CRS (Coordinate Reference System)
    -- EPSG (European Petroleum Survey Group)
    -- SRID (Spatial Reference Identifier)
  

-- Insert with SRS
INSERT INTO Landmarks (name, type, the_geom) 
VALUES ('Abrams', 'Residence', ST_GeomFromEWKT('SRID=4326;POINT(-122.151951 37.426754)'));

-- Replace old geometry column
SELECT DropGeometryColumn('Landmarks', 'the_geom')
SELECT AddGeometryColumn('Landmarks', 'the_geom', 4326, 'POINT', 2);