MongoDB
=====
### PyMongo
It maintains the connection to the database. 
For example, mongod is a demon that's running mongodb. 
You have python app that includes pymongo module. 
Using this pymongo, you can send requests and receive responses
from mongodb. PyMongo communicates with database using data protocol
with the format of bson.
```python
from pymongo import MongoClient
import pprint

# connect to mongod instance
client = MongoClient('mongodb://localhost:27017/')

tesla_s = {}

# examples database, autos collection
db = client.examples
db.autos.insert(tesla_s)

# all data in autos collection
for a in db.autos.find():
    pprint.pprint(a)
```
Find specific data
```python
# returns all data that contains the query
def find():
    autos = db.autos.find({"manufacturer" : "Toyota"})
```
Multiple Fields Query
```python
def find():
    autos = db.autos.find({"manufacturer" : "Toyota",  "class" : "mid-size car"}) 
```
Projection
```python
# only interested in name
def find():
    autos = db.autos.find({"manufacturer" : "Toyota"})
    projection = {"_id" : 0, "name" : 1}
    autos = db.autos.find(query, projection)
```
### Getting Data into MongoDB
Using mongodb command
```python
db.autos.insert(data)
```
mongo shell: mongoimport
```angular2html
# Putting data into db directly
mongoimport -d examples -c myautos --file autos.json
```
### Operators
- All operators have $
- $gt, $lt, $gte, $lte, $ne

### Exists
```python
use examples
db.cities.find()
db.cities.find({ "governmentType" : { "$exists" : 1 }})
db.cities.find({ "governmentType" : { "$exists" : 1 }}).count()
db.cities.find({ "governmentType" : { "$exists" : 1 }}).pretty()
```
### Regex
```python
db.cities.find({ "governmentType" : { "$regex" : "friendship" }})
db.cities.find({ "governmentType" : { "$regex" : "[Ff]riendship" }})
```

### Scalar
```python

```