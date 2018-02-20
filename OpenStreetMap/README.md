OpenStreetMap
====
Preprocessiong Project using XML formatted data.
 A goal here is to find all street names, audit, improve, and
 update to database.  


Steps
1. Familiarized yourself with the data
2. Find all tags using iterative parsing(+count them)
3. Find all street names formats
4. Audit and improve street names
5. Preparing data for database

See the file information
```python
less south-korea-latest.osm
ls -l south-korea-latest.osm
```

Basic OSMComponents
- OSM
    - A block of **nodes** containing especially the location in the WGS84 reference system
the **tags** of each node
    - A block of **ways**
the **references** to its nodes for each way
the tags of each way
    - A block of **relations**
the references to its members for each relation
the **tags** of each relation


Data References  
https://wiki.openstreetmap.org/wiki/OSM_XML  
https://download.geofabrik.de/asia/south-korea.html
