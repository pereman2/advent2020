import math
import re
data = None
with open("input") as f:
    data = f.read()
assert data is not None

data = data.split("\n")

bags = {}
for rule in data:
    rule_split = rule.split("contain")
    if rule_split[0] == "": continue
    l = re.sub("bags|bag|\.", "", rule_split[0]).strip()
    r = re.sub("bags|bag|\.", "", rule_split[1]).strip()
    contain = r.split(", ")
    bags[l] = []
    bags[l] += contain

SHINY = "shiny gold"

def resolve_bag(bag):
    if "no other" in bag: return -1, ""
    n = int(bag.strip()[0])
    b = bag.strip()[1:].strip()
    return n, b

def solve(bag):
    res = 0
    for cbag in bags[bag]:
        n, b = resolve_bag(cbag)
        if "no other" in b: return 0
        if SHINY == b:
            return 1
        if b != "":
            res += solve(b)

    return 1 if res > 0 else 0

res = 0
for bag in bags:
    res += solve(bag)

print(res)
