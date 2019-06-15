from bs4 import BeautifulSoup

str = open("./example", 'r').read()
soupxml = BeautifulSoup(str, 'lxml')

auth = soupxml.findAll('author')

for a in auth:
    print(a.find('firstname').text)

