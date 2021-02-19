import bisect

mark = [1] * (1100001)
primes = []
for i in range(2, 1100001):
    if mark[i]:
        primes.append(i)
    for p in primes:
        if p * i >= 1100001:
            break
        mark[p * i] = 0
        if not i % p: break


def gap(g, m, n):
    idx1 = bisect.bisect_left(primes, m)
    idx2 = bisect.bisect_left(primes, n)
    for i in range(idx1 + 1, idx2):
        if primes[i] - primes[i - 1] == g:
            return [primes[i - 1], primes[i]]
    return


# print(gap(3, 10, 10))
print(gap(4, 100, 110))
# print(gap(2, 5, 11))
