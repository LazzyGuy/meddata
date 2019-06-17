import os
import xmltodict
import json


# 16
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open('./all.json', 'r') as fd:
    js = json.load(fd)
    ids = js['IdList']["Id"]
    print(len(ids))

    count = 1
    _dir = 1
    for i in chunks(ids, 5393):
        chunk = {}
        chunk[str(count)] = i

        with open('./data/'+str(_dir)+"/"+str(count)+'.json', 'w') as f:
            f.write(json.dumps(chunk))
        count += 1

        if count > 100 and count < 200:
            _dir = 2

        if count > 200 and count < 300:
            _dir = 3


