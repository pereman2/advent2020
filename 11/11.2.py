import copy
with open("input") as f:
    data = f.read()

xd = data.split("\n")
data = []
for i, line in enumerate(xd):
    if len(line):
        data.append([])
        for j, c in enumerate(line):
            data[i].append(c)

def try_add(data, i, j, dx, dy):
    try:
        i += dx
        j += dy
        if i < 0 or j < 0:
            return None
        while data[i][j] == ".":
            i += dx
            j += dy
            if i < 0 or j < 0:
                return None
        return data[i][j]
    except:
        return None

def get_adjacent(data, i, j):
    ad = []
    ad.append(try_add(data, i, j, 0, - 1))
    ad.append(try_add(data, i, j, 0, + 1))
    ad.append(try_add(data, i, j, -1, 0))
    ad.append(try_add(data, i, j, 1, 0))
    ad.append(try_add(data, i, j, -1, -1))
    ad.append(try_add(data, i, j, -1, 1))
    ad.append(try_add(data, i, j, 1, -1))
    ad.append(try_add(data, i, j, 1, 1))
    return ad


def c(data):
    d = []
    changed = False
    for i, line in enumerate(data):
        d.append([])
        for j, c in enumerate(line):
            adjacents = get_adjacent(data, i, j)
            if c == "L" and adjacents.count("#") == 0:
                d[i].append("#")
                changed = True
            elif c == "#" and adjacents.count("#") >= 5:
                d[i].append("L")
                changed = True
            else:
                d[i].append(data[i][j])
    return d, changed

changed = True
while changed:
    data, changed = c(data)
res = 0
for line in data:
    for c in line:
        if c == "#":
            res += 1
print(res)
