# very inelegent solution
with open("./input.txt") as f:
    txt = f.readlines()

prefix = 12


def maxVoltage(num: str):
    length = len(num)
    dp = [0 for _ in range(length)]
    dp[prefix - 1] = int(num[:prefix])
    for i in range(prefix, length):
        dp[i] = updateDP(dp[i - 1], num[i])
    return dp[length - 1]


def removeChar(string: str, idx: int):
    return string[:idx] + string[idx + 1 :]


def updateDP(previous: int, i: str):
    preMax = str(previous)
    tmp = preMax + i
    candidates = [int(removeChar(tmp, i)) for i in range(len(tmp))]
    return max(candidates)


sum = 0
for num in txt:
    sum += maxVoltage(num.strip())

print(sum)
