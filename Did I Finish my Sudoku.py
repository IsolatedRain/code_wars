def done_or_not(board):  # board[i][j]
    def check(x):
        mask = 0
        tar = (1 << 9) - 1
        tar <<= 1
        for i in x:
            if mask & (1 << i):
                return False
            mask |= (1 << i)
        return mask == tar

    for r in range(9):
        if not check(board[r]):
            return "Try again!"

    for r in zip(*board):
        if not check(r):
            return "Try again!"

    leftTop = [[r, c] for r in [0, 3, 6] for c in [0, 3, 6]]
    for p in leftTop:
        grid = []
        for r in range(p[0], p[0] + 3):
            for c in range(p[1], p[1] + 3):
                grid.append(board[r][c])
        if not check(grid):
            return "Try again!"

    return "Finished"


board = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
         [4, 9, 8, 2, 6, 1, 3, 7, 5],
         [7, 5, 6, 3, 8, 4, 2, 1, 9],
         [6, 4, 3, 1, 5, 8, 7, 9, 2],
         [5, 2, 1, 7, 9, 3, 8, 4, 6],
         [9, 8, 7, 4, 2, 6, 5, 3, 1],
         [2, 1, 4, 9, 3, 5, 6, 8, 7],
         [3, 6, 5, 8, 1, 7, 9, 2, 4],
         [8, 7, 9, 6, 4, 2, 1, 5, 3]]
print(done_or_not(board))
