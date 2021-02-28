import functools


def lcm(*args):
    return functools.reduce(LCM, args) if args else 1


def gcd(a, b):
    return b if not a else gcd(b % a, a)


def LCM(a, b):
    return a * b // gcd(a, b)


print(lcm(2, 3, 4))
