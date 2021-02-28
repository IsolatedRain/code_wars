def create_spiral(n):
    if not isinstance(n, int) or n < 1: return
    pos = [[[x, y] for y in range(n)] for x in range(n)]
    digit = iter(range(1, n * n + 1))
    res = [[0] * n for _ in range(n)]
    while pos:
        for r, c in pos[0]:
            res[r][c] = next(digit)
        pos = list(zip(*pos[1:]))
        pos.reverse()
    return res


print(create_spiral(5))
