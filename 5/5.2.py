import math
data = None
with open("input5") as f:
    data = f.readlines()
assert data is not None

for i, line in enumerate(data):
    data[i] = line.strip("\n")
    
UPPER = ["B", "R"]
LOWER = ["F", "L"]

# my_id = some_id - 1 or some_id + 1
best = -1
res = {}
ids = []
for line in data:
    id_ = -1
    min_ = 0
    max_ = 127
    for c in line[:7]:
        if c in UPPER:
            min_ = int(math.ceil((max_ + min_) / 2))
        else:
            max_ = int((max_ + min_) / 2)
    row = min(min_, max_)
    min_ = 0
    max_ = 7
    for c in line[7:]:
        if c in UPPER:
            min_ = int(math.ceil((max_ + min_) / 2))
        else:
            max_ = int((max_ + min_) / 2)
    col = max(min_, max_)
    id_ = (row * 8) + col
    ids.append(id_)
    best = max(best, id_)
    if id_+1 not in res:
        res[id_+1] = 1
    else:
        res[id_+1] += 1
    if id_-1 not in res:
        res[id_-1] = 1
    else:
        res[id_-1] += 1

ids = sorted(ids)
for i, id_ in enumerate(ids):
    if id_ + 1 < len(ids) and id_ + 1 != ids[i+1]:
        if id_+2 in ids:
            print(id_+1)
    if id_ - 1 > -1 and id_ - 1 != ids[i-1]:
        if id_-2 in ids:
            print(id_-1)

