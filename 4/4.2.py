import copy
import re
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
        if len(kv) > 1:
            value = kv[1]
        else:
            value = None
        keys.append((key, value))

    return keys

def check_key(k, v):
    try:
        if k == "byr":
            if len(v) == 4:
                v = int(v)
                if v >= 1920 and v <= 2002:
                    return True
        elif k == "iyr":
            if len(v) == 4:
                v = int(v)
                if v >= 2010 and v <= 2020:
                    return True
        elif k == "eyr":
            if len(v) == 4:
                v = int(v)
                if v >= 2020 and v <= 2030:
                    return True
        elif k == "hgt":
            if "cm" in v:
                v = int(re.findall("\d+", v)[0])
                if v > 149 and v < 194:
                    return True
            elif "in" in v:
                v = int(re.findall("\d+", v)[0])
                if v > 58 and v < 77:
                    return True
        elif k == "hcl":
            if re.match("#[0-9|a-f]{6}", v):
                return True
        elif k == "ecl":
            if v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return True
        elif k == "pid":
            if len(v) == 9 and int(v):
                return True
        elif k == "cid":
            return True
        else:
            return False
    except:
        return False

fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt", "cid"]
fields_within = []
valid = 0

for i, line in enumerate(data):
    l = line.strip()
    keys = get_keys(l)
    for k, v in keys:
        if check_key(k, v):
            fields_within.append(k)
        else:
            continue
    if len(l) == 0 or i == len(data) - 1:
        if len(fields_within) >= len(fields) - 1:
            if len(fields_within) == len(fields) - 1 and "cid" in fields_within:
                pass
            else:
                valid += 1
        fields_within = []
print(valid)
