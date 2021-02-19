def buddy(start, limit):
    def getFactorSum(n: int):
        r = 0
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                r += i + n // i if i != n // i else i
        return r + 1

    for num in range(start, limit):
        a = getFactorSum(num) - 1
        b = getFactorSum(a)
        if b - 1 == num and a > num:
            return [num, a]
    return "Nothing"


# start = 1071625
# limit = 1103735
# start = 48
# limit = 50
# start = 2177
# limit = 4357
start = 310
limit = 2755
res = [1050, 1925]
print(buddy(start, limit))
