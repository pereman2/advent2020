import math
data = None
with open("input") as f:
    data = f.read()
assert data is not None

data = data.split("\n\n")

res = 0
for group in data:
    group_line = group.replace("\n", "")
    letters = []
    for c in group_line:
        if c not in letters:
            letters.append(c)

    res += len(letters)

print(res)
