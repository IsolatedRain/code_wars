# https://www.codewars.com/kata/55a5c82cd8e9baa49000004c/train/python
import collections


def divisible_count(x, y, k):
    start, m1 = divmod(x, k)
    if m1: start += 1
    end, m2 = divmod(y, k)
    return end - start + 1


print(divisible_count(6, 11, 2))
