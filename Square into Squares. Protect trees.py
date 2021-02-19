def decompose(n):
    def cal(curN, lastSqrt):
        if curN == 1:
            if lastSqrt != 1:
                res.append(1)
                return True
            return False
        L = int(curN ** 0.5)
        for sqrt in range(L, 0, -1):
            if sqrt >= lastSqrt:
                continue
            res.append(sqrt)
            if not curN - sqrt ** 2: return True
            if cal(curN - sqrt ** 2, sqrt):
                return True
            res.pop()
        return False

    for i in range(n - 1, 0, -1):
        res = [i]
        if cal(n ** 2 - i ** 2, i):
            return res[::-1]
    return []


n = 5
print(decompose(n))
