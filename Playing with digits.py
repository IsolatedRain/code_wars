def dig_pow(n, p):
    digits = map(int, list(str(n)))
    s = 0
    for num in digits:
        s += num ** p
        p += 1

    if s % n:
        return -1

    return s // n


n = 46288
p = 3
print(dig_pow(n, p))
