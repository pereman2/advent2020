data = None
with open("input2") as f:
    data = f.readlines()
assert data is not None

res = {}
found = False

corr = 0
for line in data:
    spl = line.split(" ")
    times_spl = spl[0].split("-")
    times = (int(times_spl[0]), int(times_spl[1]))
    letter = spl[1][0]
    password = spl[2]
    count = 0
    for l in password:
        if l == letter:
            count += 1
    if count >= times[0] and count <= times[1]:
        corr += 1
print(corr)
