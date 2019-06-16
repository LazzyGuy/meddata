import json
from requests import get  
from bs4 import BeautifulSoup


BASE_URL= "https://www.ncbi.nlm.nih.gov/pubmed/"


with open('2000.json') as json_file:
    data = json.load(json_file)

index=0
for json in data:
    for d in data[json]:
        index+=1
        print(index)
        if index > 1001:
            url = BASE_URL+str(d)
            print(url)
            response = get(url+'?report=xml&format=text')
            html_soup = BeautifulSoup(response.text, 'html.parser')
            with open('/home/shubham/Projects/PyDev/pubmed/xml/'+str(index)+'.xml','w+') as xml_file:
                xml_file.write(html_soup.text)
