import math
data = None
with open("input5") as f:
    data = f.readlines()
assert data is not None

for i, line in enumerate(data):
    data[i] = line.strip("\n")
    
UPPER = ["B", "R"]
LOWER = ["F", "L"]

best = -1
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
    best = max(best, id_)

print(best)
