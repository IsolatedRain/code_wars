import collections


def sum_for_list(arr):
    nums = collections.Counter(arr)
    d = collections.defaultdict(int)
    n = max(max(arr), abs(min(arr))) + 1
    mark = [0] * (n + 1)
    for i in range(2, n):
        # 倍数 筛选质数的同时， 检查该倍数 是否在 数组里。
        # O(nlogn) 复杂度
        if not mark[i]:
            p = i
            j = 1
            while p * j <= n:
                mark[p * j] = 1
                if p * j in nums:
                    d[p] += p * j * nums[p * j]
                if -p * j in nums:
                    d[p] -= p * j * nums[-p * j]
                j += 1

    return [[k, v] for k, v in d.items()]


# l = [12, 15]
# l = [15, 21, 24, 30, 45]
l = [15, 21, 24, 30, -45]
print(sum_for_list(l))
