with open("./input") as f:
    txt = f.readlines()

dial = 50
zero_times = 0


def rotate(direct, len):
    global dial, zero_times
    if direct == "L":
        dial -= len
    else:
        dial += len
    dial %= 100
    if dial == 0:
        zero_times += 1


for line in txt:
    line = line.strip()
    direct = line[0]
    line = line[1:]
    rotate(direct, int(line))

print(zero_times)
