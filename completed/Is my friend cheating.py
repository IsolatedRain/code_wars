def remov_nb(n):
    """
    a * b = sum - a - b
    a+ab+b = sum
    a+ab+b+1 = sum+1
    (a+1)*(b+1) = sum + 1
    """
    s = (1 + n) * n // 2 + 1
    res = []

    for i in range(2, int(s ** 0.5) + 1):
        if not s % i:
            if i <= n and s // i <= n:
                res.append((i - 1, s // i - 1))
                res.append((s // i - 1, i - 1))

    return sorted(res)


n = 1000003
print(remov_nb(n))
