def zeros(n):
    res = 0
    while n:
        res += n // 5
        n //= 5
    return res


print(zeros(30))
