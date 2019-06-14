import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree
import csv

# Get linkes from html
#---------------------------------------------
# html_doc = open('./top100.html', 'r').read()
# soup = beautifulsoup(html_doc, 'html.parser')

# content = soup.find("div", {"class": "content"})

# all_div = content.findAll("div", {"class": "rprt"})


# link_file = open('./data/top100links.txt', 'w')

# for item in all_div:
    # link = item.find("a")
    # link_file.write(link.get('href'))
    # link_file.write("\n")
#-----------------------------------------------


# fetch data form ind link
#-----------------------------------------------

prefix_link = "https://www.ncbi.nlm.nih.gov"

target_links = []
with open('./data/top100links.txt') as link_file:
    for link in link_file.readlines():
        target_link = prefix_link + link.replace('\n', '') + '?report=xml&format=text'
        target_links.append(target_link)

for i, t in enumerate(target_links):
    req = requests.get(t)
    content = req.text

    soup = BeautifulSoup(content, 'html.parser')
    txt = soup.find('pre').text

    _file = open('./data/top100data/'+str(i)+'.xml', '+w')

    _file.write(txt)
    print('Done with '+str(i)+' file')








