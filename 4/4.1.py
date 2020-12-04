import copy
data = None
with open("input4") as f:
    data = f.readlines()
assert data is not None

def get_keys(l):
    s = l.split(" ")
    keys = []
    for v in s:
        kv = v.split(":")
        key = kv[0]
        keys.append(key)

    return keys

fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt", "cid"]
fields_within = []
valid = 0

for i, line in enumerate(data):
    l = line.strip()
    keys = get_keys(l)
    for k in keys:
        if k in fields:
            fields_within.append(k)
    if len(l) == 0 or i == len(data) - 1:
        if len(fields_within) >= len(fields) - 1:
            if len(fields_within) == len(fields) - 1 and "cid" in fields_within:
                pass
            else:
                valid += 1

        fields_within = []
print(valid)
