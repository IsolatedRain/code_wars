import itertools
import bisect


def choose_best_sum(t, k, ls):
    if len(ls) < k: return None
    ls.sort()
    if sum(ls[:k]) > t: return None
    s = [sum(i) for i in itertools.combinations(ls, k)]
    s.sort()
    print(s)
    idx = bisect.bisect_left(s, t)
    if idx == len(s): return s[-1]
    return s[idx] if s[idx] <= t else s[idx - 1]


# print(choose_best_sum(230, 4, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]))
# print(choose_best_sum(331, 2, [73, 73, 74, 81, 85, 87, 91]))
print(choose_best_sum(230, 3, [91, 74, 73, 85, 73, 81, 87]))
