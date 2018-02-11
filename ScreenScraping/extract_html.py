
from bs4 import BeautifulSoup
import requests
import json

html_page = "https://www.transtats.bts.gov/Data_Elements.aspx?Data=2"

def extract_html():
    """
    You get the session data and pass along with the next request to prevent loading errors
    """
    s = requests.Session()

    r = s.get(html_page)
    soup = BeautifulSoup(r.text)
    viewstate_element = soup.find(id="_VIEWSTATE")
    viewstate = viewstate_element["value"]




def extract_data(soup):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(soup, "r") as html:
        option_values = []
        carrier_list = soup.find(id="CarrierList")
        for option in carrier_list.find_all('option'):
            option_values.append(option['value'])

    return option_values



def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                      data={'AirportList': "BOS",
                            'CarrierList': "VX",
                            'Submit': 'Submit',
                            "__EVENTTARGET": "",
                            "__EVENTARGUMENT": "",
                            "__VIEWSTATEGENERATOR": "8E3A4798",
                            "__EVENTVALIDATION": eventvalidation,
                            "__VIEWSTATE": viewstate
                            })

    return r.text


def test():
    soup = BeautifulSoup(open(html_page))
    data = extract_data(soup)
    print(data)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")


test()