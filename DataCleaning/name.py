"""
"name" value can be an array (or list in Python terms).
It would make it easier to process and query the data
later if all values for the name are in a Python list, instead of being
just a string separated with special characters, like now.
"""
import codecs
import csv
import pprint

CITIES = 'cities.csv'


def fix_name(name):

    result = []

    if name == 'NULL':
        return name
    if name[0] == '{':
        result = name.split('|')
        for i, row in enumerate(result):
            row = row.strip('{')
            row = row.strip('}')
            result[i] = row
    else:
        result.append(name)

    #print(result)
    return result


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra metadata
        for i in range(3):
            l = next(reader)
        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "name" in line:
                line["name"] = fix_name(line["name"])
            data.append(line)
    return data


def test():
    data = process_file(CITIES)

    print("Printing 20 results:")
    for n in range(20):
        pprint.pprint(data[n]["name"])

    #assert data[14]["name"] == ['Negtemiut', 'Nightmute']
    assert data[9]["name"] == ['Pell City Alabama']
    assert data[3]["name"] == ['Kumhari']

if __name__ == "__main__":
    test()