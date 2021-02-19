def exp_sum(n):
    nums = range(1,n+1)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in nums:
        for j in range(i, n+1):
            dp[j] += dp[j-i]

    return dp[-1]


print(exp_sum(5))
"""
3: 2 1
   1 1 1
   3
"""
