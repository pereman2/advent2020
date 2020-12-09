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
        print(data[i])
        break
    i += 1

