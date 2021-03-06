# https://www.codewars.com/kata/591eab1d192fe0435e000014/train/python
def escape(p):
    row, col = len(p), len(p[0])
    carPos, staircases, stairPos = [], [], []
    for r in range(row):
        for c in range(col):
            if p[r][c] == 2:
                carPos = [r, c]
            elif p[r][c] == 1:
                stairPos = [r, c]
        if carPos and stairPos:
            staircases.append(stairPos)
        stairPos = []

    res = []
    for stairPos in staircases:
        if stairPos == carPos:
            res[-1] = res[-1][0] + str((int(res[-1][1]) + 1))
        else:
            dist = carPos[1] - stairPos[1]
            if dist > 0:
                res.append(F"L{dist}")
            else:
                res.append(F"R{abs(dist)}")
            res.append("D1")
        carPos = [stairPos[0] + 1, stairPos[1]]
    dist = col - 1 - carPos[1]
    if dist:
        res.append(F"R{dist}")
    return res


carPark = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# carPark = [[0, 2, 0, 0, 1],
#            [0, 0, 0, 0, 1],
#            [0, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]]
# result = ["R3", "D3"]
# carPark = [[1, 0, 0, 0, 2],
#            [0, 0, 0, 0, 1],
#            [1, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0]]
# result = ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]
# carPark = [[2, 0, 0, 1, 0],
#            [0, 0, 0, 1, 0],
#            [0, 0, 0, 0, 0]]
# result = ["R3", "D2", "R1"]
print(escape(carPark))
