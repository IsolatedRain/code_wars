def land_perimeter(arr):
    land = list(map(list, arr))
    row, col = len(land), len(land[0])
    dir4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def neighbor(x, y):
        for m in dir4:
            nx, ny = x + m[0], y + m[1]
            if 0 <= nx < row and 0 <= ny < col:
                yield nx, ny

    perimeter = 0
    for r in range(row):
        for c in range(col):
            if land[r][c] == "X":
                perimeter += 4
                for neiR, neiC in neighbor(r, c):
                    if land[neiR][neiC] == "X":
                        perimeter -= 1

    return F"Total land perimeter: {perimeter}"


print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO",
                      "OXOOXX"]) == "Total land perimeter: 60")
