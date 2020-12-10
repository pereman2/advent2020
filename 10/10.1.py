import math
import re
data = None
with open("input") as f:
    data = f.read()
assert data is not None

data = data.split("\n")
data.remove("")
data = [int(l) for l in data]
data.sort()
data.append(data[len(data)-1] + 3)

sol = {0:1}
for i, jolt in enumerate(data):
    sol[jolt] = 0
    if jolt - 1 in sol:
        sol[jolt]+=sol[jolt-1]
    if jolt - 2 in sol:
        sol[jolt]+=sol[jolt-2]
    if jolt - 3 in sol:
        sol[jolt]+=sol[jolt-3]

    
print(sol[max(data)])
