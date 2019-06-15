import json
import csv
import requests
from bs4 import BeautifulSoup

js = json.load(open("./2000.json", 'r'))
ids = js['IdList']


def get_url(id):
    return "https://www.ncbi.nlm.nih.gov/pubmed/"+id+"?report=xml&format=text"

urls = [ get_url(id) for id in ids ]

get
TITLE= "Page number,Email,Author Name,Author affiliation,Co-author 1 Name,Co-author 1 Affiliation,Co-author 1 Email,Co-author 2 Name,Co-author 2 Affiliation,Co-author 2 Email,Article 1 Title,Article 1 URL,Article 1 Journal,Article 1 Pub Date,Article 1 Abstract,Article 2 Title,Article 2 URL,Article 2 Journal,Article 2 Pub Date,Article 2 Abstract,Article 3 URL,Article 3 Journal,Article 3 Pub Date,Article 3 Abstract,Article 4 Title,Article 4 URL,Article 4 Journal,Article 4 Pub Date,Article 4 Abstract,Article 5 URL,Article 5 Journal,Article 5 Pub Date,Article 5 Abstract,Article 6 Title,Article 6 URL,Article 6 Journal,Article 6 Pub Date,Article 6 Abstract,Article 7 URL,Article 7 Journal,Article 7 Pub Date,Article 7 Abstract,Article 8 Title,Article 8 URL,Article 8 Journal,Article 8 Pub Date,Article 8 Abstract,Article 9 URL,Article 9 Journal,Article 9 Pub Date,Article 9 Abstract,Article 10 Title,Article 10 URL,Article 10 Journal,Article 10 Pub Date,Article 10 Abstract"
def convert_data(soup_list):
    print("Converting..")

    # authorlist -> author[] -> lastname -> forename


COUNT = 0
BATCH=2
xml_soup_list = []

for url in urls[0:10]:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    xml = soup.find('pre').text
    soupxml = BeautifulSoup(xml, 'lxml')

    COUNT += 1
    xml_soup_list.append(soupxml)

    if count == BATCH:
        convert_data(xml_soup_list)
        xml_soup_list = []
        COUNT = 0

