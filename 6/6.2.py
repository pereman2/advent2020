import math
data = None
with open("input") as f:
    data = f.read()
assert data is not None

data = data.split("\n\n")

res = 0
for group in data:
    group_line = group.split("\n")
    letters = {}
    num_persons = len(group_line)
    for person_line in group_line:
        for c in person_line:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1

    for k, v in letters.items():
        if v == num_persons:
            res += 1

print(res)
