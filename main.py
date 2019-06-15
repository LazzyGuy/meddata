import requests
from bs4 import BeautifulSoup
import json


API="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%222018%22[PDAT]+:+%223000%22[PDAT]+AND+Journal+Article[ptyp]+AND+hasabstract[text]"

def fetch():
    req = requests.get(API)
    return req.text



print(fetch())
