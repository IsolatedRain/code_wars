def solution(n):
    arr = [0] * (n + 1)
    x = 3
    while x < n:
        arr[x] = 1
        x += 3
    y = 5
    while y < n:
        if not arr[y]:
            arr[y] = 1
        y += 5

    return sum(i for i in range(n + 1) if arr[i])


n = 10
print(solution(n))
