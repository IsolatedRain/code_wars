def paint_tiles(costs):
    def getMin2(arr: list):
        fir, sec = None, None
        for i in arr:
            if fir is None:
                fir = i
            elif i <= fir:
                sec = fir
                fir = i
            elif sec is None or i < sec:
                sec = i
        return fir, sec

    row, col = len(costs) + 1, len(costs[0])
    costs = [[0] * col] + costs
    for i in range(1, row):
        fir, sec = getMin2(costs[i - 1])
        for j in range(col):
            if costs[i - 1][j] == fir:
                costs[i][j] += sec
            else:
                costs[i][j] += fir

    return min(costs[-1])


costs = [[2, 10, 4, 1],
         [10, 7, 10, 3],
         [6, 7, 10, 7],
         [9, 7, 6, 10],
         [4, 2, 7, 10],
         [9, 4, 1, 5]]
print(paint_tiles(costs))
