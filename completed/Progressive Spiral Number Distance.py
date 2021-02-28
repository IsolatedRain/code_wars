# https://www.codewars.com/kata/5a27e3438882f334a10000e3/train/python
def distance(n):
    if n == 1: return 0
    round = 1
    minDist = 0
    while round ** 2 < n:
        round += 2
        minDist += 1
    x = (round - 2) ** 2
    L = x
    for i in range(x, round ** 2 + 1, round - 1):
        if i >= n:
            L = i
            break

    res = list(range(minDist * 2, minDist, -1)) + list(range(minDist, minDist * 2 + 1))
    for i in range(round):
        if L == n: return res[i]
        L -= 1


print(distance(4))
