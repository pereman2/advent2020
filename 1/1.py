data = None
with open("input1") as f:
    data = f.readlines()
assert data is not None

data = [int(l) for l in data]
res = {}
found = False

for n1 in data:
    for n2 in data:
        x = n1 + n2
        if n2 not in res:
            res[2020 - x] = (n1, n2)
        else:
            print(res[n2][0] * res[n2][1] * n2)
            found = True
            break
    if found:
        break
