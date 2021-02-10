def lcs(x, y):
    if not x or not y:
        return ""
    if x[0] == y[0]:
        return x[0] + lcs(x[1:], y[1:])
    lcs1 = lcs(x[1:], y)
    lcs2 = lcs(x, y[1:])
    return max(lcs1, lcs2)

    # n1, n2 = len(x), len(y)
    # if not n1 or not n2: return 0
    # dp = [[0] * n1 for _ in range(n2)]
    # for c in range(n1):
    #     if x[c] == y[0]:
    #         dp[0][c] = 1
    #     else:
    #         dp[0][c] = dp[0][c - 1] if c > 0 else 0
    # for r in range(n2):
    #     if x[0] == y[r]:
    #         dp[r][0] = 1
    #     else:
    #         dp[r][0] = dp[r - 1][0] if r > 0 else 0
    # for r in range(1, n2):
    #     for c in range(1, n1):
    #         if x[c] == y[r]:
    #             dp[r][c] = dp[r - 1][c - 1] + 1
    #         else:
    #             dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
    #
    # res = ""
    # r, c = n2 - 1, n1 - 1
    #
    # while r >= 0 and c >= 0:
    #     if x[c] == y[r]:
    #         res += x[c]
    #         r -= 1
    #         c -= 1
    #     else:
    #         if r > 0 and dp[r - 1][c] == dp[r][c]:
    #             r -= 1
    #         elif c > 0 and dp[r][c - 1] == dp[r][c]:
    #             c -= 1
    #
    # return res[::-1]


# x = "132535365"
# y = "123456789"
# x = "apple"
# y = "alpdple"
x = "abc"
y = "ac"
print(lcs(x, y))
