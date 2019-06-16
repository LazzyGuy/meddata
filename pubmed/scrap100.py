from requests import get
from bs4 import BeautifulSoup

BASE_URL= "https://www.ncbi.nlm.nih.gov"

url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=%222018%22%5BDate+-+Publication%5D+%3A+%223000%22%5BDate+-+Publication%5D)+AND+Journal+Article%5Bptyp%5D+AND+hasabstract%5Btext%5D'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')


link_container = html_soup.find_all('p',class_='title')

for link in link_container:
    href = link.a['href']
    with open('link_100.txt','a') as out:
        out.write( BASE_URL+href + '\n')


