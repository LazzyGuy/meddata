import os
import re
from bs4 import BeautifulSoup

data_dir = "./data/top100data/"
file_path = [ (os.path.join(data_dir, f), int(f[0:-4])) for f in os.listdir(data_dir)] 

for f in file_path[0:1]:
    content = open(f[0], 'r').read()
    soup = BeautifulSoup(content, 'lxml')

    print(soup.prettify(encoding=None, formatter='lxml'))
    # newFile = open(f[0], 'w').read()
