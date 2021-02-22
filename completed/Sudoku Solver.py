import time


def solve(puzzle):
    rows = [set(range(1, 10)) for _ in range(9)]
    cols = [set(range(1, 10)) for _ in range(9)]
    boxes = [set(range(1, 10)) for _ in range(9)]
    need = []
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]:
                v = puzzle[r][c]
                i = (r // 3) * 3 + c // 3
                rows[r].discard(v)
                cols[c].discard(v)
                boxes[i].discard(v)
            else:
                need.append((r, c))

    def getMin():
        nr, nc = -1, -1
        curLen = 82
        values = set()
        for r in range(9):
            for c in range(9):
                if not puzzle[r][c]:
                    boxID = (r // 3) * 3 + c // 3
                    cur = rows[r] & cols[c] & boxes[boxID]
                    if len(cur) < curLen:
                        nr, nc = r, c
                        curLen = len(cur)
                        values = cur
        return nr, nc, values

    def dfs():
        if sum(map(len, rows)) == 0:
            return True
        curR, curC, curValues = getMin()
        if curR == -1:return False
        boxID = (curR // 3) * 3 + curC // 3
        for v in curValues:
            rows[curR].discard(v)
            cols[curC].discard(v)
            boxes[boxID].discard(v)
            puzzle[curR][curC] = v
            if dfs():
                return True
            puzzle[curR][curC] = 0
            rows[curR].add(v)
            cols[curC].add(v)
            boxes[boxID].add(v)
        return False

    dfs()
    return puzzle


# p = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#      [6, 0, 0, 1, 9, 5, 0, 0, 0],
#      [0, 9, 8, 0, 0, 0, 0, 6, 0],
#      [8, 0, 0, 0, 6, 0, 0, 0, 3],
#      [4, 0, 0, 8, 0, 3, 0, 0, 1],
#      [7, 0, 0, 0, 2, 0, 0, 0, 6],
#      [0, 6, 0, 0, 0, 0, 2, 8, 0],
#      [0, 0, 0, 4, 1, 9, 0, 0, 5],
#      [0, 0, 0, 0, 8, 0, 0, 7, 9]]
# p = [[0] * 9 for _ in range(9)]
p = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
     [0, 0, 0, 4, 0, 6, 0, 0, 0],
     [0, 0, 5, 0, 7, 0, 3, 0, 0],
     [0, 6, 0, 0, 0, 0, 0, 4, 0],
     [4, 0, 1, 0, 6, 0, 5, 0, 8],
     [0, 9, 0, 0, 0, 0, 0, 2, 0],
     [0, 0, 7, 0, 3, 0, 2, 0, 0],
     [0, 0, 0, 7, 0, 5, 0, 0, 0],
     [1, 0, 0, 0, 4, 0, 0, 0, 7]]
# p[-1][-1] = 9
print(solve(p))
