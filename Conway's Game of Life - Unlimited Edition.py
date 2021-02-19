def get_generation(board, generations):
    dir8 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

    def neighbor(x: int, y: int):
        count = 0
        for m in dir8:
            nr, nc = x + m[0], y + m[1]
            if 0 <= nr < row and 0 <= nc < col and abs(board[nr][nc]) == 1:
                count += 1
        return count

    while generations:
        for b in board:
            print(b)
        print("----")
        row = len(board)
        col = len(board[0])
        generations -= 1
        for r in range(row):
            for c in range(col):
                cnt = neighbor(r, c)
                if board[r][c] < 1:
                    if cnt == 3:
                        board[r][c] = 2
                else:
                    if cnt > 3 or cnt < 2:
                        board[r][c] = -1
        for row in board:
            for c in range(len(row)):
                if row[c] < 0:
                    row[c] = 0
                if row[c] > 0:
                    row[c] = 1
    for b in board:
        print(b)

    return board


# cells = [[1, 0, 0],
#          [0, 1, 1],
#          [1, 1, 0]]
# generations = 2
cells = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
generations = 2

print(get_generation(cells, generations))
