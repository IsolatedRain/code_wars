def padovan(n):
    p1, p2, p3 = 1, 1, 1
    for i in range(4, n + 2):
        p1, p2, p3 = p2, p3, p1 + p2
    return p3


print(padovan(43))
