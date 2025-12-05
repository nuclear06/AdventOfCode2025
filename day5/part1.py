with open("./input.txt") as f:
    txt = f.readlines()
constrain, foods = [], []

mode = False
for line in txt:
    if not mode and line == "\n":
        mode = not mode
        continue
    if not mode:
        constrain.append(list(int(i) for i in line.strip().split("-")))
    else:
        foods.append(int(line.strip()))


def merge_constrain():
    global constrain
    constrain.sort(key=lambda x: x[0])
    tmp_cons = []
    for i in range(1, len(constrain)):
        if constrain[i][0] <= constrain[i - 1][1] + 1:
            constrain[i][0] = constrain[i - 1][0]
            constrain[i][1] = max(constrain[i][1], constrain[i - 1][1])
        else:
            tmp_cons.append(tuple(constrain[i - 1]))
    tmp_cons.append(constrain[-1])
    constrain = tmp_cons


import bisect

merge_constrain()

search_list = list([x[0] for x in constrain])

length = len(constrain)


def check(food):
    idx = bisect.bisect(search_list, food)
    if idx == 0:
        return False
    if food <= constrain[idx - 1][1]:
        return True
    return False


print(sum([check(x) for x in foods]))
