def spiralize(size):
    spiral = [[0] * size for _ in range(size)]
    pos = [[[x, y] for y in range(size)] for x in range(size)]
    turn = 0
    while len(pos) > 1:
        for r, c in pos[0]:
            spiral[r][c] = 1
        if turn != 2:
            pos = list(zip(*(pos[1:])))[::-1]
        else:
            pos = list(zip(*(pos[1:-1])))[::-1]
            turn = 1
        turn += 1
    return spiral


print(spiralize(10))
