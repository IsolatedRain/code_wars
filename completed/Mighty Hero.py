def count_of_heads(initial, n, swings):
    fac = 1
    for i in range(swings):
        initial -= 1
        fac *= (i + 1)
        initial += fac * n
    return initial


print(count_of_heads(51, 6, 31))
