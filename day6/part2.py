# tbh, I think it’s unfair to use python or numpy to solve this problem.
with open("./input.txt") as f:
    txt = f.readlines()

nums, operator = txt[:-1], txt[-1]
import numpy as np

nums = np.array(list([c for c in line[-2::-1]] for line in nums)).T
operator = operator[::-1].strip().split()


def list_to_num(_list):
    num = 0
    flag = 0
    for i in _list[::-1]:
        if i == " ":
            continue
        num += 10**flag * int(i)
        flag += 1
    return num


total = 0
sums, tmp = [], []
flag = 0
for n in nums:
    if np.all(n == " "):
        if operator[flag] == "+":
            sums.append(np.sum(tmp))
        else:
            sums.append(np.prod(tmp))
        tmp = []
        flag += 1
    else:
        tmp.append(list_to_num(n))
if operator[flag] == "+":
    sums.append(np.sum(tmp))
else:
    sums.append(np.prod(tmp))
print(np.sum(sums))
