def getMat(s):
    n = len(s)
    sqrLen = int(n ** 0.5) + 1
    if int(n ** 0.5) ** 2 == n:
        sqrLen -= 1
    matrix = [[0] * sqrLen for _ in range(sqrLen)]
    cnt = 0
    tar = sqrLen ** 2 - 1
    start = 1
    L = 0
    R = sqrLen - 1
    while cnt < tar:
        last = start
        for i in range(L, R, 1):
            matrix[L][i] = start
            start += 4
            cnt += 1
        start = last + 1
        last = start
        for i in range(L, R, 1):
            matrix[i][R] = start
            start += 4
            cnt += 1
        start = last + 1
        last = start
        for i in range(R, L, -1):
            matrix[R][i] = start
            start += 4
            cnt += 1
        start = last + 1
        for i in range(R, L, -1):
            matrix[i][L] = start
            start += 4
            cnt += 1
        start -= 3
        L += 1
        R -= 1
    if L == R:
        matrix[L][R] = sqrLen*sqrLen
    return matrix


def encode(s):
    # your code goes here. you can do it!
    mtx = getMat(s)
    res = ""
    for r in range(len(mtx)):
        for c in range(len(mtx)):
            i = mtx[r][c]
            res += s[i-1] if i <= len(s) else " "
    return res


def decode(s):
    # your code goes here. you can do it!
    mtx = getMat(s)
    n = len(mtx)
    res = [""] * (n * n+1)
    i = 0
    for r in range(n):
        for c in range(n):
            res[mtx[r][c] - 1] = s[i]
            i += 1
            if i >= len(s):
                break
    return "".join(res).strip()


# s = 'Romani ite domum'
s = 'Sic transit gloria mundi'
a = encode(s)
print(a)
b = decode(a)
print(b)
print(s == b)
