import json
from multiprocessing import Pool
from time import time

def f(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

js = json.load(open("./2000.json", 'r'))
one = js['1']
two = js['2']
three = js['3']
four = js['4']

t = time()
for i in [one, two, three, four]:
    print(f(i))

print(time() - t)


