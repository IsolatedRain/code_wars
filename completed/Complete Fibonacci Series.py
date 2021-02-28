# https://www.codewars.com/kata/5239f06d20eeab9deb00049b/train/python
def fibonacci(n):
    if n <= 0: return []
    if n == 1: return [0]
    res = [0, 1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res


print(fibonacci(10))
