import math


def isPP(n):
    L, R = 1, n // 2
    while L < R:
        mid = (L + R) >> 1
        v = mid * mid
        if v == n:
            return [mid, 2]
        elif v > n:
            R = mid
        else:
            L = mid + 1

    for i in range(L, 1, -1):
        p = int(round(math.log(n, i)))
        if math.pow(i, p) == n:
            return [i, p]
    return


arr = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343,
       361, 400, 441, 484]
for num in arr:
    print(isPP(num))
