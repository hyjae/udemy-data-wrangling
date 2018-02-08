"""
- using codecs module to write unicode files
- using authentication with web APIs
- using offset when accessing web APIs
"""

import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_ARTICLE = URL_MAIN + "search/v2/articlesearch.json"
API_KEY = {"search": "7c2629b351f2438c872e95bb9a7ccfb4"}
result = []


def get_from_file(name, period):
    filename = "search-{0}-{1}.json".format(name, period)
    with open(filename, "r") as f:
        return json.loads(f.read())



def pretty_print(data, indent=4):
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        print(data)


def query_site(url, params, page):
    # page 0 corresponds to records 0-9
    if API_KEY["search"] == "":
        print("You need to register for NYTimes Developer account to run this program.")
        return False

    params.update({"api-key": API_KEY["search"], "page": page})
    r = requests.get(url, params=params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


# Find how many articles mentioned the word in period in snippets.
# More than one word in one article are counted as one
# fmt: yyyymmdd offset: num of records you want to search
def get_freq(url, word, offset, begin, end):
    freq = dict()
    search_count = 0
    params = {"begin_date": begin, "end_date": end}
    pages = offset // 10

    for page in range(pages):
        results = get_data(url, page, begin, end)
        for doc in results['response']['docs']:
            search_count = search_count+1
            if word in doc['snippet']:
                date = doc['pub_date'].split('T')[0]
                if date in freq:
                    freq[date] = freq[date]+1
                else:
                    freq[date] = 1

    return search_count, freq


def get_data(url, page, begin, end):
    params = {"begin_date": begin, "end_date": end}
    return query_site(url, params, page)


# offset: the num of records
def save_file(url, offset, name, begin="20180101", end="20180201"):
    # This will process all results, by calling the API repeatedly with supplied offset value,
    # combine the data and then write all results in a file.
    count = 0
    pages = offset // 10
    period = begin+end

    full_data = []
    with codecs.open("article-{0}-{1}.json".format(name, period), encoding='utf-8', mode='w') as v:
        for page in range(pages):
            datum = get_data(url, page, begin, end)
            full_data.append(datum)

        v.write(json.dumps(full_data, indent=2))


def test():
    search_count, freq = get_freq(URL_ARTICLE, "the", 200, "20160202", "20180103")
    print("The number of searched articles:", search_count)
    print(freq)
    save_file(URL_ARTICLE, 20, "search")


if __name__ == "__main__":
    test()