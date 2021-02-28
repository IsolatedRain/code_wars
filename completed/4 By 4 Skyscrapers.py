# https://www.codewars.com/kata/5671d975d81d6c1c87000022/train/python
"""
思路： 数字：每一行,  对应的处理方式一样的，
    比如 1： 行首 = size
        4： 该行 = list(rang(1, size+1))
        2:  行末 = size, 则 行首 = size - 1
            行2 不能为 size: 则 行首不能为 1
        3:  行首 ！= size - 1
    行列互斥， 与数独同。
"""


class solvePuzzle():
    def __init__(self, clues):
        self.size = len(clues) // 4
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.view = [clues[i:i + self.size] for i in range(0, len(clues), self.size)]
        self.t2D = self.view[0]  # index -> col
        self.d2T = self.view[2][::-1]  # index -> col
        self.l2R = self.view[3][::-1]  # index -> row
        self.r2L = self.view[1]  # index -> row
        self.rows = [set(range(1, self.size + 1)) for _ in range(self.size)]
        self.cols = [set(range(1, self.size + 1)) for _ in range(self.size)]
        # self.empty = []

    def initOne(self):
        for i in range(self.size):
            if self.t2D[i] == 1:
                self.grid[0][i] = self.size
            if self.d2T[i] == 1:
                self.grid[-1][i] = self.size
            if self.l2R[i] == 1:
                self.grid[i][0] = self.size
            if self.r2L[i] == 1:
                self.grid[i][-1] = self.size
        return

    def initFour(self):
        for i in range(self.size):
            if self.t2D[i] == self.size:
                v = 1
                for j in range(self.size):
                    self.grid[j][i] = v
                    v += 1

            if self.d2T[i] == self.size:
                v = self.size
                for j in range(self.size):
                    self.grid[j][i] = v
                    v -= 1

            if self.l2R[i] == self.size:
                v = 1
                for j in range(self.size):
                    self.grid[i][j] = v
                    v += 1

            if self.r2L[i] == self.size:
                v = self.size
                for j in range(self.size):
                    self.grid[i][j] = v
                    v -= 1

    def removeFilled(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c]:
                    self.rows[r].discard(self.grid[r][c])
                    self.cols[c].discard(self.grid[r][c])

    def colCheck(self, c: int):
        td = [self.grid[0][c]]
        dt = [self.grid[0][c]]
        for r in range(1, self.size):
            if self.grid[r][c] > td[-1]:
                td.append(self.grid[r][c])
            while dt and self.grid[r][c] > dt[-1]:
                dt.pop()
            dt.append(self.grid[r][c])
        if self.t2D[c]:
            if len(td) != self.t2D[c]: return False
        if self.d2T[c]:
            if len(dt) != self.d2T[c]: return False
        return True

    def rowCheck(self, r: int):
        lr = [self.grid[r][0]]
        rl = [self.grid[r][0]]
        for c in range(1, self.size):
            if self.grid[r][c] > lr[-1]:
                lr.append(self.grid[r][c])
            while rl and self.grid[r][c] > rl[-1]:
                rl.pop()
            rl.append(self.grid[r][c])
        if self.l2R[r]:
            if len(lr) != self.l2R[r]: return False
        if self.r2L[r]:
            if len(rl) != self.r2L[r]: return False
        return True

    def getMin(self):
        nr, nc = -1, -1
        curLen = 17
        values = set()
        for r in range(self.size):
            for c in range(self.size):
                if not self.grid[r][c]:
                    cur = self.rows[r] & self.cols[c]
                    if len(cur) < curLen:
                        values = cur
                        curLen = len(cur)
                        nr, nc = r, c
        return nr, nc, values

    def dfs(self, i):
        if not sum(map(len, self.rows)):
            return True
        curR, curC, values = self.getMin()
        if not values: return False
        for v in values:
            self.grid[curR][curC] = v
            self.rows[curR].remove(v)
            if not self.rows[curR]:
                if not self.rowCheck(curR):
                    self.grid[curR][curC] = 0
                    self.rows[curR].add(v)
                    return False
            self.cols[curC].remove(v)
            if not self.cols[curC]:
                if not self.colCheck(curC):
                    self.grid[curR][curC] = 0
                    self.rows[curR].add(v)
                    self.cols[curC].add(v)
                    return False
            if self.dfs(i + 1):
                return True
            self.grid[curR][curC] = 0
            self.rows[curR].add(v)
            self.cols[curC].add(v)
        return False


def solve_puzzle(clues):
    sp = solvePuzzle(clues)
    sp.initOne()
    sp.initFour()
    sp.removeFilled()
    for g in sp.grid:
        print(g)
    sp.dfs(0)
    return tuple(tuple(row) for row in sp.grid)


# clues = (2, 2, 1, 3,
#          2, 2, 3, 1,
#          1, 2, 2, 3,
#          3, 2, 1, 3)
# print(solve_puzzle(clues) ==
#       ((1, 3, 4, 2),
#        (4, 2, 1, 3),
#        (3, 4, 2, 1),
#        (2, 1, 3, 4)))
# clues = (3, 2, 2, 3, 2, 1,
#          1, 2, 3, 3, 2, 2,
#          5, 1, 2, 2, 4, 3,
#          3, 2, 1, 2, 2, 4)
clues = (0, 0, 0, 2, 2, 0,
         0, 0, 0, 6, 3, 0,
         0, 4, 0, 0, 0, 0,
         4, 4, 0, 3, 0, 0)
print(solve_puzzle(clues))
# clues = (0, 0, 1, 2,
#          0, 2, 0, 0,
#          0, 3, 0, 0,
#          0, 1, 0, 0)
# print(solve_puzzle(clues))
# r = ((2, 1, 4, 3),
#      (3, 4, 1, 2),
#      (4, 2, 3, 1),
#      (1, 3, 2, 4))
