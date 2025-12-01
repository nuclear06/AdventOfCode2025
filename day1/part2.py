with open("./input") as f:
    txt = f.readlines()

dial = 50
zero_times = 0


def rotate(direct, len):
    global dial, zero_times
    zero_times += len // 100
    len %= 100
    print("dial:", dial, direct, len, "\ttimes:", zero_times)
    pre_dial = dial
    if direct == "L":
        dial -= len
    else:
        dial += len
    if pre_dial and dial <= 0 or dial >= 100:
        zero_times += 1
    dial %= 100


for line in txt:
    line = line.strip()
    direct = line[0]
    line = line[1:]
    rotate(direct, int(line))

print(zero_times)
