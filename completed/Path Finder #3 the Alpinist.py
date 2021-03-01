# https://www.codewars.com/kata/576986639772456f6f00030c/python
import heapq


def path_finder(area):
    grid = list(map(list, area.split("\n")))
    row, col = len(grid), len(grid[0])
    for r in range(row):
        for c in range(col):
            grid[r][c] = int(grid[r][c])
    dir4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def neighbor(r, c):
        for m in dir4:
            nr, nc = r + m[0], c + m[1]
            if 0 <= nr < row and 0 <= nc < col:
                yield nr, nc

    dp = [[float("inf")] * col for _ in range(row)]
    dp[0][0] = 0
    visited = [[0] * col for _ in range(row)]
    q = [(0, 0, 0)]
    heapq.heapify(q)
    while q:
        d, r, c = heapq.heappop(q)
        if visited[r][c]: continue
        if r == row - 1 and c == col - 1:
            return dp[-1][-1]
        visited[r][c] = 1
        for nr, nc in neighbor(r, c):
            cur = dp[r][c] + abs(grid[r][c] - grid[nr][nc])
            if cur <= dp[nr][nc]:
                dp[nr][nc] = cur
                heapq.heappush(q, (cur, nr, nc))


e = "\n".join([
    "700000",
    "077770",
    "077770",
    "077770",
    "077770",
    "000007"
])
print(path_finder(e), 14)
