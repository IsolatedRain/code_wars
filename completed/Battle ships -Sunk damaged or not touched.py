import collections


def damaged_or_sunk(board, attacks):
    row, col = len(board), len(board[0])
    boatSize = collections.defaultdict(int)
    mark = collections.defaultdict(int)
    attack = []
    for x, y in attacks:
        attack.append([row - y, x - 1])

    for r in range(row):
        for c in range(col):
            if board[r][c]:
                boatSize[board[r][c]] += 1
                mark[board[r][c]] += 1

    for x, y in attack:
        if board[x][y]:
            mark[board[x][y]] -= 1

    res = {'sunk': 0, 'damaged': 0, 'not_touched': 0, 'points': 0}
    for k, v in mark.items():
        if boatSize[k] == v:
            res["not_touched"] += 1
            res["points"] -= 1
        elif v:
            res["damaged"] += 1
            res["points"] += 0.5
        else:
            res["sunk"] += 1
            res["points"] += 1

    return res


"""
format:
{ 'sunk': 0, 'damaged': 2 , 'not_touched': 1, 'points': 0 }
"""

print(damaged_or_sunk(board=[[3, 0, 1],
                             [3, 0, 1],
                             [0, 2, 1],
                             [0, 2, 0]],
                      attacks=[[2, 1], [2, 2], [3, 2], [3, 3]]))
