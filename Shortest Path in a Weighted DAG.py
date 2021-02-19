import collections


def shortest(N, edgeList):
    edgeList.sort()
    d = [0] + [float("inf")] * (N - 1)
    for i, j, v in edgeList:
        if d[i] == float("inf") :continue
        d[j] = min(d[j], d[i] + v)

    return d[N - 1] if d[N - 1] != float("inf") else -1


# print(shortest(4, [[0, 1, 1], [0, 2, 5], [0, 3, 5], [1, 3, 3], [2, 3, 1]]))
print(shortest(5, [[0, 2, 1], [1, 2, 1], [0, 3, 1], [1, 4, 1]]))
