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

    count = 1
    for i in chunks(ids, 101132):
        chunk = {}
        chunk[str(count)] = i
        with open('./data/'+str(count)+'.json', 'w') as f:
            f.write(json.dumps(chunk))

        count += 1

