import collections


def count(chessBoard):
    res = collections.defaultdict(int)
    row, col = len(chessBoard), len(chessBoard[0])
    dp = [[0] * col for _ in range(row)]
    for c in range(col):
        if chessBoard[0][c]:
            dp[0][c] = 1
    for r in range(row):
        if chessBoard[r][0]:
            dp[r][0] = 1
    for r in range(1, row):
        for c in range(1, col):
            if chessBoard[r][c]:
                dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1]) + 1

    for r in range(row):
        for c in range(col):
            if dp[r][c] > 1:
                for i in range(dp[r][c], 1, -1):
                    res[i] += 1

    return res


board = [[0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 1, 1, 0, 1],
         [1, 1, 1, 1, 1]]
print(count(board))
