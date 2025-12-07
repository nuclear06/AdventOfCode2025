with open("./input.txt") as f:
    txt = f.readlines()

begin_loc = txt[0].index("S")
lazer = [False for _ in range(len(txt[0]) - 1)]  # exclude \n
lazer[begin_loc] = True

spliter = [l.strip() for l in txt[2::2]]

counter = 0

for sp in spliter:
    for i, loc in enumerate(lazer):
        if loc:
            if sp[i] == "^":
                lazer[i - 1] = lazer[i + 1] = True  # dont exist continuous spliter
                lazer[i] = False
                counter += 1

print(counter)
