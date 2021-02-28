import functools


def greatest_product(n):
    s = [[int(_) for _ in x] for x in map(list, n.split("0"))]
    p = lambda x, y: x * y

    def calMaxProduct(arr: list):
        if len(arr) < 5: return 0
        L, R = 0, 5
        maxP = cur = functools.reduce(p, arr[L:R])
        while R < len(arr):
            cur //= arr[L]
            cur *= arr[R]
            L += 1
            R += 1
            if cur > maxP:
                maxP = cur
        return maxP

    return max(map(calMaxProduct, s))


# print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product('2742528206377238217848'))
