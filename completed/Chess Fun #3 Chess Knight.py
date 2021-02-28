# https://www.codewars.com/kata/589433358420bf25950000b6/train/python
def chess_knight(cell):
    row = col = 8
    dir8 = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [1, 2], [1, -2], [2, 1], [2, -1]]
    r = row - int(cell[1])
    c = ord(cell[0]) - ord("a")
    res = 0
    for m in dir8:
        nr, nc = r + m[0], c + m[1]
        if 0 <= nr < row and 0 <= nc < col:
            res += 1
    return res


print(chess_knight("d4"), 8)
