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
    if (password[times[0] - 1] == letter or password[times[1] - 1] == letter) and password[times[0] - 1] != password[times[1] - 1]:
        corr += 1
print(corr)
