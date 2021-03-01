# https://www.codewars.com/kata/5765870e190b1472ec0022a2
def path_finder(maze):
    maze = list(map(list, maze.split("\n")))
    dir4 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    row, col = len(maze), len(maze[0])

    def neighbor(r, c):
        for m in dir4:
            nr, nc = r + m[0], c + m[1]
            if 0 <= nr < row and 0 <= nc < col:
                yield nr, nc

    visited = {(0, 0)}

    def dfs(r, c):
        if r == row - 1 and c == col - 1:
            return True
        for nr, nc in neighbor(r, c):
            if (nr, nc) not in visited and maze[nr][nc] != "W":
                visited.add((nr, nc))
                if dfs(nr, nc):
                    return True
        return False

    return dfs(0, 0)


d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])
print(path_finder(d), False)
