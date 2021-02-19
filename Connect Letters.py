def match(s):
    match = {'A': 'B', 'B': 'A', 'X': 'Y', 'Y': 'X'}
    n = len(s)
    dp = [[0] * n for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        t = match[s[i]]
        maxMatchID = []
        for j in range(i + 1, n):
            c = 0
            dp[i][j] = dp[i + 1][j]
            maxMatchID.append(j)
            for k in maxMatchID:
                if s[k] == t:
                    if dp[i][j] < dp[i + 1][k - 1] + dp[k + 1][j] + 1:
                        dp[i][j] = dp[i + 1][k - 1] + dp[k + 1][j] + 1
                        c = k
            if c != j:
                maxMatchID.pop()

    return dp[0][-1]


# s = "BABBYYAYAAB"
# s = "BXABAYBA"
s = "BXA"
# s = "AB"*689
print(match(s) == 3)
