def find_sum(m):
    n = len(m)
    p = [0] * (n+1)
    for row in m:
        for i, v in enumerate(row, 1):
            p[i] = v+max(p[i], p[i-1])

    return p[-1]


mtx = [[20, 20, 10, 10],
       [10, 20, 10, 10],
       [10, 20, 20, 20],
       [10, 10, 10, 20]]
print(find_sum(mtx))
