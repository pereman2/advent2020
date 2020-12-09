import math
import re
data = None
with open("input") as f:
    data = f.read()
assert data is not None

data = data.split("\n")
data.remove("")
data = [int(l) for l in data]

pre = 25
i = pre
def find_con(invalid, data):
    ex = invalid
    i = 0
    l = 0
    res = []
    while True:
        ex -= data[i]
        res.append(data[i])
        if ex == 0: return res
        if ex < 0: 
            ex = invalid
            l = l + 1
            i = l
            res = []
        i += 1
while i < len(data):
    valid = False
    for j in range(i-pre, i):
        for k in range(i-pre, i):
            if data[j] + data[k] == data[i]:
                valid = True
                break
        if valid:
            break
    if not valid:
        invalid = data[i]
        res = find_con(invalid, data[0:i])
        break
    i += 1

