from functools import lru_cache


@lru_cache(maxsize=None)
def count_subsequences(a, b):
    if len(a) == 1: return b.count(a)
    if not a or len(a) > len(b): return 0
    curRes = 0
    for i, c in enumerate(b):
        if a[0] == b[i]:
            curRes += count_subsequences(a[1:], b[i + 1:])
    return curRes


# def count_subsequences(a, b):
#     n1, n2 = len(a), len(b)
#     dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
#     for c in range(n2 + 1):
#         dp[0][c] = 1
#     for r in range(1, n1 + 1):
#         for c in range(r, n2 + 1):
#             if a[r - 1] == b[c - 1]:
#                 dp[r][c] = dp[r - 1][c - 1] + dp[r][c - 1]
#             else:
#                 dp[r][c] = dp[r][c - 1]
#     return int(str(dp[-1][-1])[:8])


a = "happy birthday"
b = "hhaappyy bbiirrtthhddaayy"
print(count_subsequences(a, b))
