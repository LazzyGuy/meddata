from requests import get
from bs4 import BeautifulSoup
import xml.dom.minidom
import os


index=0
with open('link_100.txt','r') as links:
    for line in links:
        index+=1
        line = line.strip('\n')
        print(line+'?report=xml&format=text')
        response = get(line+'?report=xml&format=text')
        html_soup = BeautifulSoup(response.text, 'html.parser')
        with open('/home/shubham/Projects/PyDev/pubmed/xml/'+str(index)+'.xml','w+') as xml_file:
            xml_file.write(html_soup.text)
        

