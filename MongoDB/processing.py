"""
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label'
  field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the
  same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the
  cleanup is up to you, e.g. removing "*" prefixes etc. If there is a singular
  synonym, the value should still be formatted in a list.
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:

[ { 'label': 'Argiope',
    'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
    'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
    'name': 'Argiope',
    'synonym': ["One", "Two"],
    'classification': {
                      'family': 'Orb-weaver spider',
                      'class': 'Arachnid',
                      'phylum': 'Arthropod',
                      'order': 'Spider',
                      'kingdom': 'Animal',
                      'genus': None
                      }
  },
  { 'label': ... , }, ...
]

  * Note that the value associated with the classification key is a dictionary
    with taxonomic labels.
"""
import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}

def remove_par(data):
    if data.find('(') != -1:
        index = data.find('(')
        return data[:index]
    return data


def process_file(filename, fields):
    data = []
    taxnomic_labels = ['family_label', 'class_label', 'phylum_label', 'order_label', 'kingdom_label', 'genus_label']

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        for i in range(3):
            l = next(reader)

        for line in reader:
            diction = dict()
            classification = dict()
            for key, value in line.items():
                if key in fields.keys():
                    new_key = fields[key]

                    if key == 'rdf-schema#label':
                        line[key] = remove_par(line[key]).strip()

                    elif key == 'name':
                        if line[key] == 'NULL' or line[key].isalnum() is False:
                            line[key] = line['rdf-schema#label']
                    if line[key] == 'NULL':
                        line[key] = None
                    else:
                        if line[key].find('/') != -1 and key != 'URI':
                            line[key] = re.sub(r'http://dbpedia.org/resource/', '', line[key]).strip()
                        if key == 'synonym':
                            line[key] = [parse_array(line[key])]
                        else:
                            line[key] = parse_array(line[key])
                    if key in taxnomic_labels:
                        classification[new_key] = line[key]
                    else:
                        diction[new_key] = line[key]

            diction['classification'] = classification
            data.append(diction)
        return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
            v = v.lstrip("{")
            v = v.rstrip("}")
            v_array = v.split("|")
            v_array = [i.strip() for i in v_array]
            return v_array
    return v


def test():
    data = process_file(DATAFILE, FIELDS)
    print("Your first entry:")
    #print(data[0])
    #print(json.dumps(data[0], indent=4))
    pprint.pprint(data[14])
    first_entry = {
        "synonym": None,
        "name": "Argiope",
        "classification": {
            "kingdom": "Animal",
            "family": "Orb-weaver spider",
            "order": "Spider",
            "phylum": "Arthropod",
            "genus": None,
            "class": "Arachnid"
        },
        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
        "label": "Argiope",
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

if __name__ == "__main__":
    test()