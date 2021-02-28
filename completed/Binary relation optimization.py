# https://www.codewars.com/kata/603928e6277a4e002bb33d5a/train/python
import collections


def optimize(mtx):
    size = len(mtx)
    inDegree = collections.defaultdict(set)
    graph = collections.defaultdict(list)
    for r in range(size):
        for c in range(size):
            if mtx[r][c]:
                graph[r].append(c)
                inDegree[c].add(r)

    A, B = set(), set()
    q = []
    for i in range(size):
        if not inDegree[i]:
            q.append(i)

    while q:
        nextQ = []
        for node in q:
            A.add(node)
            for child in graph[node]:
                B.add(child)
                for x in graph[child]:
                    inDegree[x].discard(child)
        for node in range(size):
            if node not in A and node not in B and not inDegree[node]:
                nextQ.append(node)
        q = nextQ

    return sorted(A)


a = [[0, 1, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# a = [[0, 1, 1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 0],
#      [0, 0, 0, 1, 1, 1, 0, 0, 0]]
# a = [
#     [0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0]
# ]
print(optimize(a), [0, 2, 4, 7])
