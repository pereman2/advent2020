import copy
data = None
with open("input3") as f:
    data = f.readlines()
assert data is not None
data = [[c for c in l] for l in data]
res = {}
x = 1
y = 3
TREE = '#'
OPEN = '.'

trees = 0
while x < len(data):
    l = copy.copy(data[x])
    l2 = copy.copy(data[x])
    l.pop() # remove trailing \n
    l2.pop()
    if l[y] == TREE:
        trees += 1
    y = (y + 3) % len(l)
    x += 1

print(trees)
