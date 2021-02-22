def sqInRect(l, w):
    if l == w: return None
    if l < w:
        l, w = w, l
    res = []
    while l != w:
        res.append(w)
        l -= w
        l, w = max(l, w), min(l, w)

    res.append(l)
    return res


l = 37
w = 14
print(sqInRect(l, w))
