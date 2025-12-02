with open("./input.txt") as f:
    txt = f.read()

txt = txt.split(",")


def check(i):
    i = str(i)
    tmp = i
    i += i
    i = i[1:-1]
    return i.find(tmp) != -1


ans = 0
for seq in txt:
    begin, end = seq.split("-")
    begin, end = int(begin), int(end)
    invalids = [i for i in range(begin, end + 1) if check(i)]
    ans += sum(invalids)

print(ans)
