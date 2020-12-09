import math
import re
data = None
with open("input") as f:
    data = f.read()
assert data is not None

data = data.split("\n")

inst = {}
acc = 0
pc = 0
while True:
    sentence = data[pc].split(" ")
    if pc not in inst:
        inst[pc] = 1
    else:
        print(acc)
        break
    ins = sentence[0]
    n = int(sentence[1])
    print(ins, n)
    if ins == "acc":
        acc += n
        pc += 1
    elif ins == "jmp":
        pc += n
    else:
        pc += 1
