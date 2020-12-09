import copy
data = None
with open("input") as f:
    data = f.read()
assert data is not None

data = data.split("\n")

def reset(data):
    acc = 0
    pc = 0
    reps = {}

    while True:
        sentence = data[pc].split(" ")
        ins = sentence[0]
        if len(sentence) > 1:
            n = int(sentence[1])
        else:
            n = 0
        if pc not in reps:
            reps[pc] = 1
        else:
            reps[pc] += 1
            if reps[pc] > 40:
                return -1
        if ins == "acc":
            acc += n
            pc += 1
        elif ins == "jmp":
            pc += n
        else:
            pc += 1
        if pc == len(data):
            break
    return acc

def swap(data, inst):
    for pc, line in enumerate(data):
        sentence = line.split(" ")
        ins = sentence[0]
        if len(sentence) > 1:
            n = int(sentence[1])
        if pc not in inst: 
            if ins == "nop":
                data[pc] = "jmp " + str(n)
            elif ins == "jmp":
                data[pc] = "nop " + str(n)
            inst[pc] = 1
            break
    return data, inst
c = copy.copy(data)
c, inst = swap(c, {})
res = reset(c)
while res == -1:
    c = copy.copy(data)
    c, inst = swap(c, inst)
    res = reset(c)
    print(res)
