import os
import xmltodict
import json
import pprint


data_dir = "./data/top100data/"
file_path = [ (os.path.join(data_dir, f), int(f[0:-4])) for f in os.listdir(data_dir)] 

pp = pprint.PrettyPrinter(indent=4)
for f in file_path:
    with open(f[0], 'r') as fd:
        doc = xmltodict.parse(fd.read())
        sv = open('./data/top100Json/'+str(f[1])+'.json', 'w')

        sv.write(json.dumps(doc))

