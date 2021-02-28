# https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python
res = []
for i in range(2, 99):
    for j in range(2, 65):
        v = i ** j
        if sum(map(int, list(str(v)))) == i:
            res.append(v)
res.sort()


def power_sumDigTerm(n):
    return sorted(res)[n - 1]


print(power_sumDigTerm(1))
