def color(testmap):
    mtx = [list(_) for _ in testmap.split("\n") if _]  # regions
    row, col = len(mtx), len(mtx[0])
    colors = [[0] * col for _ in range(row)]  # colorMap
    dir4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for m in mtx:
        print(m)

    def getNeighbors(x, y, curRegion):
        for m in dir4:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited:
                if mtx[nx][ny] != curRegion:
                    neighbors.add(mtx[nx][ny])
                else:
                    visited.add((nx, ny))
                    getNeighbors(nx, ny, curRegion)

    arr = []
    visited = set()
    checked = set()
    for r in range(row):
        for c in range(col):
            if mtx[r][c] not in checked:
                checked.add(mtx[r][c])
                visited = {(r, c)}
                neighbors = set()
                getNeighbors(r, c, mtx[r][c])
                arr.append([mtx[r][c], len(neighbors)])
    arr.sort(key=lambda x: -x[1])
    print(arr)

    # get curRegion coordinates and neighbor's colors
    def dfs(x, y, curRegion):
        for m in dir4:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited:
                visited.add((nx, ny))
                if mtx[nx][ny] != curRegion:
                    if colors[nx][ny]:
                        neighborColors.add(colors[nx][ny])
                else:
                    curRegionCoo.add((nx, ny))
                    dfs(nx, ny, curRegion)

    usedColors = set()
    couldUse = {1, 2, 3, 4}
    for r, c, nei in arr:
        if not colors[r][c]:
            visited = {(r, c)}
            neighborColors = set()
            curRegionCoo = {(r, c)}
            dfs(r, c, mtx[r][c])
            if usedColors - neighborColors:  # choose usedColor first
                curColor = (usedColors - neighborColors).pop()
            else:  # choose a newColor
                curColor = (couldUse - neighborColors).pop()
                usedColors.add(curColor)
            # color the region
            for curR, curC in curRegionCoo:
                colors[curR][curC] = curColor

    return len(usedColors)


# testmap = "ttttB\nyzzuB"
testmap = """
AAAAAA
ABBCCA
ABDECA
ABDDCA
AAAAAA
"""
print(color(testmap))
# testmap = """AAAAAAAAAAAAAAAAAAAA
# ABBBBBBBBBBBBBBBBBBA
# ADDDDDDDDDDDDDDDDDBA
# ADGGGGGGGGGGGGGGGDBA
# ADGFFFFFFFFFFFFFGDBA
# ADGFFFFFFFFFFFFFGDBA
# ADGFFHHHHHHHHHFFGDBA
# ADGEFHHHHHHHHHFFGDBA
# ADGEFHHHHHHHHHFFGDBA
# ADGEFHHHHHHHHHFFGDBA
# ADGEFHHHHHHHHHFFGDBA
# ADGEFHHHHHHHHHFFGDBA
# ADGEFHHHHHHHHHFFGDBA
# ADGEFFHHHHHHHHFFGCBA
# ADGEFFFFFFFFFFFFGCBA
# ADGEFFFFFFFFFFFFGCBA
# ADGEEEEEEEGGGGGGGCBA
# ADGCCCCCCCCCCCCCCCBA
# ADDDDDDDDDDDDDDBBBBA
# AAAAAAAAAAAAAAAAAAAA"""
