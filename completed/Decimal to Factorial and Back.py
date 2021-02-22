import math


def dec_2_fact_string(n):
    print(n)
    d = {i: chr(ord("A") + i - 10) for i in range(10, 36)}
    for i in range(10):
        d[i] = i
    f = [(0, 0)]
    cur = 1
    for i in range(1, n):
        cur *= i
        if cur > n: break
        f.append((cur, i))
        if cur * i >= n:
            break
    f.reverse()
    res = ""

    for i in range(len(f) - 1):
        a, b = divmod(n, f[i][0])
        n = b
        res += str(d[a])
    return res + "0"


def fact_string_2_dec(s):
    print(s)
    d = {chr(ord("A") + i - 10): i for i in range(10, 36)}
    for i in range(10):
        d[str(i)] = i
    res = 0
    s = s[::-1]
    cur = 1
    for i in range(1, len(s)):
        cur *= i
        res += cur * d[s[i]]
    return res


# n = 2982
# n = 792966973116506907019126003630149015400385
# n = 36288000
n = 371993326789901217467999448150835199999999
# n = 463
s = dec_2_fact_string(n)
# s = "4041000"
b = fact_string_2_dec(s)
print(b == n)
