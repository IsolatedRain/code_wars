# https://www.codewars.com/kata/58a6568827f9546931000027/train/python
def number_of_carries(a, b):
    strA, strB = str(a), str(b)
    n = max(len(strA), len(strB))
    strA = strA.zfill(n)
    strB = strB.zfill(n)
    a = list(map(int, list(strA)))
    b = list(map(int, list(strB)))
    res = 0
    carry = 0
    for i in range(n - 1, -1, -1):
        cur = a[i] + b[i] + carry
        if cur >= 10:
            res += 1
            carry = cur // 10
        else:
            carry = 0
    return res


# print(number_of_carries(9999, 1), 4)
# print(number_of_carries(543, 3456), 0)
a = 5057353
b = 4466658
print(number_of_carries(a, b))
