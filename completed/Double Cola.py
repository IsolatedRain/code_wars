import itertools


def who_is_next(names, r):
    n = len(names)
    if n >= r: return names[r - 1]
    x = 0
    count = 0
    while x < r:
        x += n
        n *= 2
        count += 1
    return names[((n // 2) - 1 - (x - r)) // 2 ** (count - 1)]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(who_is_next(names, 7230702951), "Penny")
