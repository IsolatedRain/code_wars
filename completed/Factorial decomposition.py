def decomp(n):
    """
    计算 <= n 的所有 质数
    计算 每个质数的贡献
    """
    # 线性筛选 质数
    primes = []
    mark = [0] * (n + 1)
    for i in range(2, n + 1):
        if not mark[i]:
            primes.append(i)
        for p in primes:
            if p * i > n: break
            mark[p * i] = 1
            if not p % i: break

    res = ""
    # 计算每个质数的贡献
    for p in primes:
        x = n
        cur = 0
        while x > 0:
            cur += x // p
            x //= p
            print(x, cur, p)
        res += f"{p}^{cur} * " if cur > 1 else f"{p} * "

    return res[:-3]


print(decomp(5) == "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19")
