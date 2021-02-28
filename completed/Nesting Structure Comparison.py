def same_structure_as(original: list, other: list):
    if not isinstance(other, type(original)): return False

    def check(a, b):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if isinstance(a[i], list):
                if isinstance(b[i], list):
                    if not check(a[i], b[i]):
                        return False
                else:
                    return False
        return True

    return check(original, other)


original = [1, [1, 1]]
other = [2, [2, 2]]
print(same_structure_as(original, other))
