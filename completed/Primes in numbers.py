import collections


def prime_factors(n):
    res = ""
    fac = 2
    while fac < n + 1:
        count = 0
        while not n % fac:
            count += 1
            n //= fac
        if count:
            if count != 1:
                res += F"({fac}**{count})"
            else:
                res += F"({fac})"
        fac += 1

    return res


# n = 7775460
# n = 2100000000
# n = 223092870
n = 35791357
# r = "(2**2)(3**3)(5)(7)(11**2)(17)"
print(prime_factors(n))

# def prime_factors(n):
#     def isPrime(num: int):
#         for x in range(2, int(num ** 0.5) + 1):
#             if not num % x:
#                 return False
#         return True
#
#     primes = []
#     mark = collections.defaultdict(int)
#     c = collections.defaultdict(int)
#     i = 2
#     while i < n + 2:
#         if not mark[i]:
#             primes.append(i)
#             while not n % i and n > 1:
#                 c[i] += 1
#                 n //= i
#             if n == 1: break
#             if isPrime(n):
#                 c[n] = 1
#                 break
#         for p in primes:
#             if p * i > n: break
#             mark[p * i] = 1
#             if not p % i: break
#         i += 1
#     res = ""
#     for k, v in c.items():
#         if v == 1:
#             res += F'({k})'
#         else:
#             res += F"({k}**{v})"
#     return res
