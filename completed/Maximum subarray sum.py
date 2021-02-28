def max_sequence(arr):
    n = len(arr)
    maxSubSum, cur = 0, 0
    for i in range(n):
        cur += arr[i]
        if cur < 0: cur = 0
        maxSubSum = max(maxSubSum, cur)
    return maxSubSum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(arr))
