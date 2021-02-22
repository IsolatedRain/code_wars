def trouble(x, t):
    n = len(x)
    res = []
    L = x[0]
    for i in range(1, n):
        if x[i] + L != t:
            res.append(L)
            L = x[i]
    res.append(L)
    return res


print(trouble([1, 3, 5, 6, 7, 4, 3], 7))
