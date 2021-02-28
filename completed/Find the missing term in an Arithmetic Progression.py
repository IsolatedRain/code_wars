# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python
def find_missing(seq):
    n = len(seq)
    diff = (seq[-1] - seq[0]) // n
    for i in range(1, n - 1):
        if seq[i] != seq[i - 1] + diff:
            return seq[i - 1] + diff


# print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
print(find_missing([-1, -4, -7, -10, -13, -16, -19, -25, -28]))
