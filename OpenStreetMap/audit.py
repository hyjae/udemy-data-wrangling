import re
import xml.etree.cElementTree as ET
import pprint
import codecs
import json
from collections import defaultdict

filename = open("example.osm", "r")


# print all different tags
def find_tags(filename):
    tags = defaultdict(int)
    tagnames = defaultdict(int)

    try:
        for _, elem in ET.iterparse(filename):
            tags[elem.tag] += 1
            if elem.tag == 'tag':
                tagnames[elem.attrib['k']] += 1
    except ET.ParseError:
        pass
    print(tags)
    print(tagnames)



def tag_types(filename):
    result = []
    try:
        for event, elem in ET.iterparse(filename, events=("start",)):
            if elem.tag == 'node':
                names = defaultdict(list)
                for tag in elem.iter('tag'):
                    if tag.attrib['k'].find('name') != -1:
                        names[tag.attrib['k']].append(tag.attrib['v'])
                if len(names) != 0:
                    result.append(names)
    except ET.ParseError:
        pass
    pprint.pprint(result)



def save_node(data, elem):

    data['id'] = elem.attrib['id']

    pos = []
    pos.append(elem.attrib['lat'])
    pos.append(elem.attrib['lon'])
    data['pos'] = pos

    created = dict()
    created['version'] = elem.attrib['version']
    created['changeset'] = elem.attrib['changeset']
    created['timestamp'] = elem.attrib['timestamp']
    created['user'] = elem.attrib['user']
    created['uid'] = elem.attrib['uid']
    data['created'] = created

    return data



def check_kor(name):
    index = name.find('(')
    if index != -1:
        name = re.sub('[0-9a-zA-Z()]+', '', name).strip()
    return name



def check_name(name):
    name = re.sub('[()]+', '', name).strip()
    return name



def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []

    try:
        with codecs.open(file_out, "w") as fo:
            for event, elem in ET.iterparse(filename, events=("start",)):

                nodedata = dict()
                if elem.tag == 'node':
                    nodeinfo = elem

                    names = dict()
                    for tag in elem.iter('tag'):
                        if tag.attrib['k'].find('name') != -1:

                            key = tag.attrib['k']
                            name = tag.attrib['v']

                            if key == 'name':
                                name = check_kor(name)
                                names['name'] = name
                            else:
                                names[key] = check_name(name)
                            nodedata['name'] = names
                            nodedata = save_node(nodedata, nodeinfo)
                            data.append(nodedata)
                            if pretty:
                                    fo.write(json.dumps(nodedata, indent=2)+"\n")
                            else:
                                    fo.write(json.dumps(nodedata) + "\n")
    except ET.ParseError:
        pass
    return data


if __name__ == '__main__':
    find_tags(filename)
    pprint.pprint(tag_types(filename))
    pprint.pprint(process_map('output', True))