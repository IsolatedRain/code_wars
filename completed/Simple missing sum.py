# https://www.codewars.com/kata/5a941f3a4a6b34edf900006f/train/python
def solve(arr):
    arr.sort()
    curSum = 0
    for v in arr:
        if v > curSum + 1:
            break
        curSum += v

    return curSum + 1


print(solve([4, 2, 7, 3, 1]), 19)
