def min_path(grid, x, y):
    row, col = len(grid), len(grid[0])
    dp = [[0] * col for _ in range(row)]
    dp[0][0] = grid[0][0]
    for r in range(1, y + 1):
        dp[r][0] = dp[r - 1][0] + grid[r][0]
    for c in range(1, x + 1):
        dp[0][c] = dp[0][c - 1] + grid[0][c]
    for r in range(1, y + 1):
        for c in range(1, x + 1):
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

    return dp[y][x]


g = [[1, 2, 3, 6, 2, 8, 1],
     [4, 8, 2, 4, 3, 1, 9],
     [1, 5, 3, 7, 9, 3, 1],
     [4, 9, 2, 1, 6, 9, 5],
     [7, 6, 8, 4, 7, 2, 6],
     [2, 1, 6, 2, 4, 8, 7],
     [8, 4, 3, 9, 2, 5, 8]]
print(min_path(g, 6, 6))
