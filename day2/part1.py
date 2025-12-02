with open("./input.txt") as f:
    txt = f.read()

txt = txt.split(",")


def check(i):
    i = str(i)
    l = len(i)
    if l % 1:
        return False
    return i[: l // 2] == i[l // 2 :]


ans = 0
for seq in txt:
    begin, end = seq.split("-")
    begin, end = int(begin), int(end)
    invalids = [i for i in range(begin, end + 1) if check(i)]
    ans += sum(invalids)

print(ans)
