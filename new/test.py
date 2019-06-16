import json
from time import time

from multiprocessing import Pool

def f(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum


t = time()
if __name__ == '__main__':
    js = json.load(open("./2000.json", 'r'))
    one = js['1']
    two = js['2']
    three = js['3']
    four = js['4']

    with Pool(4) as p:
        print(p.map(f, [one, two, three, four]))

    print(time() - t)



