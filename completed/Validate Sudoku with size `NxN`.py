class Sudoku(object):
    def __init__(self, data):
        self.sudoku = data
        self.size = len(data)
        self.N = int(len(data) ** 0.5)
        self.validMask = 0
        self.validData = self.inputCheck()
        if self.validData:
            for i in range(1, self.size + 1):
                self.validMask |= 1 << i

    def inputCheck(self):
        for row in self.sudoku:
            for item in row:
                if not item or not str(item).isdigit():
                    return False
        return True

    def is_valid(self):
        if not self.validData: return False
        if self.linesCheck() and self.boxCheck():
            return True
        return False

    def linesCheck(self):
        for i in range(self.size):
            rowMask = 0
            colMask = 0
            for j in range(self.size):
                rowMask |= 1 << self.sudoku[i][j]
                colMask |= 1 << self.sudoku[j][i]
            if rowMask != self.validMask: return False
            if colMask != self.validMask: return False
        return True

    def boxCheck(self):
        pos = [(i, j) for i in range(0, self.size, self.N) for j in range(0, self.size, self.N)]
        for p in pos:
            x, y = p[0], p[1]
            curMask = 0
            for r in range(x, x + self.N):
                for c in range(y, y + self.N):
                    curMask |= 1 << self.sudoku[r][c]
            if curMask != self.validMask: return False
        return True


a = Sudoku([[True]])
print(a.is_valid())
