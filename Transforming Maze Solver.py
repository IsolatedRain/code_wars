def rotate(n: int, v: str):
    return v[n:] + v[:n]


def couldMove(dir, curCell, neiCell):
    if dir == "N":
        return curCell[0] == "0" and neiCell[2] == '0'
    elif dir == "S":
        return curCell[2] == "0" and neiCell[0] == '0'
    elif dir == "W":
        return curCell[1] == "0" and neiCell[3] == '0'
    else:
        return curCell[3] == "0" and neiCell[1] == '0'


dir4 = {"W": (0, -1), "E": (0, 1), "N": (-1, 0), "S": (1, 0)}


def maze_solver(ar):
    a = [[bin(v)[2:].zfill(4) if v != 'B' and v != 'X' else v for v in row] for row in ar]
    row, col = len(ar), len(ar[0])
    tarR, tarC = None, None
    curR, curC = None, None
    for r in range(row):
        for c in range(col):
            if a[r][c] == "B":
                curR, curC = r, c
                a[r][c] = "0000"
            elif a[r][c] == 'X':
                tarR, tarC = r, c
                a[r][c] = "0000"
    visited = set()
    visited.add((curR, curC))
    paths = ""

    def dfs(curX, curY, n, path):
        nonlocal paths
        if curX == tarR and curY == tarC:
            t = path.replace("  ", " x ").split()
            if len(t) > 5: return False
            paths = t
            return True
        for dir, m in dir4.items():
            nr, nc = curX + m[0], curY + m[1]
            if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited:
                visited.add((nr, nc))
                if couldMove(dir, rotate(n, a[curX][curY]), rotate(n, a[nr][nc])):
                    if dfs(nr, nc, n, path + dir):
                        return True
                else:
                    tmpPath = path
                    for i in range(1, 4):
                        if couldMove(dir, rotate((i + n) % 4, a[curX][curY]), rotate((i + n) % 4, a[nr][nc])):
                            tmpPath += " " * i
                            if dfs(nr, nc, (i + n) % 4, tmpPath + dir):
                                return True
                            break
                visited.discard((nr, nc))
        return False

    dfs(curR, curC, 0, "")
    return [i if i != 'x' else "" for i in paths]


# arr = [[4, 2, 5, 4],
#        [4, 15, 11, 1],
#        ['B', 9, 6, 8],
#        [12, 7, 7, 'X']]
arr = (
    (6, 3, 10, 4, 11),
    (8, 10, 4, 8, 5),
    ('B', 14, 11, 3, 'X'),
    (15, 3, 4, 14, 15),
    (14, 7, 15, 5, 5)
)
print(maze_solver(arr))
