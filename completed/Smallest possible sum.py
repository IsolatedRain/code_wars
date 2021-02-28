# https://www.codewars.com/kata/52f677797c461daaf7000740/train/python
from math import gcd
from functools import reduce


def solution(a):
    return len(a) * reduce(gcd, a)


arr = [60, 12, 96, 48, 60, 24, 72, 36, 72, 72, 48]
print(solution(arr))
