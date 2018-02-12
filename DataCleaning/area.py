"""
Using the most siginificant digits to determine a value of all in areaLand column

fix_area() will receive a string as an input, and it
has to return a float representing the value of the area or None.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

"""
In this case, data are user-entered. 
The assumption is that the longest is the more reliable.
"""
def fix_area(area):

    if area[0] == '{':
        first = area.split('|')[0].strip('{')
        last = area.split('|')[1].strip('}')

        longer = first if len(first) > len(last) else last
        #print('Choose {} between {} and {}'.format(longer, first, last))
        try:
            return float(longer)
        except ValueError:
            return area
    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = next(reader)

        # processing file
        for line in reader:
            # calling your function to fix the area value
            #print(line)
            # Note: you can check see if the key is already in dictionary this way
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print("Printing three example results:")
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] == None
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0


if __name__ == "__main__":
    test()