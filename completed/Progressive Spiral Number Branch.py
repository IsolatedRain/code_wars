# https://www.codewars.com/kata/5a26ca51e1ce0e987b0000ee/train/python
def branch(n):
    if n == 1: return 0
    r = 1
    # 边长每圈增加 2, 确定在第几圈
    while r ** 2 < n:
        r += 2

    L = (r - 2) ** 2
    res = 3
    # 从最大的开始， 倒着减掉边长-1， 判断在 3， 2， 1， 0.
    for i in range(r ** 2, L, 1 - r):
        if n > i:
            return res + 1
        res -= 1
    return 0


print(branch(6), 0)
