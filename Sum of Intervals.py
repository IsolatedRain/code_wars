def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: [x[0], x[1]])
    intervals.append((float("inf"), float("inf")))
    n = len(intervals)
    L, R = intervals[0][0], intervals[0][1]
    mergedIntervals = []
    res = 0
    for i in range(1, n):
        if intervals[i][0] > R:
            mergedIntervals.append([L, R])
            res += R - L
            L = intervals[i][0]
            R = intervals[i][1]
        else:
            R = max(R, intervals[i][1])

    return res


# intervals = [(1, 4), (7, 10), (3, 5)]
intervals = [(308, 324), (-235, -99), (-357, -213), (-358, -32), (-266, 111), (-402, -193), (-474, 468), (186, 266),
             (69, 389), (-37, 384)]
print(sum_of_intervals(intervals))
