import functools


def convertFracts(lst):
    def gcd(x, y):
        if x < y:
            x, y = y, x
        if not x % y: return y
        return gcd(x % y, y)

    def lcn(x, y):
        return x * y // gcd(x, y)

    lst = [[i[0] // gcd(i[0], i[1]), i[1] // gcd(i[0], i[1])] for i in lst]
    de = [i[1] for i in lst]
    LCN = functools.reduce(lcn, de)
    res = []
    for N, D in lst:
        k = LCN // D
        res.append([N * k, LCN])
    return res


a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
c = convertFracts(a)
print(b == c)
