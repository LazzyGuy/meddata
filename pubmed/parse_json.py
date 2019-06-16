import json

with open('2000.json') as json_file:  
    data = json.load(json_file)


for json in data:
    for d in data[json]:
        print(d)
