def flatten(*args):
    if not args: return []
    res = []
    for arg in args:
        if isinstance(arg, list):
            res += flatten(*arg)
        else:
            res.append(arg)
    return res


print(flatten([1, 2], [3, 4, 5], [6, [7], [[8]]]))
