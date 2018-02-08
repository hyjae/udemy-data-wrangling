
import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"
RELEASE_URL = BASE_URL + "release/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print("requesting " + r.url)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)

def find_exact_name(url, params, name):
    match = []
    results = query_by_name(url, params, name)
    for i in range(len(results["artists"])):
        found_name = results["artists"][i]["name"]
        if found_name == name:
            match.append(results["artists"][i])
    return match

def find_begin_area(url, params, name):
    match = []
    artists = find_exact_name(url, params, name)
    for artist in artists:
        if 'begin-area' in artist:
            match.append(artist['begin-area']['name'])
    return match

def find_disambiguation(url, params, name):
    match = []
    artists = find_exact_name(url, params, name)
    for artist in artists:
        print(artist)
        if 'disambiguation' in artist:
            match.append(artist['disambiguation'])
    return match

def find_form_date(url, params, name):
    match = []
    artists = find_exact_name(url, params, name)
    for artist in artists:
        print(artist)
        if 'life-span' in artist:
            match.append(artist['life-span']['begin'])
    return match

def pretty_print(data, indent=4):
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        print(data)




def main():
    # The num of band named First Aid Kit
    names = find_exact_name(ARTIST_URL, query_type["releases"], "First Aid Kit")
    print(names)
    print(len(names))

    # Begin-area name for Queen?
    areas = find_begin_area(ARTIST_URL, query_type["simple"], "Queen")
    print(areas)

    # Nirvana Disambiguation?
    disam = find_disambiguation(ARTIST_URL, query_type["simple"], "Nirvana")
    print(disam)
    print(len(disam))

    # When was One Direction formed?
    dates = find_form_date(ARTIST_URL, query_type["simple"], "One Direction")
    print(dates)
if __name__ == '__main__':
    main()

