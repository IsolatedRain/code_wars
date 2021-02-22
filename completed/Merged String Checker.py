def is_merge(s, part1, part2):
    n1, n2 = len(part1), len(part2)
    if n1 + n2 != len(s): return False
    dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
    dp[0][0] = 1
    for i in range(1, n1 + 1):
        if dp[0][i - 1] and s[i - 1] == part1[i - 1]:
            dp[0][i] = 1
    for i in range(1, n2 + 1):
        if dp[i - 1][0] and s[i - 1] == part2[i - 1]:
            dp[i][0] = 1
    for r in range(1, n2 + 1):
        for c in range(1, n1 + 1):
            if (dp[r - 1][c] and part2[r - 1] == s[r + c - 1]) or (dp[r][c - 1] and part1[c - 1] == s[r + c - 1]):
                dp[r][c] = 1
    return dp[-1][-1] == 1


s = 'codewars'
p1 = 'cdw'
p2 = 'oears'
print(is_merge(s, p1, p2))
