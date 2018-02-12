"""
Observation of types

- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The type() function returns a type object describing the argument given to the
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

"""
Note: A set is unordered collection with no duplicate elements.
Curly braces or set function can be used to create sets.
"""


def check_type(value, isInt):
    if isInt:
        try:
            int(value)
            return True
        except ValueError:
            return False
    else:
        try:
            float(value)
            return True
        except ValueError:
            return False


def audit_file(filename, fields):

    fieldtypes = {}
    for field in fields:
        fieldtypes[field] = set()

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        """
        for i in range(3):
            l = reader.next()
        """
        for i, datum in enumerate(reader):
            if i == 2:
                break

        for datum in reader:
            for key, value in datum.items():
                if key in fields:
                    if value == 'NULL' or value == '':
                        fieldtypes[key].add(type(None))
                    elif value[0] == '{':
                        fieldtypes[key].add(type([]))
                    elif check_type(value, True):
                        fieldtypes[key].add(type(1))
                    elif check_type(value, False):
                        fieldtypes[key].add(type(1.1))
                    else:
                        fieldtypes[key].add(type('str'))

    f.close()
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)
    pprint.pprint(fieldtypes)
    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
