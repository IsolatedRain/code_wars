import collections


def shallowest_path(river):
    row, col = len(river), len(river[0])
    p = list(range(row * col + 2))

    def getRoot(x: int):
        if p[x] != p[p[x]]:
            p[x] = getRoot(p[x])
        return p[x]

    def union(x: int, y: int):
        xRoot, yRoot = getRoot(x), getRoot(y)
        if xRoot > yRoot:
            p[xRoot] = yRoot
        else:
            p[yRoot] = xRoot

    def neighbor(x: int, y: int):
        for m in dir8:
            nr, nc = x + m[0], y + m[1]
            if 0 <= nr < row and 0 <= nc < col:
                yield nr * col + nc

    L = row * col
    R = row * col + 1
    for r in range(row):
        union(L, r * col)
        union(R, r * col + col - 1)
    pos = []
    for r in range(row):
        for c in range(col):
            pos.append([r, c, river[r][c]])
    pos.sort(key=lambda x: x[2])

    dir8 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    visited = set()
    depth = -1
    # get the shallowest depth
    for r, c, v in pos:
        cur = r * col + c
        if cur in visited:
            continue
        visited.add(cur)
        depth = max(depth, v)
        for nei in neighbor(r, c):
            if nei in visited:
                union(cur, nei)
        if getRoot(L) == getRoot(R):
            break

    # start from left side where <= depth
    grid = [[row * col] * col for _ in range(row)]
    q = collections.deque()
    for r in range(row):
        if river[r][0] <= depth:
            grid[r][0] = 0
            q.append([r, 0, [r * col + 0]])

    res = []
    while q:
        r, c, path = q.popleft()
        if c == col - 1:
            res.append(path)
            continue
        for nei in neighbor(r, c):
            nr, nc = nei // col, nei % col
            if river[nr][nc] <= depth and grid[nr][nc] > grid[r][c] + 1:
                grid[nr][nc] = grid[r][c] + 1
                q.append([nr, nc, path + [nei]])
    res.sort(key=len)
    return [[i // col, i % col] for i in res[0]] if res else []


river = [
    [1, 8, 8],
    [8, 1, 8],
    [8, 1, 8],
    [8, 1, 8],
    [8, 1, 8],
    [8, 8, 1],
    [8, 1, 8],
    [8, 1, 1],
    [1, 8, 8]]
# river = [[1, 8],
#          [8, 8],
#          [8, 8],
#          [8, 1],
#          [8, 8],
#          [8, 8],
#          [1, 8],
#          [8, 1],
#          [8, 8]]
# river = [
#     [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#     [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#     [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#     [8, 8, 1, 1, 1, 1, 1, 1, 1, 1],
#     [8, 8, 1, 1, 8, 8, 8, 8, 1, 1],
#     [8, 8, 1, 1, 1, 8, 8, 8, 1, 1],
#     [8, 8, 8, 8, 1, 8, 8, 8, 8, 1],
#     [8, 8, 8, 8, 1, 8, 8, 8, 8, 8],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 8],
#     [1, 8, 1, 8, 8, 8, 8, 8, 1, 8],
#     [1, 1, 1, 8, 8, 8, 8, 8, 1, 8],
#     [8, 8, 1, 1, 1, 1, 1, 1, 1, 8]]
print(shallowest_path(river))
