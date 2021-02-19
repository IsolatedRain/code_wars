import collections


def puzzle_solver(pieces, width, height):
    res = [[0] * width for _ in range(height)]
    leftTop = collections.defaultdict(int)
    left = collections.defaultdict(int)
    up = collections.defaultdict(int)
    idx2num = collections.defaultdict(tuple)

    rt = None
    rd1 = rd2 = None
    ld = None
    for (a, b), (c, d), idx in pieces:
        idx2num[idx] = (a, b, c, d)
        leftTop[(a, b, c)] = idx
        left[a, c] = idx
        up[a, b] = idx
        if a == b == c is None:
            res[0][0] = idx
            rt = b
            rd1 = rd2 = d
            ld = c

    for i in range(1, width):
        cur = left[rt, rd1]
        res[0][i] = cur
        rt, rd1 = idx2num[cur][1], idx2num[cur][3]
    for i in range(1, height):
        cur = up[ld, rd2]
        res[i][0] = cur
        ld, rd2 = idx2num[cur][2], idx2num[cur][3]
    for i in range(1, height):
        for j in range(1, width):
            a = idx2num[res[i - 1][j]][2]
            b = idx2num[res[i - 1][j]][3]
            c = idx2num[res[i][j - 1]][3]
            res[i][j] = leftTop[a, b, c]
    return list(map(tuple, res))


# pieces = [((None, 5), (None, None), 3), ((17, None), (None, None), 9), ((None, 4), (None, 5), 8),
#           ((4, 11), (5, 17), 5), ((11, None), (17, None), 2), ((None, None), (None, 4), 7),
#           ((5, 17), (None, None), 1), ((None, None), (11, None), 4), ((None, None), (4, 11), 6)]
# width = 3
# height = 3
"""
None 2  | 2  None
None 4  | 4  None
-------  -------
None 4  | 4  None
None 8  | 8  None
"""
# print(puzzle_solver([((1, 2), (3, 4), 5), ((2, 5), (4, 6), 10), ((3, 4), (7, 8), 9), ((4, 6), (8, 1), 11)], 2, 2))
# print(puzzle_solver(pieces, width, height))
print(puzzle_solver([((None, None), (None, 8), 2), ((None, 8), (None, 21), 3), ((8, None), (21, None), 1),
                     ((21, None), (None, None), 6), ((None, 21), (None, None), 5), ((None, None), (8, None), 4)], 2, 3))
