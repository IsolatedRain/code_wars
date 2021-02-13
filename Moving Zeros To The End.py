def move_zeros(array):
    def isZero(x):
        return isinstance(x, bool) or x != 0

    res = list(filter(isZero, array))
    return res + [0] * (len(array) - len(res))


# arr = [0, 1, None, 2, False, 1, 0]
# arr = [1, 2, 1, 0, 1, 0, 3, 0, 1, 0]
arr = [9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(move_zeros(arr))
